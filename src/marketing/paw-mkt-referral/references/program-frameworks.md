# Referral Program Frameworks & Templates

> Ready-to-use frameworks, templates, checklists, and planning tools for launching and optimizing referral programs, affiliate programs, and partner marketing.

---

## 1. Referral Program Launch Checklist (30-Day Plan)

### Week 1: Foundation (Days 1-7)

- [ ] **Define program economics**
  - Calculate customer LTV (12-month and 24-month)
  - Determine maximum affordable cost per acquisition (target: 10-25% of LTV)
  - Set referral incentive amounts for both sides (referrer + referred)
  - Model breakeven at various participation rates (2%, 5%, 10%)
- [ ] **Choose program type**
  - One-sided vs. two-sided vs. tiered vs. milestone
  - Incentive type: cash, credit, feature unlock, subscription, merchandise
  - Attribution method: unique link, referral code, in-app invite, email invite
- [ ] **Select technology**
  - Evaluate referral platforms (ReferralCandy, GrowSurf, Viral Loops, Rewardful, FirstPromoter, or custom-built)
  - Confirm integration with payment processor, CRM, and email platform
  - Set up test environment
- [ ] **Draft program terms**
  - Eligibility rules (who can refer, who can be referred)
  - What counts as a successful referral (signup, purchase, subscription)
  - Reward fulfillment timeline
  - Fraud policy and prohibited activities
  - Program modification and termination rights

### Week 2: Build (Days 8-14)

- [ ] **Create referral program page**
  - Headline: clear value proposition ("Give $X, Get $X")
  - How-it-works section: 3 visual steps
  - Unique link/code display with one-click copy
  - Share buttons: email, SMS, WhatsApp, Twitter/X, LinkedIn, Facebook, copy link
  - Progress tracker: referrals sent, pending, completed, rewards earned
  - Social proof element
  - Terms link
- [ ] **Build referral landing page** (where referred users land)
  - Personalized headline ("Sarah invited you to try [Brand]")
  - Clear incentive display for the referred user
  - Social proof (ratings, user count, testimonials)
  - Simplified signup/purchase flow (reduce friction)
  - Mobile-optimized design
- [ ] **Set up tracking and attribution**
  - Server-side conversion tracking (primary)
  - First-party cookie tracking (fallback)
  - UTM parameters: `utm_source=referral&utm_medium=link&utm_campaign={program}&utm_content={referrer_id}`
  - CRM integration for lifetime referral attribution
  - End-to-end testing of tracking flow
- [ ] **Prepare share content**
  - Pre-written email invite copy (3 variations)
  - Pre-written SMS/WhatsApp message (2 variations)
  - Social media share copy per platform (Twitter/X, LinkedIn, Facebook)
  - Share images/OG images for social previews

### Week 3: Soft Launch (Days 15-21)

- [ ] **Beta test with 50-100 loyal customers**
  - Invite top NPS scorers or most engaged users
  - Collect feedback on flow, clarity, and incentive appeal
  - Monitor for technical issues in tracking and reward delivery
  - A/B test 2 headline variations on the referral page
- [ ] **Set up automated triggers**
  - Post-purchase referral prompt (email, 24-48 hours after purchase)
  - NPS-triggered referral request (for Promoters scoring 9-10)
  - In-app referral prompt at value moments
  - Referral reminder email (7 days after first invite sent, if no conversion)
  - Reward notification email (instant, upon successful referral)
  - Thank-you email to both referrer and referred
- [ ] **Configure reporting dashboard**
  - Referral rate (referrers / total active customers)
  - Invites sent per referrer
  - Invite-to-signup conversion rate
  - Signup-to-purchase conversion rate
  - K-factor (invites per user x conversion per invite)
  - Referral CAC vs. other channels
  - Reward costs and program ROI

### Week 4: Public Launch (Days 22-30)

- [ ] **Announce program to full customer base**
  - Dedicated launch email to all customers
  - In-app announcement banner or modal
  - Social media announcement posts
  - Blog post explaining the program
  - Homepage or navigation link to referral page
- [ ] **Activate ongoing promotion**
  - Add referral CTA to post-purchase confirmation page
  - Add referral link to email signature/footer
  - Add referral prompt to account dashboard
  - Schedule monthly referral reminder emails
- [ ] **Establish optimization cadence**
  - Weekly: review core metrics, check for tracking issues
  - Bi-weekly: analyze conversion funnel, identify dropoff points
  - Monthly: A/B test one element (incentive, copy, timing, channel)
  - Quarterly: full program review, ROI analysis, incentive recalibration

