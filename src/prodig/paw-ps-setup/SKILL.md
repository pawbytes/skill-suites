---
name: paw-ps-setup
description: Sets up Prodig Suites module in a project. Use when the user requests to 'install prodig module', 'configure Prodig Suites', 'setup product creation suite', or 'paw-ps setup'.
---

# Prodig Suites Setup

## Overview

Installs and configures Prodig Suites into a project. Prodig Suites is a product creation system that guides users from vague idea to production-ready product, supporting four product families: Knowledge, Template, Software, and Service.

This setup skill scaffolds the complete workspace structure including:

- **`{project-root}/.pawbytes/prodig-suites/`** — Module root
- **`{project-root}/.pawbytes/prodig-suites/memory/paw-ps-sidecar/`** — Shared memory sidecar
- **`{project-root}/.pawbytes/prodig-suites/products/`** — Product workspaces
- **`{project-root}/.pawbytes/prodig-suites/artifacts/`** — Generated outputs

Configuration is written to the Pawbytes ecosystem config:

- **`{project-root}/.pawbytes/config/config.yaml`** — Shared project config with `ps:` section for module-specific values
- **`{project-root}/.pawbytes/config/config.user.yaml`** — Personal settings (user_name, communication_language)
- **`{project-root}/.pawbytes/config/module-help.csv`** — Registers module capabilities

`{project-root}` is a **literal token** in config values — never substitute it with an actual path. It signals to the consuming LLM that the value is relative to the project root.

## Principles

- **Sensible defaults**: Every setting has a reasonable default; users only override what matters to them
- **Idempotent setup**: Running setup multiple times preserves existing work and memory
- **Clear confirmation**: Show exactly what will change before writing files
- **Progressive disclosure**: Scaffold starter files with headings and brief instructions, not full content
- **Capability detection**: Verify optional research/reporting capabilities and note what's missing

**Module code note:** The module uses `ps` (2 letters) as its abbreviation for "Prodig Suites". This differs from the 3-letter convention (e.g., `mkt`, `cra`, `tools`) but is intentional for brevity and consistency across all skill names in this module.

## On Activation

1. Read `./assets/module.yaml` for module metadata and variable definitions (the `code` field `ps` is the module identifier)
2. Check if `{project-root}/.pawbytes/prodig-suites/` exists — if present, inform the user this is an update
3. Check for core Pawbytes config at `{project-root}/.pawbytes/config/config.yaml`

If the user provides arguments (e.g. `accept all defaults`, `--headless`, or inline values like `default mode is template, quality bar is publish-ready`), map any provided values to config keys, use defaults for the rest, and skip interactive prompting. Still display the full confirmation summary at the end.

## Collect Configuration

Ask the user for values. Show defaults in brackets. Present all values together so the user can respond once with only the values they want to change (e.g. "change quality bar to publish-ready, rest are fine"). Never tell the user to "press enter" or "leave blank" — in a chat interface they must type something to respond.

**Default priority** (highest wins): existing config values > `./assets/module.yaml` defaults.

**Core config** (only if no core keys exist yet): `user_name` (default: Pawbytes), `communication_language` and `document_output_language` (default: English — ask as a single language question, both keys get the same answer). Of these, `user_name` and `communication_language` are written exclusively to `config.user.yaml`.

**Module config**: Read each variable in `./assets/module.yaml` that has a `prompt` field. Ask using that prompt with its default value.

Load `./references/config-variables.md` for detailed descriptions of each configuration variable.

## Create Directory Structure

After collecting configuration, create the complete workspace structure:

```bash
# Main module directories
mkdir -p "{project-root}/.pawbytes/prodig-suites/memory/paw-ps-sidecar/curated/product-types"
mkdir -p "{project-root}/.pawbytes/prodig-suites/memory/paw-ps-sidecar/daily"
mkdir -p "{project-root}/.pawbytes/prodig-suites/products"
mkdir -p "{project-root}/.pawbytes/prodig-suites/artifacts"
```

## Create Sidecar Files

