# Agentic Marketing Skills: User Guide

## Part 1: Introduction

---

# Chapter 1: What is Agentic Marketing?

## 1.1 The Vision: Your AI-Powered Marketing Department

Imagine having a full-service marketing agency at your fingertips—one that understands your brand, remembers your strategy, and can execute across every marketing channel without you needing to manage a team of specialists or learn complex marketing tools.

That is what the Pawbytes Marketing Suite delivers.

This system transforms AI assistants into a coordinated marketing team. Instead of generic, one-off responses, you get strategic planning, brand-aligned execution, and specialist expertise that builds on previous work. It is like hiring a marketing department that never forgets, works 24/7, and scales infinitely.

**What makes this different from asking an AI for marketing help?**

| Traditional AI Assistance | Agentic Marketing |
| --- | --- |
| Generic advice without context | Brand-specific recommendations based on your stored brand identity |
| One-off answers with no memory | Builds a complete plan across multiple sessions |
| You explain your business every time | Brand context is saved and reused automatically |
| No structured approach | Follows proven marketing frameworks (SOSTAC, RACE, etc.) |
| Single-channel focus | Coordinates across SEO, email, social, content, paid ads, and more |
| You manage execution | Specialist skills execute and save deliverables |

The system is designed around one core principle: **Read before acting.** Every response is grounded in your existing brand context, strategic plan, and previous work. You never get generic advice disconnected from your reality.

---

## 1.2 Who This Guide is For

This guide is written for **non-technical users** who want professional marketing results without hiring an agency or learning marketing theory.

**Primary audiences:**

### Solo Entrepreneurs and Founders
You are building a business and need marketing, but cannot afford a full team yet. You want strategy and execution without the overhead. This system lets you start with strategic planning and add channels as you grow.

### Small Business Owners
You have an established business but marketing feels scattered. You need structure—a plan that ties everything together. This system helps you build a cohesive strategy before executing across channels.

### Marketing Teams Without Specialists
You have generalist marketers who need to deliver specialist work. They can use this system to produce SEO audits, email sequences, content calendars, and paid ad strategies without deep expertise in each area.

### Anyone Who Has Asked an AI for Marketing Help and Been Frustrated
You tried using AI for marketing but got generic advice that did not fit your business. The responses felt disconnected from your actual situation. This system solves that problem by maintaining context.

**What you do NOT need:**

- Marketing certification or degree
- Technical coding skills
- Experience with marketing automation platforms
- Knowledge of marketing frameworks (the system applies them for you)

**What you DO need:**

- A clear description of what your brand sells and who it serves
- Willingness to answer a few strategic questions when asked
- A Claude Code environment (the AI assistant this system runs within)

---

## 1.3 The Problems It Solves

Most businesses face the same marketing challenges. This system addresses them directly.

### Problem 1: Marketing Expertise Gap

**The situation:** You know you need SEO, email marketing, content, social media, and paid ads. But you do not have specialists in each area. Generalist advice online is overwhelming and often contradictory.

**How this solves it:** The system includes 20 specialist skills covering every major marketing discipline. Each specialist has deep knowledge in their area and follows proven frameworks. You get specialist-quality work without hiring specialists.

**Example:** Instead of googling "how to write an email welcome sequence" and piecing together 10 articles, you describe your product and audience. The Email Marketing Specialist produces a complete sequence with subject lines, content, timing, and segmentation logic.

---

### Problem 2: Strategy-to-Execution Disconnect

**The situation:** You have a marketing plan (or think you do), but execution does not match it. Your blog posts do not support your SEO goals. Your emails do not match your brand voice. Your social posts feel random.

**How this solves it:** The system builds strategy first (using SOSTAC), then executes from that plan. Every deliverable references the strategic context. Specialists read your brand identity and SOSTAC phases before producing anything.

**Example:** Your Strategy phase identifies LinkedIn as a key channel for B2B lead generation. When you request social content, the Social Media Specialist reads that decision and produces LinkedIn-specific thought leadership content—not random Instagram memes.

---

### Problem 3: Channel Silos

**The situation:** Your SEO person does not talk to your content person. Your email campaigns ignore what you post on social. Paid ads target audiences your organic content never reached. Marketing feels fragmented.

**How this solves it:** All channels coordinate through a single strategic plan stored in your brand workspace. The Tactics phase defines which channels to use and how they work together. Each specialist reads the same source of truth.

