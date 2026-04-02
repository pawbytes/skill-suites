# Referral Program Design

Deliver customer referral programs that turn users into acquisition channels with sustainable economics.

## Program Types

| Type | How It Works | Best For |
|---|---|---|
| One-sided | Only the referrer gets a reward | Simple setup, loyalty-focused, low-margin products |
| Two-sided | Both referrer and referred get a reward | Maximum conversion, SaaS, subscriptions, marketplaces |
| Tiered | Rewards increase with number of successful referrals | Power referrers, gamification, community-driven brands |
| Milestone | Rewards unlock at specific thresholds (3, 5, 10 referrals) | Sustained engagement, preventing one-and-done behavior |
| Community | Referrals benefit a shared pool or cause (charity donation, community unlock) | Mission-driven brands, community-first products |

**Default recommendation**: Two-sided for most products. The referred person needs a reason to act, and the referrer needs a reason to share. One-sided programs have 30-50% lower conversion rates on the referred side.

## Incentive Structures

| Incentive | Examples | Best For | Margin Impact |
|---|---|---|---|
| Cash / gift cards | $10 per referral, $25 Visa card | Universal appeal, high-ticket products | Direct cost per acquisition |
| Account credit | $15 credit toward next purchase | Retention + acquisition, recurring products | Lower effective cost (not all credits redeemed) |
| Free months / subscription | 1 month free for both parties | SaaS, subscriptions, memberships | Deferred cost, high perceived value |
| Feature unlocks | Premium features for 30 days, extra storage | Freemium products, feature-gated SaaS | Near-zero marginal cost |
| Physical rewards | Branded merchandise, products, exclusive items | Lifestyle brands, high-engagement communities | Variable cost, high perceived value |
| Tiered / stacked | 1 referral = sticker, 3 = t-shirt, 10 = lifetime access | Gamified programs, power referrers | Scales with referrer value |
| Donation | $5 donated to a charity per referral | Mission-driven brands, socially conscious audiences | Fixed cost, brand alignment |

**Choosing the right incentive**: Match the incentive to the product's economics. If customer lifetime value is $500, a $25 two-sided incentive ($50 total) is a 10% acquisition cost -- strong. If LTV is $30, the same incentive is unsustainable. Rule of thumb: keep total referral cost at 10-25% of LTV.

## Referral Mechanics

**Unique referral links**: Every user gets a personalized link (e.g., `brand.com/ref/username`). Tracked via cookies or server-side. Standard attribution window: 30-90 days. Easiest to implement and share.

**Referral codes**: Unique alphanumeric codes (e.g., SARAH25). Entered at checkout or signup. Works across channels including offline. Pair with a discount for the referred user to increase code usage.

**In-app sharing**: Native share buttons within the product. Pre-written messages for email, SMS, WhatsApp, social. Share at moments of delight (after achievement, after positive experience, after onboarding completion). One-tap sharing reduces friction dramatically.

**Email invites**: Users enter friend email addresses directly. Brand sends the invitation on their behalf. Include personalization from the referrer. Highest intent signal but highest friction.

**QR codes**: Physical referral cards or in-app QR for offline sharing. Useful for retail, events, and local businesses.

## Viral Coefficient Optimization

The viral coefficient (K-factor) determines whether a referral program drives self-sustaining growth.

**K = i x c** where i = invites sent per user, c = conversion rate per invite.

| K-Factor | Meaning | Growth Effect |
|---|---|---|
| Below 0.2 | Weak referral program | Negligible contribution to growth |
| 0.2 - 0.5 | Decent supplement | 20-50% additional growth on top of other channels |
| 0.5 - 1.0 | Strong referral engine | Significant acquisition channel |
| Above 1.0 | Viral growth | Each user generates more than one new user -- exponential |

**Levers to increase K-factor**:
- Increase invites sent: Prompt at the right moment, make sharing effortless, give multiple sharing options, remind users of unclaimed rewards.
- Increase conversion per invite: Stronger incentive for the referred user, personalized landing pages ("Sarah invited you"), social proof on the referral page, reduce signup friction.
- Reduce time-to-invite: Shorten the time between signup and first referral prompt. The faster users reach value, the faster they share.

## Referral Program Page Design

Every referral program needs a dedicated page with:
- **Headline**: Clear value proposition ("Give $20, Get $20" or "Share [Brand] with friends").
- **How it works**: 3 steps, visual, no jargon. Step 1: Share your link. Step 2: Friend signs up. Step 3: You both get rewarded.
- **Unique link or code**: Prominently displayed, one-click copy.
- **Share buttons**: Email, SMS, WhatsApp, Twitter, LinkedIn, Facebook, copy link. Pre-populated messages.
- **Progress tracker**: Referrals sent, pending, completed, rewards earned.
- **Terms**: Clear, concise eligibility rules. What counts as a successful referral.
- **Social proof**: "12,847 people have earned rewards" or testimonials from successful referrers.

## Reference Lookup

For program framework templates and reward calculators:
1. Read `./references/frameworks-index.csv`
2. Match by `name`, `description`, `best_for`, `program_type`, or `tags`
3. Read only the matching file from `./references/frameworks/`

For benchmarks and KPI targets, see `./references/benchmarks.md`.
For evolving best practices, see `./references/best-practices.md`.