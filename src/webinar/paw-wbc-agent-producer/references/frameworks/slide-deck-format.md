# Slide Deck Format Guide

## Overview

The slide deck outline is LLM-ready — structured so that presentation tools (PowerPoint, Google Slides, Gamma, Beautiful.ai) can generate actual slides from it. Every slide has content points and visual direction, not just a title.

## Slide Structure

### Standard Slide Format

```markdown
## Slide N: [Slide Title]

**Title:** "[Exact title text]"

**Content Points:**
- First bullet (one idea)
- Second bullet (one idea)
- Third bullet (one idea)

**Visual Direction:** [Visual type + description]

**Speaker Notes:** See Script Section X.X

**Timing:** [Minutes]
```

---

## Required Fields Per Slide

### Title

The exact text that appears on the slide. Should be:
- Short (5-8 words max)
- Action-oriented or provocative when possible
- Clear about what the slide delivers

**Examples:**
- Good: "The 80/20 Rule Nobody Talks About"
- Good: "What 73% of Teams Get Wrong"
- Bad: "Introduction to Automation Challenges"

---

### Content Points

Bullet-level detail for the slide. Each bullet:
- One idea only
- 10-15 words max
- Scannable, not a paragraph

**Quantity guidelines:**
- Opener/close slides: 2-3 bullets
- Body slides: 3-5 bullets
- Data slides: 3-4 bullets with context

**Example:**
```markdown
**Content Points:**
- 73% of automation projects fail within 6 months
- The #1 reason isn't technology — it's process
- Teams skip the "boring" foundation work
```

---

### Visual Direction

Tells presentation tools what visual to create or source.

**Visual types:**

| Type | Description | Best For |
|------|-------------|----------|
| `diagram` | Flowchart, process diagram, framework visual | Processes, systems, frameworks |
| `chart` | Bar, line, pie chart | Data, comparisons, trends |
| `photo` | Stock or custom photo | Emotion, context, people |
| `icon` | Simple icon or icon set | Concepts, lists, features |
| `quote` | Large quote typography | Key quotes, testimonials |
| `screenshot` | App or website screenshot | Demos, examples |
| `comparison` | Side-by-side layout | Before/after, options |
| `timeline` | Linear progression | History, roadmap, steps |
| `photo-grid` | Multiple photos | Examples, gallery |
| `text-only` | No visual, typography focus | Key messages, emphasis |

**Example visual directions:**
```markdown
**Visual Direction:** Bar chart showing failure reasons, "process" bar highlighted in red

**Visual Direction:** Photo of frustrated person at desk, looking at laptop

**Visual Direction:** Diagram showing 4-step cycle with arrows, each step labeled

**Visual Direction:** Large quote on solid background, author attribution below
```

---

### Speaker Notes Reference

Links the slide to the script section.

**Format:** `See Script Section X.X`

This tells the presenter where to find the full script or talking points for this slide.

---

### Timing

Estimated minutes for this slide. Helps with:
- Pacing awareness
- Section balance
- Overall length planning

**Typical ranges:**
- Title/transition slides: 0.5-1 minute
- Content slides: 1-2 minutes
- Key moment slides: 2-3 minutes
- Demo slides: 3-5 minutes

---

## Slide Types by Section

### Opener Slides (Slides 1-3)

**Slide 1: Title Slide**
```markdown
## Slide 1: Title

**Title:** "[Webinar Title]"

**Content Points:**
- [Presenter name]
- [Date/Organization if relevant]

**Visual Direction:** Photo or branded background, title prominent

**Speaker Notes:** See Script Section 1.1

**Timing:** 1 minute
```

**Slide 2: Hook Slide**
```markdown
## Slide 2: The Hook

**Title:** "[Hook Statement]"

**Content Points:**
- [Supporting data or statement]
- [Why this matters]

**Visual Direction:** Large typography for hook, minimal visual

**Speaker Notes:** See Script Section 1.2 — key moment, full script

**Timing:** 2 minutes
```

