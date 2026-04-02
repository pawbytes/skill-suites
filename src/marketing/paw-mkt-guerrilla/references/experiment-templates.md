# Growth Experiment Templates

> Ready-to-use templates for designing, prioritizing, tracking, and analyzing growth experiments. Copy, adapt, and fill in for each experiment.

---

## 1. Growth Experiment Document Template

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

---

## 2. ICE Scoring Worksheet

Use this worksheet in team scoring sessions. Score 10-15 ideas per session with 3-5 team members. Average individual scores to reduce bias.

```markdown
# ICE Scoring Session

**Date**: [YYYY-MM-DD]
**Participants**: [Names]
**North Star Metric**: [The strategic metric all ideas are scored against]

## Scoring Scale Reference

### Impact (If this works, how big is the effect?)
| Score | Meaning |
|:-----:|---------|
| 1-2   | Negligible: <1% improvement on North Star Metric |
| 3-4   | Minor: 1-5% improvement |
| 5-6   | Moderate: 5-15% improvement |
| 7-8   | Significant: 15-30% improvement |
| 9-10  | Transformational: 30%+ improvement or unlocks a new growth vector |

### Confidence (How sure are we this will work?)
| Score | Meaning |
|:-----:|---------|
| 1-2   | Pure guess: no data, no precedent, never tried anything similar |
| 3-4   | Low: some anecdotal evidence or loose analogy to another company |
| 5-6   | Medium: supporting data exists, competitor has done something similar |
| 7-8   | High: strong internal data, customer research, or proven pattern |
| 9-10  | Very high: we have tested this before with positive results or have definitive data |

### Ease (How easy is this to implement?)
| Score | Meaning |
|:-----:|---------|
| 1-2   | Very hard: multiple weeks, multiple teams, significant engineering |
| 3-4   | Hard: 1-2 weeks, requires engineering and design |
| 5-6   | Moderate: 2-5 days, one person or small team |
| 7-8   | Easy: 1-2 days, one person, mostly configuration or content |
| 9-10  | Trivial: under a day, copy change, toggle, or configuration |

## Ideas to Score

| # | Experiment Idea | I | C | E | ICE Avg | Rank |
|---|-----------------|:-:|:-:|:-:|:-------:|:----:|
| 1 |                 |   |   |   |         |      |
| 2 |                 |   |   |   |         |      |
| 3 |                 |   |   |   |         |      |
| 4 |                 |   |   |   |         |      |
| 5 |                 |   |   |   |         |      |
| 6 |                 |   |   |   |         |      |
| 7 |                 |   |   |   |         |      |
| 8 |                 |   |   |   |         |      |
| 9 |                 |   |   |   |         |      |
| 10|                 |   |   |   |         |      |
| 11|                 |   |   |   |         |      |
| 12|                 |   |   |   |         |      |
| 13|                 |   |   |   |         |      |
| 14|                 |   |   |   |         |      |
| 15|                 |   |   |   |         |      |

## Session Decisions

**Top 3 to run this sprint**:
1. [Idea]: ICE [score] -- Owner: [name] -- Start: [date]
2. [Idea]: ICE [score] -- Owner: [name] -- Start: [date]
3. [Idea]: ICE [score] -- Owner: [name] -- Start: [date]

**Parking lot (future sprints)**:
- [Ideas 4-6 with scores]

**Killed (do not revisit without new data)**:
- [Low-scoring ideas with reason]
```

---

## 3. 50 Proven Growth Experiments by Category

### Acquisition Experiments (Getting New Users)

| # | Experiment | Expected Impact | Difficulty | Category |
|---|-----------|:-:|:-:|---|
| 1 | Create "[Competitor] alternative" SEO pages | High | Medium | SEO/Content |
| 2 | Launch on Product Hunt with 30-day prep | High | High | Launch |
| 3 | Build a free tool (calculator, grader, template generator) as lead gen | High | High | Product |
| 4 | Start a referral program with double-sided incentives | High | Medium | Viral |
| 5 | Implement "powered by" badges on free tier outputs | Medium | Low | Viral |
| 6 | Create a viral waitlist with referral-to-move-up mechanic | Medium | Medium | Launch |
| 7 | Seed content with 20 micro-creators on TikTok simultaneously | Medium | Medium | Social |
| 8 | Write and rank for 10 "how to [task your product solves]" articles | High | High | SEO/Content |
| 9 | Cross-promote with 5 complementary newsletter partners | Medium | Low | Partnership |
| 10 | Build integrations with 3 popular tools and list on their marketplaces | High | High | Partnership |
| 11 | Run a "challenge campaign" on social media with a branded hashtag | Medium | Medium | Social |
| 12 | Parasite SEO: publish optimized articles on Medium, LinkedIn, and Reddit | Medium | Low | SEO |
| 13 | Create 50 programmatic "[template] for [use case]" pages | High | High | SEO |
| 14 | Implement exit-intent popup with compelling lead magnet offer | Medium | Low | Conversion |
| 15 | Launch a podcast interviewing target customers (distribution as marketing) | Medium | High | Content |

