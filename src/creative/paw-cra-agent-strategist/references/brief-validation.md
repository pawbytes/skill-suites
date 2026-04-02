# Brief Validation

Validate incoming creative briefs against agency standards before campaign planning begins. This quality gate ensures every brief is complete, strategically sound, and ready for production.

## Agency Standards Checklist

### 1. Completeness Check

| Element | Required | Status |
|---------|----------|--------|
| Deliverables (format, quantity, specs) | ✓ | |
| Objective (clear goal, success metrics) | ✓ | |
| Target audience | ✓ | |
| Timeline (deadlines, milestones) | ✓ | |
| Brand reference | ✓ | |
| Constraints (must/must not) | ○ | |
| References/examples | ○ | |

Legend: ✓ = Required, ○ = Recommended

**If required elements missing:** Flag to Aria with specific gaps.

### 2. Brand Alignment Check

- Does the brief align with brand voice and positioning?
- Is the messaging consistent with brand guidelines?
- Are visual directions appropriate for brand identity?

**Load brand context:** `{project-root}/.pawbytes/creative-suites/brands/{brand-name}/guidelines.md`

### 3. Strategic Clarity Check

- **Objective clarity:** Is the goal specific and measurable?
- **Scope realism:** Can deliverables be produced with available tools and timeline?
- **Success criteria:** How will we know this worked?

### 4. Research Needs Assessment

Identify what additional research would strengthen the campaign:
- Competitor analysis needed?
- Audience insights missing?
- Trend data relevant?
- Platform-specific research required?

## Output

Return to Aria with:

```markdown
# Brief Validation: {Brief Name}

## Status
[ ] Approved — brief is complete and ready for campaign planning
[ ] Needs clarification — specific gaps identified below
[ ] Requires research — additional research recommended

## Completeness
- Missing: {list any required elements}
- Gaps: {list any unclear or vague areas}

## Brand Alignment
- Aligned: {yes/concerns}
- Concerns: {list any conflicts with brand guidelines}

## Strategic Assessment
- Objective clarity: {clear/needs refinement}
- Scope: {realistic/tight/overly ambitious}
- Success criteria: {defined/missing}

## Research Recommendations
- {research type}: {why needed}
- {research type}: {why needed}

## Recommended Next Steps
1. {action item}
2. {action item}
```

## Process

1. Receive brief from Aria (extracted via Brief Analysis)
2. Load brand context if available
3. Run through all four checks
4. Produce validation report
5. Return to Aria with findings and recommendations