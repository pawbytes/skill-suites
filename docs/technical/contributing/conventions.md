# Skill Conventions

This document defines patterns, best practices, and standards for building consistent, maintainable skills in Pawbytes Skill Suites.

---

## SKILL.md Conventions

### Required Elements

Every SKILL.md must include:

| Element | Purpose |
|---------|---------|
| YAML frontmatter | Metadata for skill discovery |
| `name` field | Exact skill name |
| `description` field | Purpose with trigger phrases |
| Overview section | Brief description of capabilities |

### Frontmatter Format

```yaml
---
name: paw-{module}-{skillname}
description: "Main description. Triggers: 'phrase 1', 'phrase 2', 'phrase 3'."
---
```

**Guidelines:**

- Use double quotes for the description value
- Include 3-5 trigger phrases
- Start with a concise summary (under 100 characters)
- Use `Triggers:` or `Use when:` to introduce trigger phrases

### Section Ordering

Follow this order for consistency:

1. **Overview** — What the skill does
2. **Identity** — For agent skills only
3. **Communication Style** — For agent skills only
4. **Principles** — Core behavioral guidelines
5. **On Activation** — Initialization steps
6. **Capabilities** — Table of capabilities and routes
7. **Response Protocol** — Step-by-step workflow
8. **Path Resolution** — Output paths
9. **Reference Lookup Protocol** — Framework loading
10. **Escalation Routes** — When to route to other skills
11. **Output Contract** — What deliverables include

### Standard Sections

#### Overview

```markdown
## Overview

Brief description of what the skill does and who should use it.

**Args:** Accepts `--headless` / `-H` for non-interactive execution.

**Output:** Description of deliverables and location.
```

#### Principles

```markdown
## Principles

- **Principle 1**: Description of behavior
- **Principle 2**: Description of behavior
- **Principle 3**: Description of behavior
```

#### On Activation

```markdown
## On Activation

Load available config from `{project-root}/.pawbytes/config/config.yaml` and `{project-root}/.pawbytes/config/config.user.yaml` if present. Resolve and apply throughout the session (defaults in parens):

- `{variable}` (default) — description
- `{variable}` (default) — description

Greet the user and offer to show available capabilities.
```

#### Capabilities Table

```markdown
## Capabilities

| Capability | Route |
|------------|-------|
| Capability Name | Load `./references/capability-name.md` |
| Capability Name | Load `./references/frameworks-index.csv` then matched framework |
```

#### Path Resolution

```markdown
## Path Resolution

- Brand context: `{project-root}/.pawbytes/{module}/brands/{brand-slug}/`
- Campaigns: `{project-root}/.pawbytes/{module}/brands/{brand-slug}/campaigns/{campaign-slug}/`
- Reports: `{project-root}/.pawbytes/{module}/reports/`
```

---

## Reference File Conventions

### Structure

Reference files should follow this structure:

```markdown
# Reference Title

## When to Use
Specific scenarios where this reference applies.

## Process
Step-by-step methodology.

## Checklist
- [ ] Item 1
- [ ] Item 2

## Examples
Concrete examples.

## Output
What this reference produces.
```

### Guidelines

| Guideline | Reason |
|-----------|--------|
| One topic per file | Focused loading |
| Use clear H2 headings | Easy navigation |
| Include examples | Concrete understanding |
| Define output | Clear expectations |
| Keep under 300 lines | Manageable context |

### Capability References

Capability references define specific skill functions:

```markdown
# Capability: Technical SEO

## Purpose
Delivers actionable technical SEO recommendations.

## Input Requirements
- Website URL or codebase access
- Brand context (if available)

## Process
1. Crawlability check
2. Indexation analysis
3. Core Web Vitals assessment
4. Schema validation

## Output Format
- Priority ratings (P1/P2/P3)
- Specific implementation steps
- Expected impact

## Examples
[Concrete examples]
```

---

## Framework Conventions

### Framework Index

Skills with domain-specific knowledge use `frameworks-index.csv`:

```csv
id,name,description,best_for,file,tags
technical-audit,Technical Audit,Crawlability and indexation,Site audits,frameworks/technical-audit.md,"audit,technical"
content-strategy,Content Strategy,Content planning,Editorial calendars,frameworks/content-strategy.md,"content,planning"
```

**Required columns:**

| Column | Purpose |
|--------|---------|
| `id` | Unique identifier |
| `name` | Display name |
| `description` | Brief description |
| `best_for` | When to use this framework |
| `file` | Path to framework file |
| `tags` | Comma-separated search terms |

### Framework Files

