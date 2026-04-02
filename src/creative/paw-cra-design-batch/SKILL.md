---
name: paw-cra-design-batch
description: Batch visual production workflow for campaigns. Accepts a content calendar or campaign brief, produces multiple platform-ready assets with organized bundle output and machine-readable manifest. Trigger for 'batch design', 'content calendar to assets', 'campaign batch', 'produce all campaign visuals', or 'bulk asset generation'.
---

# Batch Design Production

## Overview

Batch visual production for campaigns — transforms a content calendar or campaign brief into a complete set of platform-ready visual assets. This workflow handles multi-asset production runs: parsing the brief, building a production queue, generating each asset with brand validation, and delivering an organized bundle with a machine-readable manifest.

**Args:** Accepts `--headless` / `-H` for full autonomous batch production without interaction.

**Output:** Organized campaign asset bundle folder + `batch-manifest.json` listing every produced asset with specs.

## On Activation

Load available config from `{project-root}/.pawbytes/config/config.yaml` and `{project-root}/.pawbytes/config/config.user.yaml` (root level and `cra` section). Resolve and apply throughout the session (defaults in parens):

- `{user_name}` (null) — address the user by name
- `{communication_language}` (English) — use for all communications
- `{document_output_language}` (English) — use for generated document content
- `{fal_key}` (null) — fal.ai API key for image generation
- `{output_directory}` (`.pawbytes/creative-suites`) — base output path

Load shared agency memory from `{project-root}/.pawbytes/creative-suites/index.md`. Load active brand guidelines from `.pawbytes/creative-suites/brands/{active-brand}/guidelines.md`.

**Knowledge Base:** Check `{project-root}/.pawbytes/creative-suites/knowledge/index.md` for previously researched platform specs and design guides.

**Tool Verification:**
- fal_key availability (required — no batch production without it)
- ffmpeg availability (optional — needed only for animated carousels)
- Puppeteer/Playwright availability (optional — for template rendering)

If `--headless` or `-H` is passed, execute the full pipeline without interaction. Load `./references/autonomous-batch.md` for headless execution protocol.

Otherwise, confirm the brief/calendar with the user before beginning production.

---

## Pipeline

The batch production pipeline runs in sequential phases. Each phase completes fully before the next begins. In headless mode, all phases execute without pauses. In interactive mode, a review gate after generation allows the user to approve, revise, or reject before final bundling.

### Step 1 — Brief Intake

Load `./references/brief-intake.md`

Parse the incoming content calendar or campaign brief. Extract:
- Total number of assets required
- Per-asset specs: platform, format, dimensions, content/copy, visual direction
- Brand reference (which brand guidelines to load)
- Campaign name and any naming conventions
- Priority or ordering preferences

If the input is a content calendar, each row becomes an asset in the production queue. If the input is a campaign brief with deliverable descriptions, decompose it into individual asset specs.

**Output:** Structured asset list ready for queue building.

### Step 2 — Brand & Campaign Context Load

Load brand guidelines for the specified brand. Load any existing campaign assets from `.pawbytes/creative-suites/brands/{brand}/campaigns/{campaign}/assets/` to understand what already exists and maintain visual consistency.

If the campaign has approved copy/scripts in `.pawbytes/creative-suites/brands/{brand}/campaigns/{campaign}/scripts/`, load those for use in asset generation.

**Output:** Brand context and existing campaign context loaded into working memory.

### Step 3 — Production Queue Build

Load `./references/queue-builder.md`

Build an ordered production queue from the parsed asset list. Group assets by platform and format to enable efficient batch generation (same-platform assets can share style seeds and templates).

For each queue item, resolve:
- Platform specifications (dimensions, safe zones, format)
- Template selection (if using code-based templates)
- AI generation parameters (model, style, seed strategy)
- Text overlay requirements
- Export format and naming convention

Apply sequential naming: `{campaign}_{platform}_{type}_{NNN}.{ext}` (e.g., `summer-sale_instagram_post_001.png`).

