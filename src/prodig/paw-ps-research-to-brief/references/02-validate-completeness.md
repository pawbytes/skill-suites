# Stage 2: Validate Completeness

## Objective

Assess whether gathered inputs meet minimum thresholds for producing a meaningful product brief. Identify gaps and document decisions about proceeding with incomplete data.

---

## Completeness Matrix

### Minimum Thresholds

| Input Type | Minimum Required | Ideal State |
|------------|------------------|-------------|
| Discovery | Problem statement + vision | Full product-context.md |
| Market | Market opportunity statement | Competitive analysis + trends |
| Audience | At least 1 persona definition | Full audience profiles + journey |

**Minimum to Proceed:** At least one input type with minimum required content.

### Quality Indicators

| Indicator | Weight | Assessment |
|-----------|--------|------------|
| Evidence specificity | High | Claims backed by data/sources |
| Recency | Medium | Data less than 6 months old |
| Coverage | High | All key domains addressed |
| Internal consistency | High | No contradictions between sources |

---

## Procedure

### Step 1: Score Each Input

For each located input file, assess:

1. **Structural completeness**
   - Are expected sections present?
   - Are sections populated with content?

2. **Content quality**
   - Is content specific or generic?
   - Are claims supported by evidence?
   - Are there clear actionability indicators?

3. **Cross-reference alignment**
   - Do discovery assumptions align with market findings?
   - Do audience needs align with problem statement?

### Step 2: Identify Gaps

Document gaps in the gap log:

```markdown
## Gap Log

| Area | Missing Element | Severity | Source Dependency |
|------|-----------------|----------|-------------------|
| [area] | [what's missing] | critical/moderate/minor | [which input should provide it] |
```

### Step 3: Make Proceed Decision

**Proceed with full synthesis when:**
- All three input types present
- At least 2 have "good" quality scores
- No critical gaps identified

**Proceed with partial synthesis when:**
- At least 1 input type present with minimum content
- Critical gaps are documented
- Decision to proceed is explicit

**Block and recommend research when:**
- No inputs meet minimum threshold
- Critical gaps cannot be worked around

---

## Validation Report

Generate a validation summary:

```markdown
## Input Validation Report

### Completeness Score
- Discovery: [X/10] - [brief justification]
- Market Intelligence: [X/10] - [brief justification]
- Audience Intelligence: [X/10] - [brief justification]

### Overall Status
[READY / PROCEED_WITH_GAPS / BLOCKED]

### Critical Gaps
[List any critical gaps requiring attention]

### Recommendations
[Proceed as-is / Run additional research / Manual input needed]
```

---

## Progression Criteria

**Proceed to Stage 3 when:**
- Status is READY or PROCEED_WITH_GAPS
- If PROCEED_WITH_GAPS, gaps are documented in gap log

**Block and route when:**
- Status is BLOCKED
- Recommend running research skills: `paw-ps-discovery`, `paw-ps-research`, or `paw-ps-audience`

---

## Headless Behavior

In headless mode:
1. Apply scoring thresholds automatically
2. If BLOCKED, write validation report and exit with code 1
3. If PROCEED_WITH_GAPS, document gaps and continue
4. Never prompt for decisions—use conservative defaults