# Autonomous Wake

Protocol for headless/autonomous execution when `--headless` or `-H` flag is passed.

## Purpose

Enable fully autonomous execution of knowledge product creation without user interaction, following a structured wake sequence to gather context and complete the specified task.

## Wake Sequence

When operating in headless mode, follow this sequence:

### 1. Load Configuration

Read configuration files in order:

```
1. {project-root}/.pawbytes/config/config.yaml
2. {project-root}/.pawbytes/config/config.user.yaml
```

Extract and apply:
- `{user_name}` — for personalization
- `{communication_language}` — for output language
- `{document_output_language}` — for generated content

### 2. Load Memory Index

Read the sidecar memory index:

```
{project-root}/.pawbytes/prodig-suites/memory/paw-ps-sidecar/index.md
```

Identify:
- Active product context
- Current artifacts in progress
- Recent activity

### 3. Load Required Inputs

Load all input files needed for the task:

| Input | Path |
|-------|------|
| Product Context | `curated/product-context.md` |
| Audience Intelligence | `curated/audience-intelligence.md` |
| Output Standards | `curated/output-standards.md` |
| Knowledge Products Guidance | `curated/product-types/knowledge-products.md` |

If critical inputs are missing, log the error to daily file and exit with clear message about what's needed.

### 4. Determine Task Type

Parse the headless task argument:

| Argument | Task Type | Load Reference |
|----------|-----------|----------------|
| `--headless` (no task) | Auto-detect from context | N/A |
| `--headless:course` | Course creation | `course-creation.md` |
| `--headless:ebook` | Ebook/guide creation | `ebook-creation.md` |
| `--headless:membership` | Membership design | `membership-design.md` |

### 5. Auto-Detect Logic

If no specific task is provided, auto-detect based on:

1. **Check for explicit product type** in `product-context.md`
2. **Check for partial artifacts** — is there an outline but no content?
3. **Check for explicit request** in the activation message
4. **Default to prompt** — if unclear, output what's needed and exit

### 6. Execute Task

Follow the appropriate capability reference:

1. Load the task-specific reference
2. Execute the process phases
3. Write artifacts to the appropriate location
4. Update memory index
5. Log activity to daily file

## Output Protocol

### Success Output

On successful completion, output:

```markdown
## Task Complete

**Task**: {task type}
**Product**: {product name}
**Artifacts Created**: {count} files

### Files Written
- {file path 1}
- {file path 2}

### Key Decisions
- {decision 1}
- {decision 2}

### Next Steps
- {recommended next action}
```

### Error Output

On failure or missing inputs, output:

```markdown
## Task Incomplete

**Reason**: {why the task could not be completed}

**Missing Inputs**:
- {input 1}
- {input 2}

**Resolution**:
- {what needs to happen before this task can complete}

**Routing**: {which agent should handle this first}
```

## Error Handling

### Missing Inputs

If required inputs are missing:

1. Log to daily file: "Headless task incomplete: missing {input}"
2. Output clear message about what's needed
3. Route to appropriate agent for resolution
4. Exit gracefully (don't create partial artifacts)

### Ambiguous Context

If context is insufficient to determine task:

1. Log to daily file: "Headless task ambiguous: {reason}"
2. Output what was found and what's needed
3. Request clarification (even in headless mode, clarity is required)
4. Exit gracefully

### Creation Conflicts

If artifacts already exist:

1. Check for existing work
2. Decide: extend existing or create new version
3. If extending, read existing first
4. If creating new version, version the filename
5. Never overwrite without intention

## Headless Execution Checklist

Before executing headlessly:

- [ ] Configuration loaded
- [ ] Memory index read
- [ ] All required inputs present
- [ ] Task type determined
- [ ] Appropriate reference loaded
- [ ] Output location verified
- [ ] Ready to execute

## Logging

All headless executions are logged to daily file:

```markdown
## Headless Execution: {YYYY-MM-DD HH:MM}

**Task**: {task type}
**Status**: {success/failure}
**Duration**: {approximate time}
**Artifacts**: {count} files
**Notes**: {any relevant notes}
```

## Recovery

If a headless execution is interrupted:

1. Check daily log for last recorded activity
2. Check artifacts folder for partial outputs
3. Resume from last completed phase
4. Log recovery in daily file