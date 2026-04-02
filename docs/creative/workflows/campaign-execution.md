# Campaign Execution

## Overview

End-to-end workflow for executing a multi-asset creative campaign. This workflow covers the complete process from brief to final deliverables, coordinating Designer and Video Producer specialists.

**Time required**: 30-90 minutes depending on deliverable count

## Scenario

You have a campaign brief with multiple deliverables — social posts, carousels, videos — and need to produce them all with consistent branding and quality.

## Prerequisites

- A campaign brief (can be created with Aria, the Creative Director)
- Brand guidelines or existing brand materials
- Clear deliverable specifications

## Workflow Steps

### Step 1: Campaign Brief

Start with a clear brief. If you don't have one, Aria can help create it.

**You**: "I need a launch campaign for my new product. We need 3 Instagram posts, 2 carousels, and a TikTok video."

**Aria (Creative Director)**: Creates a campaign brief with:
- Campaign name and objectives
- Deliverable list with specifications
- Timeline and priorities
- Brand context

**Output**: `.pawbytes/creative-suites/brands/{brand}/campaigns/{campaign}/brief.md`

---

### Step 2: Review the Plan

Aria analyzes your brief and creates a production plan.

**Aria**:
```
Campaign: Product Launch

Deliverables identified:
- 3 Instagram posts (1080x1080)
- 2 Instagram carousels (1080x1080, 3-5 slides each)
- 1 TikTok video (9:16, 30-60 seconds)

Production plan:
1. Designer: Instagram posts (parallel)
2. Designer: Instagram carousels (parallel)
3. Video Producer: TikTok video (parallel)

Estimated time: 45-60 minutes
Ready to execute?
```

---

### Step 3: Production

Once you approve, the Campaign Orchestration skill dispatches work to specialists.

**Designer** produces visual assets:
- Creates each social post with brand styling
- Builds carousel slides with narrative flow
- Generates manifest files for tracking

**Video Producer** creates video content:
- Develops script/storyboard
- Produces video with music and effects
- Adds subtitles and captions
- Generates video manifest

All work happens in parallel for efficiency.

---

### Step 4: Quality Control

After production, the QC skill reviews all assets:

**Quality Control**:
```
Checking 6 deliverables...

✓ Instagram Post 1: Passes brand check, platform specs
✓ Instagram Post 2: Passes brand check, platform specs
⚠ Instagram Post 3: Minor issue - text contrast low
✓ Carousel 1: Passes brand check, platform specs
✓ Carousel 2: Passes brand check, platform specs
✓ TikTok Video: Passes brand check, platform specs

5/6 assets passed. 1 asset needs attention.
```

---

### Step 5: Final Delivery

After QC passes, receive your campaign assets.

**Output Structure**:
```
.pawbytes/creative-suites/brands/{brand}/campaigns/{campaign}/
├── assets/
│   ├── social/
│   │   ├── post-1.png
│   │   ├── post-2.png
│   │   ├── post-3.png
│   │   ├── carousel-1/
│   │   │   ├── slide-1.png
│   │   │   ├── slide-2.png
│   │   │   └── slide-3.png
│   │   └── carousel-2/
│   │       ├── slide-1.png
│   │       ├── slide-2.png
│   │       └── slide-3.png
│   └── video/
│       └── tiktok-video.mp4
├── manifests/
│   ├── design-manifest.json
│   └── video-manifest.json
├── brief.md
└── status.md
```

---

## Complete Example Dialogue

**User**: "I need a holiday campaign for my coffee shop. We want 4 Instagram posts showing seasonal drinks, 1 carousel with our holiday menu, and 2 Reels showing drink preparation."

**Aria**: "I'll create your holiday campaign brief. Let me gather some information...

Campaign brief created:
- **Name**: holiday-promo-2026
- **Brand**: cozy-coffee
- **Deliverables**: 4 posts, 1 carousel, 2 Reels
- **Style**: Warm, festive, cozy aesthetic

Production plan:
- Designer: 4 posts + 1 carousel (~30 min)
- Video Producer: 2 Reels (~20 min)
- Total estimated time: 50 minutes

Ready to start production?"

**User**: "Yes, let's go"

**Aria**: "Starting campaign execution...

Dispatching to Designer for visual assets...
Dispatching to Video Producer for Reels...

[Progress updates appear as assets complete]

Designer complete: 5 assets produced
Video Producer complete: 2 Reels produced

Running quality control...
All 7 assets passed QC.

Campaign complete! Check your assets at:
`.pawbytes/creative-suites/brands/cozy-coffee/campaigns/holiday-promo-2026/assets/`"

---

## Tips for Best Results

1. **Be specific in your brief** — More detail = better first drafts
2. **Have brand materials ready** — Logos, colors, fonts speed up production
3. **Review QC reports** — Minor issues are flagged but don't block delivery
4. **Use manifests** — JSON manifests help track what was produced and when
5. **Batch similar requests** — One campaign with multiple assets is more efficient than multiple single requests

---

## Related Workflows

- [SOSTAC Marketing Planning](../../marketing/workflows/sostac-planning.md) — Strategic planning before creative execution
- [Presentation from Marketing Plan](../../tools/workflows/presentation-from-marketing-plan.md) — Present your campaign results

## Related Skills

- [paw-cra-campaign-orchestration](../skills/paw-cra-campaign-orchestration.md) — The skill that executes campaigns
- [paw-cra-agent-creative-director](../skills/paw-cra-agent-creative-director.md) — Aria, your creative lead
- [paw-cra-quality-control](../skills/paw-cra-quality-control.md) — Campaign-level QC