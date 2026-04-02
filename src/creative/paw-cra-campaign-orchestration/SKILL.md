---
name: paw-cra-campaign-orchestration
description: Orchestrates multi-deliverable campaigns by dispatching Designer and Video Producer workflows in parallel. Use when the user requests 'run campaign', 'execute campaign', 'launch campaign production', or 'orchestrate deliverables'.
---

# Campaign Orchestration

## Overview

This workflow is the **central orchestration engine** for the Aria Creative Suite. It takes a campaign brief containing multiple deliverables (social posts, carousels, videos, brand assets), parses them into production tasks, dispatches Designer and Video Producer workflows **in parallel**, tracks progress, aggregates results, and runs quality control across all produced assets.

**Args:** Supports `--headless` / `-H` for fully autonomous campaign execution without user interaction. Supports `--template:product-launch` for the product launch campaign variant (merged from `cra-product-launch-campaign`).

**Inputs:** Campaign brief (with deliverable list), brand guidelines, optional content calendar or strategy artifacts from Strategist.

**Outputs:** `status.md` (campaign progress tracker), specialist assignments, `design-manifest.json` and `video-manifest.json` from production workflows, `qa-report.md` from quality control, campaign completion report, daily log entries.

Act as a campaign production manager who coordinates parallel workstreams. You understand creative production timelines, dependency analysis, and how to keep multiple production tracks synchronized. Your job is coordination and progress tracking, not creative judgment — that belongs to the production agents.

**Architectural context:** Designer and Video Producer are primary production agents that take briefs directly. Strategist is a service agent — only invoke Strategist if a deliverable explicitly requires research, copy, or script writing that hasn't been provided. Never gate production on Strategist by default.

## On Activation

Load available config from `{project-root}/.pawbytes/config/config.yaml` and `{project-root}/.pawbytes/config/config.user.yaml` (root level and `cra` section). If config is missing, let the user know `paw-cra-setup` can configure the module at any time. Resolve:

- `{user_name}` (null) — address the user by name
- `{communication_language}` (English) — use for all communications
- `{document_output_language}` (English) — use for generated document content
- `{fal_key}` — fal.ai API key (needed by production agents)
- `{elevenlabs_api_key}` — ElevenLabs API key (optional, for video)
- `{output_directory}` (`.pawbytes/creative-suites`) — base output path

Load shared agency memory from `{project-root}/.pawbytes/creative-suites/index.md`. Load brand guidelines from `{project-root}/.pawbytes/creative-suites/brands/{brand-name}/guidelines.md`.

Locate the campaign brief. Expected at `{project-root}/.pawbytes/creative-suites/brands/{brand-name}/campaigns/{campaign-name}/brief.md`. If not found, check if the user provided one inline or as a file path.

If `--headless`, execute all stages without interaction using the brief as-is. If `--template:product-launch`, load `./references/template-product-launch.md` for the variant pipeline.

Otherwise, confirm the brief is loaded and present a summary of detected deliverables before proceeding.

## Campaign Status File (Compaction Survival)

All progress is written to `{project-root}/.pawbytes/creative-suites/brands/{brand-name}/campaigns/{campaign-name}/status.md`. This file is both the output artifact and the recovery cache. Each stage updates it. After compaction, re-read this file plus the brief to recover full context.

```yaml
---
campaign: '{campaign-name}'
brand: '{brand-name}'
status: 'in-progress'  # pending | in-progress | quality-gate | complete | failed
current_stage: '01-brief-parsing'
brief_path: './brief.md'
created: 'ISO-8601'
updated: 'ISO-8601'
deliverables_total: 0
deliverables_complete: 0
design_track: 'pending'
video_track: 'pending'
qc_status: 'pending'
---
```

## Stages

| Stage | Purpose | Reference |
|-------|---------|-----------|
| 01 | Brief Parsing | Load `./references/01-brief-parsing.md` |
| 02 | Dependency Analysis & Queue Build | Load `./references/02-dependency-queue.md` |
| 03 | Parallel Dispatch | Load `./references/03-parallel-dispatch.md` |
| 04 | Progress Tracking & Collection | Load `./references/04-progress-collection.md` |
| 05 | Quality Gate & Completion | Load `./references/05-quality-completion.md` |

**Progression:** Each stage updates `status.md` with its results before loading the next stage. If interrupted, resume from the last completed stage by reading `status.md`.

## External Skills & Workflows

| Skill/Workflow | When Invoked | Purpose |
|----------------|--------------|---------|
| `paw-cra-agent-designer` | Stage 03 | Dispatch design production (via Agent tool) |
| `paw-cra-agent-video-producer` | Stage 03 | Dispatch video production (via Agent tool) |
| `paw-cra-agent-strategist` | Stage 02 (conditional) | Only if deliverables require unresolved copy/scripts/research |
| `paw-cra-quality-control` | Stage 05 | Aggregate QC across all produced assets |
| `paw-cra-multi-platform-export` | Stage 05 (conditional) | Suggested if platform variants are needed post-QC |

**Invocation pattern:** Use the Agent tool with the skill name in the prompt. For parallel dispatch in Stage 03, launch Designer and Video Producer agent groups simultaneously.

## Memory Contract

**Reads:**
- `{project-root}/.pawbytes/creative-suites/index.md` — agency state
- `{project-root}/.pawbytes/creative-suites/brands/{brand-name}/guidelines.md` — brand identity
- `{project-root}/.pawbytes/creative-suites/brands/{brand-name}/campaigns/{campaign-name}/brief.md` — campaign brief

**Writes:**
- `{project-root}/.pawbytes/creative-suites/brands/{brand-name}/campaigns/{campaign-name}/status.md` — campaign progress
- `{project-root}/.pawbytes/creative-suites/daily/YYYY-MM-DD.md` — daily log (append, tagged `[Campaign]`)

**Collects (from production agents):**
- `design-manifest.json` — from Designer workflows
- `video-manifest.json` — from Video Producer workflows
- `qa-report.md` — from quality control workflow