```markdown
# Framework Name

## When to Use
Specific scenarios where this framework applies.

## Prerequisites
What must be in place before using.

## Process
1. Step one
2. Step two
3. Step three

## Checklist
- [ ] Item 1
- [ ] Item 2

## Examples
Concrete examples with outcomes.

## Output
What this framework produces.
```

### Progressive Loading Pattern

Skills should use progressive disclosure:

```markdown
## Reference Lookup Protocol

This skill uses progressive disclosure:

1. Read `./references/frameworks-index.csv` — lightweight index (~10-30 rows)
2. Match user situation to `best_for` column
3. Read ONLY matched framework file(s) from `./references/frameworks/`
4. Never bulk-read all framework files
```

**Guidelines:**

- Keep index rows between 10-50
- Use specific, descriptive `best_for` values
- Tag with relevant keywords
- Never load all frameworks at once

---

## Published Documentation Conventions

Published docs under `docs/` must follow the contributor-facing standard defined in [Documentation Quality Improvement Plan](./documentation-quality-improvement-plan.md).

### Source-of-Truth Rule

- `src/**/SKILL.md` is canonical for skill names, behavior, routing, arguments, and output paths
- `docs/**` is the explanation layer for users and contributors
- Published docs may simplify source behavior, but they must never contradict it

### Canonical Published Doc Types

Use these standard structures when writing or updating docs under `docs/`.

#### Module README

1. Overview
2. Who this module is for
3. Quick navigation
4. Skill inventory
5. Common workflows
6. Output or artifact model
7. Start here
8. Related technical docs

#### Skill Page

1. Overview
2. When to use it
3. What you need to provide
4. What it does
5. What you get
6. Output location
7. Workflow overview
8. Arguments or modes
9. Related skills
10. Example prompts

#### Workflow Page

1. Goal
2. Prerequisites
3. Workflow overview
4. Step-by-step process
5. Outputs created
6. Example dialogue
7. Next steps
8. Related docs

#### Reference Page

1. Purpose
2. When to use it
3. Canonical rules
4. Examples
5. Related docs

### Markdown Usage Rules

Use:
- tables for comparisons, options, deliverables, and capability maps
- bullets for short lists, trigger phrases, and caveats
- numbered lists for sequential procedures
- typed code fences only: `bash`, `text`, `yaml`, `json`, `csv`, `mermaid`

### Mermaid Usage Rules

Use Mermaid when a diagram improves workflow, routing, or lifecycle understanding.

Preferred diagram types:
- `flowchart` for workflows and handoffs
- `sequenceDiagram` for interaction flow
- `stateDiagram` only for state transitions

Do not use Mermaid for:
- file trees
- path examples
- static inventories
- simple linear content that reads clearly as a list

Keep file trees and output layouts in `text` fences.

## Output Path Conventions

### Standard Structure

```
.pawbytes/{module}/{type}/{slug}/
```

| Part | Examples |
|------|----------|
| module | `marketing-suites`, `creative-suites`, `tools-output` |
| type | `brands`, `campaigns`, `reports`, `presentations` |
| slug | `acme-corp`, `q1-launch`, `seo-audit-2024` |

### Brand Workspace

```
.pawbytes/{module}/brands/{brand-slug}/
├── brand-context.md
├── guidelines.md
├── campaigns/
├── channels/
└── status.md
```

### Campaign Output

```
.pawbytes/{module}/brands/{brand-slug}/campaigns/{type}-{campaign-slug}/
├── strategy.md
├── brief.md
└── channels/
    └── seo/
        └── content/
```

### Tools Output

```
.pawbytes/tools-output/
├── presentations/
├── releases/
└── reports/
```

### Path Resolution in SKILL.md

```markdown
## Path Resolution

**Brand workspace root**: `{project-root}/.pawbytes/marketing-suites/brands/{brand-slug}/`

**SOSTAC plans**: `{project-root}/.pawbytes/marketing-suites/brands/{brand-slug}/sostac/`

**Campaign coordination**: `{project-root}/.pawbytes/marketing-suites/brands/{brand-slug}/campaigns/{type}-{campaign-slug}/`

If no brand slug is known, prompt for brand selection first.
```

---

## Trigger Phrase Conventions

### Format

Include trigger phrases in the description frontmatter:

```yaml
description: "SEO specialist for technical audits, keyword strategy. Triggers: 'SEO', 'keyword research', 'schema markup', 'crawlability'."
```

### Guidelines