**Example:** Your Tactics phase calls for a "Black Friday launch campaign" across email, social, and paid ads. Each specialist produces content for their channel, but all content shares the same messaging framework, timing, and audience targeting defined in the campaign strategy.

---

### Problem 4: Budget Inefficiency

**The situation:** You spend money on marketing without knowing if it works. You try channels because someone recommended them, not because they fit your situation. Budget allocation feels like guesswork.

**How this solves it:** The SOSTAC framework builds measurement into every phase. The Control phase defines what to track. The Budget Allocation framework helps you distribute spend based on your business stage and channel priorities.

**Example:** Instead of "let's try Facebook ads," your Tactics phase recommends testing channels using the Bullseye Framework. You run small experiments, measure results with defined KPIs, then scale what works. Budget goes to proven channels, not guesses.

---

### Problem 5: Inconsistent Messaging

**The situation:** Your website says one thing. Your emails say another. Your social posts use different language. Customers are confused about what you actually offer.

**How this solves it:** A single brand-context.md file defines your brand identity, voice, audience, and unique selling proposition. Every specialist reads this file before producing content. Messaging stays consistent across all channels.

**Example:** Your brand context defines your USP as "the only project management tool designed specifically for creative agencies." Your SEO specialist targets keywords related to creative agency workflows. Your email specialist writes subject lines like "Stop managing creative projects like generic tasks." Your content specialist writes case studies featuring creative agencies. Same message, every channel.

---

## 1.4 Key Concepts in Plain Language

Before diving into how the system works, understand these core concepts.

### Skills

A **skill** is a specialized capability the AI can activate. Think of skills as team members with specific expertise.

**Example skills:**
- `paw-mkt-agent-agency` — The coordinator who manages the whole team
- `paw-mkt-sostac` — The strategist who builds your marketing plan
- `paw-mkt-seo` — The SEO specialist
- `paw-mkt-email` — The email marketing specialist
- `paw-mkt-content` — The content strategist
- `paw-mkt-paid-ads` — The paid media manager

The suite includes a broad set of marketing specialists, each covering a specific marketing discipline.

When you make a request, the coordinator skill decides which specialist(s) to activate. You do not need to know skill names—the system routes automatically.

---

### Brand Context

**Brand context** is a file that stores your brand identity. It includes:

- Your brand name and what you sell
- Your target audience
- Your unique selling proposition (what makes you different)
- Your brand voice and personality
- Key competitors
- Current marketing status

This file lives in `./.pawbytes/marketing-suites/brands/{your-brand-slug}/brand-context.md`.

**Why it matters:** Every specialist reads this file before producing deliverables. This ensures everything they create aligns with your brand. You set it once, and it grounds all future work.

**How it gets created:** When you first interact with the system, it asks a few questions and creates this file for you.

---

### SOSTAC

**SOSTAC** is a marketing planning framework used by professional strategists worldwide. It stands for:

| Phase | What It Covers |
| --- | --- |
| **S** — Situation | Where are you now? Market analysis, competitors, current state. |
| **O** — Objectives | Where do you want to go? Goals, KPIs, targets. |
| **S** — Strategy | How do you get there? Big-picture approach, positioning, segments. |
| **T** — Tactics | How exactly? Channels, activities, tools. |
| **A** — Action | What is the timeline? Tasks, milestones, who does what. |
| **C** — Control | How do you measure success? Metrics, review cycles, optimization. |

The system builds your marketing plan through these six phases in order. Each phase saves a document in your brand workspace. Later phases build on earlier ones.

**Why it matters:** SOSTAC ensures your marketing is strategic, not random. You define goals before tactics. You measure before executing. The framework connects everything.

**What you do:** Answer questions at each phase. The system does the research, analysis, and documentation. You review and approve.

---

### Frameworks

**Frameworks** are proven models that structure marketing decisions. The system uses many frameworks, but you do not need to learn them—they are applied automatically based on your situation.

**Example frameworks:**

| Framework | What It Does |
| --- | --- |
| Bullseye Framework | Helps you find the best marketing channel through testing |
| AARRR Pirate Metrics | Defines what to measure at each stage of customer growth |
| RACE Framework | Structures execution across awareness to advocacy |
| See-Think-Do-Care | Maps content to customer intent levels |
| ICE Scoring | Helps prioritize which experiments to run first |
| Growth Loops | Identifies self-reinforcing viral/organic growth mechanisms |

