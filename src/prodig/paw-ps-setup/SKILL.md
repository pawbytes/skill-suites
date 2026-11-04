---
name: paw-ps-setup
description: Sets up Prodig Suites module in a project. Use when the user requests to 'install prodig module', 'configure Prodig Suites', 'setup product creation suite', or 'paw-ps setup'.
---

# Prodig Suites Setup

## Overview

Installs and configures Prodig Suites into a project. Prodig Suites is a product creation system that guides users from vague idea to production-ready product, supporting four product families: Knowledge, Template, Software, and Service.

This setup skill scaffolds the complete workspace structure including:

- **`{suite-root}/`** — Suite root, normally `{project-root}/paw-suites/products/`; one folder per product, created by the other skills
- **`{suite-root}/_memory/`** — Shared memory (index, daily logs, curated files)
- **`{suite-root}/_standards/output-standards.md`** — Quality criteria
- **`{suite-root}/README.md`** — Generated product index

Configuration is written to the Pawbytes ecosystem config:

- **`{project-root}/.pawbytes/config/config.yaml`** — Shared project config with `ps:` section for module-specific values
- **`{project-root}/.pawbytes/config/config.user.yaml`** — Personal settings (user_name, communication_language)
- **`{project-root}/.pawbytes/config/module-help.csv`** — Registers module capabilities

`{project-root}` is a **literal token** in config values — never substitute it with an actual path. It signals to the consuming LLM that the value is relative to the project root.

## Resolution rules

- `{skill-root}` is this skill's folder. Run its scripts as `uv run {skill-root}/scripts/<name>.py`.
- `{suite-root}` is `root` from `uv run {skill-root}/scripts/paw-paths.py detect`, normally `{project-root}/paw-suites/products`. A custom folder in config `ps.products_folder` (or `ps.memory_folder` for `_memory/`) wins (`detect` lists it under `overrides`; an old default is not one).
- Older releases kept everything in `{project-root}/.pawbytes/prodig-suites/` (products, plans, artifacts and a memory folder). Setup moves it; see Migrate Legacy Files.

## Principles

- **Sensible defaults**: Every setting has a reasonable default; users only override what matters to them
- **Idempotent setup**: Running setup multiple times preserves existing work and memory
- **Clear confirmation**: Show exactly what will change before writing files
- **Progressive disclosure**: Scaffold starter files with headings and brief instructions, not full content
- **Capability detection**: Verify optional research/reporting capabilities and note what's missing

## On Activation

1. Read `{skill-root}/assets/module.yaml` for module metadata and variable definitions (the `code` field `ps` is the module identifier)
2. Run `uv run {skill-root}/scripts/paw-paths.py detect`. `mode: new` means an update; `legacy` or `both` means files from an older release wait to be migrated (after the config is written); `fresh` is a first install
3. Check for core Pawbytes config at `{project-root}/.pawbytes/config/config.yaml`

If the user provides arguments (e.g. `accept all defaults`, `--headless`, or inline values like `default mode is template, quality bar is publish-ready`), map any provided values to config keys, use defaults for the rest, and skip interactive prompting. Still display the full confirmation summary at the end.

## Collect Configuration

Ask the user for values. Show defaults in brackets. Present all values together so the user can respond once with only the values they want to change (e.g. "change quality bar to publish-ready, rest are fine"). Never tell the user to "press enter" or "leave blank" — in a chat interface they must type something to respond.

**Default priority** (highest wins): existing config values > `{skill-root}/assets/module.yaml` defaults.

**Core config** (only if no core keys exist yet): `user_name` (default: Pawbytes), `communication_language` and `document_output_language` (default: English — ask as a single language question, both keys get the same answer). Of these, `user_name` and `communication_language` are written exclusively to `config.user.yaml`.

**Module config**: Read each variable in `{skill-root}/assets/module.yaml` that has a `prompt` field. Ask using that prompt with its default value.

Load `./references/config-variables.md` for detailed descriptions of each configuration variable.

## Create Directory Structure

After collecting configuration, create the complete workspace structure. When `detect` reported `legacy` or `both`, do Write Files and Migrate Legacy Files first, then come back here and create only what is still missing, so the scaffolding never collides with the files being moved.

> **Note:** `{project-root}` is a literal token that resolves to the project root directory at runtime. Do not substitute it with an actual path.

```bash
# Main module directories
mkdir -p "{suite-root}/_memory/curated/product-types"
mkdir -p "{suite-root}/_memory/daily"
mkdir -p "{suite-root}/_standards"
```

## Create Memory Files

### 1. Create index.md (Orientation File)

Create `{suite-root}/_memory/index.md`:

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

| Skill | Purpose |
|-------|---------|
| paw-ps-agent-product-builder | Main coordinator — start here |
| paw-ps-discovery | Idea exploration and validation |
| paw-ps-research | Market and competitor research |
| paw-ps-audience | Customer research and personas |
| paw-ps-research-to-brief | Convert research into product brief |
| paw-ps-strategist | Product packaging and positioning |
| paw-ps-concept-to-product-plan | Transform brief into executor-ready plan |
| paw-ps-knowledge-executor | Build courses, ebooks, guides |
| paw-ps-template-executor | Build templates, prompt packs, kits |
| paw-ps-software-executor | Build SaaS, apps, AI tools |
| paw-ps-service-executor | Build productized services |
| paw-ps-product-package-assembler | Bundle into deliverable package |
| paw-ps-publish-ready-check | Evaluate production readiness |

