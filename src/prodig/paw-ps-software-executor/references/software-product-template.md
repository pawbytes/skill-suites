# Software Product Template

## Purpose

Initial template for seeding `curated/product-types/software-products.md` when it doesn't exist. This file is copied to the curated memory location on first activation.

## Template Content

```markdown
# Software Products Guidance

## Overview

Software products include SaaS applications, mobile/desktop apps, AI tools, and internal software. They differ from knowledge and template products in that they require technical development and have distinct execution patterns focused on buildability and delivery.

## Product Types

### SaaS (Software as a Service)
- Web-based software delivered via subscription
- Examples: Project management, CRM, automation tools
- Key artifacts: Feature specs, API contracts, pricing tiers

### Applications
- Mobile or desktop software
- Examples: iOS apps, desktop utilities
- Key artifacts: Platform requirements, store assets

### AI Tools
- AI-powered products and integrations
- Examples: Chatbots, content generators, analyzers
- Key artifacts: Model specs, prompt templates, integration maps

### Internal Tools
- Operational software for teams
- Examples: Dashboards, workflow tools, admin panels
- Key artifacts: Workflow definitions, role permissions

## Feature Definition Patterns

### Value-First Approach
Start with value proposition before features:
1. What problem does this solve?
2. Who experiences it most acutely?
3. How will success be measured?

### Feature Categories
Common groupings:
- Onboarding & Account
- Core Workflow
- Data & Reporting
- Settings & Configuration
- Collaboration
- Administration

### Priority Framework
- P0: Critical (breaks core value without it)
- P1: Important (significant impact, workaround exists)
- P2: Nice-to-have (enhances but not essential)

## MVP Scoping Patterns

### Learning Goals
MVP should validate:
- Will users pay?
- Does this solve the problem?
- Is the experience intuitive?
- What features get used?

### Scope Discipline
- Include: Features that validate hypotheses
- Exclude: Features that can wait
- Document: Why each exclusion was made

### Typical MVP Size
- Simple SaaS: 3-5 core features, 4-8 weeks
- Complex SaaS: 1-2 workflows, 8-12 weeks
- Mobile App: Core functionality, 6-10 weeks
- AI Tool: Single use case, 4-8 weeks

## Technical Decision Patterns

### Stack Selection
Consider:
- Team expertise
- Time to market
- Scalability needs
- Ecosystem maturity

### Build vs. Buy
Default to buy for:
- Authentication
- Payments
- Email delivery
- File storage

Default to build for:
- Core differentiation
- Custom workflows
- Unique integrations

### Integration Strategy
- Start with essential integrations only
- Use middleware where possible
- Document API dependencies

## User Flow Patterns

### Core Flows
Most software products need:
- Authentication flow
- Onboarding flow
- Core task flow
- Settings flow

### Error Handling
Every flow needs:
- Validation errors
- System errors
- Permission errors
- Recovery paths

## Common Pitfalls

1. **Feature creep**: Adding features before validating core
2. **Vague specs**: Ambiguity leads to bugs
3. **Missing error states**: Users get stuck
4. **No success metrics**: Can't measure progress
5. **Over-engineering**: Building for scale that doesn't exist

## Artifact Checklist

Before developer handoff:
- [ ] Feature specifications with acceptance criteria
- [ ] User flows with error states
- [ ] MVP definition with exclusions
- [ ] PRD-lite with technical context
- [ ] Execution checklist complete

## Success Patterns

1. Start with learning goals
2. Define scope boundaries explicitly
3. Document decisions with rationale
4. Create testable acceptance criteria
5. Plan for iteration, not perfection

---

**Last Updated**: [Date will be set when seeded]
**Maintained By**: Software Executor
```

## Seeding Instructions

When `curated/product-types/software-products.md` does not exist:

1. Create the directory structure if needed:
   ```
   .pawbytes/prodig-suites/memory/paw-ps-sidecar/curated/product-types/
   ```

2. Copy this template content to:
   ```
   .pawbytes/prodig-suites/memory/paw-ps-sidecar/curated/product-types/software-products.md
   ```

3. Update the "Last Updated" field with current date

4. Log the initialization in daily log