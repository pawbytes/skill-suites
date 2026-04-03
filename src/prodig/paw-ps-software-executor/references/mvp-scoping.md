# MVP Scoping

## Outcome

Identify what is required for first delivery—a minimum viable product that delivers core value, validates assumptions, and establishes a foundation for iteration.

## Trigger

User requests MVP definition, scope minimum, first release, or "what should we build first?"

## Inputs Required

| Input | Source | Required |
|-------|--------|----------|
| Feature specifications | Previous artifact | Yes |
| User flows | Previous artifact | Yes |
| Product context | `curated/product-context.md` | Yes |
| Audience intelligence | `curated/audience-intelligence.md` | Yes |

## Process

### 1. Articulate Learning Goals

MVP is about learning, not feature completeness. Define what you need to learn:

```markdown
## Learning Goals

**Primary Question**: [What do we need to validate?]
**Success Indicator**: [What measurement would confirm this?]
**Timeframe**: [How long until we need to know?]

**Secondary Questions**:
1. [Question 2]
2. [Question 3]
```

**Common learning goals:**
- Will users pay for this solution?
- Does this solve the core problem?
- Is the user experience intuitive?
- What features do users actually use?
- What's the activation bottleneck?

### 2. Apply the MVP Filter

For each feature, ask:

| Question | Yes | No |
|----------|-----|-----|
| Does this directly validate our primary hypothesis? | Include | Consider cutting |
| Can we learn what we need without this? | Consider cutting | Include |
| Is this required for basic functionality? | Include | Consider cutting |
| Does this have significant technical debt risk? | Consider cutting | Include carefully |

### 3. Define MVP Feature Set

Create a definitive list of MVP features:

```markdown
## MVP Feature Set

### Core Features (Non-Negotiable)
These features are required for the MVP to function:

| Feature | Justification | Risk if Excluded |
|---------|---------------|------------------|
| [Feature 1] | [Why required] | [What breaks without it] |
| [Feature 2] | [Why required] | [What breaks without it] |

### Included Features
These features enhance MVP but have fallbacks:

| Feature | Fallback | Risk |
|---------|----------|------|
| [Feature 3] | [Workaround] | [Low/Medium] |
| [Feature 4] | [Workaround] | [Low/Medium] |

### Explicitly Excluded
These features are deferred post-MVP:

| Feature | Reason for Deferral | Planned Version |
|---------|---------------------|-----------------|
| [Feature 5] | [Why later] | [v1.1, v2.0, etc.] |
| [Feature 6] | [Why later] | [v1.1, v2.0, etc.] |
```

### 4. Create MVP User Stories

Break down MVP features into buildable stories:

```markdown
## MVP User Stories

### Epic: [Feature Area]

**Story 1**: [Title]
- As a [user], I want [action] so that [benefit]
- **Points**: [1, 2, 3, 5, 8]
- **Dependencies**: [None or list]
- **Acceptance Criteria**:
  - [ ] [Criterion 1]
  - [ ] [Criterion 2]

**Story 2**: [Title]
...
```

### 5. Define MVP Success Metrics

How will you know MVP is successful?

```markdown
## Success Metrics

### Activation
- **Metric**: [What to measure]
- **Target**: [Specific number]
- **Why it matters**: [Connection to learning goal]

### Engagement
- **Metric**: [What to measure]
- **Target**: [Specific number]
- **Why it matters**: [Connection to learning goal]

### Retention
- **Metric**: [What to measure]
- **Target**: [Specific number]
- **Why it matters**: [Connection to learning goal]

### Revenue (if applicable)
- **Metric**: [What to measure]
- **Target**: [Specific number]
- **Why it matters**: [Connection to learning goal]
```

### 6. Create Release Criteria

Define what must be true before MVP ships:

```markdown
## Release Criteria

### Functional Requirements
- [ ] All core features implemented and tested
- [ ] User flows complete without blockers
- [ ] Error handling covers edge cases
- [ ] Data persistence works correctly

### Quality Requirements
- [ ] No critical bugs
- [ ] Performance meets baseline (load time < X seconds)
- [ ] Security basics in place (auth, data protection)
- [ ] Mobile responsive (if applicable)

### Operational Requirements
- [ ] Monitoring and logging configured
- [ ] Backup and recovery tested
- [ ] Support documentation created
- [ ] Rollback procedure documented

### Compliance Requirements (if applicable)
- [ ] Terms of service and privacy policy
- [ ] Data handling compliant with regulations
- [ ] Accessibility baseline met
```

