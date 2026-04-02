# Stage 03: Parallel Dispatch

Launch Designer and Video Producer workflow groups simultaneously.

## Objective

Dispatch the design track and video track in parallel using the Agent tool. Each production agent receives a focused brief for their deliverables, brand guidelines context, and output path expectations.

## Dispatch Pattern

Use the **Agent tool** to launch parallel sub-agents. Designer and Video Producer tracks run simultaneously — do not wait for one to finish before starting the other.

### Design Track Dispatch

For each design workflow group, invoke `paw-cra-agent-designer` via Agent tool with:

- The specific deliverables assigned to this group
- Brand guidelines path: `{project-root}/.pawbytes/creative-suites/brands/{brand-name}/guidelines.md`
- Campaign context: campaign name, deadlines
- Output expectation: assets saved to campaign folder + `design-manifest.json`
- Workflow hint: which companion workflow to use (`paw-cra-design-social`, `paw-cra-design-brand`, or `paw-cra-design-batch`)
- `--headless` flag for autonomous execution

**Example prompt structure for Designer sub-agent:**
```
You are the Designer for the Aria Creative Suite. Execute the following deliverables in --headless mode:

Brand: {brand-name}
Campaign: {campaign-name}
Guidelines: {guidelines-path}

Deliverables:
1. [deliverable details with copy, platform, specs]
2. [deliverable details...]

Use the {workflow} workflow. Save all assets to the campaign folder. Generate design-manifest.json listing all produced assets.
```

### Video Track Dispatch

Same pattern for `paw-cra-agent-video-producer`:

- The specific deliverables assigned to this group
- Brand guidelines and campaign context
- Any scripts or storyboards (from brief or Strategist)
- Output expectation: video files + `video-manifest.json`
- Workflow hint: `paw-cra-video-shortform`, `paw-cra-video-longform`, or `paw-cra-video-clips`
- `--headless` flag

### Parallel Execution

Launch both tracks simultaneously:

1. **If sub-agents are available:** Dispatch Designer and Video Producer as parallel Agent tool calls in the same turn
2. **If sub-agents are not available:** Run sequentially — Design Track first, then Video Track. Note this in the status file.

## Progress Initialization

After dispatch, update `status.md`:
- Update frontmatter: `current_stage: '03-parallel-dispatch'`, `design_track: 'in-progress'`, `video_track: 'in-progress'`
- Record dispatch timestamps
- Log dispatch to daily log: `[Campaign] Dispatched {n} design deliverables and {m} video deliverables for {campaign-name}`

Then load `./references/04-progress-collection.md`.
