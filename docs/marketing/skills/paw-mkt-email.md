# `marketing-email`

## Overview

Creates email strategy and assets across lifecycle, nurture, outbound, launch, and retention. Does not own cancel flows or dunning sequences — those belong to `marketing-retention`.

## When to use it

Use `/paw-mkt-email` when you need:
- welcome or nurture sequences
- newsletters
- launch emails
- cold/outbound B2B email sequences
- transactional or lifecycle emails
- ESP setup or deliverability advice
- email automation workflows
- general re-engagement emails

For cancel flows and dunning sequences, use `marketing-retention` instead.

## Inputs to prepare

- audience segment
- goal and offer
- funnel stage
- objections and proof
- sending context or ESP constraints

## Deliverables

- email sequences (welcome, nurture, launch, win-back, cold outbound)
- newsletter templates
- campaign plans
- automation workflow recommendations
- subject line options

## Framework files

12 individual framework files, indexed in `frameworks-index.csv`:

- Welcome series (SaaS and ecommerce)
- B2B lead nurture
- Newsletter framework
- Product launch sequence
- Abandoned cart series
- Post-purchase series
- Re-engagement series
- Win-back and sunset flow
- Subject line formulas
- Quick reference tables

## Output locations

```text
brands/{brand-slug}/content/email/
```

## Related skills

- `marketing-content` — long-form content that feeds email
- `marketing-retention` — cancel flows, dunning, and lifecycle recovery
- `marketing-sales` — sales outreach email templates
- `marketing-launch` — launch email sequencing

## Sample prompts

```text
/paw-mkt-email
Write a 5-email welcome sequence.
```

```text
/paw-mkt-email
For Acorn Legal, create a 4-email nurture sequence for firms that requested a demo but did not book a call.
```

```text
/paw-mkt-email
Use our product marketing context and launch plan to draft the announcement emails for our new feature release.
```

```text
/paw-mkt-email
Build a cold outbound sequence targeting HR managers at mid-size companies.
```