**Slide 3: Agenda/Promise**
```markdown
## Slide 3: What You'll Learn

**Title:** "What We'll Cover Today"

**Content Points:**
- [First major topic]
- [Second major topic]
- [Third major topic]

**Visual Direction:** Icon list or numbered list

**Speaker Notes:** See Script Section 1.3

**Timing:** 1 minute
```

---

### Body Slides (Varies by Section)

**Content Slide**
```markdown
## Slide 8: [Topic]

**Title:** "[Clear, Compelling Title]"

**Content Points:**
- [Point 1]
- [Point 2]
- [Point 3]

**Visual Direction:** [Appropriate visual type]

**Speaker Notes:** See Script Section 3.2

**Timing:** 2 minutes
```

**Data Slide**
```markdown
## Slide 12: The Data

**Title:** "What the Numbers Show"

**Content Points:**
- [Key insight from data]
- [What this means]
- [Implication for audience]

**Visual Direction:** Chart showing [specific data], [style notes]

**Speaker Notes:** See Script Section 4.1

**Timing:** 2 minutes
```

**Key Moment Slide**
```markdown
## Slide 15: The Turning Point

**Title:** "[Dramatic Title]"

**Content Points:**
- [One powerful point]
- [Second reinforcing point]

**Visual Direction:** Large typography or impactful photo

**Speaker Notes:** See Script Section 5.1 — key moment, full script

**Timing:** 3 minutes
```

---

### Close Slides (Final 3-4 Slides)

**Recap Slide**
```markdown
## Slide 22: Key Takeaways

**Title:** "What We Learned"

**Content Points:**
- [Key insight 1]
- [Key insight 2]
- [Key insight 3]

**Visual Direction:** Icon list or numbered list

**Speaker Notes:** See Script Section 7.1

**Timing:** 2 minutes
```

**CTA Slide**
```markdown
## Slide 23: Next Steps

**Title:** "What to Do Next"

**Content Points:**
- [Specific action 1]
- [Specific action 2]
- [How to get started]

**Visual Direction:** Clear CTA button visual or step graphic

**Speaker Notes:** See Script Section 7.2 — key moment, full script

**Timing:** 2 minutes
```

**Q&A Slide**
```markdown
## Slide 24: Questions?

**Title:** "Your Questions"

**Content Points:**
- [Contact info]
- [Resource link]
- [Thank you]

**Visual Direction:** Simple, clean — focus on presenter

**Speaker Notes:** Open Q&A

**Timing:** Open
```

---

## Slide Count Guidelines

| Webinar Length | Target Slide Count | Range |
|----------------|-------------------|-------|
| 30 minutes | 15-20 slides | 12-25 |
| 45 minutes | 20-30 slides | 18-35 |
| 60 minutes | 25-40 slides | 22-45 |

**Principle:** Fewer slides with more time each is better than rushing through many slides.

---

## Full Example: Opener Section

```markdown
## Slide 1: Title

**Title:** "Email Automation That Actually Works"

**Content Points:**
- Jordan Chen, Automation Partners
- March 2026

**Visual Direction:** Branded background, clean typography

**Speaker Notes:** See Script Section 1.1

**Timing:** 0.5 minutes

---

## Slide 2: The Problem

**Title:** "What 73% of Teams Get Wrong"

**Content Points:**
- 73% of automation projects fail within 6 months
- The reason isn't technology — it's process
- Teams skip the foundation work

**Visual Direction:** Bar chart showing failure rates, "process issues" bar highlighted

**Speaker Notes:** See Script Section 1.2 — key moment, full script

**Timing:** 2 minutes

---

## Slide 3: The Promise

**Title:** "What You'll Walk Away With"

**Content Points:**
- The 4-step framework that prevents failure
- Real examples from teams who nailed it
- Your automation roadmap

**Visual Direction:** Icon list — 3 icons, one per point

**Speaker Notes:** See Script Section 1.3

**Timing:** 1 minute
```

---

## Formatting Rules

1. **One slide per heading** — Each slide starts with `## Slide N: [Title]`
2. **Required fields always present** — Title, Content Points, Visual Direction, Speaker Notes, Timing
3. **Content points as bullets** — Use `-` for each bullet point
4. **Visual direction is specific** — Include type AND description
5. **Timing is realistic** — Account for explanation, not just reading