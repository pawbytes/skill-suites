# Execution Checklist

## Purpose

A comprehensive checklist for validating software product artifacts before developer handoff. Ensures nothing is missed and the build package is complete.

## When to Use

Use this checklist:
- Before developer handoff
- After PRD-lite is finalized
- When preparing execution artifacts

## Artifact Completeness Checklist

### Feature Specifications
- [ ] All MVP features documented
- [ ] Each feature has user story
- [ ] Each feature has acceptance criteria
- [ ] Scope boundaries defined (in/out)
- [ ] Priorities assigned (P0/P1/P2)
- [ ] Dependencies mapped

### User Flows
- [ ] Core flows documented
- [ ] Entry points defined
- [ ] Decision points documented
- [ ] Error states handled
- [ ] Screen requirements specified

### MVP Definition
- [ ] Learning goals articulated
- [ ] MVP features listed
- [ ] Exclusions explicit
- [ ] Success metrics defined
- [ ] Release criteria documented
- [ ] Timeline estimated

### PRD-Lite
- [ ] One-liner is clear
- [ ] Problem statement is specific
- [ ] Target user is defined
- [ ] Scope is bounded
- [ ] Functional requirements are testable
- [ ] Technical context is specified
- [ ] Open questions have owners

### Technical Context
- [ ] Tech stack documented
- [ ] Data model overview complete
- [ ] API structure outlined
- [ ] Technical risks identified
- [ ] Integrations specified

## Build Readiness Checklist

### Development Prerequisites
- [ ] Repository structure decided
- [ ] Development environment documented
- [ ] Third-party accounts created
- [ ] API keys obtained
- [ ] Design files accessible

### Quality Requirements
- [ ] Code standards defined
- [ ] Testing strategy outlined
- [ ] Code review process established
- [ ] CI/CD pipeline planned

### Deployment Planning
- [ ] Hosting environment selected
- [ ] Domain configured
- [ ] SSL certificate planned
- [ ] Monitoring approach defined

## Handoff Readiness Checklist

### Documentation
- [ ] All artifacts in one location
- [ ] File naming is consistent
- [ ] Versions are current
- [ ] Owner is identified

### Communication
- [ ] Developer has access to all documents
- [ ] Questions channel established
- [ ] Meeting schedule agreed
- [ ] Escalation path defined

### Sign-off
- [ ] Product owner approved scope
- [ ] Technical lead approved approach
- [ ] Timeline is accepted
- [ ] Risks are acknowledged

## Output Format

Create a checklist document:

```markdown
# Execution Checklist: [Product Name]

**Date**: [YYYY-MM-DD]
**Prepared by**: [Name]
**Status**: [In Progress / Ready for Handoff]

---

## Artifact Status

| Artifact | Status | Location | Owner |
|----------|--------|----------|-------|
| Feature Specs | [Complete/Partial/Missing] | [Path] | [Name] |
| User Flows | [Complete/Partial/Missing] | [Path] | [Name] |
| MVP Definition | [Complete/Partial/Missing] | [Path] | [Name] |
| PRD-Lite | [Complete/Partial/Missing] | [Path] | [Name] |
| Technical Context | [Complete/Partial/Missing] | [Path] | [Name] |

---

## Build Readiness

[Run through Build Readiness Checklist above]

---

## Handoff Readiness

[Run through Handoff Readiness Checklist above]

---

## Outstanding Items

| Item | Owner | Due | Blocker |
|------|-------|-----|---------|
| [Item 1] | [Who] | [Date] | [Yes/No] |
| [Item 2] | [Who] | [Date] | [Yes/No] |

---

## Sign-off

- [ ] Product Owner: ________________ Date: ________
- [ ] Technical Lead: ________________ Date: ________
```

**Location:** `{project-root}/.pawbytes/prodig-suites/memory/paw-ps-sidecar/artifacts/{product-slug}/execution-checklist.md`

**Naming:** `execution-checklist.md`