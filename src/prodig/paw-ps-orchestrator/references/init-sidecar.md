# Initialize Sidecar

## Purpose

First-run setup for Prodig Suites shared memory when the sidecar doesn't exist yet.

## When to Run

Execute this process when:
- First activation of any Prodig Suites agent
- Sidecar directory doesn't exist
- Sidecar exists but is empty or corrupted

## Initialization Steps

### 1. Create Directory Structure

```text
.pawbytes/prodig-suites/
├── memory/
│   └── paw-ps-sidecar/
│       ├── index.md
│       ├── daily/
│       └── curated/
│           └── product-types/
├── products/
└── artifacts/
```

### 2. Create index.md

```markdown
# Prodig Suites Memory Index

**Created:** {YYYY-MM-DD}
**Last Updated:** {YYYY-MM-DD}

Welcome to Prodig Suites! This is the shared memory system that maintains context across all your product creation sessions.

## Active Products

No products yet. Start your first product with:
- "I want to create a course about..."
- "Help me build a template pack for..."
- "I have an idea for a SaaS product..."

## Recent Activity

*No activity yet — this will be populated as you work.*

## Curated Files Status

| File | Status | Description |
|------|--------|-------------|
| product-context.md | Not created | Will hold your active product definition |
| market-intelligence.md | Not created | Will hold research synthesis |
| audience-intelligence.md | Not created | Will hold customer insights |
| product-decisions.md | Not created | Will hold decision history |
| output-standards.md | Not created | Will hold quality criteria |

## Product Types

Prodig Suites supports four product families:

1. **Knowledge Products** — Courses, ebooks, guides, memberships
2. **Template Products** — Templates, prompt packs, digital kits
3. **Software Products** — SaaS, apps, AI tools
4. **Service Products** — Productized services, consulting packages

## How Memory Works

- **Daily files** capture session activity (chronological, append-only)
- **Curated files** hold structured knowledge (updated as you progress)
- **Index** (this file) provides quick orientation
- All agents share this memory, so context persists across sessions

## Getting Started

Tell me what you want to create, and I'll help you through the full journey from idea to production-ready product.
```

### 3. Create Starter Curated Files

#### product-context.md

```markdown
# Product Context

*No active product yet. This file will be populated when you start a product.*

## Starting a Product

Tell the orchestrator:
- What product you want to create
- What type it might be (course, template, SaaS, service)
- Who it's for (if you know)
```

#### output-standards.md

```markdown
# Output Standards

Quality criteria for Prodig Suites deliverables.

## Default Quality Bar

By default, Prodig Suites targets **production-ready** outputs.

### Production-Ready Definition

An output is production-ready when:
- It's complete (no placeholders or TODOs)
- It follows consistent structure
- It's usable by the intended audience
- It requires minimal editing before use

### Higher Bars

- **Publish-ready**: Formatted, reviewed, ready for publication
- **Sellable-ready**: Complete, polished, ready to sell

## Product-Type Standards

### Knowledge Products
- Clear learning objectives
- Logical progression
- Actionable content
- Complete materials

### Template Products
- Working templates
- Clear instructions
- Consistent formatting
- Reusable design

### Software Products
- Clear feature definition
- User flow documented
- Technical requirements stated
- MVP scope defined

### Service Products
- Clear offer structure
- Defined deliverables
- Scope boundaries
- Pricing logic

## Artifact Quality

All artifacts should:
- Use consistent naming conventions
- Be saved in correct locations
- Include necessary context
- Be version-stamped if iterative
```

### 4. Create Product Type Starter Files

#### curated/product-types/knowledge-products.md

```markdown
# Knowledge Products

Best practices and structures for courses, ebooks, guides, and memberships.

## Product Types

### Courses
- Define learning outcomes first
- Structure in modules → lessons → topics
- Include practice activities
- Plan assessments

### Ebooks/Guides
- Define reader transformation
- Structure in chapters → sections
- Include examples and templates
- Plan call-to-actions

### Memberships
- Define content pillars
- Plan release cadence
- Structure access levels
- Design community elements

## Output Structure

```text
knowledge-product/
├── curriculum.md        # Course outline or chapter structure
├── modules/
│   ├── module-1.md
│   ├── module-2.md
│   └── ...
├── materials/           # Supporting materials
└── assets/              # Images, downloads, etc.
```
```

#### curated/product-types/template-products.md

```markdown
# Template Products

Best practices for templates, prompt packs, and digital kits.

## Product Types

### Templates
- Solve specific problems
- Include clear instructions
- Use placeholder conventions
- Design for reusability

### Prompt Packs
- Group by use case
- Include example outputs
- Document parameters
- Provide variation templates

### Digital Kits
- Combine complementary assets
- Provide assembly guide
- Include source files
- Document dependencies

## Output Structure

```text
template-product/
├── templates/
│   ├── template-1.{ext}
│   └── ...
├── guide.md            # Usage instructions
├── examples/           # Example outputs
└── assets/             # Supporting files
```
```

#### curated/product-types/software-products.md

```markdown
# Software Products

Best practices for SaaS, apps, and AI tools.

## Product Types

### SaaS/Apps
- Define core value proposition
- Map user journeys
- Define MVP features
- Plan technical architecture

### AI Tools
- Define AI capabilities
- Document prompts/flows
- Plan integrations
- Design user interface

## Output Structure

```text
software-product/
├── prd-lite.md         # Product requirements
├── features/
│   ├── feature-1.md
│   └── ...
├── user-flows/
│   └── flow-1.md
└── technical/
    └── architecture.md
```
```

#### curated/product-types/service-products.md

```markdown
# Service Products

Best practices for productized services and consulting packages.

## Product Types

### Productized Services
- Define clear deliverables
- Set scope boundaries
- Standardize process
- Create pricing tiers

### Consulting Packages
- Define outcomes
- Structure engagements
- Create templates
- Document process

## Output Structure

```text
service-product/
├── offer.md            # Offer structure and pricing
├── deliverables/
│   ├── deliverable-1.md
│   └── ...
├── process.md          # Delivery process
└── templates/          # Service delivery templates
```
```

### 5. Create Daily Log Directory

Create empty directory: `daily/`

Add .gitkeep if needed for version control.

## Verification

After initialization, verify:

- [ ] `.pawbytes/prodig-suites/` exists
- [ ] `.pawbytes/prodig-suites/memory/paw-ps-sidecar/index.md` exists and has content
- [ ] `.pawbytes/prodig-suites/memory/paw-ps-sidecar/curated/` directory exists
- [ ] `.pawbytes/prodig-suites/memory/paw-ps-sidecar/daily/` directory exists
- [ ] `.pawbytes/prodig-suites/products/` directory exists
- [ ] `.pawbytes/prodig-suites/artifacts/` directory exists
- [ ] All product-type starter files created

## Post-Initialization

After setup:

1. Greet the user
2. Explain what was created
3. Offer to start a product

```markdown
Welcome to Prodig Suites! 🎉

I've set up your workspace. Here's what's ready:

📁 `.pawbytes/prodig-suites/`
  - `memory/` — Shared context across all sessions
  - `products/` — Your product workspaces
  - `artifacts/` — Generated outputs

Ready to create something? Tell me:
- What kind of product (course, template, SaaS, service)?
- What's your idea?
```