The system has a **Framework Selection Guide** that chooses the right framework for each situation. You benefit from professional marketing models without studying them.

---

### Brand Workspace

Your **brand workspace** is a folder that stores everything related to your brand's marketing:

```
./brands/{your-brand-slug}/
  brand-context.md           # Your brand identity
  sostac/                    # Your marketing plan (6 phases)
    01-situation.md
    02-objectives.md
    03-strategy.md
    04-tactics.md
    05-action.md
    06-control.md
  campaigns/                 # Named marketing campaigns
  channels/                  # Standalone channel work
  operations/                # Specialist discipline work
```

**Why it matters:** This is your "source of truth." Every specialist reads from this workspace before acting. Everything they produce saves back here. You can see your entire marketing operation in one place.

---

# Chapter 2: How It Works

## 2.1 The "Marketing Team in a Box" Concept

Think of this system as a virtual marketing agency with you as the client.

**The team structure:**

- **Agency Coordinator** (`paw-mkt-agent-agency`) — The account director who manages everything. They greet you, understand your needs, route requests to specialists, and coordinate execution.

- **Strategist** (`paw-mkt-sostac`) — The senior strategist who builds your marketing plan through the SOSTAC framework.

- **Channel Specialists** — Experts in specific channels:
  - SEO Specialist (`paw-mkt-seo`)
  - Email Marketing Specialist (`paw-mkt-email`)
  - Social Media Manager (`paw-mkt-social`)
  - Content Strategist (`paw-mkt-content`)
  - Paid Media Manager (`paw-mkt-paid-ads`)
  - Video Strategist (`paw-mkt-video`)
  - PR Specialist (`paw-mkt-pr`)
  - Influencer Manager (`paw-mkt-influencer`)
  - Community Manager (`paw-mkt-community`)

- **Operational Specialists** — Experts in marketing disciplines:
  - CRO Specialist (`paw-mkt-cro`) — Conversion rate optimization
  - Retention Specialist (`paw-mkt-retention`) — Churn prevention
  - Launch Strategist (`paw-mkt-launch`) — Product launches
  - Pricing Strategist (`paw-mkt-pricing`) — Pricing strategy
  - Growth Hacker (`paw-mkt-guerrilla`) — Unconventional tactics
  - Referral Manager (`paw-mkt-referral`) — Referral programs
  - Sales Enablement Specialist (`paw-mkt-sales`) — Sales collateral
  - Psychology Strategist (`paw-mkt-psychology`) — Behavioral science
  - Analytics Analyst (`paw-mkt-analytics`) — Tracking and reporting

**How the team works together:**

1. You speak to the Coordinator (your main contact)
2. The Coordinator reads your brand workspace to understand context
3. The Coordinator routes your request to the appropriate specialist
4. The specialist reads your brand context and SOSTAC plan
5. The specialist produces deliverables and saves them to your workspace
6. The Coordinator reports back and offers next steps

You never need to remember specialist names or invoke them manually. The Coordinator handles routing automatically.

---

## 2.2 How Skills Communicate

Skills communicate through **files in your brand workspace**.

**The communication pattern:**

```
[You] --> [Coordinator reads brand files] --> [Coordinator routes to Specialist]
       --> [Specialist reads brand files + SOSTAC] --> [Specialist produces work]
       --> [Specialist saves to workspace] --> [Coordinator reports to you]
```

**Key files that enable communication:**

| File | What Specialists Read From It |
| --- | --- |
| `brand-context.md` | Brand identity, audience, voice, USP |
| `sostac/03-strategy.md` | Target segments, positioning, big-picture approach |
| `sostac/04-tactics.md` | Which channels to use, priorities, channel mix |
| `sostac/05-action.md` | Timeline, tasks, milestones |
| `campaigns/{name}/strategy.md` | Campaign-specific messaging and timing |

**Example communication flow:**

You ask: "Write a blog post about our product benefits."

