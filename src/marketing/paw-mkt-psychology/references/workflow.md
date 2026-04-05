# Marketing Psychology Workflow

This reference defines the standard workflow, phase structure, diagnostic questions, ethical verification protocol, and deliverable format for all behavioral strategy and marketing psychology work.

---

## Workflow Overview

The Marketing Psychology Workflow is a 5-phase process that moves from context understanding through behavioral diagnosis, framework application, and ethical delivery. Psychology is a cross-cutting advisory skill — every output must fit the requesting context (CRO, email, pricing, retention, etc.) and pass ethical verification before delivery.

The core principle: **Diagnose first, prescribe second.** No psychological framework gets applied without first understanding the specific behavioral barrier blocking the desired action. Generic "add social proof" advice is lazy. Targeted "your audience exhibits status quo bias because switching costs feel uncertain — reduce perceived risk with a reversibility guarantee" is useful.

### Phase Summary

| Phase | Name | Purpose | Typical Duration |
|-------|------|---------|-----------------|
| 1 | Context Assessment | Identify requesting context, load brand/audience data, understand the decision environment | 15-30 min |
| 2 | Behavioral Diagnosis | Identify the specific cognitive or motivational barrier blocking the desired action | 30-60 min |
| 3 | Framework Selection & Application | Match barriers to highest-leverage psychological frameworks, generate specific recommendations | 1-3 hours |
| 4 | Delivery & Ethical Verification | Produce actionable output with before/after rewrites, verify ethical compliance | 30-60 min |
| 5 | Implementation Handoff | Route recommendations to originating skill for execution, define measurement | 15-30 min |

---

## Diagnostic Questions

Ask these before applying any behavioral framework. Recommendations without this data are projections, not diagnoses.

1. **Requesting context**: Which channel or skill needs psychology input? (CRO, email, pricing, retention, social, paid ads, content, sales) The recommendation must be implementable in that context.
2. **Current behavior**: What is the user currently doing instead of the desired action? Are they bouncing, abandoning, ignoring, or choosing a competitor?
3. **Decision environment**: Where does this decision happen? (Landing page, email, checkout, onboarding, pricing page, cancel flow) What information is available to the user at that moment?
4. **Audience beliefs**: What does the target audience believe about the product category, the brand, and the problem being solved? What prior experiences shape their expectations?
5. **Emotional state**: What emotional state is the audience likely in when they encounter this touchpoint? (Curious, skeptical, anxious, impatient, hopeful, frustrated)
6. **Desired action**: What specific action should the user take? Be precise — "convert" is too vague. "Click the Start Trial button after reading the pricing page" is actionable.
7. **Constraints**: What cannot change? (Pricing, product features, brand voice, regulatory requirements)

If the user cannot describe the current behavior and desired action (questions 2 and 6), the problem is not yet defined well enough for behavioral intervention. Help them clarify before proceeding.

---

## Phase 1: Context Assessment

**Purpose**: Understand the requesting context, load available brand and audience data, and map the decision environment before diagnosing any behavioral barrier.

### Entry Conditions
- A specific marketing challenge or conversion problem has been articulated
- The requesting channel or skill is identified

### Key Activities
1. **Identify the requesting skill**: Determine which channel owns the implementation. Psychology advises — other skills execute. Match the output format to what the requesting skill can actually use.
2. **Load strategic context**: Read brand positioning and SOSTAC plan when available. Understand the brand's values, audience segments, and market position.
3. **Map the decision journey**: Where in the customer journey does this touchpoint sit? What happened before this moment? What should happen after?
4. **Assess available data**: Review any existing analytics, heatmaps, session recordings, user feedback, or A/B test results that reveal actual behavior.

### Deliverables
- Context brief: requesting skill, decision environment, audience segment, available data
- Decision journey map for the specific touchpoint

### Exit Conditions
- Requesting context and channel clearly identified
- Audience beliefs and emotional state understood (or reasonable hypotheses formed)
- Decision environment mapped with before/after touchpoints

---

## Phase 2: Behavioral Diagnosis

**Purpose**: Identify the specific cognitive or motivational barrier preventing the desired action. This is the most critical phase — accurate diagnosis drives effective intervention.

### Entry Conditions
- Context assessment complete (Phase 1)
- Current behavior and desired action clearly defined

