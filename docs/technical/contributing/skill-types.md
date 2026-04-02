# Skill Types

Skills in Pawbytes Skill Suites fall into three categories: **Agent**, **Workflow**, and **Utility**. Each type serves a distinct purpose and has specific characteristics.

## Quick Comparison

| Characteristic | Agent | Workflow | Utility |
|----------------|-------|----------|---------|
| **Has persona** | Yes | No | No |
| **Uses memory** | Yes | No | No |
| **Interaction level** | High | Medium | Low |
| **Headless mode** | Limited | Full support | Full support |
| **Primary output** | Coordination, routing | Deliverables | Artifacts |
| **Complexity** | High | Medium | Low |

---

## Agent Skills

Agent skills are persistent personas with identity, memory, and the ability to coordinate other skills. They maintain conversation context across sessions and make judgment-based decisions.

### Characteristics

- **Identity section** — Defines name, role, and personality
- **Communication style** — How the agent speaks and interacts
- **Memory system** — Persists context across sessions
- **Coordination ability** — Can route to or spawn other skills
- **Judgment-based routing** — Makes decisions based on context

### When to Create an Agent Skill

Create an agent skill when you need:

- A persistent persona that users interact with over time
- Complex multi-turn interactions requiring context retention
- Coordination of multiple specialist skills
- Judgment-based decision making
- Brand or campaign memory across sessions

### Agent Skill Structure

```yaml
---
name: paw-{module}-agent-{name}
description: "Trigger phrases describing what this agent does"
---

# Agent Name

## Overview
Brief description of the agent's role and capabilities.

## Identity
I am [persona description].

## Communication Style
- Style characteristic 1
- Style characteristic 2

## Principles
- **Principle 1**: Description
- **Principle 2**: Description

## On Activation
1. Load configuration
2. Load memory from `{project-root}/.pawbytes/{module}/index.md`
3. Greet user with context

## Capabilities
| Capability | Route |
|------------|-------|
| Capability 1 | Load `./references/capability-1.md` |

## Specialist Agents (if coordinator)
| Specialist | Skill Name | When to Invoke |
|------------|------------|----------------|
| Role | `skill-name` | Trigger condition |
```

### Examples

| Skill | Module | Role |
|-------|--------|------|
| `paw-mkt-agency` | Marketing | Master coordinator routing to 22 specialists |
| `paw-cra-agent-creative-director` | Creative | Aria — orchestrates Designer, Video Producer, Strategist |
| `paw-cra-agent-designer` | Creative | Visual production specialist |
| `paw-cra-agent-video-producer` | Creative | Video production specialist |
| `paw-cra-agent-strategist` | Creative | Research and content strategy (service agent) |

### Key Patterns

#### Coordinator Pattern

Some agents are coordinators that route work to specialists:

```markdown
## Specialist Agents

| Specialist | Skill Name | When to Invoke |
|------------|------------|----------------|
| Designer | `paw-cra-agent-designer` | Visual assets |
| Video Producer | `paw-cra-agent-video-producer` | Video content |
| Strategist | `paw-cra-agent-strategist` | Research, copy (on demand) |

**Production-first routing:** Route directly to production agents when the user requests a deliverable. Do NOT require validation from service agents first.
```

#### Memory System

Agents load memory on activation:

```markdown
## On Activation

Load shared agency memory from `{project-root}/.pawbytes/creative-suites/index.md`.
Load brand guidelines from `.pawbytes/creative-suites/brands/{active-brand}/guidelines.md`.
```

---

## Workflow Skills

Workflow skills are deterministic pipelines with defined stages. They take inputs, process them through a sequence of steps, and produce outputs. Workflows do not have personas or memory.

### Characteristics

- **Stage-based structure** — Sequential phases with clear progression
- **Defined inputs and outputs** — Explicit input requirements and output artifacts
- **No persona** — Acts as a pipeline, not a character
- **Full headless support** — Can run without interaction via `--headless`
- **Reference-driven** — Loads methodology from reference files

### When to Create a Workflow Skill

Create a workflow skill when you need:

- A clear input → output transformation
- Sequential steps with defined progression
- Minimal interaction (or full automation via headless mode)
- Repeatable, consistent process execution
- Stage-gated quality control

### Workflow Skill Structure

```yaml
---
name: paw-{module}-{workflow-name}
description: "Trigger phrases. Use when user says X, Y, Z..."
---

# Workflow Name

## Overview
Brief description of what the workflow produces.

**Args:** Accepts `--headless` / `-H` for autonomous execution.

**Output:** Description of deliverables and location.

## On Activation
1. Load configuration
2. Check prerequisites
3. Identify starting stage

## Pipeline

### Stage 1: Stage Name
Load `./references/01-stage-name.md`

**Progression:** Condition for moving to next stage.

### Stage 2: Stage Name
Load `./references/02-stage-name.md`

**Progression:** Condition for completion.

## Output Structure
.pawbytes/{module}/{type}/{slug}/
```

### Examples

