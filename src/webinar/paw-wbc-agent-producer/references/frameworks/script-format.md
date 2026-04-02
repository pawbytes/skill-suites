# Script Format Guide

## Overview

Webinar scripts use a hybrid approach: full script for key moments, talking points for flexible sections. This balances preparation with natural delivery. The script clearly indicates which sections are which.

## Script Depth Strategy

### When to Write Full Script

Write word-for-word scripts for:

| Section | Why Full Script |
|---------|-----------------|
| **Opener/Hook** | First impression — must land perfectly |
| **Key moments** | 3-5 moments the audience remembers — precision matters |
| **Transitions** | Keeps flow tight, prevents rambling |
| **Close/CTA** | Last thing they hear — must be memorable |
| **Data explanations** | Numbers need context — off-script risks confusion |

### When to Use Talking Points

Use bullet-point talking points for:

| Section | Why Talking Points |
|---------|-------------------|
| **Body content** | Allows natural delivery, adaptation to audience |
| **Examples/stories** | Speaker's natural voice is more authentic |
| **Q&A prep** | Can't script the unknown |
| **Technical walkthroughs** | Flexibility for audience pace |

---

## Script Document Structure

```markdown
# Webinar Script: [Webinar Title]

## Meta
- **Total runtime:** [X minutes]
- **Key moments:** [N] sections with full script
- **Talking point sections:** [N] sections with bullets

---

## Section 1: Opener

### Section 1.1: Welcome [Full Script]

[Timing: 1 minute]

[Your opening lines word-for-word...]

---

### Section 1.2: The Hook [Full Script — KEY MOMENT]

[Timing: 2 minutes]

[Hook script word-for-word...]

---

## Section 2: The Problem

### Section 2.1: Why This Matters [Talking Points]

[Timing: 3 minutes]

**Key points:**
- [Point 1]
- [Point 2]
- [Point 3]

**Transition to next:** "[Transition phrase]"

---

## Section 3: The Solution

### Section 3.1: The Framework Reveal [Full Script — KEY MOMENT]

[Timing: 3 minutes]

[Framework introduction script word-for-word...]

---
```

---

## Full Script Format

### Structure

```markdown
### Section X.X: [Section Name] [Full Script — KEY MOMENT]

[Timing: X minutes]

[Script text here...]

[Stage directions in brackets...]

[More script text...]
```

### Formatting Conventions

| Element | Format |
|---------|--------|
| **Timing** | `[Timing: X minutes]` at start |
| **Stage directions** | `[Brackets, italic if possible]` |
| **Emphasis** | **Bold** for words to stress |
| **Pauses** | `(Pause)` on its own line |
| **Transitions** | `[Transition phrase]` at end |

### Example Full Script

```markdown
### Section 1.2: The Hook [Full Script — KEY MOMENT]

[Timing: 2 minutes]

Here's a number that stopped me in my tracks: **73% of automation projects fail within six months.**

(Pause)

Now, when I say "fail," I don't mean they don't work. I mean they don't **deliver.** The ROI never shows up. The team goes back to spreadsheets.

And here's what's fascinating — the number one reason isn't the tool. It's not the budget. It's not even the team.

[Gesture to slide]

It's process.

Teams skip the boring work. They don't map their workflows first. They don't define what success looks like.

So today, we're going to fix that. Together.

[Transition: Let me show you what I mean...]
```

---

## Talking Points Format

### Structure

```markdown
### Section X.X: [Section Name] [Talking Points]

[Timing: X minutes]

**Key points:**
- [Point 1] — [Optional: key phrase to include]
- [Point 2] — [Optional: key phrase to include]
- [Point 3] — [Optional: key phrase to include]

**Story/example:** [Brief description of story to tell]

**Data reference:** [What data point to mention]

**Transition to next:** "[Transition phrase]"
```

### Example Talking Points

```markdown
### Section 3.2: Step One - Audit [Talking Points]

[Timing: 4 minutes]

**Key points:**
- Start with what's already working — "You don't need to rebuild everything"
- Map every touchpoint — "Where does data enter? Where does it go?"
- Identify the gaps — "This is where automation breaks down"

**Story/example:** Tell the Acme Corp story — they found 12 manual steps in a "automated" process

**Data reference:** Mention the 73% stat again — tie back to hook

**Transition to next:** "Once you've mapped it, you can see what to fix. That's step two..."
```

