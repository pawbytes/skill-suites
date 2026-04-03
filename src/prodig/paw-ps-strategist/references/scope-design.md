# Scope Design

Decide what belongs in v1 — creating a focused, shippable, valuable first release.

## Purpose

Transform the product brief into a concrete v1 scope that balances value delivery with execution reality. The goal is to ship something valuable, not to ship everything.

## Required Inputs

| Input | Source | Purpose |
|-------|--------|---------|
| Product Brief | `curated/product-decisions.md` | Value proposition and boundaries |
| Product Context | `curated/product-context.md` | Constraints and priorities |
| Market Intelligence | `curated/market-intelligence.md` | Competitive feature landscape |

## Scoping Framework

### 1. Feature Inventory

List all potential features from multiple sources:

**From Value Proposition:**
- Features required to deliver core value
- Features that enable differentiation

**From User Needs:**
- Features that address primary pain points
- Features that enable key user tasks

**From Competitive Analysis:**
- Table stakes features (must have)
- Differentiation opportunities (should have)
- Nice-to-have features (could have)

### 2. Feature Prioritization

Apply a rigorous prioritization framework:

**MoSCoW with Rationale:**

| Priority | Definition | Criteria |
|----------|------------|----------|
| Must Have | Non-negotiable for v1 | Core value delivery, differentiation |
| Should Have | Important but not critical | Significant value, could defer |
| Could Have | Nice to have | Limited value, easy to add |
| Won't Have | Explicitly excluded | Low value, high effort, or later |

**Prioritization Matrix:**

For each feature, score on two dimensions:

| Value Score | Criteria |
|-------------|----------|
| 5 | Essential to core value proposition |
| 4 | Significant contribution to value |
| 3 | Moderate contribution to value |
| 2 | Minor contribution to value |
| 1 | Negligible contribution to value |

| Effort Score | Criteria |
|--------------|----------|
| 1 | Simple, quick to implement |
| 2 | Moderate complexity |
| 3 | Significant complexity |
| 4 | High complexity |
| 5 | Very high complexity |

**Priority = Value / Effort** (higher = better candidate for v1)

### 3. v1 Boundary Definition

Define the explicit boundary of v1:

**v1 Scope Statement:**
"v1 will {deliver specific value} for {specific segment} by {date} with {feature set}."

**v1 Feature Set:**
List all Must Have features with acceptance criteria:

| Feature | Acceptance Criteria | Dependencies |
|---------|---------------------|--------------|
| {feature} | {criteria} | {dependencies} |

**v1 Non-Goals:**
Explicitly state what v1 will NOT include:

| Feature | Why Deferred | Planned For |
|---------|--------------|-------------|
| {feature} | {rationale} | v{version} |

### 4. Risk Assessment for v1

Identify scope-specific risks:

**Complexity Risk:** Which features introduce significant complexity?
**Dependency Risk:** What external factors could block v1?
**Quality Risk:** How do we ensure v1 is production-ready?
**Timeline Risk:** Is the scope achievable in the target timeline?

## Output: Scope Map

Produce a structured scope document:

```markdown
# Scope Map: v1

## v1 Scope Statement
v1 will {value} for {segment} by {date} with {features}.

## Feature Inventory

### Must Have (v1)
| ID | Feature | Acceptance Criteria | Effort | Priority Score |
|----|---------|---------------------|--------|----------------|
| M1 | {feature} | {criteria} | {effort} | {score} |

### Should Have (v1 Contingent)
| ID | Feature | Acceptance Criteria | Effort | Priority Score |
|----|---------|---------------------|--------|----------------|
| S1 | {feature} | {criteria} | {effort} | {score} |

### Could Have (Post-v1)
| ID | Feature | Acceptance Criteria | Effort | Priority Score |
|----|---------|---------------------|--------|----------------|
| C1 | {feature} | {criteria} | {effort} | {score} |

### Won't Have (Explicitly Excluded)
| ID | Feature | Rationale | Revisit |
|----|---------|-----------|---------|
| W1 | {feature} | {why excluded} | {when} |

## v1 Boundaries

**Includes:**
- {boundary 1}
- {boundary 2}

**Excludes:**
- {boundary 1}
- {boundary 2}

## Risk Assessment
| Risk | Likelihood | Impact | Mitigation |
|------|------------|--------|------------|
| {risk} | H/M/L | H/M/L | {mitigation} |

## Scope Validation Checklist
- [ ] All Must Have features are truly required for value delivery
- [ ] Scope is achievable with available resources
- [ ] Scope is specific enough to execute
- [ ] Exclusions are intentional and documented
```

## Process

1. Load product brief and context
2. Generate feature inventory from all sources
3. Apply prioritization framework
4. Define v1 boundaries
5. Assess scope-specific risks
6. Produce scope map
7. Write to `curated/product-decisions.md`
8. Update `curated/product-context.md`
9. Log activity in daily file

## Quality Check

Before finalizing, verify:

- [ ] Every Must Have feature is required for core value
- [ ] Scope is focused enough to ship
- [ ] Exclusions are intentional and documented
- [ ] Acceptance criteria are testable
- [ ] Scope can be understood by executors
- [ ] Timeline is realistic for the scope