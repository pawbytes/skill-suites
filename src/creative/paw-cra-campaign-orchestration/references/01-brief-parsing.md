# Stage 01: Brief Parsing

Parse the campaign brief to extract all deliverables, platforms, deadlines, and production requirements.

## Objective

Transform the campaign brief into a structured deliverable list that can be dispatched to production agents. Every deliverable needs: type, platform, deadline, and whether it has all required inputs (copy, scripts, assets) or needs Strategist support.

## Process

Read the campaign brief from memory. Extract:

1. **Deliverable inventory** — list every requested output (social posts, carousels, videos, flyers, brand assets, etc.)
2. **Platform targets** — which platforms each deliverable targets (Instagram, TikTok, YouTube, LinkedIn, X, Facebook, print, web)
3. **Deadlines** — any time constraints or priority ordering
4. **Input availability** — for each deliverable, check if required inputs exist:
   - Copy/captions — provided, or needs Strategist?
   - Scripts/storyboards — provided, or needs Strategist?
   - Visual reference material and source assets — provided, or needs generation?
   - Brand guidelines — loaded from memory?
5. **Campaign template variant** — if `--template:product-launch` was specified, load `./references/template-product-launch.md` and merge its standard deliverable set with the brief

## Deliverable Classification

Classify each deliverable into its production track:

| Type | Production Agent | Target Workflow |
|------|-----------------|-----------------|
| Social post (single image) | Designer | `paw-cra-design-social` |
| Carousel (multi-slide) | Designer | `paw-cra-design-social` |
| Flyer / print asset | Designer | `paw-cra-design-brand` |
| Brand asset (logo, icon) | Designer | `paw-cra-design-brand` |
| Batch visual set | Designer | `paw-cra-design-batch` |
| Short-form video (Reels, TikTok, Shorts) | Video Producer | `paw-cra-video-shortform` |
| Long-form video (YouTube, web) | Video Producer | `paw-cra-video-longform` |
| Video clips / repurposing | Video Producer | `paw-cra-video-clips` |

## Output

Write the parsed deliverable list to `status.md` under a `## Deliverables` section. Each deliverable entry should include:

```markdown
### [Deliverable Name]
- **Type:** social-post | carousel | flyer | brand-asset | batch | short-video | long-video | clips
- **Platform:** Instagram, TikTok, etc.
- **Agent:** Designer | Video Producer
- **Workflow:** cra-design-social | cra-design-brand | etc.
- **Inputs ready:** yes | partial (missing: copy) | no
- **Status:** pending
- **Deadline:** [if specified]
```

Update `status.md` frontmatter: `current_stage: '01-brief-parsing'`, `deliverables_total: [count]`.

If not headless, present the deliverable summary and confirm before proceeding. Then load `./references/02-dependency-queue.md`.