---

## 2. Incentive Calculator Framework

### Step 1: Determine Maximum Referral Budget

```
Customer Lifetime Value (LTV)     = $________
Target Referral CAC (% of LTV)    = ________% (recommend 10-25%)
Maximum Total Referral Cost        = LTV x Target %
                                   = $________
```

### Step 2: Allocate Between Referrer and Referred

```
Total referral budget per referral = $________

Option A: Equal split
  Referrer reward  = $________ (50% of total)
  Referred reward  = $________ (50% of total)

Option B: Referred-heavy (higher conversion)
  Referrer reward  = $________ (40% of total)
  Referred reward  = $________ (60% of total)

Option C: Referrer-heavy (more sharing)
  Referrer reward  = $________ (60% of total)
  Referred reward  = $________ (40% of total)
```

### Step 3: Validate Against Margins

```
Average order value (AOV) or monthly price  = $________
Gross margin                                = ________%
Gross profit per customer                   = $________
Total referral cost                         = $________
Referral cost as % of gross profit          = ________%

Target: referral cost should be < 30% of gross profit on first transaction
For subscription: payback within 3-6 months of recurring revenue
```

### Step 4: Model Program Economics

```
Assumptions:
  Active customers                      = ________
  Expected participation rate           = ________% (start with 3-5%)
  Expected referrers                    = ________
  Average invites per referrer          = ________ (estimate 2-5)
  Invite-to-signup conversion rate      = ________% (estimate 10-20%)
  Signup-to-purchase conversion rate    = ________% (estimate 25-50%)

Projected results:
  Total invites sent                    = referrers x avg invites
  New signups from referrals            = invites x invite conversion %
  New paying customers from referrals   = signups x purchase conversion %
  Total referral reward cost            = new customers x total reward
  Revenue from referred customers       = new customers x AOV (or annual value)
  Program ROI                           = (revenue - cost) / cost x 100
```

---

## 3. Referral Email Templates

### Template 1: Referral Invitation Email (Sent by Brand on Behalf of Referrer)

```
Subject: {referrer_name} thinks you'd love {brand_name}

Hi {referred_name},

Your friend {referrer_name} thought you'd enjoy {brand_name} — and they
wanted to share something special with you.

Here's {incentive_amount} off your first {purchase/month/order} as a thank you
for giving us a try.

[Claim Your {incentive_amount} Reward →]

{One-sentence description of what the product does and why people love it.}

{social_proof: "Trusted by X customers" or "Rated 4.8/5 by X reviewers"}

Your unique link: {referral_link}
This offer expires in {expiry_period}.

Questions? Just reply to this email.
```

### Template 2: Referral Reminder (7 Days After Invite, No Conversion)

```
Subject: Don't forget — you've got {incentive_amount} to share

Hi {referrer_name},

You shared {brand_name} with {number} friend(s) last week, but they haven't
claimed their reward yet.

Sometimes people just need a little nudge. Here's your referral link to share
again:

{referral_link}

Remember: when they sign up, you both get {reward_description}.

Quick sharing options:
[Email] [Text] [WhatsApp] [Copy Link]

Your referral stats:
  Invites sent: {count}
  Pending: {count}
  Rewards earned: {count} ({total_value})
```

### Template 3: Reward Notification (Referral Successful)

```
Subject: 🎉 You earned {reward_amount}! {referred_name} just signed up.

Hi {referrer_name},

Great news! {referred_name} just {completed_action} using your referral,
and your {reward_amount} {reward_type} has been applied to your account.

Your referral stats:
  Total referrals: {count}
  Total earned: {total_value}
  {Progress to next tier: X more referrals to unlock {next_tier_reward}}

Keep sharing and earn more:
{referral_link}

[Share Again →]
```

### Template 4: Thank You to Referred Customer

```
Subject: Welcome to {brand_name} — here's your {incentive_amount}

Hi {referred_name},

Welcome! {referrer_name} thought you'd love us, and we're glad you're here.

Your {incentive_amount} {reward_type} has been applied to your account
and is ready to use.

Here's how to get started:
1. {First action step}
2. {Second action step}
3. {Third action step}

And once you're loving {brand_name}, you can share it too and earn
{referrer_reward} for every friend who joins:
{new_referral_link}

Questions? Reply to this email anytime.
```

### Template 5: Monthly Referral Program Digest

