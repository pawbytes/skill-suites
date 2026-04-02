# Value Metric Selection

> The value metric is what you charge for. It is one of the highest-leverage pricing decisions. The right metric aligns revenue growth with customer value growth.

---

## 1. Value Metric Options

| Metric | How it Works | Best Fit | Examples |
|---|---|---|---|
| Per user / seat | Price scales with number of users | Each user gets distinct value independently | Slack, Notion, Salesforce, Figma |
| Usage-based | Price scales with consumption | Value correlates with usage volume | Stripe (% of transactions), Twilio (per message), AWS (per GB) |
| Outcome-based | Charge % of value delivered | Clear, measurable outcome; high-trust relationship | Hiring platforms (% of salary), some agencies |
| Flat fee | One price for all | Single persona, simple product, easy to buy | Simple tools, one-size-fits-all software |
| Hybrid: base + usage | Flat base + overage charges | Predictability for customer + upside for you | Most modern SaaS |
| Per contact / record | Scales with database size | CRM, email tools where value = data volume | HubSpot (contacts), Mailchimp (subscribers) |
| Per API call / event | Developer-facing, consumption priced | Infrastructure, data, API products | Segment, Clearbit, OpenAI |

---

## 2. Choosing the Right Metric

A good value metric must pass three tests:

1. **Correlation test**: Does the customer's value increase as they use more of this metric? If yes, valid metric.
2. **Expansion test**: As the customer grows and succeeds, do they naturally consume more of this metric? Expansion revenue depends on this.
3. **Comprehension test**: Can the customer easily predict their bill and understand why they are charged what they are? Unpredictable billing creates churn.

**Common mistakes in metric selection**:
- Charging per user when users are consumers (not producers) of value—leads to license sharing.
- Usage-based pricing when the product is hard to predict—customers cap usage to control costs, limiting growth.
- Flat fee when the product serves radically different customer sizes—undercharge enterprise, overcharge SMB.

---

## 3. Expansion Revenue Design

The best pricing structures have built-in expansion logic: customers who succeed naturally pay more without requiring a sales conversation.

- **Usage-based**: expand automatically as volume grows.
- **Seat-based**: add users as team grows.
- **Feature-gating**: customers upgrade when they hit a limit they value.

Design tier limits so the most valuable customers naturally bump against them.

---

## 4. Psychological Pricing Principles

### 4.1 Charm Pricing

Prices ending in 9 ($49, $99, $199) outperform round numbers in most contexts. Exception: luxury/premium positioning where round numbers ($50, $100, $200) signal confidence.

### 4.2 Anchoring

Lead with the highest price first (either enterprise tier or annual plan) to set the anchor. Everything after looks cheaper by comparison.

### 4.3 Price-Quality Signal

In premium markets, higher price communicates higher quality. Do not undercut if positioning as best-in-class.

### 4.4 Monthly vs Annual Display

Show annual price as monthly equivalent ("$83/mo, billed annually") to reduce sticker shock while capturing annual commitment.

---

## 5. Annual vs Monthly Pricing

Offer both. Annual discount range: 15-25% is standard; below 15% and customers do not bother; above 33% and customers question why monthly is so expensive.

| Factor | Monthly Billing | Annual Billing |
|---|---|---|
| Customer preference | Lower commitment barrier | Cost savings, budget-friendly (one invoice) |
| Business benefit | Higher monthly cash flow | Lower churn, upfront cash, predictable ARR |
| Typical split | 30-40% of customers | 60-70% of customers (for established SaaS) |

Default the pricing page toggle to annual. Show "Save X%" prominently. Calculate exact dollar savings in CTA context.

---

## 6. Benchmarking to Competitive Alternatives

Build a comparison table before setting price points:

| Alternative | Monthly Cost | Key Limitation | Your Advantage |
|---|---|---|---|
| Competitor A | $X/mo | [specific limitation] | [specific advantage] |
| Competitor B | $X/mo | [specific limitation] | [specific advantage] |
| Manual process (spreadsheets, etc.) | [time cost in $] | [friction, error rate] | [specific advantage] |
| DIY / hiring someone | [$X freelancer rate] | [inconsistency, overhead] | [specific advantage] |

Price above the alternatives you beat, below the alternatives you do not.