# Chapter 9: Specialized Skills

This chapter covers six specialized marketing skills that address specific domains within the marketing function. Each skill is a deep specialist with unique frameworks, methodologies, and deliverables designed for focused expertise.

---

## 9.1 Marketing Analytics Specialist

### What It Does

The Marketing Analytics Specialist sets up tracking, dashboards, attribution, and experiment infrastructure. It transforms SOSTAC objectives into measurable outcomes and tactics into data-driven feedback loops. This is the "Control" phase of SOSTAC brought to life—the measurement backbone that validates every marketing investment.

**Core deliverables:**
- Measurement plans with KPI hierarchies
- Tracking specifications (GA4, GTM, ad platforms)
- Dashboard designs for different stakeholders
- A/B test frameworks and experiment roadmaps
- Attribution models and marketing ROI analyses

### Capabilities

| Capability | Description |
|------------|-------------|
| **Measurement Framework** | KPI hierarchy design, North Star metrics, metric definitions with formulas |
| **Tracking Setup** | GA4 configuration, GTM implementation, UTM strategies, event naming conventions |
| **Dashboard Design** | Stakeholder-specific dashboards that answer real questions |
| **Reporting** | Performance reports, trend analysis, anomaly detection |
| **Attribution Modeling** | Multi-touch attribution, triangulation across methods |
| **A/B Testing** | Hypothesis formation, sample size calculation, experiment design |
| **Funnel Analysis** | Conversion path analysis, drop-off diagnosis |
| **Marketing ROI** | Channel ROI, CAC/LTV analysis, budget allocation recommendations |

### When to Use It

**Trigger phrases:**
- "GA4 setup" / "GTM implementation"
- "analytics dashboard"
- "attribution model"
- "measurement plan"
- "tracking setup"
- "UTM strategy"
- "A/B test design" / "experiment infrastructure"
- "conversion tracking"
- "marketing ROI"

**Note:** This skill handles analytics infrastructure, not CRO hypotheses themselves. For conversion rate optimization, route to the CRO/Web specialist.

### Measurement Framework

The skill builds measurement from business objectives down to daily operational metrics:

| Tier | Purpose | Audience | Examples |
|------|---------|----------|----------|
| **Primary KPIs (1-2)** | Directly measure SOSTAC objectives | Executive, founder | Revenue, MQLs, active users |
| **Secondary KPIs (3-5)** | Progress indicators feeding primary | Marketing lead | Traffic, conversion rate, CAC |
| **Diagnostic KPIs (per channel)** | Optimization levers | Channel specialist | CTR, CPC, bounce rate, open rate |

Every metric includes a definition, formula, data source, review cadence, numeric target, and action threshold—the value that triggers investigation.

**North Star Metric:** The single metric that best captures customer value. All other metrics ladder up to this. Examples include weekly active users (SaaS), monthly repeat purchase rate (e-commerce), or qualified leads per month (B2B).

### Tool Selection Guide

| Tool | Best For | When to Use |
|------|----------|-------------|
| **GA4 + GTM** | All web properties | Default for any brand with a website |
| **Mixpanel** | Product analytics, funnels | SaaS or apps needing in-product behavior |
| **Amplitude** | Product analytics at scale | Larger product teams, deeper behavioral analysis |
| **PostHog** | Self-hosted analytics | Privacy/compliance requirements |
| **Segment** | Data routing / CDP | Sending same event data to 5+ tools |

**Decision framework:**
- **Early stage:** GA4 + GTM only
- **Product-led growth:** Add Mixpanel or PostHog
- **Scaling (5+ tools):** Add Segment as event router
- **Self-hosted/privacy-first:** PostHog
- **Enterprise:** Amplitude or Mixpanel + data warehouse

### Example: GA4 and GTM Setup

**Scenario:** A B2B SaaS company needs complete tracking setup for their marketing website and product.

**GA4 Configuration:**
1. **Data Streams:** One web stream per domain with enhanced measurement enabled (page views, scrolls, outbound clicks, site search, video engagement, file downloads)
2. **Conversions:** Mark key events as conversions (max 30)—prioritize purchase, lead form, sign-up, demo request
3. **E-commerce:** Implement full flow: view_item, add_to_cart, begin_checkout, purchase with item parameters
4. **Settings:** 14-month data retention, Google Signals enabled, linked to Google Ads, Search Console, BigQuery

