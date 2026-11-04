# CLAUDE.md

This file provides guidance to Claude Code when working with the DemoKraft AI platform's user-facing documentation.

## Project Overview

**docs** holds the Mintlify-based user guide for the DemoKraft AI platform (published at `https://docs.demokraft.ai`): getting started, AI Studio, AI Hub, integrations, and account & billing. It is written for end users. API references for the backend services are not here; they live in each service's `helpdocs/` folder (e.g. `studio/dk_ai_studio/helpdocs/studio-api-doc.md`).

## Repository Structure

`docs/mintlify-docs/` is its own git repo (`github.com/demokraft/mintlify-docs`), and everything below lives in it. All paths in this file are relative to `mintlify-docs/`.

```
docs/
└── mintlify-docs/                 # Mintlify root, git repo
    ├── CLAUDE.md                  # this file (kept off the site by .mintignore)
    ├── CHANGELOG.md               # datewise log of docs changes (kept off the site by .mintignore)
    ├── docs.json                  # site config: theme, colors, logo, navbar, navigation
    ├── index.mdx, introduction.mdx
    ├── getting-started/           # Get Started group
    ├── ai-studio/                 # AI Studio group
    ├── ai-hub/                    # AI Hub group
    ├── integrations/              # Integrations group
    ├── account/                   # Account & Billing group
    ├── images/                    # site images; page images in images/<page path>/
    ├── logo/, favicon.ico, style.css
    ├── scripts/                   # repo tooling, excluded from the site by .mintignore
    └── package.json               # npm aliases for the mint CLI
```

Changes reach the live site through GitHub PRs: `amit-dev` → `dev` → `main`.

## Key Rules and Principles

### 1. Helpdocs ↔ Plan Doc Relationship

- **Plan docs** (in service repos, e.g. `web_seller/plan_docs/video_elements_zoom_rules.md`) contain the authoritative rule text and constraints for implementation.
- **Helpdocs** (in this docs repo) explain **how to use** those features from an end-user perspective.
- **Never copy rule text from plan docs into helpdocs.** Helpdocs reference the rule by number (e.g., "See video-elements Rule § 8.5") or link to the plan doc for implementer-level detail.
- Helpdocs focus on **workflow**, **UI**, and **use cases**; plan docs focus on **constraints** and **implementation**.

### 2. Changelog Discipline (Mandatory)

Every change to this docs repo — new docs, edits, images, structure changes, `docs.json` / `.mintignore` / `style.css`, scripts, and this `CLAUDE.md` — **MUST** be recorded in `CHANGELOG.md` as a new datewise entry, most-recent-first, in the same commit as the change:

```
## YYYY-MM-DD — <short title>

**Scope**: <comma-separated list of files changed or added>

**Why**: <the user gap, feature launch, or clarification that motivated it>

**What changed**:
- bullet-per-file description of what was added/removed/modified
```

One entry per change. If a docs update is driven by a backend service change, cross-reference the service's changelog entry (e.g., "See studio/dk_ai_studio/changelog.md 2026-07-02 entry").

### 3. Mintlify Configuration

- **`docs.json`** — site config and navigation. A new page must be added to `navigation` or it is not reachable from the sidebar.
- **Pages** — `.mdx` files with YAML frontmatter and Mintlify components (callouts, steps, tabs, frames).
- **Images** — store them in the repo under `images/<page path>/` and link as `/images/<page path>/<file>`; never link GCS. Pages exported from the studio come with GCS image links: run `scripts/localize_gcs_images.py` on them (how to use: `scripts/localize-gcs-images-helpdoc.md`).

## Development Commands

Run from `docs/mintlify-docs/`, with the Mintlify CLI (`npm i -g mint`):

```bash
mint dev --port 3333                                   # local preview (port 3000 is web_seller's)
mint broken-links                                      # check internal links
mint validate                                          # strict build check
python scripts/localize_gcs_images.py --check          # fail if any GCS image link remains
```

There is no test suite. Before shipping, run the checks above and look at the changed pages in the preview.

## Writing Guidelines

### Voice & Tone

- **End-user focused** — explain what the feature does and how to use it, not how it's implemented.
- **Action-oriented** — use imperative voice ("Click the Export button", not "The user may click the Export button").
- **Screenshot/video clips** — include UI screenshots and screen recordings for complex workflows.

### Structure

- **Headings** — use H2 (`##`) for top sections, H3 (`###`) for subsections. Start with a one-sentence summary of the section's purpose.
- **Callouts** — use Mintlify callouts for tips (`<Tip>`), warnings (`<Warning>`), and info (`<Info>`).
- **Code blocks** — specify the language for syntax highlighting (e.g. ` ```json `, ` ```bash `).
- **Links** — link other pages root-relative without the extension (e.g. `/ai-studio/translate`); external links use full HTTPS URLs. Mintlify generates heading anchors from the heading text (lowercase, spaces → hyphens).

## Key Related Documents

- **Document tab and Mintlify export** (where the studio-generated pages come from) — `studio/dk_ai_studio/plan_docs/doc-generation-rules.md`
- **Video elements rules** — `web_seller/plan_docs/video_elements_zoom_rules.md` (plus `plan_docs/video-elements-*-rules.md` for the split-out §8 sub-topics)
- **Object animation rules** — `studio/dk_ai_studio/plan_docs/object-implementation-rules.md`
- **Template scene rules** — `studio/dk_ai_studio/plan_docs/template-scene-rules.md`
- **Project from template** — `studio/dk_ai_studio/plan_docs/prj-with-template-plan.md` § 5
- **Web2vdo (Vibecode a Video)** — `studio/dk_ai_studio/plan_docs/web2vdo-rules.md`

## Important Notes

- **Docs are high-traffic** — they are the first stop for users. Keep them up-to-date and accurate.
- **Images must be accessible** — use descriptive alt text on all images for screen readers.

## When to Update This Repo

**Update docs when:**
- A new user-facing feature ships (add user guide)
- A bug fix changes observable behavior (update the relevant user guide)
- User feedback reveals a gap or confusing explanation

**Do NOT update docs for:**
- Internal refactoring or code cleanup (no user-visible change)
- Temporary feature flags or debug-mode behavior
- Pre-release or experimental features not yet in production

## Important Rules

See the top-level `CLAUDE.md` for the "Rules documentation policy" section. In brief:
- Each domain's rules live in exactly ONE place (the domain's plan doc, not here).
- Helpdocs reference rules by number, never restate them.
- When a rule changes, edit only the plan doc; cross-references update only if the rule number itself changed.
