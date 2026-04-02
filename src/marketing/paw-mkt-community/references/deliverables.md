# Deliverables

All community deliverables save to the resolved path (campaign or standalone mode).

## Path Structure

```
# Campaign mode:
./.pawbytes/marketing-suites/brands/{brand-slug}/campaigns/{type}-{campaign-slug}/community/
  community-strategy-{YYYY-MM-DD}.md
  platform-setup-{platform}-{YYYY-MM-DD}.md
  engagement-calendar-{YYYY-MM}.md
  moderation-guidelines-{YYYY-MM-DD}.md
  community-launch-plan-{YYYY-MM-DD}.md
  advocacy/
    ambassador-program-{YYYY-MM-DD}.md
    referral-program-{YYYY-MM-DD}.md
  performance/
    community-report-{YYYY-MM}.md
    health-score-{YYYY-MM}.md

# Standalone mode:
./.pawbytes/marketing-suites/brands/{brand-slug}/operations/community/
  (same structure as above)
```

## Deliverable Templates

### Community Strategy Document (`community-strategy-{YYYY-MM-DD}.md`)
Sections:
- Community Purpose and Type
- Target Members (from SOSTAC segments)
- Platform Selection and Rationale
- Community Promise (one-line)
- Value Proposition for Members
- Community Structure (channels/spaces/categories)
- Roles and Permissions
- Launch Timeline
- Success Metrics and Targets
- Resource Requirements (team, tools, budget)

### Platform Setup Guide (`platform-setup-{platform}-{YYYY-MM-DD}.md`)
Sections:
- Account and Workspace Configuration
- Channel/Space Structure table (Channel, Purpose, Access, Moderation)
- Roles and Permissions table (Role, Permissions, Criteria)
- Bot/Integration Setup
- Onboarding Flow
- Moderation Configuration
- Launch Checklist

### Engagement Calendar (`engagement-calendar-{YYYY-MM}.md`)
Sections:
- Monthly Theme
- Weekly Rhythm table (Day, Activity Type, Description, Owner)
- Events Schedule table (Date, Event, Format, Host, Promotion Plan)
- Challenges and Campaigns
- Content Prompts (pre-written)
- Member Spotlight Schedule

### Moderation Guidelines (`moderation-guidelines-{YYYY-MM-DD}.md`)
Sections:
- Code of Conduct
- Moderation Team and Roles
- Response Templates (Welcome / Warning / Mute / Ban)
- Escalation Procedures table (Severity, Action, Timeline, Escalation)
- Conflict Resolution Process
- Moderation Log Template
- Review and Update Schedule

### Community Launch Plan (`community-launch-plan-{YYYY-MM-DD}.md`)
Sections:
- Community Promise
- Pre-Launch (Weeks 1-4) table (Week, Action, Owner, Status)
- Founding Member Recruitment table (Target, Outreach Channel, Message Template, Goal)
- Beta Phase (Weeks 5-6)
- Public Launch (Week 7+)
- Launch Week Event
- Seed Content (pre-written posts)
- Announcement Copy (email, social, in-product)
- 30-Day Post-Launch Plan
- Success Criteria

## Quick Reference

For operational checklists, look up `quick-reference-checklists` in `./references/frameworks-index.csv` and read the referenced file. Includes pre-launch, launch week, and weekly operations checklists.

## Response Protocol

When the user requests community building or management work:

1. Read brand context and SOSTAC when available; otherwise proceed from repo, live URL, existing assets, or user-provided context.
2. Clarify scope: Strategy, platform setup, engagement programs, moderation, launch plan, community-led growth, metrics, or full community build?
3. Assess current state: Check resolved path for prior work.
4. Deliver actionable output: Specific strategies, setup guides, engagement calendars, launch plans -- never vague advice.
5. Save deliverables: Write all outputs to resolved path.
6. Recommend first move: What to build first, who to invite, what to measure.