```
Subject: Your referral recap for {month} + a special boost

Hi {referrer_name},

Here's your {month} referral summary:

  Invites sent this month: {count}
  New referrals this month: {count}
  Rewards earned this month: {value}
  Lifetime referrals: {total_count}
  Lifetime rewards: {total_value}

{If applicable: "You're just {X} referrals away from {next_tier}!"}

{Optional: time-limited boost announcement}
This week only: earn DOUBLE rewards for every referral.
Regular reward: {amount} → Boosted reward: {2x_amount}

[Share Now →]
```

---

## 4. In-App Referral Prompt Copy Templates

### Post-Purchase Prompt
```
Enjoying {brand_name}?
Share with a friend and you'll both get {reward}.
[Share Now]  [Maybe Later]
```

### Milestone Achievement Prompt
```
Congrats on {milestone}! 🎉
Know someone who'd love this too?
Give them {referred_reward} and get {referrer_reward}.
[Invite a Friend]  [Dismiss]
```

### NPS Follow-Up (Score 9-10)
```
Thanks for the amazing rating!
Would you recommend us to a friend?
Share your link and you'll both get {reward}.
[Share My Link]  [Not Now]
```

### Feature Discovery Prompt
```
Love this feature?
Your friends will too.
Share {brand_name} and earn {reward} for each friend who joins.
[Share]  [Later]
```

### Account Dashboard Widget
```
┌─────────────────────────────────────────┐
│  Your Referrals                         │
│  Referrals: {count}  |  Earned: {value} │
│  {progress_bar} {X} more to {next_tier} │
│                                         │
│  Your link: {referral_link} [Copy]      │
│  [Email] [Text] [WhatsApp] [Twitter]    │
└─────────────────────────────────────────┘
```

---

## 5. Affiliate Onboarding Sequence

### Day 0: Welcome & Access

```
Subject: Welcome to the {brand_name} affiliate program!

Hi {affiliate_name},

You're approved! Here's everything you need to start earning:

Dashboard: {dashboard_url}
Your unique tracking link: {tracking_link}
Commission: {rate} per {sale/signup/month}
Cookie window: {duration}
Payment: {schedule} via {method}

Quick-start guide attached: "Earn Your First Commission in 15 Minutes"

Your affiliate manager: {name} ({email})
```

### Day 1: Creative Assets

```
Subject: Your creative toolkit is ready

Hi {affiliate_name},

Your affiliate asset library is loaded and ready:

📊 Banner ads: {count} designs in all standard sizes
📧 Email templates: {count} proven templates with merge fields
📱 Social copy: Platform-specific posts for {platforms}
🎬 Video clips: Product demos and testimonial clips
📄 Comparison content: vs competitor templates
🖼️ Product images: High-res lifestyle and product shots

Access everything: {asset_library_url}

Top-converting content angle: {description of what works best}
```

### Day 3: Quick-Start Guide

```
Subject: 3 proven ways to earn your first commission

Hi {affiliate_name},

Here are the 3 fastest paths to your first commission:

1. Share your link in a relevant community post or forum answer
   (avg conversion: {rate}%)

2. Write a quick review or comparison post
   (template attached — fill in 20 minutes)

3. Send to your email list with our pre-written template
   (avg conversion: {rate}%)

Your link: {tracking_link}

Pro tip: {specific optimization advice for their content type}
```

### Day 7: Check-In & Tips

```
Subject: How's it going? + tips from top earners

Your stats so far:
  Clicks: {count}
  Conversions: {count}
  Earnings: {amount}

Tips from our top affiliates:
  1. {Tip from top performer}
  2. {Tip from top performer}
  3. {Tip from top performer}

Need help? Book 15 minutes with your affiliate manager: {calendar_link}
```

### Day 14: Performance Review

```
Subject: Your 2-week performance review + optimization ideas

Your 14-day stats:
  Clicks: {count}
  Conversions: {count}
  Conversion rate: {rate}%
  Earnings: {amount}
  EPC: ${amount}

Based on your performance, here are personalized suggestions:
  {If low clicks: "Try promoting in {specific channel}"}
  {If low conversion: "Try our highest-converting landing page: {url}"}
  {If good performance: "You're on track for our {tier} bonus at {threshold}"}
```

### Day 30: Community & Growth

```
Subject: Join our affiliate community + your first month recap

Your first month results:
  Total clicks: {count}
  Total conversions: {count}
  Total earnings: {amount}

Join our affiliate community:
  {Slack/Discord invite link}
  Connect with {count} other affiliates
  Share strategies, get answers, and learn what's working

Upcoming: {seasonal promotion or new product launch affiliate opportunity}
```

