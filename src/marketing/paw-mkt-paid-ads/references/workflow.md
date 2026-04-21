# Paid Ads Workflow

This reference defines the standard PPC Campaign Lifecycle, diagnostic questions, platform-specific considerations, budget allocation frameworks, escalation routes, and ethical guidelines that govern all paid advertising work.

---

## PPC Campaign Lifecycle

Work through each phase sequentially. Launching ads without completing Phases 1-5 is spending money without a measurement system — the most expensive kind of marketing mistake.

### Phase 1: Audit & Discovery

**Purpose:** Understand the current state before making changes. Assess existing account structure, historical performance, tracking accuracy, and competitive landscape.

**Entry conditions:**
- Brand context is loaded (SOSTAC plan, product positioning, or brand brief)
- Ad platform access confirmed (Google Ads, Meta Business Manager, LinkedIn Campaign Manager, etc.)
- Budget range is known or estimable

**Diagnostic questions:**
1. **Current state**: Are there existing ad accounts? What is the monthly spend? What is the current ROAS/CPA? How long has the account been active?
2. **Business model**: Is the goal leads, e-commerce sales, app installs, SaaS trials, or brand awareness? What is the average order value / contract value?
3. **Unit economics**: What is the target CPA or ROAS? What CAC can the business sustain? What is the LTV of a customer?
4. **Audience**: Who is the ideal customer? What are their demographics, job titles, interests, pain points? Where do they spend time online?
5. **Competitive landscape**: Who are the top 3-5 competitors running paid ads? What channels and messaging do they use?
6. **Creative assets**: What ad creative exists? (Images, videos, landing pages, copy.) What is the creative production capacity?
7. **Tracking**: Is conversion tracking in place? What attribution model is active? Are offline conversions being uploaded?
8. **Constraints**: Are there brand guidelines, compliance requirements, restricted keywords, or geographic limitations?

If the user cannot answer questions 1-3, recommend defining business objectives and unit economics before launching any paid campaigns. Paid ads without target CPA/ROAS is spending without guardrails.

**Key activities:**

#### Account Structure Review (if existing account)

| Element | What to Audit | Red Flags |
|---|---|---|
| Campaign structure | Campaign types, naming conventions, organization | Too many campaigns with <$10/day budget each; no naming convention |
| Ad group structure | Theme coherence, keyword grouping, audience segmentation | 50+ keywords per ad group; mixed intent in single ad group |
| Keyword strategy | Match types, negative keywords, search term reports | Broad match only; no negative keyword lists; irrelevant search terms |
| Bidding strategy | Bid strategy per campaign, target CPA/ROAS settings | Manual CPC on high-volume campaigns; target CPA set below historical average |
| Quality Score | Keyword-level QS, ad relevance, landing page experience | Average QS below 5; high-spend keywords with QS 3-4 |
| Creative | Ad copy variants, asset diversity, creative freshness | Single ad per ad group; no RSA testing; creative older than 90 days |
| Audiences | Audience lists, remarketing setup, exclusions | No remarketing audiences; no customer list uploads; no exclusions |
| Conversion tracking | Conversion actions, attribution window, value tracking | Missing conversion actions; default attribution; no value data |

#### Historical Performance Analysis
- Pull 90-day and 12-month performance data (if available)
- Identify top-performing campaigns, ad groups, keywords, and audiences
- Identify wasted spend: high-cost, low-conversion segments
- Calculate actual CPA and ROAS by campaign and channel
- Identify seasonal patterns and trend direction

**Deliverables:**
- Account Audit Report: current state, performance summary, structural issues, wasted spend analysis
- Competitive Intelligence Brief: competitor ad messaging, channels, estimated spend, positioning gaps

**Exit conditions:**
- Current account performance is documented with key metrics
- Structural issues and wasted spend are identified
- Competitive landscape is mapped
- Proceed to Strategy & Platform Selection

---

### Phase 2: Strategy & Platform Selection

**Purpose:** Match the business objective, audience, and budget to the right platform mix. Not every business should be on every platform — channel fit determines success.

**Entry conditions:**
- Phase 1 complete — audit findings are available
- Business objectives and unit economics are defined
- Target audience is characterized

**Key activities:**

#### Channel Fit Analysis

