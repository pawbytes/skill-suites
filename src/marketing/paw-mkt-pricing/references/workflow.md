# Pricing Workflow: Pricing Strategy Pipeline

This reference defines the standard workflow, diagnostic questions, phase gates, and methodology for all pricing strategy work.

---

## Core Principle: Diagnosis Before Prescription

The most common pricing mistake is jumping to a recommendation ("charge $49/month with three tiers") without understanding the pricing problem type. A price-point issue requires different treatment than a packaging issue. A competitive response requires different urgency than a new-product pricing exercise.

**Phase 1 (Problem Classification) is a mandatory gate.** No pricing recommendation may be produced without first classifying the problem type and completing Phase 2 research. Pricing decisions based on intuition or "what feels right" systematically leave money on the table or drive away customers.

---

## Phase 1: Problem Classification

### Purpose
Diagnose the pricing problem type before exploring solutions. Different pricing problems require fundamentally different approaches, research methods, and timelines.

### Entry Conditions
- User has requested pricing-related work
- Brand context loaded (or acknowledged as unavailable)
- SOSTAC plan consulted if available

### Key Activities

#### 1.1 Classify the Pricing Problem

Every pricing engagement falls into one of four categories:

| Problem Type | Symptoms | Urgency | Typical Timeline |
|---|---|---|---|
| New pricing | Launching a new product or entering a new market; no existing price | Medium | 2-4 weeks |
| Price optimization | Revenue plateauing, win rates declining, ARPU flat, expansion revenue stalled | Medium-Low | 1-3 weeks |
| Restructuring | Current model fundamentally broken (wrong value metric, confusing tiers, misaligned packaging) | High | 3-6 weeks |
| Competitive response | Competitor launched aggressive pricing; deals stalling on price comparison | High | 1-2 weeks |

#### 1.2 Identify the Specific Symptom

| Symptom | Root Cause Hypothesis | Investigation Path |
|---|---|---|
| "We are losing deals on price" | Price-to-value gap or poor anchoring | Win/loss analysis + competitive pricing audit |
| "Customers upgrade but ARPU is flat" | Value metric misalignment or tier ceilings too high | Usage data analysis + tier limit review |
| "Free tier is too generous" | Freemium line drawn in wrong place | Feature usage by tier + conversion funnel |
| "Enterprise deals take forever" | Pricing transparency issue or missing enterprise tier | Sales cycle analysis + buyer interview |
| "Churn is high after first renewal" | Price shock at renewal or value not delivered | Exit survey data + renewal pricing review |
| "We do not know what to charge" | New product without pricing anchor | WTP research + competitive benchmarking |

#### 1.3 Assess Pricing Maturity

| Maturity Level | Characteristics | Approach |
|---|---|---|
| Level 0: No pricing | New product, no revenue | Full pricing exercise (Phases 1-5) |
| Level 1: Cost-plus or gut | Price based on costs or founder intuition | Value-based repricing (Phases 1-4) |
| Level 2: Competitive anchor | Priced relative to competitors | Differentiation-based optimization (Phases 1-3) |
| Level 3: Value-based | Price grounded in customer value delivered | Fine-tuning and expansion optimization (Phases 2-3) |
| Level 4: Dynamic/sophisticated | Price varies by segment, usage, willingness-to-pay | Testing and iteration (Phases 4-5) |

### Deliverables
- Problem classification: type, symptom, maturity level
- Research requirements: what data is needed to proceed
- Timeline estimate based on problem type

### Exit Conditions
- Pricing problem type classified
- Specific symptoms documented
- Research plan for Phase 2 agreed
- This gate must be passed before any pricing recommendation is produced

---

## Phase 2: Research & Data Gathering

### Purpose
Collect the quantitative and qualitative data needed to make defensible pricing recommendations. Every price point must be justified by research, not intuition.

### Entry Conditions
- Phase 1 complete: problem classified, research plan agreed

### Key Activities

#### 2.1 Competitive Pricing Analysis

