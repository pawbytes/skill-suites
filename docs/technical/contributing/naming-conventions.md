# Naming Conventions

Consistent naming enables discoverability, maintainability, and clear communication. This document defines naming rules for skills, folders, files, and identifiers.

## Skill Names

### Format

Skills follow the pattern: `{org}-{module}-{skillname}`

| Part | Format | Length | Examples |
|------|--------|--------|----------|
| org | lowercase letters | 3 chars | `paw` |
| module | lowercase letters | 3 chars | `mkt`, `cra`, `tools` |
| skillname | kebab-case | 2-30 chars | `seo`, `agent-designer`, `video-shortform` |

### Module Codes

| Module | Code | Description |
|--------|------|-------------|
| Marketing | `mkt` | Marketing strategy and execution |
| Creative | `cra` | Design and video production |
| Tools | `tools` | Utility functions |

### Skill Name Patterns

#### Agent Skills

Agent skills include `agent-` prefix:

```
paw-{module}-agent-{name}
```

| Correct | Incorrect |
|---------|-----------|
| `paw-mkt-agent-agency` | `paw-mkt-coordinator` |
| `paw-cra-agent-creative-director` | `paw-cra-creative-director` |
| `paw-cra-agent-designer` | `paw-cra-designer-agent` |
| `paw-cra-agent-video-producer` | `paw-cra-video-producer` |

**Note:** `paw-mkt-agent-agency` is a special case — the marketing coordinator uses `agency` instead of `agent-coordinator` for clarity.

#### Workflow Skills

Workflow skills use descriptive names without prefix:

```
paw-{module}-{workflow-name}
```

| Correct | Incorrect |
|---------|-----------|
| `paw-mkt-sostac` | `paw-mkt-sostac-workflow` |
| `paw-cra-design-social` | `paw-cra-social-design` |
| `paw-cra-video-shortform` | `paw-cra-shortform-video` |
| `paw-cra-campaign-orchestration` | `paw-cra-orchestration` |

#### Utility Skills

Utility skills use descriptive names:

```
paw-tools-{utility-name}
```

| Correct | Incorrect |
|---------|-----------|
| `paw-tools-release` | `paw-tools-release-automation` |
| `paw-tools-presentation` | `paw-tools-presentation-maker` |

### Naming Rules

| Rule | Example | Reason |
|------|---------|--------|
| Use kebab-case | `video-shortform` not `videoShortform` | Consistency, URL-safe |
| Be specific | `design-social` not `social` | Avoid ambiguity |
| Avoid redundancy | `paw-tools-release` not `paw-tools-release-tool` | Module already indicates tool |
| Match common terms | `seo` not `search-engine-optimization` | Discoverability |
| Order matters | `video-shortform` not `shortform-video` | Platform → Format pattern |

---

## Folder Names

### Skill Folders

Skill folder names match the skill name exactly:

```
src/{module}/paw-{module}-{skillname}/
```

| Correct | Incorrect |
|---------|-----------|
| `src/marketing/paw-mkt-seo/` | `src/marketing/seo/` |
| `src/creative/paw-cra-agent-designer/` | `src/creative/agent-designer/` |
| `src/tools/paw-tools-release/` | `src/tools/release/` |

### Subdirectories

Standard subdirectories within skill folders:

| Directory | Purpose | Required |
|-----------|---------|----------|
| `references/` | Knowledge files loaded during execution | Optional |
| `assets/` | Static files, configs, scripts | Optional |
| `scripts/` | Executable scripts | Optional |
| `evals/` | Test cases and evaluation | Optional |

### Reference Subdirectories

| Directory | Purpose |
|-----------|---------|
| `references/frameworks/` | Framework methodology files |
| `references/templates/` | Template files |

---

## File Names

### SKILL.md

Every skill must have a `SKILL.md` file (exact name, uppercase):

| Correct | Incorrect |
|---------|-----------|
| `SKILL.md` | `skill.md` |
| `SKILL.md` | `Skill.md` |
| `SKILL.md` | `README.md` |

### Reference Files

Reference files use kebab-case with descriptive names:

| Pattern | Example |
|---------|---------|
| Capability files | `capability-technical-seo.md` |
| Framework files | `technical-audit.md` |
| Process files | `01-brief-parsing.md` |
| Shared patterns | `shared-patterns.md` |
| Best practices | `best-practices.md` |

#### Numbered References

Sequential processes use numbered prefixes:

```
01-stage-name.md
02-stage-name.md
03-stage-name.md
```

| Correct | Incorrect |
|---------|-----------|
| `01-validate.md` | `1-validate.md` |
| `02-version.md` | `version-2.md` |
| `03-changelog.md` | `changelog.md` (when sequential) |

