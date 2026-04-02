# Research Synthesis

Convert raw research findings into decision-ready market intelligence. Create a cohesive narrative that informs product decisions.

## Purpose

Transform competitor analysis, demand signals, and gap identification into a unified market intelligence brief that answers the core question: **Should we build this, and if so, how?**

## Input Requirements

Gather existing research outputs:
- Competitor analysis (if completed)
- Demand signal analysis (if completed)
- Gap identification (if completed)
- Product context (from sidecar memory)
- User's key questions and decision points

## Synthesis Framework

### The Decision Framework

Every synthesis should inform these decisions:

| Decision | What Research Tells Us |
|----------|------------------------|
| Build or not? | Demand strength, gap opportunity, competitive intensity |
| For whom? | Audience gaps, underserved segments |
| How to position? | Positioning gaps, competitor weaknesses |
| What to build first? | Feature gaps, pain point severity |
| What to charge? | Competitor pricing, value gaps |
| What to avoid? | Saturated areas, competitor strengths |

### Evidence Hierarchy

When synthesizing, weight evidence by confidence:

```
HIGH confidence findings → Core strategy
MED confidence findings → Supporting points, validation targets
LOW confidence findings → Hypotheses to test
ASSUMED → Explicitly call out, do not build strategy on
```

## Synthesis Process

### Step 1: Gather and Review

Read all existing research:
1. `curated/market-intelligence.md` — existing synthesis
2. `products/{slug}/research/competitor-matrix.md`
3. `products/{slug}/research/demand-signals.md`
4. `products/{slug}/research/opportunity-gaps.md`

### Step 2: Extract Key Findings

For each research area, extract:

**Competitor Analysis:**
- Top 3 competitors and their positioning
- Key differentiators in market
- Competitive intensity assessment

**Demand Signals:**
- Overall demand score
- Strongest signals
- Weakest signals
- Demand trajectory

**Gap Analysis:**
- Top 3 opportunity gaps
- Highest priority opportunities
- Gaps to avoid (saturated or low value)

### Step 3: Identify Convergence and Conflict

**Convergence:** Where multiple research streams agree
- Example: Competitor weakness + gap analysis + demand signals all point to same opportunity

**Conflict:** Where research streams disagree
- Example: Strong demand but highly saturated market
- Example: Gap exists but demand signals are weak

### Step 4: Render Verdicts

For each key decision, render a verdict:

```markdown
## Decision: {Decision Topic}

**Verdict:** {Go/No-Go/Conditional}

**Evidence for:**
- {Supporting evidence 1}
- {Supporting evidence 2}

**Evidence against:**
- {Contradicting evidence 1}

**Confidence:** {HIGH/MED/LOW}

**Condition (if conditional):** {What needs to be true}
```

### Step 5: Define Strategy Implications

Based on verdicts, define:

1. **Recommended positioning** — How to differentiate
2. **Target segment** — Who to serve first
3. **MVP scope** — What to build first
4. **Pricing strategy** — Price range and model
5. **Risks to monitor** — What could go wrong
6. **Validation needed** — What to test before committing

## Output Format

### Market Intelligence Brief

