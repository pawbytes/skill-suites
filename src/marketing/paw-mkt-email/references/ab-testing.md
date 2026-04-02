# A/B Testing Framework

Test systematically to improve email performance.

## What to Test (Priority Order)

| Priority | Element | Impact | Variables |
|---|---|---|---|
| 1 | Subject lines | Highest impact on opens | Length, formula, personalization, emoji, urgency |
| 2 | Send time | Significant | Day of week, time of day |
| 3 | From name | Moderate | Brand name vs person name vs person at brand |
| 4 | CTA | High on clicks | Button text, color, placement, number of CTAs |
| 5 | Content length | Moderate | Short vs long-form |
| 6 | Personalization | Variable | Dynamic content vs static |
| 7 | Design | Low-moderate | Single column vs multi-column, image vs text |

## Testing Protocol

### Minimum Requirements

- **Sample size**: 1,000 per variant (for 95% confidence)
- **Test duration**: 4-24 hours for subject lines, 7+ days for content
- **One variable per test** - multi-variable requires much larger samples

### Documentation

Document every test:
- Hypothesis
- Variants tested
- Sample size
- Duration
- Result with confidence level
- Action taken based on result

### Timing

Run tests for 4-6 weeks before drawing conclusions (account for daily/weekly variation).

## Testing Calendar

Monthly cadence:
- Week 1 - subject line test
- Week 2 - send time test
- Week 3 - content/design test
- Week 4 - analyze and plan next month

## Compound Improvement

Small improvements compound:

```
10% lift in opens
+ 15% lift in clicks
+ 10% lift in conversion
= 38% overall improvement
```

## Statistical Significance

Use a significance calculator. Common thresholds:
- 90% confidence: acceptable for quick tests
- 95% confidence: standard for business decisions
- 99% confidence: required for major changes

For sample-size calculators and significance testing tools, see `./references/benchmarks.md`.