# paw-cra-agent-designer

## Overview

The Designer is a visual production specialist who transforms approved concepts into polished, brand-consistent assets. Creates production-ready visuals -- social posts, carousels, flyers, brand assets, and reusable code-based templates -- correctly sized for each platform.

## What It Does

| Capability | Description |
|------------|-------------|
| Social Post Design | Single-image posts for Instagram, LinkedIn, X, Facebook |
| Carousel Design | Multi-slide carousels with swipe progression |
| Flyer Design | Event flyers, promotional materials, informational handouts |
| Brand Asset Generation | Logos, icons, avatars, banners using AI models |
| Asset Resizing | Platform-specific resizes maintaining brand consistency |
| Template Creation | Reusable HTML/CSS templates for hybrid workflows |
| Research & Learn | Discovers platform specs, design trends, technical guides |

## When to Use It

- Creating social media posts or carousels
- Designing promotional flyers or brand graphics
- Generating logos, icons, or brand assets
- Resizing existing assets for different platforms
- Building reusable design templates

## Trigger Phrases

- "Create a social post for..."
- "Design a carousel about..."
- "Make a flyer for..."
- "Generate a logo for..."
- "Resize this image for..."
- "Create a template for..."

## What You Get (Deliverables)

| Output | Location |
|--------|----------|
| Production-ready images | `.pawbytes/creative-suites/brands/{brand}/campaigns/{campaign}/` |
| Design manifest | `design-manifest.json` in campaign folder |
| HTML/CSS templates | `.pawbytes/creative-suites/knowledge/templates/` |

## Arguments

| Arg | Description |
|-----|-------------|
| `--headless` or `-H` | Non-interactive execution |

## AI Models (2026)

| Model | Best For | Text Quality |
|-------|----------|--------------|
| Nano Banana Pro | Marketing posts, typography-heavy designs | Excellent |
| FLUX.2 [pro] | Premium quality, detailed imagery | Very Good |
| FLUX.2 [flex] | Balanced quality/speed, typography | Excellent |
| FLUX.1 [schnell] | Rapid prototyping, bulk generation | Good |
| Recraft V4 Pro | Vector logos, icons, brand assets | Very Good |
| Ideogram V3 | Logos, wordmarks, text-heavy graphics | Excellent |

## Tool Dependencies

| Tool | Purpose | Required |
|------|---------|----------|
| fal.ai MCP | Model discovery, schema lookup | Yes |
| fal.ai CLI (curl) | Image generation | Yes |
| ffmpeg | Animated carousels | Optional |
| Puppeteer/Playwright | HTML template rendering | Optional |

## Quick Example

**Input**: "Create an Instagram carousel about our new product launch, 4 slides, brand colors"

**Output**: Production-ready 1080x1350px carousel PNGs with brand color palette, clear visual hierarchy, swipe progression, and correct safe zones for Instagram UI. Includes `design-manifest.json` with asset details.

## Platform Specifications

| Platform | Dimensions | Aspect Ratio |
|----------|------------|--------------|
| Instagram Feed | 1080x1350px | 4:5 |
| Instagram Story | 1080x1920px | 9:16 |
| LinkedIn Feed | 1200x1200px | 1:1 |
| X (Twitter) | 1200x675px | 16:9 |
| Facebook Feed | 1200x630px | 1.91:1 |

## Related Skills

- [paw-cra-agent-creative-director](./paw-cra-agent-creative-director.md) -- Orchestrator and entry point
- [paw-cra-campaign-orchestration](./paw-cra-campaign-orchestration.md) -- Multi-deliverable campaigns
- [paw-cra-quality-control](./paw-cra-quality-control.md) -- Campaign-level QC