Use `agent-browser` for live competitive intelligence:

```bash
agent-browser --session pricing-research open "https://{competitor-domain}/pricing"
agent-browser screenshot ./competitor-pricing.png
agent-browser get text body
```

Capture for each competitor:

| Data Point | What to Record |
|---|---|
| Pricing model | Flat-rate, per-seat, usage-based, tiered, hybrid |
| Tier count and names | How many tiers, what they are called |
| Price points | Exact prices for each tier (monthly and annual) |
| Value metric | What unit the pricing scales on (users, events, storage, revenue) |
| Free tier / trial | Free forever, free trial (duration), no free option |
| Feature gating | Which features are in which tier |
| Enterprise pricing | Public or "contact sales" |
| Pricing page design | Anchoring, recommended tier, annual discount |

Benchmark: Analyze 5-8 direct competitors minimum. Include 2-3 adjacent category players for anchoring perspective.

#### 2.2 Willingness-to-Pay (WTP) Research

Load `./references/pricing-research.md` for detailed methodology.

**Van Westendorp Price Sensitivity Meter** (recommended for most cases):
- Four questions asked to 50-200 target customers:
  1. At what price would this be so cheap you would question its quality? (Too cheap)
  2. At what price is this a bargain -- a great buy for the money? (Cheap/good value)
  3. At what price is this getting expensive but you would still consider it? (Expensive but acceptable)
  4. At what price is this too expensive to consider? (Too expensive)
- Plot curves; intersection points define the acceptable price range
- Minimum sample: 50 responses for directional data, 200+ for statistical confidence

**Gabor-Granger Method** (for price point validation):
- Show product description at a specific price
- Ask: "How likely are you to purchase at this price?" (1-5 scale)
- Iterate through 4-6 price points
- Generates demand curve and revenue-maximizing price point

**Conjoint Analysis** (for packaging decisions):
- Present feature bundles at different price points
- Respondents choose preferred option
- Statistical model reveals feature value and price sensitivity
- Most rigorous but requires 300+ responses and specialized tooling

| Method | Best For | Sample Size | Timeline | Cost |
|---|---|---|---|---|
| Van Westendorp | Price range discovery | 50-200 | 1-2 weeks | Low (survey tool) |
| Gabor-Granger | Price point validation | 100-300 | 1-2 weeks | Low-medium |
| Conjoint analysis | Packaging optimization | 300+ | 3-4 weeks | High (specialized tool) |
| Customer interviews | Qualitative value understanding | 8-15 | 1-2 weeks | Low (time only) |
| Win/loss analysis | Competitive positioning | 20-30 deals | 1-2 weeks | Low (internal data) |

#### 2.3 Usage & Value Data

If the product is live, analyze:

| Data Source | What It Reveals | Priority |
|---|---|---|
| Feature usage by tier | Which features drive upgrades and which are ignored | Critical |
| Usage distribution | How usage clusters (helps define tier limits) | Critical |
| Expansion triggers | What actions correlate with upgrades | High |
| Churn by price point | Which plans have highest/lowest churn | High |
| Sales cycle length by plan | Where pricing friction slows deals | Medium |
| Support cost by tier | True cost to serve each segment | Medium |

#### 2.4 Customer Interviews

Conduct 8-15 interviews focused on value perception:

Questions to ask:
- "What problem does this solve for you, and how much was that problem costing you before?"
- "If this product disappeared tomorrow, what would you do instead? How much would that cost?"
- "Which features do you use most? Which have you never opened?"
- "Have you ever considered switching? What would trigger that?"
- "If you were re-purchasing today at the current price, would you? Why or why not?"

### Deliverables
- Competitive pricing audit (5-8 competitors, structured comparison)
- WTP research findings (if conducted) with price range recommendations
- Usage data analysis with tier limit implications
- Customer interview summary with value perception themes
- Research synthesis: key findings that inform pricing options

### Exit Conditions
- Competitive landscape documented with specific price points
- At least one primary research source completed (WTP survey, interviews, or usage analysis)
- Key findings synthesized into actionable insights
- Data gaps acknowledged with impact on recommendation confidence