**GTM Implementation:**

| Tag | Trigger | Purpose |
|-----|---------|---------|
| GA4 Configuration | All Pages | Base tracking |
| GA4 Event -- form_submit | Form Submission | Lead tracking |
| Meta Pixel -- PageView | All Pages | Meta base tracking |
| Meta Pixel -- Lead | Form Submission | Meta conversion |
| Google Ads Conversion | Thank You Page | Ads conversion |
| LinkedIn Insight | All Pages | LinkedIn tracking |

**UTM Convention:**

| Parameter | Purpose | Convention |
|-----------|---------|------------|
| utm_source | Traffic origin | `google`, `meta`, `linkedin`, `newsletter` |
| utm_medium | Marketing medium | `cpc`, `organic`, `email`, `social`, `referral` |
| utm_campaign | Campaign ID | `{year}-{month}-{campaign-name}` |
| utm_content | Creative variant | `banner-a`, `cta-red`, `video-15s` |
| utm_term | Keyword (paid search) | The keyword or audience targeted |

---

## 9.2 Pricing Strategy Specialist

### What It Does

The Pricing Strategy Specialist designs value-based pricing structures, packaging tiers, pricing pages, and willingness-to-pay research programs. It delivers specific, defensible pricing recommendations grounded in brand positioning and customer economics.

**Core deliverables:**
- Pricing strategy documents with tier structures
- Pricing page copy and layout recommendations
- Willingness-to-pay research designs
- Competitive pricing analyses
- Price increase execution plans

### Pricing Areas

| Area | Description |
|------|-------------|
| **Pricing Models** | Freemium, tiered, usage-based, flat-rate, or hybrid structures |
| **Tier Packaging** | What to gate, what to include, how to differentiate tiers |
| **Value Metric Selection** | The unit of value that scales with customer usage |
| **Pricing Page Design** | Layout, anchoring, CTA strategy, feature tables |
| **Willingness-to-Pay Research** | Van Westendorp surveys, Gabor-Granger, competitive analysis |
| **Price Increases** | Timing, sizing, communication strategy, grandfathering |

### When to Use It

**Trigger phrases:**
- "pricing tiers" / "tier structure"
- "freemium model"
- "value metric"
- "pricing page"
- "willing to pay"
- "Van Westendorp"
- "price increase"
- "pricing strategy"

### Value-Based Methodology

The skill diagnoses pricing problems before prescribing solutions:

| Symptom | Problem Type | Primary Fix |
|---------|--------------|-------------|
| Deals stalling on price | Price point vs perceived value mismatch | Value communication, not necessarily price cuts |
| High trial-to-paid drop-off | Wrong value metric or tier structure | Value metric and packaging audit |
| Low ACV | Under-extracting from best customers | Tier restructuring, usage-based expansion |
| Everyone choosing cheapest tier | Middle tier not differentiated | Packaging and decoy redesign |
| Pricing page confusion | Page design and copy problem | Pricing page redesign |

**The Floor-Ceiling Model:**

```
[Floor]                                              [Ceiling]
Next best alternative cost          Customer perceived value (max WTP)
         |_______________________________________________|
                      Acceptable Price Range
                              ^
                          Sweet spot
```

- **Floor:** What the customer currently pays (spreadsheets, cheaper tool, manual process)
- **Ceiling:** Maximum the customer would pay before cost outweighs value
- **Sweet spot:** Price between floor and ceiling—closer to ceiling for premium positioning

**Cost-Plus vs Value-Based Pricing:**

| Approach | Method | Problem |
|----------|--------|---------|
| Cost-plus (avoid) | Cost + margin = price | Ignores customer value; systematically underprices software |
| Value-based (use) | Start from value delivered, price captures fraction | Aligned with customer economics; defensible |

### Three-Tier Framework

| Tier | Role | Pricing | Customer Type |
|------|------|---------|---------------|
| **Starter / Free** | Lead generation, top-of-funnel | Free or very low ($0-$29/mo) | Self-serve, price-sensitive, early-stage |
| **Professional / Core** | Primary revenue tier, most popular | Mid-range ($49-$299/mo) | Core persona, growing team |
| **Business / Enterprise** | Maximum value capture | High or custom ($299+/mo or quote) | Power users, large teams, compliance needs |

