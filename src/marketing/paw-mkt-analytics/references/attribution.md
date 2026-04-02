# Attribution Modeling

Understand how channels contribute to conversions. Attribution is directional, not absolute — triangulate across methods.

## Models Explained

| Model | How It Works | Best For |
|---|---|---|
| Last-Touch | 100% credit to final touchpoint | Simple reporting, bottom-funnel optimization |
| First-Touch | 100% credit to first touchpoint | Understanding awareness channels |
| Linear | Equal credit to all touchpoints | Balanced view, early-stage analytics |
| Time-Decay | More credit closer to conversion | Long sales cycles, B2B |
| Position-Based (U-Shape) | 40% first, 40% last, 20% middle | Valuing discovery and closing |
| Data-Driven | Algorithmic, actual conversion paths | Mature programs, 300+ monthly conversions |

## When to Use Each

| Conversion Volume | Recommended Model |
|---|---|
| Under 100/month | Last-touch baseline, supplement with first-touch |
| 100-300/month | Position-based for balance |
| 300+/month | Data-driven in GA4 |
| B2B long cycles | Time-decay or position-based |

## Multi-Touch Implementation

- Ensure all channels are UTM-tagged
- GA4 defaults to data-driven (last-click fallback for low volume)
- Compare platform-reported vs GA4 conversions — every platform over-reports
- Build cross-channel views by exporting and normalizing data

## Incrementality Testing

The gold standard: does this channel drive conversions that would not have happened otherwise?

**Methods:**
- Geo-lift tests
- Conversion lift studies (Meta/Google built-in)
- Holdout tests (pause a channel 2-4 weeks)
- Matched market testing

**When:** Run on any channel consuming 20%+ of budget, annually or before major budget shifts.

## Marketing Mix Modeling (MMM)

For brands spending $50K+/month across 3+ channels. Uses regression to estimate channel contribution to revenue, accounting for external factors.

**Requirements:** 2+ years of weekly data

**Tools:** Meta Robyn, Google Meridian (both open source)

**Start simple:** Weekly spend per channel vs weekly revenue in a spreadsheet.

For detailed MMM process, see `marketing-mix-modeling` in frameworks-index.csv.

## Output

Save as `./.pawbytes/marketing-suites/brands/{brand-slug}/analytics/attribution-analysis-{YYYY-MM-DD}.md`

**Structure:**
- Model Used
- Top Conversion Paths
- Channel Attribution Comparison table
- Undervalued/Overvalued Channels
- Budget Reallocation Recommendations
- Incrementality Results