### Key Activities
1. **Identify the barrier category**:
   - **Cognitive barriers**: Confusion, information overload, choice paralysis, unclear value proposition
   - **Motivational barriers**: Low perceived value, insufficient urgency, weak emotional connection
   - **Trust barriers**: Skepticism, fear of commitment, privacy concerns, brand unfamiliarity
   - **Friction barriers**: Too many steps, unclear next action, cognitive load, effort exceeds perceived reward
   - **Inertia barriers**: Status quo bias, switching costs, loss aversion for current solution

2. **Diagnose root cause vs. symptom**:
   - Low click-through is a symptom. The root cause might be unclear value proposition (cognitive), weak social proof (trust), or buried CTA (friction).
   - High bounce rate is a symptom. The root cause might be message mismatch from traffic source (cognitive), slow load time (friction), or intimidating commitment level (trust).

3. **Prioritize barriers**: If multiple barriers exist, rank by impact. The highest-leverage intervention addresses the primary barrier. Fix the biggest leak first.

4. **Form behavioral hypotheses**: State each hypothesis in the format: "Users are not [desired action] because [specific barrier]. Evidence: [data point or observation]. Predicted intervention: [framework or technique]."

### Deliverables
- Behavioral diagnosis report: identified barriers ranked by impact
- Behavioral hypotheses (3 maximum) with supporting evidence

### Exit Conditions
- Primary barrier identified with supporting evidence or reasoning
- At least 1 behavioral hypothesis formed with predicted intervention
- Root cause distinguished from symptom

---

## Phase 3: Framework Selection & Application

**Purpose**: Match diagnosed barriers to the highest-leverage psychological frameworks and generate specific, implementable recommendations.

### Entry Conditions
- Behavioral diagnosis complete (Phase 2)
- Primary barrier and hypotheses defined

### Key Activities
1. **Select frameworks**: Use `./frameworks-index.csv` to match the barrier to relevant frameworks. Prioritize the top 3 — not an exhaustive list. Common matches:
   - Status quo bias → loss framing, default effect, endowment effect
   - Choice paralysis → recommendation architecture, decoy effect, satisficing design
   - Trust deficit → social proof, authority signals, risk reversal (guarantees, trials)
   - Friction → BJ Fogg behavior model (increase ability, add triggers at high-motivation moments)
   - Low urgency → scarcity (genuine only), commitment/consistency, implementation intentions

2. **Generate specific recommendations**: Each recommendation must include:
   - The principle being applied and why it addresses this specific barrier
   - The exact touchpoint where it applies
   - Before/after examples (copy rewrites, UX changes, flow modifications) when applicable
   - Expected behavioral impact

3. **Prioritize by leverage**: Rank recommendations by expected impact. The first recommendation should address the primary barrier. Secondary recommendations address supporting barriers.

4. **Consider interaction effects**: Multiple psychological techniques can conflict. Social proof + scarcity can feel manipulative. Authority + urgency can feel pushy. Design interventions that work together coherently.

### Deliverables
- Framework application brief: selected frameworks, rationale, specific recommendations
- Before/after examples for each recommendation
- Priority ranking with expected impact

### Exit Conditions
- 1-3 specific recommendations produced (not a list of 10)
- Each recommendation tied to a diagnosed barrier
- Before/after examples included where applicable

---

## Phase 4: Delivery & Ethical Verification

**Purpose**: Finalize recommendations, verify ethical compliance using the ethical gate, and produce the deliverable in a format the requesting skill can execute.

### Entry Conditions
- Framework application complete (Phase 3)
- Recommendations and examples produced

### Key Activities
1. **Ethical verification**: Every recommendation must pass the four-question ethical gate defined in the SKILL.md:
   - Would the customer feel well-served if they understood exactly what technique was being used?
   - Does the recommendation help the customer make a decision aligned with their genuine interests?
   - Is all information presented truthfully, without manufactured urgency or fabricated scarcity?
   - Would a regulatory body reviewing this tactic consider it compliant?

2. **Flag and revise**: If any recommendation fails ethical verification, revise it. Document the original technique, why it failed, and the ethical alternative. Common revisions:
   - Fabricated scarcity → genuine scarcity or honest urgency (deadline-based, not stock-based)
   - Confirmshaming → neutral opt-out language
   - Hidden commitment → transparent terms with easy reversal
   - Manipulative loss framing → honest loss framing (real consequences, not manufactured fear)

