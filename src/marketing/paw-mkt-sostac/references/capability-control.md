# Capability: Control Setup

**Outcome:** Define how to measure success and what to do when metrics drift.

**Output:** `./.pawbytes/marketing-suites/brands/{brand-slug}/sostac/06-control.md`

**Phase Question:** "How do we monitor and improve?"

## Frameworks Applied

Load from `./references/frameworks-index.csv` (filter: `sostac_phase=Control`):
- North Star Metric
- Attribution Models
- Leading vs Lagging Indicators
- PDCA Cycle
- Balanced Scorecard
- OKR Review Cadence

## Research Work

### 1. Recommend the North Star Metric
Based on business model, growth stage, and strategy. Propose the single metric that best predicts long-term success. Explain why alternatives were rejected.

### 2. Select the Attribution Model
Based on brand's channel mix, purchase cycle, and data maturity. Recommend one with reasoning. Don't ask the user to choose.

### 3. Build Leading/Lagging Indicator Framework
For each OKR Key Result, identify leading indicators that predict whether target will be hit. This is where real monitoring value lives.

### 4. Design Optimization Trigger Rules
Concrete "if X then Y" rules for every key metric. Specific enough that anyone on team can execute them.

### 5. Draft Dashboard Specification
What to monitor daily, weekly, monthly. What review meetings should cover.

### 6. Design the Feedback Loop
How learnings from Control feed back into next planning cycle.

## Presentation Format

> "Here's how we'll know if the plan is working and exactly what to do when it's not:"

**North Star Metric** — what it is and why

**Attribution model** — recommended approach for your situation

**Optimization triggers** — specific rules for when to adjust tactics

**Review cadence** — what to check daily/weekly/monthly/quarterly

**Dashboard spec** — what to build and where

**Quick confirmation** — data sources available, team capacity for analytics, existing dashboard tools

## Output Template

```markdown
## North Star Metric
(Metric, definition, current baseline, target, why this metric)

## Attribution Model
(Selected model, rationale, implementation steps, alternatives considered)

## Leading vs Lagging Indicators
| Type | Metric | Baseline | Target | Frequency | Data Source | What It Predicts |

## Balanced Scorecard
| Perspective | KPI | Target | Frequency |

## OKR Review Cadence
| Cadence | Format | Owner | Agenda | Decision Expected |

## PDCA Cycle Definition
| Phase | Activities | Owner | Frequency |

## Optimization Trigger Rules
| Metric | Threshold | Time Window | Trigger Action | Owner | Escalation Path |

## Dashboard Specification
### Daily Monitoring
### Weekly Report
### Monthly Deep Dive
### Quarterly Review

## Feedback Loop
(How learnings feed the next Situation Analysis cycle)

## Control Alignment Check
```

## Success Criteria

- North Star measures customer value, not just revenue
- Attribution model matches data maturity (don't recommend MMM if brand has <100 conversions/month)
- Every KR has leading indicators, not just lagging
- Optimization triggers are specific: "If CAC > $80 for 2 weeks, pause underperforming channels"
- Dashboard has max 7 metrics per view (cognitive load limit)

## Attribution Model Selection Guide

| Monthly Conversions | Recommended Model |
|---------------------|-------------------|
| <100 | Last-touch |
| 100-1,000 | Position-based (U-shaped) |
| 1,000-10,000 | Data-driven (GA4/platform) |
| 10,000+ | Data-driven + incrementality testing |
| $500k+ ad spend | Add MMM |

## Optimization Trigger Rules Template

For each metric, define:
- **Warning threshold** — when to pay attention
- **Action threshold** — when to intervene
- **Specific action** — what to do
- **Owner** — who does it
- **Escalation path** — if action doesn't work

Example:
| Metric | Warning | Action | Response | Owner |
|--------|---------|--------|----------|-------|
| CPC (paid search) | >20% above target | >40% above target | Pause low-performers, restructure | Paid lead |
| CAC | >20% above for 2 weeks | >30% for 4 weeks | Channel reallocation | Marketing lead |