1. Coordinator reads `brand-context.md` to know your brand name, voice, and USP
2. Coordinator reads `sostac/04-tactics.md` to confirm blog is an approved channel
3. Coordinator invokes Content Strategist skill
4. Content Strategist reads `brand-context.md` (for voice), `sostac/03-strategy.md` (for positioning), and any existing blog content in `channels/blog/content/`
5. Content Strategist writes the blog post
6. Content Strategist saves to `channels/blog/content/{post-slug}.md`
7. Coordinator confirms save and offers next steps

This pattern ensures every piece of work is grounded in your strategic context.

---

## 2.3 The Orchestrator Pattern

The system uses an **orchestrator pattern** where one skill manages others.

**Why orchestration matters:**

Without orchestration, you would need to:
- Know which specialist handles each request type
- Invoke specialists manually
- Ensure specialists have the right context
- Coordinate outputs across specialists
- Manage the overall workflow

With orchestration, the Coordinator handles all of this. You make requests naturally, and the system routes and coordinates automatically.

**The orchestration workflow:**

### Step 1: Context Assessment

When you make any marketing request, the Coordinator first assesses context:

- Do you have an existing brand workspace?
- Is SOSTAC planning complete or in progress?
- What is your current situation (pre-launch, early stage, established)?
- What context do you have (website URL, codebase, brand files, nothing)?

### Step 2: Routing Decision

Based on context assessment, the Coordinator routes to the appropriate workflow:

| Situation | Route |
| --- | --- |
| No brand workspace | Brand Onboarding workflow |
| Brand exists, no SOSTAC | Start SOSTAC planning |
| SOSTAC in progress | Resume at next incomplete phase |
| SOSTAC complete, wants to implement | Spawn implementation team |
| SOSTAC complete, wants specific task | Invoke relevant specialist |
| Multiple brands exist | Brand Selection workflow |

### Step 3: Specialist Invocation

The Coordinator invokes specialist skills as needed:

- For planning: invokes `paw-mkt-sostac`
- For SEO work: invokes `paw-mkt-seo`
- For email work: invokes `paw-mkt-email`
- And so on for each discipline

### Step 4: Progress Tracking

The Coordinator maintains progress across sessions:

- Updates SOSTAC phase completion status
- Tracks campaign progress
- Records what has been delivered
- Knows where to resume next time

---

## 2.4 Getting Started Requirements

To use this system, you need:

### Required

1. **Claude Code Environment** — This system runs within Claude Code, Anthropic's AI assistant for developers. You need Claude Code installed and configured.

2. **Agentic Marketing Skills Installed** — The skills must be installed in your Claude Code environment. Typically this means the skill files are in a `skills/` directory.

3. **A Business or Brand** — You need something to market. This can be a product, service, company, personal brand, or project. You should be able to describe what it is and who it serves.

### Recommended

1. **Website URL** — If you have a live website, the system can audit it and use it as context.

2. **Existing Marketing Materials** — Any existing content, campaigns, or strategy documents help the system understand your current state.

3. **Clear Business Goals** — Knowing what you want to achieve (sales, leads, awareness, etc.) helps the planning process move faster.

### Not Required

1. **Marketing Knowledge** — You do not need to know marketing frameworks, channels, or tactics. The system applies them.

2. **Technical Skills** — You do not need to code or use marketing automation tools. The system produces deliverables you can implement manually or with help.

3. **Existing Marketing Team** — The system replaces or supplements specialist roles.

4. **Large Budget** — The system works for businesses at any budget level. Planning happens before budget allocation.

---

## Part 2: Quick Start Guide

---

# Chapter 3: Your First Marketing Request

## 3.1 How to Start a Conversation

Starting is simple. Open Claude Code and type any marketing-related message.

**The system activates automatically when you:**
- Mention marketing, brand, campaign, or strategy
- Ask for help with a marketing task
- Provide a website URL for marketing review
- Ask about your business's growth or promotion

**Example starting messages:**

```
"Help me with marketing for my business"

"I need a marketing plan for my new product"

"I want to improve my website's SEO"

"Can you review my landing page and suggest improvements?"

"Help me write email sequences for my SaaS product"

"I need a content calendar for my blog"
```

Any of these will trigger the Marketing Agency Coordinator to activate and begin routing your request.

---

## 3.2 Example: "Help me with marketing"

Let's walk through what happens when you start with the simplest request: "Help me with marketing."

### What the Coordinator Does

**Step 1: Greet and Assess**

The Coordinator activates and greets you:

