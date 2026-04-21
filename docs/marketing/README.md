# Marketing Suite (paw-mkt-*)

The Marketing Suite provides 23 skills covering the full marketing stack -- from strategic planning through channel execution to analytics and optimization.

## Quick Navigation

| I want to... | Go to |
|--------------|-------|
| Get started with marketing | [User Guide: Introduction & Quickstart](./user-guide/part-1-2-introduction-quickstart.md) |
| Plan marketing strategy | [User Guide: SOSTAC Planning](./user-guide/part-3-chapters-5-6.md) |
| Create content & campaigns | [User Guide: Content & Social](./user-guide/part-3-chapters-7-8.md) |
| Execute across channels | [User Guide: Workflow Architecture](./user-guide/part-4-workflow-architecture.md) |
| Set up a new brand | [Workflow: New Brand Onboarding](./workflows/new-brand-onboarding.md) |
| Understand deliverables | [Reference: Deliverables & File Locations](./reference/deliverables-and-file-locations.md) |

## Skill Categories

### Coordinator & Planning
- [paw-mkt-agent-agency](./skills/paw-mkt-agent-agency.md) -- Central coordinator, routes to specialists
- [paw-mkt-sostac](./skills/paw-mkt-sostac.md) -- SOSTAC marketing planning
- [paw-mkt-product-context](./skills/paw-mkt-product-context.md) -- Product marketing context

### Channel Execution
- [paw-mkt-content](./skills/paw-mkt-content.md) -- Content strategy and production
- [paw-mkt-email](./skills/paw-mkt-email.md) -- Email marketing campaigns
- [paw-mkt-seo](./skills/paw-mkt-seo.md) -- SEO optimization
- [paw-mkt-social](./skills/paw-mkt-social.md) -- Social media marketing
- [paw-mkt-video](./skills/paw-mkt-video.md) -- Video marketing
- [paw-mkt-paid-ads](./skills/paw-mkt-paid-ads.md) -- Paid advertising
- [paw-mkt-pr](./skills/paw-mkt-pr.md) -- Public relations
- [paw-mkt-influencer](./skills/paw-mkt-influencer.md) -- Influencer marketing
- [paw-mkt-referral](./skills/paw-mkt-referral.md) -- Referral programs
- [paw-mkt-community](./skills/paw-mkt-community.md) -- Community building
- [paw-mkt-guerrilla](./skills/paw-mkt-guerrilla.md) -- Guerrilla marketing

### Conversion & Revenue
- [paw-mkt-cro](./skills/paw-mkt-cro.md) -- Conversion rate optimization
- [paw-mkt-retention](./skills/paw-mkt-retention.md) -- Customer retention
- [paw-mkt-pricing](./skills/paw-mkt-pricing.md) -- Pricing strategy
- [paw-mkt-launch](./skills/paw-mkt-launch.md) -- Product launches
- [paw-mkt-sales](./skills/paw-mkt-sales.md) -- Sales enablement
- [paw-mkt-psychology](./skills/paw-mkt-psychology.md) -- Marketing psychology

### Measurement
- [paw-mkt-analytics](./skills/paw-mkt-analytics.md) -- Analytics and reporting
- [paw-mkt-dashboard](./skills/paw-mkt-dashboard.md) -- Dashboard builder (SvelteKit)

## Workflows

- [New Brand Onboarding](./workflows/new-brand-onboarding.md) -- Set up a new brand workspace
- [SOSTAC Planning](./workflows/sostac-planning.md) -- Create a marketing strategy
- [Implementation After SOSTAC](./workflows/implementation-after-sostac.md) -- Execute your plan
- [Quick Task Without Full Plan](./workflows/quick-task-without-full-plan.md) -- One-off deliverables

## Reference

- [Brand Workspace](./reference/brand-workspace.md) -- How brand context works
- [Common Patterns](./reference/common-patterns.md) -- Reusable patterns
- [Deliverables & File Locations](./reference/deliverables-and-file-locations.md) -- Output structure
- [Skill Workflow Roadmap](./reference/skill-workflow-roadmap.md) -- Skill selection guide
- [Glossary](./reference/glossary.md) -- Terms and definitions
- [Shared Patterns](./reference/shared-patterns.md) -- Cross-skill patterns

## How the Suite Flows

```mermaid
flowchart TD
    A[paw-mkt-agent-agency] --> B{Strategy exists?}
    B -- No --> C[paw-mkt-sostac]
    C --> D[paw-mkt-product-context]
    B -- Yes --> D
    D --> E[Specialist skills]
    E --> F[.pawbytes/marketing-suites/brands/{brand-slug}/]
    F --> G[paw-mkt-analytics]
    F --> H[paw-mkt-dashboard]
```

## Design Principle

Most skills are file-producing workflows, not just prompt generators. Outputs accumulate in `.pawbytes/marketing-suites/brands/{brand-slug}/` so future sessions can resume from real artifacts instead of memory.