**Decoy Pricing:** The middle tier is the decoy, priced to make the top tier look reasonable:

```
Starter:      $29/mo  - real option for budget buyers
Professional: $99/mo  - decoy; anchors against Enterprise
Enterprise:   $149/mo - looks like only $50 more; most choose this
```

### Example: Tier Restructuring

**Scenario:** A SaaS company has 80% of customers on their cheapest tier ($29/mo), with minimal upgrade motion.

**Diagnosis:**
- Middle tier ($79/mo) lacks compelling differentiation
- No clear value metric creates natural upgrade triggers
- Feature gates are arbitrary, not based on value delivered

**Recommendation:**

| Tier | Price | Value Metric | Key Gates |
|------|-------|--------------|-----------|
| Starter | $29/mo | 3 projects, 1,000 contacts | Single user, basic analytics |
| Growth | $89/mo | 10 projects, 10,000 contacts | Team collaboration, advanced integrations |
| Scale | $199/mo | Unlimited projects, 50,000 contacts | API access, priority support, SSO |

**Decoy effect:** Growth tier positioned as "most popular" with visual emphasis. Price gap between Growth and Scale is modest ($110) relative to feature jump, making Scale feel like the smart choice for growing teams.

---

## 9.3 Marketing Psychology Specialist

### What It Does

The Marketing Psychology Specialist applies cognitive science, persuasion research, and behavioral economics to marketing decisions. It delivers specific, actionable recommendations grounded in brand context and audience psychology—not generic explanations.

**Core deliverables:**
- Before/after copy rewrites with psychological rationale
- Landing page optimization recommendations
- Pricing page psychology applications
- Email sequence persuasion design
- Ethical verification of all techniques

### Frameworks Included

| Framework | Description | Best For |
|-----------|-------------|----------|
| **Cialdini Six Principles** | Reciprocity, commitment, social proof, authority, liking, scarcity | Designing persuasion-dependent assets across the funnel |
| **Cognitive Biases Reference** | 15 biases with marketing-specific examples | Diagnosing conversion problems, writing psychology-informed copy |
| **BJ Fogg Behavioral Design** | B=MAP model (Behavior = Motivation, Ability, Prompt) | Diagnosing why behaviors don't happen |
| **Quick-Reference Table** | 20 marketing challenges mapped to principles | Rapid diagnostic for any marketing problem |
| **Psychology by Context** | Channel-by-channel guidance | Choosing which principles to apply in specific channels |
| **Pricing Psychology** | Charm pricing, decoy, anchoring, Rule of 100 | Designing pricing pages and presenting prices |
| **Strategic Mental Models** | First principles, JTBD, flywheel | Strategic planning and reasoning clarity |

### When to Use It

**Trigger phrases:**
- "cognitive bias"
- "loss aversion"
- "social proof"
- "scarcity"
- "Cialdini"
- "persuasion framework"
- "behavioral economics"
- "psychology in marketing"
- "why customers buy"

### Cialdini's Six Principles of Influence

| Principle | What It Is | Marketing Application |
|-----------|------------|----------------------|
| **Reciprocity** | People feel obligated to return favors | Lead magnets, free tools, unexpected bonuses |
| **Commitment & Consistency** | Small commitments lead to larger ones | Micro-commitment sequences, onboarding checklists, quiz funnels |
| **Social Proof** | People look to others under uncertainty | Customer counts, testimonials, logos, real-time indicators |
| **Authority** | People defer to credible experts | Founder credentials, press logos, certifications, detailed case studies |
| **Liking** | People prefer those similar to themselves | Brand personality, founder stories, community building |
| **Scarcity** | Perceived scarcity increases value | Limited cohorts, time-limited offers, waitlists, exclusivity |

**Negative social proof warning:** Never say "most people don't do X" or "many customers struggle with Y." Telling people the undesired behavior is common makes it feel normal and increases it.

### Ethical Persuasion Principles

The skill distinguishes ethical persuasion from manipulation:

**Ethical persuasion helps people make decisions aligned with their genuine interests.** The customer who acts on ethical persuasion is glad they did.

