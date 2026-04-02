# Marketing Attribution Models

### Model Comparison

#### Last-Click Attribution
- **How it works**: 100% credit to the last touchpoint before conversion
- **Pros**: Simple, easy to implement, actionable
- **Cons**: Ignores awareness and consideration touchpoints; over-credits bottom-funnel
- **Best for**: Direct response campaigns, short sales cycles
- **GA4 default**: Yes (reporting default)

#### First-Click Attribution
- **How it works**: 100% credit to the first touchpoint in the journey
- **Pros**: Highlights discovery and awareness channels
- **Cons**: Ignores nurture and conversion touchpoints
- **Best for**: Understanding top-of-funnel performance, brand awareness evaluation
- **GA4 default**: No (available in comparisons)

#### Linear Attribution
- **How it works**: Equal credit distributed across all touchpoints
- **Pros**: Acknowledges every touchpoint; balanced view
- **Cons**: Doesn't distinguish high-impact from low-impact touchpoints
- **Best for**: Long sales cycles with multiple meaningful touchpoints
- **GA4 default**: No (available in comparisons)

#### Time-Decay Attribution
- **How it works**: More credit to touchpoints closer to conversion; exponential decay
- **Pros**: Rewards recent engagement, reflects recency bias
- **Cons**: May undervalue initial awareness touchpoints
- **Best for**: B2B with long sales cycles, consideration-heavy purchases
- **GA4 default**: No (available in comparisons)

#### Position-Based (U-shaped) Attribution
- **How it works**: 40% first touch, 40% last touch, 20% distributed across middle
- **Pros**: Credits both discovery and conversion; acknowledges middle
- **Cons**: Arbitrary weighting; middle touches may be undervalued
- **Best for**: Balanced marketing programs with both awareness and conversion focus

#### Data-Driven Attribution (DDA)
- **How it works**: Machine learning analyzes all paths, assigns credit based on actual impact
- **Pros**: Most accurate; learns from your data; no arbitrary rules
- **Cons**: Requires significant data volume; black-box model; GA4 implementation varies
- **Best for**: Mature marketing programs with sufficient conversion volume
- **GA4 default**: Yes (default for Ads reports; requires sufficient data)
- **Minimum data**: ~300 conversions/month recommended for reliable DDA

#### Marketing Mix Modeling (MMM)
- **How it works**: Statistical analysis of aggregate marketing spend vs. business outcomes
- **Pros**: Privacy-friendly (no user-level data); includes offline channels; accounts for external factors
- **Cons**: Requires 2-3 years of data; expensive to implement; slow to update
- **Best for**: Enterprise brands with large multi-channel budgets; post-cookie planning
- **Tools**: Meta Robyn (open source), Google Meridian, Recast, Paramark

### Attribution Model Selection Guide
| Scenario                              | Recommended Model           |
|---------------------------------------|----------------------------|
| Limited data, simple funnel           | Last-click                 |
| Evaluating brand awareness            | First-click                |
| Long B2B sales cycle                  | Time-decay or Position-based |
| Mature program, high volume           | Data-driven                |
| Multi-channel, large budget           | MMM + DDA hybrid           |
| Privacy-first, cookieless future      | MMM + incrementality testing |

### Incrementality Testing
- **Purpose**: Measure true causal impact of a marketing channel
- **Method**: Geographic lift tests, holdout groups, PSA tests
- **When to use**: Validating attribution model outputs; evaluating channels with unclear ROAS
- **Tools**: Meta Conversion Lift, Google Geo-Lift, in-house holdout testing
