# Referral Program Lifecycle Workflow

This reference defines the standard workflow, diagnostic questions, phase gates, escalation routes, and ethical guidelines for all referral, affiliate, and partnership marketing work.

---

## Workflow Overview

The referral program lifecycle moves through six phases. Each phase has explicit entry conditions, key activities, deliverables, and exit gates. The workflow formalizes the branching point at Phase 3 where program type (referral, affiliate, or partnership) determines the technical architecture.

```
Phase 1: Program Strategy
    |
Phase 2: Incentive Design
    |
Phase 3: Technical Architecture  <-- Branches by program type
    |         |         |
    |    Referral   Affiliate   Partnership
    |         |         |           |
    |         +----+----+-----------+
    |              |
Phase 4: Launch & Activation
    |
Phase 5: Optimization
    |
Phase 6: Scale & Manage
```

---

## Diagnostic Questions

Ask these before producing any referral program recommendation. Recommendations without this data are guesses.

1. **Product economics**: What is the customer LTV? What is the current CAC? What acquisition cost ratio (referral cost / LTV) is sustainable?
2. **Current state**: Does a referral or affiliate program already exist? What has been tried? What were the results?
3. **Customer base**: How many active customers exist? What is the NPS or satisfaction score? Do customers already refer organically?
4. **Product fit**: Is the product inherently shareable (collaboration tool, social product) or does sharing need to be incentivized?
5. **Technical capacity**: What platform is the product built on? Is there an existing referral tracking system? What integrations are available?
6. **Program type**: Is the goal customer referrals, affiliate/creator partnerships, strategic B2B partnerships, or a combination?
7. **Competitive landscape**: What referral programs do competitors run? What incentive levels are standard in the category?

If the user cannot answer questions 1-2, recommend calculating unit economics before designing a program. A referral program without known LTV and CAC targets is a cost center, not a growth channel.

---

## Phase 1: Program Strategy

**Purpose**: Define the program type, goals, target audience, and economic framework before designing any mechanics.

### Entry Conditions
- Brand context or SOSTAC plan is available (or user provides equivalent context)
- Product is live with paying customers (minimum viable base for referrals)
- Basic unit economics are known (LTV, CAC, or reasonable estimates)

### Key Activities
- Classify program type: customer referral, affiliate/creator, strategic partnership, or hybrid
- Define primary goal: new customer acquisition, revenue expansion, market entry, or brand awareness
- Identify the ideal referrer profile: power users, satisfied customers, industry influencers, complementary businesses
- Assess product virality potential: is the product inherently shareable or does it require incentive-driven sharing?
- Map the customer journey to identify natural "share moments" (post-purchase, after success milestone, during collaboration)
- Benchmark competitive programs in the category
- Set K-factor targets: K > 0.5 for meaningful growth contribution, K > 1.0 for true viral growth

### Deliverables
- Program strategy brief with type classification, goals, target referrer profiles, and success metrics
- Competitive referral program analysis (3-5 competitors)
- K-factor target with supporting assumptions

### Exit Conditions
- Program type is defined and agreed upon
- Economic targets are set (target referral CAC, acceptable cost as % of LTV)
- At least 3 natural share moments are identified in the customer journey

---

## Phase 2: Incentive Design

**Purpose**: Design the reward structure that motivates referrers and converts referred prospects while remaining economically sustainable.

### Entry Conditions
- Program strategy brief is complete (Phase 1 exit)
- LTV and target referral CAC are defined
- Program type is classified

### Key Activities
- Design two-sided incentive structure (referrer reward + referee incentive)
  - Two-sided programs convert 30-50% better than one-sided
  - Referrer reward: cash, credit, subscription extension, feature unlock, or tiered rewards
  - Referee incentive: discount, extended trial, bonus feature, or credit
- Model the economics: total referral cost should be 10-25% of LTV for sustainability
  - Calculate break-even: at what conversion rate does the program pay for itself?
  - Model scenarios: pessimistic (2% referral rate), baseline (5%), optimistic (10%)
- Design reward tiers if applicable: milestone-based rewards increase engagement by 20-40%
  - Tier 1: First successful referral (immediate reward)
  - Tier 2: 3-5 referrals (bonus reward or status)
  - Tier 3: 10+ referrals (premium rewards, ambassador status)
- Set K-factor component targets:
  - Invites sent per referrer (target: 3-5 average)
  - Conversion rate per invite (target: 10-25% depending on channel)
  - K = invites_sent x conversion_rate (target > 0.5)
- Define fraud prevention rules: duplicate detection, self-referral blocking, minimum activity thresholds
- Draft referral program terms and conditions

### Deliverables
- Incentive design document with referrer rewards, referee incentives, and tier structure
- Economic model with break-even analysis and three scenarios
- K-factor model with component targets
- Draft terms and conditions

