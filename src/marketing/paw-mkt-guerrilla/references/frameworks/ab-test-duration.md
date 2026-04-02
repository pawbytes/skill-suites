# A/B Test Duration Methodology

### How Long to Run Your A/B Test

Running a test too short leads to false positives. Running too long wastes time. Use this methodology to determine the correct duration.

### Required Inputs

1. **Baseline conversion rate**: Your current conversion rate on the metric being tested.
2. **Minimum Detectable Effect (MDE)**: The smallest improvement worth detecting. (Rule of thumb: if a 5% relative improvement would not change your business, set MDE higher.)
3. **Statistical significance level**: 95% is standard (5% chance of false positive).
4. **Statistical power**: 80% is standard (20% chance of missing a real effect).
5. **Daily traffic**: Average daily visitors or users exposed to the test.

### Duration Reference Table

Based on 95% confidence, 80% power, two-sided test, 50/50 traffic split:

| Baseline Rate | MDE (Relative) | Sample Size Per Variant | At 500/day | At 1,000/day | At 5,000/day |
|:---:|:---:|:---:|:---:|:---:|:---:|
| 2% | 20% | ~62,000 | ~248 days | ~124 days | ~25 days |
| 2% | 30% | ~28,000 | ~112 days | ~56 days | ~12 days |
| 2% | 50% | ~10,000 | ~40 days | ~20 days | ~4 days |
| 5% | 10% | ~31,000 | ~124 days | ~62 days | ~13 days |
| 5% | 20% | ~8,200 | ~33 days | ~17 days | ~4 days |
| 5% | 30% | ~3,700 | ~15 days | ~8 days | ~2 days |
| 5% | 50% | ~1,400 | ~6 days | ~3 days | ~1 day |
| 10% | 10% | ~14,500 | ~58 days | ~29 days | ~6 days |
| 10% | 20% | ~3,800 | ~16 days | ~8 days | ~2 days |
| 10% | 30% | ~1,700 | ~7 days | ~4 days | ~1 day |
| 10% | 50% | ~650 | ~3 days | ~2 days | ~1 day |

### Critical Rules

1. **Never stop a test early because it "looks significant."** Peeking inflates false positive rates from 5% to 25-50%.
2. **Always run for at least 7 full days** to capture day-of-week effects, even if sample size is reached sooner.
3. **Prefer running for 2 full weeks** (14 days) for important tests to capture bi-weekly patterns.
4. **Set the test duration before launching.** Do not change it based on interim results.
5. **If you do not have enough traffic**, increase MDE (detect only larger effects) or run a before/after test instead.
6. **For very low traffic (<100/day)**, A/B testing may not be feasible. Use qualitative methods (user testing, surveys, session recordings) instead.

### Sample Size Formula (Simplified)

```
n = (Z_alpha/2 + Z_beta)^2 * (p1(1-p1) + p2(1-p2)) / (p2 - p1)^2

Where:
  n = sample size per variant
  Z_alpha/2 = 1.96 (for 95% confidence)
  Z_beta = 0.84 (for 80% power)
  p1 = baseline conversion rate
  p2 = expected conversion rate (p1 * (1 + MDE))
```

In practice, use an online calculator (VWO, Optimizely, or Evan Miller's) rather than computing by hand.
