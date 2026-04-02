# Stage 2: Production

## Outcome

Generated visual assets -- AI-created backgrounds with text overlays applied -- saved to disk and ready for validation. For carousels, all slides maintain consistent visual style.

## Layout Planning

Before generating any images, plan the visual composition:

**Single Post:**
- Determine visual hierarchy: what is seen first (headline), second (supporting visual), third (CTA/logo)
- Choose color scheme from brand guidelines (primary for backgrounds, accent for CTAs)
- Plan text placement within safe zones
- Decide generation approach: full AI generation vs. hybrid (AI background + HTML text overlay)

**Carousel:**
- Determine narrative structure from content (listicle, tutorial, myth-fact, transformation, problem-solution)
- Plan slide-by-slide content breakdown: one key idea per slide
- Design consistent visual language: color palette, typography scale, grid structure, recurring elements
- First slide = hook (bold, high-contrast, value proposition under 12 words)
- Final slide = CTA with branding
- Include swipe cues and optional progress indicators

Reference the Designer's carousel design patterns from `{project-root}/skills/paw-cra-agent-designer/references/carousel-design.md` for narrative structures.

## AI Image Generation

Use fal.ai API via CLI (curl) for generation. MCP for model discovery if needed.

**Model selection:**
- Text-heavy marketing posts: `fal-ai/nano-banana-pro`
- Photo-realistic content: `fal-ai/flux-pro/v1.1`
- Balanced quality/speed: `fal-ai/flux/dev`
- Rapid prototyping: `fal-ai/flux/schnell`

Reference `{project-root}/skills/paw-cra-agent-designer/references/ai-models-guide.md` for CLI commands and endpoint details.

### Generation Process

**Environment:** Ensure `FAL_KEY` is set from config.

**Single post generation:**

```bash
# Submit generation
curl -s -X POST "https://queue.fal.run/{model-endpoint}" \
  -H "Authorization: Key $FAL_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "prompt": "{designer-oriented prompt with brand colors, style, content}",
    "image_size": "{preset or custom width/height}"
  }' --output result.json

# Download to workspace
IMAGE_URL=$(cat result.json | jq -r '.images[0].url')
curl -s -o "{output_path}" "$IMAGE_URL"
```

**Carousel generation -- consistency strategy:**
- Use the same core style prompt across all slides (brand colors, aesthetic, typography direction)
- Vary only the content-specific elements per slide
- Generate slides sequentially, verifying style consistency
- If a slide deviates in style, regenerate with the core prompt reinforced

### Prompt Construction

Build designer-oriented prompts that include:
- Exact brand colors as HEX values
- Style direction (minimalist, bold, editorial, lifestyle)
- Content/copy to be rendered in the image
- Platform context (e.g., "Instagram 4:5 ratio, lifestyle photography")
- Typography direction if text is part of the AI generation

Reference `{project-root}/skills/paw-cra-agent-designer/references/ai-image-prompting.md` for prompt frameworks.

### Image Size Presets

| Platform Format | fal.ai Preset | Custom Dims |
|-----------------|--------------|-------------|
| Instagram 4:5 | `portrait_4_5` | 1080x1350 |
| Instagram 1:1 | `square_hd` | 1080x1080 |
| Instagram Story | `portrait_9_16` | 1080x1920 |
| LinkedIn Post | -- | 1200x627 |
| X Post | `landscape_16_9` | 1200x675 |

## Template Rendering

When using the hybrid approach (AI background + HTML/CSS text overlay):

Reference `{project-root}/skills/paw-cra-agent-designer/references/template-system.md` for architecture and `{project-root}/skills/paw-cra-agent-designer/references/template-examples.md` for code patterns.

**Critical rendering rules:**
1. Set HTML/body dimensions to exact target size with `overflow: hidden`
2. Use a `.design-container` div at exact dimensions
3. Screenshot the container element, NEVER use `fullPage: true`
4. Wait for fonts: `await page.evaluate(() => document.fonts.ready)`
5. Wait for images to load before screenshot
6. Apply brand CSS variables from guidelines

**Template selection:**

| Content Type | Template |
|-------------|----------|
| Hero image + headline | `single-post-hero` |
| Quote graphic | `single-post-quote` |
| Announcement | `single-post-announcement` |
| Statistic highlight | `single-post-stat` |
| Carousel listicle | `carousel-listicle` |
| Carousel tutorial | `carousel-tutorial` |
| Carousel story | `carousel-story` |

If no existing template fits, create an inline HTML/CSS template following the template system architecture.

## File Output

Save all generated assets to the workspace immediately after generation:

```
{output_directory}/brands/{brand}/assets/{campaign}/social/
```

Create the directory if it doesn't exist. Use naming convention:
- Single: `{platform}_{post-type}_{YYYYMMDD_HHMMSS}.png`
- Carousel: `{platform}_carousel_{YYYYMMDD_HHMMSS}_slide{NN}.png`

**Always download images to the workspace.** Never just return URLs.
