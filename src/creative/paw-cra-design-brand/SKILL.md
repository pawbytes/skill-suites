---
name: paw-cra-design-brand
description: Brand asset and flyer production pipeline. Use when user requests 'create logo', 'design brand asset', 'make flyer', 'generate icon', or 'create banner'.
---

# Brand Asset & Flyer Production

## Overview

This workflow produces brand assets (logos, icons, avatars, banners) and flyers from brief to finished files. It is the Designer's companion workflow for brand identity and promotional print/digital materials. Act as a visual production specialist who understands brand systems, vector aesthetics, and print production requirements.

**Args:** Accepts `--headless` / `-H` for non-interactive execution with sensible defaults.

**Output:** Production-ready assets in multiple formats (PNG + SVG for logos/icons, PNG/PDF for flyers at 300 DPI for print) plus a `design-manifest.json` cataloging everything produced.

**Pipeline:** Brief intake -> brand context load -> style direction -> AI generation -> brand validation -> multi-format export -> delivery with manifest.

**Key constraint:** Every output is verified against brand guidelines before delivery. Off-brand colors, fonts, or styles are caught and corrected before export.

## On Activation

Load available config from `{project-root}/.pawbytes/config/config.yaml` and `{project-root}/.pawbytes/config/config.user.yaml` (root level and `cra` section). If config is missing, let the user know `paw-cra-setup` can configure the module at any time. Resolve and apply throughout the session (defaults in parens):

- `{user_name}` (null) -- address the user by name
- `{communication_language}` (English) -- use for all communications
- `{fal_key}` (null) -- fal.ai API key (required for AI generation)
- `{output_directory}` (`.pawbytes/creative-suites`) -- base output path
- `{default_brand}` (null) -- default brand name

Load shared agency memory:
- `{project-root}/.pawbytes/creative-suites/index.md` -- active brands and campaigns
- `{project-root}/.pawbytes/creative-suites/brands/{brand}/guidelines.md` -- brand context (loaded after brand is identified)

Verify tool availability:
- `fal_key` -- required for all AI generation
- Puppeteer/Playwright -- required for flyer template rendering
- ffmpeg -- optional, for format conversion

If `--headless` or `-H` is passed, execute the full pipeline without interaction using the brief provided. Otherwise, proceed interactively through the pipeline steps.

## Pipeline

### Step 1: Brief Intake

Parse the incoming brief (from user, Aria, or campaign brief file). Extract:

| Field | Required | Default |
|-------|----------|---------|
| **Asset type** | Yes | -- |
| **Brand name** | Yes | `{default_brand}` |
| **Style direction** | No | Inferred from brand guidelines |
| **Dimensions** | No | Standard for asset type |
| **Content/copy** | For flyers | -- |
| **Output type** | No | Digital |

**Asset types supported:**

| Type | Models | Primary Output |
|------|--------|----------------|
| Logo (pictorial, abstract, combination) | Recraft V4 Pro | PNG + SVG |
| Icon | Recraft V4 Pro | PNG + SVG |
| Wordmark / Lettermark | Ideogram V3 | PNG + SVG |
| Avatar | FLUX or Recraft V4 | PNG (400x400) |
| Banner | FLUX Pro | PNG at target dimensions |
| Flyer (digital) | FLUX Pro + HTML/CSS overlay | PNG |
| Flyer (print) | FLUX Pro + HTML/CSS overlay | PNG + PDF (300 DPI) |

If interactive and the brief is incomplete, ask targeted questions to fill gaps. In headless mode, use sensible defaults and note assumptions in the manifest.

### Step 2: Brand Context

Load brand guidelines from `{project-root}/.pawbytes/creative-suites/brands/{brand-name}/guidelines.md`.

Extract and keep available throughout the pipeline:
- Color palette (primary, secondary, accent hex values)
- Typography (heading font, body font)
- Logo paths (if existing logos are referenced)
- Voice/tone keywords (inform style direction)
- Any existing asset conventions

If no brand guidelines exist, inform the user and offer to proceed with the style direction from the brief alone, or suggest running Aria's brand onboarding first.

### Step 3: Style Direction

Load `./references/style-direction.md` for model selection logic and prompt engineering guidance.

Determine the generation approach based on asset type and brief:

| Asset Category | Approach |
|----------------|----------|
| **Logos / Icons** | Vector-style via Recraft V4 Pro -- clean, scalable, minimal |
| **Wordmarks** | Typography-focused via Ideogram V3 -- precise letterforms |
| **Flyers / Banners** | AI background via FLUX Pro + HTML/CSS text overlays |
| **Avatars** | Character/brand mark via best-fit model |

Build the generation prompt incorporating brand colors, style keywords, and asset-specific requirements. For logos and icons, emphasize simplicity, scalability, and clean lines. For flyers, separate background generation from text content.

If interactive, present the style direction and model choice for approval before generation. In headless mode, proceed with the determined direction.

### Step 4: AI Generation

Load `./references/generation-pipeline.md` for CLI commands and model-specific parameters.