| Guideline | Example |
|-----------|---------|
| Use exact phrases users would say | `'SEO audit'` not `'perform SEO audit'` |
| Include 3-5 phrases | Cover common variations |
| Order by frequency | Most common first |
| Include module-specific terms | `'SOSTAC'` for marketing |
| Include output-focused phrases | `'create presentation'` |

### Examples by Skill Type

**Agent skills:**

```yaml
description: "Creative director who orchestrates the Aria Creative Suite. Use when the user asks for Aria, wants creative direction, campaign planning, brand setup."
```

**Workflow skills:**

```yaml
description: "Executes the 6-phase SOSTAC marketing planning framework. Triggers for 'SOSTAC', 'marketing plan', 'situation analysis', 'marketing strategy'."
```

**Utility skills:**

```yaml
description: "Automates software releases from version bump to GitHub release. Use when the user requests to 'create a release', 'cut a release', 'publish a new version'."
```

---

## Headless Mode Conventions

### Declaration

Skills supporting headless mode should declare it:

```markdown
## Overview

**Args:** Accepts `--headless` / `-H` for non-interactive execution.
```

### Activation Handling

```markdown
## On Activation

If `--headless` or `-H` is passed, proceed through all stages without interaction using sensible defaults. Otherwise, confirm with the user before proceeding.
```

### Stage Progression

```markdown
### Stage 1: Name

**Progression:** Move to Stage 2 when condition is met. In headless mode, use sensible defaults and proceed automatically.
```

### Default Values

Document default values used in headless mode:

```markdown
**Headless defaults:**
- Version bump: patch (unless conventional commits indicate otherwise)
- Branch: main
- Changelog: generated from commits
```

---

## Escalation Route Conventions

### Format

```markdown
## Escalation Routes

| Signal | Routes To |
|--------|-----------|
| Condition | target-skill-name |
| Condition | target-skill-name |
```

### Guidelines

| Guideline | Reason |
|-----------|--------|
| Use specific conditions | Clear routing logic |
| Use exact skill names | Enable direct invocation |
| Order by frequency | Common cases first |
| Include input/output context | Help next skill |

### Example

```markdown
## Escalation Routes

| Signal | Routes To |
|--------|-----------|
| SEO, keywords, technical audit | paw-mkt-seo |
| Content, blog, editorial | paw-mkt-content |
| Paid ads, PPC, retargeting | paw-mkt-paid-ads |
| Analytics, tracking, dashboards | paw-mkt-analytics |
```

---

## Output Contract Conventions

### Format

```markdown
## Output Contract

Each deliverable includes:
- **Item**: description
- **Item**: description
- **Item**: description
- **File saved to**: path
```

### Example

```markdown
## Output Contract

SEO deliverables include:
- **SEO type**: technical, content, local, pSEO, or GEO
- **Findings/recommendations**: specific, prioritized actions (P1/P2/P3)
- **Keywords**: target terms with volume and difficulty
- **Implementation notes**: what to change and where
- **File saved to**: path where deliverable was written
```

---

## Do's and Don'ts

### SKILL.md

| Do | Don't |
|----|-------|
| Include trigger phrases in description | Use vague descriptions |
| Define path resolution with variables | Hardcode paths |
| Use progressive disclosure for frameworks | Bulk-read all files |
| Document headless mode support | Assume interactive only |
| List escalation routes | Leave routing undefined |

### Reference Files

| Do | Don't |
|----|-------|
| Keep files focused | Cover multiple topics |
| Include examples | Stay abstract |
| Define output format | Leave deliverables unclear |
| Use numbered prefixes for sequences | Random file names |

### Frameworks

| Do | Don't |
|----|-------|
| Use frameworks-index.csv | Skip the index |
| Keep index rows concise | Include every detail |
| Use specific best_for values | Use generic descriptions |
| Tag appropriately | Skip tags |

### Output Paths

| Do | Don't |
|----|-------|
| Use path variables | Hardcode absolute paths |
| Follow standard structure | Create custom layouts |
| Document paths in SKILL.md | Assume paths are known |

---

## Quality Checklist

Before submitting a skill, verify:

- [ ] SKILL.md has YAML frontmatter with `name` and `description`
- [ ] Description includes trigger phrases
- [ ] Overview section present
- [ ] Path resolution defined (if skill produces output)
- [ ] Reference lookup protocol defined (if using frameworks)
- [ ] Escalation routes defined (if skill routes to others)
- [ ] Headless mode documented (if supported)
- [ ] Output contract defined (if skill produces deliverables)
- [ ] Identity section present (for agent skills only)
- [ ] Principles section present
- [ ] File names follow naming conventions