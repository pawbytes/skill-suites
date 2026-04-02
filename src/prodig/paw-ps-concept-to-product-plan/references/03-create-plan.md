# Stage 3: Create Plan

## Objective

Generate a detailed execution plan specific to the identified executor type.

## Process

### Step 1: Initialize Plan Structure

Create plan document with standard sections:

```markdown
# Product Plan: [Product Name]

## Metadata
- **Product:** [name]
- **Family:** [family]
- **Executor:** [assigned executor]
- **Created:** [date]
- **Source:** [brief reference]

## Executive Summary
[2-3 sentence overview of what will be built]
```

### Step 2: Define Scope Section

Document explicit boundaries:

```markdown
## Scope

### In Scope
- [Item 1]
- [Item 2]
- [Item 3]

### Out of Scope
- [Item 1]
- [Item 2]

### Assumptions
- [Assumption 1]
- [Assumption 2]
```

### Step 3: Create Executor-Specific Plan

Based on executor type, populate relevant sections:

#### For Knowledge Products

```markdown
## Content Structure

### Learning Objectives
1. [Objective 1]
2. [Objective 2]

### Content Modules
| Module | Topic | Format | Est. Length |
|--------|-------|--------|-------------|
| 1 | [topic] | [video/text/interactive] | [time] |
| 2 | [topic] | [format] | [time] |

### Research Requirements
- [Source 1]
- [Source 2]

### Deliverable Specifications
- Primary format: [PDF/video/web/other]
- Supporting materials: [worksheets/templates/checklists]
```

#### For Template Products

```markdown
## Component Architecture

### Core Components
| Component | Purpose | Customization Points |
|-----------|---------|---------------------|
| [name] | [purpose] | [points] |

### Usage Patterns
- Pattern 1: [description]
- Pattern 2: [description]

### Customization Framework
- Required inputs: [list]
- Optional configurations: [list]
- Output formats: [list]

### Documentation Requirements
- Quick start guide
- Component reference
- Example implementations
```

#### For Software Products

```markdown
## Technical Specification

### Core Features
| Feature | Priority | Complexity |
|---------|----------|------------|
| [feature] | [P1/P2/P3] | [low/medium/high] |

### Technical Architecture
- Stack: [technologies]
- Data model: [brief description]
- Integrations: [list]

### Implementation Phases
| Phase | Scope | Deliverable |
|-------|-------|-------------|
| 1 | [scope] | [deliverable] |

### Quality Requirements
- Performance: [criteria]
- Security: [requirements]
- Testing: [coverage expectations]
```

#### For Service Products

```markdown
## Service Definition

### Service Package
- Tier: [basic/standard/premium]
- Duration: [timeframe]
- Deliverables: [list]

### Delivery Process
| Phase | Activities | Duration | Output |
|-------|------------|----------|--------|
| 1 | [activities] | [time] | [output] |

### Client Touchpoints
- Kickoff: [format/timing]
- Progress reviews: [frequency]
- Delivery: [format]

### Quality Framework
- Success metrics: [list]
- Satisfaction criteria: [list]
```

### Step 4: Define Deliverables

```markdown
## Deliverables

### Primary Deliverable
- Name: [deliverable name]
- Format: [file type/medium]
- Location: [output path]

### Supporting Deliverables
| Item | Format | Purpose |
|------|--------|---------|
| [item] | [format] | [purpose] |
```

### Step 5: Set Success Criteria

```markdown
## Success Criteria

### Completion Criteria
- [ ] [Criterion 1]
- [ ] [Criterion 2]
- [ ] [Criterion 3]

### Quality Gates
- [ ] All deliverables created
- [ ] Documentation complete
- [ ] Testing/validation passed
- [ ] Review completed
```

### Step 6: Save Plan

Save to: `.pawbytes/prodig-suites/plans/{product-slug}/plan.md`

## Output

Complete plan document saved to resolved path with:
- All sections populated
- Executor-specific details included
- Deliverables specified
- Success criteria defined

## Progression Condition

Plan is complete with all required sections. Executor can use this plan without additional clarification. Success criteria are measurable and achievable.