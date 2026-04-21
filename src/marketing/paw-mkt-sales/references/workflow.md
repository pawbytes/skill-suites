# Sales Enablement Pipeline Workflow

This reference defines the standard workflow, diagnostic questions, phase gates, escalation routes, and ethical guidelines for all sales enablement work.

---

## Workflow Overview

The sales enablement pipeline moves through five phases. Each phase has explicit entry conditions, key activities, deliverables, and exit gates. The workflow ensures every piece of sales collateral is grounded in research, validated for accuracy, and distributed where reps can actually use it.

```
Phase 1: Context & Research
    |
Phase 2: Enablement Audit
    |
Phase 3: Asset Creation  <-- Routes to specific framework templates
    |       |       |       |       |       |       |
    |    Deck  One-Pager  Demo  Objection  ROI  Champion
    |       |       |       |   Handler   Calc    Kit
    |       +---+---+---+---+---+---+------+
    |           |
Phase 4: Validation
    |
Phase 5: Catalog & Distribute
```

---

## Diagnostic Questions

Ask these before producing any sales enablement material. Collateral without this context is generic filler that reps will ignore.

1. **Sales process**: What does the current sales process look like? What are the deal stages (discovery, demo, proposal, negotiation, close)?
2. **Deal cycle**: What is the average sales cycle length? What is the current win rate? Where do deals stall or die?
3. **Buyer personas**: Who are the primary buyers (economic buyer, champion, technical evaluator, end user)? What does each persona care about?
4. **Existing collateral**: What sales materials exist today? What do reps actually use? What do they ignore or work around?
5. **Competitive landscape**: Who are the top 3-5 competitors? What do their reps say about your product? What objections come up most?
6. **Proof points**: What customer success stories, metrics, case studies, and third-party validation exist? What claims can be made with evidence?
7. **Gaps and pain points**: What do reps say they need? Where do they lose deals they should win? What questions can they not answer confidently?

If the user cannot answer questions 1-3, recommend conducting sales team interviews (5-7 reps across experience levels) before building collateral. Enablement without sales input is marketing fiction.

---

## Phase 1: Context & Research

**Purpose**: Load all available brand context, competitive intelligence, and product positioning before building any collateral.

### Entry Conditions
- Brand context or SOSTAC plan is available (or user provides equivalent context)
- Product is live or in active sales (not pre-product)
- At least one active salesperson or founder selling the product

### Key Activities
- Load brand context: positioning document, value propositions, proof points, customer language
- Load SOSTAC plan if available: situation analysis, competitive landscape, target audience
- Research competitive landscape:
  - Map competitor positioning, pricing, and messaging
  - Identify competitive strengths and weaknesses
  - Document common competitive objections from sales calls
  - Review competitor sales materials if publicly available (G2 comparisons, analyst reports, review sites)
- Research customer language:
  - Review G2/Capterra/Trustpilot reviews for customer language patterns
  - Analyze support tickets for common questions and pain points
  - Review sales call recordings or notes for objection patterns
  - Extract specific outcomes and metrics from case studies
- Map the product to buyer needs:
  - Feature-to-benefit translation for each persona
  - Competitive differentiation matrix (where you win, where you lose, where it is a tie)
  - Deal stage content mapping: what information does each persona need at each stage?

### Deliverables
- Research brief summarizing competitive landscape, customer language, and proof point inventory
- Feature-benefit-proof matrix (feature -> benefit for persona -> proof point or metric)
- Deal stage content map showing what collateral is needed at each stage for each persona

### Exit Conditions
- Competitive landscape is documented with at least 3 competitors
- Proof point inventory is complete (every claim mapped to evidence)
- Customer language bank has at least 10-15 verbatim phrases from reviews, calls, or interviews
- Deal stage content map identifies specific gaps

---

## Phase 2: Enablement Audit

**Purpose**: Assess existing sales collateral, identify gaps against the deal stage content map, and prioritize what to build or rebuild.

### Entry Conditions
- Research brief is complete (Phase 1 exit)
- Access to existing sales materials (or confirmation that none exist)
- Deal stage content map is available

### Key Activities
- Inventory all existing sales collateral:
  - Decks (sales deck, pitch deck, partnership deck)
  - One-pagers (product overview, feature sheets, comparison sheets)
  - Demo scripts and talk tracks
  - Objection handling documents
  - ROI calculators or business case templates
  - Champion kits (internal selling materials)
  - Battle cards (competitive comparison cards)
  - Case studies and customer stories
  - Email templates and sequences
- Assess quality of existing materials:
  - Currency: are competitive claims current? Are metrics up to date?
  - Accuracy: does every claim have a verifiable source?
  - Voice: does the copy use customer language or marketing speak?
  - Usability: can a rep find and use this in 30 seconds during a call?
  - Coverage: does the asset serve its intended deal stage and persona?
