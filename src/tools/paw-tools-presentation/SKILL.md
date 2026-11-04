---
name: paw-tools-presentation
description: Generates McKinsey-style HTML presentations from marketing content. Use when user requests to 'create a presentation', 'generate a report', or 'build a deck' from marketing strategy or plan content.
---

# Presentation Maker

## Overview

Transforms marketing strategies, plans, and reports into polished HTML presentations using McKinsey Pyramid Principle / SCR (Situation-Complication-Resolution) structure. Act as a presentation strategist who understands both visual communication and executive-level storytelling.

**What it does:** Ingests marketing content (from paw-mkt-* skills or raw input), structures it into SCR format, generates a professional HTML document with Chart.js visualizations and hero images.

**How it works:** Three-stage progressive flow — ingest → structure → generate. Each stage completes before the next begins.

**Output:** Standalone HTML file with embedded CSS, Chart.js, and a PDF download button at `{suite-root}/presentations/`. Each presentation has unique visual character — design adapts to content type, audience, and brand signals rather than following a rigid template.

## Resolution rules

- `{skill-root}` is this skill's folder; bare paths (`references/...`, `assets/...`) resolve from it.
- `{suite-root}` is `root` from `uv run {skill-root}/scripts/paw-paths.py detect`, normally `{project-root}/paw-suites/tools`. All paths below are relative to it. A custom folder in config `tools.presentation_output_folder` wins (`detect` lists it under `overrides`; an old default is not one).
- When `detect` reports `mode: legacy` or `both`, the user's files are still partly in the old `.pawbytes/tools-output/` tree. Pass every path through `paw-paths.py locate <path>` (add `--write` for a new file) and use the path it returns. Once per session, tell the user that `paw-tools-setup` can move them to `paw-suites/tools/`, and offer it. Keep working either way.
- `{brands-folder}` is config `mkt.brands_folder`, default `{project-root}/paw-suites/marketing/brands` (the marketing suite's brand workspaces; `{project-root}/.pawbytes/marketing-suites/brands` while that suite is not migrated yet).

## On Activation

Load available config from `{project-root}/.pawbytes/config/config.yaml` and `{project-root}/.pawbytes/config/config.user.yaml` (root keys and the `tools` section). If config is present, extract:

- `communication_language` (default: English)
- `document_output_language` (default: English)

Brand context comes from the marketing suite: `{brands-folder}/{brand}/brand-context.md`, where `{brand}` is the brand the user names, else `mkt.default_brand`, else the only brand folder (ask when there are several). Use it for brand name, audience and voice, and for colors and typography when it states them. An optional `{suite-root}/brand-config.json` (`name`, `colors`, `fonts`) overrides the visual tokens when present.

**Default output path:** `{suite-root}/presentations/` (or `tools.presentation_output_folder` from config)

## Headless Mode

When invoked with `--headless` or `-H`:
- Skip user review of outline
- Use sensible defaults for all choices
- Generate complete HTML output without interaction
- Read brand config if available, otherwise use professional defaults

## Stages

### Stage 1: Ingest Content

Load `./references/01-ingest.md`

**Input sources:**
- Marketing content from paw-mkt-* skills (passed as `--from-skill <skill-name>`)
- File path to markdown/text document
- Raw text provided directly

**Progression:** Content ingested and understood → proceed to Structure

### Stage 2: Structure Outline

Load `./references/02-outline.md`

**Outcome:** McKinsey SCR/Pyramid outline presented for user review. User can edit, add, remove, or restructure sections.

**Progression:** User approves outline → proceed to Generate

### Stage 3: Generate HTML

Load `./references/03-generate.md`

**Outcome:** Complete HTML document with:
- Professional styling aligned with brand (if configured)
- Chart.js visualizations for data
- Hero/cover images (Pexels API or Gen AI)
- PDF download button via `window.print()`

## External Skills Used

- Marketing suite brand workspaces (`brand-context.md`) — brand source (optional integration)

## Output

**Location:** `{suite-root}/presentations/YYYY-MM-DD-{slugified-title}.html` (or under `tools.presentation_output_folder`).

**Filename convention:** Today's date plus the slugified title, so files sort by time. Existing presentations keep their names. After writing, run `uv run {skill-root}/scripts/paw-paths.py index` so the suite README lists it.

## Image Sources

Two options available:

1. **Pexels API** — Free stock photos. Requires `pexels_api_key` in config.
2. **fal.ai** — AI-generated images. Requires `fal_api_key` in config.

If no API keys configured, use professional placeholder or prompt user to provide images.

## Charts

Chart.js is embedded directly in HTML output. Supported types:
- Bar charts (comparisons)
- Line charts (trends over time)
- Pie/doughnut charts (proportions, market share)
- Scatter plots (correlations)

See `./references/chart-patterns.md` for implementation patterns.