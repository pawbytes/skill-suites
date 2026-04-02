---
name: paw-cra-content-research
description: On-demand research bundle for the Aria Creative Suite. Use when any agent needs competitor analysis, trend research, or content opportunity scanning to inform visual/video production.
---

# Content Research Workflow

## Overview

This workflow produces an actionable research bundle — competitor analysis, trend spotting, and content opportunity identification — that feeds directly into visual and video production. It is a **service workflow** invoked on-demand by any Aria Creative Suite agent (Strategist, Designer, Video Producer, or Aria herself) when research context is needed to inform creative decisions.

The output is not academic research. Every finding translates into a specific production recommendation: a design brief the Designer can act on, a video format the Video Producer can storyboard, a content angle with hook and platform guidance. If a finding does not lead to a "make this" recommendation, it is context, not output.

**Args:** Accepts `--headless` or `-H` for autonomous execution. Supports scoped research via `--scope competitor`, `--scope trend`, `--scope content`, or `--scope all` (default).

## On Activation

Load available config from `{project-root}/.pawbytes/config/config.yaml` and `{project-root}/.pawbytes/config/config.user.yaml` (root level and `cra` section). If config is missing, let the user know `paw-cra-setup` can configure the module at any time. Resolve:

- `{user_name}` (null) — address the user by name
- `{communication_language}` (system) — use for all communications
- `{document_output_language}` (system) — use for generated document content
- `{default_brand}` (null) — default brand to research if none specified

Load shared agency memory from `{project-root}/.pawbytes/creative-suites/index.md`. If a brand context is active or specified, load `{project-root}/.pawbytes/creative-suites/brands/{brand-name}/guidelines.md` and any existing research in `{project-root}/.pawbytes/creative-suites/brands/{brand-name}/research/`.

If `--headless`, complete the full pipeline without interaction using the active brand and scope from args. If interactive, greet and confirm research parameters before proceeding.

## Pipeline

### 1. Research Brief Intake

Parse the research request:

| Parameter | Source | Fallback |
|-----------|--------|----------|
| **Brand** | Explicit request or `--brand` arg | `{default_brand}` or active brand from index.md |
| **Scope** | `--scope` arg or explicit request | `all` (competitor + trend + content) |
| **Focus areas** | Explicit questions or topics | Derive from brand guidelines (industry, audience, competitors) |
| **Target platforms** | Explicit or from brand guidelines | Instagram, TikTok, YouTube, LinkedIn |

If interactive: confirm parameters and ask if there are specific questions or competitors to prioritize. If headless: proceed with available context.

### 2. Brand Context Load

Load from `{project-root}/.pawbytes/creative-suites/brands/{brand-name}/`:

- `guidelines.md` — brand identity, voice, visual style, industry, audience
- `research/` — any prior research reports (avoid redundant work, build on existing findings)

If no brand exists at the expected path, abort with a clear message suggesting brand onboarding through Aria.

### 3. Competitor Scan (scope: competitor or all)

Load `./references/competitor-scan.md` for detailed research guidance.

Use Exa MCP tools to analyze 3-5 competitors across:
- Content strategy and posting patterns
- Visual style and design language
- Video formats and production quality
- Platform presence and engagement signals
- Messaging and positioning

**Production lens:** For every competitor insight, note what it means for Designer and Video Producer. "Competitor X uses bold typography overlays on Reels" is more useful than "Competitor X has strong video presence."

### 4. Trend Analysis (scope: trend or all)

Load `./references/trend-analysis.md` for detailed research guidance.

Search for trends relevant to the brand's industry and audience:
- Trending content formats (carousel styles, video templates, interactive formats)
- Visual and aesthetic trends (color palettes, typography, layout patterns)
- Platform-specific trends (TikTok sounds, Instagram features, YouTube formats)
- Topical trends and hashtag movements

Classify each trend: **Fad** (<3 months), **Trend** (6-18 months), **Movement** (2+ years), **Declining** (avoid).

### 5. Content Opportunity Identification (scope: content or all)

Cross-reference competitor gaps with trending topics to find exploitable angles:
- What are competitors NOT doing that audiences want?
- Which trends align with the brand's strengths but competitors have not adopted?
- What content formats are under-served in this niche?
- Where is engagement high but content quality low (opportunity to dominate)?

Produce an **angle shortlist** — 5-10 specific content angles, each with:
- The angle (one sentence)
- Why it works (gap + trend alignment)
- Suggested format (carousel, reel, long-form video, etc.)
- Target platform

### 6. Production Recommendations

This is the most critical output section. Translate every research finding into briefs that Designer and Video Producer can act on directly.

Load `./references/production-recommendations.md` for recommendation templates.

For each recommended angle, produce:

**Design briefs** (for Designer):
- Visual concept description
- Reference style (e.g., "minimalist with bold type overlay," "before/after split")
- Platform and dimensions
- Suggested copy direction

**Video briefs** (for Video Producer):
- Format and duration
- Hook concept (first 3 seconds)
- Scene structure outline
- Audio/music direction
- Subtitle style

**Platform-specific notes:**
- Optimal posting context (time, hashtags, caption strategy)
- Platform feature usage (Instagram collab, TikTok stitch, YouTube Shorts)

### 7. Report Generation

Produce `research-report.md` following the structure in `./references/report-template.md`.

The report consolidates all findings into a scannable document with:
- Executive summary (key findings in 3-5 bullets)
- Competitor landscape
- Trend landscape
- Angle shortlist (the actionable core)
- Production recommendations (the handoff to Designer/Video Producer)
- Platform-specific playbooks
- Sources with URLs

### 8. Save to Memory

Write the report to `{project-root}/.pawbytes/creative-suites/brands/{brand-name}/research/research-report.md` with frontmatter:

```yaml
---
created: YYYY-MM-DDTHH:MM:SSZ
brand: {brand-name}
scope: {scope}
type: research
---
```

If scope-specific reports were generated, also save:
- `competitor-analysis.md` (scope: competitor or all)
- `trend-analysis.md` (scope: trend or all)
- `content-opportunities.md` (scope: content or all)

Append to `{project-root}/.pawbytes/creative-suites/daily/YYYY-MM-DD.md`:

```markdown
## [Strategist] HH:MM - Content Research Complete
- Brand: {brand-name}
- Scope: {scope}
- Key findings: {2-3 bullet summary}
- Angles identified: {count}
- Report: .pawbytes/creative-suites/brands/{brand-name}/research/research-report.md
```

### 9. Handoff

If interactive: present the angle shortlist and ask which angles to prioritize for production. Suggest routing to Designer or Video Producer with the relevant briefs.

If headless: report completion and file locations. The calling agent reads the report from memory.

## Research Tools

### Primary: Exa MCP

| Tool | Use |
|------|-----|
| `web_search_exa` | Competitor discovery, trend scanning, industry analysis |
| `crawling_exa` | Deep page content extraction from competitor sites |
| `get_code_context_exa` | Technical/platform documentation lookup |

### Fallback: Web Search

If Exa MCP is unavailable, use the Web Search tool for the same research queries.

### Optional: Agent-Browser CLI

For social media content behind login gates (Instagram feeds, TikTok For You, LinkedIn). Only use if `agent-browser` is available and auth sessions exist at `{project-root}/.pawbytes/creative-suites/.auth/`.

## Quality Standards

- Every finding must cite a source URL
- Every insight must connect to a production recommendation
- Competitor analysis focuses on content strategy, not corporate profiles
- Trend classification distinguishes fads from movements
- The angle shortlist is the most important output — it must be specific and actionable
- Production recommendations must be detailed enough for Designer/Video Producer to start work without further research
