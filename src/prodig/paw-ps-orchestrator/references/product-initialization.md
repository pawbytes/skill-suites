# Product Initialization

## Purpose

Create a new product workspace when the user starts a fresh product.

## When to Initialize

Initialize a new product when:
- User has no active products and wants to create something
- User explicitly requests to start a new product
- User's current direction is different enough to warrant a separate workspace

## Initialization Process

### 1. Gather Initial Context

Ask targeted questions to capture the product concept:

**Minimum viable questions:**
1. What's the product idea? (1-2 sentences)
2. What type of product? (course, ebook, template pack, SaaS, service, etc.)
3. Who is it for? (target audience, optional at this stage)

**Example interaction:**
```
"Let's capture your product idea. Tell me:
1. What's the core concept?
2. What type of product is this?

Don't worry if details are fuzzy — we'll refine through discovery."
```

### 2. Generate Product Slug

Create a URL-safe identifier:

| Product Name | Slug |
|--------------|------|
| AI Course for Beginners | ai-course-for-beginners |
| Notion Templates Pack | notion-templates-pack |
| SaaS Metrics Dashboard | saas-metrics-dashboard |

**Rules:**
- Lowercase only
- Use hyphens instead of spaces
- Alphanumeric characters and hyphens only
- Max 50 characters

### 3. Create Directory Structure

Scaffold the product workspace:

```
.pawbytes/prodig-suites/products/{product-slug}/
├── product-context.md      # Product definition and current state
├── artifacts/              # Generated outputs
│   └── .gitkeep
└── notes/                  # User's working notes
    └── .gitkeep
```

### 4. Initialize product-context.md

Create the initial product context file:

```markdown
# Product: {Product Name}

**Slug:** {product-slug}
**Type:** {product-type}
**Created:** {YYYY-MM-DD}
**Status:** discovery
**Current Stage:** discovery

## Concept

{User's initial description}

## Target Audience

{If captured, otherwise: "To be defined in audience discovery"}

## Goals

- {Goal 1 if stated}
- {Goal 2 if stated}

## Constraints

{Any constraints mentioned by user}

## Key Decisions

| Decision | Choice | Rationale | Date |
|----------|--------|-----------|------|
| Product type | {type} | User stated | {date} |

## Stage Progress

| Stage | Status | Started | Completed |
|-------|--------|---------|-----------|
| Discovery | in_progress | {date} | - |
| Research | pending | - | - |
| Audience | pending | - | - |
| Strategy | pending | - | - |
| Execution | pending | - | - |
| Packaging | pending | - | - |
| Readiness | pending | - | - |

## Related Files

- Market Intelligence: (pending)
- Audience Intelligence: (pending)
- Product Decisions: (pending)
- Artifacts: `./artifacts/`
```

### 5. Update Sidecar Index

Add the new product to the shared sidecar index:

```markdown
## Active Products

| Product | Type | Stage | Last Active |
|---------|------|-------|-------------|
| {product-name} | {type} | discovery | {date} |
```

### 6. Log to Daily File

Record the initialization:

```markdown
## {YYYY-MM-DD}

### {timestamp} - paw-ps-orchestrator

**Action:** Product initialized

**Product:** {product-name}
**Type:** {product-type}
**Initial concept:** {concept summary}

**Next:** Discovery or Research phase
```

## Product Selection

When multiple products exist, help user select:

### Discovery and Presentation

```markdown
I found {N} products in progress:

| # | Product | Type | Stage | Last Active |
|---|---------|------|-------|-------------|
| 1 | AI Course | knowledge | strategy | 2 days ago |
| 2 | Templates Pack | template | execution | 1 week ago |

Which would you like to continue, or start something new?
```

### Load Selected Product

When user selects a product:

1. Read `{product-slug}/product-context.md`
2. Check for related curated files (market-intelligence.md, etc.)
3. Summarize current state
4. Offer context-appropriate next steps

## Product Archival

When a product is complete or abandoned:

1. Mark status in product-context.md:
   ```markdown
   **Status:** archived
   **Archive Reason:** {launched|abandoned|merged}
   **Archived Date:** {date}
   ```

2. Move to archive directory:
   ```
   .pawbytes/prodig-suites/products/_archived/{product-slug}/
   ```

3. Update sidecar index to remove from active list

## Multi-Product Management

### Switching Products

When user wants to work on a different product:

```
"Switching to '{product}'. Let me load its context...

**Current state:** {stage} stage
**Last action:** {last action}
**Next recommended:** {next step}

Ready to continue?"
```

### Parallel Products

User can have multiple active products:

- Each has its own workspace
- Shared memory contains overview of all
- Switching is seamless via product selection

## Edge Cases

### Duplicate Product Names

If user tries to create a product with existing name:

```
"You already have a product called '{name}'. Would you like to:
1. Continue that product
2. Create a new version with a different name
3. Archive the old one and create fresh"
```

### Merging Products

If user wants to merge two products:

1. Create merged product-context.md combining both
2. Note the merge in product-decisions.md
3. Archive the source products
4. Continue with merged product

### Splitting Products

If user wants to split a product:

1. Create new product-context.md for each split
2. Distribute relevant context to each
3. Note the split in original product-decisions.md
4. User can continue with either or both