### Exit Conditions
- Incentive structure is approved by stakeholders
- Economic model shows sustainability at baseline scenario
- Fraud prevention rules are defined

---

## Phase 3: Technical Architecture

**Purpose**: Design the tracking system, attribution model, and integration points. This phase branches based on program type.

### Entry Conditions
- Incentive design is finalized (Phase 2 exit)
- Technical platform and constraints are understood
- Integration requirements are mapped

### Key Activities — All Program Types
- Define unique identifier system: referral links, codes, or both
  - Links: better for digital sharing, trackable, can include UTM parameters
  - Codes: better for offline/verbal sharing, easier to remember, work across channels
- Design attribution model:
  - First-touch vs last-touch vs multi-touch for referral credit
  - Attribution window: 30 days is standard, 90 days for enterprise/long sales cycles
  - Cookie-based + account-based attribution for reliability
- Select or build tracking infrastructure:
  - Build: custom referral tracking in product (best for product-led referrals)
  - Buy: ReferralCandy, Friendbuy, Rewardful, PartnerStack, Impact (match to program type)
  - Hybrid: tracking platform + custom product integration

### Branch: Customer Referral Program
- Build referral widget or dashboard within the product
- Integrate with user account system for automatic reward fulfillment
- Design share flow: email invite, unique link copy, social share buttons
- Set up conversion tracking: referred signup, activation, and payment events
- Implement double-sided reward fulfillment automation

### Branch: Affiliate/Creator Program
- Set up affiliate portal with unique tracking links and performance dashboard
- Define commission structure: one-time vs recurring, percentage vs flat fee
- Build creative asset library for affiliates (banners, copy, landing pages)
- Integrate with payment system for automated commission payouts
- Set up affiliate tier system based on performance

### Branch: Strategic Partnership
- Design co-branded landing pages or integration pages
- Build API-level integration tracking if applicable
- Set up revenue share or lead share tracking
- Create partner onboarding documentation and assets
- Define joint success metrics and reporting cadence

### Deliverables
- Technical architecture document with system diagram
- Tracking and attribution specification
- Integration plan with timeline
- Platform selection recommendation (build vs buy analysis)

### Exit Conditions
- Tracking system is built or configured and tested
- Attribution model is validated with test referrals
- Reward fulfillment automation is verified end-to-end
- Share mechanics (links, codes, widgets) are functional

---

## Phase 4: Launch & Activation

**Purpose**: Seed the program with initial referrers, build the onboarding flow, and execute the promotional plan.

### Entry Conditions
- Technical infrastructure is live and tested (Phase 3 exit)
- Share mechanics are functional
- Reward fulfillment is automated and verified

### Key Activities
- Identify and recruit seed referrers (top 50-100 most engaged customers)
  - Personal outreach, not mass email: "You're one of our best customers — we built something for you"
  - Provide early access to the referral program before public launch
  - Target: 20-30% of seeded users make at least one referral in the first 2 weeks
- Build the referral onboarding flow:
  - In-product prompt at the natural share moment (post-success, post-purchase)
  - Clear explanation of the reward structure (referrer AND referee benefits)
  - One-click sharing with pre-written messages the referrer can customize
  - Referral dashboard showing status, pending rewards, and leaderboard (if applicable)
- Execute promotional plan:
  - Email announcement to full customer base with clear CTA
  - In-product banner or modal announcing the program
  - Social media announcement with referrer success stories (if available from seed phase)
  - Blog post explaining the program with FAQ
- Set up referral reminder cadence:
  - Trigger-based: after positive support interaction, after hitting usage milestone, after renewal
  - Time-based: monthly reminder to active users who have not referred

### Deliverables
- Seed referrer outreach sequence (3-email sequence)
- Referral onboarding flow specification
- Launch email and in-product announcement copy
- Referral reminder automation rules

### Exit Conditions
- Seed referrers are active and generating initial referrals
- Referral onboarding flow is live and functional
- Program is announced to full customer base
- Baseline metrics are being tracked: referral rate, K-factor, conversion rate

---

## Phase 5: Optimization

**Purpose**: Systematically improve program performance through testing, friction reduction, and channel expansion.

### Entry Conditions
- Program has been live for at least 30 days
- Baseline metrics are established (Phase 4 exit)
- Minimum 100 referral attempts for statistical significance on conversion tests

### Key Activities
- A/B test incentive structures:
  - Test reward amount: +25% vs -25% from baseline
  - Test reward type: cash vs credit vs feature unlock
  - Test two-sided vs one-sided (validate the 30-50% lift assumption)
  - Test immediacy: instant reward vs delayed reward
- Optimize share moments:
  - Analyze which in-product moments generate the most referrals
  - Test adding referral prompts at new touchpoints
  - Test removing underperforming prompts (referral fatigue is real)
