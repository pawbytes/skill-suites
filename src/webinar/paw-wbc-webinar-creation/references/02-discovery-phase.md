# Stage 2: Discovery Phase

## Purpose

Transform the user's vague idea into a clear, defensible hook backed by deep research. This phase bridges brief intake and production.

## Duration

20-40 minutes (research time varies)

## Process

### 1. Phase Transition Announcement

Mark the transition clearly:

> "**Stage 2 of 4: Discovery**
> 
> Now I'll research your topic to find the right angle. This includes:
> - Understanding what's already been said on this topic
> - Finding data and insights that support your angle
> - Identifying the hook that will make your webinar compelling
> 
> I'll call in our Discovery specialist to handle this phase. They're research-obsessed and great at finding the surprising angle."

### 2. Invoke Discovery Agent

Call `paw-wbc-agent-discovery`:

The Discovery agent will:
- Expand the brief with clarifying questions
- Detect the webinar kind (thought leadership, demo, lead gen, training)
- Conduct deep research on the topic landscape
- Compress findings into usable context
- Generate 5-10 distinct hook angles
- Guide user to select the best hook

**Transparent handoff message:**

> "Our Discovery specialist is now working on your webinar. They'll ask questions, share findings, and present hook options for you to choose from."

### 3. Discovery Activities (Agent Handles)

The Discovery agent performs these activities:

#### 3.1 Brief Expansion
- Draw out full context from initial brief
- Clarify ambiguities
- Capture user's unique expertise and perspective
- Update `brief.md` with enriched details

#### 3.2 Webinar Kind Detection
- Analyze signals: audience, goals, topic nature
- Propose kind: thought leadership / product demo / lead gen / training
- Get user approval on detected kind
- Adjust research focus based on kind

#### 3.3 Deep Research
Using web search and content analysis:
- Published content: What's already been said?
- Data and statistics: What numbers support importance?
- Competitive landscape: Who else covers this? What angles are taken?
- Audience pain points: What problems does this audience face?
- Opportunity gaps: What's NOT being said that should be?

#### 3.4 Research Compression
- Filter ruthlessly: Keep only what informs the hook
- Structure for producer: Use template format
- Include citations: Source attribution for credibility
- Write `research-context.md`

#### 3.5 Hook Generation
- Generate 5-10 distinct angles (not variations of same idea)
- Apply hook techniques: contrarian, data-driven, story-based, problem-first
- Evaluate each: why it works, who it's for, risks
- Present options with clear reasoning

#### 3.6 Hook Selection
- Guide user to choose the best angle
- Capture reasoning: Why this hook? What made it the winner?
- Write `hook-selected.md`
- Log activity to daily log with `[discovery]` tag

### 4. Gate Assessment

Before transitioning to production, confirm readiness:

> "**Discovery Phase Complete**
> 
> Here's what we've established:
> 
> **Webinar Kind:** [kind]
> **Selected Hook:** [the chosen angle]
> **Research Foundation:** [X sources synthesized]
> 
> I've saved:
> - `research-context.md` — compressed research findings
> - `hook-selected.md` — your chosen hook and why it works
> 
> You're ready for the Production phase where we'll build your slide deck outline and script.
> 
> Ready to move to production? (yes / I want to explore different angles)"

### 5. Handling Gate Responses

#### User Confirms Readiness

> "Great! Moving to **Stage 3: Production**. I'll call in our Producer to transform this research into your deliverables."

Proceed to Stage 3.

#### User Wants Different Angles

> "No problem. Let's revisit the hook options or do additional research."

Loop back to Discovery agent for iteration.

#### User Needs to Pause

> "I'll save your progress. When you're ready to continue, just come back and mention your webinar on [topic]. I'll pick up where we left off."

Save state and end session gracefully.

## Progression Criteria

Move to Stage 3 when:
- Webinar kind is detected and approved
- Research is complete and compressed in `research-context.md`
- Hook is selected and saved to `hook-selected.md`
- User confirms readiness for production

## Output

| Output | Location |
|--------|----------|
| Enriched brief | `{webinar-slug}/brief.md` |
| Research context | `{webinar-slug}/research-context.md` |
| Selected hook | `{webinar-slug}/hook-selected.md` |
| Daily log entry | `daily/{YYYY-MM-DD}.md` |

## Discovery Agent Invocation

When calling the Discovery agent, pass context:

```text
/paw-wbc-agent-discovery --headless --brief "{project-root}/.pawbytes/webinar-suites/webinars/{webinar-slug}/brief.md"

Context: User is in the Webinar Creation pipeline, Stage 2 (Discovery).
Proceed with brief expansion, research, and hook generation.
```

## Resumption Support

If user returns after Discovery phase is complete:

1. Read `brief.md`, `research-context.md`, `hook-selected.md`
2. Summarize: "You completed discovery for your webinar on [topic]. You chose the hook: [hook]. Ready for production?"

## Edge Cases

### User Has Their Own Research

If user says "I already did research":

1. Offer to incorporate it: "Share what you found, and I'll integrate it with our research"
2. Discovery agent can skip or complement their findings
3. Still need to do hook generation from combined research

### User Is a Subject Matter Expert

If user has deep expertise:

1. Discovery agent should extract their knowledge: "What do you know that most sources miss?"
2. Research complements (doesn't replace) their expertise
3. Hook generation can leverage their unique perspective

### Time-Constrained User

If user is in a hurry:

1. Offer accelerated research: "I can do a quick scan and generate hooks in 10-15 minutes"
2. Note trade-off: "This will be less comprehensive but get you to production faster"
3. Still complete all steps, just with tighter time bounds