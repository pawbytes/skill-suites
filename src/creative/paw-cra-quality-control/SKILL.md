---
name: paw-cra-quality-control
description: Aggregate cross-asset quality control for campaigns. Use when the user requests 'run QC', 'quality check campaign', 'review all assets', or 'generate QA report'.
---

# Quality Control

## Overview

This workflow aggregates quality control across all produced visual and video assets in a campaign, then generates a pass/fail report with revision tickets for anything that needs rework. Act as a meticulous QA lead who understands both brand standards and platform technical requirements.

**Args:** Accepts `--headless` / `-H` for autonomous execution against a campaign folder.

**Output:** `qa-report.md` with per-asset pass/fail verdicts, severity-rated issues, and revision tickets routed back to owning production workflows.

**Key distinction:** This is campaign-level cross-asset QC. Individual production workflows (Designer, Video Producer) already have embedded per-asset review gates. This workflow aggregates those results and adds cross-asset consistency checking that no single production workflow can do alone --- verifying that all campaign assets feel like a cohesive set.

## On Activation

Load available config from `{project-root}/.pawbytes/config/config.yaml` and `{project-root}/.pawbytes/config/config.user.yaml` (root level and `cra` section). If config is missing, let the user know `paw-cra-setup` can configure the module at any time. Resolve and apply throughout the session (defaults in parens):

- `{user_name}` (null) --- address the user by name
- `{communication_language}` (English) --- use for all communications
- `{document_output_language}` (English) --- use for generated document content
- `{output_directory}` (`.pawbytes/creative-suites`) --- base output path

Load shared agency memory from `{project-root}/.pawbytes/creative-suites/index.md`. Identify the active brand and campaign. Load brand guidelines from `.pawbytes/creative-suites/brands/{brand-name}/guidelines.md`.

**Campaign folder resolution:** Accept a campaign folder path as argument, or infer from the active campaign in memory. The campaign folder is expected at `.pawbytes/creative-suites/brands/{brand-name}/campaigns/{campaign-name}/` or `.pawbytes/creative-suites/campaigns/{campaign-name}/`. If no campaign can be resolved, ask the user.

If `--headless` or `-H` is passed, run the full pipeline without interaction: collect assets, run all QC checks, generate report, route results.

Otherwise, greet the user, confirm the target campaign, and proceed through the stages below. Offer a summary of what will be checked before starting.

## Stages

This workflow progresses through four stages. Each stage writes findings to the in-progress `qa-report.md` using the document-as-cache pattern for compaction survival.

| Stage | Purpose | Reference |
|-------|---------|-----------|
| 1. Asset Collection | Scan campaign folder, discover all manifests and assets | Load `./references/01-asset-collection.md` |
| 2. Per-Asset QC | Visual checks, video checks, brand compliance per asset | Load `./references/02-per-asset-qc.md` |
| 3. Cross-Asset Consistency | Verify cohesion across the full campaign asset set | Load `./references/03-cross-asset-consistency.md` |
| 4. Report & Route | Generate final report, create revision tickets, update status | Load `./references/04-report-and-route.md` |

## Severity Model

All issues use a three-tier severity:

| Severity | Meaning | Effect |
|----------|---------|--------|
| **Critical** | Asset is unusable or off-brand --- wrong dimensions, broken file, wrong logo, unreadable text | Asset fails. Revision ticket created. |
| **Warning** | Asset is usable but suboptimal --- slight color drift, audio slightly hot, missing optional metadata | Asset passes with note. Revision recommended. |
| **Info** | Observation or suggestion --- could improve but not a quality gate issue | Logged for reference. No revision ticket. |

An asset **passes** if it has zero critical issues. A campaign is **QC-approved** only when all assets pass.

## Manifest Types

Production workflows emit these manifest files. This workflow reads all of them:

| Manifest | Producer | Contains |
|----------|----------|----------|
| `design-manifest.json` | Designer workflows | Image assets, dimensions, format, brand colors used |
| `video-manifest.json` | Video Producer workflows | Video assets, codec, resolution, duration, subtitle status |
| `clip-manifest.json` | `paw-cra-video-clips` | Extracted clips with reframing and platform targets |
| `batch-manifest.json` | `paw-cra-design-batch` | Batch-produced visual assets with content calendar mapping |
