# Skill Folder Structure

## Overview

Every skill resides in its own directory following a consistent structure. This document defines what goes in a skill folder and the purpose of each component.

## Required Files

| File | Required | Purpose |
|------|----------|---------|
| `SKILL.md` | Yes | Main skill definition |
| `references/frameworks-index.csv` | For frameworks | Progressive disclosure index |
| `references/frameworks/*.md` | For frameworks | Domain-specific methodologies |
| `assets/module.yaml` | Setup only | Module configuration schema |

## Directory Layout

```
skill-name/
├── SKILL.md                    # Required: Main definition
│
├── references/                 # Optional: Knowledge files
│   ├── capability-*.md         # Capability documentation
│   ├── shared-patterns.md      # Shared patterns (loaded directly)
│   ├── best-practices.md       # Best practices (loaded directly)
│   ├── frameworks-index.csv    # Framework index (for progressive disclosure)
│   └── frameworks/             # Framework files
│       ├── framework-1.md
│       └── framework-2.md
│
├── assets/                     # Optional: Static files
│   ├── module.yaml             # Setup skills only: configuration schema
│   ├── module-help.csv         # Setup skills: CLI help entries
│   └── scripts/                # Executable scripts
│       └── tool-discovery.sh
│
└── evals/                      # Optional: Test cases
    └── test-cases.md
```

## Directory Purposes

### `references/`

Knowledge files loaded during skill execution. Contains:

| File Type | Loading Pattern | Purpose |
|-----------|-----------------|---------|
| `capability-*.md` | Direct load when capability matched | Specific capability implementation |
| `shared-patterns.md` | Direct load on activation | Common patterns used across capabilities |
| `best-practices.md` | Direct load on activation | Quality guidelines |
| `frameworks-index.csv` | Always read first | Index for progressive disclosure |
| `frameworks/*.md` | Selective load via index | Domain methodologies |

**Key distinction:** Capability files are loaded when a specific capability is matched. Framework files use progressive disclosure via the CSV index.

### `assets/`

Static resources that support skill execution:

| File Type | Purpose |
|-----------|---------|
| `module.yaml` | Configuration schema for setup skills |
| `module-help.csv` | CLI help text entries |
| `scripts/` | Executable shell scripts |
| `templates/` | Reusable templates (presentations, etc.) |

### `evals/`

Test definitions for quality assurance:

```markdown
# Test Cases

## Case 1: Basic Activation
**Input:** User says "help with SEO"
**Expected:** Load SEO capability, show available options

## Case 2: Brand Context
**Input:** User has active brand, requests SEO audit
**Expected:** Read brand context before generating recommendations
```

## Real-World Examples

### Specialist Skill Structure

```
paw-mkt-seo/
├── SKILL.md
└── references/
    ├── capability-technical-seo.md
    ├── capability-content-seo.md
    ├── capability-local-seo.md
    ├── capability-link-building.md
    ├── capability-geo.md
    ├── capability-deliverables.md
    ├── capability-best-practices.md
    ├── capability-workflow.md
    ├── capability-research.md
    ├── shared-patterns.md
    ├── frameworks-index.csv
    └── frameworks/
        ├── technical-audit.md
        ├── schema-markup.md
        ├── core-web-vitals.md
        └── ... (18 more)
```

### Agent Skill Structure

```
paw-cra-agent-creative-director/
├── SKILL.md
└── references/
    ├── tool-discovery.md
    ├── brand-onboarding.md
    ├── brand-update.md
    ├── brief-analysis.md
    ├── campaign-planning.md
    ├── agent-routing.md
    ├── fast-path.md
    ├── save-memory.md
    ├── memory-system.md
    ├── init.md
    └── autonomous-wake.md
```

### Setup Skill Structure

```
paw-mkt-setup/
├── SKILL.md
└── assets/
    ├── module.yaml
    ├── module-help.csv
    └── scripts/
        ├── tool-discovery.sh
        ├── tool-discovery.bat
        ├── chrome-profiles.sh
        └── chrome-profiles.bat
```

## File Naming Conventions

| File Type | Convention | Example |
|-----------|------------|---------|
| SKILL.md | Always `SKILL.md` | `SKILL.md` |
| Capability files | `capability-{name}.md` | `capability-technical-seo.md` |
| Framework files | `kebab-case.md` | `technical-audit.md` |
| Other references | `kebab-case.md` | `shared-patterns.md` |
| CSV files | `kebab-case.csv` | `frameworks-index.csv` |
| YAML files | `kebab-case.yaml` | `module.yaml` |

## What NOT to Include

- Generated outputs (those go to `.pawbytes/`)
- Temporary files
- IDE-specific configurations
- Secrets or API keys (use `config.user.yaml`)