# paw-cra-quality-control

## Overview

Campaign-level quality control that aggregates cross-asset QC for all produced visual and video assets. Generates a pass/fail report with severity-rated issues and creates revision tickets for anything needing rework.

## What It Does

| Stage | Purpose |
|-------|---------|
| Asset Collection | Scan campaign folder, discover all manifests and assets |
| Per-Asset QC | Visual checks, video checks, brand compliance per asset |
| Cross-Asset Consistency | Verify cohesion across the full campaign asset set |
| Report & Route | Generate final report, create revision tickets, update status |

## When to Use It

- Running final QC before campaign delivery
- Reviewing all assets in a campaign for consistency
- Generating QA reports for client review
- Identifying assets that need rework
- Validating brand compliance across campaign

## Trigger Phrases

- "Run QC for [campaign]"
- "Quality check the campaign"
- "Review all assets"
- "Generate QA report"

## What You Get (Deliverables)

| Output | Location |
|--------|----------|
| QA report | `.pawbytes/creative-suites/brands/{brand}/campaigns/{campaign}/qa-report.md` |
| Revision tickets | Embedded in qa-report.md, routed to production workflows |

## Arguments

| Arg | Description |
|-----|-------------|
| `--headless` or `-H` | Autonomous execution against a campaign folder |

## Severity Model

| Severity | Meaning | Effect |
|----------|---------|--------|
| **Critical** | Asset unusable or off-brand (wrong dimensions, broken file, wrong logo) | Asset fails. Revision ticket created. |
| **Warning** | Asset usable but suboptimal (slight color drift, audio hot) | Asset passes with note. Revision recommended. |
| **Info** | Observation or suggestion | Logged for reference. No revision ticket. |

**Pass criteria**: An asset passes if it has zero critical issues. A campaign is QC-approved only when all assets pass.

## Manifest Types

| Manifest | Producer | Contains |
|----------|----------|----------|
| `design-manifest.json` | Designer workflows | Image assets, dimensions, format, brand colors |
| `video-manifest.json` | Video Producer workflows | Video assets, codec, resolution, duration, subtitles |
| `clip-manifest.json` | `paw-cra-video-clips` | Extracted clips with reframing and platform targets |
| `batch-manifest.json` | `paw-cra-design-batch` | Batch-produced visual assets |

## Quick Example

**Input**: "Run QC for the product-launch campaign"

**Output**: `qa-report.md` with per-asset pass/fail verdicts. 8 assets pass with no issues. 1 asset has a critical issue (wrong aspect ratio for Instagram) and fails. Revision ticket created for Designer to fix dimensions. Campaign status updated to reflect QC results.

## Per-Asset Checks

- Correct dimensions and aspect ratio
- Brand color compliance
- Typography consistency
- File integrity (no corruption)
- Platform-specific requirements

## Cross-Asset Consistency Checks

- Visual style cohesion across all assets
- Color palette consistency
- Typography hierarchy alignment
- Messaging consistency
- Platform fit verification

## Key Distinction

This is campaign-level cross-asset QC. Individual production workflows (Designer, Video Producer) have embedded per-asset review gates. This workflow aggregates those results and adds cross-asset consistency checking that no single production workflow can do alone.

## Related Skills

- [paw-cra-agent-creative-director](./paw-cra-agent-creative-director.md) -- Orchestrator
- [paw-cra-campaign-orchestration](./paw-cra-campaign-orchestration.md) -- Campaign execution
- [paw-cra-agent-designer](./paw-cra-agent-designer.md) -- Visual production
- [paw-cra-agent-video-producer](./paw-cra-agent-video-producer.md) -- Video production