---

## Phase 3: Model & Options Development

### Purpose
Build 2-3 distinct pricing options with financial projections, trade-offs, and strategic rationale. Never present a single option -- decision-makers need contrast to evaluate.

### Entry Conditions
- Phase 2 complete: research data available
- Competitive landscape documented
- Customer value perception understood (from research or interviews)

### Key Activities

#### 3.1 Select Pricing Model

| Model | Best For | Expansion Built In | Complexity |
|---|---|---|---|
| Flat-rate | Simple products, single use case | No | Lowest |
| Per-seat | Collaboration tools, team products | Yes (add users) | Low |
| Usage-based | Infrastructure, API, consumption products | Yes (natural growth) | Medium |
| Tiered (feature-gated) | Multi-segment products with clear feature progression | Partial (upgrade path) | Medium |
| Hybrid (base + usage) | Products with both platform value and variable consumption | Yes (both vectors) | High |
| Freemium | Products with viral potential or large TAM | Yes (conversion funnel) | Medium |

#### 3.2 Choose the Value Metric

Load `./references/value-metric.md` for detailed selection methodology.

A good value metric passes three tests:
1. **Scales with customer value**: As the customer gets more value, they naturally use more of the metric
2. **Easy to understand**: Customers can predict their bill before purchasing
3. **Difficult to game**: Customers cannot artificially reduce the metric without reducing their usage

| Value Metric | Works For | Watch Out For |
|---|---|---|
| Users / seats | Collaboration tools | Seat-sharing workarounds; penalizes growth |
| Monthly active users (MAU) | Product-led growth tools | Hard to predict; customers dislike variable bills |
| Events / API calls | Analytics, infrastructure | Unpredictable cost for customer |
| Revenue processed | Payment, e-commerce tools | Aligns perfectly with value; scales naturally |
| Storage / data volume | Storage, backup, media tools | Cheap input metric; may not correlate with value |
| Projects / workspaces | Project management, design tools | Easy to understand; natural expansion |

#### 3.3 Design Tier Structure

Load `./references/tier-structure.md` for detailed patterns.

Standard tier architecture:

| Tier | Purpose | Pricing Position | Feature Strategy |
|---|---|---|---|
| Free / Trial | Acquisition, product-led growth | $0 | Core value visible, limits drive upgrade |
| Starter / Basic | Individual users, small teams | Below median WTP | Core features, reasonable limits |
| Professional / Pro | Primary revenue driver, target segment | At median WTP | Full feature set, higher limits |
| Business / Team | Teams and departments | 2-3x Pro price | Collaboration features, admin controls |
| Enterprise | Large organizations with custom needs | "Contact sales" | Custom limits, SLAs, dedicated support |

Best practice: 3 tiers for most products. 4 if there is a clear enterprise segment. 5 is the maximum before decision fatigue hurts conversion.

#### 3.4 Build Financial Projections

For each pricing option, project:

| Projection | Formula | Timeframe |
|---|---|---|
| Expected ARPU | Weighted average across tier distribution | Monthly |
| Revenue impact | (New ARPU - Current ARPU) x Customer base | Monthly and annual |
| Conversion rate impact | Estimated based on price elasticity research | Monthly |
| Expansion revenue | Projected upgrade and usage growth | 12-month |
| Churn rate impact | Estimated based on price-value alignment | Monthly |
| Break-even analysis | Time to recover implementation/migration costs | Months |

#### 3.5 Present 2-3 Options

Structure each option as:

**Option A: [Name]** (e.g., "Conservative Optimization")
- Model: [pricing model]
- Value metric: [metric]
- Tiers: [tier structure with specific prices]
- Financial projection: [revenue impact estimate]
- Risk: [what could go wrong]
- Best if: [conditions under which this option wins]

**Option B: [Name]** (e.g., "Growth-Optimized Restructure")
- Same structure as Option A

