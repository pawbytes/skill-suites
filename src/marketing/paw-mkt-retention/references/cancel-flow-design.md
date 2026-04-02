# Cancel Flow Design Capability

A well-designed cancel flow saves 25-35% of customers who intend to cancel. It is not manipulation -- it is giving the customer information, options, and offers they may genuinely want before making a permanent decision.

## Cancel Flow Architecture

```
Cancel button --> [Pause Gate] --> [Exit Survey (4-6 reasons)] --> [Dynamic Offer (reason-matched)]
  --> Accept: confirm save, update billing/plan
  --> Decline: [Confirmation Page] graceful exit (data export, community, support)
  --> [Post-Cancel Sequence] win-back emails start
```

See `./frameworks/cancel-confirmation-copy.md` for full confirmation page copy and post-cancel email.
See `./frameworks/offer-decision-tree.md` for the offer decision tree.

## Exit Survey Design

**Principles:**
- Show 4-6 options maximum. More than 6 creates survey fatigue and reduces data quality.
- Include "Other" with an optional text field as the final option.
- Do not make the survey mandatory -- if a customer skips it, let them cancel. Forcing engagement creates resentment.
- Make options honest and non-judgmental. Customers notice when options are designed to manipulate.
- Use the survey data. If you collect it and nothing changes, it is performative.

**Recommended options (adapt copy to match brand voice):**

| # | Reason Label | Data Use |
|---|---|---|
| 1 | It's too expensive | Trigger discount or pause offer |
| 2 | I'm not using it enough | Trigger usage coaching + pause offer |
| 3 | It's missing a feature I need | Trigger roadmap acknowledgment |
| 4 | I'm switching to a competitor | Trigger differentiation + comparison |
| 5 | I had a technical issue | Trigger immediate support escalation |
| 6 | Something else | Route to text field + general offer |

See `./frameworks/exit-survey-copy.md` for exact microcopy for each option.

## Dynamic Offer Logic

Match the intervention precisely to the stated reason. Generic offers applied to all cancellation reasons perform significantly worse than targeted offers.

| Reason | Primary Offer | Secondary Option |
|---|---|---|
| Too expensive | 20-30% discount for 3 months or a permanent plan downgrade | Pause for 1-3 months |
| Not using it enough | Free 1:1 onboarding session + pause option | Usage tips + resource hub |
| Missing feature | Acknowledge the gap, share roadmap timeline if honest, offer workaround | Pause until feature ships |
| Switching to competitor | Direct feature comparison, differentiation statement, case study | One-month free to reconsider |
| Technical issue | Immediate escalation to senior support + account credit | Free extension while issue resolves |
| Other | Manager callback offer or open-ended "What would keep you?" | General discount or pause |

**Offer hierarchy by value:**
1. Pause (costs nothing, preserves the relationship, buys time)
2. Downgrade (reduces revenue but retains customer)
3. Time-limited discount (3-month incentive with full price resuming)
4. Free extension (1 month free, delays cancel 30 days)
5. Feature access (unlock higher plan feature at current price)

**Critical rule:** Show the single best-matched offer for the stated reason rather than all offers at once -- multiple simultaneous offers reduce acceptance rates and train customers to hunt for deals. Exception: if the cancel reason is ambiguous, a choice of two options (e.g., pause vs. downgrade) can outperform a single guess.

## Save Rate Benchmarks

| Metric | Target | Best-in-Class |
|---|---|---|
| Cancel flow impression rate | 80%+ of cancellers see the flow | 90%+ |
| Survey completion rate | 60-70% of impressions | 75%+ |
| Save rate (all methods) | 25-35% of intending cancellers | 35-45% |
| Offer acceptance rate | 15-25% of offer impressions | 25-35% |
| Pause adoption rate (where offered) | 10-20% | 20-30% |

## Cancel Flow Tools

| Tool | Best For | Pricing Signal |
|---|---|---|
| **Churnkey** | SaaS, full cancel flow + dunning, smart offers | Mid-market |
| **ProsperStack** | SaaS, high customisation, A/B testing | Mid-market |
| **Chargebee Retention** | Chargebee billing users, native integration | Enterprise |
| **Custom-built** | Full control, requires engineering resources | Any |
| **Stripe Portal** | Basic only, no dynamic offer logic | Free with Stripe |

For brands on Stripe without a dedicated cancel flow tool, Churnkey integrates directly and adds the offer logic layer. For brands on Chargebee or Recurly, use their native retention modules first.

## Cancel Flow Copy and UX Principles

- **Never use dark patterns.** Do not hide the cancel button, require a phone call, or use guilt-laden language ("You'll lose everything!"). These destroy trust and generate public complaints.
- **Tone: helpful, not desperate.** The cancel flow is a customer service interaction, not a negotiation.
- **Mobile-first.** A significant share of cancellations happen on mobile. Test the full flow on a phone.
- **One screen per step.** Do not combine the exit survey and the offer on the same screen.
- **Respect the decision.** If they decline the offer, complete the cancellation immediately. Do not add additional friction screens.

## Deliverable

**Cancel Flow Design**: `cancel-flow-{YYYY-MM-DD}.md`
- Architecture diagram
- Exit survey copy
- Offer decision tree
- Confirmation page copy
- Tool recommendation