| Platform | Best For | Minimum Monthly Budget | Audience Signal |
|---|---|---|---|
| **Google Search** | High-intent capture, bottom-funnel | $1,000+ | Active search intent; knows they have a problem |
| **Google Performance Max** | Full-funnel automated campaigns | $3,000+ | Mixed intent; Google-managed signals |
| **Meta (Facebook/Instagram)** | Awareness, consideration, retargeting; visual products | $1,500+ | Interest/behavior-based; interruption model |
| **LinkedIn** | B2B lead gen, account-based marketing, recruiting | $3,000+ | Job title, company size, industry targeting |
| **TikTok** | Awareness, younger demographics, viral creative | $1,500+ | Interest/behavior-based; entertainment context |
| **YouTube** | Brand awareness, consideration, remarketing | $2,000+ | Interest/intent-based; video engagement |
| **Reddit** | Niche communities, developer/tech audiences | $500+ | Subreddit-based; community context |
| **Programmatic/Display** | Retargeting, awareness at scale | $2,000+ | Contextual, behavioral, or list-based |

#### Platform Selection Decision Framework

Answer these questions to select channels:

1. **Is the audience actively searching for solutions?** -> Google Search is mandatory
2. **Is the product visual or demonstrable?** -> Meta and TikTok are strong candidates
3. **Is this B2B with identifiable job titles?** -> LinkedIn is the primary platform
4. **Is the budget under $3K/month total?** -> Focus on ONE platform rather than spreading thin
5. **Is remarketing possible (existing traffic)?** -> Add remarketing across platforms regardless of primary channel
6. **Is the sales cycle longer than 30 days?** -> Multi-touch, multi-platform strategy required

#### Budget Allocation Framework

| Scenario | Allocation Model |
|---|---|
| **New account, proving concept** | 100% on single highest-fit platform. Prove unit economics before diversifying. |
| **Proven single channel, scaling** | 70% proven channel, 20% next-highest-fit channel, 10% testing budget |
| **Multi-channel, optimizing** | Allocate by channel ROAS with 10-15% held for testing new channels/audiences |
| **Mature program** | Use Marketing Mix Modeling or incrementality testing to guide allocation |

**Budget minimums by objective:**

| Objective | Minimum Monthly to Learn | Minimum Monthly to Scale |
|---|---|---|
| Lead generation (B2B) | $2,000 | $5,000+ |
| E-commerce sales | $1,500 | $5,000+ |
| SaaS trial signups | $1,500 | $3,000+ |
| Brand awareness | $3,000 | $10,000+ |
| App installs | $2,000 | $5,000+ |

**Deliverables:**
- Channel Strategy Document: selected platforms with rationale, budget allocation, expected performance ranges
- Audience Strategy: primary and secondary audiences per platform, exclusion lists, remarketing plan

**Exit conditions:**
- Platform mix is selected with budget allocated
- Audience strategy is defined per platform
- Expected CPA/ROAS ranges are documented (based on benchmarks + audit data)
- Proceed to Campaign Architecture

---

### Phase 3: Campaign Architecture

**Purpose:** Build a scalable, organized account structure that enables clear performance measurement, controlled budget allocation, and systematic optimization.

**Entry conditions:**
- Phase 2 complete — platforms selected, budget allocated, audiences defined
- Landing pages identified or in development
- Conversion tracking requirements documented

**Key activities:**

#### Account Structure Best Practices

**Google Ads structure:**

```
Account
  -> Campaign (by objective + match type or audience tier)
    -> Ad Group (by theme/keyword cluster or audience segment)
      -> Keywords (tightly themed, 5-15 per ad group)
      -> Ads (3+ RSA variants per ad group)
      -> Extensions (sitelinks, callouts, structured snippets)
```

**Meta Ads structure:**

```
Account
  -> Campaign (by objective: conversions, traffic, awareness)
    -> Ad Set (by audience segment)
      -> Ads (3-6 creative variants per ad set)
```

**Naming conventions (universal):**

`[Platform]_[Objective]_[Audience/Targeting]_[Geography]_[Creative Type]_[Date]`

Example: `GOOG_Search_Brand_US_RSA_2024Q3`
Example: `META_Conv_Lookalike-Purchasers_US_Video_2024Q3`

#### Bidding Strategy Selection