| Ethical Practice | Dark Pattern (Avoid) |
|------------------|----------------------|
| Genuine scarcity (real limits) | Fake scarcity (countdowns that reset) |
| Real social proof (actual testimonials) | Fabricated testimonials |
| Honest anchoring (verifiable prices) | Fake anchors ("Was $999" never actually charged) |
| Loss framing (real costs they incur) | Manipulative fear-mongering |
| Transparent pricing | Hidden fees, drip pricing |

**The ethical test:** If the customer understood exactly how the technique was being used, would they still feel well-served? If no, redesign.

### Example: Copy Optimization with Psychology

**Scenario:** A B2B software company's landing page uses a gain-framed headline: "Improve your team's productivity by 40%."

**Analysis:** The audience is status quo biased—they've managed with current tools for years. Loss framing typically outperforms in this context.

**Recommendation:**

| Before | After | Principle Applied |
|--------|-------|-------------------|
| "Improve your team's productivity by 40%" | "Stop losing 12 hours per week to manual reporting" | Loss aversion |
| "Trusted by 500+ companies" | "Join 500+ teams who eliminated their reporting bottleneck" | Social proof with specificity |
| "Free trial available" | "Start your free trial—no credit card required, setup in 5 minutes" | Friction reduction + commitment |
| "Contact us for enterprise pricing" | "Enterprise teams save an average of $127K/year. See your ROI." | Authority + specificity |

**Result:** The rewritten copy speaks to what the audience fears losing (time, money) rather than what they might gain—more compelling for status quo buyers.

---

## 9.4 Community Building Specialist

### What It Does

The Community Building Specialist designs, launches, and scales owned community platforms that drive retention, advocacy, and acquisition. It grounds every recommendation in brand positioning and audience context.

**Core deliverables:**
- Community strategy documents
- Platform selection analyses
- Launch plans and founding member recruitment
- Engagement program designs
- Moderation guidelines
- Community health metrics frameworks

### Platforms Covered

| Platform | Best For | Scale Ceiling |
|----------|----------|---------------|
| **Discord** | Gaming, Web3, creators, developers, 18-35 audiences | 100K+ members |
| **Slack** | B2B, professional, enterprise communities | 5K members |
| **Circle** | Course creators, membership businesses, coaching | 50K members |
| **Skool** | Course creators wanting community + course in one | 50K members |
| **Facebook Groups** | Broad consumer audiences (35+), local communities | 250K+ members |
| **Reddit** | Topic-based, technical audiences, organic discovery | Unlimited |
| **Forum Software (Discourse)** | Technical communities, open-source, SEO-driven | Unlimited |

### Platform Selection Matrix

| Factor | Discord | Slack | Circle | Skool | FB Groups | Reddit | Forum |
|--------|---------|-------|--------|-------|-----------|--------|-------|
| **Audience age** | 18-35 | 25-55 | 25-50 | 25-50 | 30-65 | 18-45 | 20-50 |
| **Setup cost** | Free | $$$ | $$ | $ | Free | Free | $-$$$ |
| **Real-time chat** | Strong | Strong | Weak | Weak | Weak | Weak | Weak |
| **Async discussion** | Medium | Medium | Strong | Strong | Strong | Strong | Strong |
| **Gamification** | Bots | None | Limited | Built-in | None | Karma | Trust levels |
| **Branding control** | Medium | Low | High | Medium | None | None | Full |
| **Data ownership** | Low | Medium | Medium | Low | None | None | Full |
| **SEO value** | None | None | Optional | Limited | Low | High | High |

**Decision framework (in priority order):**
1. Where your audience already spends time
2. Communication style (real-time vs async)
3. Ownership and control needs
4. Budget and scale considerations

### When to Use It

**Trigger phrases:**
- "Discord community" / "Slack community"
- "community platform"
- "community-led growth"
- "forum"
- "champions program" / "ambassador program"
- "community engagement strategy"

### Community-Led Growth Model

The CLG flywheel operates in four stages:

1. **Attract:** Community content, member stories, organic search draw new prospects
2. **Activate:** Onboarding converts visitors into participating members within 48 hours
3. **Engage:** Consistent value delivery (events, content, peer support) deepens investment
4. **Advocate:** Engaged members refer others, create content, defend the brand

**Key metrics:**
- Referral rate: Top communities generate 15-25% of new members through member referrals
- Activation rate: First 48 hours determine whether a member stays or ghosts
- Engagement depth: Time to mature = 6-12 months before judging ROI

