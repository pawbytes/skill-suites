# Section Templates — Scoping

Type: `scoping` — post-yes project plan / statement of work. Tone: collaborative, precise, mutually accountable. Both parties should leave knowing exactly what will be built, when, and what each side owes.

## Section order

1. Assumptions callout (autonomous only)
2. **Project overview** — goal, success criteria, out-of-scope explicitly stated
3. **Background & context** — why this project, link to prior work if returning client
4. **Objectives** — measurable outcomes (from brief)
5. **Scope of work** — deliverables with acceptance criteria per item
6. **Approach & methodology** — how work will be executed
7. **Roles & responsibilities** — RACI-style: seller vs client obligations
8. **Timeline & milestones** — phases with dates, dependencies, client input deadlines
9. **Pricing & payment schedule** — line-items + milestone triggers
10. **Risk register** — full matrix with client-shared risks flagged
11. **Change control** — how scope changes are handled (reference terms.md)
12. **Communication plan** — cadence, channels, escalation
13. **Team** — bios for assigned roles
14. **Terms & conditions** — verbatim from `terms.md` (SOW/scoping variant if present)
15. **Acceptance & signatures** — sign-off block

## Tone notes

- Precision over persuasion — the deal is largely won; this document prevents scope creep.
- Every deliverable needs acceptance criteria ("done means…").
- Client responsibilities must be explicit (content, access, approvals, data).
- Out-of-scope section is as important as in-scope.
- Pull clauses from `library/scope-templates.md` where they match service type.

## Template skeleton

```markdown
# Statement of Work — {project name}

**Client:** {client name}
**Prepared by:** {seller name}
**Date:** {date}
**Version:** 1.0

> **Assumptions** *(autonomous mode only)*
> - {assumption}

## Project overview

**Goal:** {from brief}
**Success criteria:**
- {measurable outcome 1}
- {measurable outcome 2}

**Out of scope:**
- {explicit exclusion 1}
- {explicit exclusion 2}

## Background
{Context from brief + client history if returning.}

## Objectives
1. {Objective — measurable}
2. {Objective — measurable}

## Scope of work

### Deliverable 1: {name}
**Description:** …
**Acceptance criteria:**
- [ ] …
- [ ] …

### Deliverable 2: {name}
…

## Approach
{Methodology — phases, tools, environments.}

## Roles & responsibilities

| Activity | {Seller} | {Client} |
|----------|----------|----------|
| Requirements validation | R | A |
| Content provision | C | R |
| Review & approval | C | A |
| … | … | … |

*R = Responsible, A = Accountable, C = Consulted*

## Timeline & milestones

| Milestone | Target date | Deliverable | Payment trigger |
|-----------|-------------|-------------|-----------------|
| Kickoff | … | Signed SOW | {deposit %} |
| … | … | … | … |

## Investment

| Item | Details | Amount |
|------|---------|--------|
| … | … | … |

**Total:** {total}
**Payment schedule:** {milestone triggers}

## Risk register

| Risk | Likelihood | Impact | Mitigation | Owner |
|------|------------|--------|------------|-------|
| Client delay on content | Med | High | Buffer in timeline; escalation at day N | Client |
| … | … | … | … | … |

## Change control
{From terms.md or standard clause — how changes are requested, estimated, approved.}

## Communication plan
- **Standups:** {cadence}
- **Status reports:** {cadence}
- **Escalation:** {contact path}

## Team
{Assigned roles from bios.md}

## Terms & conditions
{Verbatim from brand/boilerplate/terms.md}

## Acceptance

| Party | Name | Signature | Date |
|-------|------|-----------|------|
| {Seller} | | | |
| {Client} | | | |
```

## Short variation (`draft-v1-short.md`)

Project overview + deliverables list + timeline summary + total price + acceptance block. For client quick review before full SOW workshop.

## Long variation (`draft-v1-long.md`)

Full acceptance criteria per deliverable, complete RACI, expanded risk register, workshop/discovery phase detail, technical environment specs from research tech-stack section, full payment schedule with discount modeling if present.
