# paw-cra-design-brand

## Overview

Brand asset and flyer production pipeline that creates logos, icons, banners, avatars, and promotional materials. Outputs production-ready files in multiple formats with brand validation ensuring every asset matches established guidelines.

## What It Does

| Capability | Description |
|------------|-------------|
| Logos | Pictorial, abstract, and combination marks with PNG + SVG output |
| Icons | Scalable icon assets with vector format |
| Wordmarks | Typography-focused letterform designs |
| Avatars | Profile images at 400x400 standard |
| Banners | Platform-specific or custom dimensions |
| Flyers | Digital (PNG) and print (PNG + PDF at 300 DPI) |

## When to Use It

- You need a new logo or brand mark
- You want icons or avatar images for a brand
- You need promotional flyers for print or digital
- You require banners for web or social
- You want multi-format exports (PNG, SVG, PDF)

## Trigger Phrases

- "create logo"
- "design brand asset"
- "make flyer"
- "generate icon"
- "create banner"
- "design wordmark"

## What You Get (Deliverables)

| Output | Location |
|--------|----------|
| Logo/icon PNG (512px, 1024px) | `.pawbytes/creative-suites/brands/{brand}/assets/brand-identity/` |
| Logo/icon SVG | Same folder |
| Flyers (PNG, PDF) | `.pawbytes/creative-suites/brands/{brand}/assets/flyers/` |
| Banners | `.pawbytes/creative-suites/brands/{brand}/assets/banners/` |
| design-manifest.json | Assets folder root |

## Asset Types and Models

| Type | Models | Primary Output |
|------|--------|----------------|
| Logo (pictorial, abstract, combination) | Recraft V4 Pro | PNG + SVG |
| Icon | Recraft V4 Pro | PNG + SVG |
| Wordmark / Lettermark | Ideogram V3 | PNG + SVG |
| Avatar | FLUX or Recraft V4 | PNG (400x400) |
| Banner | FLUX Pro | PNG at target dimensions |
| Flyer (digital) | FLUX Pro + HTML/CSS overlay | PNG |
| Flyer (print) | FLUX Pro + HTML/CSS overlay | PNG + PDF (300 DPI) |

## Pipeline Steps

1. **Brief Intake** - Parse asset type, brand, style, dimensions
2. **Brand Context** - Load colors, typography, logo rules from guidelines
3. **Style Direction** - Determine model and prompt approach
4. **AI Generation** - Execute via fal.ai, download to local
5. **Flyer Rendering** - HTML/CSS overlay for text content (flyers only)
6. **Brand Validation** - Verify colors, typography, style consistency
7. **Multi-Format Export** - Generate all required formats and sizes
8. **Manifest & Delivery** - Write manifest, update daily log

## Quick Example

**Input**: "Create a minimalist logo for brand 'Nova', tech startup vibe, blue color palette"

**Output**:
- `logo_full-color_512.png`
- `logo_full-color_1024.png`
- `logo_full-color.svg` (traced from raster)
- `logo_monochrome.png`
- `logo_reversed.png`
- `design-manifest.json`

## Related Skills

- [paw-cra-design-social](./paw-cra-design-social.md) - Social posts and carousels
- [paw-cra-design-batch](./paw-cra-design-batch.md) - Bulk asset production
- [paw-cra-agent-designer](./paw-cra-agent-designer.md) - Designer agent for visual production