---

## 6. Partner Program Tier Structure

### Tier Definitions

| Element | Registered | Silver | Gold | Platinum |
|---|---|---|---|---|
| **Qualification** | Sign partnership agreement | 5+ qualified referrals/quarter OR $10K+ influenced revenue | 15+ referrals/quarter OR $50K+ influenced revenue | 30+ referrals/quarter OR $100K+ influenced revenue |
| **Revenue share** | 10-15% | 15-20% | 20-25% | 25-30%+ (negotiable) |
| **Partner manager** | Self-service portal | Shared partner manager | Dedicated partner manager | Senior dedicated manager + exec sponsor |
| **Co-marketing** | Logo on partner page | Co-branded blog posts, newsletter swap | Joint webinars, co-branded content, shared case studies | Joint product launches, co-branded campaigns, event sponsorship |
| **Training** | Self-paced online training | Monthly group training sessions | Quarterly strategy sessions | Custom training, certification program |
| **Lead sharing** | Referral link only | Referral link + lead registration | Referral + co-sell opportunities | Full pipeline visibility + co-sell + deal registration |
| **Marketing assets** | Basic asset library | Custom landing pages | Co-branded collateral, MDF ($500-$2K/quarter) | Custom co-branded materials, MDF ($2K-$10K/quarter) |
| **Support** | Knowledge base | Priority email support | Dedicated support channel | 24/7 priority support + escalation path |
| **Recognition** | Partner directory listing | Silver badge, quarterly spotlight | Gold badge, annual award eligibility | Platinum badge, keynote opportunities, advisory board |
| **Review cadence** | Annual | Quarterly | Monthly | Bi-weekly |

### Partner Progression Notifications

```
Subject: Congratulations! You've reached {tier} partner status

Hi {partner_name},

Your dedication is paying off. Based on your performance over the past
quarter, you've earned {tier} partner status in the {brand_name}
partner program.

What's new at {tier} level:
  • {Benefit 1}
  • {Benefit 2}
  • {Benefit 3}
  • Revenue share: now {rate}% (up from {previous_rate}%)

Your {quarter} performance:
  Referrals: {count}
  Revenue influenced: ${amount}
  Commissions earned: ${amount}

Next tier ({next_tier}) requirements:
  {requirement_description}
  You're {X}% of the way there.

Let's schedule a strategy session to maximize your new benefits:
{calendar_link}
```

---

## 7. Co-Marketing Agreement Template Outline

```
CO-MARKETING AGREEMENT OUTLINE

1. PARTIES
   - Company A: {brand_name}, {contact}, {role}
   - Company B: {partner_name}, {contact}, {role}

2. OBJECTIVES
   - Mutual goal: {description}
   - Company A goal: {specific metric target}
   - Company B goal: {specific metric target}

3. ACTIVITIES
   - Activity 1: {description, owner, timeline}
   - Activity 2: {description, owner, timeline}
   - Activity 3: {description, owner, timeline}

4. RESPONSIBILITIES
   Company A will:
   - {responsibility 1}
   - {responsibility 2}

   Company B will:
   - {responsibility 1}
   - {responsibility 2}

5. DATA SHARING
   - Lead data shared: {what data, in what format}
   - Each party maintains opt-in compliance for their list
   - No raw list sharing; each brand emails their own list
   - Data handling: GDPR/CCPA compliant

6. BRAND GUIDELINES
   - Each party approves creative using their brand before publication
   - Approved assets and usage rights
   - Prohibited uses

7. BUDGET
   - Total budget: $________
   - Company A contribution: $________
   - Company B contribution: $________
   - Split model: {equal, proportional to audience size, etc.}

8. MEASUREMENT
   - Shared KPIs: {list}
   - Reporting cadence: {weekly/monthly}
   - Attribution method: {UTM, unique landing pages, codes}

9. TIMELINE
   - Start date: {date}
   - End date: {date}
   - Key milestones: {list}

10. TERMINATION
    - Either party may terminate with {X} days written notice
    - Outstanding obligations upon termination

11. SIGNATURES
```

---

## 8. Referral Program A/B Test Ideas (25 Tests)

