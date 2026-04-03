# Stage 3: Synthesize Brief

## Objective

Create a structured product brief by consolidating validated research inputs into a single, coherent document with traceability to source materials.

---

## Brief Template

The product brief follows this structure:

```markdown
# Product Brief: {product-name}

**Version:** 1.0
**Generated:** {date}
**Status:** Draft
**Product Slug:** {product-slug}

---

## Executive Summary

[2-3 paragraph synthesis of the product opportunity]

---

## Problem Statement

[From discovery: What problem exists? Who experiences it? Why does it matter?]

**Source:** product-context.md

---

## Solution Vision

[From discovery: What is the proposed solution? How does it address the problem?]

**Source:** product-context.md

---

## Market Opportunity

[From market research: Market size, growth, timing, competitive position]

### Market Context
- **Market Size:** [TAM/SAM/SOM if available]
- **Growth Rate:** [if available]
- **Key Trends:** [bullet list]

### Competitive Landscape
[Summary of competitive position and differentiation]

**Source:** market-intelligence.md

---

## Target Audience

[From audience research: Primary personas and their characteristics]

### Primary Persona: {persona-name}
- **Demographics:** [summary]
- **Goals:** [what they want to achieve]
- **Pain Points:** [key frustrations]
- **Behaviors:** [relevant patterns]

**Source:** audience-intelligence.md

---

## Success Criteria

[From discovery: How will success be measured?]

| Metric | Target | Rationale |
|--------|--------|-----------|
| [metric] | [target] | [why this matters] |

---

## Constraints & Assumptions

### Constraints
- [Technical, resource, or time constraints]

### Assumptions
- [Assumptions made about market, users, or technology]

**Confidence Level:** [High/Medium/Low]

---

## Key Risks

[From market research and cross-analysis]

| Risk | Severity | Mitigation |
|------|----------|------------|
| [risk] | [high/medium/low] | [proposed mitigation] |

---

## Next Steps

1. [Immediate action items]
2. [Validation needs]
3. [Open questions]

---

## Source Traceability

| Section | Primary Source | Last Updated |
|---------|----------------|--------------|
| Problem Statement | product-context.md | [date] |
| Market Opportunity | market-intelligence.md | [date] |
| Target Audience | audience-intelligence.md | [date] |
```

---

## Synthesis Procedure

### Step 1: Map Sources to Sections

| Brief Section | Primary Source | Fallback |
|---------------|----------------|----------|
| Executive Summary | All sources (synthesis) | - |
| Problem Statement | product-context.md | market-intelligence.md |
| Solution Vision | product-context.md | - |
| Market Opportunity | market-intelligence.md | - |
| Target Audience | audience-intelligence.md | - |
| Success Criteria | product-context.md | - |
| Constraints & Assumptions | product-context.md | All sources |
| Key Risks | market-intelligence.md | All sources |

### Step 2: Extract and Transform

For each section:
1. Read relevant content from source file
2. Transform raw research into brief format
3. Maintain traceability with source citations
4. Flag any interpretation or synthesis decisions

### Step 3: Cross-Reference Validation

Check for:
- Consistency between problem statement and audience pain points
- Alignment between market opportunity and success criteria
- Coverage of risks against constraints

### Step 4: Write Brief Document

1. Write complete brief to `.pawbytes/prodig-suites/products/{product-slug}/product-brief.md`
2. Record generation timestamp
3. Note any sections with partial or missing source data

---

## Handling Missing Sources

When a source is missing:

| Missing Source | Impact | Handling |
|----------------|--------|----------|
| product-context.md | Problem, Vision, Success | Mark sections as "Requires Discovery Input" |
| market-intelligence.md | Market context | Note "Market research pending" |
| audience-intelligence.md | Audience section | Use problem statement as proxy, flag gap |

Never fabricate content. Use explicit placeholders for missing information.

---

## Quality Checklist

Before proceeding to Stage 4:

- [ ] All present sections have source citations
- [ ] Executive summary synthesizes all available inputs
- [ ] No contradictions between sections
- [ ] Gaps are explicitly marked, not hidden
- [ ] Success criteria are measurable
- [ ] Risks are specific and actionable

---

## Progression Criteria

**Proceed to Stage 4 when:**
- Brief document is written
- All available sources are reflected
- Source traceability is complete
- Quality checklist passes

**Block if:**
- Critical sections are empty and not marked as gaps
- Synthesis introduces contradictions not present in sources