Execute generation using the fal.ai CLI (curl). Model endpoints:

| Model | Endpoint | Use For |
|-------|----------|---------|
| Recraft V4 Pro | `fal-ai/recraft-v4` | Logos, icons, brand marks |
| Ideogram V3 | Discover via fal.ai MCP | Wordmarks, text-heavy logos |
| FLUX.2 Pro | `fal-ai/flux-pro/v1.1` | Flyer backgrounds, banners, avatars |

Generate 2-3 variations for interactive mode (user picks best). Generate 1 best-fit for headless mode.

Download all generated images to `{project-root}/.pawbytes/creative-suites/brands/{brand-name}/assets/wip/` immediately -- never leave assets as URLs only.

### Step 5: Flyer Template Rendering (flyers only)

Load `./references/flyer-rendering.md` for template architecture and rendering pipeline.

For flyers and banners that need text overlays:

1. Use the AI-generated image as background
2. Build HTML/CSS overlay with headline, body copy, CTA, brand logo, and contact info
3. Apply brand typography and colors from guidelines
4. Render via Puppeteer/Playwright using element-specific screenshots (never `fullPage: true`)
5. For print: render at 300 DPI equivalent resolution (A4 = 2480x3508px)

**Critical:** Use element-specific screenshots on `.design-container` to avoid white gaps. See template system reference for the correct rendering approach.

### Step 6: Brand Validation

Before export, verify every produced asset against brand guidelines:

**Color check:** All brand colors used match the palette from guidelines. No unapproved colors introduced by AI generation.

**Typography check:** For flyers/banners with text overlays -- fonts match brand specs, sizes maintain hierarchy, contrast meets 4.5:1 minimum.

**Style consistency:** Visual style aligns with brand tone (e.g., minimalist brand should not get a maximalist logo).

**Technical check:**
- Logo/icon assets work at both small (32px) and large (1024px+) sizes
- Flyer content stays inside safety zones (3mm from trim for print)
- Resolution meets requirements (300 DPI for print, 72+ DPI for digital)

If validation fails, note the issues and either auto-correct (e.g., color replacement) or flag for revision. In interactive mode, present issues to user. In headless mode, attempt correction and log any unresolvable issues.

### Step 7: Multi-Format Export

Export approved assets to final location:

**Logos and Icons:**
- Full color PNG (transparent background) at 512px and 1024px
- SVG: Use Recraft V4 Pro's native SVG output when available. For raster-only sources, use `potrace` or `vtracer` CLI for bitmap-to-vector tracing — note that AI-generated raster images produce approximate SVG outlines, not true vector art. Flag in manifest as `svg_source: "traced"` vs `svg_source: "native"`.
- Monochrome variant
- Reversed (white on transparent) variant

**Flyers:**
- Digital: PNG at target dimensions, RGB
- Print: High-res PNG (300 DPI) + PDF with bleed margins. For 300 DPI rendering in Puppeteer, set viewport to print dimensions at 300/72 scale (e.g., A4 = `{ width: 2480, height: 3508, deviceScaleFactor: 1 }`). Note: output is RGB — if CMYK is required for a professional print shop, inform the user that a post-export conversion via ImageMagick (`convert input.png -colorspace CMYK output.tiff`) or a dedicated prepress tool is needed. Flag in manifest as `color_mode: "RGB"` with a note when print output is requested.

**Banners and Avatars:**
- PNG at exact target dimensions

**File naming:** `{asset-type}_{descriptor}_{date}.{ext}`
**Location:** `{project-root}/.pawbytes/creative-suites/brands/{brand-name}/assets/`

Organize into subdirectories:
```
assets/
  brand-identity/
    logo/
    icons/
  flyers/
  banners/
  avatars/
```

### Step 8: Manifest & Delivery

Write `design-manifest.json` to the brand assets directory:

```json
{
  "workflow": "paw-cra-design-brand",
  "brand": "{brand-name}",
  "created": "ISO-8601 timestamp",
  "assets": [
    {
      "type": "logo",
      "description": "Primary logo, full color",
      "files": ["logo/logo-full-color-512.png", "logo/logo-full-color-1024.png", "logo/logo-full-color.svg"],
      "dimensions": "512x512, 1024x1024",
      "colorMode": "RGB",
      "status": "approved"
    }
  ],
  "validation": {
    "brandConsistency": "pass",
    "technicalSpecs": "pass",
    "issues": []
  }
}
```

Append activity to daily log at `{project-root}/.pawbytes/creative-suites/daily/YYYY-MM-DD.md`:
```
[Designer] Brand asset production for {brand-name}: {count} assets created. See design-manifest.json.
```

Present final summary with file paths and any notes.

## References

| Reference | Purpose | Loaded When |
|-----------|---------|-------------|
| `./references/style-direction.md` | Model selection, prompt engineering by asset type | Step 3 |
| `./references/generation-pipeline.md` | fal.ai CLI commands, async generation, download | Step 4 |
| `./references/flyer-rendering.md` | HTML/CSS template architecture, Puppeteer rendering | Step 5 (flyers only) |