### Incentive Tests
1. **Incentive amount**: $10 vs. $20 vs. $30 per referral (measure conversion rate and ROI)
2. **Incentive type**: Cash vs. account credit vs. free month vs. feature unlock
3. **Sided-ness**: One-sided (referrer only) vs. two-sided (both parties)
4. **Incentive ratio**: Equal split (50/50) vs. referred-heavy (40/60) vs. referrer-heavy (60/40)
5. **Percentage vs. fixed**: "$15 off" vs. "20% off" (for same effective discount at average order)
6. **Tiered vs. flat**: Same reward every time vs. escalating rewards per referral
7. **Time-limited boost**: Standard reward vs. 2x reward for 72 hours (measure urgency effect)

### Referral Page Tests
8. **Headline framing**: Benefit-focused ("Give $20, Get $20") vs. action-focused ("Share and Earn") vs. social ("Invite Friends to Join")
9. **Steps display**: 3-step visual vs. single paragraph explanation
10. **Social proof**: With user count ("12,847 rewards earned") vs. without
11. **Share button layout**: Horizontal row vs. grid vs. prominent single CTA
12. **Default share channel**: Email pre-selected vs. all channels equal prominence

### Referral Landing Page Tests
13. **Personalization**: "Sarah invited you" vs. generic "A friend invited you" vs. no mention
14. **Form length**: Email-only signup vs. email + name vs. full registration
15. **Social proof type**: Star ratings vs. testimonials vs. customer count vs. media logos
16. **CTA copy**: "Claim Your Reward" vs. "Get Started Free" vs. "Accept Invitation"

### Timing and Trigger Tests
17. **Prompt timing**: Immediately post-purchase vs. 24 hours later vs. 7 days later
18. **NPS-triggered vs. untriggered**: Referral ask after NPS 9-10 vs. generic post-purchase ask
19. **Frequency**: Monthly referral reminder vs. quarterly vs. event-triggered only
20. **In-app placement**: Account dashboard widget vs. post-action modal vs. navigation item

### Channel and Format Tests
21. **Email subject line**: "Share and earn" vs. "Your friends want this" vs. "[Name], give your friends $X"
22. **Share message tone**: Casual ("Check this out!") vs. benefit-led ("Get $X off this tool I love") vs. personal ("I've been using this and thought of you")
23. **Email vs. in-app**: Email referral prompt vs. in-app prompt (same timing, different channel)
24. **SMS referral**: SMS prompt vs. email prompt (for mobile-heavy audiences)
25. **QR code addition**: Referral page with QR code vs. without (measure offline/event sharing)

### Advanced Tests
26. **Gamification**: Standard referral vs. referral with progress bar and milestones
27. **Charity option**: Standard cash reward vs. "donate your reward to charity" option
28. **Referral contest**: Standard ongoing program vs. monthly competition with leaderboard
29. **Expiring rewards**: No expiry vs. 30-day expiry vs. 7-day expiry on referral reward
30. **Reminder cadence**: Single reminder vs. 3-touch reminder sequence over 14 days

---

## 9. Referral Landing Page Framework

### Above the Fold

```
┌─────────────────────────────────────────────────────────┐
│  [Brand Logo]                          [Login] [Signup] │
│                                                         │
│  {Referrer_name} invited you to try {Brand}             │
│                                                         │
│  {Primary headline: clear value proposition}             │
│  {Subheadline: what the product does in one sentence}   │
│                                                         │
│  Your exclusive offer: {incentive for referred user}     │
│                                                         │
│  [Primary CTA: "Claim Your {Reward}" or "Get Started"]  │
│                                                         │
│  {Social proof: "Trusted by X,XXX customers"            │
│   or star rating with review count}                     │
└─────────────────────────────────────────────────────────┘
```

### Below the Fold

```
┌─────────────────────────────────────────────────────────┐
│  How it works:                                          │
│  1. Sign up using this link (takes {X} seconds)         │
│  2. {First value action}                                │
│  3. {Outcome / benefit}                                 │
│                                                         │
│  Why people love {Brand}:                               │
│  • {Benefit 1 with specific proof point}                │
│  • {Benefit 2 with specific proof point}                │
│  • {Benefit 3 with specific proof point}                │
│                                                         │
│  {Customer testimonial with photo/name}                 │
│  "{Quote about the product}" — {Name}, {Title}          │
│                                                         │
│  [Secondary CTA: "Start Your Free Trial"]               │
│                                                         │
│  {Trust badges: security, money-back guarantee,         │
│   media mentions, partner logos}                        │
└─────────────────────────────────────────────────────────┘
```