- Reduce friction in the referral flow:
  - Measure drop-off at each step: view program -> copy link -> share -> recipient clicks -> recipient converts
  - Simplify share mechanics: reduce steps, improve copy, test channels
  - Optimize the referee landing experience: does the referred visitor convert at a higher rate than organic?
- Expand channels:
  - Test new share channels: SMS, WhatsApp, in-product collaboration invites
  - Test offline referral mechanics (QR codes, verbal codes)
  - Test community-specific referral campaigns
- Optimize the K-factor components:
  - Increase invites sent: test referral prompts, reminder cadence, gamification
  - Increase conversion per invite: test referee incentives, landing pages, onboarding

### Benchmarks for Optimization Targets

| Metric | Poor | Average | Good | Excellent |
|--------|------|---------|------|-----------|
| Referral participation rate | < 2% | 2-5% | 5-15% | > 15% |
| Invites sent per referrer | < 2 | 2-3 | 3-5 | > 5 |
| Referred visitor conversion | < 5% | 5-15% | 15-25% | > 25% |
| K-factor | < 0.2 | 0.2-0.5 | 0.5-0.8 | > 0.8 |
| Referral revenue contribution | < 5% | 5-10% | 10-25% | > 25% |
| Referred customer LTV vs organic | < 1.0x | 1.0x | 1.1-1.2x | > 1.25x |

### Deliverables
- A/B test plan with hypotheses, metrics, and sample sizes
- Friction analysis report with drop-off data at each funnel step
- Optimization roadmap prioritized by expected impact
- Updated K-factor model with actual data

### Exit Conditions
- At least 3 A/B tests completed with statistically significant results
- Referral participation rate exceeds 5% of active users
- K-factor is trending upward and above 0.3
- Referral channel contributes measurable new customers monthly

---

## Phase 6: Scale & Manage

**Purpose**: Scale the program while maintaining quality, preventing fraud, managing partners, and ensuring sustainable economics.

### Entry Conditions
- Program is optimized and generating consistent results (Phase 5 exit)
- Referral economics are proven sustainable
- Growth targets require scaling beyond current participation

### Key Activities
- Implement fraud prevention and detection:
  - Automated anomaly detection: sudden spikes in referrals from single accounts, referral circles, geographic clustering
  - Self-referral prevention: email domain matching, device fingerprinting, IP analysis
  - Quality thresholds: referred customers must meet minimum activity or payment thresholds before rewards pay out
  - Monthly audit: review top referrers for legitimacy, investigate flagged accounts
  - Clawback policy: reverse rewards for fraudulent or reversed conversions
- Scale partner management (for affiliate/partnership programs):
  - Tiered partner program with clear advancement criteria
  - Automated partner onboarding with self-serve asset library
  - Regular partner communication: newsletter, performance reports, program updates
  - Partner advisory board for top performers (co-create program improvements)
- Build comprehensive reporting:
  - Executive dashboard: referral revenue, CAC, LTV of referred customers, program ROI
  - Operational dashboard: daily referrals, conversion funnel, reward payouts, fraud flags
  - Partner dashboard: individual partner performance, commission tracking, content performance
- Manage payouts at scale:
  - Automated payout processing on defined schedule (monthly or bi-weekly)
  - Multiple payout methods: platform credit, bank transfer, PayPal, gift cards
  - Tax compliance: 1099 reporting for US affiliates earning > $600/year
  - Currency handling for international programs
- Plan program evolution:
  - Seasonal campaigns: double rewards during growth pushes
  - Referral contests: leaderboard competitions for top referrers
  - Ambassador program: formalize top referrers into brand ambassadors with exclusive benefits
  - New market expansion: adapt program for new geographies or segments

### Deliverables
- Fraud prevention playbook with detection rules and response procedures
- Partner management process documentation
- Reporting dashboard specification
- Payout operations manual
- Program evolution roadmap

### Exit Conditions
- Fraud rate is below 3% of total referrals
- Program economics remain within target CAC range at scale
- Reporting is automated and stakeholders receive regular updates
- Payout operations run without manual intervention for standard cases

---

## Escalation Routes

| Situation | Route To | Why |
|-----------|----------|-----|
| Influencer campaigns beyond affiliate structure | paw-mkt-influencer | Influencer relationship management requires dedicated strategy |
| Community building for advocates | paw-mkt-community | Community platforms and engagement need specialized approach |
| Email sequences for referral nurture | paw-mkt-email | Drip sequences, automation, and deliverability expertise |
| Content for co-marketing assets | paw-mkt-content | Long-form content creation and editorial quality |
| Paid promotion of referral program | paw-mkt-paid-ads | Ad creative, targeting, and budget optimization |
| Social media promotion of program | paw-mkt-social | Platform-specific content strategy and community engagement |
| PR for partnership announcements | paw-mkt-pr | Media relations and press release distribution |
| Analytics and attribution setup | paw-mkt-analytics | Tracking infrastructure and measurement framework |

