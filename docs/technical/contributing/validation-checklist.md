# Skill Validation Checklist

A comprehensive checklist for validating skill quality before submission. Use this to ensure your skill follows Pawbytes conventions and will function correctly in the ecosystem.

---

## Required Elements

Every skill MUST have these elements:

### SKILL.md Structure

- [ ] `SKILL.md` file exists at skill root
- [ ] YAML frontmatter present at the top of SKILL.md
- [ ] `name` field in frontmatter matches folder name
- [ ] `description` field includes trigger phrases
- [ ] Overview section describes what the skill does

### Naming

- [ ] Skill name follows convention: `{org}-{module}-{skillname}`
- [ ] `org` is `paw` (3 letters)
- [ ] `module` is 3 letters (`mkt`, `cra`, `tools`)
- [ ] `skillname` uses kebab-case
- [ ] Folder name exactly matches skill name

### Path Resolution

- [ ] Output paths defined in SKILL.md
- [ ] Paths use variable tokens (not hardcoded)
- [ ] Paths follow `.pawbytes/{module}/` structure

---

## By Skill Type

### Agent Skills

Agent skills have persistent personas with memory and identity.

**Required:**

- [ ] Identity section present
- [ ] Communication style defined
- [ ] Principles listed
- [ ] On Activation section present

**Identity section should include:**

- [ ] Name/role of the agent
- [ ] Personality traits
- [ ] Professional stance

**Example identity:**
```markdown
## Identity

I am the master coordinator for a full-service digital marketing agency, managing brands, routing users to correct workflows, and spawning specialist teams for campaign implementation.
```

**Communication style should specify:**

- [ ] Tone (formal, conversational, technical, etc.)
- [ ] How options are presented
- [ ] Example phrases

**Example communication style:**
```markdown
## Communication Style

- **Confident but not arrogant** - "Here's what I'd recommend" not "You should do this"
- **Conversational** - natural dialogue, not form-filling
- **Proactive** - suggests next steps, catches issues early
```

### Workflow Skills

Workflow skills are deterministic pipelines with defined steps.

**Required:**

- [ ] Clear input specification
- [ ] Step-by-step process documented
- [ ] Output specification
- [ ] Progression conditions defined

**Workflow structure:**

- [ ] Stages or phases clearly numbered
- [ ] Each stage has a reference file route
- [ ] Progression conditions explain when to move to next stage

**Example:**
```markdown
## Workflow

1. **Validate** - Load `./references/01-validate.md`
2. **Version** - Load `./references/02-version.md`
3. **Changelog** - Load `./references/03-changelog.md`
4. **Release** - Load `./references/04-release.md`

Each stage specifies its progression condition. If a stage fails, stop and inform the user.
```

### Utility Skills

Utility skills are single-purpose tools with minimal interaction.

**Required:**

- [ ] Clear purpose statement
- [ ] Input/output specification
- [ ] `--headless` support documented (if applicable)

---

## Configuration Integration

### On Activation Section

All skills that use configuration must have an On Activation section:

- [ ] Lists config file locations
- [ ] Specifies fallback defaults
- [ ] Defines behavior when config is missing

**Example:**
```markdown
## On Activation

Load available config from `{project-root}/.pawbytes/config/config.yaml` and `{project-root}/.pawbytes/config/config.user.yaml` if present. Resolve and apply throughout the session (defaults in parens):

- `{user_name}` (null) - address the user by name
- `{communication_language}` (English) - use for all communications
```

---

## Framework Integration

### Skills with Frameworks

If your skill uses progressive disclosure for domain knowledge:

- [ ] `references/frameworks-index.csv` exists
- [ ] CSV has required columns: `id`, `name`, `description`, `best_for`, `file`, `tags`
- [ ] Framework files exist in `references/frameworks/`
- [ ] Index references correct file paths
- [ ] `best_for` column has specific, useful values

**CSV format:**
```csv
id,name,description,best_for,file,tags
technical-audit,Technical Audit,Crawlability issues,Site audits,frameworks/technical-audit.md,"audit,technical"
keyword-strategy,Keyword Strategy,Keyword research,Content planning,frameworks/keyword-strategy.md,"keywords"
```

### Reference Lookup Protocol

Skills with frameworks must document how to load them:

- [ ] Protocol documented in SKILL.md
- [ ] Specifies reading index first
- [ ] Emphasizes selective loading (never bulk-read)

**Example:**
```markdown
## Reference Lookup Protocol

1. Read `./references/frameworks-index.csv` - lightweight index (~10 rows)
2. Match user's situation to `best_for` column
3. Read ONLY matched framework file(s) from `./references/frameworks/`
4. Never bulk-read all framework files
```

---

## Reference Files

### Capability References

If your skill has capability routing:

- [ ] Capabilities table maps capabilities to files
- [ ] Reference files exist at the specified paths
- [ ] Each reference is focused on one topic