```markdown
# Market Intelligence Brief: {Product Concept}

**Last Updated:** {date}
**Research Depth:** {quick scan / standard / deep dive}

---

## Executive Summary

[3-4 sentences answering: Should we build this? For whom? How to win?]

**Bottom Line:** {Go/No-Go/Conditional with one-line reason}

---

## The Market

### Market Overview
- **Category:** {product category}
- **Market size:** {size} `[CONFIDENCE]`
- **Growth trajectory:** {assessment}
- **Key players:** {top 3-5 competitors}

### Demand Assessment
- **Demand strength:** {Strong/Moderate/Weak}
- **Demand score:** {X}/5
- **Key signals:** {top 2-3 signals}
- **Trajectory:** {growing/stable/declining}

### Competitive Landscape
- **Competitive intensity:** {Low/Medium/High}
- **Market maturity:** {Emerging/Growing/Mature}
- **Differentiation opportunity:** {assessment}

---

## The Opportunity

### Market Gaps Identified

| Gap | Type | Opportunity | Confidence |
|-----|------|-------------|------------|
| {Gap 1} | {type} | {High/Med/Low} | {confidence} |
| {Gap 2} | {type} | {High/Med/Low} | {confidence} |

### Underserved Segments

| Segment | Currently Served By | Opportunity |
|---------|--------------------|-------------| 
| {Segment 1} | {competitors or "None"} | {assessment} |

### Positioning Opportunities

**Available positions:**
1. {Position 1} — {why available}
2. {Position 2} — {why available}

**Saturated positions:**
- {Position to avoid} — {why saturated}

---

## Strategic Recommendations

### Recommended Positioning
{How to position the product for differentiation}

**Rationale:** {Why this positioning wins}

### Target Segment (Primary)
**Who:** {segment description}
**Why:** {why this segment}
**How to reach:** {channels}

### MVP Scope Recommendations

**Must-have features:**
1. {Feature 1} — addresses {gap/pain point}
2. {Feature 2} — addresses {gap/pain point}

**Differentiators to lead with:**
- {Differentiator 1}

**Features to defer:**
- {Feature} — {why defer}

### Pricing Guidance

- **Market range:** {low} - {high}
- **Recommended position:** {budget/mid/premium}
- **Suggested range:** {range}
- **Pricing model:** {subscription/one-time/freemium}

---

## Decision Verdicts

### Should we build this?

**Verdict:** {Go / No-Go / Conditional}

**Evidence for:**
- {Evidence 1}
- {Evidence 2}

**Evidence against:**
- {Evidence 1}

**Confidence:** {HIGH/MED/LOW}

{If Conditional:}
**Conditions for Go:**
- {Condition 1}
- {Condition 2}

---

## Risks and Mitigations

| Risk | Likelihood | Impact | Mitigation |
|------|------------|--------|------------|
| {Risk 1} | {H/M/L} | {H/M/L} | {strategy} |

---

## Validation Priorities

Before committing, validate:
1. **{Unknown 1}** — {how to validate}
2. **{Unknown 2}** — {how to validate}

---

## Confidence Assessment

| Area | Confidence | Key Uncertainty |
|------|------------|-----------------|
| Demand | {H/M/L} | {uncertainty} |
| Competition | {H/M/L} | {uncertainty} |
| Opportunity | {H/M/L} | {uncertainty} |
| Strategy | {H/M/L} | {uncertainty} |

**Overall research confidence:** {HIGH/MED/LOW}

---

## Sources Summary

### High-Confidence Sources
- [Source 1](url) — {what it informed}
- [Source 2](url) — {what it informed}

### Lower-Confidence Sources
- [Source 3](url) — {what it informed, why lower confidence}

---

## Appendix: Raw Research

Detailed research available at:
- Competitor Matrix: `products/{slug}/research/competitor-matrix.md`
- Demand Signals: `products/{slug}/research/demand-signals.md`
- Opportunity Gaps: `products/{slug}/research/opportunity-gaps.md`

---

## Next Steps

1. **Immediate:** {what to do now}
2. **Short-term:** {what to do next}
3. **Before build:** {what to validate}

*Research conducted: {date}*
*Next review recommended: {date + 3 months}*
```

## Quality Standards

Every synthesis must:

- **Answer the core question:** Should we build this?
- **Separate evidence from inference:** Clear labeling throughout
- **Acknowledge uncertainty:** Confidence levels on all key findings
- **Provide actionable direction:** Specific recommendations
- **Enable decision-making:** Clear verdicts, not just observations

## Completion Criteria

Synthesis is complete when:
- [ ] All research streams integrated
- [ ] Core question answered with verdict
- [ ] Strategic recommendations provided
- [ ] Risks identified with mitigations
- [ ] Validation priorities defined
- [ ] Confidence levels assigned throughout
- [ ] Sources documented

## Update Protocol

When new research is gathered:

1. **Update the relevant section** in the brief
2. **Re-assess verdicts** if new evidence changes conclusions
3. **Update confidence levels** as appropriate
4. **Log the update** in the daily file
5. **Note:** "Updated {section} based on {new research}"

## Handoff

When synthesis is complete:
1. Save to `curated/market-intelligence.md` (primary)
2. Also save to `products/{slug}/research/market-intelligence-brief.md`
3. Log activity in daily file
4. Notify orchestrator or recommend next step:
   - If Go: Route to strategist for product definition
   - If Conditional: Route to audience agent for validation
   - If No-Go: Route to discovery for pivot exploration