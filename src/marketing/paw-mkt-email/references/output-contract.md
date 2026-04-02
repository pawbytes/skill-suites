# Output Contract

Define what email deliverables look like and where they save.

## Deliverable Types

| Deliverable | Filename | Key Sections |
|---|---|---|
| Email Sequence | `sequence-{type}-{YYYY-MM-DD}.md` | Trigger, exit conditions, segment, goal, sequence map table, full email drafts, A/B test plan, success metrics |
| Newsletter Plan | `newsletter-plan-{YYYY-MM-DD}.md` | Name, frequency/timing, audience segments, content framework, subject line strategy, growth plan, editorial calendar, KPIs |
| Automation Workflow | `automation-{workflow-name}-{YYYY-MM-DD}.md` | Trigger, audience, goal, workflow diagram, email summaries, exit conditions, frequency caps, testing plan |
| Copywriting Templates | `email-templates-{type}-{YYYY-MM-DD}.md` | 10-15 subject line formulas, 5-10 preheader formulas, body templates, 5-10 CTA options |
| Deliverability Audit | `deliverability-audit-{YYYY-MM-DD}.md` | Authentication status, reputation scores, inbox placement, complaint rates, remediation plan |
| Cold Email Sequence | `cold-outbound-{campaign-name}-{YYYY-MM-DD}.md` | Full copy per email, angle notes, personalization variables, CTA instructions |

## Path Resolution

**Campaign mode** (working within named campaign):
```
./.pawbytes/marketing-suites/brands/{brand-slug}/campaigns/{type}-{campaign-slug}/channels/email/content/
```
Read campaign strategy at: `./.pawbytes/marketing-suites/brands/{brand-slug}/campaigns/{type}-{campaign-slug}/strategy.md`

**Standalone mode** (evergreen or independent work):
```
./.pawbytes/marketing-suites/brands/{brand-slug}/channels/email/content/
```

**Legacy fallback** (old directory structure):
```
./.pawbytes/marketing-suites/brands/{brand-slug}/content/email/
```
Suggest migration to new structure.

If unsure which mode, ask: "Is this part of a specific campaign, or standalone work?"

## Sequence Map Format

For email sequences, include a sequence map table:

| Email | Delay | Subject | Message Purpose | CTA |
|---|---|---|---|---|
| 1 | Immediate | [Subject] | [Purpose] | [Action] |
| 2 | Day 3 | [Subject] | [Purpose] | [Action] |
| 3 | Day 7 | [Subject] | [Purpose] | [Action] |

## Individual Email Format

Each email in deliverable includes:

```
Email Type: [welcome/nurture/sales/etc]
Subject Line: [Subject] (A/B variant: [Variant] if applicable)
Preview Text: [Preheader]
Body Copy: [Complete email ready for ESP]
CTA: [Primary action] - [link placeholder]
Sequence Position: [Where this fits in flow]
```

## Performance Reports

Monthly performance reports save to:
```
./.pawbytes/marketing-suites/brands/{brand-slug}/channels/email/performance/monthly-report-{YYYY-MM}.md
```

Include: key metrics vs benchmarks, test results, optimization recommendations.

## File Saved Confirmation

Every deliverable ends with:
```
File saved to: [resolved path]/[filename]
```