**Option C: [Name]** (e.g., "Premium Repositioning")
- Same structure as Option A

### Deliverables
- 2-3 pricing options with complete tier structures and specific prices
- Financial projections for each option (12-month revenue model)
- Comparison matrix: trade-offs across options
- Value metric analysis with recommendation

### Exit Conditions
- 2-3 distinct options developed (not minor variations of the same approach)
- Each option has specific price points (not ranges)
- Financial projections completed for each option
- Trade-offs clearly documented

---

## Phase 4: Recommendation

### Purpose
Present the recommended pricing option with clear justification, anticipated objections, and implementation requirements.

### Entry Conditions
- Phase 3 complete: 2-3 options developed with projections

### Key Activities

#### 4.1 Recommendation Framework

Present the recommendation using this structure:

1. **Recommended option**: Which option and why
2. **Key evidence**: 2-3 data points from research that support this choice
3. **Expected impact**: Revenue projection with confidence level (high/medium/low)
4. **Risks and mitigations**: What could go wrong and how to hedge
5. **What we are NOT recommending**: Why the other options were rejected (with conditions under which to reconsider)
6. **Implementation requirements**: Technical, marketing, and operational changes needed

#### 4.2 Sensitivity Analysis

For the recommended option, model scenarios:

| Scenario | Assumption Change | Revenue Impact |
|---|---|---|
| Optimistic | Conversion rate +20%, churn -10% | +[X]% revenue |
| Base case | Current conversion, current churn | +[Y]% revenue |
| Pessimistic | Conversion rate -15%, churn +5% | +[Z]% revenue |
| Downside | Conversion rate -30%, churn +15% | [Risk of negative impact] |

The recommendation must be defensible even in the pessimistic scenario.

#### 4.3 Stakeholder Objection Map

Anticipate and pre-address common objections:

| Stakeholder | Likely Objection | Pre-emptive Response |
|---|---|---|
| Sales team | "Customers will push back on higher prices" | Win/loss data shows price is #3 objection, not #1; value communication training plan included |
| Product team | "We can't gate features this way" | Technical implementation plan with timeline and effort estimate |
| Finance | "What if conversion drops?" | Sensitivity analysis shows break-even even at -15% conversion; A/B test plan de-risks |
| CEO/founder | "What about our cheapest/most loyal customers?" | Grandfathering plan for existing customers; new pricing applies to new signups only |
| Customer success | "How do we communicate this?" | Communication plan included with email templates, FAQ, and training materials |

#### 4.4 Pricing Page Recommendations

Load `./references/pricing-page.md` for detailed pricing page strategy.

For the recommended option, include:
- Tier naming and positioning
- Recommended (highlighted) tier
- Annual discount structure (typically 15-25% discount for annual billing)
- CTA copy for each tier
- Feature comparison table structure
- FAQ items for the pricing page

### Deliverables
- Pricing recommendation document with full justification
- Sensitivity analysis across 4 scenarios
- Stakeholder objection map with responses
- Pricing page wireframe / content specification
- Communication plan outline for price change (if applicable)

### Exit Conditions
- Single recommended option presented with evidence-based justification
- Sensitivity analysis completed
- Key stakeholder objections anticipated and addressed
- Implementation path outlined

---

## Phase 5: Testing & Rollout

### Purpose
De-risk the pricing change through testing, plan the migration for existing customers, build the communication plan, and establish monitoring for post-launch.

### Entry Conditions
- Phase 4 recommendation approved by decision-maker
- Technical feasibility confirmed

### Key Activities

#### 5.1 A/B Test Plan

If traffic allows (1,000+ pricing page visitors/month):

| Test | What to Test | Primary Metric | Sample Size | Duration |
|---|---|---|---|---|
| Price point | Current vs recommended price | Revenue per visitor | 2,000+ per variant | 2-4 weeks |
| Tier structure | Current vs new tier packaging | Plan distribution + ARPU | 2,000+ per variant | 4-6 weeks |
| Pricing page | Current layout vs new anchoring | Conversion rate | 1,000+ per variant | 2-3 weeks |
| Annual discount | Current % vs new % | Annual plan adoption rate | 1,500+ per variant | 3-4 weeks |

