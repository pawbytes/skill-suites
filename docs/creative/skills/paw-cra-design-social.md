# paw-cra-design-social

## Overview

Social post and carousel production pipeline that transforms briefs into platform-ready visual assets. This is the most common visual output in the Aria Creative Suite, handling everything from single posts to multi-slide carousels with brand validation built into the production flow.

## What It Does

| Capability | Description |
|------------|-------------|
| Single posts | Platform-correct images for Instagram, LinkedIn, TikTok, X, Facebook |
| Carousels | Multi-slide sequences with visual consistency across all slides |
| Stories | Vertical format content for Instagram and Facebook Stories |
| Brand validation | Embedded checks ensure colors, typography, and style match guidelines |
| AI generation | Multiple models optimized for different content types |

## When to Use It

- You need a single social media post for any platform
- You want to create a carousel or multi-slide content
- You have a brief with platform, format, and copy ready
- You need stories or vertical-format social content
- You want brand-consistent visuals without manual design work

## Trigger Phrases

- "create social post"
- "design carousel"
- "run social design workflow"
- "make an Instagram post"
- "create LinkedIn carousel"

## What You Get (Deliverables)

| Output | Location |
|--------|----------|
| PNG/JPG images | `.pawbytes/creative-suites/brands/{brand}/assets/{campaign}/social/` |
| design-manifest.json | Same folder as assets |

## Platform Specifications

| Platform | Post | Carousel | Story |
|----------|------|----------|-------|
| Instagram | 1080x1350 (4:5) | 1080x1080 or 1080x1350 | 1080x1920 |
| LinkedIn | 1200x627 | 1080x1080 (PDF) | 1080x1920 |
| TikTok | 1080x1920 | -- | 1080x1920 |
| X (Twitter) | 1200x675 | -- | -- |
| Facebook | 1200x630 | 1080x1080 | 1080x1920 |

## AI Model Selection

| Use Case | Primary Model | Fallback |
|----------|--------------|----------|
| Text-heavy posts | Nano Banana Pro | FLUX.2 [flex] |
| Photo-realistic | FLUX.2 [pro] | FLUX.2 [flex] |
| Rapid prototyping | FLUX.1 [schnell] | -- |
| Carousel consistency | FLUX.2 [flex] | Nano Banana Pro |

## Pipeline Stages

1. **Brief & Context** - Parse brief, load platform specs, resolve copy
2. **Production** - Plan layout, generate AI imagery, render text overlays
3. **Validation & Export** - Brand check, platform validation, export with manifest

## Quick Example

**Input**: "Create an Instagram carousel for our spring sale, 3 slides, brand is Acme, highlight 30% off"

**Output**: 
- `instagram_carousel_2026-04-02_slide01.png`
- `instagram_carousel_2026-04-02_slide02.png`
- `instagram_carousel_2026-04-02_slide03.png`
- `design-manifest.json`

## Related Skills

- [paw-cra-design-brand](./paw-cra-design-brand.md) - Logos, icons, flyers
- [paw-cra-design-batch](./paw-cra-design-batch.md) - Bulk campaign production
- [paw-cra-multi-platform-export](./paw-cra-multi-platform-export.md) - Resize for all platforms