# Routing Patterns

This document explains how coordinator skills route requests to specialists in multi-skill modules.

## Overview

Marketing and Creative modules use a **coordinator pattern** where a central agent routes requests to specialized skills.

```
User Request
     │
     ▼
┌─────────────────────┐
│    Coordinator      │
│                     │
│  • Load brand       │
│  • Analyze request  │
│  • Route to         │
│    specialist       │
└──────────┬──────────┘
           │
           │ Route based on request type
           │
    ┌──────┴──────┬──────────────┬─────────────┐
    ▼             ▼              ▼             ▼
┌─────────┐ ┌─────────┐ ┌─────────────┐ ┌─────────┐
│SEO      │ │Content  │ │Paid Ads     │ │Email    │
│Specialist│ │Specialist│ │Specialist  │ │Specialist│
└─────────┘ └─────────┘ └─────────────┘ └─────────┘
```

## Coordinator Pattern

### When to Use

| Pattern | Best For |
|---------|----------|
| **Coordinator** | Multi-skill modules, complex routing, brand context management |
| **Direct** | Simple skills, utility functions, single-purpose tools |

### Coordinator Responsibilities

1. **Context Loading** — Read brand workspace, SOSTAC progress, active campaigns
2. **Request Analysis** — Determine what type of work is needed
3. **Routing** — Direct to appropriate specialist
4. **Coordination** — Manage multi-specialist projects
5. **Progress Tracking** — Update status files

## Marketing Module Routing

### Coordinator: paw-mkt-agent-agency

```
paw-mkt-agent-agency (Coordinator)
    │
    ├── paw-mkt-sostac         (SOSTAC planning)
    ├── paw-mkt-product-context (Positioning, personas)
    ├── paw-mkt-seo            (Technical/content SEO)
    ├── paw-mkt-content        (Content marketing)
    ├── paw-mkt-email          (Email sequences)
    ├── paw-mkt-social         (Social media)
    ├── paw-mkt-paid-ads       (PPC, retargeting)
    ├── paw-mkt-video          (Video scripts)
    ├── paw-mkt-pr             (Press, crisis)
    ├── paw-mkt-influencer     (Creator partnerships)
    ├── paw-mkt-cro            (Conversion optimization)
    ├── paw-mkt-referral       (Referral programs)
    ├── paw-mkt-retention      (Churn reduction)
    ├── paw-mkt-pricing        (Pricing strategy)
    ├── paw-mkt-launch         (GTM, Product Hunt)
    ├── paw-mkt-sales          (Sales enablement)
    ├── paw-mkt-community      (Discord/Slack)
    ├── paw-mkt-analytics      (Dashboards)
    ├── paw-mkt-guerrilla      (Growth hacks)
    ├── paw-mkt-psychology     (Behavioral)
    └── paw-mkt-dashboard      (Visualization)
```

### Routing Table

```markdown
## Escalation Routes

| Signal | Routes To |
|--------|-----------|
| SEO, keywords, technical audit | paw-mkt-seo |
| Content, blog, editorial | paw-mkt-content |
| Paid ads, PPC, retargeting | paw-mkt-paid-ads |
| Email sequences, newsletters | paw-mkt-email |
| Social media, organic | paw-mkt-social |
| Influencer, creator partnerships | paw-mkt-influencer |
| PR, press, crisis comms | paw-mkt-pr |
| CRO, conversion optimization | paw-mkt-cro |
| Launch, GTM, Product Hunt | paw-mkt-launch |
| Pricing, packaging | paw-mkt-pricing |
| Retention, churn, dunning | paw-mkt-retention |
| Community, Discord/Slack | paw-mkt-community |
| Referral, affiliate, partnerships | paw-mkt-referral |
| Sales enablement, decks | paw-mkt-sales |
| Analytics, tracking, dashboards | paw-mkt-analytics |
| Video, YouTube, TikTok | paw-mkt-video |
| Psychology, persuasion | paw-mkt-psychology |
| Guerrilla, growth hacks | paw-mkt-guerrilla |
| Positioning, personas, ICP | paw-mkt-product-context |
| SOSTAC planning | paw-mkt-sostac |
| Dashboard visualization | paw-mkt-dashboard |
```

## Creative Module Routing

### Coordinator: paw-cra-agent-creative-director (Aria)

```
paw-cra-agent-creative-director (Aria - Coordinator)
    │
    ├── paw-cra-agent-designer      (Visual production)
    ├── paw-cra-agent-video-producer (Video production)
    └── paw-cra-agent-strategist    (Research - on demand)
```

### Production-First Routing

**Key Principle:** Route based on OUTPUT TYPE, not analysis.

```
User Request
     │
     ├── "Create a social post" ──────► Designer (directly)
     │
     ├── "Make a short video" ────────► Video Producer (directly)
     │
     ├── "Research competitors" ──────► Strategist (on demand)
     │
     └── "Campaign with multiple
          deliverables" ──────────────► campaign-orchestration workflow
```

### Routing Decision Tree