### Example: Discord Community Launch

**Scenario:** A developer tools company wants to launch a Discord community for their users.

**Pre-Launch (4-8 weeks before):**

1. **Define the one-line promise:** "The place where developers get unstuck on [Product] in under 10 minutes."
2. **Build waitlist:** Landing page with email capture
3. **Recruit founding members:** Personal outreach to 30 power users, beta testers, and vocal customers

**Server Structure (start lean):**

| Channel | Purpose |
|---------|---------|
| #welcome | Read-only rules and introduction |
| #introductions | New member intros |
| #general | Open discussion |
| #help | Product questions |
| #showcase | Member projects |
| #announcements | Company updates |

**Beta Phase (2-4 weeks):**
- Founding members only
- Test workflows, gather feedback
- Identify champions for moderator roles

**Launch Day:**
- Announce across all channels simultaneously
- Launch with an AMA or live session
- 48-hour welcome challenge: "Introduce yourself and share what you're building"

**First 100 Days:**

| Phase | Focus |
|-------|-------|
| Days 1-30 | Foundation: setup, seeding, founding member recruitment |
| Days 31-60 | Launch: public launch, onboarding, first events |
| Days 61-90 | Growth: analyze metrics, refine strategy, scale what works |
| Days 91-100 | Stabilize: establish rhythms, publish first community report |

---

## 9.5 Guerrilla Marketing Specialist

### What It Does

The Guerrilla Marketing Specialist designs and executes unconventional marketing tactics, viral campaigns, competitive disruption strategies, and growth experiments that deliver high-impact results on constrained budgets.

**Core deliverables:**
- Viral campaign designs
- Growth hack experiments
- Competitive disruption strategies
- Budget guerrilla tactics
- Risk assessments for bold campaigns

### Tactic Types

| Category | Description | Typical Cost |
|----------|-------------|--------------|
| **Viral Campaigns** | Designed for high shareability and cultural moment capture | $0-$500 |
| **Growth Hacks** | Low-cost, high-leverage tactics for rapid growth | $0-$200 |
| **Competitive Disruption** | Ambush marketing, competitor moment riding | $100-$500 |
| **Street-Level Marketing** | Stickers, projections, creative QR placement | $50-$300 |
| **Guerrilla Social Media** | Trend-jacking, meme marketing, reply-guy strategy | $0 |
| **Community Infiltration** | Value-first presence in existing communities | $0 (high time) |

### When to Use It

**Trigger phrases:**
- "growth hack"
- "viral campaign"
- "guerrilla marketing"
- "low-budget marketing"
- "marketing stunt"
- "unconventional tactics"
- "competitive disruption"

### Viral Campaign Design Framework

Every viral campaign needs five elements (score each 1-5):

| Element | Question |
|---------|----------|
| **Shareability** | Would someone share this to look smart, funny, or caring? |
| **Emotion** | Does it trigger strong emotion (surprise, laughter, awe, outrage, joy)? |
| **Simplicity** | Can someone explain it in one sentence? |
| **Timing** | Is this culturally relevant right now? |
| **Platform fit** | Is the format native to the distribution platform? |

**Campaigns scoring 20+ have strong viral potential. Below 15, rethink the concept.**

**The sharing test:** People share content that makes them look good. Ask: "Does sharing this make the sharer appear smart, funny, generous, informed, or caring?" If not, redesign.

### Risk Assessment Framework

Every guerrilla tactic must be evaluated before execution:

| Risk Category | Questions to Ask |
|---------------|------------------|
| **Legal** | Does this violate laws, regulations, or platform terms? |
| **Reputational** | Could this backfire? Screenshot test: would this embarrass us? |
| **Financial** | What is worst-case financial exposure? |
| **Operational** | Can we execute reliably? What if logistics fail? |
| **Competitive** | Could competitors use this against us? |

**Go/No-Go Scoring:**
- Score each risk category 1-5 (1 = negligible, 5 = severe)
- Score potential reward 1-10
- Calculate: Reward Score / Average Risk Score

| Ratio | Decision |
|-------|----------|
| Above 3.0 | Strong go |
| 2.0-3.0 | Proceed with mitigation |
| Below 2.0 | Rethink or abandon |