```
I'm your Marketing Agency Coordinator. I help manage your brands,
build strategic plans, and coordinate specialist teams for execution.

Let me check your current setup...
```

**Step 2: Check for Existing Brands**

The Coordinator scans for existing brand workspaces:

```
Looking in ./brands/ for existing work...
```

**Scenario A: No brands found**

If you have no existing brand workspace:

```
I found no brands in your portfolio.

Would you like to start marketing for a new brand? I'll help you:
1. Create a brand workspace
2. Define your brand identity
3. Build a strategic marketing plan
4. Execute across channels

Tell me about what you're marketing — what's the product or service,
and who is your target audience?
```

**Scenario B: One brand found**

If one brand workspace exists:

```
I found brand **Acme Tools** — a B2B SaaS for construction project management.
Status: SOSTAC 3/6 complete (Strategy phase done, Tactics next)

Would you like to:
1. Continue SOSTAC planning (finish Tactics phase)
2. Work on something else with this brand
3. Create a new brand
```

**Scenario C: Multiple brands found**

If multiple brand workspaces exist:

```
I found 3 brands in your portfolio:

  1. **Acme Tools** — B2B SaaS for construction project management
     Status: SOSTAC 3/6 complete | 2 active campaigns

  2. **Wellness App** — Personal fitness tracking mobile app
     Status: SOSTAC not started

  3. **Consulting Co** — Business strategy consulting services
     Status: SOSTAC complete | Implementing

Which brand would you like to work on? (Enter number, name, or "new")
```

---

### Step 3: Route Based on Situation

The Coordinator routes based on what it finds:

| What It Finds | Where It Routes |
| --- | --- |
| No brand workspace | Brand Onboarding (create brand-context.md) |
| Brand exists, no SOSTAC | Start SOSTAC planning from Situation phase |
| SOSTAC in progress | Resume at next incomplete phase |
| SOSTAC complete | Offer implementation or specific tasks |

---

## 3.3 What Happens Automatically

Several things happen automatically that you might not notice:

### Context Loading

When a brand workspace exists, the Coordinator automatically reads key files:

1. `brand-context.md` — To understand your brand identity
2. `sostac/README.md` — To check SOSTAC progress
3. Any completed SOSTAC phase files — To understand your strategy

You do not need to remind the system about your brand. It remembers.

### Framework Selection

When the Strategist works on SOSTAC phases, it automatically:

1. Reads the frameworks index (a catalog of available models)
2. Matches your situation to appropriate frameworks
3. Loads only the frameworks that fit your needs

You benefit from frameworks like Bullseye, AARRR, and Growth Loops without selecting them manually.

### Specialist Routing

When you request specific work, the Coordinator automatically:

1. Maps your request to the right specialist skill
2. Ensures the specialist has access to brand context
3. Coordinates output location

You do not need to know which specialist handles SEO versus content versus email.

### Progress Tracking

The Coordinator automatically:

1. Updates SOSTAC status after each phase completes
2. Records deliverables in your workspace
3. Knows where to resume if you return later

Your marketing work accumulates rather than resets each session.

---

## 3.4 Understanding the Output

The system produces several types of output. Here is how to interpret each.

### SOSTAC Phase Documents

Each SOSTAC phase produces a structured document saved to your workspace:

**Example: 01-situation.md**

```
# Situation Analysis — Acme Tools

## Executive Summary
Acme Tools operates in the construction project management SaaS market,
estimated at $2.3B annually with 12% YoY growth...

## Market Landscape
[Detailed analysis of market size, trends, segments]

## Competitive Analysis
[Assessment of key competitors with positioning map]

## Current State Assessment
[Review of existing marketing, assets, capabilities]

## SWOT Analysis
Strengths: [List]
Weaknesses: [List]
Opportunities: [List]
Threats: [List]

## TOWS Strategic Options
[Strategic options derived from SWOT]

## Key Insights
1. [Insight with evidence]
2. [Insight with evidence]
...

## Recommendations
[Specific recommendations with reasoning]
```

**How to use these documents:**

- Read the **Executive Summary** for the big picture
- Review **Key Insights** for actionable findings
- Check **Recommendations** for what to do next
- Reference detailed sections when making decisions

The Strategist does the research and analysis. You review and validate.

---

### Specialist Deliverables

Each specialist produces channel-specific outputs:

