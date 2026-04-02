# Workflow Integration Capability

## Overview
Coordinate with agency ecosystem, manage file organization, and handle escalation routing. Ensures SEO deliverables integrate with broader marketing workflow.

## When to Use
- Agency coordination
- File organization setup
- Cross-channel collaboration
- Escalation routing
- Monthly reporting structure

## Capability Workflow

### Agency Connection

**Input**:
- Brand context and SOSTAC plan from agency coordinator

**Output**:
- All deliverables to resolved path (see Path Resolution)

**Collaboration**:
- Content Strategist: briefs feed content creation
- Paid Media: keyword data informs PPC
- Analytics: tracking and reporting
- PR: digital PR and link building overlap

**Reporting**:
- Monthly performance summaries to `./.pawbytes/marketing-suites/brands/{brand-slug}/analytics/seo/`

### File Organization

```
# Campaign mode:
./.pawbytes/marketing-suites/brands/{brand-slug}/campaigns/{type}-{campaign-slug}/channels/seo/content/

# Standalone mode (default):
./.pawbytes/marketing-suites/brands/{brand-slug}/channels/seo/content/

# Legacy fallback:
./.pawbytes/marketing-suites/brands/{brand-slug}/content/seo/
```

### When to Escalate

**No website yet**:
- Recommend web development before SEO

**Heavily regulated industry (medical, legal, financial)**:
- Flag YMYL considerations
- Recommend legal review

**Urgent paid media need**:
- Route to Paid Media specialist
- SEO is long-term strategy

**Technical issues needing developer access**:
- Document requirements clearly for dev team
- Provide implementation-ready specifications

## Output

- Monthly SEO reports
- Cross-channel recommendations
- Escalation documentation