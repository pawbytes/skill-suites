# Stage 3: Production Phase

## Purpose

Transform research and chosen hook into production-ready deliverables: a detailed slide deck outline and script ready for rehearsal.

## Duration

15-30 minutes

## Process

### 1. Phase Transition Announcement

Mark the transition clearly:

> "**Stage 3 of 4: Production**
> 
> Now I'll transform your research into deliverables. This includes:
> - Structuring your webinar narrative
> - Building a detailed slide deck outline
> - Writing your script (full script for key moments, talking points for flexibility)
> 
> I'll call in our Producer to handle this phase. They're structured and pragmatic — great at turning insights into presentable content."

### 2. Invoke Producer Agent

Call `paw-wbc-agent-producer`:

The Producer agent will:
- Load discovery context (brief, research, hook)
- Structure the webinar narrative arc
- Generate slide-by-slide outline with content and visual direction
- Write script with full copy for key moments
- Surface recommendations for Q&A or backup slides

**Transparent handoff message:**

> "Our Producer is now building your webinar. They'll create your slide deck outline and script based on the research and hook we've established."

### 3. Production Activities (Agent Handles)

The Producer agent performs these activities:

#### 3.1 Context Ingestion
- Load `brief.md` — audience context and goals
- Load `research-context.md` — compressed findings
- Load `hook-selected.md` — chosen angle and reasoning
- Understand the webinar kind and its structural implications

#### 3.2 Webinar Structuring
Based on webinar kind and hook, the Producer:
- Selects appropriate narrative arc
- Creates section outline: opener, body sections, close
- Plans 3-5 key moments that must land
- Ensures narrative discipline (arc, tension, resolution)

#### 3.3 Slide Deck Outline Generation
For each slide (target 20-30 slides for 30-45 min webinar):
- **Title:** Clear, compelling headline
- **Content points:** Bullet-level detail of what's on the slide
- **Visual direction:** Diagram, photo, chart, icon, etc.
- **Speaker notes reference:** Which script section applies
- **Timing:** Estimated minutes

Format is LLM-ready for easy generation.

#### 3.4 Script Writing
- **Full script sections:** Opener, close, and key moments get word-for-word copy
- **Talking point sections:** Body content gets key phrases and transitions
- **Timing markers:** Estimate minutes per section for pacing
- **Delivery notes:** Pause points, emphasis, transitions

Script is designed to be rehearsal-ready.

#### 3.5 Recommendations
From research, surface insights that:
- Didn't make the main flow but could strengthen Q&A
- Could be backup slides for audience questions
- Are worth having in the user's back pocket

#### 3.6 Daily Log
Write to daily log with `[producer]` tag:
- Slide count generated
- Script sections completed
- Key recommendations surfaced

### 4. Production Completion Announcement

When the Producer finishes:

> "**Production Phase Complete**
> 
> Your webinar is ready. I've created:
> 
> **Slide Deck Outline:** [X] slides with content points and visual direction
> **Script:** Full script for [X] key moments, talking points for other sections
> **Recommendations:** [X] insights for Q&A or backup
> 
> All files are saved to your webinar workspace."

### 5. Preview Key Deliverables

Offer a quick preview:

> "Would you like me to walk you through the structure, or shall we move to final delivery?"

Options:
- **Walk through structure** — Producer summarizes the narrative arc and key slides
- **Move to delivery** — Skip to Stage 4 for full output presentation

## Progression Criteria

Move to Stage 4 when:
- Slide deck outline is complete and saved
- Script is written and saved
- Recommendations are surfaced and saved
- User is ready to receive final deliverables

## Output

| Output | Location |
|--------|----------|
| Slide deck outline | `{webinar-slug}/slide-deck-outline.md` |
| Script | `{webinar-slug}/script.md` |
| Recommendations | `{webinar-slug}/recommendations.md` |
| Daily log entry | `daily/{YYYY-MM-DD}.md` |

## Producer Agent Invocation

When calling the Producer agent, pass context:

```text
/paw-wbc-agent-producer

Context: User is in the Webinar Creation pipeline, Stage 3 (Production).
Discovery outputs are complete:
- Brief: {webinar-slug}/brief.md
- Research: {webinar-slug}/research-context.md
- Hook: {webinar-slug}/hook-selected.md
Proceed with webinar structuring, slide deck outline, and script generation.
```

## Resumption Support

If user returns after Production phase is complete:

1. Read all output files
2. Summarize: "Your webinar on [topic] is complete. You have a [X]-slide outline and script ready. Would you like me to walk through the deliverables?"

## Edge Cases

### User Wants Revisions

If user wants changes after seeing outputs:

1. Note specific feedback: "What would you like to adjust?"
2. Producer can iterate on specific sections
3. Save updated versions
4. Log revision activity

### User Wants Different Structure

If user wants to restructure:

1. Producer can propose alternative structures
2. Discuss trade-offs of different approaches
3. Generate revised outline and script

### User Is Satisfied Mid-Phase

If user is happy with partial output:

1. Save what's complete
2. Note what's pending
3. Offer to complete remaining sections when they return

## Output Quality Standards

The Producer ensures:

### Slide Deck Outline
- Every slide has clear purpose
- Content points are specific (not vague "talk about X")
- Visual direction is actionable
- Narrative flows logically
- Timing is realistic

### Script
- Full-script sections are word-for-word ready
- Talking points give flexibility without being vague
- Key moments have impact (rhythm, emphasis, pauses)
- Transitions between sections are smooth
- Opener hooks immediately
- Close has clear call-to-action

### Recommendations
- Insights are genuinely useful
- Connected to research findings
- Relevant to Q&A scenarios
- Not filler content