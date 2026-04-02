# Cohort Analysis Methodology

### What Is Cohort Analysis?
Grouping users by a shared characteristic (usually acquisition date) and tracking their behavior over time. Essential for understanding retention, LTV, and product-market fit.

### Cohort Types

#### Acquisition Cohorts
- **Grouped by**: Sign-up date (week or month)
- **Track**: Retention rate, activation rate, revenue per user
- **Use case**: Are we acquiring better or worse users over time?

#### Behavioral Cohorts
- **Grouped by**: Action taken (e.g., completed onboarding, used feature X)
- **Track**: Retention, upgrade rate, LTV
- **Use case**: Which behaviors correlate with retention?

#### Channel Cohorts
- **Grouped by**: Acquisition channel (organic, paid, referral)
- **Track**: Retention, LTV, payback period
- **Use case**: Which channels bring the highest-quality users?

### Cohort Retention Table Template
| Cohort    | Month 0 | Month 1 | Month 2 | Month 3 | Month 6 | Month 12 |
|-----------|---------|---------|---------|---------|---------|----------|
| Jan 2026  | 100%    | 65%     | 52%     | 45%     | 35%     | -        |
| Feb 2026  | 100%    | 68%     | 55%     | 48%     | -       | -        |
| Mar 2026  | 100%    | 70%     | 58%     | -       | -       | -        |

### Reading Cohort Data
- **Horizontal**: How a single cohort retains over time (retention curve)
- **Vertical**: How retention at a given period changes across cohorts (improvement trend)
- **Diagonal**: What is happening right now across all active cohorts
- **Healthy sign**: Retention flattens (finds a floor) rather than continually declining
- **Product-market fit signal**: Month-over-month retention improvement in newer cohorts
