# Autonomous Wake Protocol

## Purpose

Enable headless execution for the Software Executor when `--headless` or `-H` flag is passed.

## Activation Sequence

When headless mode is triggered:

### 1. Load Context

```
Read in order:
1. {project-root}/.pawbytes/prodig-suites/memory/paw-ps-sidecar/index.md
2. {project-root}/.pawbytes/prodig-suites/memory/paw-ps-sidecar/curated/product-context.md
3. {project-root}/.pawbytes/prodig-suites/memory/paw-ps-sidecar/curated/audience-intelligence.md
4. {project-root}/.pawbytes/prodig-suites/memory/paw-ps-sidecar/curated/market-intelligence.md
5. {project-root}/.pawbytes/prodig-suites/memory/paw-ps-sidecar/curated/output-standards.md
```

### 2. Determine Task

Based on named task argument or infer from context:

| Named Task | Action |
|------------|--------|
| `--headless:features` | Execute feature definition |
| `--headless:mvp` | Execute MVP scoping |
| `--headless:prd` | Generate PRD-lite |
| `--headless` (no task) | Assess and recommend next action |

### 3. Validate Inputs

Check for required inputs based on task:

**Feature Definition requires:**
- product-context.md (present/absent)
- audience-intelligence.md (present/absent)

**User Flow Shaping requires:**
- Feature specifications (previous artifact or will create)

**MVP Scoping requires:**
- Feature specifications
- User flows

**PRD-Lite requires:**
- MVP definition
- Technical context (or will create)

### 4. Execute Task

Run the appropriate capability without user interaction:

1. Load capability reference
2. Execute process steps
3. Generate artifacts
4. Write to product workspace
5. Update daily log

### 5. Report Results

Output a summary:

```markdown
# Software Executor: Headless Execution Complete

**Task**: [Task performed]
**Product**: [Product name]
**Duration**: [Elapsed time]

## Outputs Created
| Artifact | Path |
|----------|------|
| [Artifact 1] | [Path] |
| [Artifact 2] | [Path] |

## Decisions Made
- [Decision 1]
- [Decision 2]

## Next Recommended Actions
1. [Action 1]
2. [Action 2]

## Status
[Ready for review / Needs input: {specific input needed}]
```

## Error Handling

If required inputs are missing:

```markdown
# Software Executor: Headless Execution Blocked

**Task**: [Attempted task]
**Blocker**: [Missing input]

**Required**: [What's needed]
**Location**: [Where it should be]

**Options**:
1. Run [appropriate agent] first
2. Provide input via: [file path]
3. Use interactive mode for clarification
```

## Example Execution

```bash
# Named task: feature definition
/paw-ps-software-executor --headless:features

# Named task: MVP scoping
/paw-ps-software-executor --headless:mvp

# Named task: PRD-lite
/paw-ps-software-executor --headless:prd

# Auto-assess
/paw-ps-software-executor --headless
```

## Quality Gates

Before completing headless execution:

- [ ] All required inputs were present
- [ ] Artifacts were written to correct location
- [ ] Daily log was updated
- [ ] No ambiguous decisions were made (or flagged)
- [ ] Next steps are clearly defined