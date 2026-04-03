# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Repository Structure

```
src/
├── marketing/   # paw-mkt-* skills (23 skills)
├── creative/    # paw-cra-* skills (15 skills)
└── tools/       # paw-tools-* skills (3 skills)
_bmad/
├── bmb/         # BMad builder tools (agent/workflow/module builders)
└── core/        # BMad core skills
```

Skills are installed via `npx skills add pawbytes/skill-suites` — see `.claude-plugin/marketplace.json` for the category manifest.

---

## Naming Conventions

### Skill Names

Format: `{org}-{module}-{skillname}`

| Part | Format | Examples |
|------|--------|----------|
| org | 3 lowercase letters | `paw` |
| module | 3 lowercase letters | `mkt`, `cra`, `tools` |
| skillname | kebab-case | `seo`, `agent-designer`, `video-shortform` |

**Agent skills** include `agent-` prefix: `paw-{module}-agent-{name}`

| Correct | Incorrect |
|---------|-----------|
| `paw-cra-agent-designer` | `paw-cra-designer-agent` |
| `paw-mkt-agency` | `paw-mkt-coordinator` (special case) |

**Workflow skills** use descriptive names without prefix.

**Utility skills** use descriptive names: `paw-tools-release`, `paw-tools-presentation`

### Folder Names

Match skill name exactly:

| Correct | Incorrect |
|---------|-----------|
| `src/marketing/paw-mkt-seo/` | `src/marketing/seo/` |
| `src/creative/paw-cra-agent-designer/` | `src/creative/agent-designer/` |

### File Names

| Item | Convention | Example |
|------|------------|---------|
| SKILL.md | Exact uppercase | `SKILL.md` |
| Reference files | kebab-case | `technical-audit.md` |
| Numbered refs | `01-name.md` | `01-validate.md` |
| CSV files | kebab-case | `frameworks-index.csv` |
| Python scripts | snake_case | `parse_commits.py` |

---

## Skill Types

| Characteristic | Agent | Workflow | Utility |
|----------------|-------|----------|---------|
| Has persona/identity | Yes | No | No |
| Uses memory | Yes | No | No |
| Interaction level | High | Medium | Low |
| Headless mode | Limited | Full support | Full support |
| Primary output | Coordination, routing | Deliverables | Artifacts |

### When to Use Each

| Your Need | Skill Type |
|-----------|------------|
| Persistent persona with memory | Agent |
| Coordination of multiple skills | Agent (Coordinator) |
| Multi-turn conversations | Agent |
| Judgment-based decisions | Agent |
| Sequential pipeline with stages | Workflow |
| Clear input → output process | Workflow |
| Repeatable process with gates | Workflow |
| Single focused task | Utility |
| CI/CD integration | Utility |

---

## Skill Folder Structure

```
skill-name/
├── SKILL.md                    # Required: Main definition with YAML frontmatter
├── references/                 # Knowledge files loaded during execution
│   ├── frameworks-index.csv    # Lightweight index for progressive disclosure
│   ├── capability-*.md         # Capability documentation
│   └── frameworks/             # Full framework files (loaded on match only)
├── assets/                     # Static files (scripts, templates, module.yaml)
└── evals/                      # Test cases
```

---

## SKILL.md Conventions

### Required Elements

```yaml
---
name: paw-{module}-{skillname}
description: "Main description. Triggers: 'phrase 1', 'phrase 2', 'phrase 3'."
---

# Skill Name

## Overview
Brief description of what the skill does.

**Args:** Accepts `--headless` / `-H` for non-interactive execution.

**Output:** Description of deliverables and location.
```

### Section Order

1. **Overview** — What the skill does
2. **Identity** — For agent skills only (name, role, personality)
3. **Communication Style** — For agent skills only
4. **Principles** — Core behavioral guidelines
5. **On Activation** — Initialization steps (load config, memory, brand context)
6. **Capabilities** — Table mapping capabilities to reference files
7. **Response Protocol** — Step-by-step workflow
8. **Path Resolution** — Output paths using variables
9. **Reference Lookup Protocol** — Framework loading strategy
10. **Escalation Routes** — When to route to other skills (table format)
11. **Output Contract** — What deliverables include

### Agent Skill Identity Section

```markdown
## Identity
I am [persona description].

## Communication Style
- Style characteristic 1
- Style characteristic 2

## On Activation
Load shared memory from `{project-root}/.pawbytes/{module}/index.md`.
Load brand guidelines from `.pawbytes/{module}/brands/{active-brand}/guidelines.md`.
```

### Workflow Skill Structure

```markdown
## Pipeline

### Stage 1: Stage Name
Load `./references/01-stage-name.md`

**Progression:** Condition for moving to next stage.

### Stage 2: Stage Name
Load `./references/02-stage-name.md`

**Progression:** Condition for completion.
```

---

## Progressive Disclosure Pattern

