# Stage 1: Load Brief

## Objective

Load and validate the product brief to ensure all necessary information is available for planning.

## Process

### Step 1: Locate Product Brief

Check for product brief in this order:

1. **Explicit path** - If provided as argument, use that path
2. **Product decisions file** - `.pawbytes/prodig-suites/brands/{brand-slug}/products/{product-slug}/product-decisions.md`
3. **Brief file** - `.pawbytes/prodig-suites/brands/{brand-slug}/products/{product-slug}/brief.md`
4. **Product context** - `.pawbytes/prodig-suites/brands/{brand-slug}/products/{product-slug}/product-context.md`

### Step 2: Verify Brief Completeness

Check for required sections:

| Section | Required | Description |
|---------|----------|-------------|
| Product name | Yes | Clear identifier |
| Product family | Yes | knowledge/template/software/service |
| Problem statement | Yes | What problem this solves |
| Target audience | Yes | Who will use this |
| Core value proposition | Yes | Why this product |
| Scope | Yes | What's included/excluded |
| Success criteria | Recommended | How to measure success |

### Step 3: Extract Key Decisions

Parse the brief for:

- **Product family:** knowledge | template | software | service
- **Product type:** Specific type within family (e.g., course, starter-kit, saas, consulting)
- **Scope boundaries:** Explicit inclusions and exclusions
- **Packaging decisions:** How it will be delivered
- **Dependencies:** External requirements or integrations

### Step 4: Flag Missing Information

If critical sections are missing:

1. Check if information exists in product-context.md
2. Check if decisions were recorded in brand context
3. List missing items that must be resolved before proceeding

## Output

```markdown
## Brief Summary

**Product:** [name]
**Family:** [knowledge/template/software/service]
**Type:** [specific type]
**Target:** [audience]
**Core problem:** [problem statement]

### Scope
- In scope: [list]
- Out of scope: [list]

### Key Decisions
- [Decision 1]
- [Decision 2]

### Completeness Status
[ ] All required sections present
[ ] Product family identified
[ ] Scope defined
[ ] Target audience specified

[If incomplete, list missing items]
```

## Progression Condition

Brief is loaded and verified complete. All required sections present, or missing items are documented for resolution in planning stage.