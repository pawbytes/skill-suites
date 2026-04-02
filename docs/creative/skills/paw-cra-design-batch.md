# paw-cra-design-batch

## Overview

Batch visual production workflow that transforms content calendars or campaign briefs into complete sets of platform-ready assets. Handles multi-asset production runs with organized output bundles and machine-readable manifests for tracking.

## What It Does

| Capability | Description |
|------------|-------------|
| Calendar parsing | Convert content calendar rows into production queue |
| Multi-asset generation | Produce many assets in a single run |
| Platform grouping | Group assets by platform for efficient generation |
| Brand validation | Check every asset against brand guidelines |
| Organized bundles | Structured folder output by platform and format |
| Manifest tracking | Machine-readable record of all produced assets |

## When to Use It

- You have a content calendar needing visual assets
- You need to produce multiple campaign assets at once
- You want bulk asset generation with consistency
- You have a campaign brief with multiple deliverables
- You need organized output across multiple platforms

## Trigger Phrases

- "batch design"
- "content calendar to assets"
- "campaign batch"
- "produce all campaign visuals"
- "bulk asset generation"

## What You Get (Deliverables)

| Output | Location |
|--------|----------|
| Organized asset bundle | `.pawbytes/creative-suites/brands/{brand}/campaigns/{campaign}/assets/batch-{date}/` |
| batch-manifest.json | Bundle root folder |

## Output Structure

```
batch-{date}/
  instagram/
    posts/
    carousels/
    stories/
  linkedin/
    posts/
    carousels/
  tiktok/
  x-twitter/
  facebook/
  youtube/
  print/
  batch-manifest.json
```

## AI Model Selection for Batch

| Priority | Model | Best For |
|----------|-------|----------|
| Quality | Nano Banana Pro | Marketing posts with typography |
| Balanced | FLUX.2 [flex] | Bulk generation with good quality/speed |
| Speed | FLUX.1 [schnell] | Large batches where speed matters |

## Pipeline Steps

1. **Brief Intake** - Parse calendar/brief, extract asset specs
2. **Brand & Campaign Context** - Load guidelines and existing assets
3. **Production Queue Build** - Create ordered queue with resolved specs
4. **Batch Generation Loop** - Generate, overlay, validate, export each asset
5. **Bundle Organization** - Move assets into platform folders
6. **Batch Manifest** - Generate machine-readable manifest
7. **Review Gate** - Approve batch (interactive) or auto-approve (headless)
8. **Status Update** - Write to campaign status and daily log

## Error Handling

- Individual asset failures are logged but do not halt the batch
- Transient errors (HTTP 429, 5xx) trigger one retry after 5 seconds
- Missing brand guidelines result in `brand_validated: false` flag
- Template failures fall back to pure AI generation

## Quick Example

**Input**: Content calendar with 12 Instagram posts, 6 LinkedIn posts, 4 TikTok thumbnails for "Summer Sale" campaign

**Output**:
- `instagram/posts/summer-sale_instagram_post_001.png` through `_012.png`
- `linkedin/posts/summer-sale_linkedin_post_001.png` through `_006.png`
- `tiktok/summer-sale_tiktok_thumbnail_001.png` through `_004.png`
- `batch-manifest.json` with all 22 assets catalogued

## Related Skills

- [paw-cra-design-social](./paw-cra-design-social.md) - Individual social posts
- [paw-cra-design-brand](./paw-cra-design-brand.md) - Logos and brand assets
- [paw-cra-multi-platform-export](./paw-cra-multi-platform-export.md) - Export variants for all platforms