Skills with domain knowledge must use this pattern to keep context lean:

```markdown
## Reference Lookup Protocol

1. Read `./references/frameworks-index.csv` — lightweight index (~10-30 rows)
2. Match user situation to `best_for` column
3. Read ONLY matched framework file(s) from `./references/frameworks/`
4. Never bulk-read all framework files
```

### frameworks-index.csv Format

```csv
id,name,description,best_for,file,tags
technical-audit,Technical Audit,Crawlability issues,Site audits,frameworks/technical-audit.md,"audit,technical"
schema-markup,Schema Markup,JSON-LD examples,Structured data,frameworks/schema-markup.md,"schema"
```

**Required columns:** `id`, `name`, `description`, `best_for`, `file`, `tags`

---

## Module System

### Module Structure

```
src/{module}/
├── paw-{module}-setup/              # Setup skill (required)
│   ├── SKILL.md
│   └── assets/
│       └── module.yaml              # Configuration schema
├── paw-{module}-{coordinator}/      # Coordinator skill
└── paw-{module}-{specialist-n}/     # Specialist skills
```

### Module Registration

In `.claude-plugin/marketplace.json`:

```json
{
  "name": "marketing-suites",
  "description": "...",
  "skills": [
    "./src/marketing/paw-mkt-setup",
    "./src/marketing/paw-mkt-agency",
    // ... more skills
  ]
}
```

### Configuration Hierarchy

Three-level resolution (later overrides earlier):

1. **Module defaults** → `module.yaml` (in setup skill)
2. **Project config** → `.pawbytes/config/config.yaml`
3. **User overrides** → `.pawbytes/config/config.user.yaml`

### Path Variables

| Variable | Resolves To |
|----------|-------------|
| `{project-root}` | Project root directory |
| `{user_name}` | User's name from config |
| `{output_folder}` | Output directory path |
| `{communication_language}` | Response language |
| `{brand-slug}` | Brand identifier |
| `{campaign-slug}` | Campaign identifier |

---

## Output Paths

### Standard Structure

```
.pawbytes/{module}/{type}/{slug}/
```

| Module | Output Directory |
|--------|------------------|
| Marketing | `.pawbytes/marketing-suites/` |
| Creative | `.pawbytes/creative-suites/` |
| Tools | `.pawbytes/tools-output/` |

### Brand Workspace

```
.pawbytes/{module}/brands/{brand-slug}/
├── brand-context.md
├── guidelines.md
├── status.md
├── campaigns/
└── channels/
```

### Path Resolution in SKILL.md

```markdown
## Path Resolution

**Brand workspace root**: `{project-root}/.pawbytes/marketing-suites/brands/{brand-slug}/`

**Campaign coordination**: `{project-root}/.pawbytes/marketing-suites/brands/{brand-slug}/campaigns/{type}-{campaign-slug}/`

If no brand slug is known, prompt for brand selection first.
```

---

## Key Architectural Patterns

### Coordinator Pattern

Central coordinator routes to specialists:

```markdown
## Escalation Routes

| Signal | Routes To |
|--------|-----------|
| SEO, keywords, technical audit | paw-mkt-seo |
| Content, blog, editorial | paw-mkt-content |
| Paid ads, PPC, retargeting | paw-mkt-paid-ads |
```

### Production-First Routing (Creative Module)

When a user requests a deliverable, route directly to production agents:

- **Images/graphics** → Designer (directly)
- **Videos** → Video Producer (directly)
- **Research/copy** → Strategist (on-demand only, NOT a required gate)

### Output Contract

```markdown
## Output Contract

Every deliverable includes:
- **Action type**: what was done
- **Files saved**: where artifacts were written
- **Recommendations**: what to do next
- **File saved to**: resolved path
```

---

## Release Workflow

Create releases using the release skill:

```
/paw-tools-release
```

Options:
- Headless: `/paw-tools-release --headless`
- Specific version: `/paw-tools-release --version 1.2.0`

The skill handles version bumping, changelog generation, git tagging, and GitHub release creation. It detects version files automatically and infers version bump from conventional commits.

---

## Quality Checklist

Before submitting a skill:

- [ ] SKILL.md has YAML frontmatter with `name` and `description`
- [ ] Description includes trigger phrases (`Triggers:` or `Use when:`)
- [ ] Overview section present
- [ ] Path resolution defined (if skill produces output)
- [ ] Reference lookup protocol defined (if using frameworks)
- [ ] Escalation routes defined (if skill routes to others)
- [ ] Headless mode documented (if supported)
- [ ] Output contract defined (if skill produces deliverables)
- [ ] Identity section present (for agent skills only)
- [ ] Principles section present
- [ ] File and folder names follow naming conventions

---

## Documentation

- `docs/technical/contributing/` — Skill types, naming conventions, patterns
- `docs/technical/architecture/` — Module system, routing patterns, skill lifecycle
- `README.md` — Full skill catalog and installation instructions