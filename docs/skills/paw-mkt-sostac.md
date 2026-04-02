# `marketing-sostac`

## Overview

Builds a full SOSTAC marketing plan by researching first and delivering strategic recommendations — not running an interview. The skill does the analysis work, then validates findings with the user rather than extracting information through questions.

## Philosophy: Research → Recommend → Validate

Each phase follows this three-step sequence:

1. **Research** — automated web research, competitor analysis, benchmarks
2. **Recommend** — presents findings and strategic options with trade-offs
3. **Validate** — 2–4 targeted questions to fill genuine gaps ("Based on X, I recommend Y — does that align?")

The user should feel like they hired a strategist who shows up prepared, not one who shows up with a clipboard.

## When to use it

Use `/paw-mkt-sostac` when:
- you need a full marketing plan
- your current tactics feel disconnected
- you want strategy saved to files for future sessions
- a coordinator routed you here

## Inputs to prepare

Nothing is required upfront. The skill starts with auto-discovery research. If you have the following, it helps speed up validation:

- brand website or URL
- product overview or description
- known competitors
- goals or KPIs
- budget and team constraints

## What the interaction looks like

The skill runs 7 phases in sequence, resuming from the first incomplete phase:

| Phase | What happens | Output |
|-------|-------------|--------|
| 0 — Auto-Discovery | Automated web research before first user interaction | `00-auto-discovery.md` |
| 1 — Situation | Competitive analysis, SWOT, market sizing | `01-situation.md` |
| 2 — Objectives | Benchmarked OKR/KPI recommendations | `02-objectives.md` |
| 3 — Strategy | Positioning, segments, channel strategy | `03-strategy.md` |
| 4 — Tactics | Channel-level execution plan with ICE scoring | `04-tactics.md` |
| 5 — Action | Roled roadmap, ownership, timeline | `05-action.md` |
| 6 — Control | KPI dashboards and review cadences | `06-control.md` |

After all 6 phases: `plan-summary.md` (executive summary).

### Auto-Discovery (Phase 0)

Runs automatically before the user is asked anything. Covers:
- Brand web presence
- Competitor analysis
- Market sizing and category trends
- Customer language (reviews, forums, G2, Reddit)
- SEO and paid ad landscape

### Resumption logic

Before starting, the skill reads `sostac/README.md`, checks which phase files exist, re-reads all completed phases, then picks up at the first incomplete phase. Completed phases are never re-researched.

## Deliverables

- `00-auto-discovery.md` — pre-research synthesis
- Six phase files (`01-situation.md` through `06-control.md`)
- `plan-summary.md` — executive summary

## Output locations

```text
brands/{brand-slug}/sostac/
```

## Frameworks used

38 individual framework files, indexed in `frameworks-index.csv`. Selected automatically per phase:

SWOT+TOWS, PESTLE, Porter's Five Forces, TAM/SAM/SOM, JTBD, OKR, RACE, STP, Ansoff, positioning statement, AARRR, ICE scoring, 7P, RACI, PDCA, Balanced Scorecard, Blue Ocean, Kotter change model, North Star Metric, OKR review cadence, PIE framework, objective cascade, leading/lagging indicators, and more.

## Related skills

- `marketing-agency` — routes to SOSTAC when no plan exists
- `product-marketing-context` — run after SOSTAC to build deep positioning doc
- All execution specialists — feed from SOSTAC output

## Sample prompts

```text
/paw-mkt-sostac
Build a complete marketing plan for our brand.
```

```text
/paw-mkt-sostac
Continue the existing SOSTAC plan for Acorn Legal from the next incomplete phase.
```

```text
/paw-mkt-sostac
We sell a workflow tool for recruiting teams. We need a strategy before investing more in SEO, paid ads, and email.
```