---

## Timing Markers

### Purpose

Timing markers help speakers:
- Know if they're on pace
- Identify sections to expand or trim
- Plan for audience attention spans

### Placement

- Every section starts with timing
- Key moments may have internal timing notes
- Total runtime at document start

### Timing Guidelines

| Section Type | Typical Range |
|--------------|---------------|
| Opener | 3-5 minutes |
| Body section | 5-10 minutes each |
| Key moment | 2-4 minutes |
| Close | 4-6 minutes |
| Q&A | Open-ended |

---

## Rehearsal Notes Integration

### In-Script Notes

Mark sections that need extra rehearsal:

```markdown
### Section 3.1: The Framework Reveal [Full Script — KEY MOMENT]

[Rehearsal note: Practice the reveal pause — count to 3 before saying "It's process"]

[Timing: 3 minutes]

[Script...]
```

### Post-Script Notes Section

Include a rehearsal guide at the end:

```markdown
---

## Rehearsal Guide

### High-Priority Sections
1. Section 1.2: The Hook — timing of the pause is critical
2. Section 3.1: Framework Reveal — practice smooth visual transition
3. Section 7.2: CTA — commit to memory, no notes

### Timing Checkpoints
- At Slide 8: Should be ~12 minutes in
- At Slide 15: Should be ~25 minutes in
- At Slide 22: Should be ~35 minutes in

### Common Pitfalls
- Section 4 tends to run long — watch the clock
- Q&A prep is easy to skip — don't
- Transition to CTA needs energy lift — practice the shift
```

---

## Key Moments Identification

### How to Mark Key Moments

Key moments are the 3-5 things the audience remembers. Mark them clearly:

```markdown
[Full Script — KEY MOMENT]
```

### Standard Key Moments

Most webinars have these key moments:

| Moment | Location | Purpose |
|--------|----------|---------|
| Hook | Opener | First impression, grab attention |
| Turn | Mid-body | The insight that changes everything |
| Proof | Late body | Credibility lock-in |
| CTA | Close | What to do next |
| Optional | Varies | Surprise, counterintuitive insight, memorable story |

---

## Q&A Prep Section

### Structure

```markdown
---

## Q&A Preparation

### Anticipated Questions

**Q: [Question you expect]**
A: [Key points for answer]
- [Point 1]
- [Point 2]

**Q: [Question you expect]**
A: [Key points for answer]

### Backup Content

If Q&A is slow, have these ready:
- [Story not in main presentation]
- [Additional data point]
- [Common misconception to address]

### Tough Questions

**Q: [Challenging question]**
A: [Honest, confident response]
- Acknowledge the concern
- Provide perspective
- Offer specific next step
```

---

## Full Example: Complete Section

```markdown
## Section 3: The Framework

### Section 3.1: The Reveal [Full Script — KEY MOMENT]

[Rehearsal note: Build tension before the reveal. Slow down at "But here's what actually works..."]

[Timing: 3 minutes]

We've seen the problem. Teams are working harder, not smarter. Automation that was supposed to save time is creating **more** work.

(Pause)

But here's what actually works.

(Pause — let it land)

Four steps. That's it. Four steps that separate the teams who succeed from the 73% who don't.

[Advance slide]

Step one: **Audit.** Not the scary kind. I'm talking about a simple map of what you're doing right now. Every touchpoint. Every handoff. Every place data enters and exits.

Step two: **Simplify.** Before you automate, eliminate. I'll show you how teams cut 40% of their process before adding a single tool.

Step three: **Automate.** Now — and only now — you bring in the tools. The right ones, for the right reasons.

Step four: **Optimize.** This is where most teams stop. The winners keep going.

[Transition: Let's dive into each one...]
```

---

## Output Checklist

Before saving the script, verify:

- [ ] All key moments marked with `[Full Script — KEY MOMENT]`
- [ ] Every section has timing marker
- [ ] Full script sections have stage directions
- [ ] Talking point sections have key phrases
- [ ] Transitions between sections are written
- [ ] Rehearsal guide included at end
- [ ] Q&A prep section included
- [ ] Total runtime matches target (30/45/60 minutes)