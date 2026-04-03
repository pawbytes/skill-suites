# Language Capture

## Purpose

Surface the words, phrases, and metaphors the audience actually uses. Creates a messaging-language bank that ensures product communication resonates rather than alienates.

## When to Use

- After persona construction (at minimum)
- User asks "how should I talk about this?"
- Preparing marketing copy or sales scripts
- Naming features or products
- Understanding audience mental models

## Prerequisites

- Personas defined
- Problem statements documented (preferred)
- Product context loaded

## Method

### Step 1: Identify Language Sources

Gather language from real audience communication:

| Source | What It Reveals | How to Access |
|--------|-----------------|---------------|
| Customer interviews | Natural phrasing, emotional language | Transcripts, notes |
| Sales calls | Objections, questions, decision language | Call recordings, CRM notes |
| Support tickets | Frustration language, feature requests | Ticket system export |
| Reviews | What they praise/complain about | Amazon, G2, Capterra, App Store |
| Forums/Reddit | Unfiltered opinions, slang | Search by topic/problem |
| Social media | How they talk publicly | Twitter, LinkedIn, TikTok comments |
| Competitor copy | Industry-standard language | Competitor websites, ads |
| Search queries | How they describe problems | Google Search Console, keyword tools |

### Step 2: Extract Language Patterns

Collect three types of language:

#### Words They Use (Vocabulary)

The specific terms and phrases in their natural speech:

**Capture format:**
```markdown
**Word/Phrase:** {term}
**Context:** When/where they use it
**Meaning:** What they mean by it (if different from literal)
**Example:** Direct quote using it
```

**Look for:**
- Industry-specific terms (e.g., "churn" for SaaS, "listing" for real estate)
- Role-specific jargon (e.g., "MQL" for marketers, "retainer" for lawyers)
- Slang or informal terms (e.g., "side hustle", "passive income")
- Metaphors they naturally use (e.g., "funnel", "pipeline", "tribe")

#### Words That Resonate (Hooks)

Language that triggers emotional or intellectual response:

**Capture format:**
```markdown
**Hook:** {phrase}
**Why it works:** Emotional/psychological reason
**Use case:** Where to use in messaging
**Example context:** Situation where it lands
```

**Look for:**
- Aspirations (e.g., "financial freedom", "work-life balance")
- Fears (e.g., "falling behind", "looking amateur")
- Identity markers (e.g., "creative entrepreneur", "solopreneur")
- Outcome language (e.g., "get your time back", "finally feel organized")

#### Words to Avoid (Repellents)

Language that causes friction, confusion, or negative response:

**Capture format:**
```markdown
**Word/Phrase:** {term}
**Why avoid:** Reason (jargon, cliché, trigger, competitor-owned)
**Alternative:** Better way to say it
**Exception:** When it might be okay (if ever)
```

**Look for:**
- Technical jargon they don't understand (e.g., "API integration" for non-technical)
- Overused marketing speak (e.g., "revolutionary", "game-changing")
- Terms competitors own (e.g., " CRM" owns "social CRM")
- Words that trigger skepticism (e.g., "guarantee", "secret")
- Loaded terms with negative associations (e.g., "hustle" for burned-out founders)

### Step 3: Map Mental Models

Language reveals how the audience thinks:

#### Conceptual Metaphors

How they conceptualize abstract ideas:

| If they say... | Their mental model is... |
|----------------|-------------------------|
| "Grow my business" | Business as a living thing |
| "Build my list" | Audience as construction |
| "Capture leads" | Prospects as prey |
| "Nurture relationships" | Connections as plants |
| "Scale up" | Business as expandable structure |

**Use these metaphors in messaging to align with their worldview.**

#### Causal Language

How they explain cause and effect:

- "I need X so I can Y" → Understand their logic chain
- "X always leads to Y" → Their mental rules
- "If only I had X" → Their perceived missing link

#### Identity Language

How they describe themselves:

- "I'm a [role]" → How they see themselves professionally
- "I'm not a [role]" → What they reject or distance from
- "I'm trying to become a [role]" → Their aspirational identity

### Step 4: Create Messaging Angles

Transform language insights into messaging directions:

```markdown
## Messaging Angle: {Name}

**Based on:** Language pattern discovered

**Core message:** {one-line message}

**Supporting language:**
- {word/phrase 1}
- {word/phrase 2}
- {word/phrase 3}

**Audience segment:** Who this resonates with

**Tone:** How to deliver it

**Example usage:**
> {example copy using this angle}

**Avoid:** What NOT to say with this angle
```

### Step 5: Build Language Bank

Compile all findings into a reference document:

```markdown
# Language Bank

**Audience:** {persona names}
**Last Updated:** YYYY-MM-DD

## Vocabulary They Use

| Term | Context | Example |
|------|---------|---------|
| {term} | {context} | {example quote} |

## Phrases That Resonate

| Phrase | Emotion | Use When |
|--------|---------|----------|
| {phrase} | {emotion} | {situation} |

## Words to Avoid

| Word | Why Avoid | Say Instead |
|------|-----------|-------------|
| {word} | {reason} | {alternative} |

## Metaphors That Work

| Metaphor | Use For | Example |
|----------|---------|---------|
| {metaphor} | {concept} | {example} |

## Messaging Angles

### Angle 1: {Name}
- Core message: {message}
- Best for: {segment/situation}
- Example: {example copy}

### Angle 2: {Name}
- Core message: {message}
- Best for: {segment/situation}
- Example: {example copy}

## Competitor Language

| Competitor | Their Language | Our Differentiation |
|------------|----------------|---------------------|
| {competitor} | {their terms} | {our terms} |
```

## Output

### Files Created

1. **Language Bank:** `{product-slug}/audience/language-bank.md`

### Memory Update

Update `curated/audience-intelligence.md`:
- Add vocabulary summary to Language Bank section
- Add messaging angles
- Note any validated or assumed language patterns

## Language Discovery Techniques

### For Vocabulary
- "How would you describe what you do to a friend?"
- "What words do you use when talking about [topic]?"
- "What terms does your industry use that outsiders might not understand?"

### For Hooks
- "What makes you stop and pay attention when you see [type of content]?"
- "What promise would make you click?"
- "What headline would make you say 'this is for me'?"

### For Repellents
- "What words make you roll your eyes when you see marketing?"
- "What promises sound too good to be true?"
- "What language feels inauthentic or salesy?"

### For Mental Models
- "When you think about [concept], what image comes to mind?"
- "How would you explain [concept] to a beginner?"
- "What's the difference between [X] and [Y] in your mind?"

## Quality Checklist

Before finalizing language capture:

- [ ] Vocabulary comes from real audience quotes, not assumptions
- [ ] Hooks are tied to emotional triggers
- [ ] Words to avoid have clear reasons documented
- [ ] Metaphors align with audience worldview
- [ ] Messaging angles have example usage
- [ ] Language differentiates from competitors
- [ ] Tone matches persona communication style

## Anti-Patterns to Avoid

| Don't | Do Instead |
|-------|------------|
| Using your jargon | Using their vocabulary |
| "Our platform leverages AI" | "We use smart automation" (if that's their term) |
| Marketing speak | Their natural language |
| Complex terminology | Simple, clear language |
| Competitor's language | Your differentiated language |

## Handoff

When language capture is complete:
- **Route to Strategist** with messaging inputs for product definition
- **Route to Marketing** (via Orchestrator) for campaign messaging
- **Archive in memory** for future reference by all agents