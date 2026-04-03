# Specialist Routing

## Purpose

Define when and how to invoke each specialist agent in Prodig Suites.

## Specialist Roster

| Specialist | Skill Name | Stage | Primary Function |
|------------|------------|-------|------------------|
| Discovery | paw-ps-discovery | Discovery | Idea expansion, concept shaping |
| Research | paw-ps-research | Research | Market analysis, competitor research |
| Audience | paw-ps-audience | Audience | Customer insight, persona building |
| Strategist | paw-ps-strategist | Strategy | Product definition, scope design |

## When to Route to Each Specialist

### paw-ps-discovery

**Route when:**
- User has a vague idea that needs shaping
- User wants to explore multiple product directions
- User is stuck on what to create
- User asks "what should I build?"
- No specific product concept yet

**Don't route when:**
- Clear product concept already exists
- User wants validation of existing idea (→ Research)
- User wants customer understanding (→ Audience)

**Example triggers:**
- "I have an idea but it's not fully formed"
- "I want to create something in {space} but not sure what"
- "Help me brainstorm product ideas"
- "What products could I build for {audience}?"

---

### paw-ps-research

**Route when:**
- User wants to understand the market
- User asks about competitors
- User needs demand validation
- User wants to identify opportunities
- Research stage in journey

**Don't route when:**
- User already has research (check market-intelligence.md)
- User wants customer insights (→ Audience)
- User wants product definition (→ Strategist)

**Example triggers:**
- "Who are my competitors?"
- "Is there demand for this?"
- "Research the market for {product}"
- "What's the competitive landscape?"
- "Validate this idea"

**Expected outputs:**
- Competitor matrix/report
- Demand signal summary
- Opportunity gap analysis
- Market intelligence brief

---

### paw-ps-audience

**Route when:**
- User needs to understand customers
- User asks about target audience
- User wants persona development
- User needs problem/pain mapping
- Audience stage in journey

**Don't route when:**
- Personas already complete (check audience-intelligence.md)
- User wants market data (→ Research)
- User wants product strategy (→ Strategist)

**Example triggers:**
- "Who would buy this?"
- "Create a buyer persona"
- "What problems does my audience have?"
- "Understand my target customer"
- "Map customer pain points"

**Expected outputs:**
- Persona document
- Problem statement set
- Value signal mapping
- Language/copy bank

---

### paw-ps-strategist

**Route when:**
- User wants to define the product
- User asks about scope or features
- User needs packaging recommendations
- User has research complete and wants next step
- Strategy stage in journey

**Don't route when:**
- Research or audience missing (recommend those first)
- User wants execution (→ Executor after strategy)
- User wants just brainstorming (→ Discovery)

**Example triggers:**
- "Define my product"
- "What should be in version 1?"
- "Create a product brief"
- "How should I package this?"
- "Design the scope for {product}"

**Expected outputs:**
- Product brief
- Scope map
- Packaging recommendation
- Executor handoff spec

---

## Routing Sequence

The typical sequence follows the journey:

```
Discovery → Research → Audience → Strategist
    │           │          │           │
    │           │          │           └─→ Executor (after strategy)
    │           │          │
    │           │          └────────────── Can proceed in parallel with Research
    │           │
    │           └───────────────────────── Research can proceed without Audience
    │
    └───────────────────────────────────── Discovery may loop back if direction changes
```

### Parallel Execution

Research and Audience can run in parallel if:
- User wants both market and customer insight
- No dependencies between the two
- Time efficiency matters

**Example:** "I need market research AND customer personas — can we do both?"

**Response:** "Yes! Research and Audience are independent. I can route to both in parallel and we'll synthesize at the end."

### Sequential Requirements

Some sequences must be ordered:
- Strategist needs inputs from Research and/or Audience
- Executor needs Strategist's product brief
- Workflows need prior stage outputs

## Routing Protocol

### 1. Check Prerequisites

Before routing, verify:
- Required prior work exists
- Context is ready for the specialist
- User is at the right stage

### 2. Prepare Handoff

Create a handoff context including:
- Product context summary
- Relevant curated file contents
- Specific task or question
- Any constraints or preferences

### 3. Invoke via Agent Tool

Use the Agent tool with subagent_type appropriate for the specialist's function.

### 4. Receive Output

The specialist returns:
- Deliverables produced
- Memory updates made
- Recommended next actions

### 5. Update Memory

After specialist completes:
- Save outputs to appropriate curated files
- Log activity to daily file
- Update product-context.md if stage changed

## Cross-Specialist Patterns

### Service Layer Pattern

Some specialists provide intelligence that others consume:
- Research → produces market-intelligence.md → consumed by Strategist
- Audience → produces audience-intelligence.md → consumed by Strategist
- Strategist → produces product-decisions.md → consumed by Executors

### Handoff Without User

When routing from one specialist to another:
- Summarize what was accomplished
- Pass relevant context
- Note what the next specialist should do
- Log the transition in daily file

### User as Router

Sometimes the user brings output from one specialist to another:
- Acknowledge the prior work
- Load the relevant context
- Continue without re-doing completed work