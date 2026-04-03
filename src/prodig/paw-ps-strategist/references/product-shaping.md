# Product Shaping

Define the offer and its boundaries to produce a clear product brief that guides all subsequent decisions.

## Purpose

Transform market and audience intelligence into a compelling product definition that answers: What are we building? Who is it for? Why does it matter? How will it win?

## Required Inputs

Before product shaping, ensure these are available:

| Input | Source | Purpose |
|-------|--------|---------|
| Market Intelligence | `curated/market-intelligence.md` | Competitive landscape, market size, trends |
| Audience Intelligence | `curated/audience-intelligence.md` | User needs, pain points, segments |
| Product Context | `curated/product-context.md` | Existing product decisions and constraints |

If inputs are missing, route to appropriate research agent before proceeding.

## Shaping Framework

### 1. Value Proposition Definition

Answer the core question: "What value do we deliver that no one else can?"

**Elements:**

| Element | Question | Source |
|---------|----------|--------|
| Target Segment | Who has the problem? | Audience Intelligence |
| Problem Statement | What pain do they feel? | Audience Intelligence |
| Solution Concept | How do we solve it? | Market + Audience synthesis |
| Differentiation | Why us vs alternatives? | Market Intelligence |
| Proof Points | How do we know? | Both sources |

### 2. Product Boundaries

Define what the product IS and IS NOT:

**In Scope:**
- Core problem we solve
- Primary user segments we serve
- Key capabilities we deliver
- Essential quality attributes

**Out of Scope:**
- Problems we don't solve (yet)
- Segments we don't target
- Features we don't include
- Quality attributes we de-prioritize

### 3. Success Criteria

Define how we'll know if the product is successful:

| Metric Type | Definition | Target |
|-------------|------------|--------|
| Business | Revenue, adoption, retention | Specific targets |
| User | Satisfaction, task completion | Specific targets |
| Technical | Performance, reliability | Specific targets |
| Learning | What we want to validate | Assumptions to test |

### 4. Assumptions and Risks

Document what we're assuming and what could go wrong:

**Key Assumptions:**
- Market assumptions (size, growth, willingness to pay)
- User assumptions (needs, behavior, adoption)
- Technical assumptions (feasibility, performance)
- Business assumptions (costs, timeline, resources)

**Key Risks:**
- Market risks (competition, timing)
- User risks (adoption, satisfaction)
- Technical risks (complexity, dependencies)
- Business risks (budget, team, timeline)

## Output: Product Brief

Produce a structured product brief:

```markdown
# Product Brief: {Product Name}

## Executive Summary
One paragraph capturing the product essence.

## Value Proposition
**For** {target segment}
**Who** {has this problem}
**We provide** {solution}
**That** {key benefit}
**Unlike** {alternatives}
**We** {differentiation}

## Product Boundaries

### In Scope
- {boundary 1}
- {boundary 2}
- {boundary 3}

### Out of Scope
- {boundary 1}
- {boundary 2}

## Success Criteria
| Metric | Target | Measurement |
|--------|--------|-------------|
| {metric} | {target} | {how measured} |

## Key Assumptions
1. {assumption} — validated by {evidence or experiment}
2. {assumption} — validated by {evidence or experiment}

## Key Risks
| Risk | Likelihood | Impact | Mitigation |
|------|------------|--------|------------|
| {risk} | H/M/L | H/M/L | {mitigation} |

## Next Steps
1. {immediate next action}
2. {follow-up action}
```

## Process

1. Load and synthesize market and audience intelligence
2. Draft value proposition using the framework
3. Define product boundaries (in/out scope)
4. Establish success criteria with targets
5. Document assumptions and risks
6. Produce product brief
7. Write to `curated/product-decisions.md`
8. Update `curated/product-context.md` with new decisions
9. Log activity in daily file

## Quality Check

Before finalizing, verify:

- [ ] Value proposition is specific and differentiated
- [ ] Boundaries are clear and actionable
- [ ] Success criteria are measurable
- [ ] Assumptions are testable
- [ ] Risks have mitigation strategies
- [ ] Brief can be understood by someone not in the room