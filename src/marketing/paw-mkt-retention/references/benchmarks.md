# Retention Benchmarks, Metrics, and Cohort Analysis

> Detailed retention metrics, industry benchmarks, and cohort analysis methodology. Referenced from SKILL.md Sections 1.3, 6.1, and 6.2.

---

## 1. Cohort Retention Analysis

Run retention curves by signup cohort (monthly or quarterly). Key questions:
- Which cohorts have the steepest early drop-off? (Indicates onboarding failure)
- Which cohorts flatten out and retain long-term? (Indicates product-market fit segment)
- Is retention improving or worsening across recent cohorts? (Indicates product or go-to-market trends)

Present as a cohort retention table: rows = signup month, columns = months since signup (M0-M24), cells = % of original cohort still active.

### Cohort Table Template

```
| Cohort    | M0   | M1   | M2   | M3   | M6   | M12  | M18  | M24  |
|-----------|------|------|------|------|------|------|------|------|
| Jan 2025  | 100% | ?%   | ?%   | ?%   | ?%   | ?%   | ?%   | ?%   |
| Feb 2025  | 100% | ?%   | ?%   | ?%   | ?%   | ?%   | ?%   |      |
| Mar 2025  | 100% | ?%   | ?%   | ?%   | ?%   | ?%   |      |      |
```

### What to Look For

- **Steep early drop-off (M0-M3):** Onboarding failure. Customers are not reaching the aha moment. Fix activation before adding more customers.
- **Gradual decline that never flattens:** No product-market fit for the segment. Customers are not finding lasting value.
- **Flattening curve after M3-M6:** Healthy retention. Customers who survive the first 3-6 months tend to stay. Focus on getting more customers past that inflection point.
- **Improving curves over time:** Product or onboarding improvements are working. Keep investing.
- **Worsening curves over time:** Quality or onboarding regression. Investigate what changed.

### Segmenting Cohorts

Always segment cohort analysis by:
- **Plan tier:** Enterprise vs SMB churn behaves very differently
- **Acquisition channel:** Organic signups may retain differently from paid acquisition
- **Activation status:** Activated vs non-activated cohorts reveal the true impact of onboarding
- **Geography:** Different markets may have different retention patterns

---

## 2. Retention Dashboard Metrics

Track these metrics weekly or monthly depending on business size. Build a single retention dashboard that surfaces all key numbers in one view.

| Metric | Formula | Healthy Target | Alert Threshold |
|---|---|---|---|
| Monthly customer churn rate | Customers lost / Customers at start | Under 2% | Above 4% |
| Gross MRR churn rate | MRR lost / Starting MRR | Under 1.5% | Above 3% |
| Net Revenue Retention | (Start MRR + Expansion - Contraction - Churn) / Start MRR | Above 100% | Below 90% |
| Cancel flow impression rate | Customers seeing flow / Customers cancelling | 80%+ | Below 60% |
| Save rate | Customers saved / Customers who saw flow | 25-35% | Below 15% |
| Offer acceptance rate | Offers accepted / Offers shown | 15-25% | Below 10% |
| Dunning recovery rate | Payments recovered / Payments failed | 50-60% | Below 30% |
| Win-back rate (90d) | Reactivations / Total churned | 10-15% | Below 5% |
| MRR saved per month | Sum of MRR from saves + dunning recovery | Varies by plan pricing | Baseline from Month 1 |
| Health score distribution | % Green / Yellow / Red | 70%+ Green | Under 50% Green |

---

## 3. Industry Benchmarks by Business Type

| Business Type | Monthly Churn | Annual Churn | NRR Target |
|---|---|---|---|
| SMB SaaS | 2-5% | 22-46% | 90-100% |
| Mid-market SaaS | 1-2% | 12-22% | 100-115% |
| Enterprise SaaS | 0.5-1% | 6-11% | 110-140% |
| Consumer subscription | 5-8% | 46-64% | 80-95% |
| E-commerce subscription box | 6-10% | 54-70% | 80-90% |

**Context note**: These are averages. Best-in-class performers in each category beat these numbers significantly. Use them as a floor, not a ceiling.

---

## 4. Leading vs Lagging Indicators

**Lagging indicators** (tell you what happened -- use for reporting):
- Monthly churn rate
- MRR lost to churn
- Win-back rate

**Leading indicators** (tell you what is about to happen -- use for intervention):
- Health score distribution (% of accounts in Yellow/Red)
- Activation rate for new signups (leading indicator of future churn in 30-90 days)
- NPS score trends
- Failed payment volume
- Average days since last login across customer base

Build alerts on leading indicators. By the time lagging indicators move, churn has already happened.

---

## 5. Retention Reporting Cadence

| Report | Frequency | Audience | Content |
|---|---|---|---|
| Retention dashboard | Weekly | Retention team, CS | All metrics, health distribution, MRR saved |
| Churn analysis | Monthly | Leadership | Churn rate, reasons breakdown, cohort curves, actions taken |
| Dunning recovery report | Weekly | Finance, CS | Payments failed, recovery rate, outstanding balance |
| Cancel flow performance | Monthly | Product, CS | Impression rate, save rate, offer acceptance by type |
| Win-back campaign report | Monthly | Marketing | Emails sent, open/click rates, reactivations, MRR recovered |
