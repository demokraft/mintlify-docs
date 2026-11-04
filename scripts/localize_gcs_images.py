#!/usr/bin/env python3
"""Copy GCS-hosted doc images into this repo and point the docs at the copies.

Docs exported from the DemoKraft studio (Document tab -> Mintlify export) embed
screenshots as public GCS URLs that live inside a studio project's working
folder. If that project is deleted or regenerated, the doc loses its images.
This script removes that dependency: every GCS image used by a page is
downloaded once into images/<page path>/<file name>, and the page's link is
rewritten to the local /images/... path. Mintlify then serves the image from
its own CDN.

What the script guarantees:
- Only the URL inside a link changes. Files are edited as raw bytes, so alt
  text, markup, line endings and all other content stay byte-for-byte the same.
- Images are stored exactly as downloaded (no resizing or re-encoding).
  Mintlify re-encodes images for delivery itself, so pre-compressing would not
  help readers and could degrade small UI text.
- Nothing is missed silently: any GCS reference the script cannot rewrite
  (an unknown link form, a non-image file, a non-doc file) stops the run.

Usage (from the repo root or anywhere):
    python scripts/localize_gcs_images.py            # dry run: report only
    python scripts/localize_gcs_images.py --apply    # download + rewrite
    python scripts/localize_gcs_images.py --check    # exit 1 if any GCS reference remains

The run is idempotent: pages already migrated have no GCS references and are
skipped, so it is safe to run on the whole repo after adding new docs.
Every migrated image is recorded in scripts/gcs-image-manifest.csv.
Full guide (workflow, error messages and fixes): scripts/localize-gcs-images-helpdoc.md
"""

import argparse
import concurrent.futures
import csv
import hashlib
import os
import re
import struct
import sys
import tempfile
import urllib.parse
import urllib.request

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
IMAGES_DIR = "images"
MANIFEST = os.path.join(REPO_ROOT, "scripts", "gcs-image-manifest.csv")

# Directories never scanned: tooling, dependencies, and the image store itself.
# scripts/ is skipped because the manifest there deliberately lists the old URLs.
SKIP_DIRS = {".git", "node_modules", "scripts", IMAGES_DIR}
# Repo-root files never scanned: both are in .mintignore (never published), and
# the changelog legitimately describes old GCS paths in prose.
SKIP_FILES = {"CHANGELOG.md", "CLAUDE.md"}
BINARY_EXTS = {".png", ".jpg", ".jpeg", ".gif", ".webp", ".avif", ".svg", ".ico",
               ".mp4", ".webm", ".mov", ".pdf", ".woff", ".woff2", ".ttf", ".otf", ".zip"}
DOC_EXTS = {".mdx", ".md"}

# Any of these in a scanned file counts as a GCS reference that must be handled.
GCS_MARKERS = re.compile(
    rb"storage\.googleapis\.com|storage\.cloud\.google\.com|gs://|dk-transcoder-assets",
    re.IGNORECASE,
)
# The link forms the script can rewrite. The closing delimiter is part of the
# match so a URL is only replaced where it ends, never as part of a longer URL.
GCS_URL = rb"https?://(?:[a-z0-9.-]+\.)?storage\.googleapis\.com/[^\s\"')<>]+"
LINK_FORMS = [
    re.compile(rb'(src=")(' + GCS_URL + rb')(")', re.IGNORECASE),   # <img src="URL" />
    re.compile(rb"(src=')(" + GCS_URL + rb")(')", re.IGNORECASE),   # <img src='URL' />
    re.compile(rb"(\]\()(" + GCS_URL + rb")(\))", re.IGNORECASE),   # ![alt](URL)
]
CONTENT_TYPES = {
    ".jpg": "image/jpeg", ".jpeg": "image/jpeg", ".png": "image/png",
    ".gif": "image/gif", ".webp": "image/webp", ".svg": "image/svg+xml",
}
# Images above either limit are listed for a manual decision (e.g. resize to
# about 2x the displayed width); the script never shrinks anything itself.
WARN_BYTES = 2 * 1024 * 1024
WARN_WIDTH = 2560


def scan_files():
    """Yield (relative path, bytes) for every text file that may hold links."""
    for root, dirs, files in os.walk(REPO_ROOT):
        dirs[:] = [d for d in dirs if d not in SKIP_DIRS]
        for name in files:
            if os.path.splitext(name)[1].lower() in BINARY_EXTS:
                continue
            if root == REPO_ROOT and name in SKIP_FILES:
                continue
            path = os.path.join(root, name)
            with open(path, "rb") as f:
                yield os.path.relpath(path, REPO_ROOT).replace(os.sep, "/"), f.read()