```
                        User Request
                             │
                             ▼
                 ┌───────────────────────┐
                 │ What is the OUTPUT     │
                 │ type requested?        │
                 └───────────┬───────────┘
                             │
        ┌────────────────────┼────────────────────┐
        │                    │                    │
        ▼                    ▼                    ▼
   Images/Graphics      Video/Motion        Research/Copy
        │                    │                    │
        ▼                    ▼                    ▼
   ┌─────────┐        ┌───────────┐        ┌───────────┐
   │ Designer│        │  Video    │        │Strategist │
   │         │        │ Producer  │        │(on-demand)│
   └─────────┘        └───────────┘        └───────────┘
```

### When to Involve Strategist

**Invoke Strategist when:**
- User explicitly asks for research, strategy, or content planning
- Production agents need copy/scripts not in the brief
- Campaign planning requires competitive analysis
- User wants a content calendar before production

**Do NOT invoke Strategist when:**
- User provides complete brief with copy/specs
- User says "create a social post about X"
- User says "make a short video about X"

### Specialist Skills Table

```markdown
## Specialist Agents

| Specialist | Skill Name | When to Invoke |
|------------|------------|----------------|
| Designer | paw-cra-agent-designer | Visual assets — social posts, carousels, flyers, logos |
| Video Producer | paw-cra-agent-video-producer | Video content — short-form, long-form, motion |
| Strategist | paw-cra-agent-strategist | On demand — research, scripts, copy |
```

## Routing Implementation

### Escalation Routes Section

Skills define routing in an escalation table:

```markdown
## Escalation Routes

| Signal | Routes To |
|--------|-----------|
| User needs pricing strategy | paw-mkt-pricing |
| User needs content plan | paw-mkt-content |
| User needs video script | paw-mkt-video |
```

### Programmatic Routing

Coordinators can route based on conditions:

```markdown
## Response Protocol

1. **Assess the request** — Determine if this is:
   - New brand onboarding
   - SOSTAC routing
   - Campaign coordination
   - Direct specialist request

2. **Read brand context** — Check existing workspace before recommending

3. **Route or coordinate** — For single-skill, route directly.
   For multi-channel, assess SOSTAC readiness and spawn teams.
```

## Multi-Skill Orchestration

### Team Spawning

For multi-channel work, coordinators spawn teams:

```
┌─────────────────┐
│   Coordinator   │
│                 │
│ Assess SOSTAC   │
│ readiness       │
└────────┬────────┘
         │
         │ SOSTAC 4/6 complete
         │ (Tactics defined)
         ▼
┌─────────────────┐
│  Spawn Team     │
│                 │
│ • SEO          │
│ • Content      │
│ • Email        │
└─────────────────┘
```

### Campaign Orchestration

The `paw-cra-campaign-orchestration` workflow coordinates multiple specialists:

```
paw-cra-campaign-orchestration
    │
    ├── Dispatcher for Designer
    ├── Dispatcher for Video Producer
    └── Optional: Strategist (on demand)
```

## Routing vs Direct Invocation

### When to Route Through Coordinator

- User's intent is ambiguous
- Brand context needs to be loaded
- Multi-skill coordination needed
- Progress tracking required

### When to Invoke Directly

- User explicitly names the skill
- Request is clearly single-purpose
- No brand context needed
- Simple utility function

## Example Routing Scenarios

### Scenario 1: Ambiguous Request

```
User: "Help me with marketing"

Coordinator (paw-mkt-agent-agency):
1. Load brand context
2. Check SOSTAC progress
3. Ask clarifying questions
4. Route to appropriate specialist
```

### Scenario 2: Direct Specialist Request

```
User: "I need an SEO audit for my site"

Coordinator:
- Recognizes SEO trigger
- Routes directly to paw-mkt-seo

paw-mkt-seo:
- Loads technical-audit framework
- Executes audit methodology
- Reports findings
```

### Scenario 3: Multi-Channel Campaign

```
User: "Launch a new product"

Coordinator:
1. Check SOSTAC progress
2. If Tactics phase incomplete → paw-mkt-sostac
3. If Tactics defined → Spawn team:
   - paw-mkt-launch (GTM)
   - paw-mkt-content (launch content)
   - paw-mkt-social (social launch)
   - paw-mkt-email (launch sequence)
```

### Scenario 4: Creative Production

```
User: "Create a carousel for Instagram"

Aria (Coordinator):
- Recognizes visual output type
- Routes directly to Designer
- Does NOT require Strategist validation

Designer:
- Loads brand guidelines
- Creates carousel
- Outputs to brand workspace
```

## Best Practices

### For Coordinators

1. **Read before routing** — Always check existing context
2. **Explain routing decisions** — Tell user why you're routing
3. **Track progress** — Update status files after routing
4. **Recommend next steps** — Suggest logical next actions

### For Specialists

1. **Accept context from coordinator** — Don't re-read what was loaded
2. **Report completion** — Update status after work
3. **Escalate appropriately** — Route to other specialists when needed
4. **Save to correct paths** — Follow path resolution rules