## Getting Started

Tell me what you want to create, and I'll help you through the full journey from idea to production-ready product.
```

### 2. Create Starter Curated Files

Create each curated file in `{suite-root}/_memory/curated/` with headings and brief instructions (`output-standards.md` goes to `{suite-root}/_standards/` instead):

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

#### output-standards.md (in `{suite-root}/_standards/`)

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

Create `{suite-root}/_memory/curated/product-types/`:

#### knowledge-products.md

````markdown
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
│   └── ...
├── materials/           # Supporting materials
└── assets/              # Images, downloads, etc.
```

## Quality Checklist

- [ ] Learning objectives defined
- [ ] Logical progression verified
- [ ] Practice activities included
- [ ] All content complete (no placeholders)
````

#### template-products.md

````markdown
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
````

#### software-products.md

````markdown
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
````

#### service-products.md

````markdown
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
│   └── deliverable-1.md
├── process.md          # Delivery process
└── templates/          # Service delivery templates
```

## Quality Checklist

- [ ] Deliverables are clear
- [ ] Scope is bounded
- [ ] Pricing is defined
- [ ] Process is documented
````

## Verify Capabilities

Check for optional capabilities that enhance Prodig Suites:

### Research Capabilities

- [ ] Web search tool available (WebSearch, mcp__exa__web_search_exa)
- [ ] Code graph context available (mcp__CodeGraphContext__*)

### Reporting Capabilities

- [ ] Presentation generation available (paw-tools-presentation)
- [ ] Release tools available (paw-tools-release)

Note any missing capabilities in the confirmation message. These are optional but enhance the suite's power.

## Write Files

Write a temp JSON file with the collected answers structured as `{"core": {...}, "module": {...}}` (omit `core` if it already exists). Then run both scripts:

```bash
uv run {skill-root}/scripts/merge-config.py \
  --config-path "{project-root}/.pawbytes/config/config.yaml" \
  --user-config-path "{project-root}/.pawbytes/config/config.user.yaml" \
  --module-yaml {skill-root}/assets/module.yaml \
  --answers {temp-file}

uv run {skill-root}/scripts/merge-help-csv.py \
  --target "{project-root}/.pawbytes/config/module-help.csv" \
  --source {skill-root}/assets/module-help.csv \
  --module-code ps
```

Both scripts output JSON to stdout with results. If either exits non-zero, surface the error and stop.

Run either script with `--help` for full usage.

## Migrate Legacy Files

After the config is written, when `detect` reported `legacy` or `both`: run `uv run {skill-root}/scripts/paw-paths.py --project-root "{project-root}" plan`, show its `summary` along with any conflicts, and run `paw-paths.py apply` once the user confirms. Each product's files, plan and executor artifacts land in one folder (`{product-slug}/`, `{product-slug}/plan/`, `{product-slug}/build/`); the old memory folder becomes `_memory/`; output standards move to `_standards/`. Report what moved and what stayed (`MOVED.md` in the old folder lists it).

Then, in every install mode, run `uv run {skill-root}/scripts/paw-paths.py index` to write `{suite-root}/README.md`.

## Confirm

Use the script JSON output to display what was written — config values set, user settings written to `config.user.yaml` (`user_keys` in result), help entries added, fresh install vs update. Then display the `module_greeting` from `{skill-root}/assets/module.yaml` to the user.

Display a comprehensive summary:

```markdown
## Setup Complete

### Configuration
- Default product mode: {value}
- Quality bar: {value}
- Output style: {value}
- Research depth: {value}

### Created Directories
- paw-suites/products/_memory/
- paw-suites/products/_standards/

### Migration
{What moved from .pawbytes/prodig-suites/ and what stayed, or "nothing to migrate"}

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
Start with `paw-ps-agent-product-builder` to create your first product.
```

Then display the `module_greeting` from `{skill-root}/assets/module.yaml`.

## Outcome

Once the user's `user_name` and `communication_language` are known (from collected input, arguments, or existing config), use them consistently for the remainder of the session: address the user by their configured name and communicate in their configured language.

## Output Contract

Once setup completes, the following are guaranteed:

- **Action type**: Module installation/configuration
- **Files created**:
  - `{suite-root}/` directory structure and `{suite-root}/README.md`
  - `{suite-root}/_memory/index.md`
  - `{suite-root}/_memory/curated/*.md`
  - `{suite-root}/_standards/output-standards.md`
  - `{suite-root}/_memory/curated/product-types/*.md`
  - `{project-root}/.pawbytes/config/config.user.yaml` (if core config collected)
- **Recommendations**: Suggest running `paw-ps-agent-product-builder` to start first product
- **File saved to**: `{suite-root}/`