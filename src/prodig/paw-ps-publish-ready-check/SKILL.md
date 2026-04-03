---
name: paw-ps-publish-ready-check
description: "Evaluate whether a product is production-ready, publish-ready, or sellable-ready. Triggers: 'publish ready', 'ready check', 'readiness review', 'quality check', 'production ready', 'sellable ready', 'can I publish', 'release check', 'final review'."
---

# Publish Ready Check

## Overview

A rigorous quality evaluation workflow that determines whether a product meets the threshold for production, publication, or sale. This workflow protects the suite from overclaiming readiness by applying clear quality bars rather than superficial approval.

**Args:** Accepts `--headless` / `-H` for non-interactive execution.

**Output:** Readiness report (HTML), gap analysis, final verdict with fix list if applicable.

---

## Pipeline

### Stage 1: Load Bundle
Load `./references/01-load-bundle.md`

Gather the packaged product bundle and locate all relevant standards and context files. Establish what type of product is being evaluated and which standards apply.

**Progression:** Proceed when product bundle is located and product type is identified.

### Stage 2: Assess Quality
Load `./references/02-assess-quality.md`

Apply quality standards systematically across all dimensions: functionality, completeness, clarity, usability, and documentation. Score each dimension against defined criteria.

**Progression:** Proceed when all quality dimensions have been assessed and scored.

### Stage 3: Check Gaps
Load `./references/03-check-gaps.md`

Identify what specifically blocks release. Classify gaps as critical (must fix), important (should fix), or minor (nice to have). Generate actionable fix list.

**Progression:** Proceed when all gaps are documented with severity classification.

### Stage 4: Generate Verdict
Load `./references/04-generate-verdict.md`

Make final determination: production-ready, publish-ready, sellable-ready, or not-ready. Apply the appropriate threshold based on the target readiness level.

**Progression:** Complete when verdict is issued and documented.

---

## On Activation

1. Determine the product workspace root: `{project-root}/.pawbytes/prodig-suites/`
2. Identify active product from `.pawbytes/prodig-suites/active-product.md` if it exists
3. If no active product and not in headless mode, prompt user to specify:
   - Product slug (which product to evaluate)
   - Target readiness level (production / publish / sellable)
4. Begin pipeline at Stage 1

---

## Readiness Levels

| Level | Definition | Quality Bar |
|-------|------------|-------------|
| **Production-ready** | Complete, functional, usable by intended audience | Core functionality works, documentation adequate, no critical bugs |
| **Publish-ready** | Formatted, polished, ready for publication platform | Production-ready + professional presentation, platform requirements met |
| **Sellable-ready** | Complete, polished, has all selling assets | Publish-ready + marketing assets, pricing, support materials |

**Hierarchy:** Sellable-ready requires publish-ready, which requires production-ready.

---

## Input Sources

| Source | File Path | Purpose |
|--------|-----------|---------|
| Product Bundle | `.pawbytes/prodig-suites/products/{product-slug}/bundle/` | Packaged product files |
| Output Standards | `.pawbytes/prodig-suites/standards/output-standards.md` | Quality criteria |
| Product Context | `.pawbytes/prodig-suites/products/{product-slug}/product-context.md` | Product type and requirements |
| Product Brief | `.pawbytes/prodig-suites/products/{product-slug}/product-brief.md` | Scope and promises |
| Product Decisions | `.pawbytes/prodig-suites/products/{product-slug}/product-decisions.md` | Prior decisions |

**Minimum Requirement:** Product bundle must exist. Standards may be loaded from references if not in workspace.

---

## Output Structure

```
.pawbytes/prodig-suites/products/{product-slug}/
├── readiness-report.html         # Structured assessment (HTML)
├── readiness-report.md           # Plain text version
├── gap-analysis.md               # Detailed gap breakdown
├── fix-list.md                   # Actionable fixes (if not ready)
└── product-decisions.md          # Appended verdict
```

Daily log entry at:
```
.pawbytes/prodig-suites/memory/paw-ps-sidecar/daily/YYYY-MM-DD.md
```

---

## Reference Lookup Protocol

1. Read `./references/readiness-criteria.csv` — lightweight index of criteria by product type
2. Match product type to relevant criteria rows
3. Apply matched criteria during Stage 2 assessment
4. Reference full standards from `./references/frameworks/` only when needed

---

## Output Contract

Every execution delivers:

- **Action type:** Readiness evaluation
- **Verdict:** production-ready / publish-ready / sellable-ready / not-ready
- **Files saved:**
  - `readiness-report.html` — Structured assessment
  - `readiness-report.md` — Plain text version
  - `gap-analysis.md` — Gap breakdown
  - `fix-list.md` — (If not ready) Actionable fixes
- **Recommendations:** Next steps based on verdict
- **File saved to:** `.pawbytes/prodig-suites/products/{product-slug}/`

---

## Headless Mode

When invoked with `--headless` or `-H`:

1. Attempt to read active product from `.pawbytes/prodig-suites/active-product.md`
2. If not found, scan for most recently modified product workspace
3. Default target readiness level to `publish-ready` unless specified via args
4. Execute all stages without prompts
5. Document any assumptions in the report
6. Exit with status code:
   - 0: Ready (verdict matches target)
   - 1: Not ready (gaps exist)
   - 2: Error (inputs missing)

---

## Quality Gates

| Stage | Gate Condition |
|-------|----------------|
| Load Bundle | Product bundle located, product type identified |
| Assess Quality | All quality dimensions scored |
| Check Gaps | All gaps documented with severity |
| Generate Verdict | Verdict issued with justification |

---

## Non-Negotiables

This workflow must apply **clear quality bars**, not superficial approval:

1. **No rubber-stamping** — Every verdict must be justified with evidence
2. **Gap visibility** — All blocking issues documented, none hidden
3. **Honest assessment** — Better to delay release than ship broken products
4. **User clarity** — Fix list must be actionable and specific
5. **Standards matter** — Apply the criteria, don't lower the bar

---

## Escalation Routes

| Signal | Routes To | Why |
|--------|-----------|-----|
| Quality issues found | paw-ps-orchestrator | Coordinate fixes with specialists |
| Standards unclear | paw-ps-strategist | Clarify quality requirements |
| Multiple products to check | paw-ps-orchestrator | Batch coordination |