**High-risk indicators (pause and escalate):**
- Legal or reputational risk score 4+
- Involves minors
- Involves health or safety claims
- Targets vulnerable populations
- Uses competitor trademarks
- Requires physical permits or insurance

### Example: Low-Budget Viral Campaign

**Scenario:** A bootstrapped startup has $200 for marketing. They need maximum impact.

**Recommended tactic: Sticker campaign with QR tracking**

**Execution:**

| Step | Action | Cost |
|------|--------|------|
| 1 | Design eye-catching stickers with QR code | $50 (1,000 stickers) |
| 2 | Create unique landing page per placement location | $0 |
| 3 | Place in high-traffic areas target audience frequents | $0 (legs) |
| 4 | Track scans per location to identify best spots | $0 (analytics) |
| 5 | Double down on winning locations | $50 (more stickers) |

**Measurement:**
- QR scans by location
- Landing page conversions
- Cost per acquisition

**Risk assessment:**
- Legal: 2/5 (check local ordinances on sticker placement)
- Reputational: 1/5 (low risk if design is tasteful)
- Financial: 1/5 (max exposure is the $200 budget)
- Operational: 2/5 (execution is straightforward)

**Go/No-Go Ratio:**
- Average risk: 1.5
- Reward score: 6
- Ratio: 4.0 (strong go)

---

## 9.6 Sales Enablement Specialist

### What It Does

The Sales Enablement Specialist builds sales collateral that reps actually use—decks, one-pagers, demo scripts, objection handlers, ROI calculators, champion kits, and battle cards. Every deliverable is anchored to brand positioning and serves the specific deal stage.

**Core deliverables:**
- Sales decks with story arc
- One-pagers (product, executive, technical)
- Objection handling guides
- Demo scripts
- ROI calculators
- Champion kits
- Battle cards (internal only)

### Collateral Types

| Type | When to Use | Audience | Format |
|------|-------------|----------|--------|
| **Sales Deck** | Main presentation | All buyers | 10-12 slides |
| **Product One-Pager** | Post-meeting recap, champion tool | All buyers | 1 page |
| **Executive Summary** | Economic buyer enters late | C-suite | 1 page |
| **Battle Card** | Competitive shortlist | Sales rep only (internal) | 1 page |
| **Technical Brief** | Security/IT review | Technical buyer | 1-2 pages |
| **ROI Calculator** | Proposal support, board approval | Economic buyer | Spreadsheet |
| **Demo Script** | Product demonstrations | All buyers | Script + notes |

### When to Use It

**Trigger phrases:**
- "sales deck" / "pitch deck"
- "one-pager"
- "demo script"
- "objection handling"
- "champion kit"
- "battle card"
- "sales enablement"
- "ROI calculator"

### Customer Language Methodology

**Build what sales actually uses, not what marketing thinks they need.**

| Principle | Application |
|-----------|-------------|
| **One asset, one job** | No Swiss-army-knife collateral |
| **Customer language** | Pull from G2 reviews, call transcripts, interviews—not marketing speak |
| **Scannable over comprehensive** | Reps have 30 seconds mid-call |
| **Every claim needs proof** | Specific metrics and verifiable sources |
| **Deal stage determines content** | Not asset type |

**Example transformation:**

| Marketing Speak | Customer Language |
|-----------------|-------------------|
| "Our AI-powered platform optimizes workflows" | "Teams tell us they used to spend 3 hours a week on this task—now it takes 15 minutes" |
| "Best-in-class solution" | "The only tool that does X, Y, and Z in one place" |
| "Seamless integration" | "Connects to your existing Salesforce in under 10 minutes" |

### Sales Deck Story Arc

A sales deck is not a feature catalog—it's a story where the prospect is the hero:

| Slide | Title | Purpose | Key Rule |
|-------|-------|---------|----------|
| 1 | The Problem | Industry-wide pain, quantified | Lead with stat they recognize; use customer language |
| 2 | Cost of Inaction | Financial/time/reputation cost | Translate pain into money |
| 3 | Market Shift | Why now? (regulation, tech, competition) | Name specific trigger |
| 4 | Our Solution | One clear statement (max 15 words) | "We help [persona] [outcome] by [mechanism]" |
| 5 | Product Walkthrough | 3-4 screens tied to Slide 1 pains | Real UI, presenter notes with talk track |
| 6 | Proof | Customer results, metrics, logos | 3-5 metrics + verbatim quote |
| 7 | Case Study | Before/after/result with numbers | Role, company size, timeframe |
| 8 | How It Works | Implementation overview | 3-step diagram, time-to-value |
| 9 | ROI Summary | Quantify value using prospect's numbers | "Based on what you shared" |
| 10 | Pricing | Starting price or "plans start at" | Lead with most popular plan |
| 11 | Next Steps | One low-friction ask | Specific date + "What would make you confident?" |

