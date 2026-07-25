# Sanity Check & Discount Modeling

Always loaded after price computation, before writing `pricing.json`.

## Sanity check

Compare computed `total` (and tier range if applicable) against:

1. **Research benchmarks** — `pricingBenchmarks` from dossier; cite in `benchmarkSources[]`
2. **Pricing history** — similar past quotes; note if this quote is above/below median
3. **Brief budget** — if `brief.md` includes `budget`, populate `clientBudgetSignal`
4. **Seller floor** — from rate calibration

### Verdict rules

| Verdict | When |
| ------- | ---- |
| `within-market` | Within benchmark range or within ±20% of history median |
| `below-market` | More than 20% under benchmark low or historical won-quote median |
| `above-market` | More than 20% over benchmark high without premium justification |
| `insufficient-benchmarks` | No benchmarks and < 2 history entries — note reliance on defaults |

### Flags (optional)

- `"above-client-budget"` — recommended tier exceeds stated budget
- `"below-seller-floor"` — rate/ total below historical minimum
- `"thin-history"` — calibration from defaults or single data point
- `"scope-budget-mismatch"` — brief scope unrealistic for stated budget

`summary` — 2–3 sentences a seller can read aloud to defend or adjust the quote.

## Discount modeling

Produce **at least three** entries in `discountModeling[]`:

1. **List price** — `percent: 0`, `newTotal` = baseline
2. **Standard discount** — e.g. 10% — strategic accounts, repeat client
3. **Stretch discount** — e.g. 15–20% — maximum without breaking floor

For each:

- `newTotal = total × (1 - percent/100)` (round consistently)
- `impactNotes` — margin impact, whether still `within-market`, relationship rationale

Interactive mode: ask if seller has a target discount cap before modeling stretch scenarios.

## Negotiation guidance (prose to seller)

After writing JSON, briefly tell seller:

- Which tier/ total to lead with
- Maximum discount before sanity check flips to `below-market`
- If client budget mismatch, suggest scope trim (Good tier) not silent discount

## Write order

1. Complete sanity check object
2. Complete discount modeling array
3. Validate full document against `pricing-json-schema.md`
4. Write `{run-folder}/pricing.json`
5. Append history entry