### Key Design Principles
- Personalization: Include the referrer's name prominently
- Incentive visibility: The referred person's reward should be immediately visible
- Minimal friction: Shortest possible signup form (email only if possible)
- Mobile-first: Majority of referral clicks come from mobile devices
- Fast load: Under 2 seconds; every second of delay reduces conversion by ~7%
- No navigation distractions: Remove full site navigation; single clear CTA

---

## 10. Partner Pitch Email Templates

### Template 1: Cold Partnership Outreach

```
Subject: {Their brand} + {Your brand}: quick partnership idea

Hi {name},

I'm {your_name} from {your_brand}. We {one-sentence description}.

I noticed we share a similar audience — {describe overlap}. I had a quick
idea for how we could help each other:

{Specific partnership proposal in 2-3 sentences. Be concrete about what
you're suggesting and what value they'd get.}

Some context on our audience:
  • {audience_size} {users/subscribers/customers}
  • {relevant_metric} (engagement rate, open rate, etc.)
  • {audience_description} (demographics, industries, etc.)

Would you be open to a 15-minute call to explore this? I'm flexible on
timing this week or next.

{your_name}
{your_title}, {your_brand}
```

### Template 2: Integration Partnership Proposal

```
Subject: Integration idea: {their product} + {your product}

Hi {name},

Our customers keep asking us about integrating with {their product}. We've
had {X} requests in the past {timeframe}.

I think there's a real opportunity:
  • {Count} of our customers already use {their product}
  • An integration would {describe mutual benefit}
  • We'd promote the integration to our {audience_size} users

We've already scoped what the integration would look like on our side.
Happy to share our technical proposal and discuss how to make this work
for both teams.

Would a 20-minute call work? I can loop in our head of product if helpful.
```

### Template 3: Co-Marketing Proposal

```
Subject: Co-marketing idea: {specific activity}

Hi {name},

I have a specific co-marketing idea I think would work well for both
{their brand} and {your brand}:

The idea: {describe the specific activity — joint webinar, co-authored
report, newsletter swap, bundle offer, etc.}

Why it makes sense:
  • Our audiences overlap but our products don't compete
  • {Their brand} brings {their strength}; {your brand} brings {your strength}
  • Expected reach: {combined audience metric}

I'd propose a small pilot first — {describe a low-commitment first step}
— and if it works, we can explore more.

Interested?
```

### Template 4: Affiliate Program Invitation

```
Subject: Earn {commission_rate} promoting {brand_name}

Hi {name},

I've been following your content on {platform} — particularly {specific
piece they published}. Your audience aligns perfectly with {brand_name}.

We just launched our affiliate program and I'd love to invite you:

  Commission: {rate} per {sale/signup/recurring month}
  Cookie window: {duration}
  Avg. earnings per referral: ${amount}
  Top affiliates earn: ${range}/month

We provide:
  • Custom tracking links and dashboard
  • Email templates, banner ads, social copy
  • Dedicated affiliate manager (that's me)
  • Monthly payments via {payment method}

Want to give it a try? Here's your application link: {url}

Or if you have questions, just reply — happy to chat.
```

---

## 11. Quick Reference: Referral Program KPI Targets

| Metric | Minimum Viable | Good | Excellent |
|---|---|---|---|
| Participation rate | 2-3% | 5-10% | 10-15%+ |
| K-factor | 0.1-0.2 | 0.3-0.5 | 0.5-1.0+ |
| Invites per referrer | 1-2 | 3-5 | 5-10+ |
| Invite-to-signup rate | 5-10% | 10-20% | 20-30%+ |
| Signup-to-purchase rate | 15-25% | 25-40% | 40-60%+ |
| Referral CAC vs. paid CAC | 50-75% of paid | 30-50% of paid | Under 30% of paid |
| Time to first referral | 60+ days | 30-60 days | Under 30 days |
| Program ROI | 2-3x | 3-5x | 5x+ |
| Referred customer LTV vs. organic | Equal | 10-16% higher | 16-25% higher |
| Referred customer retention | Equal | 20-30% higher | 37%+ higher |

---

## Sources

This framework document synthesizes templates and structures from:
- Extole 2026 Referral Marketing Playbook
- Viral Loops referral best practices and A/B testing guides (2025)
- Mention Me A/B testing framework for referral optimization (2025)
- Prefinery startup referral program case studies (2025)
- ReferralCandy program benchmarks and templates (2025-2026)
- Tapfiliate affiliate program management guide (2026)
- Kiflo partner engagement strategies playbook (2026)
- Industry standard partner program tier structures (PartnerStack, Impact, Kiflo)

Last updated: March 2026
