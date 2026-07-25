# Line-Item Pricing

Loaded when `mode` is `line-item`. Produces hours × rate breakdown with explicit totals per deliverable phase.

## When to use

- Scoping proposals with granular audit trail
- RFP responses requiring itemized cost tables
- Seller or client explicitly requested line-item format
- `--headless` default when config says `line-item`

## Process

1. **Decompose scope** — map `brief.md` `requirements[]` and `projectDescription` to 4–12 line items (phases or deliverables). Pull clause names from `scope-templates.md` when matching service type exists.

2. **Estimate hours** — per line item, realistic effort including review/PM overhead. Document uncertainty in `notes` if brief is thin.

3. **Apply rate** — per `rate-calibration.md`:
   - Role/blended rate from pricing history median for similar `proposalType`
   - Else research benchmark hourly band mid-point
   - Else `default_hourly_rate`

4. **Compute amounts** — `amount = hours × rate` for each line; `total = sum(amounts)`.

5. **Optional contingency** — single line item "Contingency / PM" (5–15%) only if brief complexity warrants; note in `calibrationNotes`.

## Output

Populate `pricing.json`:

- `mode`: `"line-item"`
- `lineItems[]`: full array with all entries
- `tiers`: `[]` or omit
- `valueBased`: omit
- `total`: sum of line items
- `selectedTier`: omit

## Explainability

`calibrationNotes` must list:

- Hour estimation basis (brief requirements cited)
- Rate source (history date, benchmark, or default)
- Any fixed-fee overrides

## Interactive prompts

If hours are ambiguous, ask seller for caps or prior similar project duration — do not silently guess large numbers.

## After line-item build

Proceed to `sanity-check-and-discounts.md`, write `pricing.json`, append history.
