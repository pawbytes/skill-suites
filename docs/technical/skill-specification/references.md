# Reference Documents

## Purpose

Reference documents are knowledge files loaded during skill execution. They contain capability implementations, best practices, and shared patterns.

## Types of References

| Type | Loading Pattern | Purpose |
|------|-----------------|---------|
| Capability | Matched on demand | Specific capability implementation |
| Shared Patterns | Loaded on activation | Common patterns across capabilities |
| Best Practices | Loaded on activation | Quality guidelines |
| Init | Loaded on first run | First-time setup guidance |
| Memory System | Loaded on activation | Memory discipline rules |

## Directory Structure

```
references/
├── capability-*.md         # Capability implementations
├── shared-patterns.md      # Common patterns
├── best-practices.md       # Quality guidelines
├── init.md                 # First-run initialization
├── memory-system.md        # Memory discipline
├── save-memory.md          # Memory persistence protocol
├── autonomous-wake.md      # Headless execution
└── frameworks/             # Progressive disclosure frameworks
    └── frameworks-index.csv
```

## Capability Files

Capability files define how to implement specific capabilities mentioned in the SKILL.md capabilities table.

### Naming Convention

```
capability-{name}.md
```

Examples:
- `capability-technical-seo.md`
- `capability-content-seo.md`
- `capability-local-seo.md`

### Capability File Structure

```markdown
# Capability Name

## Purpose
What this capability does.

## When to Use
Specific scenarios.

## Process

### Step 1: Preparation
What to prepare or read first.

### Step 2: Execution
The main workflow.

### Step 3: Output
What to produce and where to save it.

## Checklist
- [ ] Item 1
- [ ] Item 2

## Examples
Concrete examples.
```

### Example Capability File

```markdown
# Technical SEO Capability

## Purpose
Diagnose and fix technical issues affecting search visibility.

## When to Use
- Site audit requested
- Crawlability issues suspected
- Performance problems reported
- Quarterly health check

## Process

### Step 1: Gather Context
Read brand context and any existing audit history:
```
.pawbytes/marketing-suites/brands/{brand-slug}/brand-context.md
.pawbytes/marketing-suites/brands/{brand-slug}/channels/seo/
```

### Step 2: Run Diagnostics
1. Crawlability check
2. Indexation audit
3. Core Web Vitals test
4. Mobile-friendliness test

### Step 3: Prioritize Findings
Rate each issue P1/P2/P3 based on impact and effort.

### Step 4: Deliver Recommendations
Save to `.pawbytes/marketing-suites/brands/{brand-slug}/channels/seo/audits/`

## Output Format
- Executive summary
- Prioritized issue list
- Specific fix recommendations
- Expected impact per fix
```

## Shared Patterns

Shared patterns are loaded on every activation and contain common logic used across multiple capabilities.

### Example: shared-patterns.md

```markdown
# Shared Patterns

## Context Routing

Before any capability, determine the starting context:

### Blank Page Mode
No existing brand or campaign. Start fresh.

### Codebase Mode
Working with existing project files.

### Live URL Mode
Analyzing a live website.

## Pre-Flight Sequence

1. Load configuration from `.pawbytes/config/`
2. Check for active brand context
3. Verify required tools are available
4. Load relevant memory/session state

## File Resolution

Always use variables for paths:
- `{project-root}` — Project root
- `{brand-slug}` — Current brand identifier
- `{campaign-slug}` — Current campaign identifier
```

## Best Practices

Best practices files contain quality guidelines that apply to all outputs.

### Example: best-practices.md

```markdown
# Best Practices

## Output Quality

- Every recommendation must be actionable
- Include specific implementation steps
- Provide priority ratings (P1/P2/P3)
- Reference sources when applicable

## Communication

- Lead with impact
- Use bullet points for lists
- Include examples for clarity
- Summarize at the end

## File Management

- Always write outputs to resolved paths
- Use consistent naming conventions
- Include timestamps in filenames when relevant
- Never overwrite without confirmation
```

## Init Files

Init files handle first-time activation when no prior context exists.

### Example: init.md

```markdown
# First-Time Initialization

Welcome! This appears to be your first time using this skill.

## Setup Checklist

1. **Configuration** — Verify settings in `.pawbytes/config/`
2. **Brand Context** — Would you like to onboard a brand?
3. **Tool Verification** — Checking available tools...

## What I Can Do

Brief overview of capabilities.

## Getting Started

Suggest first actions for new users.
```

## Memory System Files

Memory system files define how agents persist and recall information.

### memory-system.md

Defines the memory architecture and discipline.

### save-memory.md

Protocol for persisting memory after significant changes.

```markdown
# Save Memory Protocol

## When to Save

- After brand onboarding
- After campaign creation
- After significant decisions
- Before session ends

## What to Save

- Active brand reference
- Recent work summary
- Pending items
- Key decisions made

## Where to Save

`.pawbytes/{module}/index.md`
```

## Autonomous Wake Files

For headless/non-interactive execution.

### Example: autonomous-wake.md

```markdown
# Autonomous Wake

When `--headless` or `-H` is passed, execute without interaction.

## Protocol

1. Load configuration silently
2. Parse task from arguments
3. Execute without prompts
4. Write output to resolved path
5. Return structured result

## Headless Output

Return JSON structure with:
- Status: success/failure
- Output path
- Summary
- Next recommended action
```

## Reference vs Framework

| Aspect | Reference | Framework |
|--------|-----------|-----------|
| Loading | Direct or on-demand | Progressive via CSV |
| Content | Capabilities, patterns | Methodologies |
| Index | No index file | Requires CSV index |
| Size | Any size | Optimized for selective load |
| Use case | Always-needed knowledge | Large domain knowledge bases |

## Best Practices

1. **One topic per file** — Keep references focused
2. **Clear headings** — Use H2 for main sections
3. **Include examples** — Concrete scenarios help understanding
4. **Define output** — What this reference produces
5. **Cross-reference** — Link to related references when helpful