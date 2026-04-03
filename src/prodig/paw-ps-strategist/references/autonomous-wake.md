# Autonomous Wake

Execute headless tasks without user interaction. Used when `--headless` or `-H` flag is passed.

## Wake Sequence

### 1. Environment Check

Verify required resources:

| Check | Action if Missing |
|-------|-------------------|
| Sidecar memory exists | Create structure |
| Product context exists | Initialize from flags |
| Intelligence files exist | Return error with missing inputs |
| Output directory writable | Return error |

### 2. Task Determination

Parse the task from invocation:

| Flag | Task | Required Inputs |
|------|------|-----------------|
| `--headless:shape` | Product shaping | market-intelligence.md, audience-intelligence.md |
| `--headless:scope` | Scope design | product-decisions.md (brief) |
| `--headless:package` | Packaging logic | product-decisions.md (brief, scope) |
| `--headless:handoff` | Execution handoff | product-decisions.md (brief, scope, packaging) |
| `--headless` (no task) | Full pipeline | All intelligence files |

### 3. Input Validation

Before executing, verify all required inputs exist:

```markdown
## Input Check

| Required | Status | Path |
|----------|--------|------|
| market-intelligence.md | ✓/✗ | {path} |
| audience-intelligence.md | ✓/✗ | {path} |
| product-context.md | ✓/✗ | {path} |

**Result:** {Proceed/Halt with error}
```

If inputs missing:
1. Write error to daily log
2. Return structured error response
3. Exit gracefully

### 4. Execute Task

Load appropriate capability reference and execute:

**For shaping:**
1. Load `./references/product-shaping.md`
2. Read intelligence files
3. Generate product brief
4. Write to `product-decisions.md`
5. Update `product-context.md`
6. Log activity

**For scoping:**
1. Load `./references/scope-design.md`
2. Read product brief
3. Generate scope map
4. Append to `product-decisions.md`
5. Log activity

**For packaging:**
1. Load `./references/packaging-logic.md`
2. Read product brief and scope
3. Generate packaging recommendation
4. Append to `product-decisions.md`
5. Log activity

**For handoff:**
1. Load `./references/execution-handoff.md`
2. Read all decisions
3. Generate handoff spec
4. Append to `product-decisions.md`
5. Log activity

**For full pipeline:**
Execute all four in sequence.

### 5. Output Report

Produce structured output for headless caller:

```markdown
# Headless Execution Report

## Task: {task name}

## Status: {Success/Failed}

## Inputs Consumed
- {file 1}
- {file 2}

## Outputs Produced
| File | Path |
|------|------|
| {output} | {path} |

## Key Decisions
1. {decision}
2. {decision}

## Errors
{Any errors encountered}

## Duration
{Execution time}

## Next Steps
1. {recommended action}
```

## Error Codes

| Code | Meaning | Action |
|------|---------|--------|
| 0 | Success | Return outputs |
| 1 | Missing inputs | List required files |
| 2 | Validation failed | Detail validation errors |
| 3 | Write failed | Detail write error |
| 4 | Unknown task | List valid tasks |

## Silent Mode Rules

- No user prompts
- No questions — make reasonable defaults
- Log everything to daily file
- Return structured report
- Exit cleanly on error