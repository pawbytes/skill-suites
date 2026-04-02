# Brief Analysis

Transform a creative brief or loose requirements into structured, actionable specifications. Route directly to the appropriate production agent based on output type.

## Workflow

1. **Aria receives brief** — User provides verbal description, document, or reference materials
2. **Aria extracts structure** — Parse the brief into the standard format below
3. **Route by output type:**
   - Visual deliverables → `paw-cra-agent-designer` (directly)
   - Video deliverables → `paw-cra-agent-video-producer` (directly)
   - Mixed deliverables → `paw-cra-campaign-orchestration` (parallel dispatch)
   - Research/strategy needed → `paw-cra-agent-strategist` (on demand)
4. **Confirm with user** — Present the structured brief and routing plan before dispatching

## When to Involve Strategist (Optional)

Strategist is a service agent — invoke on demand, not as a mandatory gate:

- **Invoke if:** Brief is vague, missing copy/scripts, needs competitive research, or user explicitly asks for strategic input
- **Skip if:** Brief is complete with copy, specs, and clear direction → route directly to production

## Goal

Ensure every stakeholder (user, specialists, Aria) shares the same understanding of what's being created and why. The priority is getting to visual/video production quickly — the suite's core value is producing assets, not documents.

## Input Sources

- User's verbal description
- Provided brief document
- Email or message content
- Reference materials (links, files)

## Extraction Framework

**1. The What (Output Type — determines routing)**
- What is being created? (format, quantity, scope)
- What channels/platforms? (social, web, print, video)
- What constraints? (dimensions, duration, file types)

**2. The Why**
- What's the goal? (awareness, conversion, engagement, launch)
- What success looks like (metrics, outcomes)

**3. The Who**
- Target audience
- Existing brand (from memory or new)

**4. The When**
- Deadlines
- Dependencies
- Review cycles

**5. The Context**
- Background or backstory
- Reference examples
- Things to avoid

## Output

Create a structured brief in memory: `{project-root}/.pawbytes/creative-suites/brands/{brand-name}/campaigns/{campaign}/brief.md`

```markdown
# {Brief Name}

## Deliverables
- {format}: {quantity} × {dimensions/specs}
- {format}: ...

## Objective
{goal statement}

## Audience
{audience description}

## Brand
{brand name or profile reference}

## Timeline
- Brief received: {date}
- Draft due: {date}
- Final due: {date}

## Constraints
- Must: {requirements}
- Must not: {restrictions}

## Copy / Script
{provided copy, or note "needs Strategist support"}

## References
- {links or file paths}

## Notes
{additional context}
```

## Routing Decision

After extracting the brief, determine the production path:

| Brief Contains | Route | Notes |
|----------------|-------|-------|
| Visual deliverables only | `paw-cra-agent-designer` | Direct production |
| Video deliverables only | `paw-cra-agent-video-producer` | Direct production |
| Mixed visual + video | `paw-cra-campaign-orchestration` | Parallel dispatch |
| "I need research first" | `paw-cra-agent-strategist` or `paw-cra-content-research` | Service request |
| Vague/incomplete brief | Ask clarifying questions | Then route by output type |
| Missing copy but has visual specs | `paw-cra-agent-designer` (they can request Strategist mid-workflow) | Don't block production |

Confirm with the user:
- "Here's what I understand you need: {summary}. I'll route this to {specialist}. Sound good?"
- If gaps exist, highlight them but don't block: "I noticed copy isn't provided — the Designer can work with the Strategist to draft it during production."