- Gap analysis against the deal stage content map:
  - Which deal stages have no collateral?
  - Which personas are underserved?
  - Which competitive situations lack battle cards?
  - Which objections have no documented response?
- Prioritize by impact:
  - High priority: assets for the deal stage where most deals stall
  - Medium priority: competitive battle cards for top 3 competitors
  - Lower priority: nice-to-have assets for edge-case personas or rare objections

### Scoring Framework for Asset Priority

| Factor | Weight | Scoring |
|--------|--------|---------|
| Deal stage impact | 40% | Which deal stage loses the most revenue? Assets for that stage score highest. |
| Rep request frequency | 25% | What do reps ask for most often? High demand = high score. |
| Competitive pressure | 20% | Does a competitor have this asset and you do not? Score based on competitive gap. |
| Effort to create | 15% | Quick wins (update existing) score higher than net-new builds. Inverse weight. |

### Deliverables
- Enablement audit report with inventory, quality assessment, and gap analysis
- Prioritized asset creation backlog with impact scoring
- Recommended build order with estimated effort per asset

### Exit Conditions
- Complete inventory of existing materials with quality ratings
- Gap analysis identifies at least 3 high-priority assets to create or rebuild
- Prioritized backlog is agreed upon with stakeholders
- Build order and timeline are established

---

## Phase 3: Asset Creation

**Purpose**: Build specific sales collateral using the appropriate framework templates, grounded in the research from Phase 1.

### Entry Conditions
- Prioritized backlog is defined (Phase 2 exit)
- Research brief and proof point inventory are available
- Target persona and deal stage for the asset are clear

### Key Activities — Asset-Specific Routing

Route to the specific framework template based on asset type:

| Asset Type | Framework Reference | Key Focus |
|-----------|-------------------|-----------|
| Sales Deck | `./references/sales-deck.md` | Narrative arc: problem -> cost of inaction -> solution -> proof -> call to action |
| One-Pager | `./references/one-pagers.md` | Single page, scannable, one job per sheet |
| Objection Handler | `./references/objection-handling.md` | Verbatim response scripts with proof points per objection |
| Demo Script | `./references/demo-scripts.md` | Discovery questions -> tailored demo flow -> specific talk track |
| ROI Calculator | `./references/roi-calculator.md` | Input assumptions, calculation logic, output business case |
| Champion Kit | `./references/champion-kits.md` | Internal selling materials the champion can forward to their boss |
| Battle Card | `./references/competitive-research.md` | Side-by-side comparison, landmines, trap-setting questions |

### Universal Asset Creation Rules
- Every claim must have a source: customer quote, case study metric, third-party validation, or internal data
- Use customer language, not marketing speak. Pull verbatim phrases from the customer language bank.
- Design for scannability: reps have 30 seconds mid-call. Headers, bullets, bold keywords.
- One asset, one job: a battle card is not a product overview. A demo script is not a sales deck.
- Include "when to use" instructions: what deal stage, what persona, what situation triggers this asset
- Version and date every asset. Stale collateral is worse than no collateral.

### Deliverables
- Completed asset(s) matching the framework template
- Source documentation mapping every claim to its evidence
- Usage guide: when to use, who it is for, how to customize

### Exit Conditions
- Asset is complete and follows the framework template
- Every claim has a documented source
- Usage guide is attached
- Asset is reviewed by at least one sales rep for usability feedback

---

## Phase 4: Validation

**Purpose**: Verify every claim has proof, every metric is sourced, competitive claims are current, and the asset meets quality standards.

### Entry Conditions
- Asset draft is complete (Phase 3 exit)
- Source documentation is available
- At least one sales rep is available for review

### Key Activities
- Claim verification audit:
  - List every factual claim in the asset
  - Verify each claim against its documented source
  - Flag claims without sources for removal or research
  - Check that customer quotes are attributed and have permission for use
  - Verify all metrics are current (within 6 months for market data, 12 months for customer metrics)
- Competitive accuracy check:
  - Verify competitor pricing, features, and positioning are current
  - Check that competitive claims are defensible (documented source, not hearsay)
  - Confirm that "trap-setting questions" in battle cards reference real competitive weaknesses, not FUD
  - Update any stale competitive intelligence
- Usability review:
  - Sales rep review: can they use this mid-call? Is it scannable? Does it match how they sell?
  - Persona fit: does the language match the buyer persona? Technical for evaluators, business for executives?
  - Deal stage fit: does the asset serve the intended stage? Too much detail for early stage? Too little for late stage?
- Legal and compliance review (if applicable):
  - Verify competitive comparison claims meet legal standards (no defamation, supported by evidence)
  - Confirm customer testimonials have release authorization
  - Check ROI claims include appropriate disclaimers