| Strategy | When to Use | Minimum Data |
|---|---|---|
| Manual CPC | Account launch with no historical data; testing new keywords | N/A |
| Maximize Conversions | Sufficient conversion volume, budget-constrained | 15+ conversions/month |
| Target CPA | Stable CPA goal with consistent conversion volume | 30+ conversions/month per campaign |
| Target ROAS | E-commerce or value-based bidding with conversion value data | 50+ conversions/month per campaign |
| Maximize Conversion Value | High-value variance, want algorithm to optimize for value | 50+ conversions/month per campaign |

**Bidding rules:**
- Never set target CPA below your historical average CPA — the algorithm will starve the campaign
- Allow 2-4 weeks for Smart Bidding to learn before evaluating performance
- Do not make bid strategy changes more frequently than every 2 weeks
- Use portfolio bid strategies when campaigns share similar goals and conversion types

#### Audience Architecture

| Audience Tier | Platform | Source | Use Case |
|---|---|---|---|
| **Tier 1: Remarketing** | All platforms | Website visitors, cart abandoners, trial users | Highest ROAS; close warm leads |
| **Tier 2: Customer Match** | Google, Meta, LinkedIn | CRM lists (email, phone) | Upsell, cross-sell, exclusion |
| **Tier 3: Lookalikes** | Meta, LinkedIn, Google | Based on converters or high-value customers | Scale beyond existing audiences |
| **Tier 4: Interest/Behavior** | Meta, TikTok, LinkedIn | Platform-defined segments | Prospecting; awareness |
| **Tier 5: Broad/Keyword** | Google Search, YouTube | Search intent, contextual | Intent capture; widest reach |

**Deliverables:**
- Campaign Architecture Document: complete account structure, naming conventions, campaign types, ad group organization
- Bidding Strategy Plan: strategy per campaign with rationale and expected learning period
- Audience Plan: tiered audience architecture with source data requirements

**Exit conditions:**
- Account structure is documented and reviewable before build
- Bidding strategies are selected with minimum data requirements noted
- Audience architecture covers all funnel stages
- Proceed to Creative Production

---

### Phase 4: Creative Production

**Purpose:** Produce ad creative that earns attention, communicates value, and drives action. Creative quality is the primary scaling lever in modern paid media — algorithm optimization has a ceiling; creative does not.

**Entry conditions:**
- Phase 3 complete — campaign structure and audiences are defined
- Brand guidelines are available (tone, visual identity, messaging pillars)
- Landing pages are identified for each campaign

**Key activities:**

#### Ad Copy Framework

Every ad must contain three elements:
1. **Hook**: Captures attention in the first 2 seconds (video) or first line (text). Speaks to the audience's problem, desire, or identity.
2. **Value Proposition**: What the product does, who it is for, and why it matters — specific, not generic.
3. **Call to Action**: Clear next step with reduced friction ("Start Free Trial" not "Learn More" when possible).

#### Platform-Specific Creative Specs

| Platform | Format | Key Specs | Best Practices |
|---|---|---|---|
| **Google Search** | RSA | 15 headlines (30 chars), 4 descriptions (90 chars) | Mix keyword, benefit, CTA, urgency, and social proof headlines. Pin sparingly. |
| **Google Display** | Responsive display | Multiple images, headlines, descriptions, logos | Provide 5+ images in all aspect ratios; test video assets |
| **Meta Feed** | Image/Video + text | Primary text (125 chars visible), headline, description | Lead with hook in primary text; 4:5 or 1:1 image ratio; 15-30s video |
| **Meta Stories/Reels** | Full-screen vertical video | 9:16 ratio, 15-60s | Native feel; text overlays; strong first 3 seconds |
| **LinkedIn** | Single image/video/carousel | Primary text (150 chars above fold), headline | Professional tone; specific metrics/results; speak to job role |
| **TikTok** | Vertical video | 9:16 ratio, 15-60s | Creator-style; hook in first second; fast pacing; trending audio |

#### Creative Testing Framework

| Test Type | What to Test | Minimum Variants | Evaluation Period |
|---|---|---|---|
| **Hook test** | First line of copy or first 3s of video | 3-5 hooks | 7 days or 1,000 impressions per variant |
| **Value prop test** | Different benefits or angles | 2-3 angles | 14 days or sufficient conversions |
| **Format test** | Image vs. video vs. carousel | 2-3 formats | 14 days |
| **CTA test** | Different calls to action | 2-3 CTAs | 14 days or sufficient conversions |
| **Audience-creative match** | Same creative across different audiences | N/A (audience variable) | 14 days |

