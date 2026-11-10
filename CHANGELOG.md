# Changelog

Datewise log of changes to this docs repo (`docs/mintlify-docs/`). Most recent first. See `CLAUDE.md` for the required entry format. Entries before 2026-11-01 name this file `docs/CHANGELOG.md` and `CLAUDE.md` as `docs/CLAUDE.md`, their location at the time.

## 2026-11-10 — Introduction and Studio overview cover PAMP, Brand Kit, Presets, Pronunciation & Vocabulary, Doc templates; feature pages synced with the studio helpdocs

**Scope**: `introduction.mdx`, `ai-studio/overview.mdx`, `ai-studio/pamp.mdx`, `ai-studio/preset.mdx`, `ai-studio/pron-vocab.mdx`.

**Why**: the introduction did not mention Prompt a Motion Premium, Brand Kit, Presets, Pronunciation & Vocabulary or Doc templates, and the Studio overview lacked PAMP, Brand Kit and Doc templates. Comparing the feature pages with `studio/dk_ai_studio/helpdocs/` (PAMP, preset, vocabulary-pronunciation) and the web_seller UI found wrong or missing facts. Two stale helpdoc lines were fixed in the studio repo at the same time: see `studio/dk_ai_studio/changelog.md` 2026-11-10.

**What changed**:
- `introduction.mdx` — Prompt a Motion Premium added as a way to start (and premium motion-graphics videos to the Create list); new section "Set It Up Once. Stay On-Brand Everywhere." with Brand Kit, Presets, Pronunciation & Vocabulary and Doc Templates, each linking to its guide; the documents bullet names doc templates.
- `ai-studio/overview.mdx` — cards for Prompt a Motion Premium, Brand Kit and Doc templates; the prompting tip names PAMP; the Presets card names the project types it applies to; translation count 40 → 41 (the language table on `ai-studio/translate` lists 41); the docs card no longer states a count.
- `ai-studio/pron-vocab.mdx` — the applicability step names the real options (**All languages** / **This language only**; the page said "Default"), multiple rows per word, the two preview icons and the language filter; new "Good to know" section (spelling vs sound, applies to every project type and Translate, 50-entry limits, changes apply to new content only) and a mispronunciation tip.
- `ai-studio/preset.mdx` — note that presets are not available for template or prompt-generated projects; each operation is independent (a voice-over without Script enhancement, captions without a voice-over; Rule 6 as amended 2026-11-10, see `studio/dk_ai_studio/changelog.md`); closing the tab, the busy project and partial failure while applying.
- `ai-studio/pamp.mdx` — the duration choices (the style sets the video type, so "video type" was removed), up to five images, voiceover and music cannot both be off, up to three storyboard feedback rounds, closing the page while it runs, editor Feedback as a written change (the music level and track controls are hidden in the app), the first export taking a few minutes, and a note listing the editor panels a PAMP video does not offer.

## 2026-11-09 — AI Voiceover: Speed control named in the voice step

**Scope**: `ai-studio/ai-voiceover.mdx`.

**Why**: the studio now applies the chosen speed for ElevenLabs voices in every language of recorded and template projects (before, voices in 13 languages ignored it); see `studio/dk_ai_studio/changelog.md` 2026-11-09 and `studio/dk_ai_studio/plan_docs/elevenlabs-v4-plan.md`.

**What changed**: the "Select a voice" step names the **Speed** control and says it is greyed out for the few voices that only speak at their natural pace.

## 2026-11-04 — Doc templates user guide rewritten; images localized; script skips unpublished root files

**Scope**: `ai-studio/doc-temp.mdx`, new `images/ai-studio/doc-temp/` (5 images), `docs.json` (navigation entry), `scripts/localize_gcs_images.py`, `scripts/localize-gcs-images-helpdoc.md`, `scripts/gcs-image-manifest.csv`.

**Why**: the first draft of the Doc templates page (exported from the studio) covered the feature only at a high level and left out most of what users need to build a template: what a template can and cannot change, the five standard templates and when to use each, every setting in the editor, the three structure modes, the "whole script" switch, the save checks, the regeneration limit and what regenerating replaces. The fuller end-user text already existed in `studio/dk_ai_studio/helpdocs/doc-template-helpdoc.md`. The page also still linked its screenshots on GCS.

