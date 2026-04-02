# ICE Scoring for Experiment Prioritization

## Overview
- Created by Sean Ellis (growth hacking pioneer) in the early 2010s.
- Fast, practical method for ranking marketing experiments and initiatives.
- Turns subjective debates into structured judgments.
- Used in weekly or biweekly planning cycles to maintain momentum.

## The Three Dimensions

**Impact (1-10)**: How much will this move the needle on our target metric?
- 10: Transformative impact on primary KPI (e.g., 2x conversion rate)
- 7-9: Significant impact, clear improvement expected
- 4-6: Moderate impact, incremental improvement
- 1-3: Minimal impact, nice-to-have

**Confidence (1-10)**: How sure are we that this will achieve the expected impact?
- 10: Strong data / evidence from similar past experiments
- 7-9: Good supporting data, analogous case studies
- 4-6: Reasonable hypothesis, some indirect evidence
- 1-3: Pure gut feeling, novel/untested idea

**Ease (1-10)**: How easy is this to implement?
- 10: Can do in a few hours, no dependencies
- 7-9: A few days, minimal resources needed
- 4-6: 1-2 weeks, moderate resources / coordination required
- 1-3: Multiple weeks, significant resources, complex dependencies

## Scoring Formula
```
ICE Score = (Impact + Confidence + Ease) / 3
```
Alternative (multiplicative):
```
ICE Score = Impact x Confidence x Ease
```
The additive version (average) is more commonly used in marketing contexts as it is less punitive for low scores in one dimension.

## ICE Scoring Example — Marketing Experiments
| Experiment | Impact | Confidence | Ease | ICE Score | Priority |
|---|---|---|---|---|---|
| A/B test homepage headline | 8 | 7 | 9 | 8.0 | 1st |
| Launch referral program | 9 | 5 | 4 | 6.0 | 3rd |
| Add exit-intent popup | 7 | 8 | 8 | 7.7 | 2nd |
| Redesign pricing page | 8 | 6 | 3 | 5.7 | 4th |
| Test TikTok ads | 6 | 3 | 7 | 5.3 | 5th |

## Best Practices
- Score as a team to reduce individual bias. Average team scores.
- Re-score monthly as confidence increases with new data.
- Complement with RICE (Reach, Impact, Confidence, Effort) when reach varies significantly between experiments.
- Use ICE for rapid weekly prioritization; use more detailed models (NPV, payback) for large investments.
- Document assumptions behind each score for future reference.
