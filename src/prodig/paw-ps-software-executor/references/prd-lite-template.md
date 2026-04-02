# PRD-Lite Template

## Purpose

A PRD-lite is a concise, actionable product requirements document that developers can build from. Unlike traditional PRDs that can run dozens of pages, a PRD-lite captures essential decisions in 2-5 pages.

## When to Use

Use PRD-lite when:
- MVP is scoped and ready for developer handoff
- Features are defined but need consolidation
- External developers need context
- Internal team needs alignment before build

## Template Structure

```markdown
# PRD-Lite: [Product Name]

**Version**: [X.Y]
**Status**: [Draft / Review / Approved]
**Last Updated**: [YYYY-MM-DD]
**Owner**: [Name]

---

## 1. Product Summary

### One-Liner
[Single sentence describing what this product does and for whom]

### Problem Statement
[2-3 sentences on the problem being solved]

### Success Metric
[Primary metric that indicates product success]

---

## 2. Target User

### Primary Persona
- **Role**: [Job title or role]
- **Context**: [When/where they use this]
- **Pain Point**: [Specific problem they face]
- **Current Solution**: [How they solve it now]

### User Outcomes
[What the user can do after using this product that they couldn't do before]

---

## 3. Scope

### MVP Includes

| Feature | Description | Priority |
|---------|-------------|----------|
| [Feature 1] | [Brief description] | P0 |
| [Feature 2] | [Brief description] | P0 |
| [Feature 3] | [Brief description] | P1 |

### MVP Excludes

| Feature | Reason | Future Version |
|---------|--------|----------------|
| [Feature X] | [Why deferred] | [vX.X] |
| [Feature Y] | [Why deferred] | [vX.X] |

---

## 4. User Experience

### Core Flow
[Describe the primary user journey in 3-5 steps]

1. User [action]
2. System [response]
3. User [action]
4. System [response]
5. User achieves [outcome]

### Key Screens
[List the essential screens/pages]

| Screen | Purpose | Key Elements |
|--------|---------|--------------|
| [Screen 1] | [What it enables] | [Primary components] |
| [Screen 2] | [What it enables] | [Primary components] |

---

## 5. Functional Requirements

### [Feature Area 1]

**Requirement**: [What the system must do]
**Acceptance Criteria**:
- Given [context], when [action], then [result]
- Given [context], when [action], then [result]

**Constraints**:
- [Technical or business constraints]

### [Feature Area 2]

**Requirement**: [What the system must do]
**Acceptance Criteria**:
- Given [context], when [action], then [result]

**Constraints**:
- [Technical or business constraints]

---

## 6. Non-Functional Requirements

### Performance
- Page load: [target]
- API response: [target]
- Concurrent users: [capacity]

### Security
- Authentication: [method]
- Data encryption: [requirements]
- Compliance: [regulations if applicable]

### Reliability
- Uptime target: [percentage]
- Data backup: [frequency]

---

## 7. Technical Context

### Platform
- **Frontend**: [Framework/technology]
- **Backend**: [Framework/technology]
- **Database**: [Type and provider]
- **Hosting**: [Provider]

### Integrations
| Service | Purpose | Status |
|---------|---------|--------|
| [Service 1] | [What it enables] | [Required/Optional] |
| [Service 2] | [What it enables] | [Required/Optional] |

### Data Model (High-Level)
[Describe key entities and relationships]

---

## 8. Release Criteria

### Must Ship With
- [ ] All P0 features implemented and tested
- [ ] Core user flow complete without blockers
- [ ] Authentication working correctly
- [ ] Error handling in place
- [ ] Basic monitoring configured

### Quality Gates
- [ ] No critical bugs
- [ ] Performance meets targets
- [ ] Security review complete
- [ ] Documentation updated

---

## 9. Timeline & Milestones

| Milestone | Target Date | Status |
|-----------|-------------|--------|
| [Milestone 1] | [Date] | [Status] |
| [Milestone 2] | [Date] | [Status] |
| [Milestone 3] | [Date] | [Status] |
| MVP Launch | [Date] | [Status] |

---

## 10. Risks & Mitigations

| Risk | Likelihood | Impact | Mitigation |
|------|------------|--------|------------|
| [Risk 1] | [H/M/L] | [H/M/L] | [How we'll handle it] |
| [Risk 2] | [H/M/L] | [H/M/L] | [How we'll handle it] |

---

## 11. Open Questions

| Question | Owner | Due Date | Resolution |
|----------|-------|----------|------------|
| [Question 1] | [Who decides] | [Date] | [Answer when resolved] |
| [Question 2] | [Who decides] | [Date] | [Answer when resolved] |

---

## Appendix

### Related Documents
- [Link to feature specs]
- [Link to user flows]
- [Link to MVP definition]
- [Link to design files]

### Revision History
| Version | Date | Changes | Author |
|---------|------|---------|--------|
| [X.Y] | [Date] | [Summary] | [Name] |
```

## Output

**Format:** Markdown document using template above

**Location:** `{project-root}/.pawbytes/prodig-suites/memory/paw-ps-sidecar/artifacts/{product-slug}/prd-lite.md`

**Naming:** `prd-lite.md`

## PRD-Lite vs. Full PRD

| Aspect | PRD-Lite | Full PRD |
|--------|----------|----------|
| Length | 2-5 pages | 10-50+ pages |
| Audience | Development team | All stakeholders |
| Detail level | Essential decisions | Comprehensive |
| Update frequency | High | Low |
| Best for | MVPs, fast-moving teams | Enterprise, regulated industries |

## Quality Checklist

Before considering PRD-lite complete:

- [ ] One-liner is accurate and memorable
- [ ] Success metric is measurable
- [ ] Scope boundaries are explicit
- [ ] Acceptance criteria are testable
- [ ] Technical context is specific enough
- [ ] Open questions have owners and due dates
- [ ] Risks have mitigations

## Example PRD-Lite (Condensed)

```markdown
# PRD-Lite: Invoice Automation Tool

**Version**: 1.0
**Status**: Approved
**Last Updated**: 2026-04-02
**Owner**: Product Team

---

## 1. Product Summary

### One-Liner
Invoice Flow automates invoice data extraction and approval routing for small finance teams.

### Problem Statement
Small finance teams spend 10+ hours per week manually entering invoice data and chasing approvals. This leads to payment delays and processing errors.

### Success Metric
Reduce invoice processing time by 50% within 30 days of onboarding.

---

## 2. Target User

### Primary Persona
- **Role**: Finance Manager at companies with 10-50 employees
- **Context**: Processes 20-50 invoices per week
- **Pain Point**: Manual data entry is error-prone and time-consuming
- **Current Solution**: Spreadsheet tracking with email approvals

### User Outcomes
After using Invoice Flow, users can process invoices in half the time with automatic data extraction and streamlined approvals.

---

## 3. Scope

### MVP Includes

| Feature | Description | Priority |
|---------|-------------|----------|
| Invoice upload | Drag-drop PDF/image upload | P0 |
| Data extraction | AI-powered field extraction | P0 |
| Approval workflow | Configurable approval chains | P0 |
| Dashboard | Invoice status overview | P1 |

### MVP Excludes

| Feature | Reason | Future Version |
|---------|--------|----------------|
| ERP integration | Requires significant development | v1.1 |
| Payment processing | Legal/compliance complexity | v2.0 |
| Mobile app | Web-first approach | v1.2 |
```

## Escalation

If PRD-lite reveals missing decisions or unresolved questions, escalate to the appropriate capability (feature definition, MVP scoping, strategist) before finalizing.