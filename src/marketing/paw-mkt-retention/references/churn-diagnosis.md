# Churn Diagnosis Capability

Before designing any retention intervention, understand what kind of churn is happening and why. Prescribing solutions before diagnosing is the most common retention mistake.

## Types of Churn

| Type | Definition | Primary Cause | Recovery Approach |
|---|---|---|---|
| Voluntary (active) | Customer deliberately cancels | Value perception, missing features, competitor, price | Cancel flow, proactive retention, win-back |
| Involuntary (passive) | Payment fails and account lapses | Expired card, insufficient funds, bank block | Dunning sequences, Smart Retry, card updater |
| Implicit | Customer stops using but does not cancel | Disengagement, poor onboarding, habit not formed | Health scoring, proactive outreach |
| Contractual expiry | Fixed-term contract ends and is not renewed | No renewal conversation, poor ongoing value delivery | QBRs, renewal playbooks, expansion offers |

**Involuntary churn represents 30-50% of all SaaS churn** and is the highest-recovery-rate category. Address it first.

## Calculating Churn Rates

**Monthly Churn Rate (Customer)**
```
(Customers lost in period / Customers at start of period) x 100
```
Target: under 2% for SMB SaaS, under 0.5% for enterprise SaaS, under 5% for consumer subscription.

**Monthly Revenue Churn (Gross MRR Churn)**
```
(MRR lost to cancellations + downgrades in period / MRR at start of period) x 100
```
Target: under 1.5% monthly gross MRR churn.

**Net Revenue Retention (NRR)**
```
((Starting MRR + Expansion MRR - Contraction MRR - Churned MRR) / Starting MRR) x 100
```
Target: above 100% (expansion exceeds churn). Best-in-class SaaS: 120-140%.

**Revenue Churn Rate vs Customer Churn Rate**: These diverge significantly when you have plan tiers. If enterprise customers churn less than SMB customers, revenue churn will be lower than customer churn -- which is healthy. Segment both metrics by customer cohort and plan type.

## Cohort Retention Analysis

Run retention curves by signup cohort (monthly or quarterly) to identify onboarding failures, product-market fit segments, and trend direction. Always segment by plan tier, acquisition channel, activation status, and geography.

For the full cohort table template, interpretation guide, and segmentation methodology, see `./benchmarks.md` Section 1.

## Identifying Churn Causes

Use all available signals. Prioritise in this order:

**Qualitative (direct feedback)**
- Exit survey data from cancel flow (most reliable for voluntary churn)
- Customer success call notes and support ticket themes
- NPS detractor verbatim responses
- Direct outreach to recently churned customers (email or call within 7 days of churn)

**Quantitative (behavioural signals)**
- Feature adoption rates: which features are churned customers NOT using?
- Login frequency trajectory in the 30-60 days before churn
- Support volume: do churned customers have more tickets? Unresolved tickets?
- Billing events: how many churned customers had at least one failed payment?
- Onboarding completion rates for churned vs retained cohorts

**Common churn causes by business type:**

| Business Type | Top Churn Causes |
|---|---|
| SaaS (SMB) | Price sensitivity, product not sticky enough, competitor switch, poor onboarding |
| SaaS (Enterprise) | Contract renewal not prioritised, stakeholder change, budget cut, implementation failure |
| Consumer subscription | Forgot they were subscribed, seasonal need, price, forgot to cancel |
| E-commerce subscription | Product quality, variety fatigue, price vs value, no longer needed |

## Deliverable

**Churn Diagnosis Report**: `churn-diagnosis-{YYYY-MM-DD}.md`
- Churn type breakdown
- Cohort analysis
- Root cause findings
- Prioritised recommendations

## Recommended Priority Order

If starting a retention programme from scratch, implement in this sequence:

1. **Payment recovery** (highest ROI, fastest wins -- enable Card Updater and Smart Retries this week)
2. **Dunning email sequence** (capture remaining involuntary churn)
3. **Cancel flow** (address voluntary churn at the moment of intent)
4. **Health scoring and proactive intervention** (prevent churn before intent forms)
5. **Win-back campaign** (re-engage churned customers)
6. **Ongoing churn analysis and cohort monitoring** (sustain improvements)