If traffic is insufficient for A/B testing: launch to new signups only and compare cohort performance over 60-90 days.

#### 5.2 Migration Strategy for Existing Customers

| Segment | Migration Approach | Timeline |
|---|---|---|
| Free tier users | Immediate (if free tier changes) or grandfathered | At launch |
| Monthly subscribers | Grandfather for 90 days, then new pricing | 90 days post-launch |
| Annual subscribers | Grandfather until renewal, then new pricing | At renewal |
| Enterprise / custom | Renegotiate individually at renewal | At contract renewal |
| High-LTV loyal customers | Extended grandfather period (180 days) or loyalty discount | 180 days post-launch |

Grandfathering principles:
- Never surprise-charge existing customers a higher price
- Give minimum 30-day notice before any price increase takes effect
- Offer annual lock-in at current price as an option
- Be transparent about why pricing is changing

#### 5.3 Communication Plan

| Timing | Channel | Message | Audience |
|---|---|---|---|
| 30 days before | Email | "We are updating our pricing on [date]" with rationale | All existing customers |
| 30 days before | Blog post | Public announcement with new pricing details | Public |
| 14 days before | Email | Reminder with comparison (old vs new) and grandfathering details | Affected customers |
| 7 days before | In-app | Banner notification with link to FAQ | Active users |
| Launch day | Email | Pricing is now live, what has changed, what to expect | All customers |
| Launch day | Pricing page | Updated with new structure | New visitors |
| 7 days after | Email | FAQ follow-up addressing common questions | Customers who opened previous emails |

Communication tone: honest, respectful, and value-focused. Lead with what customers GET, not what they PAY.

#### 5.4 Post-Launch Monitoring

| Metric | Check Frequency | Alert Threshold |
|---|---|---|
| Signup conversion rate | Daily (first 2 weeks) | >15% drop from baseline |
| Plan distribution (tier mix) | Daily (first 2 weeks) | Recommended tier < 40% of signups |
| Upgrade rate | Weekly | >20% drop from baseline |
| Churn rate | Weekly | >25% increase from baseline |
| Support tickets mentioning pricing | Daily | >3x normal volume |
| ARPU (new customers) | Weekly | Below base-case projection |
| Revenue per pricing page visitor | Weekly | >10% drop from baseline |

Rollback triggers:
- Signup conversion drops >30% for 7+ consecutive days
- Churn rate doubles within 30 days of change
- Net revenue impact is negative at 30-day mark

#### 5.5 Iteration Plan

| Review Point | Decision | Possible Actions |
|---|---|---|
| 30 days post-launch | Initial health check | Adjust messaging, tweak feature gating, expand A/B tests |
| 60 days post-launch | Trend confirmation | Confirm uplift trajectory, adjust projections |
| 90 days post-launch | Full impact assessment | Document results, plan next optimization cycle |
| 6 months post-launch | Strategic review | Evaluate market changes, plan annual pricing refresh |

### Deliverables
- A/B test plan with test specifications and sample size calculations
- Customer migration plan with segment-level grandfathering rules
- Communication plan with email templates, blog post draft, and FAQ
- Post-launch monitoring dashboard specification
- Rollback criteria and contingency plan

### Exit Conditions
- Test plan ready for execution (or direct rollout plan if testing is not feasible)
- Migration plan approved
- Communication assets drafted
- Monitoring dashboard specified

---

## Diagnostic Questions

Ask these before producing any pricing recommendation. Pricing without this context is guessing.