3. **Format for requesting context**: Adapt the deliverable to the requesting skill's needs:
   - CRO: page-level copy rewrites, UX recommendations, A/B test hypotheses
   - Email: subject line rewrites, body copy frameworks, sequence structure
   - Pricing: tier display recommendations, anchoring strategy, price communication
   - Retention: save offer framing, cancel flow psychology, win-back messaging
   - Content: headline frameworks, CTA psychology, engagement hooks
   - Social: post psychology, engagement triggers, community motivation

4. **Write deliverable**: Save to the resolved path per Path Resolution.

### Deliverables
- Psychology recommendation document with ethical verification status
- Before/after examples per recommendation
- Ethical gate results (passed/flagged/revised per recommendation)

### Exit Conditions
- All recommendations pass ethical verification (or are revised until they do)
- Deliverable formatted for the requesting skill's implementation context
- File saved to resolved path

---

## Phase 5: Implementation Handoff

**Purpose**: Route recommendations back to the originating skill for execution and define how to measure behavioral impact.

### Entry Conditions
- Deliverable produced and ethically verified (Phase 4)
- Requesting skill identified

### Key Activities
1. **Route to originating skill**: Psychology recommends — other skills implement. Clearly state which skill should execute each recommendation:
   - Copy rewrites on landing pages → `paw-mkt-cro`
   - Email subject line and body changes → `paw-mkt-email`
   - Pricing display changes → `paw-mkt-pricing`
   - Cancel flow and retention messaging → `paw-mkt-retention`
   - Content headline and CTA changes → `paw-mkt-content`
   - Social post psychology → `paw-mkt-social`
   - Ad creative psychology → `paw-mkt-paid-ads`

2. **Define measurement**: For each recommendation, specify:
   - What metric should change (conversion rate, click-through rate, save rate, etc.)
   - Expected direction and rough magnitude
   - Minimum observation period before evaluating (typically 2-4 weeks or 1,000+ exposures)
   - How to isolate the behavioral intervention's impact from other changes

3. **Suggest next phase**: If the intervention reveals deeper behavioral patterns, recommend follow-up analysis. If the primary barrier is resolved, suggest moving to secondary barriers.

### Deliverables
- Implementation handoff brief: who implements what, measurement plan
- Suggested follow-up analysis (if applicable)

### Exit Conditions
- Each recommendation has a clear owner (requesting skill)
- Measurement criteria defined per recommendation
- Handoff communicated (or documented for async workflow)

---

## Deliverable Format

All psychology work saves to the resolved path (see Path Resolution in SKILL.md).

| Deliverable | Filename | Key Sections |
|---|---|---|
| Behavioral Audit | `behavioral-audit-{context}-{YYYY-MM-DD}.md` | Context, diagnosed barriers, framework recommendations, before/after examples, ethical verification |
| Copy Rewrite Brief | `copy-rewrite-{context}-{YYYY-MM-DD}.md` | Original copy, barrier diagnosis, rewritten versions with principle annotations |
| Pricing Psychology Brief | `pricing-psychology-{YYYY-MM-DD}.md` | Tier analysis, anchoring strategy, decoy recommendations, price communication |
| Behavioral Intervention Roadmap | `behavioral-roadmap-{YYYY-MM-DD}.md` | Prioritized interventions, implementation owner per item, measurement plan |

---

## Framework Quick Reference

Use `./frameworks-index.csv` for full framework lookup. Below is a barrier-to-framework quick map for common situations:

| Barrier Type | Primary Frameworks | Common Touchpoints |
|---|---|---|
| Status quo bias | Loss framing, endowment effect, default architecture | Cancel flows, upgrade prompts, switching pages |
| Choice paralysis | Recommendation architecture, decoy effect, satisficing | Pricing pages, plan selection, feature comparison |
| Trust deficit | Social proof, authority signals, risk reversal | Landing pages, checkout, signup forms |
| Low perceived value | Anchoring, contrast principle, concrete outcomes | Pricing, headlines, value propositions |
| Friction and effort | BJ Fogg (ability + triggers), progressive disclosure | Signup flows, onboarding, form design |
| Urgency deficit | Genuine scarcity, commitment devices, implementation intentions | CTAs, limited offers, event registration |
| Emotional disconnect | Storytelling, identity alignment, loss/gain framing | Brand messaging, email sequences, social content |
