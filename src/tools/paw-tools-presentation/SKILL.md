---
name: paw-tools-presentation
description: Generates McKinsey-style HTML presentations from marketing content. Use when user requests to 'create a presentation', 'generate a report', or 'build a deck' from marketing strategy or plan content.
---

# Presentation Maker

## Overview

Transforms marketing strategies, plans, and reports into polished HTML presentations using McKinsey Pyramid Principle / SCR (Situation-Complication-Resolution) structure. Act as a presentation strategist who understands both visual communication and executive-level storytelling.

**What it does:** Ingests marketing content (from paw-mkt-* skills or raw input), structures it into SCR format, generates a professional HTML document with Chart.js visualizations and hero images.

**How it works:** Three-stage progressive flow — ingest → structure → generate. Each stage completes before the next begins.

**Output:** Standalone HTML file with embedded CSS, Chart.js, and a PDF download button at `{project-root}/.pawbytes/tools-output/presentations/`. Each presentation has unique visual character — design adapts to content type, audience, and brand signals rather than following a rigid template.

## On Activation

Load available config from `{project-root}/.pawbytes/config/config.yaml` and `{project-root}/.pawbytes/config/config.user.yaml`. If config is present, extract:

- `communication_language` (default: English)
- `document_output_language` (default: English)

Read brand config from `{project-root}/.pawbytes/tools-output/paw-mkt-setup/brand-config.json` if available — use for colors, typography, and brand voice.

**Default output path:** `{project-root}/.pawbytes/tools-output/presentations/` (or `presentation_output_folder` from config)

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

- `paw-mkt-setup` — Brand config source (optional integration)

## Output

**Location:** `{presentation_output_folder}` or `{project-root}/.pawbytes/tools-output/presentations/{slugified-title}.html`

**Filename convention:** Slugified version of the presentation title.

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