# paw-cra-campaign-orchestration

## Overview

The central orchestration engine for the Aria Creative Suite. Takes a campaign brief with multiple deliverables, parses them into production tasks, dispatches Designer and Video Producer workflows in parallel, tracks progress, aggregates results, and runs quality control.

## What It Does

| Stage | Purpose |
|-------|---------|
| Brief Parsing | Parse campaign brief, identify all deliverables |
| Dependency Analysis | Analyze dependencies, build production queue |
| Parallel Dispatch | Launch Designer and Video Producer simultaneously |
| Progress Tracking | Track progress, collect manifests, update status |
| Quality Gate | Run QC, aggregate results, finalize campaign |

## When to Use It

- Executing multi-deliverable campaigns
- Running campaigns with both visual and video assets
- Launching product campaigns with coordinated deliverables
- Tracking campaign production progress
- Coordinating parallel production workstreams

## Trigger Phrases

- "Run campaign [name]"
- "Execute campaign [name]"
- "Launch campaign production"
- "Orchestrate deliverables for..."

## What You Get (Deliverables)

| Output | Location |
|--------|----------|
| Campaign status | `.pawbytes/creative-suites/brands/{brand}/campaigns/{campaign}/status.md` |
| Design manifests | `design-manifest.json` from Designer |
| Video manifests | `video-manifest.json` from Video Producer |
| QA report | `qa-report.md` from quality control |

## Arguments

| Arg | Description |
|-----|-------------|
| `--headless` or `-H` | Fully autonomous execution without interaction |
| `--template:product-launch` | Product launch campaign variant |

## Campaign Status File

Progress is tracked in `status.md` with frontmatter:

```yaml
---
campaign: '{campaign-name}'
brand: '{brand-name}'
status: 'in-progress'  # pending | in-progress | quality-gate | complete | failed
current_stage: '01-brief-parsing'
deliverables_total: 0
deliverables_complete: 0
design_track: 'pending'
video_track: 'pending'
qc_status: 'pending'
---
```

## External Skills Invoked

| Skill | Stage | Purpose |
|-------|-------|---------|
| `paw-cra-agent-designer` | 03 | Design production |
| `paw-cra-agent-video-producer` | 03 | Video production |
| `paw-cra-agent-strategist` | 02 | Only if deliverables need unresolved copy/scripts |
| `paw-cra-quality-control` | 05 | Aggregate QC across all assets |
| `paw-cra-multi-platform-export` | 05 | Platform variants post-QC (optional) |

## Quick Example

**Input**: Campaign brief with 3 social posts, 2 carousels, and 1 TikTok video

**Output**: Designer produces 5 visual assets while Video Producer produces 1 video simultaneously. Progress tracked in `status.md`. Final QC report confirms all assets pass brand and platform standards.

## Memory Contract

**Reads:**
- Agency state from `index.md`
- Brand guidelines from `brands/{brand}/guidelines.md`
- Campaign brief from `campaigns/{campaign}/brief.md`

**Writes:**
- Campaign status to `status.md`
- Daily log entries tagged `[Campaign]`

**Collects:**
- `design-manifest.json` from Designer
- `video-manifest.json` from Video Producer
- `qa-report.md` from quality control

## Related Skills

- [paw-cra-agent-creative-director](./paw-cra-agent-creative-director.md) -- Orchestrator
- [paw-cra-agent-designer](./paw-cra-agent-designer.md) -- Visual production
- [paw-cra-agent-video-producer](./paw-cra-agent-video-producer.md) -- Video production
- [paw-cra-quality-control](./paw-cra-quality-control.md) -- Campaign-level QC