# Stage 2: Assess Quality

## Purpose

Apply quality standards systematically across all dimensions. Score each dimension against defined criteria to build a complete picture of product readiness.

---

## Quality Dimensions

### 1. Functionality

**Question:** Does the product work as intended?

| Criterion | Score | Evidence |
|-----------|-------|----------|
| Core features functional | Pass / Fail / N/A | |
| No critical bugs | Pass / Fail / N/A | |
| Edge cases handled | Pass / Fail / N/A | |
| Performance acceptable | Pass / Fail / N/A | |

**Verification method:** Test main workflows, check error handling, verify performance claims.

### 2. Completeness

**Question:** Is everything included that should be?

| Criterion | Score | Evidence |
|-----------|-------|----------|
| All promised features present | Pass / Fail / N/A | |
| All referenced files included | Pass / Fail / N/A | |
| No placeholder content | Pass / Fail / N/A | |
| Scope fully covered | Pass / Fail / N/A | |

**Verification method:** Cross-reference with product brief, verify manifest matches contents.

### 3. Clarity

**Question:** Is the product immediately understandable?

| Criterion | Score | Evidence |
|-----------|-------|----------|
| Clear naming throughout | Pass / Fail / N/A | |
| No unexplained jargon | Pass / Fail / N/A | |
| Logical organization | Pass / Fail / N/A | |
| Purpose obvious in 30s | Pass / Fail / N/A | |

**Verification method:** Fresh-user test — can someone unfamiliar understand it quickly?

### 4. Usability

**Question:** Can users succeed without friction?

| Criterion | Score | Evidence |
|-----------|-------|----------|
| Works on first attempt | Pass / Fail / N/A | |
| Error messages helpful | Pass / Fail / N/A | |
| Recovery path exists | Pass / Fail / N/A | |
| Standard tools supported | Pass / Fail / N/A | |

**Verification method:** Follow quick start from scratch, attempt common mistakes.

### 5. Documentation

**Question:** Is documentation sufficient?

| Criterion | Score | Evidence |
|-----------|-------|----------|
| Quick start exists | Pass / Fail / N/A | |
| Full guide available | Pass / Fail / N/A | |
| Examples included | Pass / Fail / N/A | |
| Troubleshooting covers common issues | Pass / Fail / N/A | |

**Verification method:** Try to complete main task using only provided documentation.

### 6. Presentation (for Publish/Sellable)

**Question:** Is the product professionally presented?

| Criterion | Score | Evidence |
|-----------|-------|----------|
| Visual design polished | Pass / Fail / N/A | |
| Formatting consistent | Pass / Fail / N/A | |
| Professional appearance | Pass / Fail / N/A | |
| Platform requirements met | Pass / Fail / N/A | |

**Verification method:** Visual review, platform specification checklist.

### 7. Selling Assets (for Sellable)

**Question:** Are all selling assets present?

| Criterion | Score | Evidence |
|-----------|-------|----------|
| Marketing copy complete | Pass / Fail / N/A | |
| Preview/images included | Pass / Fail / N/A | |
| Pricing defined | Pass / Fail / N/A | |
| Support materials ready | Pass / Fail / N/A | |

**Verification method:** Listing requirements checklist.

---

## Scoring System

### Score Definitions

| Score | Meaning |
|-------|---------|
| **Pass** | Criterion fully met |
| **Fail** | Criterion not met (blocking issue) |
| **Partial** | Criterion partially met (non-blocking) |
| **N/A** | Not applicable to this product type |

### Dimension Status

Calculate for each dimension:

```
Status = Pass if all criteria Pass
       = Fail if any critical criterion Fail
       = Partial if mix of Pass and Partial
```

### Overall Quality Score

```
Ready if: All dimensions Pass or Partial
Not Ready if: Any dimension Fail
```

---

## Assessment Process

### Step 1: Apply Type-Specific Criteria

Load relevant criteria from `readiness-criteria.csv` based on product type:

1. Read the CSV
2. Filter rows matching product type
3. Apply each criterion
4. Record pass/fail with evidence

### Step 2: Test Core Workflows

Execute main user workflows:
1. Identify top 3 user journeys
2. Walk through each journey
3. Note any friction or failure
4. Record time-to-value

### Step 3: Verify Claims

Cross-reference with product brief:
1. List all promised outcomes
2. Verify each outcome is achievable
3. Note any unfulfilled claims
4. Flag misleading promises

### Step 4: Document Evidence

For each dimension:
- Record specific evidence
- Note any concerns
- Identify gaps for Stage 3

---

## Assessment Record Template

```
QUALITY ASSESSMENT

Product: {name}
Type: {type}
Target: {readiness-level}
Date: {date}

DIMENSION: Functionality
| Criterion | Score | Evidence |
|-----------|-------|----------|
| Core features functional | {score} | {evidence} |
| No critical bugs | {score} | {evidence} |
| ... | ... | ... |
DIMENSION STATUS: {Pass/Fail/Partial}

DIMENSION: Completeness
...

OVERALL STATUS: {Ready/Not Ready}
```

---

## Quality Gate

Before proceeding to Stage 3:

- [ ] All dimensions assessed
- [ ] All criteria scored
- [ ] Evidence documented
- [ ] Overall status determined

If any dimension is **Fail**, the product is **Not Ready** — proceed to Stage 3 to document gaps.