| Skill | Module | Purpose |
|-------|--------|---------|
| `paw-mkt-sostac` | Marketing | 6-phase marketing plan (Situation → Control) |
| `paw-cra-design-social` | Creative | Social post and carousel production |
| `paw-cra-campaign-orchestration` | Creative | Multi-deliverable campaign execution |
| `paw-cra-video-shortform` | Creative | TikTok/Reels/Shorts video production |
| `paw-cra-quality-control` | Creative | Campaign-level QC with severity ratings |

### Key Patterns

#### Stage Progression

Each stage has a clear progression condition:

```markdown
### Stage 1: Brief & Context
Load `./references/01-brief-and-context.md`

**Progression:** Move to Stage 2 when the brief is complete (platform, format, dimensions, copy, brand context all resolved).
```

#### Headless Mode

Workflows support full automation:

```markdown
## On Activation

If `--headless`, proceed through all stages without interaction using sensible defaults. Otherwise, confirm the brief with the user before production begins.
```

#### HITL Review Gates

Some workflows require human approval between stages:

```markdown
## HITL Review Gates

**Human-in-the-Loop checkpoints are MANDATORY.** Never auto-advance through multiple phases without user review.

### Phase Completion Gate (After Each Phase)

After saving a phase document, **STOP and present for review:**

**Review Options:**
1. Approve & Continue
2. Request Changes
3. Deep Dive
```

---

## Utility Skills

Utility skills are single-purpose tools that perform focused tasks with minimal interaction. They are often used as building blocks by other skills or for automation workflows.

### Characteristics

- **Single responsibility** — One focused task
- **Minimal interaction** — Often fully automated
- **Full headless support** — Designed for automation
- **Clear inputs/outputs** — Well-defined contract
- **May have CLI integration** — Scripts and tools

### When to Create a Utility Skill

Create a utility skill when you need:

- A simple transformation or generation task
- Automation support (CI/CD, scripts)
- Single-purpose functionality
- Minimal user interaction
- Integration with external tools

### Utility Skill Structure

```yaml
---
name: paw-tools-{utility-name}
description: "Trigger phrases. Use when user requests X, Y, Z."
---

# Utility Name

## Overview
Brief description of what the utility does.

**Args:** Accepts `--headless` / `-H` for non-interactive execution.

**Output:** Description of artifacts produced.

## On Activation
Load configuration and detect mode.

## Prerequisites
Required tools, environment, or state.

## Workflow
Sequential steps to complete the task.

## Output Artifacts
| Artifact | Location |
|----------|----------|
| File type | Path |

## Scripts
- `./scripts/script-name.py` — Purpose
```

### Examples

| Skill | Module | Purpose |
|-------|--------|---------|
| `paw-tools-release` | Tools | Release automation (version bump, changelog, git tag, GitHub release) |
| `paw-tools-presentation` | Tools | McKinsey-style HTML presentation generator |

### Key Patterns

#### Prerequisites Check

Utilities verify requirements before proceeding:

```markdown
## Prerequisites

Before starting, verify:

1. **Git repository** — Must be in a git repository
2. **GitHub CLI** — `gh` must be installed and authenticated
3. **Clean working tree** — Abort if uncommitted changes exist

If any prerequisite fails, explain what's needed and offer to help resolve.
```

#### Script Integration

Utilities often include helper scripts:

```markdown
## Scripts

- `./scripts/detect_version_files.py` — Finds and parses version files
- `./scripts/parse_commits.py` — Parses conventional commits for changelog

Run `<script> --help` for usage details.
```

---

## Decision Matrix

Use this matrix to decide which skill type to create:

| Your Need | Skill Type |
|-----------|------------|
| Persistent persona with memory | Agent |
| Coordination of multiple skills | Agent (Coordinator) |
| Multi-turn conversations | Agent |
| Judgment-based decisions | Agent |
| Sequential pipeline with stages | Workflow |
| Clear input → output process | Workflow |
| Repeatable process with gates | Workflow |
| Automation with optional interaction | Workflow or Utility |
| Single focused task | Utility |
| Minimal interaction | Utility |
| CI/CD integration | Utility |

## Hybrid Considerations

Some skills blur the lines between types:

| Example | Why It's Hybrid |
|---------|-----------------|
| `paw-mkt-sostac` | Workflow with HITL gates — stages are deterministic, but phases require human approval |
| `paw-cra-agent-designer` | Agent with production capabilities — has identity but also produces deliverables |
| `paw-tools-presentation` | Utility with stages — single-purpose but uses stage-based execution |

When in doubt:
- **Need memory/persistence?** → Agent
- **Need persona/identity?** → Agent
- **Need stages with progression?** → Workflow
- **Need minimal interaction?** → Utility

## Do's and Don'ts

### Do's

- Create an Agent when you need coordination across multiple skills
- Create a Workflow when the process is deterministic and repeatable
- Create a Utility when the task is focused and automatable
- Support `--headless` mode for Workflows and Utilities
- Define clear output contracts for all skill types
- Use progressive disclosure for extensive knowledge bases

### Don'ts

- Don't create an Agent for simple, stateless operations
- Don't give Utilities a persona or identity section
- Don't skip HITL gates in Workflows that require human judgment
- Don't bulk-load all framework files — use progressive disclosure
- Don't create overlapping skills — consolidate or split clearly