**Example:**
```markdown
## Capabilities

| Capability | Route |
|------------|-------|
| Technical SEO | Load `./references/capability-technical-seo.md` |
| Content SEO | Load `./references/capability-content-seo.md` |
```

### Escalation Routes

If your skill routes to other skills:

- [ ] Escalation routes table present
- [ ] Signal column describes when to route
- [ ] Routes To column uses exact skill names

**Example:**
```markdown
## Escalation Routes

| Signal | Routes To |
|--------|-----------|
| Content creation beyond keyword briefs | paw-mkt-content |
| Link building via PR and earned media | paw-mkt-pr |
```

---

## Setup Skills

Setup skills have additional requirements:

### module.yaml

- [ ] `assets/module.yaml` exists
- [ ] `code` field present (3-letter module identifier)
- [ ] `name` field present
- [ ] `description` field present
- [ ] `module_version` field present
- [ ] Configuration variables defined with `prompt`, `default`, `result` fields

**Example:**
```yaml
code: mkt
name: Agentic Marketing Suite
description: Multi-line description
module_version: 1.0.0

output_folder:
  prompt: "Where should output be saved?"
  default: "{project-root}/.pawbytes/marketing-suites"
  result: "{value}"
  directories: true
  user_setting: true
```

---

## Quality Checks

### Description Quality

The description field is critical for skill discovery:

- [ ] Includes specific trigger phrases
- [ ] Phrases are user-friendly (what users would actually say)
- [ ] Covers the main use cases
- [ ] No more than 2-3 sentences

**Good:**
```yaml
description: SEO specialist for technical audits, keyword strategy, local SEO. Triggers: 'SEO', 'keyword research', 'schema markup', 'crawlability'.
```

**Bad:**
```yaml
description: Does SEO things.
```

### Path Quality

- [ ] Uses `{project-root}` token (not actual paths)
- [ ] Uses `{brand-slug}` variable for brand-specific paths
- [ ] Follows module conventions

**Standard path patterns:**
```
.pawbytes/{module}/brands/{brand-slug}/
.pawbytes/{module}/brands/{brand-slug}/campaigns/{type}-{campaign-slug}/
.pawbytes/{module}/reports/
```

### Code Quality

- [ ] No hardcoded absolute paths
- [ ] No hardcoded API keys
- [ ] Variable substitution used consistently
- [ ] File references use relative paths from skill root

---

## Integration Checks

### Coordinator Pattern

If your skill is a coordinator:

- [ ] Routes to all relevant specialists
- [ ] Does not execute production work itself
- [ ] Has clear escalation routes

### Specialist Pattern

If your skill is a specialist:

- [ ] Documents when it should be invoked
- [ ] Reads brand/context files before acting
- [ ] Writes outputs to correct paths

### Memory Integration

If your skill uses memory:

- [ ] Documents memory read locations
- [ ] Documents memory write locations
- [ ] Uses correct memory index file

---

## Published Documentation Checks

Apply these checks when reviewing docs under `docs/`.

### Accuracy Against Source Truth

- [ ] Canonical skill names match `src/**/SKILL.md`
- [ ] Output paths and artifacts match `src/**/SKILL.md`
- [ ] Published behavior does not contradict source behavior

### Structure and Formatting

- [ ] Page follows the expected structure for its doc type
- [ ] Tables, bullets, and numbered lists are used appropriately
- [ ] Code fences are typed (`bash`, `text`, `yaml`, `json`, `csv`, `mermaid`)
- [ ] Important warnings or caveats are surfaced clearly

### Mermaid and Visual Grammar

- [ ] Mermaid is used only where workflow, routing, or lifecycle clarity benefits from it
- [ ] File trees and output layouts remain in `text` fences
- [ ] Diagram type fits the content (`flowchart`, `sequenceDiagram`, `stateDiagram` only when justified)

### Navigation and Link Quality

- [ ] Related-doc links resolve correctly
- [ ] Hub pages still point to the right destination after changes
- [ ] Next-step navigation is clear for the intended audience

## Final Checklist

Before submitting:

- [ ] All required elements present
- [ ] Skill type specific requirements met
- [ ] Configuration integration documented
- [ ] Framework setup correct (if applicable)
- [ ] Reference files exist and are valid
- [ ] Quality checks passed
- [ ] Naming conventions followed
- [ ] Paths use tokens, not hardcoded values

---

## Common Issues

| Issue | Fix |
|-------|-----|
| Missing frontmatter | Add YAML block at top of SKILL.md |
| No trigger phrases in description | Add "Triggers:" or "Use when:" to description |
| Hardcoded paths | Replace with `{project-root}` tokens |
| Missing capability files | Create referenced files or fix paths |
| Bulk framework loading | Add Reference Lookup Protocol section |
| No escalation routes for coordinator | Add Escalation Routes table |