**Creative refresh cadence:**
- Meta/TikTok: refresh creative every 2-4 weeks (fatigue sets in faster on social)
- Google Search: refresh ad copy every 4-8 weeks; add new RSA variants
- LinkedIn: refresh every 4-6 weeks
- Display/Programmatic: refresh every 4-8 weeks

#### Landing Page Alignment

Every ad must land on a page that continues the conversation:

- **Message match**: The landing page headline must reflect the ad's promise. If the ad says "Cut Reporting Time by 80%," the landing page headline must reinforce that specific claim.
- **Audience match**: Landing pages for cold traffic need more context and trust signals than remarketing pages.
- **CTA match**: The landing page CTA should match the ad's promised action. "Start Free Trial" should land on a page with a free trial signup, not a generic homepage.
- **Speed**: Landing pages must load in under 3 seconds on mobile. Every second of delay costs ~7% in conversion rate.

**Deliverables:**
- Ad Creative Brief: per campaign — messaging angles, headlines, descriptions, visual direction
- Ad Copy Variants: production-ready copy for each platform and format
- Creative Testing Plan: test matrix with variants, success metrics, and evaluation timeline

**Exit conditions:**
- Ad creative is produced for all campaigns and formats
- Landing page alignment is verified for every ad -> landing page combination
- Creative testing plan is documented
- Proceed to Tracking Setup

---

### Phase 5: Tracking Setup

**Purpose:** Ensure every dollar spent can be measured back to a business outcome. Tracking setup is the bridge between ad spend and revenue attribution.

**Entry conditions:**
- Phase 4 complete — campaigns and creative are ready
- Landing pages are live or in staging
- Analytics infrastructure is in place (GA4, GTM, or equivalent)

**Key activities:**

#### Conversion Tracking Checklist

| Platform | Tracking Method | Required Setup |
|---|---|---|
| **Google Ads** | Google Tag (gtag.js) or GTM | Conversion actions defined; conversion value set; enhanced conversions enabled |
| **Meta** | Meta Pixel + Conversions API (CAPI) | Pixel installed; CAPI configured; events mapped to funnel stages |
| **LinkedIn** | Insight Tag + Conversions API | Insight Tag installed; conversion events defined; CAPI for accuracy |
| **TikTok** | TikTok Pixel + Events API | Pixel installed; Events API configured; events mapped |
| **Google Analytics 4** | GA4 tag via GTM | Events configured; conversions marked; audiences built |

**Critical tracking requirements:**
- **Enhanced conversions** (Google): hash and send first-party data (email, phone) for higher match rates
- **Conversions API** (Meta, LinkedIn, TikTok): server-side event sending for accurate measurement with cookie restrictions
- **Offline conversion import** (all platforms): upload CRM data (lead -> MQL -> SQL -> closed/won) for true ROI measurement
- **Value-based bidding**: send conversion values (revenue, deal size) to enable ROAS-based optimization

#### Attribution Model Selection

| Model | Platform | Best For | Setup |
|---|---|---|---|
| Data-driven | Google Ads, GA4 | Default for most accounts | Automatic with sufficient data |
| Last-click | All platforms | Simple, clear attribution | Default fallback |
| 7-day click, 1-day view | Meta | Standard social attribution | Meta default; adjust window by sales cycle |
| 30-day click | LinkedIn | B2B with longer consideration | Recommended for B2B |
| Custom | GA4 | Multi-channel analysis | Requires GA4 configuration |

#### UTM Parameter Requirements

All paid traffic must use consistent UTM parameters:

| Parameter | Paid Ads Standard | Example |
|---|---|---|
| `utm_source` | Platform name | `google`, `meta`, `linkedin`, `tiktok` |
| `utm_medium` | `cpc`, `cpm`, `paid-social` | `cpc` (search), `paid-social` (social ads) |
| `utm_campaign` | Campaign name (match ad platform naming) | `q3-brand-search`, `retargeting-cart-abandoners` |
| `utm_term` | Keyword or audience name | `{keyword}` (auto), `lookalike-purchasers` |
| `utm_content` | Ad variant identifier | `headline-a-video-v2`, `carousel-testimonials` |

**Auto-tagging**: Enable auto-tagging (gclid) in Google Ads alongside manual UTM parameters for full data in both GA4 and Google Ads reporting.

