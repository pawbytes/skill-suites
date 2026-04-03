# Problem Discovery

## Purpose

Clarify and document the pains and desired outcomes that define the audience's relationship to the problem space. Surface what matters most and why existing solutions fall short.

## When to Use

- User asks "what problems does my audience have?"
- Need to map customer pain points
- Validating product-market fit assumptions
- Preparing for value proposition work
- Understanding why current solutions fail

## Prerequisites

- Personas defined or in progress
- Product context loaded from product-context.md
- Any existing audience data from audience-intelligence.md

## Method

### Step 1: Identify Problem Categories

Start with broad problem spaces, then narrow:

1. **Functional Problems**
   - Task friction: What takes too long or too much effort?
   - Quality issues: What results are unsatisfactory?
   - Missing capabilities: What can't they do that they need to?
   - Integration gaps: What doesn't work together?

2. **Emotional Problems**
   - Anxiety: What worries or stresses them?
   - Frustration: What annoys or angers them?
   - Fear: What are they afraid of?
   - Inadequacy: What makes them feel incompetent?

3. **Social Problems**
   - Reputation: How might they look bad to others?
   - Status: What prevents them from advancing?
   - Belonging: Where do they feel excluded?
   - Influence: Where do they lack authority?

4. **Financial Problems**
   - Cost: What's too expensive?
   - Revenue: What opportunities are they missing?
   - Risk: What could cause financial loss?
   - Efficiency: Where is money being wasted?

### Step 2: Discover Specific Pains

For each persona, ask probing questions:

**Daily Experience:**
- "Walk me through a typical day. Where do you feel friction?"
- "What's the worst part of your day? Why?"
- "What task do you dread doing? What makes it painful?"

**Current Solutions:**
- "How do you currently solve this problem?"
- "What have you tried? What happened?"
- "What's missing from the tools you use today?"

**Impact Assessment:**
- "What happens if this problem isn't solved?"
- "How does this affect your work/life/business?"
- "What's the cost of this problem continuing?"

**Desired State:**
- "What would 'solved' look like for you?"
- "If you had a magic wand, what would change?"
- "What would you do with the time/money/energy saved?"

### Step 3: Map Pain Intensity

Rate each pain on multiple dimensions:

| Dimension | Scale | What It Measures |
|-----------|-------|------------------|
| Frequency | Daily/Weekly/Monthly/Rare | How often they feel it |
| Intensity | 1-10 | How much it hurts when felt |
| Impact | Low/Medium/High | Consequence of not solving |
| Urgency | Immediate/Soon/Someday | Timeline for seeking solution |

**Pain Priority Matrix:**

```
                HIGH INTENSITY
                     │
     ┌───────────────┼───────────────┐
     │               │               │
     │   CRITICAL    │    URGE TO    │
     │   (Solve now) │    SOLVE      │
     │               │               │
FREQ ├───────────────┼───────────────┤ HIGH
     │               │               │
     │   NUISANCE    │    ANNOYING   │
     │               │               │
     │               │               │
     └───────────────┼───────────────┘
                     │
                LOW INTENSITY
```

### Step 4: Document Problem Statements

For each validated pain, create a structured problem statement:

```markdown
## Problem: {Problem Name}

**Summary:** One-line description of the problem

**Audience:** Which persona(s) experience this

**Context:** When/where does this problem occur

**Frequency:** How often they encounter it

**Intensity:** How much it hurts (1-10)

**Current Solutions:**
- Solution A: What they do now
- Solution B: Alternative approaches
- Gap: Why these fall short

**Root Cause:** Why does this problem exist?

**Impact:** What happens if unsolved

**Desired Outcome:** What they want instead

**Emotional Component:** How it makes them feel

**Opportunity:** What a better solution would do
```

### Step 5: Validate Problem Assumptions

For each problem statement, note:

| Element | Confidence | Evidence Needed |
|---------|------------|-----------------|
| Problem exists | Validated/Inferred/Assumed | What would confirm? |
| Audience affected | Validated/Inferred/Assumed | Who else should we ask? |
| Intensity accurate | Validated/Inferred/Assumed | What data supports? |
| Gap is real | Validated/Inferred/Assumed | What competitors claim? |

## Output

### Files Created

1. **Problem Statements:** `{product-slug}/audience/problem-statements.md`

### Memory Update

Update `curated/audience-intelligence.md`:
- Add problem summaries to Problem Statements section
- Update persona pain sections
- Update Gaps & Assumptions table

### Problem Statement Summary Format

```markdown
## Problem Statements

| Problem | Audience | Intensity | Frequency | Status |
|---------|----------|-----------|-----------|--------|
| {problem} | {persona} | {1-10} | {freq} | validated/assumed |

### Priority Problems

1. **{Problem 1}** — {why it's priority}
2. **{Problem 2}** — {why it's priority}
3. **{Problem 3}** — {why it's priority}

### Solved by Competitors

| Problem | Competitor | Gap |
|---------|------------|-----|
| {problem} | {competitor} | {why still a problem} |
```

## Discovery Questions by Problem Type

### Time/Efficiency Problems
- "How much time do you spend on this today?"
- "What would you do with that time if you got it back?"
- "What's the real cost of this time (hourly rate × hours)?"

### Quality/Outcome Problems
- "What does 'good' look like for this outcome?"
- "How often do you achieve that today?"
- "What prevents you from hitting that mark consistently?"

### Knowledge/Skill Problems
- "What do you wish you knew how to do?"
- "How are you handling this without that knowledge?"
- "What would change if you had that skill?"

### Money/Cost Problems
- "What are you spending to solve this today?"
- "What's the cost of NOT solving it?"
- "What would you pay for a better solution?"

### Emotional/Psychological Problems
- "How does this situation make you feel?"
- "What's the impact on your confidence/stress/relationships?"
- "What would feeling differently about this be worth?"

## Quality Checklist

Before finalizing problem discovery:

- [ ] Problems are specific, not generic
- [ ] Each problem connects to a persona
- [ ] Intensity and frequency are documented
- [ ] Current solutions and gaps are identified
- [ ] Emotional component is captured
- [ ] Root causes are explored
- [ ] Assumptions are flagged for validation

## Anti-Patterns to Avoid

| Don't | Do Instead |
|-------|------------|
| "They need efficiency" | "They spend 4 hours/week on manual data entry that could be automated" |
| "They want to save money" | "They're paying for three separate tools that don't integrate" |
| Listing all possible problems | Prioritizing by intensity and frequency |
| Assuming problems exist | Validating with evidence or flagging assumption |

## Handoff

When problem discovery is complete:
- **Route to Value Signal Mapping** to connect pains to value
- **Route to Research** if problems need market validation
- **Route to Strategist** if ready for product definition based on problems