def find_references(rel, data):
    """Return the rewritable GCS image links in a file, plus any problems.

    Every GCS marker in the file must sit inside a rewritable link; otherwise
    the file has a reference this script would miss, which is reported.
    """
    problems = []
    markers = [m.start() for m in GCS_MARKERS.finditer(data)]
    if not markers:
        return [], problems
    if os.path.splitext(rel)[1].lower() not in DOC_EXTS:
        return [], [f"{rel}: GCS reference in a non-doc file; update it by hand"]

    refs, covered = [], []
    for form in LINK_FORMS:
        for m in form.finditer(data):
            url = m.group(2).decode("ascii")
            ext = os.path.splitext(urllib.parse.urlsplit(url).path)[1].lower()
            line = data.count(b"\n", 0, m.start()) + 1
            if ext not in CONTENT_TYPES:
                problems.append(f"{rel}:{line}: GCS link is not an image ({url})")
                continue
            refs.append({"url": url, "line": line})
            covered.append((m.start(2), m.end(2)))
    for pos in markers:
        if not any(a <= pos < b for a, b in covered):
            line = data.count(b"\n", 0, pos) + 1
            problems.append(f"{rel}:{line}: GCS reference in a link form this script does not handle")
    return refs, problems


def local_paths(doc_rel, url):
    """Map a GCS URL used by a doc to (file path on disk, path used in the doc).

    Images go to images/<doc path without extension>/<original file name>, so
    each page's images sit together and identical names from different studio
    projects (frame_0.jpg, ...) cannot collide.
    """
    name = urllib.parse.unquote(os.path.basename(urllib.parse.urlsplit(url).path))
    folder = os.path.splitext(doc_rel)[0]
    disk = os.path.join(REPO_ROOT, IMAGES_DIR, *folder.split("/"), name)
    # Percent-encode only what a link cannot hold (e.g. spaces); for the usual
    # frame_N.jpg names this is the plain path.
    link = "/" + urllib.parse.quote(f"{IMAGES_DIR}/{folder}/{name}", safe="/")
    return disk, link


def image_width(data):
    """Pixel width of a PNG or JPEG from its header, or None if unknown."""
    if data[:8] == b"\x89PNG\r\n\x1a\n":
        return struct.unpack(">I", data[16:20])[0]
    if data[:2] == b"\xff\xd8":
        i = 2
        while i + 9 < len(data):
            if data[i] != 0xFF:
                i += 1
                continue
            marker = data[i + 1]
            if marker in (0xC0, 0xC1, 0xC2, 0xC3, 0xC5, 0xC6, 0xC7, 0xC9, 0xCA, 0xCB, 0xCD, 0xCE, 0xCF):
                return struct.unpack(">H", data[i + 7:i + 9])[0]
            i += 2 + struct.unpack(">H", data[i + 2:i + 4])[0]
    return None


def download(url):
    """Fetch an image, refusing anything that is not a 200 with the right type."""
    with urllib.request.urlopen(url, timeout=60) as resp:
        if resp.status != 200:
            raise RuntimeError(f"HTTP {resp.status} for {url}")
        ctype = resp.headers.get("Content-Type", "").split(";")[0].strip().lower()
        data = resp.read()
    ext = os.path.splitext(urllib.parse.urlsplit(url).path)[1].lower()
    if ctype != CONTENT_TYPES[ext]:
        raise RuntimeError(f"content-type {ctype!r} does not match {ext} for {url}")
    return data


