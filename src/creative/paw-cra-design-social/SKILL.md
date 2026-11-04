---
name: paw-cra-design-social
description: Social post and carousel production pipeline. Use when the user requests to 'create social post', 'design carousel', or 'run social design workflow'.
---

# Social Design Workflow

## Overview

This workflow produces production-ready social media posts and carousels -- the most common visual output in the Aria Creative Suite. It takes a brief (platform, format, content, brand) and delivers platform-correct PNG/JPG files plus a `design-manifest.json`.

**Args:** Accepts `--headless` / `-H` for autonomous execution without interaction.

**Output:** Visual assets at exact platform dimensions saved to the campaign's `designs/social/` (or `{suite-root}/brands/{brand}/designs/social/{YYYY-MM-DD}/` outside a campaign) plus `design-manifest.json`.

Act as a visual production pipeline operator. This workflow is production-first -- it produces images, not documents. Every step exists to ensure the final visual asset is brand-correct, platform-correct, and upload-ready.

**Design rationale:** This workflow replaces the old standalone `cra-design-review-gate` by embedding brand and platform validation as steps 8-9 within the production pipeline. Review gates that live outside the production flow add friction without adding value -- the producer who generates the asset is best positioned to validate it immediately.

## On Activation

Load available config from `{project-root}/.pawbytes/config/config.yaml` and `{project-root}/.pawbytes/config/config.user.yaml` (root level and `cra` section). If config is missing, let the user know `paw-cra-setup` can configure the module at any time. Resolve and apply throughout (defaults in parens):

- `{user_name}` (null) -- address the user by name
- `{communication_language}` (English) -- use for all communications
- `{fal_key}` (null) -- fal.ai API key for image generation (required)
- `{suite-root}` is `root` from `uv run {skill-root}/scripts/paw-paths.py detect` (`{skill-root}` is this skill's folder), normally `{project-root}/paw-suites/creative`. Every `{suite-root}/...` path below is relative to it. A custom folder in config `cra.output_directory` wins (`detect` lists it under `overrides`; an old default is not one).
- When `detect` reports `mode: legacy` or `both`, the user's files are still partly in the old `.pawbytes/creative-suites/` tree. Pass every path through `paw-paths.py locate <path>` (add `--write` for a new file) and use the path it returns. Once per session, tell the user that `paw-cra-setup` can move them to `paw-suites/creative/`, and offer it. Keep working either way.

Load shared agency memory from `{suite-root}/_memory/index.md` to understand active brands and campaigns. Load brand guidelines from `{suite-root}/brands/{brand}/guidelines.md` once the brand is identified.

Check `{suite-root}/_memory/knowledge/index.md` for previously researched platform specs and design knowledge.

**Tool verification:** Confirm `fal_key` is available before proceeding. Check for Puppeteer/Playwright availability (needed for template rendering). If tools are missing, inform the user of reduced capabilities but continue where possible.

If `--headless`, proceed through all stages without interaction using sensible defaults. Otherwise, confirm the brief with the user before production begins.

## Pipeline

The workflow has three stages. Each loads its reference on entry.

### Stage 1: Brief & Context

Load `./references/01-brief-and-context.md`

Parse and validate the incoming brief. Load platform specifications and best practices. Resolve copy -- either from the brief or by invoking the Strategist. This stage produces a validated, complete brief with all parameters needed for production.

**Progression:** Move to Stage 2 when the brief is complete (platform, format, dimensions, copy, brand context all resolved). In headless mode, infer missing parameters from context and proceed.

### Stage 2: Production

Load `./references/02-production.md`

Plan the visual layout, generate AI imagery, and render text overlays. For carousels, maintain visual consistency across all slides. This stage produces the raw visual assets.

**Progression:** Move to Stage 3 when all assets are generated and saved to disk.

### Stage 3: Validation & Export

Load `./references/03-validation-and-export.md`

Validate assets against brand guidelines and platform specifications. Export to the correct location with proper naming. Write the design manifest and update status logs. This stage produces the final deliverables.

**Progression:** Workflow complete when `design-manifest.json` is written and daily log is updated.

---

## Quick Reference

### Supported Platforms

| Platform | Post | Carousel | Story |
|----------|------|----------|-------|
| Instagram | 1080x1350 (4:5) | 1080x1080 or 1080x1350 | 1080x1920 |
| LinkedIn | 1200x627 | 1080x1080 (PDF) | 1080x1920 |
| TikTok | 1080x1920 | -- | 1080x1920 |
| X (Twitter) | 1200x675 | -- | -- |
| Facebook | 1200x630 | 1080x1080 | 1080x1920 |

### AI Model Selection

| Use Case | Primary Model | Fallback |
|----------|--------------|----------|
| Text-heavy posts | Nano Banana Pro | FLUX.2 [flex] |
| Photo-realistic | FLUX.2 [pro] | FLUX.2 [flex] |
| Rapid prototyping | FLUX.1 [schnell] | -- |
| Carousel consistency | FLUX.2 [flex] | Nano Banana Pro |

### Output Structure

```
{suite-root}/brands/{brand}/campaigns/{campaign}/designs/social/
  {platform}_{format}_{date}.png
  {platform}_{format}_{date}_slide01.png  (carousel)
  {platform}_{format}_{date}_slide02.png  (carousel)
  design-manifest.json
```
