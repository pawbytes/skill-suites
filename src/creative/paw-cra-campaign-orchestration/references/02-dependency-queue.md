# Stage 02: Dependency Analysis & Queue Build

Determine production order, resolve missing inputs, and build the dispatch plan.

## Objective

Analyze dependencies between deliverables, resolve any missing inputs (copy, scripts, research), and create an ordered dispatch plan that maximizes parallel execution.

## Dependency Analysis

**Core parallelism rule:** Visual assets (Designer) and video assets (Video Producer) can always run in parallel — they have no cross-dependencies. Within each track, most deliverables are also independent unless one explicitly builds on another (e.g., a video that uses a carousel's imagery).

Identify:

1. **Fully independent deliverables** — can dispatch immediately (most common case)
2. **Deliverables needing Strategist input** — require copy, scripts, or research before production can begin. These create a sequential dependency: Strategist first, then production agent.
3. **Cross-deliverable dependencies** — rare cases where one deliverable feeds another (e.g., brand asset generation before social posts that use those assets)

## Strategist Resolution (Conditional)

If any deliverables have `Inputs ready: partial` or `Inputs ready: no`:

1. Group the missing inputs by type (copy, scripts, research)
2. Invoke `paw-cra-agent-strategist` via Agent tool with a focused brief requesting only the missing inputs
3. Wait for Strategist outputs before those specific deliverables can be dispatched
4. Deliverables with complete inputs proceed to dispatch immediately — do not block the entire campaign on Strategist

**Key principle:** Only involve Strategist for explicitly missing inputs. If copy or scripts were provided in the brief, use them directly.

## Production Queue Build

Group deliverables into two parallel dispatch tracks:

### Design Track
Group by workflow type for efficient batching:
- **Social batch** — all social posts and carousels → `paw-cra-design-social` (or `paw-cra-design-batch` if 3+)
- **Brand batch** — all flyers and brand assets → `paw-cra-design-brand`

### Video Track
Group by workflow type:
- **Short-form batch** — all Reels/TikTok/Shorts → `paw-cra-video-shortform`
- **Long-form batch** — all YouTube/web videos → `paw-cra-video-longform`
- **Clips batch** — all repurposing tasks → `paw-cra-video-clips`

### Dispatch Order

```
Phase 1 (if needed): Strategist resolves missing inputs
Phase 2 (parallel):
  ├── Design Track: [grouped deliverables]
  └── Video Track: [grouped deliverables]
Phase 3: Quality gate (after both tracks complete)
```

## Output

Update `status.md`:
- Add `## Dispatch Plan` section with the grouped queue
- Add `## Strategist Requests` section if any were needed
- Update frontmatter: `current_stage: '02-dependency-queue'`

Record specialist assignments — which agent handles which deliverables.

If not headless, present the dispatch plan and confirm. Then load `./references/03-parallel-dispatch.md`.
