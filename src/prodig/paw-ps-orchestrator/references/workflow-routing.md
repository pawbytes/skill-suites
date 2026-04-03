# Workflow Routing

## Purpose

Define when to trigger workflows versus routing to agents.

## Available Workflows

| Workflow | Skill Name | Trigger | Purpose |
|----------|------------|---------|---------|
| Research to Brief | paw-ps-research-to-brief | Synthesize research into brief | Convert research findings to product brief |
| Concept to Plan | paw-ps-concept-to-product-plan | Turn brief into plan | Create executor-ready product plan |
| Package Assembler | paw-ps-product-package-assembler | Bundle artifacts | Package product into final bundle |
| Publish Ready Check | paw-ps-publish-ready-check | Quality review | Verify product readiness |

## When to Use Workflows vs Agents

### Use Workflow When:
- Clear input → output transformation
- Process is repeatable and standardized
- Minimal judgment required
- User wants efficiency over exploration
- Synthesis of multiple inputs needed

### Use Agent When:
- Judgment-based decisions needed
- Exploration or discovery required
- Multi-turn conversation expected
- Context needs to be built interactively
- User wants guidance through ambiguity

## Workflow Triggers

### paw-ps-research-to-brief

**Inputs required:**
- Research findings (market-intelligence.md)
- Audience insights (audience-intelligence.md) - optional but recommended
- Product concept (product-context.md)

**Outputs:**
- Product brief
- Updated product-decisions.md

**When to trigger:**
- User has completed research and audience
- User says "create a brief from my research"
- After research agent completes with sufficient findings
- Headless mode: when research stage is complete

**Prerequisite check:**
```markdown
Before triggering:
1. Check market-intelligence.md exists and has content
2. Check product-context.md has a defined concept
3. Optionally check audience-intelligence.md
```

---

### paw-ps-concept-to-product-plan

**Inputs required:**
- Product brief (from product-decisions.md or separate brief file)
- Chosen product family (knowledge, template, software, service)

**Outputs:**
- Product plan/spec package
- Executor handoff bundle

**When to trigger:**
- User has an approved product brief
- User says "create an execution plan"
- After strategist completes with a brief
- Ready to move to execution phase

**Prerequisite check:**
```markdown
Before triggering:
1. Verify product brief exists and is approved
2. Confirm product family is decided
3. Check strategist has completed definition
```

---

### paw-ps-product-package-assembler

**Inputs required:**
- Product artifacts (from execution phase)
- Output standards (output-standards.md)
- Product type guidance

**Outputs:**
- Packaged product bundle
- Completeness check report

**When to trigger:**
- User has execution artifacts ready
- User says "package my product"
- After executor completes
- Preparing for readiness review

**Prerequisite check:**
```markdown
Before triggering:
1. Check artifacts directory has relevant files
2. Verify output-standards.md exists
3. Confirm execution phase is substantially complete
```

---

### paw-ps-publish-ready-check

**Inputs required:**
- Packaged product bundle
- Output standards
- Product type requirements

**Outputs:**
- Readiness report
- Gap analysis
- Final verdict (production-ready / publish-ready / sellable-ready)

**When to trigger:**
- User has a packaged product
- User asks "is this ready to sell?"
- After packaging workflow completes
- Final quality gate

**Prerequisite check:**
```markdown
Before triggering:
1. Verify product bundle exists
2. Check output-standards.md is defined
3. Confirm all artifacts are in place
```

## Workflow Sequences

### Full Product Synthesis Sequence

```text
Research + Audience
        │
        ▼
┌─────────────────────┐
│ research-to-brief   │
│    workflow         │
└─────────────────────┘
        │
        ▼
   Product Brief
        │
        ▼
┌─────────────────────┐
│ concept-to-plan     │
│    workflow         │
└─────────────────────┘
        │
        ▼
  Execution Plan
        │
        ▼
    [Executor]
        │
        ▼
┌─────────────────────┐
│ package-assembler   │
│    workflow         │
└─────────────────────┘
        │
        ▼
  Product Bundle
        │
        ▼
┌─────────────────────┐
│ publish-ready-check │
│    workflow         │
└─────────────────────┘
        │
        ▼
  Readiness Report
```

### Headless Mode Sequences

For `--headless` execution, workflows can be chained:

**Full synthesis chain:**
```bash
--headless --chain research-to-brief,concept-to-plan
```

**Packaging chain:**
```bash
--headless --chain package-assembler,publish-ready-check
```

## Workflow Invocation

### Interactive Mode

When invoking a workflow interactively:

1. Explain what the workflow will do
2. Confirm the user wants to proceed
3. Invoke via Skill tool
4. Present results and recommendations

**Example:**
"You've completed research for your AI course. I'll run the research-to-brief workflow to synthesize everything into a product brief. This will:
- Consolidate your research findings
- Identify key decisions
- Create a structured brief

Proceed?"

### Headless Mode

For headless invocation:

1. Verify prerequisites programmatically
2. Invoke workflow with `--headless` flag
3. Handle outputs automatically
4. Update memory and continue

**Example invocation:**
```bash
/paw-ps-research-to-brief --headless
```

## Workflow-Agent Coordination

### Before Workflow: Agent Preparation

Agents should prepare clean inputs:
- Research agent ensures market-intelligence.md is complete
- Audience agent ensures audience-intelligence.md is complete
- Strategist ensures product brief is clear

### After Workflow: Agent Review

Agents may review workflow outputs:
- Strategist reviews brief from research-to-brief
- Executor reviews plan from concept-to-plan
- Orchestrator reviews readiness report

### Workflow Calls Agent

Some workflows may need agent support:
- Package assembler might request missing artifacts
- Readiness check might route gaps to executor