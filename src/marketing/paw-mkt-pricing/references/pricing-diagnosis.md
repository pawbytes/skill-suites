# Pricing Diagnosis

> Classify the pricing problem type before recommending solutions. Different symptoms require different fixes.

---

## 1. Identify the Pricing Problem

Ask the user: **"What triggered this pricing conversation?"** Then map to a problem type:

| Symptom | Problem Type | Primary Fix |
|---|---|---|
| Deals stalling on price, losing to competitors | Price point too high vs perceived value | Value communication, not necessarily price cuts |
| High trial-to-paid drop-off | Wrong value metric or wrong tier structure | Value metric and packaging audit |
| Low average contract value (ACV) | Under-extracting value from best customers | Tier restructuring, usage-based expansion |
| Churn spike after price increase | Poor change communication or bad timing | Price increase strategy |
| "You should have a cheaper option" | Missing entry tier or wrong audience | Tier addition or audience refocus |
| Customers maxing out the top tier | Pricing ceiling too low | Enterprise tier or usage overage design |
| Everyone choosing the cheapest tier | Middle tier not differentiated enough | Packaging and decoy redesign |
| Pricing page confusion, low conversion | Page design and copy problem | Pricing page redesign |

---

## 2. Pricing Audit Questions

Before building recommendations, gather answers to:

1. What is the current pricing structure? (tiers, price points, value metric)
2. What percentage of customers are on each tier?
3. What is the current MRR/ARR and average contract value (ACV)?
4. What is the trial-to-paid conversion rate?
5. What is the monthly churn rate by tier?
6. Who are the top 3-5 direct competitors and what do they charge?
7. Has any pricing research (surveys, interviews, win/loss analysis) been done?
8. When was the last price change and what happened to conversion and churn?
9. What segment does the brand primarily serve: SMB, mid-market, or enterprise?
10. Is pricing self-serve, sales-assisted, or sales-led?

---

## 3. Value-Based Pricing Foundation

### 3.1 The Floor-Ceiling Model

Pricing exists on a spectrum between two boundaries:

```
[Floor]                                              [Ceiling]
Next best alternative cost          Customer perceived value (max WTP)
         |_______________________________________________|
                      Acceptable Price Range
                              ^
                          Sweet spot
                    (closer to ceiling for
                      premium positioning)
```

- **Floor**: What the customer currently pays for the problem (spreadsheets, a cheaper tool, a manual process, a freelancer). The floor is not your cost to serve—cost-plus pricing leaves money on the table.
- **Ceiling**: The maximum the customer would pay before the pain of cost outweighs the value. Determined by willingness-to-pay research.
- **Sweet spot**: Price between floor and ceiling. For premium brands, price closer to the ceiling. For volume plays, price closer to the floor.

### 3.2 Cost-Plus vs Value-Based Pricing

**Cost-plus** (avoid): Take cost to serve, add margin percentage, arrive at price. Ignores what the customer is willing to pay. In software, COGS is near-zero but value is high. Systematically underprices.

**Value-based** (use): Start from value delivered, work backwards to price that captures a fraction of that value.
- Example: If tool saves $50,000/year in labor, charging $5,000/year captures 10% of value—excellent deal for customer, strong business for you.

### 3.3 Competitive Anchoring

Pricing signals quality. Use competitive prices as anchors, not as ceilings.

- If you price significantly below competitors, customers assume lower quality (even if you are better).
- If you price above competitors, you must justify premium with visible differentiation.
- Undifferentiated products compete on price. Differentiated products command premiums.

Determine which quadrant the brand occupies:

| | Lower Price | Higher Price |
|---|---|---|
| **Higher Quality/Value** | Value disruptor (grow fast, monetize later) | Premium positioning (target) |
| **Lower Quality/Value** | Budget tier (low margin, high volume) | Avoid this quadrant |

---

## 4. Common Pricing Mistakes

| Mistake | Why It Happens | Fix |
|---|---|---|
| Underpricing (most common) | Founders price based on cost, not value; fear of losing deals | Run Van Westendorp research; compare to next best alternative cost |
| Too many tiers (4+) | Trying to serve everyone | Collapse to 3 tiers; use add-ons for edge cases |
| Wrong value metric | Copying competitors without validating fit | Test correlation: does customer value scale with the metric? |
| Fully opaque pricing | Fear of self-service, preference for sales control | Drives away self-serve buyers; publish at least starting prices |
| Identical features across tiers | Lazy packaging | Gate on value metric + power features; tiers must have clear identity |
| Annual discount too high (>33%) | Short-term cash grab | Signals monthly is overpriced; cap annual discount at 25% |
| No expansion mechanism | Set-and-forget pricing | Design usage limits or feature gates that trigger upgrades |
| Pricing page feature list too long | More features = more value (wrong) | More features = more confusion; limit to 5-8 per tier |
| Never raising prices | Fear of churn | Costs trust and revenue; small annual increases are expected |
| Same price globally | Ignoring purchasing power parity | Offer regional pricing (PPP) for high-growth emerging markets |

---

## 5. Ethics: Persuasion Without Manipulation

Pricing psychology relies on cognitive biases—anchoring, decoy effects, charm pricing, loss framing. These techniques influence perception and can cross into manipulation.

### 5.1 Ethical Pricing Practices

- **Genuine anchoring**: Original prices were actually offered. Competitor comparisons are accurate. Problem cost anchors are verifiable.
- **Honest tier differentiation**: Each tier genuinely serves the customer type described. Feature gates exist because they create value for the target segment—not to force upgrades.
- **Transparent pricing**: Prices visible before signup. No hidden fees. Trial terms clear. Add-on costs disclosed upfront.
- **Fair expansion**: Usage-based pricing correlates with customer value. Overage charges predictable. Customers can monitor spend.
- **Honest discounts**: "Save $X" calculated from genuine original price. Annual discounts represent real savings.
- **Clear cancellation**: Easy to cancel, no dark patterns. Customers know what they're buying.

### 5.2 Dark Patterns to Avoid

| Pattern | Description | Why It Harms |
|---|---|---|
| Fake anchors | "Was $999" when price never actually charged | Deceptive; FTC enforcement risk |
| Hidden add-ons | Core features require expensive add-ons not shown until checkout | Churn, chargebacks, trust destruction |
| Drip pricing | Base price displayed, mandatory fees added at checkout | Regulatory violations |
| Confusing tiers | Deliberately complex packaging to prevent comparison | Decision paralysis, buyer's remorse |
| False scarcity | "Only 5 spots at this price" when price never changes | Trust destruction when discovered |
| Hidden auto-renewal | Annual renewal charged without clear disclosure | Chargebacks, regulatory risk |
| Cancellation friction | Multiple steps, guilt language, obstacles to cancel | Reputation damage, regulatory risk |

### 5.3 The Ethical Test

Before implementing any pricing technique, ask: **If the customer understood exactly how the pricing was structured, would they still feel it was fair?** If no, redesign the pricing.

---

## Deliverables

| Deliverable | Filename | Key Sections |
|---|---|---|
| Pricing Strategy | `pricing-strategy-{YYYY-MM-DD}.md` | Diagnosis, value metric, tier structure, rationale, research summary, competitive positioning |
| Competitive Pricing Analysis | `pricing-competitive-analysis-{YYYY-MM-DD}.md` | Competitor tier comparison, value metric comparison, price positioning map, gaps and opportunities |