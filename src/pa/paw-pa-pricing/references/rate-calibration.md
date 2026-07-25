# Rate Calibration

Always loaded before computing prices. Determines **which hourly/project rate** applies before line-item or tier math.

## Priority order

1. **Pricing history** — `{memory-root}/library/pricing-history.json`
2. **Research benchmarks** — `pricingBenchmarks` from research dossier
3. **Config default** — `default_hourly_rate` (fallback only)

## History matching

Find comparable entries:

| Match signal | Weight |
| ------------ | ------ |
| Same `proposalType` | High |
| Same client (from `clientName`) | High |
| Overlapping line item names / tier totals within ±30% scope | Medium |
| Same industry (if recorded) | Medium |
| Any entry within last 12 months | Low (recency tie-break) |

**Calibrated rate:**

- Line-item: median `rate` across matching entries' line items, or derive `total/hours` from won quotes
- Tiered: median Better-tier `total` for similar scope; back-solve implied rate if hours estimated
- Prefer **won** quotes over lost/null when rates differ materially — note in `calibrationNotes`

If ≥ 3 comparable entries: use median. If 1–2: use mean, flag `thin-history`. If 0: skip to benchmarks.

## Benchmark fallback

From research dossier `pricingBenchmarks.observations[]`:

- Extract hourly or project range mid-point
- If project range only, estimate hours from brief scope and divide — show work in `calibrationNotes`

## Default fallback

`default_hourly_rate` from config when history and benchmarks both empty. State explicitly: "First-run calibration — no pricing history; using configured default $X/hr."

## Seller floor

If user or history implies a minimum acceptable rate (e.g. no historical quote below $100/hr), do not go below without `sanityCheck.flags` containing `"below-seller-floor"` and strategic justification.

## Output

Write prose `calibrationNotes` in `pricing.json` summarizing:

- Which history entries influenced rate (dates, clients, won/lost)
- Benchmark sources used
- Default fallback if applicable
- Effective blended rate used for this quote
