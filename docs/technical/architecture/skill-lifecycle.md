# Skill Lifecycle

This document explains the complete lifecycle of a skill from discovery to completion.

## Lifecycle Phases

```
┌─────────────────────────────────────────────────────────────────┐
│                          DISCOVERY                               │
│                                                                  │
│  Skill found via marketplace or direct reference                │
│  Trigger phrases in description frontmatter enable discovery    │
└────────────────────────────────┬────────────────────────────────┘
                                 │
                                 ▼
┌─────────────────────────────────────────────────────────────────┐
│                          ACTIVATION                              │
│                                                                  │
│  User invokes via trigger phrase or explicit command            │
│  Example: "Help me with SEO strategy" → paw-mkt-seo            │
└────────────────────────────────┬────────────────────────────────┘
                                 │
                                 ▼
┌─────────────────────────────────────────────────────────────────┐
│                         INITIALIZE                               │
│                                                                  │
│  ┌──────────────────┐  ┌──────────────────┐                    │
│  │ Load Config      │  │ Check Memory     │                    │
│  │ .pawbytes/config │  │ .pawbytes/index  │                    │
│  └────────┬─────────┘  └────────┬─────────┘                    │
│           │                     │                               │
│           └──────────┬──────────┘                               │
│                      ▼                                           │
│           ┌──────────────────┐                                  │
│           │ Load Brand       │                                  │
│           │ Context          │                                  │
│           └──────────────────┘                                  │
└────────────────────────────────┬────────────────────────────────┘
                                 │
                                 ▼
┌─────────────────────────────────────────────────────────────────┐
│                          EXECUTION                               │
│                                                                  │
│  ┌──────────────────┐                                          │
│  │ Match User       │  Read capabilities table                 │
│  │ Request          │  Find matching capability                │
│  └────────┬─────────┘                                          │
│           │                                                      │
│           ▼                                                      │
│  ┌──────────────────┐                                          │
│  │ Load Reference   │  Load capability file                    │
│  │                  │  Read frameworks-index.csv               │
│  └────────┬─────────┘  Load matched framework files            │
│           │                                                      │
│           ▼                                                      │
│  ┌──────────────────┐                                          │
│  │ Process Request  │  Follow methodology                      │
│  │                  │  Generate deliverables                   │
│  └────────┬─────────┘                                          │
└───────────┼─────────────────────────────────────────────────────┘
            │
            ▼
┌─────────────────────────────────────────────────────────────────┐
│                           OUTPUT                                 │
│                                                                  │
│  Write artifacts to resolved paths:                             │
│  • .pawbytes/{module}/brands/{brand}/                           │
│  • .pawbytes/{module}/reports/                                  │
│  • Brand workspace files                                        │
└────────────────────────────────┬────────────────────────────────┘
                                 │
                                 ▼
┌─────────────────────────────────────────────────────────────────┐
│                         COMPLETION                               │
│                                                                  │
│  ┌──────────────────┐  ┌──────────────────┐                    │
│  │ Update Memory    │  │ Report Results   │                    │
│  │ (agent skills)   │  │ to User          │                    │
│  └────────┬─────────┘  └────────┬─────────┘                    │
│           │                     │                               │
│           └──────────┬──────────┘                               │
│                      ▼                                           │
│           ┌──────────────────┐                                  │
│           │ Recommend        │                                  │
│           │ Next Steps       │                                  │
│           └──────────────────┘                                  │
└─────────────────────────────────────────────────────────────────┘
```

## Phase Details

### 1. Discovery

Skills are discovered through:

**Trigger Phrases** — In YAML frontmatter:

```yaml
---
name: paw-mkt-seo
description: SEO specialist. Triggers: 'SEO', 'keyword research', 'schema markup', 'crawlability'
---
```

When user says "Help with keyword research", the system matches to `paw-mkt-seo`.

**Direct Invocation** — Explicit skill reference:

```
User: "Use paw-mkt-seo to audit my site"
```

### 2. Activation

The skill is loaded and its `SKILL.md` is read:

```markdown
## On Activation

Load available config from `{project-root}/.pawbytes/config/config.yaml`
and `{project-root}/.pawbytes/config/config.user.yaml` if present.

Greet the user and offer to show available capabilities.
```

### 3. Initialize

Skills perform setup tasks:

| Task | Location | Purpose |
|------|----------|---------|
| Load config | `.pawbytes/config/` | Get user preferences, API keys |
| Check memory | `.pawbytes/{module}/index.md` | Resume previous context |
| Load brand | `.pawbytes/{module}/brands/{brand}/` | Get brand context |

**Configuration Variables:**