### 7. Estimate Timeline

Create a realistic build timeline:

```markdown
## MVP Timeline

### Phase 1: Foundation (Week X-Y)
- [Setup tasks]
- [Infrastructure]

### Phase 2: Core Features (Week X-Y)
- [Feature development]

### Phase 3: Integration & Testing (Week X-Y)
- [Testing]
- [Bug fixes]

### Phase 4: Polish & Launch (Week X-Y)
- [Final touches]
- [Deployment]

**Total Duration**: X weeks
**Buffer**: X% for unknowns
```

## Output

**Format:** Markdown document

**Structure:**
1. Learning goals
2. MVP feature set (included/excluded)
3. User stories
4. Success metrics
5. Release criteria
6. Timeline estimate

**Location:** `{project-root}/.pawbytes/prodig-suites/memory/paw-ps-sidecar/artifacts/{product-slug}/mvp-definition.md`

**Naming:** `mvp-definition.md`

## Quality Checklist

Before delivery, verify:

- [ ] Learning goals are specific and measurable
- [ ] MVP feature set has explicit exclusions
- [ ] Every included feature maps to a learning goal
- [ ] Success metrics are quantified
- [ ] Release criteria are testable
- [ ] Timeline is realistic with buffer

## MVP Anti-Patterns

| Anti-Pattern | Problem | Fix |
|--------------|---------|-----|
| **Kitchen sink** | Including too many features | Focus on learning goals |
| **Broken window** | Shipping poor quality | Maintain release criteria |
| **Vanity metrics** | Measuring wrong things | Connect metrics to hypotheses |
| **No feedback loop** | Launch without learning plan | Define success metrics upfront |
| **Perfect is enemy** | Never shipping due to perfectionism | Ship to learn, iterate |

## MVP Size Guidelines

| Product Type | Typical MVP Scope | Timeline |
|--------------|-------------------|----------|
| Simple SaaS | 3-5 core features | 4-8 weeks |
| Complex SaaS | 1-2 workflows end-to-end | 8-12 weeks |
| Mobile App | Core functionality, 1-2 screens | 6-10 weeks |
| AI Tool | Single primary use case | 4-8 weeks |
| Internal Tool | One complete workflow | 2-6 weeks |

## Example Output

```markdown
## MVP Definition: Task Automation Platform

### Learning Goals

**Primary Question**: Will knowledge workers pay for an automation tool that reduces repetitive task time by 50%?

**Success Indicator**: 100 paying customers within 60 days of launch

**Timeframe**: 90 days to validate

**Secondary Questions**:
1. Which automation types are most valuable?
2. What's the acceptable learning curve?
3. What integrations are essential?

### MVP Feature Set

#### Core Features (Non-Negotiable)
| Feature | Justification | Risk if Excluded |
|---------|---------------|------------------|
| User authentication | Required for any personalized experience | Product doesn't function |
| Task builder | Core value proposition | No automation possible |
| Basic triggers | Automation requires triggers | No automation possible |
| Basic actions | Automation requires actions | No automation possible |

#### Included Features
| Feature | Fallback | Risk |
|---------|----------|------|
| Email trigger | Manual task entry | Medium |
| Spreadsheet action | Copy-paste results | Low |
| Templates | Build from scratch | Medium |

#### Explicitly Excluded
| Feature | Reason for Deferral | Planned Version |
|---------|---------------------|-----------------|
| Webhook triggers | Complex, few early adopters need | v1.1 |
| API access | Requires documentation, support | v1.2 |
| Team collaboration | Adds complexity, individual value first | v2.0 |
| Advanced scheduling | Nice-to-have, simple scheduling sufficient | v1.1 |
```

## Escalation

If feature specifications or user flows are incomplete, escalate to those capabilities before MVP scoping. If timeline or technical constraints are unclear, engage technical planning.