### CSV Files

CSV files use kebab-case:

| Correct | Incorrect |
|---------|-----------|
| `frameworks-index.csv` | `frameworks_index.csv` |
| `module-help.csv` | `ModuleHelp.csv` |

### Script Files

Python scripts use snake_case:

| Correct | Incorrect |
|---------|-----------|
| `init_memory.py` | `init-memory.py` |
| `parse_commits.py` | `parseCommits.py` |
| `detect_version_files.py` | `detect-version-files.py` |

---

## Identifiers

### Brand Slugs

Brand identifiers use lowercase with hyphens:

| Correct | Incorrect |
|---------|-----------|
| `acme-corp` | `AcmeCorp` |
| `my-brand` | `my_brand` |
| `company-name-inc` | `CompanyNameInc` |

### Campaign Slugs

Campaign identifiers use lowercase with hyphens:

| Correct | Incorrect |
|---------|-----------|
| `q1-launch` | `Q1Launch` |
| `spring-sale-2024` | `spring_sale_2024` |
| `product-announcement` | `productAnnouncement` |

### Tags and Labels

Tags use lowercase with hyphens:

| Correct | Incorrect |
|---------|-----------|
| `social-media` | `Social Media` |
| `video-production` | `VideoProduction` |
| `technical-seo` | `technical_seo` |

---

## YAML Frontmatter

### Name Field

The `name` field matches the skill name exactly:

```yaml
---
name: paw-mkt-seo
description: "SEO specialist for..."
---
```

| Correct | Incorrect |
|---------|-----------|
| `name: paw-mkt-seo` | `name: SEO Specialist` |
| `name: paw-cra-agent-designer` | `name: Designer` |

### Description Field

The description includes trigger phrases:

```yaml
---
name: paw-mkt-seo
description: "SEO specialist for technical audits, keyword strategy, local SEO. Triggers: 'SEO', 'keyword research', 'schema markup', 'crawlability'."
---
```

**Format:** Main description followed by `Triggers:` or `Use when:` with trigger phrases.

---

## Path Variables

### Variable Names

Path variables use snake_case with curly braces:

| Variable | Resolves To |
|----------|-------------|
| `{project-root}` | Project root directory |
| `{user_name}` | User's name from config |
| `{output_folder}` | Output directory path |
| `{module}` | Module name (e.g., `marketing-suites`) |
| `{brand-slug}` | Brand identifier |
| `{campaign-slug}` | Campaign identifier |

### Path Examples

```markdown
## Path Resolution

- Brand context: `{project-root}/.pawbytes/{module}/brands/{brand-slug}/`
- Campaigns: `{project-root}/.pawbytes/{module}/brands/{brand-slug}/campaigns/{campaign-slug}/`
- Reports: `{project-root}/.pawbytes/{module}/reports/`
```

---

## Do's and Don'ts

### Do's

- Use canonical skill IDs from source in published docs (`paw-mkt-*`, `paw-cra-*`, `paw-tools-*`)
- Use kebab-case for skill names, folders, and markdown files
- Use snake_case for Python scripts
- Use lowercase for all identifiers
- Include trigger phrases in descriptions
- Match folder names to skill names exactly
- Use numbered prefixes for sequential reference files
- Use one canonical path form in reference docs and label shorthand paths clearly when used

### Don'ts

| Don't | Instead |
|-------|---------|
| `paw-mkt-SEO` | `paw-mkt-seo` |
| `paw-cra-AgentDesigner` | `paw-cra-agent-designer` |
| `src/marketing/seo/` | `src/marketing/paw-mkt-seo/` |
| `skill.md` | `SKILL.md` |
| `AcmeCorp` | `acme-corp` |
| `technical_audit.md` | `technical-audit.md` |

---

## Quick Reference

| Item | Convention | Example |
|------|------------|---------|
| Skill name | `{org}-{module}-{skillname}` | `paw-mkt-seo` |
| Agent skill | `paw-{module}-agent-{name}` | `paw-cra-agent-designer` |
| Skill folder | Match skill name | `src/marketing/paw-mkt-seo/` |
| SKILL.md | Exact uppercase | `SKILL.md` |
| Reference files | kebab-case | `technical-audit.md` |
| Numbered refs | `01-name.md` | `01-validate.md` |
| CSV files | kebab-case | `frameworks-index.csv` |
| Python scripts | snake_case | `parse_commits.py` |
| Brand slugs | lowercase-hyphen | `acme-corp` |
| Campaign slugs | lowercase-hyphen | `q1-launch` |
| Path variables | `{snake_case}` | `{project-root}` |