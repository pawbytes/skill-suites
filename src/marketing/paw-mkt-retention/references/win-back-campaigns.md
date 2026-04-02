# Win-Back Campaigns Capability

Not every churned customer is lost permanently. Customers leave for reasons that change: the budget frees up, the competitor disappoints, their business grows into your product again. A structured win-back programme captures this re-engagement.

## Win-Back Segmentation

Do not send the same win-back message to all churned customers. Segment first.

| Segment | Criteria | Approach |
|---|---|---|
| High-value churned | MRR above $200, churned in last 90 days | Personal outreach, strong offer, senior team |
| Price-sensitive | Cancelled "too expensive" | Pricing change announcement, lower plan, deal |
| Feature-driven | Cancelled "missing feature" | Feature launch announcement when the feature ships |
| Disengaged | Low usage before churn, no exit survey response | Re-education, new use case, proof of value |
| Involuntary recovered | Failed payment, account lapsed without intent | Simple reactivation email, no offer needed |
| Long-lapsed (90d+) | Churned more than 90 days ago | Product update angle, major change message |

## Win-Back Email Sequence (3-email core)

**Timing**: First win-back email goes out 7-14 days post-cancellation. Sending sooner feels desperate. Sending later misses the window when the brand is still top of mind.

| Email | Timing | Focus | CTA |
|---|---|---|---|
| Email 1 | 7-14 days post-cancel | Warm check-in + what changed | "Take another look" |
| Email 2 | 21-30 days post-cancel | Specific value proof + offer | "Come back + incentive" |
| Email 3 | 45-60 days post-cancel | Last-chance, feature announcement, or news | "Reactivate with [X]" |

For high-value churned customers, add a fourth personal outreach (phone or video) between Email 2 and Email 3.

See `./frameworks/win-back-email-sequence.md` for full email copy outlines.

## Win-Back Offers

| Offer Type | Best For | Duration |
|---|---|---|
| X months free | Disengaged churners, show value again | 1-2 months |
| Discount for Y months | Price-sensitive churners | 3-6 months, then full price |
| Upgraded plan at current plan price | Feature-driven churners | 3 months trial |
| No offer, just news | Involuntary churners, high-trust segments | N/A |
| Product credit | E-commerce subscription, physical product | One-time credit |

**Escalating offers**: Start without a discount in Email 1. Add an offer in Email 2. Strengthen or change the offer type in Email 3. Avoid leading with maximum incentive -- it trains customers to churn to get deals.

## Win-Back Triggers (Non-Time-Based)

Beyond the standard time-based sequence, trigger win-back outreach on specific events:

- **Feature launch**: Email all churned customers who cited "missing feature X" as their reason, when feature X ships. Include a changelog link and direct reactivation CTA.
- **Pricing change**: Email churned customers who cited "too expensive" when pricing drops or a lower plan tier launches.
- **Major product update**: Annual-style "Here's what's new" email to all churned customers on the product anniversary or after a major version launch.
- **Competitor news** (negative): If a major competitor has an outage, price hike, or acquisition, reach out with a timely "The timing might be right" message.

## Win-Back Benchmarks

| Metric | Target |
|---|---|
| Win-back rate (0-90 days churned) | 10-15% |
| Win-back rate (90-180 days churned) | 3-8% |
| Win-back LTV vs new customer LTV | Win-back customers retain 20-30% longer (they know the product) |
| Win-back email open rate | 25-35% (brand familiarity effect) |
| Offer acceptance rate | 15-25% of those who open |

## Deliverable

**Win-Back Campaign**: `winback-campaign-{YYYY-MM-DD}.md`
- Segment definitions
- Email sequence (3-4 emails)
- Offer strategy
- Event-based trigger plan