**Deliverables:**
- Conversion Tracking Spec: per platform — events, values, attribution windows, server-side setup
- Tracking QA Checklist: test procedures for each conversion event
- UTM Parameter Map: mapping of campaigns to UTM values

**Exit conditions:**
- All conversion events fire correctly in staging/preview
- Server-side tracking is configured for primary platforms
- UTM parameters are consistent across all campaign URLs
- Tracking QA is complete — proceed to Launch

---

### Phase 6: Launch & QA

**Purpose:** Catch errors before they cost money. A systematic pre-launch review prevents the most common (and most expensive) paid media mistakes.

**Entry conditions:**
- Phases 1-5 complete — strategy, structure, creative, and tracking are ready
- Budget is approved and billing is configured
- Stakeholders are informed of launch timeline

**Key activities:**

#### Pre-Launch Checklist

| Category | Check | Status |
|---|---|---|
| **Billing** | Payment method active; budget caps set at account and campaign level | [ ] |
| **Targeting** | Geographic targeting correct; language targeting set; audience exclusions active | [ ] |
| **Negative keywords** | Negative keyword lists applied (Google); brand terms excluded from prospecting (if applicable) | [ ] |
| **Audiences** | Remarketing audiences populated (minimum 100 users for Google, 1,000 for Meta); exclusions set | [ ] |
| **Ad copy** | All ads approved by platform; no policy violations; final URL correct | [ ] |
| **Landing pages** | Pages live and loading in <3s; mobile-responsive; CTA functional; tracking fires | [ ] |
| **Conversion tracking** | All conversion events verified in platform debug/preview mode | [ ] |
| **Budget** | Daily/lifetime budgets set correctly; no overspend risk on day 1 | [ ] |
| **Bid strategy** | Correct bid strategy applied; target CPA/ROAS set at viable level | [ ] |
| **Schedule** | Ad schedule set (if not 24/7); time zone correct | [ ] |
| **Extensions** | Sitelinks, callouts, structured snippets, call extensions (Google) configured | [ ] |
| **Attribution** | Attribution model confirmed; attribution window set | [ ] |

#### Campaign Activation Protocol
1. Launch campaigns in the morning (platform local time) to allow full-day monitoring
2. Set conservative initial budgets — 50-75% of target daily budget for the first 3 days
3. Enable all campaigns simultaneously (unless phased launch is planned)
4. Verify spend is pacing correctly within 2 hours of launch
5. Check conversion tracking fires within 4 hours (or with first conversions)

#### Day-1 Monitoring Checklist
- [ ] Impressions are serving (all campaigns)
- [ ] Clicks are registering (check for 0-click campaigns)
- [ ] Spend is within expected range (no budget overshoot)
- [ ] Conversion tracking is recording (at least test conversions)
- [ ] Search term report shows relevant queries (Google Search)
- [ ] Ad approval status — no disapproved ads
- [ ] Landing pages are loading correctly (spot-check on mobile)
- [ ] No unexpected audience overlap or exclusion issues

**Deliverables:**
- Pre-Launch QA Report: completed checklist with sign-off
- Launch Confirmation: campaigns live, initial metrics within expected range
- Day-1 Monitoring Report: early performance snapshot, any issues identified

**Exit conditions:**
- All campaigns are live and serving
- Conversion tracking is confirmed working
- No critical issues identified in Day-1 monitoring
- Proceed to Optimization Cycle

---

### Phase 7: Optimization Cycle

**Purpose:** Systematically improve campaign performance through data-driven adjustments. Optimization is continuous — not a one-time activity.

**Entry conditions:**
- Phase 6 complete — campaigns are live with verified tracking
- Minimum 7 days of data (14 days preferred for Smart Bidding)
- Conversion data is flowing accurately

**Key activities:**

#### Optimization Cadence

| Timeframe | Focus | Actions |
|---|---|---|
| **Daily** | Anomaly detection | Check spend pacing, conversion volume, any sudden metric changes. Add negative keywords from search term reports (Google). |
| **Weekly** | Performance review | Analyze by campaign, ad group, audience, creative. Pause underperformers. Increase budget on winners. Adjust bids. |
| **Bi-weekly** | Creative refresh assessment | Evaluate creative fatigue (rising CPA, declining CTR). Plan and launch new creative variants. |
| **Monthly** | Strategic review | Channel-level ROAS/CPA analysis. Budget reallocation across channels. Audience expansion/contraction. Test new campaign types. |
| **Quarterly** | Full audit | Complete account audit (repeat Phase 1 scope). Strategy alignment with business objectives. Platform mix review. |

