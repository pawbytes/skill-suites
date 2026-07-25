# Tiered Pricing (Good / Better / Best)

Loaded when `mode` is `tiered` — the **default** (`default_pricing_mode: tiered`). Packages scope into three anchored tiers with a recommended middle option.

## When to use

- Pitch proposals where choice architecture drives conversion
- Scope flexes ( MVP vs full vs premium )
- Seller wants upsell path without line-item negotiation noise

## Tier design

| Tier | Role | Typical scope |
| ---- | ---- | ------------- |
| **Good** | Entry / MVP | Core deliverables only; minimal support |
| **Better** | Recommended anchor | Full brief scope; standard support — **mark `recommended: true`** |
| **Best** | Premium | Full scope + extras (training, extended support, add-ons) |

Custom tier names allowed if user specifies; keep three tiers unless brief demands two (then Good/Best only — note in `calibrationNotes`).

## Pricing logic

1. **Scope Better first** — fully satisfies `brief.md` requirements and timeline. Estimate as line items internally (don't expose unless user wants hybrid), sum to `betterTotal`.

2. **Derive Good** — remove nice-to-haves, reduce support window, defer optional requirements. Target **65–80%** of Better unless brief is already minimal.

3. **Derive Best** — add high-value extras aligned with research intel (training, monitoring, extra iteration round). Target **130–160%** of Better.

4. **Round thoughtfully** — round to sensible increments ($500 / $1,000) but document true calc in `calibrationNotes`; never arbitrary round numbers without trace.

5. **Set `total`** — equals recommended tier total (`Better` default).

## Includes / excludes

Each tier needs:

- `includes[]` — bullet deliverables client receives
- `excludes[]` (optional) — clarifies what's not in tier
- `positioning` — one sentence sales framing

Pull deliverable language from `scope-templates.md` when available.

## Anchoring

- Present Better as the "full brief" solution — Good is the budget door, Best is the aspiration anchor.
- If brief `budget` is stated, note in sanity check which tier fits; don't silently force below-market Good tier.

## Output

```json
{
  "mode": "tiered",
  "tiers": [ /* Good, Better, Best */ ],
  "selectedTier": "Better",
  "total": 12000,
  "lineItems": []
}
```

Optional: attach hidden `lineItems` breakdown for Better tier only if generation needs detail — document in `calibrationNotes`.

## After tier build

Sanity check, discount modeling, write `pricing.json`, append history.