### Activation Experiments (Getting Users to First Value)

| # | Experiment | Expected Impact | Difficulty | Category |
|---|-----------|:-:|:-:|---|
| 16 | Reduce signup form to just email (ask for details later) | Medium | Low | Signup |
| 17 | Add an onboarding checklist with progress indicator | High | Medium | Onboarding |
| 18 | Pre-populate with sample data so users see value immediately | High | Medium | Onboarding |
| 19 | Send activation-focused email within 2 hours of signup | Medium | Low | Email |
| 20 | Add interactive product tour for first-time users | Medium | Medium | Onboarding |
| 21 | Implement a "quick start" template/wizard | High | Medium | Onboarding |
| 22 | Show a personalized dashboard based on signup intent | Medium | High | Personalization |
| 23 | A/B test "reverse trial" (full access for 14 days, then downgrade) vs. standard freemium | High | Medium | Pricing |
| 24 | Reduce time-to-value by cutting unnecessary onboarding steps | High | Low | Onboarding |
| 25 | Add social proof to the post-signup experience ("12,847 teams use this") | Low | Low | Social proof |
| 26 | Implement smart defaults based on user role/industry selection | Medium | Medium | Personalization |
| 27 | Create a "first win" celebration moment (animation, congratulations) | Low | Low | Engagement |
| 28 | Send a personal welcome email from the founder (not automated-looking) | Medium | Low | Email |
| 29 | Add a "skip to value" option that bypasses detailed setup | Medium | Low | Onboarding |
| 30 | Implement AI-powered onboarding that adapts to user behavior | High | High | AI |

### Retention Experiments (Keeping Users)

| # | Experiment | Expected Impact | Difficulty | Category |
|---|-----------|:-:|:-:|---|
| 31 | Send a re-engagement email when users are inactive for 7 days | Medium | Low | Email |
| 32 | Implement weekly digest email showing value delivered | Medium | Medium | Email |
| 33 | Add a "streak" or usage gamification mechanic | Medium | Medium | Engagement |
| 34 | Build a community (Discord/Slack) for users | High | High | Community |
| 35 | Create a "what you missed" notification for inactive users | Medium | Low | Notification |
| 36 | Implement feature discovery prompts for under-used features | Medium | Low | Engagement |
| 37 | Launch a customer feedback loop (NPS + action on detractors) | Medium | Medium | Feedback |
| 38 | Create habit-forming triggers (daily/weekly usage prompts) | Medium | Medium | Engagement |
| 39 | Implement cancellation flow with save offers and pause option | High | Medium | Churn |
| 40 | Add collaborative features that increase switching costs | High | High | Product |

### Referral Experiments (Getting Users to Invite Others)

| # | Experiment | Expected Impact | Difficulty | Category |
|---|-----------|:-:|:-:|---|
| 41 | Add "share your results" button after a success moment | Medium | Low | Viral |
| 42 | Implement a referral leaderboard with milestone rewards | Medium | Medium | Viral |
| 43 | Trigger referral prompt after users complete their first meaningful task | Medium | Low | Viral |
| 44 | Create shareable output pages (portfolios, reports, results) with branding | High | Medium | Viral |
| 45 | Offer extra storage/features for each successful referral | Medium | Low | Viral |

### Revenue Experiments (Getting Users to Pay More)

