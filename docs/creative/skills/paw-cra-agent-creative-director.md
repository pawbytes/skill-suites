# paw-cra-agent-creative-director (Aria)

## Overview

Aria is the creative director and orchestrator of the Aria Creative Suite -- a team of AI specialists for modern content creation. She discovers available tools, onboards brands, analyzes briefs, plans campaigns, quality-checks deliverables, and routes work to the right specialist.

## What It Does

| Capability | Description |
|------------|-------------|
| Tool Discovery | Checks available tools and APIs on first activation |
| Brand Onboarding | Guides users through brand setup with voice, visuals, and guidelines |
| Brief Analysis | Parses creative briefs and identifies deliverable requirements |
| Campaign Planning | Breaks down multi-asset campaigns into production tasks |
| Campaign Orchestration | Dispatches Designer and Video Producer workflows in parallel |
| Quality Control | Aggregates QC across all campaign assets |
| Agent Routing | Routes requests to the correct specialist (Designer, Video Producer, Strategist) |
| Fast-Path | Skips validation gates for expert users with explicit specs |

## When to Use It

- Starting a new creative project or campaign
- Onboarding a new brand into the Creative Suite
- When you need creative direction but aren't sure which specialist to call
- Coordinating multi-deliverable campaigns with both visual and video assets
- Checking campaign status or reviewing progress
- Running quality control across all produced assets

## Trigger Phrases

- "Aria, help me with..."
- "I need a creative director"
- "Start a new campaign"
- "Onboard my brand"
- "What can the Creative Suite do?"
- "Run a campaign for [product/launch]"

## What You Get (Deliverables)

| Output | Location |
|--------|----------|
| Brand guidelines | `.pawbytes/creative-suites/brands/{brand-name}/guidelines.md` |
| Campaign briefs | `.pawbytes/creative-suites/brands/{brand-name}/campaigns/{campaign}/brief.md` |
| Campaign status | `.pawbytes/creative-suites/brands/{brand-name}/campaigns/{campaign}/status.md` |
| QA reports | `.pawbytes/creative-suites/brands/{brand-name}/campaigns/{campaign}/qa-report.md` |

## Arguments

| Arg | Description |
|-----|-------------|
| `--headless` or `-H` | Autonomous execution without interaction |
| `--headless:discover` | Tool availability check only |
| `--headless:status` | Campaign overview only |
| `--yolo` | Skip validation gates (expert mode) |

## Quick Example

**Input**: "Aria, I need to launch a product campaign with social posts and a TikTok video"

**Output**: Aria analyzes the brief, routes the social posts to Designer and the TikTok video to Video Producer in parallel, tracks progress, and runs quality control. Final deliverables include production-ready images and MP4 files with subtitles.

## Specialist Agents

Aria orchestrates these specialists based on output type:

| Specialist | Skill Name | Routes When |
|------------|------------|-------------|
| Designer | `paw-cra-agent-designer` | Images, graphics, carousels, flyers, brand assets |
| Video Producer | `paw-cra-agent-video-producer` | Videos, motion graphics, clips, voiceover |
| Strategist | `paw-cra-agent-strategist` | Research, scripts, copy, content strategy (on demand) |

**Production-first routing**: Route directly to Designer or Video Producer for visual/video deliverables. Strategist is only invoked when research or copy support is explicitly needed.

## Related Skills

- [paw-cra-agent-designer](./paw-cra-agent-designer.md) -- Visual production specialist
- [paw-cra-agent-video-producer](./paw-cra-agent-video-producer.md) -- Video production specialist
- [paw-cra-agent-strategist](./paw-cra-agent-strategist.md) -- Research and copy specialist
- [paw-cra-campaign-orchestration](./paw-cra-campaign-orchestration.md) -- Multi-deliverable campaign execution
- [paw-cra-quality-control](./paw-cra-quality-control.md) -- Campaign-level QC