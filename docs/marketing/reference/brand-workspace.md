# Reference: Brand Workspace

Every brand lives in its own local workspace:

```text
brands/{brand-slug}/
```

This keeps strategy, channel deliverables, and analytics together.

## Common structure

```text
brands/{brand-slug}/
├── brand-context.md
├── product-marketing-context.md
├── sostac/
├── campaigns/
├── content/
├── analytics/
└── assets/
```

## Key files

### `brand-context.md`
The lightweight source of truth for the brand:
- what the company does
- target audience
- stage
- USP
- current marketing status
- competitors

### `product-marketing-context.md`
The deeper positioning layer:
- customer language
- personas
- objections
- differentiation
- proof points
- voice guidance

### `sostac/`
The strategic planning folder built by `/paw-mkt-sostac`.

### `campaigns/`
Execution plans, experiments, and campaign systems.

### `content/`
Publishable assets and content production artifacts.

### `analytics/`
Tracking plans, reports, and performance reviews.

## Why this structure matters

The suite is designed to resume across sessions. Saving work in the brand workspace makes later tasks better because each specialist can read real context before producing anything new.

## Best practice

When a brand grows, keep strategy and outputs in the same workspace rather than scattering documents across unrelated folders.
