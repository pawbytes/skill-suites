# Growth Experiment Document Template

Use this template for every growth experiment. Fill in before starting. Complete the results section after the experiment concludes.

```markdown
# Growth Experiment: [Descriptive Name]

**Date created**: [YYYY-MM-DD]
**Owner**: [Name]
**Status**: [ ] Planned  [ ] Running  [ ] Completed  [ ] Killed

---

## Hypothesis

If we [specific change or action],
then [primary metric] will [improve/decrease] by [X%]
because [reasoning based on data, customer insight, or precedent].

## ICE Score

| Dimension   | Score (1-10) | Rationale |
|-------------|:------------:|-----------|
| Impact      |              |           |
| Confidence  |              |           |
| Ease        |              |           |
| **Average** |              |           |

## Metrics

**Primary metric**: [The one number that defines success]
**Current baseline**: [Current value of the primary metric]
**Target**: [What success looks like -- specific number or percentage improvement]

**Secondary metrics** (supporting signals):
- [Metric 2]: current value [X], watching for [direction]
- [Metric 3]: current value [X], watching for [direction]

**Guardrail metrics** (must not degrade):
- [Metric that should not get worse]: current value [X], alert if [threshold]

## Experiment Design

**Type**: [ ] A/B test  [ ] Before/after  [ ] Multivariate  [ ] Feature flag  [ ] Manual

**Control (A)**: [What the current experience looks like]
**Variant (B)**: [What the changed experience looks like]
**Variant (C)**: [Optional additional variant]

**Audience**: [Who sees the experiment -- percentage of traffic, user segment, geography]
**Traffic split**: [50/50, 80/20, etc.]
**Sample size needed**: [Calculate using methodology in Section 5]
**Duration**: [Minimum days to run for statistical significance]
**Start date**: [YYYY-MM-DD]
**End date**: [YYYY-MM-DD]

## Implementation

- [ ] Step 1: [Technical implementation step]
- [ ] Step 2: [Content or design change]
- [ ] Step 3: [Tracking and measurement setup]
- [ ] Step 4: [QA and verification]
- [ ] Step 5: [Launch]

## Risk and Rollback

**What could go wrong**: [Potential negative outcomes]
**Rollback plan**: [How to revert if something breaks]
**Monitoring**: [What to watch during the experiment]

## Success Thresholds

- **Ship**: If primary metric improves by [X%] or more with [Y%] statistical confidence.
- **Iterate**: If primary metric improves by [Z%] but below ship threshold.
- **Kill**: If primary metric does not improve or degrades.

---

## Results (Fill After Experiment)

**Date completed**: [YYYY-MM-DD]
**Actual duration**: [X days]
**Sample size achieved**: [N visitors/users]

| Metric         | Control | Variant | Lift   | Confidence |
|----------------|---------|---------|--------|------------|
| Primary metric |         |         |        |            |
| Secondary 1    |         |         |        |            |
| Secondary 2    |         |         |        |            |
| Guardrail      |         |         |        |            |

**Decision**: [ ] Ship  [ ] Iterate  [ ] Kill

## Learnings

**What we learned**:
- [Key insight 1]
- [Key insight 2]

**What surprised us**:
- [Unexpected finding]

**What to test next**:
- [Follow-up experiment idea based on this result]

## Impact (Fill 30 Days After Shipping)

**Actual impact on primary metric (30-day post-ship)**: [X% improvement]
**Revenue impact (if applicable)**: [$X]
**Notes**: [Any long-term observations]
```
