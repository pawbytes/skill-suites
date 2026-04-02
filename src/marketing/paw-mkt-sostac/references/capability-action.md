# Capability: Action Planning

**Outcome:** Convert tactics into executable sprint plan with clear ownership, budget, and risk mitigation.

**Output:** `./.pawbytes/marketing-suites/brands/{brand-slug}/sostac/05-action.md`

**Phase Question:** "Who does what, when?"

## Frameworks Applied

Load from `./references/frameworks-index.csv` (filter: `sostac_phase=Action`):
- RACI Matrix
- Agile Marketing Sprints
- Objective-and-Task Budgeting
- Kotter's Change Model

## Research Work

### 1. Identify Quick Wins
From ICE-scored backlog, pull highest-ease, high-impact items that can ship in Week 1 and Month 1. Present as immediate action list.

### 2. Build the 90-Day Sprint Plan
Break tactical plan into 2-week sprints with specific deliverables. Sequence based on dependencies and ICE priority.

### 3. Draft the RACI Matrix
Based on team size and capabilities from Situation. If team is small, flag where one person covers multiple roles and where outsourcing is needed.

### 4. Calculate Objective-and-Task Budget
Bottom-up: list every task needed to achieve each KR, cost it, sum it. Compare to allocated budget from Phase 4.

### 5. Build the Risk Register
Based on everything known about the brand's situation, flag top 5-7 risks with concrete mitigation plans.

## Presentation Format

> "Here's your execution roadmap:"

**Quick wins** — what to do this week and this month for immediate impact

**90-day sprint plan** — specific deliverables per sprint, sequenced by priority

**Resource requirements** — who does what, where gaps exist

**Bottom-up budget** — what it actually costs vs what was allocated

**Top risks** — what could go wrong and how to prevent it

**Confirmations needed** — team capacity, tool access, hard deadlines

## Output Template

```markdown
## Execution Summary

## Quick Wins
### This Week
### Month 1
### Month 3

## RACI Matrix
| Activity | Responsible | Accountable | Consulted | Informed |

## 90-Day Sprint Plan
| Sprint | Dates | Goal | Key Deliverables | Owner | Dependencies |

## Objective-and-Task Budget
| Key Result | Required Task | Cost | Frequency | Annual Total |
| | | | | Total Budget Required: |

## Budget Reconciliation
(Bottom-up total vs allocated budget — gap analysis and recommendations)

## Resource Allocation
| Role | Responsibility | Hours/Week | Cost/Month | Source (In-house/Outsource) |

## Dependencies Map

## Risk Register
| Risk | Likelihood | Impact | Mitigation | Owner | Early Warning Signal |

## Tools Setup Checklist
| Tool | Setup Task | Owner | Deadline |

## Action Plan Alignment Check
```

## Success Criteria

- Quick wins can genuinely ship in Week 1 / Month 1
- Sprint plan has realistic WIP limits
- RACI exposes resource bottlenecks before they happen
- Budget reconciliation shows gap (or surplus) with recommendations
- Every risk has a specific mitigation, not just "monitor"

## Resource Reality Check

Before finalizing, verify:
- Does one person have more than 2 sprint items? Flag it.
- Is budget > 20% off allocation? Adjust scope or budget.
- Are dependencies in correct sequence? No blockers in sprint 1 for items needed in sprint 3.

## Definition of Done

Every deliverable needs clear "done" definition:
- "Blog post done" = written, edited, approved, scheduled with meta tags and images
- "Email sequence done" = written, set up in tool, tested, approved
- "Landing page done" = designed, built, tested, approved, tracking verified