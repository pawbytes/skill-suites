# paw-cra-agent-strategist

## Overview

The Strategist is a research-driven content planner who transforms brand goals into actionable content strategies. Conducts competitor analysis, discovers trending opportunities, and produces scripts and copy ready for production. Every recommendation is grounded in research.

## What It Does

| Capability | Description |
|------------|-------------|
| Brief Validation | Validates briefs against agency standards when requested |
| Competitor Research | Analyzes 3-5 competitors across content, style, and positioning |
| Content Research | Researches topics, formats, and content opportunities |
| Trend Spotting | Identifies trending formats, aesthetics, and platform trends |
| Script Writing | Produces video scripts with hooks, structure, and CTAs |
| Copy Drafting | Writes copy for social posts, ads, and campaigns |
| Content Calendar | Creates posting schedules aligned with strategy |
| Browser Research | Accesses gated content behind logins via agent-browser |

## When to Use It

- Analyzing competitor content strategies
- Researching trending content formats
- Planning content strategy or calendar
- Writing video scripts or social copy
- Validating briefs before production
- Finding content opportunities and gaps

## Trigger Phrases

- "Research competitors for..."
- "What content trends are..."
- "Write a script for..."
- "Create copy for..."
- "Help me plan content for..."
- "I need the Strategist"

## What You Get (Deliverables)

| Output | Location |
|--------|----------|
| Research reports | `.pawbytes/creative-suites/brands/{brand}/research/` |
| Scripts and copy | `.pawbytes/creative-suites/brands/{brand}/campaigns/{campaign}/` |
| Content calendars | `.pawbytes/creative-suites/brands/{brand}/campaigns/{campaign}/` |
| Activity logs | `.pawbytes/creative-suites/daily/YYYY-MM-DD.md` |

## Arguments

| Arg | Description |
|-----|-------------|
| `--headless` or `-H` | Autonomous execution |
| `--headless:research` | Run competitor scan |
| `--headless:trends` | Run trend analysis |

## Research Tools

| Tool | Purpose |
|------|---------|
| agent-browser CLI | Access gated content (Instagram, LinkedIn, TikTok) |
| Exa MCP (`web_search_exa`) | Web search with clean results |
| Exa MCP (`crawling_exa`) | Deep page content extraction |
| Web Search | Fallback if Exa unavailable |

## Methodologies

| Framework | Application |
|-----------|-------------|
| SWOT Analysis | Competitor analysis |
| Porter's Five Forces | Competitive positioning |
| Content Pillar Framework | Topic authority building |
| 7-Part Retention Framework | Video script structure |
| AIDA, PAS, BAB | Copywriting formulas |

## Quick Example

**Input**: "Research competitors for my skincare brand and suggest content opportunities"

**Output**: A research report covering 3-5 competitor content strategies, trending formats in the skincare niche, and 5-10 specific content angles with design briefs and video briefs ready for Designer and Video Producer to act on.

## Routing After Completion

When artifacts are approved, Strategist proactively suggests next steps:

| Artifact Complete | Route To |
|-------------------|----------|
| Script approved | Designer or Video Producer |
| Copy draft approved | Designer |
| Content calendar finalized | Campaign orchestration |
| Research report delivered | Designer or continue Strategist |

## Related Skills

- [paw-cra-agent-creative-director](./paw-cra-agent-creative-director.md) -- Orchestrator
- [paw-cra-agent-designer](./paw-cra-agent-designer.md) -- Visual production
- [paw-cra-agent-video-producer](./paw-cra-agent-video-producer.md) -- Video production
- [paw-cra-content-research](./paw-cra-content-research.md) -- Research workflow