# SKILL.md Format Specification

## Overview

The `SKILL.md` file is the main definition for every skill. It uses YAML frontmatter for metadata and Markdown for the skill definition.

## YAML Frontmatter (Required)

Every SKILL.md must start with YAML frontmatter:

```yaml
---
name: skill-name
description: "Description with trigger phrases. Use when user says X, Y, Z..."
---
```

### Required Fields

| Field | Purpose | Format |
|-------|---------|--------|
| `name` | Skill identifier | `{org}-{module}-{skillname}` |
| `description` | Discovery metadata | Include trigger phrases |

### Description Best Practices

The `description` field should include trigger phrases for skill discovery:

```yaml
---
name: paw-mkt-seo
description: "SEO specialist for technical audits, keyword strategy, local SEO, link building, pSEO, and GEO optimization. Triggers: 'SEO', 'keyword research', 'schema markup', 'crawlability', 'pSEO', 'GEO', 'search rankings', 'link building'."
---
```

```yaml
---
name: paw-cra-agent-designer
description: Visual production expert for production-ready social posts, carousels, flyers, brand assets, and code-based templates. Trigger when user requests 'create social post', 'design carousel', 'make flyer', 'generate logo', 'resize image', or 'create template'.
---
```

## Standard Sections

### Overview

Brief description of what the skill does and who should use it.

```markdown
## Overview

Delivers actionable SEO strategies grounded in brand positioning. Covers technical 
SEO audits, content keyword research, local SEO, link building, programmatic SEO 
systems, and AI search optimization (GEO). Outputs prioritized recommendations, 
implementation-ready schema markup, and monthly action plans.
```

### Identity (Agent Skills Only)

Defines how the skill presents itself. Required for agent skills, omitted for workflow/utility skills.

```markdown
## Identity

Senior SEO specialist with deep expertise across technical SEO, content SEO, 
local SEO, link building, digital PR, and AI search optimization (GEO).
```

```markdown
## Identity

I am a detail-oriented visual production expert who speaks in terms of layouts, 
compositions, visual hierarchy, and aesthetic precision.
```

### Communication Style

Defines how the agent communicates.

```markdown
## Communication Style

- **Direct and actionable**: Every recommendation includes specific implementation steps
- **Prioritized**: P1/P2/P3 rankings for all action items
- **Evidence-based**: Recommendations cite SERP patterns, competitor data, or guidance
- **Example**: "Your LCP is 4.2s (target: 2.5s). Priority P1. Fix: Preload hero image."
```

### Principles

Core principles that guide the skill's behavior.

```markdown
## Principles

- **Read Before Acting**: Never generate content without first reading existing files
- **Brand Consistency**: Every output aligns with brand context
- **File System as Source of Truth**: All plans and progress live in brand directory
- **Incremental Value**: Adapt to user needs; quick tasks don't require full workflows
```

### On Activation

Steps executed when skill activates. This is critical for initializing state.

```markdown
## On Activation

Load available config from `{project-root}/.pawbytes/config/config.yaml` and 
`{project-root}/.pawbytes/config/config.user.yaml` if present. Resolve and apply 
throughout the session (defaults in parens):

- `{user_name}` (null) — address the user by name
- `{communication_language}` (English) — use for all communications
- `{document_output_language}` (English) — use for generated document content

Read `./references/shared-patterns.md` for starting context routing.

Greet the user and offer to show available capabilities.
```

### Capabilities

Table mapping capabilities to reference files. This is the routing mechanism.

```markdown
## Capabilities

| Capability | Route |
|------------|-------|
| Technical SEO | Load `./references/capability-technical-seo.md` |
| Content SEO | Load `./references/capability-content-seo.md` |
| Local SEO | Load `./references/capability-local-seo.md` |
| Link Building & Digital PR | Load `./references/capability-link-building.md` |
| AI Search Optimization (GEO) | Load `./references/capability-geo.md` |
```

### Response Protocol

Step-by-step workflow for handling requests.