| # | Experiment | Expected Impact | Difficulty | Category |
|---|-----------|:-:|:-:|---|
| 46 | A/B test annual vs. monthly pricing prominence on pricing page | Medium | Low | Pricing |
| 47 | Implement usage-based upgrade prompts ("You've used 90% of your limit") | High | Medium | Upsell |
| 48 | Add a "most popular" badge to the plan you want users to choose | Low | Low | Pricing |
| 49 | Test 3 different price points for the same plan (price sensitivity) | High | Low | Pricing |
| 50 | Create a premium tier with exclusive features and position it as aspirational | Medium | Medium | Pricing |

---

## 4. A/B Test Duration Methodology

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

---

## 5. Experiment Tracking Dashboard Template

Track all experiments in a single view. Use a spreadsheet, Notion database, or project management tool.

```markdown
# Growth Experiment Tracker

## Active Experiments

| Experiment | Owner | Status | Start | End | ICE | Primary Metric | Baseline | Target | Current | Confidence |
|-----------|-------|--------|-------|-----|:---:|---------------|----------|--------|---------|:----------:|
|           |       | Running|       |     |     |               |          |        |         |            |
|           |       | Running|       |     |     |               |          |        |         |            |
|           |       | Running|       |     |     |               |          |        |         |            |

## Completed Experiments (Last 30 Days)

| Experiment | Owner | Decision | Primary Metric | Baseline | Result | Lift | Confidence | Learning |
|-----------|-------|----------|---------------|----------|--------|:----:|:----------:|----------|
|           |       | Ship     |               |          |        |      |            |          |
|           |       | Kill     |               |          |        |      |            |          |
|           |       | Iterate  |               |          |        |      |            |          |

## Experiment Backlog (Prioritized by ICE)

| # | Experiment Idea | I | C | E | ICE | Category | Next Step |
|---|----------------|:-:|:-:|:-:|:---:|----------|-----------|
| 1 |                |   |   |   |     |          |           |
| 2 |                |   |   |   |     |          |           |
| 3 |                |   |   |   |     |          |           |

## Weekly Velocity

| Week | Experiments Launched | Experiments Completed | Win Rate | Key Learning |
|------|:-------------------:|:--------------------:|:--------:|-------------|
|      |                     |                      |          |             |
|      |                     |                      |          |             |
|      |                     |                      |          |             |

## Monthly Summary

| Month | Total Experiments | Wins | Losses | Inconclusive | Win Rate | Cumulative Impact |
|-------|:-----------------:|:----:|:------:|:------------:|:--------:|:-----------------:|
|       |                   |      |        |              |          |                   |
|       |                   |      |        |              |          |                   |
```

### Dashboard Metrics to Track

- **Experiment velocity**: Experiments launched per week. Target: 2-3 for early-stage, 5-10 at scale.
- **Win rate**: Percentage of experiments that ship. Industry average: 15-30%. If above 50%, you are not testing bold enough ideas.
- **Average cycle time**: Days from idea to results. Target: under 14 days for most experiments.
- **Cumulative impact**: Total improvement on North Star Metric from all shipped experiments.
- **Ideas in backlog**: Should always have 20-30 scored ideas ready to run.

---

## 6. Failed Experiment Analysis Template

Failed experiments are learning opportunities. Every killed experiment should generate insights.

```markdown
# Failed Experiment Analysis: [Experiment Name]

**Date completed**: [YYYY-MM-DD]
**Owner**: [Name]

---

## What We Tested

[Brief description of the experiment -- what changed, who saw it, how long it ran.]

## What We Expected

Hypothesis: If we [change], then [metric] would [improve by X%] because [reasoning].

## What Actually Happened

| Metric | Control | Variant | Lift | Confidence |
|--------|---------|---------|:----:|:----------:|
|        |         |         |      |            |
|        |         |         |      |            |
|        |         |         |      |            |

**Decision**: Killed because [specific reason -- not significant, negative result, etc.]

## Why It Failed (Root Cause Analysis)

Analyze why the hypothesis was wrong. Check each possibility:

- [ ] **Wrong assumption about user behavior**: We assumed users would [X], but they actually [Y].
- [ ] **Wrong audience**: The experiment targeted [segment], but the real opportunity is [different segment].
- [ ] **Wrong metric**: The primary metric did not capture the real effect. We should have measured [alternative].
- [ ] **Wrong magnitude**: The change was too small to detect or too small to matter.
- [ ] **Technical issues**: The implementation had bugs, tracking errors, or sample ratio mismatch.
- [ ] **External factors**: Seasonality, competitor actions, or market changes affected results.
- [ ] **Insufficient sample size**: The test did not run long enough to reach statistical significance.
- [ ] **The hypothesis was simply wrong**: The assumed causal mechanism does not exist.

**Most likely root cause**: [One-sentence explanation]

## What We Learned

1. [Key learning that can inform future experiments]
2. [Insight about user behavior, messaging, or product]
3. [Data point we did not have before]

## What This Changes

- **Stop doing**: [Anything we should stop based on this learning]
- **Start testing**: [New experiment ideas generated by this failure]
- **Update assumptions**: [Beliefs about our users or product that need revision]

## Follow-Up Experiments

| Experiment Idea | How It Builds on This Learning | ICE Estimate |
|----------------|-------------------------------|:------------:|
|                |                               |              |
|                |                               |              |

## Did We Fail Fast Enough?

- Duration: [X days] -- Was this the minimum needed?
- Cost: [$ or hours invested] -- Was this proportionate to the potential learning?
- Could we have gotten this insight faster through [user interviews / surveys / competitor analysis / desk research]?
- **Lesson for experiment design**: [How to structure similar tests more efficiently]
```

