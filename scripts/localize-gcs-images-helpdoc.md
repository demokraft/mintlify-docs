# Localize GCS images: how to use `localize_gcs_images.py`

Docs exported from the studio (Document tab → Mintlify export) link their screenshots to public GCS URLs inside a studio project's working folder. If that project is deleted or regenerated, the images on the docs site break. This script copies those images into the docs repo and points the page at the copies, so Mintlify serves them from its own CDN.

Run it every time you add or replace a page that came from a studio export.

## Requirements

- Python 3.8 or newer. Only the standard library is used, so there is nothing to install.
- Internet access to `storage.googleapis.com`.
- Run it inside the docs git repo (`docs/mintlify-docs`), on a clean working tree, so `git diff` shows exactly what it changed.

## Commands

Run these from `docs/mintlify-docs` (the script finds the repo root on its own, so any folder works):

| Command | What it does | Changes files? |
|---|---|---|
| `python scripts/localize_gcs_images.py` | Dry run: lists every page with GCS image links and how many | No |
| `python scripts/localize_gcs_images.py --apply` | Downloads the images and rewrites the links | Yes |
| `python scripts/localize_gcs_images.py --check` | Exits 1 if any GCS reference remains, 0 if none. Use before a commit or in CI | No |

## Usual workflow for a new doc

1. Add the exported `.mdx` page to the repo (and to the `docs.json` navigation) as usual.
2. Dry run, and check that the pages and link counts it lists are the ones you expect:
   ```bash
   python scripts/localize_gcs_images.py
   ```
3. Apply:
   ```bash
   python scripts/localize_gcs_images.py --apply
   ```
4. Review and verify:
   ```bash
   git status                 # new images/<page path>/ folder, changed .mdx, updated manifest
   git diff -- '*.mdx'        # only image URLs should differ
   python scripts/localize_gcs_images.py --check
   mint broken-links
   ```
5. Preview with `mint dev --port 3333` (web_seller uses port 3000) and look at the page.
6. Commit the page, its `images/<page path>/` folder and `scripts/gcs-image-manifest.csv` together. Add an entry to `CHANGELOG.md`.

## What the script does

- **Finds** GCS image links in every text file in the repo (skipping `.git`, `node_modules`, `scripts/` and `images/`). Two link forms are rewritten:
  - `<img src="URL" ... />` (single or double quotes)
  - `![alt](URL)`
- **Downloads** each image once into `images/<page path>/<original file name>`. For example, `ai-studio/captions.mdx` gets `images/ai-studio/captions/frame_3.jpg`. Giving each page its own folder matters because studio file names (`frame_0.jpg`, …) repeat across projects.
- **Stores the image exactly as downloaded.** It never resizes or re-encodes. Mintlify re-encodes images for delivery (AVIF/WebP, quality 85, sized to the reader's screen), so compressing first would not help readers and could blur small UI text.
- **Rewrites only the URL** inside each link to `/images/<page path>/<file>`. It edits the raw bytes, so the alt text, markup and line endings stay as they were. Before writing a page, it checks that mapping the new paths back gives the original file exactly.
- **Records** each image in `scripts/gcs-image-manifest.csv`: page, old URL, line numbers, new path, sha256, size and width. Later runs add to this file and keep the older rows.
- **Leaves the GCS files alone.** Nothing is deleted from GCS.

The script is safe to run again. Pages that no longer have GCS links are not touched.

## When the script stops

It stops rather than skip anything. Problems found while scanning stop it before anything changes (exit code 2). A stop during `--apply` can leave earlier pages already done. Each written page is complete, so fix the cause and run it again: done pages are skipped.

| Message | Cause | What to do |
|---|---|---|
| `GCS reference in a link form this script does not handle` | A GCS URL outside the two supported forms: a bare URL, an `href`, frontmatter, etc. | Change that line by hand: download the image into `images/<page path>/`, link it as `/images/<page path>/<file>`, then re-run. |
| `GCS link is not an image` | A GCS link to a video, PDF or similar | Decide by hand whether it belongs in the repo. The script only handles `.jpg .jpeg .png .gif .webp .svg`. |
| `GCS reference in a non-doc file` | A GCS URL in `docs.json`, CSS, etc. | Update that file by hand. |
| `HTTP …` or `content-type … does not match` | The image is gone from GCS, or the URL is wrong | Get the image again from the studio project (or re-export the doc), then re-run. |
| `… already exists with different content` | The page's image folder already has a file with that name but different bytes. This is typical when a page is **re-exported** from the studio. | If the whole page is being replaced, delete `images/<page path>/` (only that page uses it) and re-run. Otherwise rename or remove the old file by hand. |
| `Two images map to …` | Two different URLs on one page have the same file name | Rename one image by hand and update its link. |

## Large images

At the end of `--apply`, the script lists any image over **2 MB** or wider than **2560 px**. It doesn't change them. Screenshots from the studio are normally 1920 px and under 0.6 MB, so they won't appear. If one does show up, consider resizing it to about twice the width it's shown at before committing. That keeps the repo small without visible loss.

## Using it as a guard

`--check` prints each remaining GCS reference and exits 1, or exits 0 when there are none, so it can run in CI or a pre-commit hook:

```bash
python scripts/localize_gcs_images.py --check || exit 1
```

## Notes

- `scripts/` is listed in `.mintignore`, so the script, this guide and the manifest are not published on the docs site.
- First run (2026-11-01): 21 pages, 263 links, 232 images. See `CHANGELOG.md`.
