# Context Router

## Purpose

Route user requests to the appropriate capability based on their current context and stated intent.

## Routing Decision Tree

```
User Request
     │
     ▼
┌─────────────────────┐
│ Is there an active  │──No──→ Offer product selection or creation
│    product?         │
└─────────────────────┘
     │Yes
     ▼
┌─────────────────────┐
│ What is the user    │
│ asking for?         │
└─────────────────────┘
     │
     ├─ New idea/direction ──→ Discovery agent
     │
     ├─ Market/competitors ──→ Research agent
     │
     ├─ Customer/persona ────→ Audience agent
     │
     ├─ Product definition ──→ Strategist agent
     │
     ├─ Build/create ────────→ Execution routing (see below)
     │
     ├─ Package/assembly ────→ Product package assembler workflow
     │
     └─ Review/quality ──────→ Publish ready check workflow
```

## Execution Routing

When user wants to build or create:

```
What product type?
     │
     ├─ Course/ebook/guide ────→ Knowledge executor
     │
     ├─ Template/prompt pack ──→ Template executor
     │
     ├─ SaaS/app/AI tool ──────→ Software executor
     │
     └─ Service/consulting ────→ Service executor
```

## Context-Aware Routing

### Load Context First

Before routing, always check:

1. **product-context.md** — current product definition
2. **product-decisions.md** — key decisions made
3. **Daily log** — recent activity

### Avoid Redundant Work

If user asks for something already done:

"I see you already have {artifact} from {date}. Want to:
1. Review and refine it
2. Continue to the next stage
3. Start fresh with new direction"

### Batch Related Requests

If user asks for multiple things in one session:

"I can help with all of that. Here's the recommended sequence:
1. {First action} → {skill}
2. {Second action} → {skill}
3. {Third action} → {skill}

Shall I proceed in order, or prioritize differently?"

## Routing Examples

### Example 1: New User, Vague Request

**User:** "I want to create something"

**Context:** No active product, no history

**Response:** 
"Welcome to Prodig Suites! Let's figure out what you want to create.

What kind of digital product interests you?
- **Knowledge product** — course, ebook, guide, membership
- **Template product** — templates, prompt packs, digital kits
- **Software product** — SaaS, app, AI tool
- **Service product** — consulting package, productized service

Or tell me about a problem you'd like to solve."

---

### Example 2: Active Product, Clear Request

**User:** "I need competitor analysis"

**Context:** Active product "AI Course for Beginners" at discovery stage

**Response:**
"Got it — competitor analysis for your AI Course. I'll route you to the research specialist.

Before I do: any specific competitors you're aware of, or should we discover them from scratch?"

**Route to:** `paw-ps-research`

---

### Example 3: Stage Mismatch

**User:** "Build my course"

**Context:** Active product at discovery stage, no strategy brief

**Response:**
"I'd love to help build your course! But I notice we haven't defined the strategy yet — things like scope, curriculum approach, and target audience.

Quick path:
1. **Fast-track** — I'll ask 3 key questions, then build
2. **Full strategy** — Route to strategist for proper planning

Which works for you?"

---

### Example 4: Workflow Trigger

**User:** "Is my product ready to sell?"

**Context:** Product artifacts complete, not yet reviewed

**Response:**
"Let me check your product bundle and run a readiness review. This will verify you have everything needed for a sellable product."

**Route to:** `paw-ps-publish-ready-check` workflow

## Routing to Workflows vs Agents

### Route to Agent When:
- User needs judgment-based decisions
- Multi-turn conversation expected
- Exploration or discovery needed
- Context needs to be built up

### Route to Workflow When:
- Clear input → output transformation
- Repeatable process
- Minimal interaction needed
- Stage synthesis required

## Handoff Protocol

When routing to a specialist:

1. **Summarize context** — what we know so far
2. **State the ask** — what the specialist should do
3. **Note constraints** — any limitations or preferences
4. **Save to daily log** — record the routing decision

Example handoff prompt structure:

```
Routing to {specialist} for {product}:

Context: {summary from product-context.md and relevant curated files}

Task: {specific ask from user}

Constraints: {any scope, time, or preference constraints}

Please proceed with {capability needed}.
```