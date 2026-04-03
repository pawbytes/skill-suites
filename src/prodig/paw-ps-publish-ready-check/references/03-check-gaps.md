# Stage 3: Check Gaps

## Purpose

Identify what specifically blocks release. Classify gaps by severity and generate an actionable fix list. This stage ensures transparency about what needs to change before the product is ready.

---

## Gap Classification

### Severity Levels

| Level | Definition | Impact on Release |
|-------|------------|-------------------|
| **Critical** | Blocks core functionality or violates promises | Must fix before any release |
| **Important** | Significantly impacts user experience | Should fix before publish/sale |
| **Minor** | Nice to have but not blocking | Can fix post-release |

### Gap Categories

| Category | Examples |
|----------|----------|
| **Functional** | Broken features, errors, crashes |
| **Content** | Missing content, placeholder text, thin value |
| **Documentation** | Unclear instructions, missing examples |
| **Presentation** | Formatting issues, unprofessional appearance |
| **Compliance** | Platform requirements, legal issues |
| **Selling** | Missing marketing assets, pricing undefined |

---

## Gap Detection Process

### Step 1: Review Failed Criteria

From Stage 2 assessment, extract all criteria that scored:
- **Fail** → Critical gap
- **Partial** → Important gap (usually)

For each failed criterion:
1. Describe the specific issue
2. Explain why it fails
3. Identify what's needed to pass
4. Estimate effort to fix

### Step 2: Identify Missing Elements

Check for commonly missed items:

**For all products:**
- [ ] No "Untitled" or generic names
- [ ] No placeholder text
- [ ] No broken links
- [ ] No broken references
- [ ] No TODO comments left in

**For publish-ready:**
- [ ] Platform specifications met
- [ ] File formats correct
- [ ] Preview materials ready
- [ ] Metadata complete

**For sellable-ready:**
- [ ] Product description written
- [ ] Pricing defined
- [ ] Preview images created
- [ ] Support plan defined
- [ ] Refund policy clarified

### Step 3: Check for Hidden Gaps

Look for issues not captured in criteria:

1. **Inconsistencies**
   - Naming inconsistent across files
   - Terminology varies
   - Style varies between sections

2. **Fragility**
   - Works only in specific conditions
   - Breaks with edge-case inputs
   - Depends on unstated assumptions

3. **Gaps in experience**
   - User might get stuck
   - Unclear what to do next
   - No help for common mistakes

4. **Value concerns**
   - Promises more than delivers
   - Time-to-value exceeds claims
   - Outcome not achievable as described

### Step 4: Validate Against Claims

Cross-reference with product brief:

| Claim | Status | Gap (if any) |
|-------|--------|--------------|
| {claim 1} | Met / Not Met | {gap description} |
| {claim 2} | Met / Not Met | {gap description} |

---

## Gap Documentation

### Gap Record Format

```
GAP: {short title}
SEVERITY: Critical / Important / Minor
CATEGORY: Functional / Content / Documentation / Presentation / Compliance / Selling
LOCATION: {specific file or component}

CURRENT STATE:
{what exists now}

REQUIRED STATE:
{what should exist}

FIX APPROACH:
{how to fix it}

EFFORT: {hours/days}
DEPENDENCIES: {other gaps or requirements}
```

### Example Gap Records

```
GAP: Missing installation instructions
SEVERITY: Important
CATEGORY: Documentation
LOCATION: docs/getting-started.md

CURRENT STATE:
File exists but only says "Install the package" with no steps.

REQUIRED STATE:
Step-by-step installation guide covering:
- Prerequisites
- Installation command
- Verification steps
- Common installation issues

FIX APPROACH:
Write complete installation section following documentation template.
Add screenshots of installation process.

EFFORT: 2 hours
DEPENDENCIES: None
```

```
GAP: Broken import on Windows
SEVERITY: Critical
CATEGORY: Functional
LOCATION: src/main.js line 45

CURRENT STATE:
Import uses Unix-style path, fails on Windows.

REQUIRED STATE:
Cross-platform path handling that works on all operating systems.

FIX APPROACH:
Replace hardcoded path with path.join() or path.resolve().

EFFORT: 30 minutes
DEPENDENCIES: None
```

---

## Fix List Generation

### Prioritization

Order fix list by:
1. Severity (Critical first)
2. Effort (Quick wins within severity)
3. Dependencies (Fix dependencies first)

### Fix List Format

```markdown
# Fix List: {product-name}

**Generated:** {date}
**Target Readiness:** {level}
**Total Gaps:** {count}
**Critical:** {count}
**Important:** {count}
**Minor:** {count}

---

## Critical (Must Fix)

### 1. {gap-title}
- **Location:** {file/component}
- **Issue:** {brief description}
- **Fix:** {approach}
- **Effort:** {estimate}

### 2. ...

---

## Important (Should Fix)

### 1. {gap-title}
...

---

## Minor (Nice to Have)

### 1. {gap-title}
...

---

## Summary

Total estimated effort: {hours}
Recommended sequence: {order}
```

---

## Gap Summary Metrics

Record for the report:

| Metric | Count |
|--------|-------|
| Total gaps | |
| Critical | |
| Important | |
| Minor | |
| Estimated effort | |

---

## Quality Gate

Before proceeding to Stage 4:

- [ ] All failed criteria converted to gaps
- [ ] All gaps classified by severity
- [ ] Fix approach documented for each
- [ ] Effort estimated
- [ ] Fix list generated

**Note:** Even if gaps exist, proceed to Stage 4 to generate the verdict. The verdict will reflect the gap status.