**SEO Specialist:**
- Technical SEO audit
- Keyword strategy
- Content optimization recommendations
- On-page SEO checklist

**Email Specialist:**
- Email sequence with subject lines, body copy, timing
- Segmentation logic
- A/B test recommendations

**Content Specialist:**
- Blog posts, articles, case studies
- Content calendar
- Content briefs for writers

**Paid Ads Specialist:**
- Campaign structure
- Ad copy variations
- Targeting recommendations
- Budget allocation

**How to use these deliverables:**

- Deliverables are implementation-ready
- You can use them directly or adapt them
- Each deliverable references your brand context
- Files are saved in your workspace for future reference

---

### Campaign Strategy Documents

When you create a campaign, the system produces a strategy document:

```
# Campaign: Spring Product Launch

## Meta
- Type: launch
- Brand: Acme Tools
- Created: 2024-03-15
- Status: Planning

## Objective
Drive 500 trial signups within 30 days of launch...

## Target Audience
Construction project managers at mid-size firms (50-200 employees)

## Channels
Email (announcement + sequence), LinkedIn (thought leadership),
Paid search (branded + competitor keywords), PR (industry press)

## Key Messages
1. "Finally, project management built for construction—not generic tools retrofitted"
2. "See why 50 construction firms switched this quarter"
...

## Timeline
| Phase | Dates | Activities |
| Pre-launch | Mar 15-22 | Email teaser, LinkedIn posts |
| Launch day | Mar 23 | Announcement email, PR release, paid ads live |
| Post-launch | Mar 24-Apr 22 | Nurture sequence, social engagement |
```

**How to use campaign documents:**

- Campaign strategy guides all channel work
- Each specialist reads this before producing channel content
- Timeline coordinates cross-channel execution
- Success metrics define what to track

---

## 3.5 Following Up and Iterating

After any deliverable, you can iterate naturally.

### Asking for Changes

```
"The email subject lines feel too formal. Can you make them more conversational?"

"Add a section about competitor pricing to the situation analysis."

"The blog post is good but needs more specific examples. Add 2-3 case examples."
```

The specialist reads your feedback and revises. Previous context is maintained.

### Requesting Next Steps

```
"What should we do next?"

"Start the Tactics phase"

"Write the first blog post from the content calendar"

"Set up tracking for the launch campaign"
```

The Coordinator suggests logical next steps based on your current progress.

### Building Over Time

Each session builds on previous work:

```
Session 1: Create brand workspace + start SOSTAC
Session 2: Complete SOSTAC Situation + Objectives phases
Session 3: Complete Strategy + Tactics phases
Session 4: Complete Action + Control phases
Session 5: Start implementation — spawn content specialist
Session 6: Review blog posts, request email sequence
Session 7: Create launch campaign, coordinate across channels
...
```

Your marketing operation grows systematically without resetting.

---

# Chapter 4: The Marketing Agency Coordinator

## 4.1 Your Primary Entry Point

The **Marketing Agency Coordinator** (`marketing-agency`) is your main contact for every marketing request.

**Why it is the primary entry point:**

- It greets you and understands your needs
- It maintains awareness of your brand portfolio
- It routes requests to appropriate specialists
- It coordinates work across specialists
- It tracks progress across sessions

**You should start most conversations through the Coordinator.** It handles routing so you do not need to know specialist names or invoke them manually.

---

## 4.2 What It Does Automatically

The Coordinator performs several actions without you requesting them:

### On Every Interaction

1. **Load Configuration** — Reads your preferences from config files
2. **Check Brand Portfolio** — Scans `./brands/` for existing workspaces
3. **Read Brand Context** — If a brand is active, reads its context files
4. **Check SOSTAC Status** — Determines where planning stands
5. **Assess Context Type** — Determines if you have a codebase, URL, or blank-page situation

### On Routing Decisions

1. **Match Request to Workflow** — Determines if you need planning, specialist work, or campaign coordination
2. **Invoke Specialist** — Calls the appropriate skill
3. **Provide Context** — Points the specialist to relevant brand files
4. **Coordinate Output** — Ensures deliverables save to correct locations

### On Progress Tracking

1. **Update Status Files** — Marks phases complete, records deliverables
2. **Maintain Resume Point** — Knows where you left off
3. **Report to You** — Summarizes what was done and suggests next steps

---

