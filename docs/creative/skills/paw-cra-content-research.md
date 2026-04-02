# paw-cra-content-research

## Overview

A service workflow that produces actionable research bundles -- competitor analysis, trend spotting, and content opportunity identification -- that feed directly into visual and video production. Every finding translates into a specific production recommendation.

## What It Does

| Stage | Purpose |
|-------|---------|
| Research Brief Intake | Parse brand, scope, focus areas, target platforms |
| Brand Context Load | Load guidelines and prior research |
| Competitor Scan | Analyze 3-5 competitors' content strategies |
| Trend Analysis | Identify trending formats, aesthetics, movements |
| Content Opportunities | Find gaps and exploitable angles |
| Production Recommendations | Create briefs for Designer and Video Producer |
| Report Generation | Consolidate findings into actionable report |
| Save to Memory | Write report and update daily log |

## When to Use It

- Any agent needs competitor analysis before production
- Researching content opportunities for a brand
- Identifying trending formats before campaign planning
- Finding gaps in competitor content strategies
- Generating production-ready briefs from research

## Trigger Phrases

- "Research competitors for..."
- "What are the trends in..."
- "Find content opportunities for..."
- "Analyze the competitor landscape..."

## What You Get (Deliverables)

| Output | Location |
|--------|----------|
| Research report | `.pawbytes/creative-suites/brands/{brand}/research/research-report.md` |
| Competitor analysis | `research/competitor-analysis.md` |
| Trend analysis | `research/trend-analysis.md` |
| Content opportunities | `research/content-opportunities.md` |
| Daily log | `.pawbytes/creative-suites/daily/YYYY-MM-DD.md` |

## Arguments

| Arg | Description |
|-----|-------------|
| `--headless` or `-H` | Autonomous execution |
| `--scope competitor` | Competitor analysis only |
| `--scope trend` | Trend analysis only |
| `--scope content` | Content opportunities only |
| `--scope all` | Full research bundle (default) |

## Research Tools

| Tool | Use |
|------|-----|
| `web_search_exa` | Competitor discovery, trend scanning |
| `crawling_exa` | Deep page content extraction |
| `get_code_context_exa` | Technical/platform documentation |
| Web Search | Fallback if Exa unavailable |
| agent-browser CLI | Gated social content (optional) |

## Trend Classification

| Classification | Duration | Action |
|----------------|----------|--------|
| Fad | <3 months | Use sparingly, quick turnaround |
| Trend | 6-18 months | Safe to build content around |
| Movement | 2+ years | Strategic foundation |
| Declining | N/A | Avoid |

## Quick Example

**Input**: "Research content opportunities for my fitness app brand, scope: all"

**Output**: Research report with 3-5 competitor analyses, trending fitness content formats, and 5-10 specific content angles. Each angle includes design briefs (visual concept, reference style, platform) and video briefs (format, hook, scene structure) ready for production.

## Production Recommendations

Every finding translates to actionable briefs:

**Design Briefs include:**
- Visual concept description
- Reference style
- Platform and dimensions
- Copy direction

**Video Briefs include:**
- Format and duration
- Hook concept (first 3 seconds)
- Scene structure outline
- Audio/music direction
- Subtitle style

## Quality Standards

- Every finding cites a source URL
- Every insight connects to production recommendation
- Competitor analysis focuses on content strategy
- Angle shortlist is specific and actionable
- Briefs are detailed enough for immediate production

## Related Skills

- [paw-cra-agent-strategist](./paw-cra-agent-strategist.md) -- Research specialist
- [paw-cra-agent-designer](./paw-cra-agent-designer.md) -- Visual production
- [paw-cra-agent-video-producer](./paw-cra-agent-video-producer.md) -- Video production