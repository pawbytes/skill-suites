# Stage 2: Assess Quality

## Purpose

Apply quality standards systematically across all dimensions. Score each dimension against defined criteria to build a complete picture of product readiness.

---

## Quality Dimensions

### 1. Functionality

**Question:** Does the product work as intended?

| Criterion | Score | Evidence |
|-----------|-------|----------|
| Core features functional | Pass / Fail / Partial / N/A | |
| No critical bugs | Pass / Fail / Partial / N/A | |
| Edge cases handled | Pass / Fail / Partial / N/A | |
| Performance acceptable | Pass / Fail / Partial / N/A | |

**Verification method:** Test main workflows, check error handling, verify performance claims.

### 2. Completeness

**Question:** Is everything included that should be?

| Criterion | Score | Evidence |
|-----------|-------|----------|
| All promised features present | Pass / Partial / Fail / N/A | |
| All referenced files included | Pass / Partial / Fail / N/A | |
| No placeholder content | Pass / Partial / Fail / N/A | |
| Scope fully covered | Pass / Partial / Fail / N/A | |

**Verification method:** Cross-reference with product brief, verify manifest matches contents.

### 3. Clarity

**Question:** Is the product immediately understandable?

| Criterion | Score | Evidence |
|-----------|-------|----------|
| Clear naming throughout | Pass / Partial / Fail / N/A | |
| No unexplained jargon | Pass / Partial / Fail / N/A | |
| Logical organization | Pass / Partial / Fail / N/A | |
| Purpose obvious in 30s | Pass / Partial / Fail / N/A | |

**Verification method:** Fresh-user test — can someone unfamiliar understand it quickly?

### 4. Usability

**Question:** Can users succeed without friction?

| Criterion | Score | Evidence |
|-----------|-------|----------|
| Works on first attempt | Pass / Partial / Fail / N/A | |
| Error messages helpful | Pass / Partial / Fail / N/A | |
| Recovery path exists | Pass / Partial / Fail / N/A | |
| Standard tools supported | Pass / Partial / Fail / N/A | |

**Verification method:** Follow quick start from scratch, attempt common mistakes.

### 5. Documentation

**Question:** Is documentation sufficient?

| Criterion | Score | Evidence |
|-----------|-------|----------|
| Quick start exists | Pass / Partial / Fail / N/A | |
| Full guide available | Pass / Partial / Fail / N/A | |
| Examples included | Pass / Partial / Fail / N/A | |
| Troubleshooting covers common issues | Pass / Partial / Fail / N/A | |

**Verification method:** Try to complete main task using only provided documentation.

### 6. Presentation (for Publish/Sellable)

**Question:** Is the product professionally presented?

| Criterion | Score | Evidence |
|-----------|-------|----------|
| Visual design polished | Pass / Partial / Fail / N/A | |
| Formatting consistent | Pass / Partial / Fail / N/A | |
| Professional appearance | Pass / Partial / Fail / N/A | |
| Platform requirements met | Pass / Partial / Fail / N/A | |

**Verification method:** Visual review, platform specification checklist.

### 7. Selling Assets (for Sellable)

**Question:** Are all selling assets present?

| Criterion | Score | Evidence |
|-----------|-------|----------|
| Marketing copy complete | Pass / Partial / Fail / N/A | |
| Preview/images included | Pass / Partial / Fail / N/A | |
| Pricing defined | Pass / Partial / Fail / N/A | |
| Support materials ready | Pass / Partial / Fail / N/A | |

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

```text
Status = Pass if all criteria Pass
       = Fail if any criterion in functional dimension Fail
       = Partial if mix of Pass and Partial
```

**Critical criteria:** All criteria in the Functionality dimension are considered critical. A Fail on any functional criterion blocks the dimension.

### Overall Quality Score

```text
Ready if: All dimensions Pass or Partial
Not Ready if: Any dimension Fail
```

---

## Assessment Process

### Step 1: Apply Type-Specific Criteria

Load relevant criteria from `readiness-criteria.csv`:

1. Read the CSV
2. Filter rows where `best_for` matches:
   - "All products" (always include)
   - Target readiness level (e.g., "Publish/Sellable" for publish-ready)
   - Product family (e.g., "Knowledge products", "Templates")
3. Apply each matched criterion
4. Record Pass/Fail/Partial/N/A with evidence

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

```text
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