#### Optimization Decision Framework

| Signal | Diagnosis | Action |
|---|---|---|
| High impressions, low CTR | Ad relevance issue or audience mismatch | Test new creative; refine targeting; review ad-audience fit |
| High CTR, low conversions | Landing page issue or audience quality issue | Audit landing page; check message match; review audience intent |
| High CPA, sufficient volume | Efficiency issue | Tighten targeting; test creative; optimize bidding; improve landing page |
| Low impressions | Budget too low, targeting too narrow, or bid too low | Increase budget, broaden targeting, or raise bids |
| Declining ROAS over time | Audience saturation or creative fatigue | Expand audiences; refresh creative; test new channels |
| Inconsistent daily performance | Insufficient budget for algorithm learning | Consolidate campaigns; increase daily budget to 10x target CPA minimum |

#### Budget Scaling Rules

| Scaling Scenario | Rule |
|---|---|
| Campaign hitting CPA target consistently (2+ weeks) | Increase budget by 20-30% per week maximum |
| Campaign above CPA target | Do NOT scale. Optimize first: creative, landing page, audiences |
| Testing new audience or channel | Allocate 10-15% of total budget; run for 14+ days before judging |
| Seasonal opportunity | Pre-build creative and audiences 2-3 weeks before expected demand increase |
| Budget cuts required | Cut lowest-ROAS campaigns first; protect remarketing and high-intent campaigns |

#### Creative Rotation Protocol

| Metric | Fatigue Signal | Action |
|---|---|---|
| CTR | Declining 20%+ from initial performance | Replace creative; new hook or visual treatment |
| Frequency | Above 3.0 (Meta/social), above 5.0 (remarketing) | Expand audience or refresh creative |
| CPA | Rising 15%+ with stable CTR | Test new value prop angles; refresh landing page |
| Relevance/Quality score | Declining | Update ad copy to match current audience needs; improve landing page |

**Deliverables:**
- Weekly Optimization Log: changes made, rationale, expected impact
- Monthly Performance Report: channel-level metrics, budget vs. actual, optimization actions, next-month plan
- Quarterly Strategy Review: full account assessment, strategic recommendations, budget reallocation proposal

**Exit conditions:**
- Optimization cycle is active and documented
- Performance trends are positive or stabilized with clear action plans
- Stakeholders receive regular performance reporting

---

## Escalation Routes

Paid ads work frequently surfaces needs that require other skills:

| Finding | Escalate To | Context to Pass |
|---|---|---|
| Landing page conversion rate below benchmark | **paw-mkt-cro** | Landing page URL, traffic source, current CVR, bounce rate, ad messaging |
| Attribution data shows cross-channel complexity | **paw-mkt-analytics** | Attribution model data, channel interaction paths, conversion lag data |
| Ad copy needs brand voice refinement | **paw-mkt-content** | Current ad copy, brand guidelines, audience context, performance data |
| Email nurture needed for lead gen campaigns | **paw-mkt-email** | Lead source, qualification criteria, current follow-up process |
| Organic keywords cannibalizing paid keywords | **paw-mkt-seo** | Keyword overlap data, organic rankings, paid keyword performance |
| Pricing objection surfacing in ad performance | **paw-mkt-pricing** | Ad performance by pricing mention, competitor pricing context |
| Retargeting audience too small | **paw-mkt-content** or **paw-mkt-seo** | Current traffic volume, content gaps, organic growth opportunities |
| Campaign strategy needs full marketing alignment | **paw-mkt-agent-agency** | Campaign performance, channel mix, budget allocation, strategic objectives |

**Escalation protocol**: When escalating, always provide: (1) the specific metric and its current value, (2) the platform and campaign context, (3) the business impact, (4) any diagnosis already performed. Do not escalate raw platform data without interpretation.

---

## Ethics: Ad Transparency & Responsible Advertising

Paid advertising has regulatory requirements and ethical obligations. Compliance is non-negotiable; ethical advertising is a competitive advantage.

### Ethical Advertising Principles