```markdown
- `{user_name}` — Address user by name
- `{communication_language}` — Response language
- `{output_folder}` — Where to save artifacts
```

### 4. Execution

The core processing phase:

#### 4.1 Match Request to Capability

```markdown
## Capabilities

| Capability | Route |
|------------|-------|
| Technical SEO | Load `./references/capability-technical-seo.md` |
| Content SEO | Load `./references/capability-content-seo.md` |
| Local SEO | Load `./references/capability-local-seo.md` |
```

Skills read the capabilities table and match to user request.

#### 4.2 Load References

**Progressive disclosure pattern:**

```
1. Read frameworks-index.csv (~20-30 rows)
2. Match user situation to best_for column
3. Load ONLY matched framework files
4. Never bulk-read all frameworks
```

**Example index:**

```csv
id,name,description,best_for,file,tags
technical-audit,Technical Audit,Crawlability issues,Site audits,frameworks/technical-audit.md,"audit"
schema-markup,Schema Markup,JSON-LD examples,Structured data,frameworks/schema-markup.md,"schema"
```

#### 4.3 Process Request

Follow the methodology in loaded references:

```markdown
## Response Protocol

1. **Understand** — Parse user request
2. **Match** — Find relevant capability
3. **Load** — Read reference/framework file
4. **Execute** — Follow methodology
5. **Output** — Write artifacts
6. **Report** — Summarize results
```

### 5. Output

Skills write artifacts to the file system:

```markdown
## Path Resolution

**Campaign mode:**
  - Save to `.pawbytes/marketing-suites/brands/{brand}/campaigns/{campaign}/channels/seo/`

**Standalone mode:**
  - Save to `.pawbytes/marketing-suites/brands/{brand}/channels/seo/`
```

**Output Contract:**

Every skill should produce:

| Output | Description |
|--------|-------------|
| Action type | What was done |
| Files saved | Where artifacts were written |
| Recommendations | What to do next |
| Status | Success/partial/failure |

### 6. Completion

Final steps:

**Update Memory (Agent Skills):**

```markdown
## Memory

Writes to:
- `{project-root}/.pawbytes/creative-suites/index.md` — Active brands, campaigns
- `{project-root}/.pawbytes/creative-suites/brands/{brand}/guidelines.md` — Brand identity
```

**Report Results:**

```markdown
## Output Contract

Every coordination deliverable includes:
- **Action type**: routing decision, team spawn, etc.
- **Brand**: which brand workspace this applies to
- **Next recommended action**: what the user should do next
- **File saved to**: resolved path
```

**Escalation Routes:**

Skills can recommend other skills:

```markdown
## Escalation Routes

| Signal | Routes To |
|--------|-----------|
| Content creation beyond keyword briefs | paw-mkt-content |
| Link building via PR | paw-mkt-pr |
| Landing page conversion optimization | paw-mkt-cro |
```

## State Management

Skills maintain context through:

### File System

All persistent state lives in files:

```
.pawbytes/{module}/
├── index.md              # Memory entry point
├── brands/{brand}/
│   ├── brand-context.md  # Brand identity
│   ├── status.md         # Progress tracking
│   └── campaigns/        # Campaign files
```

### Memory System (Agent Skills)

Agent skills use a sidecar memory:

```markdown
## On Activation

Load sidecar memory from `{project-root}/.pawbytes/creative-suites/index.md`
— this is the single entry point to the memory system.
```

### Configuration

Runtime settings from config files:

```yaml
# config.yaml
user_name: User
communication_language: English
output_folder: "{project-root}/.pawbytes/marketing-suites"
```

## Special Modes

### Headless Mode

For non-interactive execution:

```markdown
If `--headless` or `-H` is passed, load `./references/headless-mode.md`
and execute without interaction.
```

### Fast-Path Mode

For expert users:

```markdown
Fast-path: `--yolo` skips validation gates for expert users with explicit specs.
```

## Example: SEO Skill Lifecycle

```
1. DISCOVERY
   User: "I need help with technical SEO"
   Match: paw-mkt-seo (via trigger phrase)

2. ACTIVATION
   Load SKILL.md
   Execute On Activation section

3. INITIALIZE
   Load config from .pawbytes/config/
   Check for brand context

4. EXECUTION
   Match to "Technical SEO" capability
   Load capability-technical-seo.md
   Read frameworks-index.csv
   Match "Site audits" → technical-audit.md
   Execute audit methodology

5. OUTPUT
   Save audit report to:
   .pawbytes/marketing-suites/brands/{brand}/channels/seo/

6. COMPLETION
   Report findings with P1/P2/P3 priorities
   Recommend next steps (fix crawlability, then schema)
   Suggest routing to paw-mkt-content for content SEO
```