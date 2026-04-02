# Abandoned Cart Series

**Goal:** Recover abandoned carts. **Trigger:** Cart created, no purchase within 1 hour. **Emails:** 3 over 72 hours.

### Email 1: Gentle Reminder (1 hour)
- **Subjects:** "You left something behind, [Name]" | "Your cart is waiting for you" | "Did something go wrong?"
- **Elements:** Cart contents with product images/names/prices, NO discount yet, checkout help offer, trust signals (security badge, return policy, payment options)
- **CTA:** "Complete your order" (single prominent button)

### Email 2: Social Proof + Urgency (24 hours)
- **Subjects:** "[Product name] is selling fast" | "Other shoppers are eyeing your cart"
- **Elements:** Cart contents again, 1-2 product reviews, scarcity ("Only [X] left" if true), small incentive (free shipping or 5-10% off), FAQ on top objections
- **CTA:** "Return to your cart"

### Email 3: Final Push + Incentive (72 hours)
- **Subjects:** "Last chance: [X]% off your cart" | "A little something to help you decide"
- **Elements:** Cart contents, strongest incentive (10-15% off or free shipping), deadline on incentive (48hr), loss aversion ("We'll release reserved items"), one-click checkout
- **CTA:** "Complete your order and save [X]%"

### Branching Logic
- Purchases after any email --> stop sequence; enter post-purchase flow
- Clicks Email 2 but no purchase --> trigger Email 3 sooner (48hr)
- Cart value above $150 --> higher discount or personal outreach
- Repeat customer --> skip discount, use loyalty language
- No action after Email 3 --> wait 7 days, move to re-engagement segment