---

## Ethics: Sustainable Growth Without Manipulation

Referral programs leverage social trust. Misusing that trust damages both the brand and the referrer-referee relationship.

### Ethical Referral Practices

- **Transparent incentives**: Both referrer and referee know exactly what each party receives. No hidden terms.
- **Genuine recommendations**: The program should amplify organic word-of-mouth, not manufacture it. If customers would not recommend the product without incentives, fix the product first.
- **Honest representation**: Referral messages should accurately describe the product. Pre-written share messages must be truthful.
- **Fair reward fulfillment**: Rewards are delivered as promised, on time, without hidden conditions that void eligibility.
- **Respectful outreach**: Referral invitations should not spam recipients. Limit invite frequency and provide clear opt-out.
- **Privacy compliance**: Referral data collection complies with GDPR, CCPA, and applicable privacy regulations. Referred contacts are not added to marketing lists without consent.

### Patterns to Avoid

| Pattern | Description | Why It Harms |
|---------|-------------|--------------|
| Manufactured urgency | "Refer now — this reward expires in 2 hours!" with resetting timers | Destroys trust in the program and the referrer's credibility |
| Spam incentives | Rewarding volume of invites sent rather than quality of referrals | Trains referrers to spam their networks, damaging relationships |
| Hidden qualification | Reward requires conditions not disclosed upfront (e.g., referred user must spend $500) | Referrer feels cheated, stops participating, warns others |
| Fake social proof | "10,000 people have referred!" when the number is fabricated | Discovered fraud destroys all program credibility |
| Aggressive nag screens | Blocking product use until user refers or dismisses multiple times | Creates resentment, increases churn, not acquisition |
| Pyramid dynamics | Multi-level commission structures that reward recruitment over product use | Regulatory risk, brand damage, attracts wrong participants |

### The Trust Test

Before implementing any referral tactic, ask: **Would the referrer be comfortable if the referred friend saw exactly how the program works, including the incentives?** If the answer is no, redesign the mechanic.

---

## Path Resolution

**Campaign mode** -- working within a named campaign:
  -> Save to `./.pawbytes/marketing-suites/brands/{brand-slug}/campaigns/{type}-{campaign-slug}/referral/`
  -> Read campaign strategy at `./.pawbytes/marketing-suites/brands/{brand-slug}/campaigns/{type}-{campaign-slug}/strategy.md`

**Standalone mode** -- evergreen or independent work:
  -> Save to `./.pawbytes/marketing-suites/brands/{brand-slug}/operations/referral/`

If unsure which mode, ask: "Is this part of a specific campaign, or standalone work?"

---

## Deliverables

All referral work saves to the resolved path (see Path Resolution above).

| Deliverable | Filename | Key Sections |
|-------------|----------|--------------|
| Program Strategy Brief | `strategy-{program-type}-{YYYY-MM-DD}.md` | Program type, goals, target referrers, competitive analysis, K-factor targets |
| Incentive Design | `incentive-design-{YYYY-MM-DD}.md` | Reward structure, economic model, tier design, terms and conditions |
| Technical Architecture | `technical-architecture-{YYYY-MM-DD}.md` | System diagram, attribution model, integration plan, platform recommendation |
| Launch Plan | `launch-plan-{YYYY-MM-DD}.md` | Seed referrer list, outreach sequences, onboarding flow, promotional plan |
| Optimization Report | `optimization-report-{YYYY-MM-DD}.md` | Test results, friction analysis, K-factor trends, recommendations |
| Program Operations Manual | `operations-manual-{YYYY-MM-DD}.md` | Fraud prevention, partner management, payout procedures, reporting |

---

## Response Protocol

When the user requests referral, affiliate, or partnership marketing work:

1. **Route starting context** (blank-page, codebase, or live URL) -- see `./references/shared-patterns.md`
2. **Read strategic context** -- brand positioning and SOSTAC first; otherwise codebase, live site, or prior deliverables
3. **Ask diagnostic questions** if the user has not provided this information. Do not design a program without knowing LTV and current referral activity.
4. **Determine program type** -- referral, affiliate, partnership, or hybrid. This drives the Phase 3 branch.
5. **Assess current phase** -- is this a new program (start at Phase 1) or optimization of an existing one (enter at Phase 5)?
6. **Deliver phase-appropriate output** -- strategy, incentive design, technical spec, launch plan, or optimization recommendations depending on where the user is in the lifecycle.
7. **Save deliverables** to the resolved path.
8. **Recommend next phase** -- what to do next, what to measure, when to advance.