```markdown
## Response Protocol

When the user requests SEO work:

1. **Route the starting context** using `./references/shared-patterns.md`
2. **Read strategic context** (brand, SOSTAC) before proposing changes
3. **Clarify scope**: Which discipline? Technical, content, local, pSEO, GEO?
4. **Load relevant capability**: Read the matched capability file
5. **Lookup frameworks**: Read `./references/frameworks-index.csv` and load matched files
6. **Deliver actionable output**: Specific, implementable recommendations
7. **Save deliverables**: Write outputs to the resolved path
8. **Recommend next steps**: Suggest what to work on next
```

### Path Resolution

Output path conventions for where files are written.

```markdown
## Path Resolution

**Campaign mode** -- working within a named campaign:
  - Save to `./.pawbytes/marketing-suites/brands/{brand-slug}/campaigns/{type}-{campaign-slug}/channels/seo/content/`

**Standalone mode** -- evergreen or independent work:
  - Save to `./.pawbytes/marketing-suites/brands/{brand-slug}/channels/seo/content/`

**Legacy fallback** -- old directory structure detected:
  - Save to `./.pawbytes/marketing-suites/brands/{brand-slug}/content/seo/`
```

### Reference Lookup Protocol

How to load frameworks using progressive disclosure.

```markdown
## Reference Lookup Protocol

This skill uses progressive disclosure to save tokens.

1. Read `./references/frameworks-index.csv` -- lightweight index (~24 rows)
2. Match the user's situation to the `best_for` column
3. Read ONLY the matched framework file(s) from `./references/frameworks/`
4. Never bulk-read all framework files

General references (best-practices.md, shared-patterns.md) are read directly.
```

### Escalation Routes (Optional)

When to route to other skills.

```markdown
## Escalation Routes

| Signal | Routes To |
|--------|-----------|
| Content creation beyond keyword briefs | paw-mkt-content |
| Link building via PR and earned media | paw-mkt-pr |
| Landing page conversion optimization | paw-mkt-cro |
| Paid search complement to organic | paw-mkt-paid-ads |
```

### Output Contract

What the skill delivers.

```markdown
## Output Contract

SEO deliverables include:
- **SEO type**: technical, content, local, pSEO, or GEO
- **Findings/recommendations**: specific, prioritized actions (P1/P2/P3)
- **Keywords**: target terms with volume and difficulty when available
- **Implementation notes**: what to change and where
- **Expected impact**: which metrics should improve
- **File saved to**: path where deliverable was written
```

## Optional Sections

### Examples

Sample dialogues showing expected interactions:

```markdown
## Examples

**User:** "I need to improve my site's SEO"
**Response:** "I can help with that. Let me check your brand context first..."
```

### Tools

External tools and APIs used:

```markdown
## Tool Dependencies

| Tool | Purpose | Required |
|------|---------|----------|
| fal.ai MCP | Image generation | Yes |
| ffmpeg | Video conversion | Optional |
```

### Guardrails

Safety boundaries and constraints:

```markdown
## Guardrails

- Never modify production databases
- Always confirm before bulk operations
- Respect rate limits on external APIs
```

### Memory

How the agent uses the memory system:

```markdown
## Memory

- Brand context stored in `.pawbytes/creative-suites/brands/{brand}/`
- Session state in `.pawbytes/creative-suites/index.md`
- Load on activation, save on significant changes
```

## Section Ordering

For consistency, follow this order:

1. Overview
2. Identity (agent skills)
3. Communication Style
4. Principles
5. On Activation
6. Capabilities
7. Response Protocol
8. Path Resolution
9. Reference Lookup Protocol
10. Escalation Routes
11. Output Contract
12. Optional sections (Examples, Tools, Guardrails, Memory)

## Variable Substitution

Skills use variables in curly braces that are resolved at runtime:

| Variable | Resolves To |
|----------|-------------|
| `{project-root}` | Project root directory |
| `{user_name}` | User's name from config |
| `{communication_language}` | Language from config |
| `{brand-slug}` | Current brand identifier |

```markdown
Save to `{project-root}/.pawbytes/marketing-suites/brands/{brand-slug}/`
```