---

## 7. Experiment Idea Generation Prompts

Use these prompts in brainstorming sessions to generate experiment ideas across the AARRR funnel:

### Acquisition
- What if we targeted [competitor]'s unhappy customers with a comparison page?
- What if we built a free version of our most popular paid feature as a standalone tool?
- What if we launched on [platform] with a [type of content] that solves [specific problem]?
- What if we partnered with [complementary product] for a co-marketing campaign?
- What if we created programmatic pages for every [use case / integration / location]?

### Activation
- What if we reduced our signup form to just one field?
- What if we showed users a personalized demo based on their industry before signup?
- What if we eliminated the first three steps of onboarding?
- What if new users could import data from their current tool in one click?
- What if we sent a personal video welcome message from a team member?

### Retention
- What if we sent a "here's the value you got this week" summary email every Friday?
- What if we gamified daily usage with a streak counter?
- What if we created a user community where members help each other?
- What if we proactively reached out to users whose usage dropped 50% week-over-week?
- What if we added a "save for later" feature that gives users a reason to come back?

### Referral
- What if we offered users an extra month free for every referral who converts?
- What if our product outputs included a "Made with [Product]" watermark that linked to us?
- What if we created a public leaderboard of top referrers with exclusive rewards?
- What if we triggered a referral prompt immediately after users achieve their first success?
- What if we made it possible to share results or outputs publicly as a portfolio?

### Revenue
- What if we tested a 20% price increase on new signups only?
- What if we offered annual plans with 2 months free instead of 1?
- What if we created a premium tier with white-glove support and custom features?
- What if we implemented usage-based pricing instead of flat pricing?
- What if we added a "team" plan with per-seat pricing and collaborative features?

---

## 8. Quick Reference: Experiment Dos and Don'ts

### Do
- Write the hypothesis before building anything.
- Set success criteria before launching.
- Run experiments for the full planned duration.
- Document everything, especially failures.
- Test one variable at a time (unless running multivariate tests with proper design).
- Celebrate learnings from failed experiments.
- Maintain a backlog of 20-30 scored ideas.
- Share results with the whole team.

### Don't
- Stop tests early because interim results look promising.
- Run tests without enough traffic to reach significance.
- Test multiple changes simultaneously and attribute results to one change.
- Ignore guardrail metrics (overall revenue, user satisfaction, support tickets).
- Discard failed experiments without analysis.
- Run experiments without clear ownership.
- Let experiments run indefinitely without a decision.
- Copy competitor experiments without understanding the reasoning behind them.

---

## Sources

- Sean Ellis, "Hacking Growth" -- experiment framework, ICE scoring.
- Aakash Gupta, "10 A/B Testing Best Practices for PMs" (2025).
- VWO A/B Test Duration Calculator methodology (2026).
- Evan Miller, "Sample Size Calculator" -- statistical methodology.
- GrowthLayer, "Pre- and Post-Test Calculators" (2026).
- ExperimentHQ, "A/B Test Duration Calculator" (2026).
- Contentful, "A/B Testing Best Practices" (2025).
- Ward van Gasteren, "ICE Framework" (2025).
- Daphne Tideman, "Growth Waves: Most Startups Prioritise Wrong" (2025).
