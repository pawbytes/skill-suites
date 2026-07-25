# Value-Based Pricing

Loaded when `mode` is `value-based`. Price ties to **client outcome value**, not hours — requires credible value signals from brief or research.

## Prerequisites

Before value-based pricing, confirm at least one of:

- Quantified outcome in brief (revenue target, cost savings, risk reduction)
- Client intel with measurable impact potential
- Prior case study with outcome metrics for similar work

If missing, warn seller and recommend `tiered` or `line-item` instead — do not invent ROI figures.

## Process

1. **Define value unit** — what economic outcome does the client gain? (annual savings, revenue uplift, risk avoided). Cite source: `brief.md`, research dossier, or case-study match.

2. **Estimate `clientOutcomeValue`** — conservative, cited number. Range is OK — use conservative bound for pricing math; note range in `valueNarrative`.

3. **Choose value capture rate** — typical **10–25%** of first-year value for projects; retainers may use monthly value slice. Justify from:
   - Seller's past value-based quotes in `pricing-history.json`
   - Industry norms if cited in research benchmarks
   - Strategic positioning (premium vs penetration)

4. **Compute `total`** — `clientOutcomeValue × priceAsPercentOfValue`, unless seller sets strategic price with documented rationale.

5. **Cross-check** — implicit hourly rate = total ÷ estimated hours. If far below calibrated rate, flag in sanity check. Value price must not violate seller floor without explicit strategic note.

## Output

```json
{
  "mode": "value-based",
  "valueBased": {
    "clientOutcomeValue": 80000,
    "valueNarrative": "First-year ops savings from automation (brief: reduce manual processing 20 hrs/wk)",
    "priceAsPercentOfValue": 0.15,
    "total": 12000,
    "rationale": "15% capture; comparable to 2025-08 won quote for similar outcome"
  },
  "total": 12000,
  "tiers": [],
  "lineItems": []
}
```

Optional supporting `lineItems[]` for transparency ("what we deliver for this value price") — recommended for RFP/scoping types.

## Explainability

`calibrationNotes` links value math to sources. `sanityCheck` compares value price to market project ranges from research — value-based doesn't ignore market reality.

## After value build

Discount modeling (value deals often negotiate %), write `pricing.json`, append history.
