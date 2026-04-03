# Stage 4: Prepare Handoff

## Objective

Format and package the execution-ready handoff for the specific executor.

## Process

### Step 1: Create Handoff Document

Generate executor-specific handoff:

```markdown
# Executor Handoff: [Product Name]

## Quick Start

**Executor:** [executor name]
**Product:** [product name]
**Family:** [product family]
**Priority:** [P1/P2/P3]

**Start with:** [first action executor should take]

---

## Your Mission

[Single paragraph describing what you need to build]

---

## Source Materials

| Document | Path | Purpose |
|----------|------|---------|
| Product Plan | [path] | Full execution details |
| Product Brief | [path] | Original decisions |
| Product Context | [path] | Background context |

---

## Execution Parameters

### Scope Boundaries
- **Build this:** [what to create]
- **Do NOT build:** [what to exclude]

### Quality Requirements
- [Requirement 1]
- [Requirement 2]

### Constraints
- Timeline: [if specified]
- Resources: [if specified]
- Dependencies: [if any]

---

## Deliverables Checklist

- [ ] [Deliverable 1]
- [ ] [Deliverable 2]
- [ ] [Deliverable 3]

---

## Completion Criteria

This handoff is complete when:
1. [Criterion 1]
2. [Criterion 2]
3. [Criterion 3]

---

## Questions?

If you need clarification on:
- **Scope** → Check product plan section [X]
- **Technical details** → Check product plan section [Y]
- **Context** → Check product-context.md

If still unclear, escalate to coordinator.
```

### Step 2: Create Executor Command

Generate the command for launching the executor:

## Launch Command

```bash
/paw-ps-[executor-type]-executor --headless
```

Or with a specific task:

```bash
/paw-ps-knowledge-executor --headless:course
/paw-ps-template-executor --headless:templates
/paw-ps-software-executor --headless:mvp
/paw-ps-service-executor --headless:delivery
```

### Step 3: Update Product Context

Append to `product-context.md`:

```markdown
## Planning Complete

**Date:** [date]
**Plan location:** `.pawbytes/prodig-suites/plans/{product-slug}/plan.md`
**Handoff location:** `.pawbytes/prodig-suites/plans/{product-slug}/handoff.md`
**Assigned executor:** [executor name]

### Ready For
- [ ] Execution by assigned executor
- [ ] Review by stakeholder
- [ ] Queue for scheduled build
```

### Step 4: Save Handoff Bundle

Save to: `.pawbytes/prodig-suites/plans/{product-slug}/handoff.md`

### Step 5: Create Execution Checklist (Optional)

For complex products, create execution checklist:

```markdown
# Execution Checklist: [Product Name]

## Pre-Execution
- [ ] All source materials accessible
- [ ] Environment/tools ready
- [ ] Dependencies resolved

## During Execution
- [ ] Follow plan sequence
- [ ] Log progress in product-context.md
- [ ] Flag blockers immediately

## Post-Execution
- [ ] All deliverables created
- [ ] Self-review completed
- [ ] Documentation updated
- [ ] Ready for review
```

## Output Structure

```text
.pawbytes/prodig-suites/plans/{product-slug}/
├── plan.md           # Full execution plan
├── handoff.md        # Executor-ready instructions
└── checklist.md      # Execution checklist (if complex)
```

## Output

```markdown
## Handoff Complete

**Plan saved to:** `.pawbytes/prodig-suites/plans/{product-slug}/plan.md`
**Handoff saved to:** `.pawbytes/prodig-suites/plans/{product-slug}/handoff.md`
**Product context updated:** Yes

### Next Step
Execute: `/paw-ps-[executor-type]-executor --headless`

### Summary
- Product: [name]
- Executor: [assigned executor]
- Deliverables: [count] items
- Estimated complexity: [rating]
```

## Progression Condition

Handoff bundle is complete and self-contained. Executor has all information needed to begin work. Product context is updated with plan references.