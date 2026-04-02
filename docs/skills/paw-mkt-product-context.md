# `product-marketing-context`

## Overview

Creates or updates the deep positioning file every specialist should read before producing marketing work.

## When to use it

Use `/paw-mkt-product-context` when:
- output feels generic or off-brand
- you want better personas, objections, and proof points captured
- SOSTAC is complete and you want a distilled reference
- you need stronger customer language for copywriting

## Inputs to prepare

- active brand
- `brand-context.md`
- SOSTAC files if they exist
- customer quotes, objections, reviews, proof points, and personas if available

## What the interaction looks like

The skill either:
- extracts what it can from SOSTAC, then asks only for missing gaps, or
- runs a focused interview if no SOSTAC plan exists

## Deliverables

A 12-section positioning document covering:
- product overview
- audience and personas
- pain points
- competition
- differentiation
- objections
- customer language
- brand voice
- proof points
- marketing goals

## Output location

```text
brands/{brand-slug}/paw-mkt-product-context.md
```

## Related skills

All specialists benefit from this file, especially:
- `marketing-content`
- `marketing-email`
- `marketing-seo`
- `marketing-social`
- `marketing-paid-ads`
- `marketing-sales`

## Sample prompts

```text
/paw-mkt-product-context
Create the product marketing context for our brand.
```

```text
/paw-mkt-product-context
Use our completed SOSTAC plan to build this file, then ask me only about missing customer language and proof points.
```

```text
/paw-mkt-product-context
Refresh our existing positioning document with new objections, proof, and customer phrases from recent calls.
```
