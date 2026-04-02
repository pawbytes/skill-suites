# Contributing to Pawbytes Skill Suites

## Overview

This guide helps contributors understand how to build, structure, and name skills in the Pawbytes Skill Suites monorepo. Skills are the building blocks of the system — each one provides a focused capability that can be invoked independently or as part of a larger workflow.

## Who This Guide Is For

| Audience | What You'll Learn |
|----------|-------------------|
| **New contributors** | How skills are structured and named |
| **Module builders** | Patterns for different skill types |
| **Integrators** | How skills fit together in workflows |

## Documentation in This Section

| Document | Purpose |
|----------|---------|
| [Skill Types](./skill-types.md) | Agent vs Workflow vs Utility — when to use each |
| [Naming Conventions](./naming-conventions.md) | File, folder, and skill naming rules |
| [Conventions](./conventions.md) | Patterns, best practices, and standards |
| [Documentation Quality Improvement Plan](./documentation-quality-improvement-plan.md) | Reusable phased plan for improving published docs |

## Quick Start

### 1. Understand Skill Types

Skills fall into three categories:

- **Agent Skills** — Persistent personas with memory (e.g., `paw-mkt-agency`, `paw-cra-agent-creative-director`)
- **Workflow Skills** — Deterministic pipelines with defined steps (e.g., `paw-mkt-sostac`, `paw-cra-design-social`)
- **Utility Skills** — Single-purpose tools with minimal interaction (e.g., `paw-tools-release`, `paw-tools-presentation`)

See [Skill Types](./skill-types.md) for detailed comparisons.

### 2. Follow Naming Conventions

Skill names follow the pattern: `{org}-{module}-{skillname}`

| Part | Format | Examples |
|------|--------|----------|
| org | 3 letters | `paw` |
| module | 3 letters | `mkt`, `cra`, `tools` |
| skillname | kebab-case | `seo`, `agent-designer`, `release` |

See [Naming Conventions](./naming-conventions.md) for complete rules.

### 3. Follow Core Conventions

Every skill should:

1. Have a `SKILL.md` with YAML frontmatter (`name` and `description`)
2. Include trigger phrases in the description
3. Define output paths using variables
4. Use progressive disclosure for frameworks

See [Conventions](./conventions.md) for patterns and best practices.

## Module Organization

```
src/
├── marketing/    # paw-mkt-* skills (23 skills)
├── creative/     # paw-cra-* skills (15 skills)
└── tools/        # paw-tools-* skills (3 skills)
```

Each module has:

- A **setup skill** (`paw-{module}-setup`) for configuration
- **Agent skills** with `agent-` prefix for persistent personas
- **Workflow skills** for deterministic pipelines
- **Utility skills** for focused tools

## Skill Folder Structure

```
skill-name/
├── SKILL.md                    # Required: Main definition
│
├── references/                 # Optional: Knowledge files
│   ├── capability-*.md         # Capability documentation
│   ├── frameworks-index.csv    # Framework index
│   └── frameworks/             # Framework files
│       └── *.md
│
├── assets/                     # Optional: Static files
│   ├── module.yaml             # Setup skills only
│   └── scripts/                # Executable scripts
│
└── evals/                      # Optional: Test cases
    └── *.json
```

## Key Concepts

### Progressive Disclosure

Skills with extensive domain knowledge use progressive disclosure to keep context lean:

1. Read `frameworks-index.csv` first (~10-30 rows)
2. Match user situation to `best_for` column
3. Load ONLY matched framework files
4. Never bulk-read all framework files

### Coordinator Pattern

Marketing and Creative modules use a central coordinator that routes to specialists:

```
User Request
     │
     ▼
┌─────────────────┐
│   Coordinator   │  paw-mkt-agency, paw-cra-agent-creative-director
└────────┬────────┘
         │
         ├── Load brand context
         ├── Analyze request type
         └── Route to specialist
                │
                ▼
         ┌─────────────┐
         │  Specialist │  paw-mkt-seo, paw-cra-agent-designer
         └─────────────┘
```

### Production-First Routing

In the Creative module, route directly to production agents when the user requests a deliverable:

- **Images/graphics** → Designer (directly)
- **Videos** → Video Producer (directly)
- **Research/copy** → Strategist (on demand only)

Do NOT require Strategist validation before production.

## Getting Help

- Check existing skills in `src/marketing/` and `src/creative/` for examples
- Read the SKILL.md files to understand patterns
- Review the conventions document for specific patterns

## Next Steps

1. Read [Skill Types](./skill-types.md) to understand the three categories
2. Review [Naming Conventions](./naming-conventions.md) before creating new skills
3. Follow [Conventions](./conventions.md) for consistent skill development