**What changed**:
- `ai-studio/doc-temp.mdx` — rewritten from the studio helpdoc in the site's style: overview with the rollout note and a "what a template does, and what it doesn't" list; a table of the five standard templates (best for / what you get) and how to View one; create-your-own as Steps with tables for About, Voice, Structure (Fixed / Guided / Topic) and Sections (heading placeholders, level, content shape, optional); the "Give the writer the whole script" section with its Steps restriction and the not-available tip; the checks the editor runs on save; tips for good templates; generating with the first-open picker; Regenerate with the two-per-project limit, the replace warning and the Product Doc fallback; copied and translated projects. Links to `/ai-studio/generate-doc` for editing the result. A duplicate Home screenshot (`_1`, identical to `_0`) and the reuse of the Product Doc screenshot in the save step were dropped.
- `images/ai-studio/doc-temp/` — the page's 5 screenshots copied from GCS by the script; links rewritten to `/images/ai-studio/doc-temp/<file>`.
- `docs.json` — `ai-studio/doc-temp` added to the AI Studio navigation after `generate-doc`.
- `scripts/localize_gcs_images.py` — new `SKIP_FILES` (`CHANGELOG.md`, `CLAUDE.md` at the repo root): both are in `.mintignore`, and the changelog's 2026-11-01 entry describes the old GCS path in prose, which made the script stop on every run once the file moved into the repo. `scripts/localize-gcs-images-helpdoc.md` — the "what the script does" line names the skipped files.
- `scripts/gcs-image-manifest.csv` — 5 rows added.

## 2026-11-01 — CLAUDE.md and CHANGELOG.md moved into the docs git repo

**Scope**: `CLAUDE.md`, `CHANGELOG.md` (moved from `docs/` into `docs/mintlify-docs/`), `.mintignore`, `scripts/localize-gcs-images-helpdoc.md`.

**Why**: both files sat outside the `mintlify-docs` git repo, so neither was versioned.

**What changed**:
- `CLAUDE.md`, `CHANGELOG.md` — moved into the repo root. Paths inside them are now repo-relative, and the structure tree shows them in the repo.
- `.mintignore` — lists both files so they are not published as site pages.
- `scripts/localize-gcs-images-helpdoc.md` — changelog references updated to the new location.
- `CLAUDE.md` — the changelog rule now names config files, scripts and `CLAUDE.md` explicitly, and requires the entry in the same commit as the change.
- Root `web-seller/CLAUDE.md` (outside this repo) — new `docs` section pointing here, and this changelog added to its list of mandatory per-service changelogs.

## 2026-11-01 — docs/CLAUDE.md corrected; helpdoc for the image script

**Scope**: `docs/CLAUDE.md`, new `mintlify-docs/scripts/localize-gcs-images-helpdoc.md`, `mintlify-docs/scripts/localize_gcs_images.py` (docstring pointer only).

**Why**: `docs/CLAUDE.md` described a layout and tooling this repo does not have (a `docs/docs/` root with `mint.json`, `seller/`/`buyer/`/`admin/`/`billing/`/`settings/`/`api/`/`assets/` folders, the old `mintlify` CLI with `build`/`deploy`, `.md` relative links). It also carried REST API documentation guidance for a site that has no API section, and a "deployment is manual" note. The localize script also needed a how-to guide.

**What changed**:
- `docs/CLAUDE.md` — repository structure rewritten to match `mintlify-docs/` (`docs.json`, real section folders, `images/`, `scripts/`, own git repo, PR flow `amit-dev` → `dev` → `main`). Config section now covers `docs.json` and `.mdx` pages, and the image rule points to the script and its helpdoc. Commands updated to the `mint` CLI (`dev --port 3333`, `broken-links`, `validate`) plus the script's `--check`. Link guidance now uses root-relative paths with no extension. Removed: the service API helpdoc table (with a broken `object-animations-helpdoc.md` path), the API-documentation section, the manual-deploy, link-checker and versioning notes, and an "update docs when an API endpoint changes" line. Added a related-docs pointer to `doc-generation-rules.md` (the source of studio-exported pages), and pointed web2vdo at `web2vdo-rules.md`.
- `scripts/localize-gcs-images-helpdoc.md` — new: requirements, commands, workflow for a new doc, what the script does, every stop message with its fix (including re-exported pages), the large-image list, and use as a CI guard. Not published (`scripts/` is in `.mintignore`).

