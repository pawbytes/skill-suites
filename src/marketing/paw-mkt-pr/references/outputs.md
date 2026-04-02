# Outputs and Deliverables

> File organization, path resolution, and response protocol for PR deliverables.

## Path Resolution: Campaign vs Standalone

**Campaign mode** -- working within a named campaign:
```
./.pawbytes/marketing-suites/brands/{brand-slug}/campaigns/{type}-{campaign-slug}/channels/pr/content/
```
Read campaign strategy at `./.pawbytes/marketing-suites/brands/{brand-slug}/campaigns/{type}-{campaign-slug}/strategy.md`

**Standalone mode** -- evergreen or independent work:
```
./.pawbytes/marketing-suites/brands/{brand-slug}/channels/pr/content/
```

**Legacy fallback** -- old directory structure detected:
```
./.pawbytes/marketing-suites/brands/{brand-slug}/campaigns/pr/
```
Suggest migration to new structure.

If unsure which mode, ask: "Is this part of a specific campaign, or standalone work?"

## File Organization

```
## Campaign mode:
./.pawbytes/marketing-suites/brands/{brand-slug}/campaigns/{type}-{campaign-slug}/channels/pr/content/
  pr-strategy-{YYYY-MM-DD}.md
  pitch-templates-{YYYY-MM-DD}.md          # customized from ./references/frameworks/
  press-releases/
    press-release-{slug}-{YYYY-MM-DD}.md
  media-lists/
    media-list-{campaign}-{YYYY-MM-DD}.md
  campaign-briefs/
    pr-campaign-{name}-{YYYY-MM-DD}.md

## Standalone mode (default for evergreen work):
./.pawbytes/marketing-suites/brands/{brand-slug}/channels/pr/content/
  pr-strategy-{YYYY-MM-DD}.md
  pitch-templates-{YYYY-MM-DD}.md          # customized from ./references/frameworks/
  crisis-plan-{YYYY-MM-DD}.md
  media-kit-{YYYY-MM-DD}.md
  press-releases/
    press-release-{slug}-{YYYY-MM-DD}.md
  media-lists/
    media-list-{campaign}-{YYYY-MM-DD}.md
  campaign-briefs/
    pr-campaign-{name}-{YYYY-MM-DD}.md
  spokesperson-prep/
    spokesperson-prep-{topic}-{YYYY-MM-DD}.md
  performance/
    pr-report-{YYYY-MM}.md
```

## Deliverable Types

**PR Strategy** (`pr-strategy-{YYYY-MM-DD}.md`): SOSTAC alignment, objectives, target audience, key messages, media tier targets, PR-SEO plan, campaign calendar, budget, success metrics.

**Press Release** (`press-releases/press-release-{slug}-{YYYY-MM-DD}.md`): Standard structure with distribution plan.

**Pitch Templates** (`pitch-templates-{YYYY-MM-DD}.md`): Exclusive, data story, expert commentary, trend, product launch pitches customized per campaign. Base templates in `./references/frameworks/`.

**Media List** (`media-lists/media-list-{campaign}-{YYYY-MM-DD}.md`): Standard template with outreach status.

**Crisis Plan** (`crisis-plan-{YYYY-MM-DD}.md`): Team, tiers, holding statements, channels, escalation.

**Media Kit** (`media-kit-{YYYY-MM-DD}.md`): Company overview, key facts, leadership bios, brand assets, recent coverage.

**Campaign Brief** (`campaign-briefs/pr-campaign-{name}-{YYYY-MM-DD}.md`): Objective, news hook, target media by tier, key messages, spokesperson, assets, distribution plan, timeline, link targets, metrics.

**Spokesperson Prep** (`spokesperson-prep/spokesperson-prep-{topic}-{YYYY-MM-DD}.md`): Key messages, proof points, bridging phrases, difficult questions with responses, off-limits topics.

**Performance Report** (`performance/pr-report-{YYYY-MM}.md`): Monthly summary, mentions by tier/sentiment, backlinks, referral traffic, share of voice, HARO stats, recommendations.

## Response Protocol

When the user requests PR work:

1. **Read brand context and SOSTAC** when available; otherwise proceed from the repo, newsroom assets, live website or profile footprint, or user-provided context
2. **Clarify scope**: PR strategy, press release, journalist outreach, crisis plan, media kit, spokesperson prep, reputation management, or digital PR campaign?
3. **Assess current state**: Check the resolved path for prior deliverables
4. **Deliver actionable output**: Specific press releases, pitch templates, media lists, crisis plans, and campaign briefs -- never vague advice
5. **Save deliverables**: Write all outputs to the resolved path
6. **Recommend next steps**: What to pitch first, which journalists to prioritize, when to follow up

## Output Contract

PR deliverables include:
- **PR type**: press release, media pitch, crisis plan, media kit, spokesperson prep, or digital PR campaign
- **Target media**: specific publications, journalists, or outlets
- **Key message**: core narrative and supporting proof points
- **Distribution plan**: outreach sequence and follow-up timeline
- **Success metrics**: coverage targets, backlink goals, or sentiment benchmarks
- **File saved to**: path where the deliverable was written