**Output:** Ordered production queue with fully resolved specs per asset.

### Step 4 — Batch Generation Loop

Load `./references/batch-generation.md`

For each asset in the production queue:

1. **Load platform specs** — Confirm dimensions, safe zones, format requirements
2. **Generate AI imagery** — Use fal.ai with the resolved prompt and parameters. Use the Designer's AI model selection guide for model choice. Download all generated images to local paths.
3. **Apply template/text overlay** — If the asset uses a code-based template, render the HTML/CSS overlay with the generated background. If pure AI generation, apply any text overlays via image editing.
4. **Brand validate** — Check output against brand guidelines: correct colors, typography, logo placement, visual style consistency. Flag any deviations.
5. **Export with sequential naming** — Save to the campaign asset folder with the naming convention from Step 3.

Track progress: log each completed asset to a running tally. If an asset fails generation, log the failure with reason and continue to the next asset — do not halt the entire batch.

**Output:** Generated assets in the campaign folder + per-asset generation log.

### Step 5 — Bundle Organization

Organize all generated assets into a clean campaign folder structure:

```
{output_directory}/brands/{brand}/campaigns/{campaign}/assets/batch-{date}/
  instagram/
    posts/
    carousels/
    stories/
  linkedin/
    posts/
    carousels/
  tiktok/
  x-twitter/
  facebook/
  youtube/
  print/
  batch-manifest.json
```

Move or copy assets from their generation location into this organized structure. Ensure every asset has a unique, sequential filename within its platform folder.

### Step 6 — Batch Manifest

Generate `batch-manifest.json` in the bundle root. This manifest is the machine-readable record of everything produced.

Load `./references/manifest-schema.md` for the full schema.

The manifest includes:
- Campaign metadata (name, brand, date, total assets)
- Per-asset entries: filename, platform, dimensions, format, file size, generation model, generation status (success/failed/skipped), brand validation status
- Summary statistics: total produced, total failed, total skipped, platforms covered

### Step 7 — Review Gate

**Interactive mode:** Present a summary of all generated assets organized by platform. Show thumbnails or file paths. Include the count of successes, failures, and any brand validation warnings. Ask the user to approve the batch, request revisions on specific assets, or reject.

**Headless mode:** Skip this gate entirely. Log the summary to the daily activity file and proceed to status update.

### Step 8 — Status Update

Write completion status to campaign memory and daily log.

**Campaign status:** Update `.pawbytes/creative-suites/brands/{brand}/campaigns/{campaign}/status.md` with batch production results — what was produced, where it lives, any failures.

**Daily log:** Append to `.pawbytes/creative-suites/daily/{YYYY-MM-DD}.md`:

```markdown
## {HH:MM} [Designer/Batch]
**Task:** Batch production — {campaign}
**Brand:** {brand}
**Produced:** {N} assets across {M} platforms
**Failed:** {F} assets
**Location:** {bundle path}
**Manifest:** {manifest path}
```

---

## Error Handling

- **Missing fal_key:** Abort batch with clear message — cannot produce assets without generation capability
- **Individual asset failure:** Log the failure. Retry once after a 5-second delay for transient errors (HTTP 429, 500, 502, 503, 504, timeout). If the retry also fails, skip to the next asset and include in manifest as `status: "failed"` with error reason and `retried: true`.
- **Brand guidelines missing:** Warn and proceed with best-effort generation; flag all assets as `brand_validated: false` in manifest
- **Template rendering failure:** Fall back to pure AI generation for that asset; note the fallback in manifest

## Platform Specs Quick Reference

Reference `./references/platform-specs-quick.md` for the condensed dimension lookup table used during queue building. For full specifications, reference the Designer's `platform-specifications.md`.

## AI Model Selection

Use the Designer agent's model selection guide. For batch production, prefer:
- **Nano Banana Pro** — Best for marketing posts with typography
- **FLUX.2 [flex]** — Balanced quality/speed for bulk generation
- **FLUX.1 [schnell]** — Use for rapid prototyping or very large batches where speed matters more than premium quality
