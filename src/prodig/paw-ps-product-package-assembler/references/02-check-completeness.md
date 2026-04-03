# Stage 2: Check Completeness

Verify artifact inventory against product-type requirements to identify missing pieces before final review.

## Goal

Produce a completeness report showing what's present, what's missing, and what's optional but recommended.

## Completeness Criteria

Completeness criteria come from two sources:

1. **Product type requirements** — defined in output-standards.md
2. **Product-specific requirements** — defined in product context

### Product Type Requirements

Load `{project-root}/.pawbytes/prodig-suites/output-standards.md` to get the standard requirements for each product type:

| Product Type | Required | Recommended | Optional |
|--------------|----------|-------------|----------|
| Document | Main document, outline, sources | Research notes, revision history | Glossary, appendices |
| Application | Code package, README, setup guide | Tests, documentation | Examples, tutorials |
| Campaign | Creative assets, copy, strategy brief | Timeline, budget | Analytics setup |
| Report | Report document, data sources, methodology | Executive summary, visualizations | Raw data, code |
| Presentation | Slide deck, speaker notes | Handouts, recordings | Follow-up materials |

### Product-Specific Requirements

Check `{product-slug}/context.md` for any custom requirements specified during discovery:

```yaml
requirements:
  required:
    - main-document
    - technical-specs
  recommended:
    - user-guide
    - api-documentation
  optional:
    - video-tutorial
```

## Verification Process

For each artifact category:

1. **Required artifacts** — Must be present. Missing = incomplete package.
2. **Recommended artifacts** — Should be present. Missing = warning.
3. **Optional artifacts** — Nice to have. Missing = info only.

Cross-reference artifact inventory against requirements:

```markdown
## Completeness Check

### Required Artifacts
| Requirement | Status | Artifact |
|-------------|--------|----------|
| Main document | PRESENT | artifacts/main.md |
| Outline | MISSING | — |
| Sources | PRESENT | artifacts/sources.md |

### Recommended Artifacts
| Requirement | Status | Artifact |
|-------------|--------|----------|
| Research notes | MISSING | — |
| Revision history | PRESENT | artifacts/history.md |

### Summary
- Required present: 2/3 (67%)
- Recommended present: 1/2 (50%)
- Overall completeness: PARTIAL
```

## Missing Items Classification

Classify missing items by impact:

| Impact | Description | Action |
|--------|-------------|--------|
| **Blocker** | Required artifact missing, package unusable | Must resolve before packaging |
| **Warning** | Recommended artifact missing, quality impact | Flag in report, proceed with note |
| **Info** | Optional artifact missing, minimal impact | Log for reference |

## Output

Update `packaging-status.md` with completeness results:

```markdown
## Completeness Report

### Status: PARTIAL

### Required Artifacts ({present}/{total})
| Requirement | Status | Artifact | Notes |
|-------------|--------|----------|-------|
| ... | ... | ... | ... |

### Missing Required (BLOCKERS)
1. {requirement-name} — {impact description}
   - Suggested action: {action}

### Missing Recommended (WARNINGS)
1. {requirement-name} — {impact description}

### Completeness Score
- Required: {percentage}%
- Recommended: {percentage}%
- Overall: {percentage}%
```

## Progression

- **All required present:** Proceed to Stage 3 (Organize Bundle)
- **Missing required items (interactive):** Ask user whether to:
  - Wait for execution to complete
  - Route back to executor
  - Proceed with incomplete package
- **Missing required items (headless):** Route back to orchestrator with missing items list

Do not proceed to Stage 3 until all blockers are resolved or explicitly acknowledged.