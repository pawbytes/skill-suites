# A/B Testing & Experiment Design Reference

> Complete methodology for designing, running, and analyzing marketing experiments including sample size calculations, hypothesis frameworks, ICE prioritization, implementation options, and common pitfalls.

---

## Test Types

| Type | Description | When to Use | Traffic Needed |
|---|---|---|---|
| **A/B** | Two versions (control vs variant) | Most tests — clear single change | Lowest |
| **A/B/n** | Multiple variants simultaneously | Testing 3-4 headline options at once | 2-3x more |
| **Multivariate (MVT)** | Multiple elements changed in combination | Interaction effects (headline + CTA) | 10x+ more |
| **Split URL** | Two separate pages, traffic split at server level | Major page redesigns, different layouts | Same as A/B |
| **Holdout** | Control group excluded from a change | Measuring incrementality of a program | Same as A/B |

Default to A/B. Only use MVT when you have very high traffic (10k+ conversions/month per variant needed).

---

## Hypothesis Formation

Structure: "Because [observation/data], we believe [change] will cause [expected outcome] for [audience]. We'll know this when [specific metric moves by X%]."

**Weak:** "Test a new homepage."
**Strong:** "Because our heatmap shows 70% of visitors don't scroll past the hero, we believe moving the pricing table above the fold will increase free trial signups by 15% for first-time visitors. We'll know this when the sign_up event rate is 15% higher in the variant at 95% confidence."

Every hypothesis needs: observation (data backing the idea), change (specific, one thing), outcome (measurable metric), and success threshold (the lift that makes implementation worth it).

---

## Sample Size and Duration

**Calculate before starting.** Never start a test without knowing the required sample.

Quick reference table (95% significance, 80% power):

| Baseline Conversion | Detectable Lift | Samples Needed Per Variant |
|---|---|---|
| 1% | 20% | ~46,000 |
| 2% | 20% | ~23,000 |
| 5% | 20% | ~9,000 |
| 5% | 10% | ~37,000 |
| 10% | 20% | ~4,500 |
| 10% | 10% | ~18,000 |
| 10% | 50% | ~600 |
| 20% | 20% | ~2,200 |

Use [Evan Miller's sample size calculator](https://www.evanmiller.org/ab-testing/sample-size.html) or build one from these inputs: baseline rate, minimum detectable effect (MDE), significance (95%), power (80%).

**Duration**: Run for at least 7 days regardless of sample (captures weekly cycles). Maximum 4-6 weeks (seasonality and novelty effects degrade results). If traffic won't hit sample size in 4 weeks, the test is underpowered — either increase MDE or find a higher-volume metric.

**Split**: 50/50 by default. Use 90/10 for high-risk changes (new checkout flow, pricing change) to limit exposure.

---

## Metrics Strategy

Define three metric types before launching:

- **Primary metric**: Directly tied to the hypothesis. This is the decision metric (e.g., signup rate, revenue per visitor). One primary metric only.
- **Secondary metrics**: Provide context and interpretation support (e.g., if signup rate rises, also watch activation rate to ensure quality isn't dropping).
- **Guardrail metrics**: Metrics you cannot afford to harm even if the primary wins (e.g., testing a more aggressive upsell modal — guardrail: cancellation rate must not increase).

A test can "win" on primary but fail on guardrails — in that case, it should not be shipped.

---

## ICE Prioritization

Score every test idea 1-10 on three dimensions:
- **Impact**: How large is the expected lift if this wins? (affects primary KPI)
- **Confidence**: How much evidence supports this hypothesis? (data, past tests, user research)
- **Ease**: How fast and cheap to implement and run to significance?

ICE Score = (Impact + Confidence + Ease) / 3

Run highest-ICE tests first. Keep a living ICE-scored backlog in `testing-roadmap-{YYYY-QN}.md`.

---

## Implementation Options

| Approach | How it works | Pros | Cons |
|---|---|---|---|
| **Client-side** | JavaScript swaps elements after page load | Fast to deploy, no dev needed (Optimizely, VWO) | Flickering, blocked by ad blockers, slight perf impact |
| **Server-side** | Variant determined before response is sent | No flicker, more reliable, works in apps | Requires dev involvement, slower to deploy |
| **Feature flags** | Code-level toggle for experiments | Most robust, works across full stack (LaunchDarkly, Unleash) | Developer dependency for every test |

Default: client-side for marketing page tests. Server-side or feature flags for anything inside the product.

---

## Analyzing Results

**The cardinal rule: do not look at results before reaching sample size.** Peeking and stopping early is the most common cause of false positives. Set a "do not check before" date and stick to it.

After reaching sample:
1. Check statistical significance (95% threshold)
2. Check practical significance — is the lift commercially meaningful given implementation cost?
3. Check secondary and guardrail metrics — did anything else move?
4. Segment the results — does the winner hold across device types, traffic sources, new vs returning?
5. Document in the testing roadmap: hypothesis, variants, sample, duration, winner, confidence level, actual lift, segments checked, next action

Ship winners after stakeholder approval — present results with statistical and practical significance before deployment. Archive losers — a failed test is still a learning (document why it failed).

---

## Common Pitfalls

- **Peeking**: Stopping when results "look good" produces 20-50% false positive rates
- **Simultaneous tests**: Running overlapping tests on the same page contaminate both results unless properly segmented
- **Ignoring seasonality**: Tests spanning holidays or promotions need longer runtimes to average out
- **Underpowered tests**: False negatives are as costly as false positives — a real improvement missed
- **Dismissing negatives**: A negative result is high-confidence information; learn from it
- **Single segment winners**: A headline that wins for mobile may lose for desktop — always check

---

## Testing Roadmap Structure

Quarterly roadmap structure (save as `testing-roadmap-{YYYY-QN}.md`):
- Testing capacity: monthly traffic, expected tests/month, tools available
- Active tests: hypothesis, start date, sample progress, estimated end date
- Planned tests: ICE-scored backlog
- Completed tests: results, lift, shipped/not shipped, learning
- Cumulative impact: revenue or conversion improvement from shipped winners

Compound effect: 5% lift per test, 10 tests/year = 63% cumulative improvement.

---

*See also: `./references/frameworks.md` Section 5 (A/B Test Design Framework) for the condensed checklist and `./references/best-practices.md` Section 5 (Experimentation Framework) for industry benchmarks.*
