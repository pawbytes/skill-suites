# Value Signal Mapping

## Purpose

Connect audience pains to buyer motivation, revealing what they truly value and how a product can deliver meaningful outcomes. Translates problems into value proposition inputs.

## When to Use

- After persona construction and problem discovery
- User asks "what does my audience value?"
- Preparing value proposition or positioning
- Deciding which features to prioritize
- Creating messaging and marketing copy

## Prerequisites

- Personas defined (or in progress)
- Problem statements documented
- Product context loaded

## Method

### Step 1: Identify Value Categories

Value manifests in different forms. Map pains to these categories:

| Category | What It Means | Example |
|----------|---------------|---------|
| **Time** | Saving, freeing up, or redirecting time | "Get 5 hours back per week" |
| **Money** | Earning more, spending less, or avoiding loss | "Save $500/month on tools" |
| **Effort** | Reducing friction, complexity, or struggle | "Eliminate 3 hours of manual work" |
| **Quality** | Better outcomes, consistency, or reliability | "Double your conversion rate" |
| **Status** | Looking better to peers, clients, or market | "Look like a Fortune 500 company" |
| **Security** | Reducing risk, anxiety, or uncertainty | "Never worry about data loss again" |
| **Growth** | Learning, advancing, or improving | "Master new skills in half the time" |
| **Control** | Having agency, visibility, or predictability | "Know exactly where every dollar goes" |
| **Connection** | Belonging, access, or relationships | "Join 10,000+ successful founders" |

### Step 2: Map Pains to Value

For each problem, ask:

1. **What outcome would make this pain go away?**
   - Functional outcome: What they'd be able to do
   - Emotional outcome: How they'd feel
   - Social outcome: How they'd be perceived

2. **What does solving this enable?**
   - Immediate enablement: What they could do right away
   - Ripple effects: What else becomes possible

3. **What is this outcome worth to them?**
   - Monetary value: What would they pay?
   - Time value: How much time is this worth?
   - Emotional value: How much peace of mind?

### Step 3: Extract Value Signals

A value signal has these components:

```markdown
## Value Signal: {Name}

**Pain Addressed:** Connected problem statement

**Category:** Time/Money/Effort/Quality/Status/Security/Growth/Control/Connection

**Outcome Desired:**
- Functional: {what they want to accomplish}
- Emotional: {how they want to feel}
- Social: {how they want to be perceived}

**Emotional Driver:** The core feeling they seek

**Evidence:** How we know this matters to them

**Feature Implication:** What product feature delivers this value

**Messaging Angle:** How to communicate this value

**Proof Points:** What would convince them this is real
```

### Step 4: Prioritize Value Signals

Rank value signals by:

| Factor | Weight | Assessment |
|--------|--------|------------|
| Pain intensity | 30% | How much does solving this matter? |
| Audience reach | 25% | How many people want this? |
| Competitive gap | 20% | How well do alternatives deliver? |
| Delivery feasibility | 15% | Can we actually provide this? |
| Communication clarity | 10% | Can we articulate this clearly? |

**Value Signal Priority Matrix:**

```
              HIGH REACH
                  │
    ┌─────────────┼─────────────┐
    │             │             │
    │   TABLE     │   HERO      │
    │   STAKES    │   SIGNAL    │
    │             │             │
INT ├─────────────┼─────────────┤ HIGH
    │             │             │
    │   NICHE     │   WILD      │
    │   SIGNAL    │   CARD      │
    │             │             │
    └─────────────┼─────────────┘
                  │
              LOW REACH
```

- **Hero Signals:** High intensity + High reach = Lead with these
- **Table Stakes:** High intensity + Low reach = Must have for niche
- **Niche Signals:** Low intensity + Low reach = Differentiation within segment
- **Wild Cards:** Low intensity + High reach = Maybe not as important as reach suggests

### Step 5: Create Value Proposition Inputs

Synthesize signals into inputs for positioning:

#### Primary Value Proposition
Based on top hero signal(s):

**Format:**
> For [persona], who [pain statement], [product] provides [value signal]. Unlike [alternatives], we [differentiator].

**Example:**
> For solo therapists building private practices, who struggle with the business side while trying to focus on clients, PracticeFlow provides control and confidence in running your business. Unlike generic practice management tools, we're built specifically for the therapy journey from agency to private practice.

#### Supporting Value Signals
List 2-3 additional signals that reinforce:

- Signal 1: Secondary value that supports primary
- Signal 2: Tertiary value that differentiates
- Signal 3: Emotional value that connects

## Output

### Files Created

1. **Value Signals:** `{product-slug}/audience/value-signals.md`

### Memory Update

Update `curated/audience-intelligence.md`:
- Add value signal summaries to Value Signals section
- Connect to personas and problem statements

### Value Signal Summary Format

```markdown
## Value Signals

| Signal | Pain | Category | Priority | Feature Implication |
|--------|------|----------|----------|---------------------|
| {signal} | {pain} | {category} | {hero/table/niche} | {feature} |

### Hero Signals (Lead With These)

1. **{Signal Name}**
   - Outcome: {what they get}
   - Emotion: {how they feel}
   - Message: {how to say it}

### Table Stakes (Must Have)

1. **{Signal Name}**
   - Outcome: {what they get}
   - Feature: {what to build}

### Differentiators (Niche Value)

1. **{Signal Name}**
   - Who values this: {specific segment}
   - Why it matters: {reason}
```

## Value Extraction Questions

### For Time Value
- "If this was solved, what would you do with that time?"
- "What's your time worth per hour? Multiply that by hours saved."
- "What opportunities are you missing because you're stuck doing this?"

### For Money Value
- "What are you currently spending to solve this?"
- "What would you pay to make this problem go away?"
- "What's the financial impact of this problem continuing?"

### For Emotional Value
- "How would you feel if this was completely solved?"
- "What's that peace of mind worth to you?"
- "How does this problem affect your confidence or stress?"

### For Status Value
- "How would others perceive you if this was handled?"
- "What recognition or respect would come from this?"
- "How does this problem affect how others see you?"

### For Security Value
- "What are you worried might happen if this isn't addressed?"
- "What would change if you knew this was handled?"
- "What risks are you currently exposed to?"

## Quality Checklist

Before finalizing value signals:

- [ ] Each signal connects to a documented pain
- [ ] Category is assigned (time, money, effort, etc.)
- [ ] Emotional driver is identified
- [ ] Feature implication is clear
- [ ] Messaging angle is articulated
- [ ] Priority is assigned based on matrix
- [ ] Differentiation from alternatives considered

## Anti-Patterns to Avoid

| Don't | Do Instead |
|-------|------------|
| "They want to be more efficient" | "They want to leave work at 5pm without guilt" |
| "They value time savings" | "They want to attend their kid's soccer games" |
| Generic value propositions | Specific outcomes tied to documented pains |
| Listing features | Connecting features to emotional outcomes |

## Handoff

When value signal mapping is complete:
- **Route to Language Capture** to capture the words that express this value
- **Route to Strategist** for product definition based on value
- **Route to Marketing** (via Orchestrator) for messaging development