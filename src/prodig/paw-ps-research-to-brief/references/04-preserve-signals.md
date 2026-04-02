# Stage 4: Preserve Signals

## Objective

Document key evidence sources and unresolved uncertainties to ensure no critical information is lost during the synthesis process. Create a signal log that traces brief decisions back to research findings.

---

## Signal Categories

### 1. Evidence Signals

Strong data points that influenced brief content.

| Field | Description |
|-------|-------------|
| Signal ID | Unique identifier (SIG-001, SIG-002, etc.) |
| Source | Originating file and section |
| Content | The actual evidence |
| Brief Impact | How it shaped the brief |
| Confidence | High/Medium/Low |

### 2. Uncertainty Signals

Open questions, assumptions, or gaps requiring validation.

| Field | Description |
|-------|-------------|
| Signal ID | Unique identifier (UNC-001, UNC-002, etc.) |
| Type | Gap, Assumption, Conflict, Outdated |
| Description | The uncertainty |
| Impact | Consequence if unresolved |
| Resolution Path | How to address it |

### 3. Decision Signals

Explicit choices made during synthesis.

| Field | Description |
|-------|-------------|
| Signal ID | Unique identifier (DEC-001, DEC-002, etc.) |
| Decision | What was decided |
| Rationale | Why this choice |
| Alternatives Considered | Other options |
| Reversibility | Easy/Hard to change later |

---

## Procedure

### Step 1: Scan for Evidence Signals

Review each source file for:
- Quantified claims (statistics, metrics)
- Cited sources and references
- Expert opinions or quotes
- Verified observations

For each, create an evidence signal entry:

```markdown
## Evidence Signals

### SIG-001
- **Source:** market-intelligence.md > Market Size
- **Content:** "TAM estimated at $2.3B with 15% CAGR through 2027"
- **Brief Impact:** Market Opportunity section growth rate
- **Confidence:** Medium (secondary research)
```

### Step 2: Identify Uncertainty Signals

Review for:
- Stated assumptions without evidence
- Conflicting information between sources
- Missing critical data
- Outdated information

Create uncertainty signal entries:

```markdown
## Uncertainty Signals

### UNC-001
- **Type:** Assumption
- **Description:** Assumed 60% of target audience has smartphones
- **Impact:** Affects mobile-first strategy viability
- **Resolution Path:** Run audience technology survey

### UNC-002
- **Type:** Conflict
- **Description:** Market research shows growing demand; audience research shows low awareness
- **Impact:** Market timing unclear
- **Resolution Path:** Validate with primary research
```

### Step 3: Document Decision Signals

Record synthesis decisions:

```markdown
## Decision Signals

### DEC-001
- **Decision:** Defined primary persona as "Small Business Owner"
- **Rationale:** Largest segment with clearest pain points
- **Alternatives Considered:** "Enterprise Manager" (secondary), "Freelancer" (too small)
- **Reversibility:** Medium - affects messaging and features

### DEC-002
- **Decision:** Set success metric: 10% market penetration in Year 1
- **Rationale:** Conservative based on competitor benchmarks
- **Alternatives Considered:** 5% (too conservative), 20% (optimistic)
- **Reversibility:** High - metric can be adjusted
```

### Step 4: Write Signal Notes

Create `signal-notes.md`:

```markdown
# Signal Notes: {product-name}

**Generated:** {date}
**Brief Version:** 1.0

---

## Summary

- Evidence Signals: [count]
- Uncertainty Signals: [count]
- Decision Signals: [count]

---

## Evidence Signals

[All SIG entries]

---

## Uncertainty Signals

[All UNC entries]

---

## Decision Signals

[All DEC entries]

---

## Priority Actions

Based on signal analysis, recommended next actions:

1. [Highest priority uncertainty to resolve]
2. [Evidence that needs validation]
3. [Decision that should be reviewed with stakeholders]
```

### Step 5: Update Product Decisions

If `product-decisions.md` exists, append:

```markdown
## Brief Generated: {date}

- **Brief Version:** 1.0
- **Evidence Count:** [N]
- **Uncertainty Count:** [N]
- **Decision Count:** [N]
- **Primary Gaps:** [list critical uncertainties]

---
```

---

## Signal Preservation Rules

1. **Never lose a source citation.** Every claim in the brief should trace to a signal.

2. **Never hide uncertainty.** Gaps are documented, not smoothed over.

3. **Never fabricate confidence.** Signal confidence reflects source quality.

4. **Always enable reversal.** Decision signals include alternatives for future reference.

---

## Progression Criteria

**Complete when:**
- All evidence signals extracted from available sources
- All uncertainties identified and categorized
- All synthesis decisions documented
- Signal notes file written
- Product decisions file updated (if exists)

---

## Final Deliverables

| File | Location |
|------|----------|
| Product Brief | `.pawbytes/prodig-suites/products/{product-slug}/product-brief.md` |
| Signal Notes | `.pawbytes/prodig-suites/products/{product-slug}/signal-notes.md` |

---

## Exit Report

Generate final status:

```markdown
## Workflow Complete

**Product:** {product-slug}
**Brief Version:** 1.0
**Status:** SUCCESS / SUCCESS_WITH_GAPS

### Files Created
- product-brief.md
- signal-notes.md

### Signal Summary
- Evidence: [N] signals
- Uncertainties: [N] signals ([X] critical)
- Decisions: [N] signals

### Recommendations
1. [Review brief with stakeholders]
2. [Address critical uncertainties: {list}]
3. [Validate key assumptions before proceeding to design]
```