1. **Current pricing**: What is your current pricing model and price points? How long has it been in place?
2. **Problem trigger**: What prompted this pricing work? (Revenue plateau, competitive pressure, new product, restructuring?)
3. **Revenue metrics**: What is your current MRR/ARR? ARPU? Revenue growth rate?
4. **Conversion data**: What is your pricing page conversion rate? Free-to-paid conversion rate (if freemium)? Trial-to-paid rate (if free trial)?
5. **Customer segments**: What is your customer breakdown by plan tier? (How many on each tier?)
6. **Win/loss data**: What percentage of deals are you winning? In lost deals, how often is price cited as the primary reason?
7. **Competitive landscape**: Who are your top 3-5 competitors? What do they charge? How does your product compare feature-by-feature?
8. **Value metric understanding**: What unit of value does your customer care most about? (Users, usage, outcomes, features?)
9. **Customer feedback**: Have you conducted any willingness-to-pay research? Do you have customer feedback on pricing?
10. **Constraints**: Are there technical constraints on billing (what your payment system supports)? Sales team constraints? Contractual obligations to existing customers?

If the user cannot answer questions 1-3, recommend installing pricing analytics (plan distribution, conversion by tier, ARPU tracking) before making changes. Pricing changes without measurement capability are unrecoverable experiments.

---

## Escalation Routes

| Signal Detected | Escalate To | Reason |
|---|---|---|
| Pricing page conversion issues (UX/copy) | paw-mkt-cro | CRO specialist for page optimization |
| Pricing email communication sequences | paw-mkt-email | Email specialist for migration and announcement sequences |
| Competitive intelligence beyond pricing | paw-mkt-paid-ads or paw-mkt-seo | Broader competitive analysis |
| Full go-to-market launch of new pricing | paw-mkt-launch | Launch strategy requires multi-channel coordination |
| Brand positioning questions during pricing work | paw-mkt-product-context | Pricing must align with positioning |
| Retention impact of price increase | paw-mkt-retention | Churn prevention around pricing changes |
| Sales enablement for new pricing | paw-mkt-sales | Sales team needs updated collateral and training |
| Legal review of pricing terms | Flag for legal counsel | Terms, auto-renewal, compliance |
| Financial modeling of pricing change impact | Recommend finance team | Detailed P&L modeling beyond marketing scope |

---

## Ethics: Pricing Transparency

Pricing directly affects customers' ability to make informed purchasing decisions. Ethical pricing builds long-term trust and LTV. Manipulative pricing extracts short-term revenue and destroys brands.

### Ethical Pricing Practices

- **Price transparency**: All costs visible before purchase. No hidden fees revealed at checkout.
- **Honest anchoring**: The "original price" shown for comparison must be a real price that was actually charged, not a fabricated anchor.
- **Clear trial terms**: Before entering payment info, customers know exactly when billing starts, how much it will be, and how to cancel.
- **Fair grandfathering**: Existing customers get reasonable notice and transition time for price increases. No surprise charges.
- **Value-aligned pricing**: Price increases come with corresponding value increases. Raising prices without adding value erodes trust.
- **Accessible tiers**: If the product serves a range of customers, pricing should not exclude the segment that needs it most (consider startup/education/nonprofit discounts).

### Persuasion Techniques: Ethical vs Manipulative

| Technique | Ethical Use | Manipulative Use |
|---|---|---|
| Anchoring | Show highest tier first to make mid-tier feel reasonable | Fabricate inflated "original price" for fake discount |
| Decoy pricing | Add tier that makes the target tier look like best value | Design intentionally bad tier to manipulate choice |
| Annual discount | Genuine savings for commitment (15-25% is standard) | Hiding true monthly cost, making annual the only real option |
| Urgency | Time-limited offer that genuinely expires | Countdown timer that resets; "limited time" that runs forever |
| Social proof | "10,000 teams trust us" when accurate | Fabricated customer counts or fake testimonials |
| Loss framing | "Don't lose your data -- upgrade before trial ends" | "YOUR ACCOUNT WILL BE DELETED" when data is retained |

Before implementing any pricing technique, ask: **If the customer fully understood the pricing mechanics, would they feel the price is fair?** If not, reprice.

---

## Path Resolution