### Validation Checklist

| Check | Pass Criteria |
|-------|---------------|
| Every metric has a source | 100% — no unsourced numbers |
| Customer quotes have permission | Written approval on file |
| Competitive claims are current | Verified within 30 days |
| No marketing speak | Customer language throughout |
| Scannable in 30 seconds | Rep can extract key points mid-call |
| Deal stage appropriate | Content depth matches the stage |
| Persona targeted | Language and benefits match the buyer |
| Dated and versioned | Asset header includes version and date |

### Deliverables
- Validated asset with all claims verified
- Validation report documenting source checks and any changes made
- Legal clearance (if applicable)

### Exit Conditions
- 100% of factual claims are sourced and verified
- Competitive information is confirmed current
- At least one sales rep has reviewed and approved usability
- Asset is versioned and dated

---

## Phase 5: Catalog & Distribute

**Purpose**: Add the validated asset to the content library, distribute to the sales team, and provide training on when and how to use it.

### Entry Conditions
- Asset has passed validation (Phase 4 exit)
- Content library path is defined
- Sales team distribution channel is identified

### Key Activities
- Catalog the asset:
  - Add to content library with metadata: type, persona, deal stage, competitor (if battle card), date, version
  - Tag for searchability: keywords, use case, situation trigger
  - Link to source documentation for future updates
  - Set review cadence: quarterly for competitive materials, semi-annually for product materials
- Distribute to sales team:
  - Push to the team's collateral system (Google Drive, Notion, Highspot, Seismic, or equivalent)
  - Send announcement with: what it is, when to use it, where to find it, how to customize it
  - Include a 2-minute walkthrough video or written guide if the asset is complex
- Provide training recommendations:
  - Role-play session using the new asset (15-minute team exercise)
  - Include in onboarding for new reps
  - Add to the deal stage playbook
- Set up feedback and iteration loop:
  - Track usage: how often is the asset accessed? By whom?
  - Collect rep feedback after 30 days: what works, what does not, what is missing?
  - Schedule first review: 30 days for new assets, quarterly for established ones
  - Define update triggers: new competitor, product change, pricing change, new case study

### Content Library Organization

```
./.pawbytes/marketing-suites/brands/{brand-slug}/operations/sales/
  library/
    decks/
      sales-deck-v{X}-{YYYY-MM-DD}.md
    one-pagers/
      overview-{persona}-v{X}-{YYYY-MM-DD}.md
    battle-cards/
      vs-{competitor}-v{X}-{YYYY-MM-DD}.md
    objection-handlers/
      objections-{topic}-v{X}-{YYYY-MM-DD}.md
    demo-scripts/
      demo-{persona}-v{X}-{YYYY-MM-DD}.md
    roi-calculators/
      roi-model-v{X}-{YYYY-MM-DD}.md
    champion-kits/
      champion-kit-{persona}-v{X}-{YYYY-MM-DD}.md
  audit/
    enablement-audit-{YYYY-MM-DD}.md
  research/
    competitive-landscape-{YYYY-MM-DD}.md
    customer-language-bank-{YYYY-MM-DD}.md
```

### Deliverables
- Cataloged asset in the content library with full metadata
- Distribution announcement to sales team
- Training recommendation or walkthrough guide
- Feedback collection plan with review cadence

### Exit Conditions
- Asset is in the content library with correct metadata and tags
- Sales team has been notified and knows where to find it
- Review cadence is scheduled
- Feedback mechanism is in place

---

## Escalation Routes

| Situation | Route To | Why |
|-----------|----------|-----|
| Pricing objection handling requires pricing strategy input | paw-mkt-pricing | Pricing model, tier structure, and discount authority decisions |
| Product positioning needs refinement based on sales feedback | paw-mkt-product-context | Positioning document, differentiation, and persona updates |
| Long-form content creation (case studies, whitepapers) | paw-mkt-content | Editorial quality, SEO optimization, and content strategy |
| Sales performance analytics and win/loss tracking | paw-mkt-analytics | Dashboard setup, attribution, and measurement infrastructure |
| Email sequences for sales nurture | paw-mkt-email | Drip campaigns, automation workflows, and deliverability |
| Competitive intelligence requires live research | paw-mkt-agent-agency | Multi-channel coordination and research orchestration |
| Landing page optimization for sales-driven traffic | paw-mkt-cro | Conversion rate optimization for demo request or trial pages |
| Video demos or walkthrough production | paw-mkt-video | Video scripting, production, and optimization |

---

## Ethics: Honest Sales Enablement

Sales collateral directly influences purchase decisions. Accuracy and honesty are not optional — they are the foundation of sustainable sales.

### Ethical Enablement Practices

