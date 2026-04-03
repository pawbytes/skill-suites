# Stage 1: Load Bundle

## Purpose

Gather the packaged product bundle and establish context for evaluation. Identify product type, locate standards, and prepare for systematic assessment.

---

## Steps

### 1. Locate Product Workspace

Check for active product:
```
{project-root}/.pawbytes/prodig-suites/active-product.md
```

If not found, prompt for product slug (in interactive mode) or scan for most recently modified workspace (in headless mode).

### 2. Identify Product Bundle

Look for packaged bundle at:
```
{project-root}/.pawbytes/prodig-suites/products/{product-slug}/bundle/
```

Bundle should contain:
- Main product files
- Documentation
- Assets
- Manifest or index

### 3. Load Product Context

Read product context files:
- `product-context.md` — Product type, target audience, scope
- `product-brief.md` — Promised outcomes, features
- `product-decisions.md` — Prior decisions that affect readiness

### 4. Load Output Standards

Check for workspace standards:
```
{project-root}/.pawbytes/prodig-suites/standards/output-standards.md
```

If not found, use built-in criteria from `./references/readiness-criteria.csv`.

### 5. Determine Product Type

Classify the product to select appropriate criteria:

| Type | Indicators |
|------|------------|
| **Knowledge Product** | Ebooks, guides, courses, tutorials |
| **Template** | Notion templates, spreadsheets, planners |
| **Prompt Pack** | Collections of AI prompts |
| **Digital Kit** | Bundled assets, templates, guides |
| **Software** | Apps, tools, scripts, integrations |
| **Service** | Service offerings, consulting packages |
| **Membership** | Subscription content, community access |

### 6. Confirm Target Readiness Level

Determine which readiness level to evaluate against:

- **Production-ready** — Functional, usable
- **Publish-ready** — Polished, platform-ready
- **Sellable-ready** — Complete with selling assets

If not specified:
- Default to `publish-ready` for standalone products
- Default to `sellable-ready` for products in marketplace
- Default to `production-ready` for internal tools

---

## Checklist

Before proceeding to Stage 2:

- [ ] Product workspace located
- [ ] Bundle directory exists and is populated
- [ ] Product type identified
- [ ] Target readiness level confirmed
- [ ] Output standards loaded (workspace or defaults)
- [ ] Product context reviewed

---

## Output

At the end of this stage, record:

```
PRODUCT: {product-slug}
TYPE: {product-type}
TARGET: {readiness-level}
BUNDLE: {bundle-path}
STANDARDS: {standards-source}
```

This context will be used throughout the remaining stages.