### Objection Handling Framework

The ARFA framework for every response:

1. **Acknowledge** — Validate concern without agreeing with premise
2. **Reframe** — Shift from their framing to yours
3. **Respond** — Deliver counter with proof
4. **Advance** — End with forward-moving question

**Objection categories:**

| Category | Common Variants | Core Reframe |
|----------|-----------------|--------------|
| **Price/Budget** | "Too expensive", "No budget" | Shift from price to cost-of-inaction and ROI |
| **Timing** | "Not right time", "In middle of project" | Design phased approach or pre-event evaluation |
| **Competition** | "Evaluating [Competitor]", "Already use [Competitor]" | Surface criteria, address 2-3 you win on |
| **Authority/Buy-In** | "Need buy-in", "Boss needs to approve" | Arm champion with internal meeting materials |
| **Status Quo** | "Happy with current solution" | Probe hidden friction; quantify current cost |
| **Technical/Risk** | "Security?", "How hard to implement?" | Lead with certifications and timelines |

### Example: Sales Deck Creation

**Scenario:** A B2B SaaS company needs a new sales deck for their account executives.

**Story arc development:**

**Slide 1 - The Problem:**
> "Marketing teams waste 12 hours per week pulling reports from 6 different tools."

**Slide 2 - Cost of Inaction:**
> "That's $52K per year in lost productivity for a 5-person team—plus delayed decisions that cost deals."

**Slide 3 - Market Shift:**
> "In 2025, privacy changes broke 40% of traditional tracking. The teams that adapted are winning."

**Slide 4 - Our Solution:**
> "We help marketing teams get real-time insights from all their tools in one dashboard, without logging into 6 platforms."

**Slide 5 - Product Walkthrough:**
> [3 UI screens: unified dashboard, automated reports, alert system]

**Slide 6 - Proof:**
> "Teams report saving 10+ hours per week and making decisions 3x faster."
> — 500+ customers including [recognizable logos]

**Slide 7 - Case Study:**
> "Acme Corp reduced reporting time from 8 hours to 30 minutes per week, leading to 23% more campaigns launched."

**Slide 8 - How It Works:**
> 1. Connect your tools (10 minutes)
> 2. Customize your dashboard
> 3. Set automated reports

**Slide 9 - ROI Summary:**
> "Based on your team size, you'd save ~$48K/year in productivity. Payback: 2 months."

**Slide 10 - Pricing:**
> "Plans start at $99/month. Most teams your size choose Pro at $249/month."

**Slide 11 - Next Steps:**
> "Would a 14-day trial help you evaluate? What would you need to feel confident?"

---

## Summary: Specialized Skills Quick Reference

| Skill | Primary Function | Key Trigger Phrases | Main Deliverable |
|-------|------------------|---------------------|------------------|
| **Marketing Analytics** | Tracking, dashboards, attribution, A/B testing | GA4, GTM, analytics, dashboard, attribution | Measurement plan, tracking spec |
| **Pricing Strategy** | Pricing models, tiers, willingness-to-pay | Pricing tiers, value metric, pricing page | Pricing strategy document |
| **Marketing Psychology** | Behavioral science and persuasion | Cognitive bias, Cialdini, persuasion, social proof | Copy rewrites with rationale |
| **Community Building** | Owned community platforms | Discord community, Slack community, community-led growth | Community launch plan |
| **Guerrilla Marketing** | Unconventional tactics, viral campaigns | Growth hack, viral campaign, guerrilla marketing | Campaign design with risk assessment |
| **Sales Enablement** | Sales collateral that reps use | Sales deck, one-pager, objection handling | Deck, one-pager, objection guide |

All specialized skills integrate with the SOSTAC framework and reference brand context when available. They escalate to other skills when requests fall outside their domain.