## 2026-11-01 — Doc images moved from GCS into the repo

**Scope**: 21 `.mdx` pages (`account/billing`, `ai-hub/{host-content,insights,playlist,widget}`, `ai-studio/{brand-kit,captions,effects-2,how-objects,how-templates,intro-scene,pamp,presentation,preset,prompt-a-motion,prompt-a-studio,pron-vocab,screen-rec,seg-add-del,translate,trim-split}`), new `mintlify-docs/images/<section>/<page>/` folders, new `mintlify-docs/scripts/localize_gcs_images.py` + `scripts/gcs-image-manifest.csv`, `.mintignore`, `docs/CLAUDE.md` (image-path line). Branch `local-doc-images` of the docs repo.

**Why**: the screenshots in these pages were public GCS URLs inside the working folders of 21 studio projects (`dk-transcoder-assets/seller/{sid}/studio/{pid}/video_screenshot_file/`), so deleting or regenerating a project would silently break its doc's images. Images in the repo are served by Mintlify from its own CDN.

**What changed**:
- 263 image links (232 unique images) rewritten from GCS URLs to `/images/<page path>/<original file name>`. Only the URL inside each link changed: verified every page is byte-identical to the previous commit once the paths are mapped back, with CRLF line endings kept.
- 232 images stored exactly as downloaded (60 MB, no resizing or re-encoding: Mintlify re-encodes for delivery itself); each is byte-identical to its GCS original (sha256 in the manifest). The GCS objects were not deleted.
- `scripts/localize_gcs_images.py` — reusable for new docs exported from the studio: dry run by default, `--apply` to migrate, `--check` to fail if any GCS link remains. Stops on any GCS reference it cannot rewrite safely, and lists images over 2 MB or 2560 px for a manual decision. `scripts/` is in `.mintignore` so it is not published.
- `docs/CLAUDE.md` — the image-path guidance pointed at an `assets/` folder the site never used; now points at `images/` and the script.
- Look and feel: the pages now get Mintlify's CDN re-encode (AVIF/WebP, quality 85, responsive sizes) instead of the original JPEGs, the same as the logos and other repo images already get. Check text-heavy screenshots at full size on the deployed site.

## 2026-09-03 — Documented the new Palette/Font pickers (Prompt tab)

**Scope**: `mintlify-docs/ai-studio/prompt-a-studio.mdx`, `mintlify-docs/ai-studio/prompt-a-motion.mdx`, `mintlify-docs/ai-studio/prompt-a-video-best.mdx`. Backend/frontend companion (same date): `web_seller/changelog.md` and `studio/dk_ai_studio/changelog.md` — the feature itself, web2vdo-rules.md Rule 196.

**Why**: the Prompt tab of "Prompt a Studio" / "Prompt a Motion" shipped two new pickers (Palette and Font, next to the image upload button) so users can choose a brand look by clicking instead of typing "Brand guidelines: ..." into the prompt. Existing docs only described the type-it-in-the-prompt path.

**What changed**:
- `prompt-a-studio.mdx` — added a `<Tip>` under "Branding and Asset Specification" pointing at the new pickers, noting typed brand colors/font still win if both are used, and that leaving the pickers alone keeps the existing default look.
- `prompt-a-motion.mdx` — same `<Tip>`, added to the "Use prompt inputs" step.
- `prompt-a-video-best.mdx` — updated the pre-generation checklist table's "Brand colors and font" row and the "Prompt a Studio: Pre-Generation Tips" bullet to mention the pickers alongside the existing typing guidance (this doc is the one both other pages link to for best practices, so kept it consistent rather than leaving it describing only the older, typing-only path).