### 1. Create index.md (Orientation File)

Create `{project-root}/.pawbytes/prodig-suites/memory/paw-ps-sidecar/index.md`:

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
- "I want to productize my service for..."

## Recent Activity

*No activity yet — this will be populated as you work.*

## Curated Files Status

| File | Status | Description |
|------|--------|-------------|
| product-context.md | Pending | Active product definition |
| market-intelligence.md | Pending | Research synthesis |
| audience-intelligence.md | Pending | Customer insights |
| product-decisions.md | Pending | Decision history |
| output-standards.md | Ready | Quality criteria (has defaults) |

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

## Quick Reference

| Agent | Purpose |
|-------|---------|
| paw-ps-orchestrator | Main coordinator — start here |
| paw-ps-discovery | Idea exploration and validation |
| paw-ps-audience | Customer research and personas |
| paw-ps-research | Market and competitor research |
| paw-ps-strategist | Product packaging and positioning |

## Getting Started

Tell me what you want to create, and I'll help you through the full journey from idea to production-ready product.
```

### 2. Create Starter Curated Files

Create each curated file with headings and brief instructions:

#### product-context.md

```markdown
# Product Context

*No active product yet. This file will be populated when you start a product.*

## How to Use This File

This file captures the essential context for your active product:

- **Product Name** — Working title
- **Product Type** — Knowledge, Template, Software, or Service
- **Core Premise** — What it does and why
- **Target Audience** — Who it's for
- **Current Stage** — discovery, research, brief, execution

## Starting a Product

Tell the orchestrator:
- What product you want to create
- What type it might be (if you know)
- Who it's for (if you know)
```

#### market-intelligence.md

```markdown
# Market Intelligence

*Market research will be synthesized here.*

## Purpose

Captures competitive landscape, market positioning, and opportunity signals.

## Sections (populated by research)

- **Competitive Landscape** — Who else serves this market
- **Market Gaps** — Underserved needs and opportunities
- **Positioning Signals** — How to differentiate
- **Validation Points** — Evidence of demand
```

#### audience-intelligence.md

```markdown
# Audience Intelligence

*Customer insights will be synthesized here.*

## Purpose

Captures deep understanding of target customers and their needs.

## Sections (populated by research)

- **Primary Persona** — Core customer profile
- **Pain Points** — Problems they're trying to solve
- **Desired Outcomes** — What success looks like
- **Buying Triggers** — What motivates purchase
- **Language Patterns** — How they describe their problems
```

#### product-decisions.md

```markdown
# Product Decisions

*Key decisions will be logged here.*

## Purpose

Tracks important decisions made during product development with context for future reference.

## Decision Log Format

| Date | Decision | Rationale | Alternatives Considered |
|------|----------|-----------|------------------------|
| | | | |

## Why This Matters

- Provides context for future iterations
- Helps explain "why did we do X?"
- Prevents revisiting settled questions
```

#### output-standards.md

```markdown
# Output Standards

Quality criteria for Prodig Suites deliverables.

## Configured Quality Bar

**Current Setting:** {quality_bar from config}

### Quality Bar Definitions

| Level | Definition |
|-------|------------|
| draft | Complete structure with placeholder content |
| production-ready | Complete, no placeholders, usable by intended audience |
| publish-ready | Polished, formatted, ready for publication |
| sellable-ready | Complete, polished, ready to sell |

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

## Output Style

**Current Setting:** {output_style from config}

| Style | Description |
|-------|-------------|
| structured-practical | Clear sections, actionable, ready to use |
| narrative-engaging | Story-driven, conversational, engaging |
| technical-detailed | Comprehensive, thorough, documentation-heavy |
```

### 3. Create Product Type Files

Create `{project-root}/.pawbytes/prodig-suites/memory/paw-ps-sidecar/curated/product-types/`:

#### knowledge-products.md

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

```
knowledge-product/
├── curriculum.md        # Course outline or chapter structure
├── modules/
│   ├── module-1.md
│   └── ...
├── materials/           # Supporting materials
└── assets/              # Images, downloads, etc.
```

## Quality Checklist

- [ ] Learning objectives defined
- [ ] Logical progression verified
- [ ] Practice activities included
- [ ] All content complete (no placeholders)
```

