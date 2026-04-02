# Payment Recovery and Dunning Capability

Involuntary churn is the most recoverable form of churn because the customer did not intend to leave. A well-designed dunning sequence can recover 50-60% of failed transactions. Act immediately -- recovery rates drop sharply with each passing day.

## Understanding Payment Failure Types

| Failure Type | Cause | Recovery Approach |
|---|---|---|
| Soft decline | Temporary: insufficient funds, daily limit, bank hold | Retry at different times; notify customer |
| Hard decline | Permanent: card number invalid, account closed, blocked | Immediate customer notification required |
| Expired card | Card passed expiration date | Proactive card updater service |
| 3DS/authentication failure | Strong Customer Authentication required (EU/UK) | Send authentication link to customer |

**Card Updater (Account Updater)**: Stripe, Braintree, and most payment processors offer a service that automatically updates expired or replaced card details with the issuing bank. Enable this. It silently recovers a significant portion of involuntary churn before the customer even knows there was a problem.

## Smart Retry Logic

Do not retry immediately on failure -- it often results in another decline and damages your success rate with the card network.

**Smart retry rules:**
- Soft decline (insufficient funds): retry after 24-48 hours, then 72 hours
- Soft decline at end of month: retry on the 1st-2nd of the following month (paycheck timing)
- Hard decline: do not retry; notify the customer immediately
- Timing: avoid retries at midnight. Retry during business hours in the customer's timezone
- Maximum retries: 4-6 total before moving to manual recovery

Tools like Stripe Billing's Smart Retries, Chargebee's Receivables, or Recurly's Intelligent Retries use machine-learning optimised retry timing. Enable them. They outperform fixed-schedule retry logic significantly.

## Dunning Email Sequence

The dunning sequence runs in parallel with Smart Retry logic. Each email should sound human, not like a system alert.

**Full sequence: Days 0-21**

| Day | Trigger | Tone | Primary CTA |
|---|---|---|---|
| Day 0 | Payment fails | Soft, helpful | Update payment method |
| Day 1 | No update | Friendly, direct | Update payment details |
| Day 3 | No update | More direct | Update now (link) |
| Day 7 | No update | Urgent | Save your account |
| Day 14 | No update | Final warning | Last chance to update |
| Day 21 | Grace period expires | Neutral, confirmatory | Reactivate if cancelled |

Full email body copy and subject lines for all 6 emails are in `./frameworks/dunning-email-sequence.md`.

**High-value account escalation:**
- Accounts above $500 MRR: add phone or chat outreach at Day 7
- Accounts above $2,000 MRR: personal call from account manager at Day 3
- Accounts above $5,000 MRR: executive reach-out, immediate escalation

## Account Grace Period Design

Define what happens when payment fails and the dunning sequence runs its course:

| Day | Account Status |
|---|---|
| Day 0-6 | Full access, soft notification |
| Day 7-13 | Full access, prominent in-app banner |
| Day 14-20 | Read-only access or feature degradation (data preserved) |
| Day 21 | Downgrade to free tier or cancellation, data retained for 90 days |

**Data retention**: Always retain customer data for a minimum of 30-90 days post-cancellation. The ability to reactivate without losing their work is a significant reactivation incentive. Communicate this explicitly: "Your data is safe and waiting for you."

## Payment Recovery Benchmarks

| Metric | Target | Notes |
|---|---|---|
| Smart Retry recovery rate | 15-25% of failed payments | Recovered without customer action |
| Card Updater recovery rate | 5-15% | Silent background recovery |
| Dunning email recovery rate | 30-40% of remaining failures | After retry and updater |
| Total involuntary churn recovery | 50-60% of all failed payments | Combined methods |
| Recovery rate by Day 7 | 70% of eventual recoveries happen within 7 days | Front-load communication urgency |

## Deliverable

**Dunning Sequence**: `dunning-sequence-{YYYY-MM-DD}.md`
- Retry logic
- Email sequence (all 6 emails)
- Grace period policy
- High-value escalation steps