- **Every claim needs proof**: No unsourced metrics, no fabricated customer quotes, no invented case studies. If the proof does not exist, do not make the claim.
- **Competitive honesty**: Compare on facts, not FUD. If a competitor genuinely has a stronger feature, acknowledge it and pivot to your differentiation — do not deny it.
- **Customer language, not spin**: Use the words customers actually say, not marketing-polished versions that lose authenticity.
- **ROI transparency**: ROI calculators must show assumptions clearly. The customer should be able to challenge any input and understand how the output changes.
- **Testimonial integrity**: Only use testimonials from real customers who gave permission. Do not edit quotes to change meaning.
- **Pricing honesty**: Sales materials must reflect actual pricing. No "bait" pricing in early-stage materials that changes at proposal.

### Patterns to Avoid

| Pattern | Description | Why It Harms |
|---------|-------------|--------------|
| Fabricated metrics | "Customers see 10x ROI" without any data | Erodes trust when questioned; legal exposure |
| Competitive FUD | Spreading fear about competitors without factual basis | Damages reputation when discovered; loses credibility |
| Cherry-picked quotes | Editing testimonials to change meaning or context | Customer backlash; quote attribution challenges |
| Phantom case studies | Referencing unnamed or fictional customer stories | Sales reps lose confidence in materials; prospects verify |
| Outdated comparisons | Battle cards with competitor data from 12+ months ago | Reps get embarrassed in calls when prospect corrects them |
| One-size-fits-all | Same deck for CEO and technical evaluator | Neither persona feels addressed; deal stalls |

### The Rep Confidence Test

Before distributing any sales asset, ask: **Would a sales rep feel confident presenting this to a skeptical, well-informed prospect who has also talked to our top competitor?** If the answer is no, strengthen the evidence or remove the claim.

---

## Path Resolution

**Campaign mode** -- working within a named campaign:
  -> Save to `./.pawbytes/marketing-suites/brands/{brand-slug}/campaigns/{type}-{campaign-slug}/sales/`

**Standalone mode** -- evergreen or independent work:
  -> Save to `./.pawbytes/marketing-suites/brands/{brand-slug}/operations/sales/`

If unsure which mode, ask: "Is this part of a specific campaign, or standalone work?"

---

## Deliverables

All sales enablement work saves to the resolved path (see Path Resolution above).

| Deliverable | Filename | Key Sections |
|-------------|----------|--------------|
| Research Brief | `research-brief-{YYYY-MM-DD}.md` | Competitive landscape, customer language bank, proof point inventory |
| Enablement Audit | `enablement-audit-{YYYY-MM-DD}.md` | Inventory, quality assessment, gap analysis, prioritized backlog |
| Sales Deck | `sales-deck-v{X}-{YYYY-MM-DD}.md` | Narrative arc, slide-by-slide content, speaker notes |
| One-Pager | `one-pager-{topic}-v{X}-{YYYY-MM-DD}.md` | Single-page layout with headline, benefits, proof, CTA |
| Battle Card | `battle-card-vs-{competitor}-v{X}-{YYYY-MM-DD}.md` | Comparison matrix, landmines, trap questions, win themes |
| Objection Handler | `objection-handler-{topic}-v{X}-{YYYY-MM-DD}.md` | Objection, response script, proof point, follow-up |
| Demo Script | `demo-script-{persona}-v{X}-{YYYY-MM-DD}.md` | Discovery questions, demo flow, talk track, close |
| ROI Calculator | `roi-calculator-v{X}-{YYYY-MM-DD}.md` | Input assumptions, calculation logic, output template |
| Champion Kit | `champion-kit-v{X}-{YYYY-MM-DD}.md` | Executive summary, business case, FAQ, internal email draft |
| Content Library Index | `library-index-{YYYY-MM-DD}.md` | Catalog of all assets with metadata, tags, and review dates |

---

## Response Protocol

When the user requests sales enablement work:

1. **Route starting context** (blank-page, codebase, or live URL) -- see `./references/shared-patterns.md`
2. **Read strategic context** -- brand positioning and SOSTAC first; then competitive intelligence and product context
3. **Ask diagnostic questions** if the user has not provided this information. Do not build collateral without knowing the sales process and buyer personas.
4. **Determine asset type** -- deck, one-pager, battle card, objection handler, demo script, ROI calculator, champion kit, or full audit
5. **Assess current state** -- check resolved path for prior work; in codebase mode, inspect existing collateral and product implementation
6. **Load the appropriate framework template** from `./references/` for the specific asset type
7. **Deliver the asset** following the framework template, grounded in Phase 1 research
8. **Validate** -- ensure every claim has proof, every metric is sourced, competitive claims are current
9. **Save deliverables** to the resolved path
10. **Recommend distribution** -- where to catalog, who to notify, when to review