**Campaign mode** -- working within a named campaign:
  -> Save to `./.pawbytes/marketing-suites/brands/{brand-slug}/campaigns/{type}-{campaign-slug}/pricing/`

**Standalone mode** -- evergreen or independent work:
  -> Save to `./.pawbytes/marketing-suites/brands/{brand-slug}/operations/pricing/`

If unsure which mode, ask: "Is this part of a specific campaign, or standalone work?"

---

## Deliverables

All pricing work saves to the resolved path (see Path Resolution above).

| Deliverable | Filename | Key Sections |
|---|---|---|
| Pricing Diagnosis | `pricing-diagnosis-{YYYY-MM-DD}.md` | Problem classification, symptoms, maturity assessment, research plan |
| Competitive Pricing Audit | `competitive-audit-{YYYY-MM-DD}.md` | 5-8 competitor comparison, screenshots, positioning map |
| WTP Research Report | `wtp-research-{YYYY-MM-DD}.md` | Methodology, sample, findings, acceptable price range |
| Pricing Options | `pricing-options-{YYYY-MM-DD}.md` | 2-3 options with tier structures, prices, projections, trade-offs |
| Pricing Recommendation | `pricing-recommendation-{YYYY-MM-DD}.md` | Recommended option, evidence, sensitivity analysis, objection map |
| Rollout Plan | `pricing-rollout-{YYYY-MM-DD}.md` | A/B test plan, migration strategy, communication plan, monitoring |
| Pricing Page Spec | `pricing-page-spec-{YYYY-MM-DD}.md` | Page structure, copy, tier naming, CTA, FAQ, annual discount strategy |

File structure:

```
# Campaign mode:
./.pawbytes/marketing-suites/brands/{brand-slug}/campaigns/{type}-{campaign-slug}/pricing/
  pricing-diagnosis-{YYYY-MM-DD}.md
  competitive-audit-{YYYY-MM-DD}.md
  wtp-research-{YYYY-MM-DD}.md
  pricing-options-{YYYY-MM-DD}.md
  pricing-recommendation-{YYYY-MM-DD}.md
  pricing-rollout-{YYYY-MM-DD}.md
  pricing-page-spec-{YYYY-MM-DD}.md
  screenshots/

# Standalone mode:
./.pawbytes/marketing-suites/brands/{brand-slug}/operations/pricing/
  (same structure as above)
```

---

## Response Protocol

When the user requests pricing work:

1. **Load context**: Read brand context and SOSTAC plan when available. Check for existing pricing deliverables.
2. **Run Phase 1 Diagnosis**: Ask diagnostic questions. Classify the pricing problem. Do NOT jump to tier design or price points.
3. **Conduct research** (Phase 2): Load the appropriate research approach:
   - Competitive analysis -> `./references/pricing-diagnosis.md` + browser research
   - WTP research design -> `./references/pricing-research.md`
   - Value metric analysis -> `./references/value-metric.md`
4. **Build options** (Phase 3): Develop 2-3 pricing options with projections:
   - Tier structure design -> `./references/tier-structure.md`
   - Segment-specific considerations -> `./references/segment-pricing.md`
5. **Present recommendation** (Phase 4): Single recommended option with justification:
   - Pricing page strategy -> `./references/pricing-page.md`
6. **Plan rollout** (Phase 5): Testing, migration, and communication:
   - Price increase execution -> `./references/price-increase.md`
7. **Save deliverables** to the resolved path.
8. **Recommend next steps**: What to implement, what to test, when to review.

### When to compress the workflow

Not every pricing engagement requires all 5 phases at full depth:

| Request | Phases to Compress | Notes |
|---|---|---|
| "Quick pricing page feedback" | Skip to Phase 4 (pricing page) | Still ask diagnostic questions 1-3 |
| "Review our tier structure" | Phases 1-3 (lighter Phase 2) | Competitive check is still required |
| "We need to raise prices" | Phases 1, 4-5 (focus on rollout) | Load `./references/price-increase.md` directly |
| "Full pricing strategy" | All 5 phases at full depth | Standard workflow |
