# Execution Handoff

Prepare executor-ready instructions that transform product decisions into clear execution direction.

## Purpose

Create unambiguous, complete instructions that enable executors to implement the product without requiring additional clarification. A good handoff eliminates guesswork.

## Required Inputs

| Input | Source | Purpose |
|-------|--------|---------|
| Product Brief | `curated/product-decisions.md` | Value proposition and success criteria |
| Scope Map | `curated/product-decisions.md` | v1 features and boundaries |
| Packaging Recommendation | `curated/product-decisions.md` | Tier structure and pricing |

## Handoff Framework

### 1. Context Transfer

Ensure executors understand the WHY:

**Strategic Context:**
- What problem are we solving?
- Who are we solving it for?
- How will we measure success?
- What are the key constraints?

**Decision Context:**
- What key decisions have been made?
- What alternatives were considered?
- What trade-offs were accepted?

### 2. Specification Clarity

For each feature, provide complete specifications:

**Feature Specification Template:**

| Element | Content |
|---------|---------|
| Feature ID | Unique identifier |
| Name | Clear feature name |
| Description | What it does (user perspective) |
| Acceptance Criteria | When it's done (testable) |
| Technical Notes | Implementation guidance |
| Dependencies | What it depends on |
| Priority | Must/Should/Could |
| Estimated Effort | Size indication |
| Risks | Known risks or complexity |

### 3. Boundary Clarity

Explicitly state constraints and non-goals:

**Constraints:**
- Technical constraints (platform, performance, security)
- Business constraints (timeline, budget, resources)
- Design constraints (brand, UX patterns)
- External constraints (compliance, integrations)

**Non-Goals:**
- Features explicitly out of scope
- Segments not being served
- Problems not being solved
- Quality attributes not prioritized

### 4. Quality Gates

Define what "done" looks like:

**Completion Criteria:**
- All acceptance criteria met
- Quality standards satisfied
- Documentation complete
- Testing requirements fulfilled

**Review Gates:**
- Design review requirements
- Code review requirements
- User acceptance requirements
- Stakeholder sign-off requirements

### 5. Risk Communication

Transfer known risks to executors:

**Technical Risks:**
- Complexity concerns
- Dependency risks
- Performance risks
- Integration risks

**Execution Risks:**
- Timeline risks
- Resource risks
- Scope creep risks
- Quality risks

## Output: Executor Handoff Spec

Produce a structured handoff document:

```markdown
# Executor Handoff Spec: {Product Name} v1

## Document Control
| Element | Value |
|---------|-------|
| Version | {version} |
| Date | {date} |
| Author | Strategist |
| Status | {Draft/Ready/Approved} |

## Strategic Context

### Problem Statement
{What problem are we solving}

### Target Users
{Who we are building for}

### Success Metrics
| Metric | Target | Priority |
|--------|--------|----------|
| {metric} | {target} | H/M/L |

### Key Decisions
| Decision | Rationale |
|----------|-----------|
| {decision} | {why} |

## Scope Summary

**v1 Includes:**
- {summary of included features}

**v1 Excludes:**
- {summary of excluded features}

## Feature Specifications

### {Feature ID}: {Feature Name}

**Description:**
{What it does from user perspective}

**Acceptance Criteria:**
- [ ] {criterion 1}
- [ ] {criterion 2}
- [ ] {criterion 3}

**Technical Notes:**
{Implementation guidance}

**Dependencies:**
- {dependency 1}
- {dependency 2}

**Priority:** {Must/Should/Could}
**Effort Estimate:** {size}

**Risks:**
| Risk | Likelihood | Impact | Mitigation |
|------|------------|--------|------------|
| {risk} | H/M/L | H/M/L | {mitigation} |

{Repeat for each feature}

## Constraints

### Technical Constraints
| Constraint | Rationale |
|------------|-----------|
| {constraint} | {why} |

### Business Constraints
| Constraint | Rationale |
|------------|-----------|
| {constraint} | {why} |

### Design Constraints
| Constraint | Rationale |
|------------|-----------|
| {constraint} | {why} |

## Non-Goals

| Non-Goal | Rationale |
|----------|-----------|
| {non-goal} | {why excluded} |

## Quality Gates

### Completion Criteria
- [ ] All acceptance criteria satisfied
- [ ] {additional criteria}

### Review Requirements
| Review Type | Required | Approver |
|-------------|----------|----------|
| {type} | Yes/No | {role} |

## Open Questions
| Question | Owner | Due |
|----------|-------|-----|
| {question} | {who} | {when} |

## Appendix

### Reference Documents
- Product Brief: {link/path}
- Scope Map: {link/path}
- Packaging Recommendation: {link/path}

### Glossary
| Term | Definition |
|------|------------|
| {term} | {definition} |
```

## Process

1. Load all product decisions
2. Extract strategic context
3. Create feature specifications
4. Document constraints and non-goals
5. Define quality gates
6. Identify and communicate risks
7. Produce handoff spec
8. Write to `curated/product-decisions.md`
9. Update `curated/product-context.md`
10. Log activity in daily file

## Quality Check

Before finalizing, verify:

- [ ] Strategic context is complete and clear
- [ ] Every feature has acceptance criteria
- [ ] Constraints are explicit and unambiguous
- [ ] Non-goals prevent scope creep
- [ ] Quality gates are testable
- [ ] Risks are communicated
- [ ] A new team member could execute from this spec
- [ ] No critical information is assumed or implied