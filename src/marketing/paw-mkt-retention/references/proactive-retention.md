# Proactive Retention Capability

The most effective retention happens before the customer ever clicks "Cancel." Identify at-risk customers early, intervene with the right message at the right time, and prevent the cancellation intent from forming in the first place.

## Customer Health Scoring

Build a health score for every active account. Assign weights to signals based on their correlation with churn in your specific product. The framework below is a starting point -- calibrate against your own data.

**Engagement signals (up to 40 points)**

| Signal | Healthy | At Risk | Weight |
|---|---|---|---|
| Login frequency | Consistent with baseline | Declining 30%+ below baseline | 15 pts |
| Core feature usage | Weekly use of primary feature | No core feature use in 14d | 15 pts |
| Session depth | Using 3+ features per session | Single-feature sessions only | 10 pts |

**Relationship signals (up to 30 points)**

| Signal | Healthy | At Risk | Weight |
|---|---|---|---|
| Support tickets | Zero or resolved quickly | Open tickets 7d+ | 10 pts |
| NPS / CSAT score | Promoter (9-10) or Passive (7-8) | Detractor (0-6) | 10 pts |
| Customer success engagement | Regular check-ins, responsive | No response to last 2 outreach attempts | 10 pts |

**Business signals (up to 30 points)**

| Signal | Healthy | At Risk | Weight |
|---|---|---|---|
| Seat/usage expansion | Growing or stable | Removing seats or reducing usage | 15 pts |
| Billing contact change | No change | Billing contact replaced | 5 pts |
| Contract status | Active, upcoming renewal confirmed | Renewal not confirmed 60d out | 10 pts |

**Health score tiers:**

| Tier | Score Range | Status | Action |
|---|---|---|---|
| Green | 70-100 | Healthy | Focus on expansion -- upsell, referral, advocacy |
| Yellow | 40-69 | At-risk | Trigger check-in sequence, offer success support |
| Red | 0-39 | High risk | Immediate outreach, executive escalation for high-value |

## Risk Signal Monitoring

Set up automated alerts when any of these signals cross thresholds:

**Immediate alerts (trigger outreach within 24 hours)**
- No login in 14 days (product type dependent -- adjust for lower-frequency tools)
- Support ticket unresolved for 5+ days
- NPS detractor score submitted
- Billing contact changed

**Weekly monitoring triggers**
- Login frequency declined more than 30% week-over-week for two consecutive weeks
- Core feature usage dropped to zero in the past 7 days
- Health score dropped by 20+ points in a single week

**30-day trend alerts**
- No team expansion in a multi-seat product that was previously growing
- Repeated single-session logins (log in, look around, log out -- nothing done)
- No API activity in an API-dependent integration

## Intervention Playbooks

Match the intervention to the health tier and signal type. Escalate effort with score severity.

**Yellow tier -- Email-first intervention**

Sequence triggered automatically when a customer drops to Yellow:
- Day 0: Personal email from Customer Success ("Checking in on your [Brand] experience")
- Day 3: Useful resource relevant to their use case or industry
- Day 7: Direct offer of a 1:1 session ("30 minutes to unlock more from [Brand]")
- Day 14: If no engagement, escalate to Red-tier intervention

See `./frameworks/proactive-retention-emails.md` for email copy outlines.

**Red tier -- Multi-channel intervention**

- Day 0: Personal email from a named CSM or founder (not automated-looking)
- Day 1: Follow-up in-product message or push notification (if available)
- Day 2: Phone or video call attempt for accounts above $500 MRR
- Day 5: Offer a concrete value session (audit their setup, propose improvements)
- Day 10: Senior team escalation for accounts above $2,000 MRR

**Intervention tone principles:**
- Lead with curiosity, not alarm ("I noticed you haven't been in recently -- everything okay?")
- Offer genuine help before mentioning retention or account status
- Give the customer agency -- make it easy to reply "I'm done" without friction
- Track intervention outcomes: how many Yellow accounts return to Green? How many escalate to Red or churn despite intervention?

## Onboarding as Retention Foundation

The highest-leverage retention intervention happens in the first 30 days. Customers who reach the "aha moment" (first meaningful result from the product) in week 1 retain at 2-3x the rate of those who do not.

- Define the single most important activation event for your product (the action most correlated with long-term retention).
- Build onboarding to drive every new customer to that activation event within 7 days.
- Monitor activation rate as a leading indicator of future retention.
- Customers who have not activated by day 14 need immediate human intervention, not more automated emails.

## Deliverable

**Health Score Framework**: `health-scoring-{YYYY-MM-DD}.md`
- Score model
- Signal weights
- Tier thresholds
- Alert setup
- Intervention playbook per tier