## 4.3 Brand Selection Workflow

When you have multiple brands, the Coordinator presents a selection prompt.

**Example selection prompt:**

```
I found 3 brands in your portfolio:

  1. **Acme Tools** — B2B SaaS for construction project management
     Status: SOSTAC 3/6 complete | 2 active campaigns

  2. **Wellness App** — Personal fitness tracking mobile app
     Status: SOSTAC not started

  3. **Consulting Co** — Business strategy consulting services
     Status: SOSTAC complete | Implementing

Which brand would you like to work on? (Enter number, name, or "new")
```

**How to respond:**

| Your Response | What Happens |
| --- | --- |
| "1" or "Acme Tools" | Selects that brand, loads context, suggests next steps |
| "2" | Selects Wellness App, offers to start SOSTAC |
| "new" | Starts Brand Onboarding for a new brand |
| "all" | Offers to work sequentially or compare |

**What the Coordinator does after selection:**

1. Reads `brand-context.md` for that brand
2. Reads `sostac/README.md` to check planning status
3. Reads any completed SOSTAC phase files
4. Checks for active campaigns
5. Suggests next steps based on status

---

## 4.4 When to Use It vs. Direct Skill Access

### Use the Coordinator for:

- Starting any marketing conversation
- Multiple-brand portfolio management
- Strategic planning (SOSTAC)
- Campaign coordination across channels
- Checking overall progress
- Requesting work without knowing which specialist handles it

### Direct specialist access for:

You rarely need direct specialist access. The Coordinator handles routing. However, if you know exactly what you need and want to skip coordination:

- Requesting repeat work from a known specialist
- Quick one-off tasks when context is already loaded
- Testing a specific specialist capability

**Even for these, starting through the Coordinator works fine.** It simply routes faster when context is clear.

---

## 4.5 The Routing Decision Tree

The Coordinator follows a decision tree to route your requests. Understanding this helps you know what to expect.

### Step 1: Identify Working Context

```
Did user provide...
  - A repo/local project? → Use as working context
  - A live URL? → Audit first, use as context
  - No repo/URL? → Scan ./brands/ for existing workspaces

If ./brands/ is empty → Ask if they want to create a new brand
If one brand exists → Auto-select, confirm
If multiple brands → Present selection list
```

### Step 2: Read Brand Context

```
For active brand workspace, read:
  1. brand-context.md — Brand identity
  2. product-marketing-context.md — Deep positioning (if exists)
  3. sostac/ — Check phase file existence
  4. campaigns/ — Check named campaigns
```

### Step 3: Determine Workflow

```
Check SOSTAC status and user intent:

| SOSTAC Status | User Intent | Route |
| --- | --- | --- |
| No SOSTAC folder | Any | Start SOSTAC planning |
| SOSTAC in progress | Continue planning | Resume at next phase |
| SOSTAC in progress | Wants to implement | Warn incomplete, offer to finish |
| SOSTAC complete | Wants to implement | Spawn specialist team |
| SOSTAC complete | Wants specific task | Invoke relevant specialist |
| SOSTAC complete | Wants to update plan | Re-open specific phase |
```

### Step 4: Handle Specific Requests

```
For targeted requests (e.g., "write a blog post"):
  1. Select and load brand
  2. Check SOSTAC status
  3. If plan exists → invoke relevant specialist
  4. If no plan → recommend planning first, respect choice to proceed
```

---

## Summary: What You Learned

**Part 1 covered:**

- Agentic Marketing is a coordinated team of specialist skills that maintains context
- It solves expertise gaps, strategy disconnects, channel silos, budget inefficiency, and inconsistent messaging
- Key concepts: Skills, Brand Context, SOSTAC, Frameworks, Brand Workspace
- The system works like a virtual agency with you as the client

**Part 2 covered:**

- Start by typing any marketing request in Claude Code
- The Coordinator greets you, checks your setup, and routes automatically
- Output includes SOSTAC documents, specialist deliverables, and campaign strategies
- Iterate naturally by asking for changes or next steps
- The Coordinator is your primary entry point for most requests

**Next chapters (Part 3+) will cover:**

- The SOSTAC planning process in detail
- Working with specific specialists
- Creating and managing campaigns
- Measuring and optimizing results

---

*This user guide continues in Part 3: Strategic Planning with SOSTAC.*