# Deliverables & Outputs

Production-ready deliverables for paid advertising campaigns. For complete templates, see `./references/deliverable-templates.md`.

---

## Deliverable Types

### 1. Campaign Brief
Full strategic brief covering objective, audience, structure, copy, bidding, tracking, and testing plan.

**Save as:** `campaign-brief-{campaign-name}-{YYYY-MM-DD}.md`

### 2. Ad Copy Document
Platform-specific ad copy with multiple angle/hook variants, character count verification, and testing priority.

**Save as:** `ad-copy-{platform}-{campaign}-{YYYY-MM-DD}.md`

### 3. Audience Targeting Spec
Cold/warm/hot audience definitions with targeting criteria, estimated sizes, exclusions, and lookalike strategy.

**Save as:** `audience-spec-{platform}-{YYYY-MM-DD}.md`

### 4. Budget Allocation Plan
Platform and funnel-stage budget splits with scaling rules and reallocation triggers.

**Save as:** `budget-plan-{YYYY-MM}.md`

### 5. Performance Benchmarks
Industry and funnel-stage benchmarks with optimization thresholds.

**Save as:** `benchmarks-{platform}-{YYYY-MM-DD}.md`

See also: `./references/benchmarks.md` for cross-platform industry benchmark data.

### 6. A/B Testing Plan
Hypothesis, variables, control/variant setup, sample size, and decision framework.

**Save as:** `ab-test-plan-{test-name}-{YYYY-MM-DD}.md`

---

## File Organization

### Campaign mode:
```
./.pawbytes/marketing-suites/brands/{brand-slug}/campaigns/{type}-{campaign-slug}/channels/paid-ads/content/
  campaign-brief-{name}-{YYYY-MM-DD}.md
  ad-copy-{platform}-{campaign}-{YYYY-MM-DD}.md
  audience-spec-{platform}-{YYYY-MM-DD}.md
  budget-plan-{YYYY-MM}.md
```

### Standalone mode (default for evergreen work):
```
./.pawbytes/marketing-suites/brands/{brand-slug}/channels/paid-ads/content/
  campaign-brief-{name}-{YYYY-MM-DD}.md
  ad-copy-{platform}-{campaign}-{YYYY-MM-DD}.md
  audience-spec-{platform}-{YYYY-MM-DD}.md
  budget-plan-{YYYY-MM}.md
  benchmarks-{platform}-{YYYY-MM-DD}.md
  ab-test-plan-{name}-{YYYY-MM-DD}.md
  performance/
    monthly-report-{YYYY-MM}.md
  creative/
    video-scripts/
    ad-copy-archive/
```

---

## Output Contract

Paid ads deliverables include:
- **Platform:** Google, Meta, LinkedIn, TikTok, etc.
- **Campaign type:** search, display, video, shopping, etc.
- **Audience definition:** targeting parameters
- **Ad copy/creative:** headlines, descriptions, CTAs per ad format
- **Budget recommendation:** daily/monthly spend with reasoning
- **KPIs:** target CPA, ROAS, or CTR benchmarks
- **File saved to:** path where the deliverable was written

---

## Response Protocol

When the user requests paid ads work:

1. **Read brand context and SOSTAC** when available; otherwise proceed from the codebase, live site, tracking setup, existing creative assets, or user-provided context
2. **Clarify scope:** Which platform? Campaign type? Funnel stage? New campaign or optimization?
3. **Assess current state:** Check the resolved path for prior work
4. **Deliver actionable output:** Specific campaigns, copy, audiences, budgets - never vague advice
5. **Save deliverables:** Write all outputs to the resolved path
6. **Recommend next steps:** What to launch first, what to test, when to optimize

---

## When to Escalate

- No conversion tracking set up - recommend implementation before spending
- No landing page - recommend building one before driving traffic
- Budget under $500/month - recommend focusing on 1 platform only
- Heavily regulated industry (pharma, finance, alcohol) - flag platform-specific ad policies
- SEO may be more cost-effective - route to SEO specialist for organic opportunities