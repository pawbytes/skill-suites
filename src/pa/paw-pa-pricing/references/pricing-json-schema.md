# Pricing JSON Schema

Canonical output contract for `{run-folder}/pricing.json`. Downstream `paw-pa-generation` and the orchestrator read this file. Validate before write.

## Top-level fields

| Field | Type | Required | Description |
| ----- | ---- | -------- | ----------- |
| `schemaVersion` | string | yes | `"1.0"` |
| `mode` | enum | yes | `"line-item"` \| `"tiered"` \| `"value-based"` |
| `clientName` | string | yes | From brief |
| `proposalSlug` | string | yes | Run folder slug, e.g. `acme-corp-2026-07-03` |
| `generated` | string | yes | ISO date `YYYY-MM-DD` |
| `currency` | string | yes | ISO 4217, default `"USD"` |
| `total` | number | yes | Primary quoted amount (selected tier, line-item sum, or value price) |
| `selectedTier` | string | no | For tiered mode — which tier is recommended, e.g. `"Better"` |
| `lineItems` | array | mode-dependent | Required when `mode` is `line-item`; optional detail for other modes |
| `tiers` | array | mode-dependent | Required when `mode` is `tiered` |
| `valueBased` | object | mode-dependent | Required when `mode` is `value-based` |
| `calibrationNotes` | string | yes | How rates were chosen — history entries, benchmarks, defaults |
| `sanityCheck` | object | yes | Market defensibility assessment |
| `discountModeling` | array | yes | At least two discount scenarios |

## `lineItems[]` entry

```json
{
  "name": "Discovery & requirements",
  "hours": 8,
  "rate": 125,
  "amount": 1000,
  "notes": "Workshop + brief validation"
}
```

- `amount` must equal `hours × rate` (or document fixed-fee override in `notes`).

## `tiers[]` entry

```json
{
  "name": "Better",
  "total": 12000,
  "includes": ["Core deliverable A", "Support window 30 days"],
  "excludes": ["Optional integration X"],
  "positioning": "Recommended — full scope with support",
  "recommended": true
}
```

- Exactly one tier should have `"recommended": true` unless user specifies otherwise.
- Standard names: `Good`, `Better`, `Best` — or custom tier names with same structure.

## `valueBased` object

```json
{
  "clientOutcomeValue": 80000,
  "valueNarrative": "Estimated annual savings from automation",
  "priceAsPercentOfValue": 0.15,
  "total": 12000,
  "rationale": "15% of first-year value; aligns with similar engagements"
}
```

## `sanityCheck` object

```json
{
  "verdict": "within-market",
  "summary": "Total sits mid-range vs Clutch benchmarks and seller history",
  "benchmarkSources": [
    "research-dossier: Shopify rebuild $45k-$85k",
    "pricing-history: 2025-11-02 similar quote $72k won"
  ],
  "clientBudgetSignal": "Brief states $50k — Better tier above; Good tier fits",
  "flags": []
}
```

`verdict` enum: `"within-market"` | `"below-market"` | `"above-market"` | `"insufficient-benchmarks"`

`flags` optional strings: e.g. `"below-seller-floor"`, `"above-client-budget"`, `"thin-history"`

## `discountModeling[]` entry

```json
{
  "label": "10% strategic discount",
  "percent": 10,
  "newTotal": 10800,
  "impactNotes": "Still within market; margin impact ~$1,200"
}
```

Include baseline `"label": "List price", "percent": 0` as first entry.

## Example: tiered (minimal)

```json
{
  "schemaVersion": "1.0",
  "mode": "tiered",
  "clientName": "Acme Corp",
  "proposalSlug": "acme-corp-2026-07-03",
  "generated": "2026-07-03",
  "currency": "USD",
  "total": 12000,
  "selectedTier": "Better",
  "lineItems": [],
  "tiers": [
    {"name": "Good", "total": 8000, "includes": ["MVP scope"], "positioning": "Essential delivery", "recommended": false},
    {"name": "Better", "total": 12000, "includes": ["Full scope", "30-day support"], "positioning": "Recommended", "recommended": true},
    {"name": "Best", "total": 18000, "includes": ["Full scope", "90-day support", "Training"], "positioning": "Maximum value", "recommended": false}
  ],
  "calibrationNotes": "Rate $125/hr from pricing-history median; tiers scoped from brief requirements.",
  "sanityCheck": {
    "verdict": "within-market",
    "summary": "Better tier aligns with benchmark mid-point",
    "benchmarkSources": ["research-dossier pricing benchmarks"],
    "flags": []
  },
  "discountModeling": [
    {"label": "List price", "percent": 0, "newTotal": 12000, "impactNotes": "Baseline"},
    {"label": "10% discount", "percent": 10, "newTotal": 10800, "impactNotes": "Acceptable for strategic account"}
  ]
}
```

## History append entry (separate file)

Appended to `library/pricing-history.json` — simplified:

```json
{
  "date": "2026-07-03",
  "client": "Acme Corp",
  "proposalSlug": "acme-corp-2026-07-03",
  "proposalType": "pitch",
  "mode": "tiered",
  "lineItems": [],
  "tiers": [{"name": "Better", "total": 12000}],
  "total": 12000,
  "won": null,
  "clientFeedback": null
}
```

Orchestrator updates `won` and `clientFeedback` later via outcome intake.