## 2026-09-01 — Language-support accuracy pass across Prompt a Video docs (incl. Norwegian enablement)

**Scope**: `mintlify-docs/ai-studio/prompt-a-video-best.mdx`, `mintlify-docs/ai-studio/prompt-a-motion.mdx`, `mintlify-docs/ai-studio/prompt-a-studio.mdx`. Backend/frontend companion: `studio/dk_ai_studio/changelog.md` and `web_seller/changelog.md` (same date) — Norwegian was actually enabled in code as part of this pass, not just documented.

**Why**: while reformatting the Language section the user had hand-edited in `prompt-a-video-best.mdx`, found the "39 languages" claim didn't match the actual code (`vibecodeMotionLanguageList()` / `dk_vibecode_language.ENABLED_LANGUAGES`), which gated 38 enabled with Norwegian, Arabic, and Urdu shown as "(coming soon)". Cross-checking surfaced the same "total 39" claim, a duplicated "Finnish" entry, and a misplaced "always available" Norwegian in the two sibling docs. Investigating the Norwegian gate (per user request) found no architectural blocker — unlike Arabic/Urdu's RTL requirement, Norwegian had every Round-1 prerequisite already (Latin script, space-separated, an ElevenLabs TTS row) and was just never carried over from the general voice/Translate list into the vibecode-specific enabled set. Per explicit user decision, the code was fixed rather than just documented as "coming soon".

**What changed**:
- `prompt-a-video-best.mdx` — reformatted the raw indented Language section into proper `<Info>`/`<Note>` Mintlify components; corrected the count and content to 39 live languages (Norwegian included) with Arabic/Urdu as the only two "coming soon"; clarified both Prompt a Studio and Prompt a Motion now share the same picker (previously implied Studio was English-locked).
- `prompt-a-motion.mdx` — fixed its `<Info>` language box to the same 39/2 split, removed a duplicate "Finnish" entry, moved Norwegian out of the plain list into a labeled "Coming soon" line (then back into the live list once Norwegian was enabled in code).
- `prompt-a-studio.mdx` — same `<Info>` box fix; also corrected a separate "34+ languages" mention in the Video Type/Duration section to the accurate count.

**Not yet done**: `prompt-a-motion-rules.md` Rule 119 and the two changelogs above carry the authoritative rule-text/code-change record for the Norwegian enablement itself — this entry covers only the customer-facing doc updates that resulted.

---

## 2026-09-01 — Prompt a Video Best Practices: new 5-type Video Type taxonomy, auto-detection, and review-checkpoint clarifications

**Scope**: `mintlify-docs/ai-studio/prompt-a-video-best.mdx`, `mintlify-docs/ai-studio/prompt-a-studio.mdx`. Backend reference updated to match: `studio/dk_ai_studio/helpdocs/web2vdo-helpdoc.md`.

**Why**: `prompt-a-video-best.mdx` §7.2 "Video Type" still described the old 3-value taxonomy (Intro/Explainer/Launch), but the shipped web2vdo feature now offers 5 types (Explainer/How-To/Educational/Announcement-Update/Comparison) with automatic detection from the prompt text as the primary mechanism — the picker is only a fallback. The doc also didn't mention that the detected type can be corrected at the Checkpoint A story-direction review, and its "Effective Feedback Examples" table didn't distinguish which examples apply at which review checkpoint.

**What changed**:
- `prompt-a-video-best.mdx` — §3 core-input-elements table, §4 skeleton template, §7.2 Video Type (full rewrite to the 5-type table + auto-detect explanation), §10 Checkpoint A description (added the type-correction dropdown mention), §10 feedback-examples table (added a note that most examples apply at Checkpoint B, not A), §13 checklist (replaced a stale "especially for Launch videos" reference).
- `prompt-a-studio.mdx` — corrected its own "intro, explainer, or launch video" mention to the current 5-type list plus the auto-detect fallback note.
- `web2vdo-helpdoc.md` — corrected the Type table's first row from "Explain / Demo" to "Explainer", matching the actual UI dropdown label.
