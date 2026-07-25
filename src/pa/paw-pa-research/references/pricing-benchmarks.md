# Pricing Benchmarks Research

Loaded when web research is enabled, or when `{memory-root}/library/pricing-history.json` has relevant past quotes. Feeds `paw-pa-pricing` calibration and sanity checks.

## Goal

Gather **market rate observations** for the work type in this brief — hourly bands, project ranges, retainer norms — with cited sources.

## Sources

1. **`pricing-history.json`** — seller's own past quotes (highest trust for calibration); cite entry dates and outcomes
2. **Web listings** — agency rate cards, Clutch/G2 project bands, public RFP award ranges, job-post budgets for similar scope
3. **Research dossier web evidence** — reuse if examples include budget figures (cross-cite URL)
4. **Brief `budget` field** — client-stated budget is a signal, tag source `brief.md (client stated)`

## Output shape

```json
"pricingBenchmarks": {
  "summary": "Where this scope typically prices; seller history vs market",
  "observations": [
    {
      "workType": "Shopify Plus B2B rebuild",
      "range": "$45,000-$85,000 USD",
      "source": "https://clutch.co/... or pricing-history entry 2025-11-02",
      "notes": "US mid-market agencies; fixed-price projects"
    }
  ]
}
```

Include at least one observation from **seller history** if `pricing-history.json` has a comparable entry (same `proposalType` or overlapping line items).

## Discipline

- Ranges must come from **observed data** — multiple data points preferred; single data point labeled "single observation."
- Never fabricate Clutch scores, award amounts, or rate surveys.
- Note currency; default USD unless brief/config specifies otherwise.
- Flag when client budget (`brief.md`) sits below market — pricing workflow uses this for sanity check.

## Local-only mode

Use only `pricing-history.json` and `brief.md` budget. `summary` must state: "No live market scan — benchmarks from seller history and brief only."

## After gathering

Append to findings JSON. These observations become `sanityCheck.benchmarkSources` in `paw-pa-pricing`.
