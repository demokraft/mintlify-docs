# Changelog

Datewise log of changes to this docs repo (`docs/mintlify-docs/`). Most recent first. See `CLAUDE.md` for the required entry format. Entries before 2026-11-01 name this file `docs/CHANGELOG.md` and `CLAUDE.md` as `docs/CLAUDE.md`, their location at the time.

## 2026-11-16 — Choose your video type: audience beyond customers and sales

**Scope**: `ai-studio/guidance-video-type.mdx`.

**Why**: owner review: the page read as if videos were only for customers and the sales team, while teams also use them for internal training, L&D, onboarding, partners, and support. The page is now linked from the web_seller welcome modal and the Home title (see `web_seller/changelog.md` 2026-11-16 entry).

**What changed**:
- `ai-studio/guidance-video-type.mdx` — the "Use it to…" sentence in the opening now covers customers and prospects, the sales team, and employees, partners, and support teams through internal training and L&D programs.

## 2026-11-15 — Prompting best practices: language lists scoped per option

**Scope**: `ai-studio/prompt-a-video-best.mdx`.

**Why**: owner review: Prompt a Studio / Prompt a Motion and Prompt a Motion Premium support different languages, and the § 7 list was titled as if it applied to all three.

**What changed**:
- § 7 Language: opening line covers all three options; a bold line says the lists differ; the 39-language box is titled for Prompt a Studio and Prompt a Motion; the Premium note became a titled box (fewer languages, some styles fewer still, styles hidden when they don't support the language) that points to `ai-studio/pamp` for the list (single source; matches web_seller `pampStyleConfig.js`, 16 languages, none staged).

## 2026-11-15 — Brand Kit recommended for a consistent brand theme and language

**Scope**: `ai-studio/prompt-a-video-best.mdx`, `ai-studio/guidance-video-type.mdx`, `ai-studio/record-upload-best.mdx`.

**Why**: owner request: Brand Kit is the recommended way to keep brand theme, language, CTA, tagline and logo consistent without repeating them in every prompt or project.

**What changed**:
- `ai-studio/prompt-a-video-best.mdx` — § 3 Tip recommending a Brand Kit (what it stores, attach once, no repeating in each prompt); checklist puts the Brand Kit first as recommended.
- `ai-studio/guidance-video-type.mdx` — first-video tip "Set up your brand once" linking `ai-studio/brand-kit`.
- `ai-studio/record-upload-best.mdx` — "Brand it" step: select the Brand Kit in the intro and outro scenes (as in `ai-studio/intro-scene`), link added.

## 2026-11-15 — Record & Upload Tips: AI voice is optional; script enhancement needs an AI voice

**Scope**: `ai-studio/record-upload-best.mdx`.

**Why**: owner clarification: users can keep their original narration, but an original voice can't be regenerated, so script enhancement only takes effect with an AI voice.

**What changed**:
- "Speak as you go" says you can keep your own voice, or fix slips by editing the script and switching to an AI voice.
- Polish table: new step 1 "Choose your voice"; "Fix the script" and "Generate the AI voiceover" marked AI voice only; a Note for users keeping their own voice (skip those steps; an enhanced script needs an AI voice to be heard).
- Common mistakes: "Enhancing the script but keeping your own voice" added; the regenerate bullet names the AI voice.
- Checklist: voice choice item; script, product-name and voiceover items marked AI voice.

## 2026-11-15 — Presets named as one-click polish on the first-time-user pages

**Scope**: `ai-studio/guidance-video-type.mdx`, `getting-started/gettingstarted.mdx`.

**Why**: owner request: tell users who want one-click polish to use a preset (Record & Upload Tips already does).

**What changed**:
- `ai-studio/guidance-video-type.mdx` — first-video tip "Polish in one click with a preset", linking `ai-studio/preset`.
- `getting-started/gettingstarted.mdx` — the export Warning names a preset for one-click polish, linking `ai-studio/preset`.

## 2026-11-15 — Self-review: script wording, clicks split scenes, audience sentence

**Scope**: `ai-studio/guidance-video-type.mdx`, `ai-studio/record-upload-best.mdx`.

**Why**: end-of-task self-review of the day's changes.

**What changed**:
- `ai-studio/guidance-video-type.mdx` — "AI writes the script and adds the voiceover…" became "AI helps with…", because a recording's script is transcribed (a silent one starts empty) and nothing is added until applied, as Record & Upload Tips says; the audience sentence reworded; the before-and-after row names all prompt options (each offers the Comparison video type).
- `ai-studio/record-upload-best.mdx` — "Click on purpose" says clicks in an extension recording also split it into scenes (owner confirmed).

## 2026-11-15 — "What can you create?" and "Which video should I make?" kept separate and cross-linked; references to the new guides

**Scope**: `getting-started/what-content.mdx`, `ai-studio/guidance-video-type.mdx`, `introduction.mdx`, `ai-studio/overview.mdx`, `getting-started/gettingstarted.mdx`.

**Why**: the two pages overlap on "what you can make". Kept separate (owner decision): `what-content` is the ideas catalog by team, `guidance-video-type` is how to start, which option to use, and what Demokraft AI can't do. Both, and Record & Upload Tips, needed links from the pages first-time users read.

**What changed**:
- `getting-started/what-content.mdx` — Tip linking to "Which video should I make?" after the team cards.
- `ai-studio/guidance-video-type.mdx` — the Tip to "What can you create?" says what each page is for; help doc row back to recorded, uploaded, or presentation projects (owner confirmed presentation projects support docs, matching the Document tab in web_seller `Studio.js`).
- `introduction.mdx` — the What Content Tip also links "Which video should I make?".
- `ai-studio/overview.mdx` — "What you can create" links "What can you create?"; the "Upload a screen recording" card, which had no link, links Record & Upload Tips.
- `getting-started/gettingstarted.mdx` — Warning before the export step: a recording isn't polished automatically, with a link to Record & Upload Tips.

## 2026-11-15 — Video type guide: website URL start, screenshots optional, option order

**Scope**: `ai-studio/guidance-video-type.mdx`, `ai-studio/record-upload-best.mdx`.

**Why**: owner review: the intro left out starting from a website URL; prompt-based videos don't need product screenshots; products can be web apps or desktop software; preferred option order.

**What changed**:
- `ai-studio/guidance-video-type.mdx` — intro names the website URL as a starting point and covers web apps and desktop software; "built for" text no longer implies screens are required; "When to use which option" order is record, upload, presentation, Prompt a Motion Premium, Prompt a Motion, Prompt a Studio, template, with a line that the prompt options start from a URL or description and screenshots are optional; the "can't do" screenshot bullet and the first-video tip say screenshots are optional.
- `ai-studio/record-upload-best.mdx` — intro says recording works for web apps and desktop software (Chrome tab, application window, or entire screen, as in `ai-studio/screen-rec`).

## 2026-11-15 — New Record & Upload Tips guide (record-upload-best); silent videos; polish isn't automatic

**Scope**: `ai-studio/record-upload-best.mdx` (new), `ai-studio/screen-rec.mdx`, `docs.json`, `ai-studio/overview.mdx`, `ai-studio/guidance-video-type.mdx`.

**Why**: users record or upload a video and export it right away, expecting it to be polished automatically, and expect a script for silent videos. Recorded and uploaded projects had no best-practices guide (the prompt options do).

**What changed**:
- `ai-studio/record-upload-best.mdx` — new guide: "polish isn't automatic" warning (export right away = original recording); before you record (now the single home of the recording tips); what happens when the project opens (narration is transcribed, not rewritten; a silent video gets no script and every scene starts empty; an uploaded silent video is one scene, a Chrome extension recording is split at the clicks and each scene stays silent, confirmed by the owner and in `studio/dk_ai_studio/app/core/dk_video_process.py` no-voiceover branch); silent videos (check or split the scenes, write the script, enhance with AI, generate voice, or keep it silent; presets need a script); polish order (script, cut, voice, effects, brand, captions and music) with a link per step; presets as one-click polish; review and export; common mistakes; checklist. Feature details stay in each feature page.
- `ai-studio/screen-rec.mdx` — "Best Practices During Recording" bullets moved to the new guide; the section is now a pointer.
- `docs.json` — new page after the Chrome Extension page.
- `ai-studio/overview.mdx`, `ai-studio/guidance-video-type.mdx` — one-line pointers to the new guide.

## 2026-11-15 — Self-review fixes: main SaaS examples, camera clips, links to the new guides

**Scope**: `ai-studio/guidance-video-type.mdx`, `ai-studio/prompt-a-video-best.mdx`, `ai-studio/overview.mdx`, `ai-studio/pamp.mdx`.

**Why**: owner review of the two entries below: list the main SaaS examples, say where a filmed clip can go, and make the new pages reachable.

**What changed**:
- `ai-studio/guidance-video-type.mdx` — use-case table rebuilt from the owner's main examples (SaaS launch/intro/explainer, feature introductions and release announcements, walkthroughs and app demos, step-by-step demos, setup and configuration guides, dashboard demos, before-and-after comparisons, education/support/training, help doc guides, GIFs, social clips); camera footage: a clip goes in as a scene (recorded, uploaded, presentation projects) or as an image/video element (template projects); "can't show your real product screens" replaces the placeholder wording, which held only for Prompt a Studio and Prompt a Motion; Premium feedback marked paid-plan; the "plan the scenes" tip folded into the shot-list section.
- `ai-studio/prompt-a-video-best.mdx` — the § 8 Premium note no longer repeats the paid-plan feedback point (stated in § 1 and § 10).
- `ai-studio/overview.mdx` — one-line pointer to "Which video should I make?".
- `ai-studio/pamp.mdx` — Tip linking to Prompting best practices, which now covers Premium.

## 2026-11-15 — Prompting best practices covers Prompt a Motion Premium; what a prompt is

**Scope**: `ai-studio/prompt-a-video-best.mdx`.

**Why**: the page covered only Prompt a Studio and Prompt a Motion, and users write photoreal shot lists (camera, lenses, per-second timelines, exact 10-second length) instead of a product description. Premium facts checked against web_seller code (shared composer: same 40–8,000 character prompt, 5,000 character instructions, 5 images; durations 20–90 s, free 20 s) and `studio/dk_ai_studio/plan_docs/pampv3/pampv3-rules.md` (one review, Rule 35; video type detection; content built from stated facts).

**What changed**:
- Title and intro name all three prompt options.
- New "What a prompt is (and isn't)" section: a prompt is a product description with context for the video; include / leave out table (no shot lists, camera directions, photoreal requests, or picker settings typed as text).
- New "Using this guide with Prompt a Motion Premium" table: which sections apply, which differ, which don't.
- § 1 table gains a Premium column and a Format row; rule of thumb names Premium.
- § 5 note: the fact-to-scene idea applies to Premium, scene types depend on the style. § 6: points 1–5 apply to all; missing images scoped to Studio and Motion.
- § 7: Premium durations; custom lengths can't be typed; Video Type works the same in all three; Premium languages and no translation.
- § 8: Premium notes (style first, format before generating, optional voiceover, paid-plan feedback). § 10: Premium has a single review, closing the page doesn't cancel; the cancel warning scoped to Studio and Motion; after-the-build Premium bullet.
- § 11: shot-list pitfall. § 13: Premium checklist item.

## 2026-11-15 — New "Choose your video type" guide for first-time users

**Scope**: `ai-studio/guidance-video-type.mdx` (new), `docs.json`.

**Why**: users are trying Demokraft AI for ultra-realistic or reels-style videos, which it is not built for. First-time users need one short page that says what kinds of videos it makes, which creation option to start from, and what to do when they need realistic footage.

**What changed**:
- `ai-studio/guidance-video-type.mdx` — new page for first-time users: who it is for (teams at software, SaaS and technology companies: leaders, product, product marketing, sales, customer success, L&D); what Demokraft AI is built for, as a use case → best way to start table (launch/explainer/intro, walkthrough/how-to, customer education/support, training, help docs and guides, GIFs, social clips); "When to use which option" table covering all seven creation options (use-it-when + one example each) and an editable-vs-fast note; social formats (portrait and square through Prompt a Motion Premium only; every other option is landscape 16:9, checked against web_seller code); "What Demokraft AI can't do" (no realistic/cinematic footage, no avatars or presenters, no lifestyle reels, no podcasts or webinar videos (short webinar teasers or recaps stay in scope, matching `getting-started/what-content`), not a camera-footage editor, no unseen product screens, no invented facts, prompt videos up to 90 seconds, no format change later, no hands-on editing or translation of motion videos); what to do when realistic footage is needed (own clips as scenes or elements, AI Creative Service); "Write a product description, not a shot list" with a won't-work / works example pair (a fictional product, no real brand); first-video tips, including "let Demokraft AI plan the scenes" (the storyboard is planned for you and reviewed before the build). Durations, languages, plan limits and prompting advice are not repeated; the page links to `getting-started/what-content`, `ai-studio/prompt-a-video-best`, `ai-studio/pamp#video-formats` and each option's guide.
- `docs.json` — page added to the AI Studio group after the Overview.

## 2026-11-13 — Presets guide covers intro and outro scenes; Intro/Outro Scene Options page covers all 24 templates, Brand Kit, logo and fonts

**Scope**: `ai-studio/preset.mdx`, `ai-studio/intro-scene.mdx`, `introduction.mdx`, `ai-studio/overview.mdx`.

**Why**: presets gained Intro scene and Outro scene steps, a "will not be applied to this project" list before applying, and a clearer result summary (in prod 2026-11-12 and 2026-11-13), and the scenes feature grew from the classic templates to 24 templates with Brand Kit, logo, body font and script-aware fonts. Both pages still described the earlier state. Compared with `studio/dk_ai_studio/helpdocs/preset-config-helpdoc.md` and `helpdocs/studio/intro-outro-scenes-helpdoc.md`. See `studio/dk_ai_studio/changelog.md` and `web_seller/changelog.md` entries of 2026-11-11 to 2026-11-13.

**What changed**:
- `ai-studio/preset.mdx` — Intro scene and Outro scene named as steps; collapsed step cards and the Settings button; new section "Add an intro and an outro" (only what is specific to presets: the two steps, the intro title filled from the project name, scenes run first; every scene setting links to `ai-studio/intro-scene`, the single source, owner); the apply step says an existing intro or outro is replaced (an intro or outro added in the middle is left alone) and lists what will not be applied (voice-over, deleted logo, unavailable font); result summary states named; new Troubleshooting section.
- `ai-studio/intro-scene.mdx` — what scenes are; one table of all 24 templates by type (intro, chapter break, outro) with a short look note for Spotlight, Aurora, Kinetic, Frame and Mosaic (no old/new split, owner); common settings, Body Font, required fields per template, text in other languages; Brand kit and Logo sections; intro title starts as the project name; durations no longer stated as a fixed 3 seconds (the range depends on the template); "rendered once", change or remove, Presets and Translation sections; list formatting and "sceen" typo fixed.
- `introduction.mdx`, `ai-studio/overview.mdx` — the Presets text names the intro and outro scene.

**Not done**: no new screenshots. The existing images show the earlier UI (no Intro/Outro cards in the preset editor, no Spotlight / Aurora / Kinetic / Frame / Mosaic templates, Brand kit selector or Logo field); new ones are needed to match.

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