- **Truthful claims**: Every claim in ad copy must be substantiated. "Best in class" requires proof. "#1 rated" requires a verifiable source. Performance claims need evidence.
- **Clear disclosure**: Sponsored content, affiliate relationships, and paid partnerships must be disclosed per FTC guidelines and platform policies.
- **Fair comparison**: Competitor comparisons must be factual and verifiable. Do not misrepresent competitor capabilities or pricing.
- **Honest urgency**: Time-limited offers actually expire. "Limited spots" means limited spots. Countdown timers reflect real deadlines.
- **Respectful targeting**: Do not exploit vulnerable populations, personal hardships, or sensitive categories for targeting advantage.
- **Landing page honesty**: The ad promise must be fulfilled on the landing page. Bait-and-switch (ads for one offer, landing page for another) violates both ethics and platform policies.

### Platform-Specific Compliance

| Platform | Key Policy Areas | Common Violations |
|---|---|---|
| **Google Ads** | Misleading content, trademark use, healthcare claims, financial services | Superlative claims without proof, trademark in ad copy without authorization |
| **Meta** | Personal attributes, discrimination, special categories (housing, credit, employment) | "Are you..." targeting copy, age/gender exclusions on housing ads |
| **LinkedIn** | Professional content standards, data use | Misleading job title targeting, scraping profile data |
| **TikTok** | Age-appropriate content, prohibited products | Targeting minors, restricted product categories |

### Dark Patterns to Avoid in Paid Ads

| Pattern | Description | Why It Harms |
|---|---|---|
| Bait-and-switch | Ad promises one offer; landing page shows different/worse offer | Policy violations, refunds, brand damage, account suspension |
| Fake scarcity in ads | "Only 3 left!" when inventory is unlimited | FTC enforcement risk; erodes trust when discovered |
| Misleading pricing | Showing low price in ad; real price higher with fees | Chargebacks, policy violations, negative reviews |
| Cloaking | Showing different content to ad reviewers vs. real users | Immediate account ban on all platforms |
| Targeting exploitation | Using sensitive data (health, financial stress) to target vulnerable users | Ethical violation; regulatory risk; brand damage |
| Engagement bait | "Comment YES to get..." without actual fulfillment | Policy violations; erodes audience trust |
| Competitor impersonation | Using competitor brand terms or logos to mislead | Trademark violations; legal risk; account suspension |

### The Business Case for Ad Transparency

Deceptive ads create short-term clicks and long-term damage:
- **Account risk**: Policy violations lead to ad disapprovals, account suspensions, and permanent bans
- **Quality Score impact**: Misleading ads get low relevance scores, increasing CPC over time
- **Conversion quality**: Misleading ads attract wrong-fit users who churn, request refunds, and leave negative reviews
- **Brand perception**: Users remember and share negative ad experiences

Transparent ads attract qualified users who convert, retain, and refer.

Before publishing any ad, ask: **If the user who clicks this ad reads the landing page, will they feel the ad accurately represented what they would find?** If not, rewrite the ad.

---

## Path Resolution: Campaign vs Standalone

**Campaign mode** — working within a named campaign:
  -> Save to `./.pawbytes/marketing-suites/brands/{brand-slug}/campaigns/{type}-{campaign-slug}/channels/paid-ads/content/`
  -> Read campaign strategy at `./.pawbytes/marketing-suites/brands/{brand-slug}/campaigns/{type}-{campaign-slug}/strategy.md`

**Standalone mode** — evergreen or independent work:
  -> Save to `./.pawbytes/marketing-suites/brands/{brand-slug}/channels/paid-ads/content/`

**Legacy fallback** — old directory structure detected:
  -> Save to `./.pawbytes/marketing-suites/brands/{brand-slug}/campaigns/paid-ads/`
  -> Suggest migration to new structure

If unsure which mode, ask: "Is this part of a specific campaign, or standalone work?"

---

## Deliverables

All paid ads work saves to the resolved path (see Path Resolution above).

