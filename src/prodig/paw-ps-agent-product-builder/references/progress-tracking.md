# Progress Tracking

## Purpose

Track product progress across the creation journey and surface status to users.

## Progress Indicators

### Stage-Based Progress

Track which stages are complete:

```
Progress: ████░░░ 4/7 stages (57%)

✓ Discovery     — Concept defined
✓ Research      — Competitors analyzed
✓ Audience      — Personas created
✓ Strategy      — Brief complete (in progress)
○ Execution     — Not started
○ Packaging     — Not started
○ Readiness     — Not started
```

### Stage Status Values

| Status | Meaning |
|--------|---------|
| `pending` | Not yet started |
| `in_progress` | Currently being worked on |
| `blocked` | Waiting for dependency |
| `complete` | Finished and verified |

## Tracking Files

### Product Context Progress

Update product-context.md with stage tracking:

```markdown
## Stage Progress

| Stage | Status | Started | Completed | Key Outputs |
|-------|--------|---------|-----------|-------------|
| Discovery | complete | 2024-01-15 | 2024-01-15 | Concept doc |
| Research | complete | 2024-01-16 | 2024-01-18 | Competitor matrix |
| Audience | complete | 2024-01-19 | 2024-01-20 | 3 personas |
| Strategy | in_progress | 2024-01-21 | - | Brief draft |
| Execution | pending | - | - | - |
| Packaging | pending | - | - | - |
| Readiness | pending | - | - | - |
```

### Index Summary

Update index.md with quick status:

```markdown
## Active Products

| Product | Stage | Progress | Last Active | Next Step |
|---------|-------|----------|-------------|-----------|
| AI Course | Strategy | 57% | Today | Complete brief |
| Templates | Execution | 71% | Yesterday | Finish templates |
```

## Progress Queries

### User Asks for Status

When user says "status" or "where am I":

```markdown
## Product: {name}

**Stage:** {current stage}
**Progress:** {percentage} ({X}/7 stages)

### Completed
✓ {stage 1}: {brief note}
✓ {stage 2}: {brief note}

### Current
► {current stage}: {what's happening}

### Upcoming
○ {next stage 1}
○ {next stage 2}

**Recommended next action:** {specific action}
```

### Progress Report Command

For `--headless:status`:

```markdown
# Prodig Suites Status Report

**Generated:** {timestamp}

## Active Products: 2

### AI Course for Beginners
- **Stage:** Strategy (in_progress)
- **Progress:** 4/7 stages (57%)
- **Last activity:** Brief draft created
- **Next:** Complete scope definition

### Notion Templates Pack
- **Stage:** Execution (in_progress)  
- **Progress:** 5/7 stages (71%)
- **Last activity:** 8/12 templates complete
- **Next:** Finish remaining templates

## Blocked Items
- None

## Recent Decisions
- AI Course: Chose video format over text
- Templates: Scoped to 12 templates for v1
```

## Milestones

### Stage Completion Milestones

Each stage has completion criteria:

| Stage | Milestone | Verification |
|-------|-----------|--------------|
| Discovery | Concept defined | product-context.md has clear concept |
| Research | Research complete | market-intelligence.md populated |
| Audience | Audience defined | audience-intelligence.md has personas |
| Strategy | Brief approved | product-decisions.md has brief decision |
| Execution | Artifacts complete | Artifacts directory has all needed files |
| Packaging | Bundle assembled | Product bundle exists |
| Readiness | Quality verified | Readiness report shows pass |

### Celebrating Progress

Acknowledge milestones to maintain momentum:

```markdown
🎉 **Milestone reached!**

Research stage complete. You now have:
- {X} competitors analyzed
- {Y} market gaps identified
- Key demand signals documented

Ready for audience discovery?
```

## Blocking Issues

### Tracking Blocks

When a stage is blocked:

```markdown
| Stage | Status | Block Reason |
|-------|--------|--------------|
| Execution | blocked | Waiting for design assets |
```

### Block Resolution

1. Identify what's needed to unblock
2. Route to appropriate agent or action
3. Update status when resolved

```markdown
**Blocked:** Execution waiting for brand guidelines

**Resolution options:**
1. Create brand guidelines now (→ Designer)
2. Proceed with minimal branding
3. Skip execution until resolved

What would you like to do?
```

## Progress Persistence

### Daily Log Entries

Log significant progress changes:

```markdown
### 14:32 - paw-ps-agent-product-builder

**Milestone:** Research complete for {product}

**Findings:**
- Identified 5 key competitors
- Demand signals strong in {segment}
- Gap: {opportunity}

**Progress:** 2/7 → 3/7 stages

**Next:** Audience discovery recommended
```

### Stage Transitions

When moving between stages:

1. Update product-context.md stage field
2. Update stage progress table
3. Log transition in daily file
4. Update index.md summary

## Historical Progress

### Looking Back

To see historical progress:

```markdown
## Progress History for {product}

**Week of Jan 15:**
- Started: Discovery
- Completed: Discovery, Research
- Progress: 0% → 43%

**Week of Jan 22:**
- Started: Audience (was in_progress)
- Completed: Audience, Strategy
- Progress: 43% → 71%
```

### Velocity Tracking

Track how fast stages complete:

```markdown
**Average stage duration:**
- Discovery: 1 day
- Research: 2-3 days
- Audience: 1-2 days
- Strategy: 1-2 days
- Execution: 3-5 days
- Packaging: 1 day
- Readiness: 1 day

**Estimated remaining:** {days} for {product}
```