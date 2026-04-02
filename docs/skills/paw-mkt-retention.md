# `marketing-retention`

## Overview

Focuses on churn reduction, lifecycle recovery, and engagement systems that keep customers. Owns the post-cancellation and at-risk-customer lifecycle.

## When to use it

Use `/paw-mkt-retention` when you need:
- churn diagnosis
- cancel-flow design or improvements
- dunning sequences for failed payments
- win-back campaigns
- proactive retention emails for at-risk customers
- lifecycle recovery ideas
- save offers and discount strategy

This skill owns cancel flows and dunning — not general email sequences or newsletters (use `marketing-email` for those).

## Inputs to prepare

- churn or cohort data if available
- lifecycle stage context
- known cancellation reasons
- customer segments
- current retention metrics (churn rate, LTV, health scores)

## Deliverables

- churn analysis
- retention campaign plans
- cancel flow copy and logic
- dunning email sequences
- win-back flows
- proactive retention email series
- dynamic save offer recommendations

## Framework files

10 individual framework files, indexed in `frameworks-index.csv`:

- Cancel flow copy and A/B testing
- Cancel confirmation copy variants
- Dunning email sequence (full multi-step)
- Dynamic offer templates by segment
- Exit survey copy
- Offer decision tree
- Proactive retention emails for at-risk customers
- Subject line reference
- Win-back email sequence

## Output locations

```text
brands/{brand-slug}/campaigns/retention/
```

## Related skills

- `marketing-email` — general email sequences and newsletters
- `marketing-analytics` — churn analysis, cohort tracking
- `marketing-referral` — win-back through referral incentives
- `product-marketing-context` — customer language for retention copy

## Sample prompts

```text
/paw-mkt-retention
Help us reduce churn.
```

```text
/paw-mkt-retention
Build a win-back plan for users who canceled in the last 90 days.
```

```text
/paw-mkt-retention
Use our lifecycle data and customer objections to redesign our cancel flow.
```

```text
/paw-mkt-retention
Write a dunning sequence for failed payments — 3 emails, escalating urgency.
```