| Deliverable | Filename | Key Sections |
|---|---|---|
| Account Audit | `audit-{platform}-{YYYY-MM-DD}.md` | Current state, structure assessment, performance analysis, wasted spend, recommendations |
| Campaign Strategy | `strategy-{campaign-slug}-{YYYY-MM-DD}.md` | Objectives, platform selection, budget allocation, audience strategy, creative approach |
| Campaign Architecture | `architecture-{platform}-{YYYY-MM-DD}.md` | Account structure, naming conventions, campaigns, ad groups, bidding strategies |
| Ad Creative Brief | `creative-brief-{campaign-slug}-{YYYY-MM-DD}.md` | Messaging angles, headlines, descriptions, visual direction, per-platform specs |
| Ad Copy | `ad-copy-{platform}-{campaign-slug}-{YYYY-MM-DD}.md` | Production-ready ad copy variants for all formats |
| Tracking Setup Spec | `tracking-spec-{YYYY-MM-DD}.md` | Conversion events, pixel/API setup, attribution settings, UTM map |
| Pre-Launch QA | `launch-qa-{campaign-slug}-{YYYY-MM-DD}.md` | Completed checklist, sign-off, known issues |
| Performance Report | `report-{platform}-{YYYY-MM}-{YYYY-MM-DD}.md` | Metrics, trends, optimizations made, recommendations |
| Quarterly Review | `quarterly-review-{YYYY}-Q{N}-{YYYY-MM-DD}.md` | Full account assessment, strategic recommendations, budget proposals |

File structure:

```
# Campaign mode:
./.pawbytes/marketing-suites/brands/{brand-slug}/campaigns/{type}-{campaign-slug}/channels/paid-ads/content/
  audit-{platform}-{YYYY-MM-DD}.md
  strategy-{campaign-slug}-{YYYY-MM-DD}.md
  architecture-{platform}-{YYYY-MM-DD}.md
  creative-brief-{campaign-slug}-{YYYY-MM-DD}.md
  ad-copy-{platform}-{campaign-slug}-{YYYY-MM-DD}.md
  tracking-spec-{YYYY-MM-DD}.md
  launch-qa-{campaign-slug}-{YYYY-MM-DD}.md
  report-{platform}-{YYYY-MM}-{YYYY-MM-DD}.md

# Standalone mode:
./.pawbytes/marketing-suites/brands/{brand-slug}/channels/paid-ads/content/
  (same structure as above)
```

---

## Response Protocol

When the user requests paid ads work:

1. **Route the starting context** (see `./references/shared-patterns.md` for Starting Context Router). Decide whether this is audit, strategy, campaign build, optimization, or reporting work.
2. **Read the strongest available context** (Pre-Flight): brand and SOSTAC first when available; then existing account data and performance history.
3. **Identify the platform and scope.** Read the appropriate reference file before producing recommendations:
   - Google Ads -> `./references/google-ads.md`
   - Meta Ads -> `./references/meta-ads.md`
   - LinkedIn Ads -> `./references/linkedin-ads.md`
   - TikTok Ads -> `./references/tiktok-ads.md`
   - Programmatic/Display -> `./references/programmatic.md`
   - Creative strategy -> `./references/creative-strategy.md`
   - Campaign strategy -> `./references/campaign-strategy.md`
   - Competitive research -> `./references/competitive-research.md`
   - Benchmarks -> `./references/benchmarks.md`
4. **Ask the diagnostic questions** from Phase 1 if the user has not already provided this context. Do not produce campaign recommendations without knowing business objectives, unit economics, and current state.
5. **Work through the PPC Campaign Lifecycle phases** in order. If the user requests a specific phase (e.g., "write ad copy"), verify that prerequisite phases are addressed or explicitly skipped.
6. **Deliver platform-specific output.** Follow platform specs exactly — character limits, format requirements, and policy constraints.
7. **Save deliverables** to the resolved path (see Path Resolution).
8. **Recommend next steps**: What to launch immediately, what to test first, when to review performance, what optimization cadence to follow.

### When to escalate

- Landing page conversion issues identified -- route to **paw-mkt-cro** skill with page performance data and ad messaging context.
- Attribution complexity requires deeper analytics setup -- route to **paw-mkt-analytics** skill with tracking requirements and conversion data.
- Ad copy needs alignment with content strategy or brand voice -- route to **paw-mkt-content** skill with current copy, performance data, and brand guidelines.
- Email sequences needed for lead nurturing from ad campaigns -- route to **paw-mkt-email** skill with lead source, volume, and qualification criteria.
- SEO keyword overlap or organic cannibalization -- route to **paw-mkt-seo** skill with keyword data and organic ranking context.
- Pricing strategy questions surfacing from ad performance data -- route to **paw-mkt-pricing** skill with competitive context and conversion data.
- Brand positioning or messaging questions -- route to **paw-mkt-product-context** or brand context update.