def write_manifest(rows):
    """Merge rows into the manifest, keyed by (doc, url), keeping older entries."""
    fields = ["doc", "url", "lines", "local_path", "sha256", "bytes", "width"]
    existing = {}
    if os.path.exists(MANIFEST):
        with open(MANIFEST, newline="", encoding="utf-8") as f:
            for r in csv.DictReader(f):
                existing[(r["doc"], r["url"])] = r
    for r in rows:
        existing[(r["doc"], r["url"])] = r
    with open(MANIFEST, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=fields)
        w.writeheader()
        for key in sorted(existing):
            w.writerow(existing[key])


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    mode = ap.add_mutually_exclusive_group()
    mode.add_argument("--apply", action="store_true", help="download images and rewrite the docs")
    mode.add_argument("--check", action="store_true", help="exit 1 if any GCS reference remains")
    args = ap.parse_args()

    docs, problems = {}, []
    for rel, data in scan_files():
        refs, probs = find_references(rel, data)
        problems += probs
        if refs:
            docs[rel] = (data, refs)

    total_refs = sum(len(refs) for _, refs in docs.values())
    unique = {(rel, r["url"]) for rel, (_, refs) in docs.items() for r in refs}

    if args.check:
        for p in problems:
            print("PROBLEM:", p)
        for rel, (_, refs) in sorted(docs.items()):
            print(f"GCS: {rel}: {len(refs)} image link(s)")
        sys.exit(1 if (docs or problems) else 0)

    print(f"{len(docs)} doc(s), {total_refs} GCS image link(s), {len(unique)} unique image(s) per doc")
    for rel, (_, refs) in sorted(docs.items()):
        print(f"  {rel}: {len(refs)} link(s)")
    if problems:
        print("\nStopping: these references cannot be migrated automatically:")
        for p in problems:
            print("  " + p)
        sys.exit(2)
    if not docs:
        print("Nothing to do.")
        return
    if not args.apply:
        print("\nDry run. Re-run with --apply to download and rewrite.")
        return

    # Plan every target first, so collisions stop the run before any change.
    targets = {}
    for rel, url in sorted(unique):
        disk, link = local_paths(rel, url)
        clash = [k for k, v in targets.items() if v[0].lower() == disk.lower() and k != (rel, url)]
        if clash:
            sys.exit(f"Two images map to {disk}: {url} and {clash[0][1]}")
        targets[(rel, url)] = (disk, link)

    urls = sorted({url for _, url in unique})
    print(f"\nDownloading {len(urls)} image(s)...")
    with concurrent.futures.ThreadPoolExecutor(8) as pool:
        fetched = dict(zip(urls, pool.map(download, urls)))

    # Store images. An existing file is reused only if its bytes are identical.
    rows, warnings = [], []
    for (rel, url), (disk, link) in sorted(targets.items()):
        data = fetched[url]
        if os.path.exists(disk):
            with open(disk, "rb") as f:
                if f.read() != data:
                    sys.exit(f"{disk} already exists with different content; resolve it by hand")
        else:
            os.makedirs(os.path.dirname(disk), exist_ok=True)
            fd, tmp = tempfile.mkstemp(dir=os.path.dirname(disk))
            with os.fdopen(fd, "wb") as f:
                f.write(data)
            os.replace(tmp, disk)
        width = image_width(data)
        if len(data) > WARN_BYTES or (width or 0) > WARN_WIDTH:
            warnings.append(f"{disk}: {len(data) // 1024} KB, {width}px wide")
        lines = ";".join(str(r["line"]) for r in docs[rel][1] if r["url"] == url)
        rows.append({"doc": rel, "url": url, "lines": lines,
                     "local_path": link, "sha256": hashlib.sha256(data).hexdigest(),
                     "bytes": len(data), "width": width or ""})

    # Rewrite each doc, then prove only the URLs changed before writing it.
    for rel, (data, refs) in sorted(docs.items()):
        mapping = {r["url"].encode(): targets[(rel, r["url"])][1].encode() for r in refs}
        new = data
        for form in LINK_FORMS:
            new = form.sub(lambda m: m.group(1) + mapping[m.group(2)] + m.group(3), new)
        restored = new
        for old_url, link in mapping.items():
            restored = restored.replace(link, old_url)
        if restored != data:
            sys.exit(f"{rel}: rewrite would change more than the image URLs; nothing written for it")
        if GCS_MARKERS.search(new):
            sys.exit(f"{rel}: GCS reference still present after rewrite")
        with open(os.path.join(REPO_ROOT, rel), "wb") as f:
            f.write(new)

    write_manifest(rows)

    # Every local path written into a doc must exist with the exact case
    # (Mintlify builds on Linux, which is case-sensitive).
    for (rel, url), (disk, _) in targets.items():
        folder, name = os.path.split(disk)
        if name not in os.listdir(folder):
            sys.exit(f"{disk} missing (or case differs) for {rel}")

    print(f"Done: {len(docs)} doc(s), {total_refs} link(s) rewritten, {len(targets)} image(s) stored.")
    print(f"Manifest: {os.path.relpath(MANIFEST, REPO_ROOT)}")
    if warnings:
        print("\nLarge images (consider resizing to ~2x displayed width before committing):")
        for w in warnings:
            print("  " + w)


if __name__ == "__main__":
    main()