#### template-products.md

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

```
template-product/
├── templates/
│   └── template-1.{ext}
├── guide.md            # Usage instructions
├── examples/           # Example outputs
└── assets/             # Supporting files
```

## Quality Checklist

- [ ] Templates are functional
- [ ] Instructions are clear
- [ ] Formatting is consistent
- [ ] Design is reusable
```

#### software-products.md

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

```
software-product/
├── prd-lite.md         # Product requirements
├── features/
│   └── feature-1.md
├── user-flows/
│   └── flow-1.md
└── technical/
    └── architecture.md
```

## Quality Checklist

- [ ] Value proposition clear
- [ ] MVP scope defined
- [ ] User flows documented
- [ ] Technical requirements stated
```

#### service-products.md

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

```
service-product/
├── offer.md            # Offer structure and pricing
├── deliverables/
│   └── deliverable-1.md
├── process.md          # Delivery process
└── templates/          # Service delivery templates
```

## Quality Checklist

- [ ] Deliverables are clear
- [ ] Scope is bounded
- [ ] Pricing is defined
- [ ] Process is documented
```

## Verify Capabilities

Check for optional capabilities that enhance Prodig Suites:

### Research Capabilities

- [ ] Web search tool available (WebSearch, mcp__exa__web_search_exa)
- [ ] Code graph context available (mcp__CodeGraphContext__*)

### Reporting Capabilities

- [ ] Presentation generation available (paw-tools-presentation)
- [ ] Release tools available (paw-tools-release)

Note any missing capabilities in the confirmation message. These are optional but enhance the suite's power.

## Write Config

Write configuration to the Pawbytes ecosystem config:

1. **Core config** (if not present) → `{project-root}/.pawbytes/config/config.yaml`
2. **User settings** → `{project-root}/.pawbytes/config/config.user.yaml`
3. **Module help** → `{project-root}/.pawbytes/config/module-help.csv` (append if exists, create if not)

## Confirm

Display a comprehensive summary:

```
## Setup Complete

### Configuration
- Default product mode: {value}
- Quality bar: {value}
- Output style: {value}
- Research depth: {value}

### Created Directories
- .pawbytes/prodig-suites/memory/paw-ps-sidecar/
- .pawbytes/prodig-suites/products/
- .pawbytes/prodig-suites/artifacts/

### Created Files
- index.md — Orientation file
- product-context.md — Active product context
- market-intelligence.md — Market research synthesis
- audience-intelligence.md — Customer insights
- product-decisions.md — Decision log
- output-standards.md — Quality criteria
- product-types/*.md — Product family guides

### Capability Status
{List available/missing optional capabilities}

### What's Next
Start with `paw-ps-orchestrator` to create your first product.
```

Then display the `module_greeting` from `./assets/module.yaml`.

## Outcome

Once the user's `user_name` and `communication_language` are known (from collected input, arguments, or existing config), use them consistently for the remainder of the session: address the user by their configured name and communicate in their configured language.

## Output Contract

Once setup completes, the following are guaranteed:

- **Action type**: Module installation/configuration
- **Files created**:
  - `{project-root}/.pawbytes/prodig-suites/` directory structure
  - `{project-root}/.pawbytes/prodig-suites/memory/paw-ps-sidecar/index.md`
  - `{project-root}/.pawbytes/prodig-suites/memory/paw-ps-sidecar/curated/*.md`
  - `{project-root}/.pawbytes/prodig-suites/memory/paw-ps-sidecar/curated/product-types/*.md`
  - `{project-root}/.pawbytes/config/config.user.yaml` (if core config collected)
- **Recommendations**: Suggest running `paw-ps-orchestrator` to start first product
- **File saved to**: `{project-root}/.pawbytes/prodig-suites/`