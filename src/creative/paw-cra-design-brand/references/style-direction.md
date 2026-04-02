# Style Direction

Model selection logic and prompt engineering for brand asset production. Loaded during Step 3 of the pipeline.

## Model Selection Matrix

Choose the AI model based on asset type and desired aesthetic:

| Asset Type | Primary Model | Endpoint | Why |
|------------|---------------|----------|-----|
| **Logo (pictorial/abstract)** | Recraft V4 Pro | `fal-ai/recraft-v4` | Vector-style output, clean lines, scalable aesthetics |
| **Logo (combination mark)** | Recraft V4 Pro | `fal-ai/recraft-v4` | Symbol + text, maintains balance |
| **Icon set** | Recraft V4 Pro | `fal-ai/recraft-v4` | Consistent stroke weight, pixel-aligned |
| **Wordmark / Lettermark** | Ideogram V3 | Discover via MCP `search_models` | Superior text rendering, precise letterforms |
| **Flyer background** | FLUX.2 Pro | `fal-ai/flux-pro/v1.1` | High detail, print-quality imagery |
| **Banner background** | FLUX.2 Pro | `fal-ai/flux-pro/v1.1` | Wide format, detailed scenes |
| **Avatar / profile image** | FLUX.2 Flex or Recraft V4 | Model-dependent | Character marks or brand symbols |

**Fallback:** If the primary model is unavailable or produces poor results, fall back to FLUX.2 Pro for general imagery or Nano Banana Pro for text-heavy designs.

## Prompt Engineering by Asset Type

### Logos and Icons

Build prompts emphasizing:
- **Simplicity** -- "minimalist", "clean lines", "simple geometry"
- **Scalability** -- "vector style", "works at any size", "scalable"
- **Brand alignment** -- include exact hex colors, industry context, brand personality
- **Technical** -- "transparent background", "centered composition", "isolated subject"

**Prompt template:**
```
{brand_name} logo, {logo_type} style, {color_palette_description},
{aesthetic_direction}, clean design, scalable, professional quality,
transparent background, vector style, {industry_context}
```

**Icon-specific additions:**
```
consistent stroke weight, pixel-aligned, {size}px grid,
{outline|filled|duotone} style, {brand_color} primary
```

### Wordmarks

Build prompts emphasizing:
- **Typography** -- "custom lettering", "distinctive typography", "letterform design"
- **Readability** -- "legible at small sizes", "clear letterforms"
- **Brand personality** -- "modern", "elegant", "bold", "playful" (match brand voice)

**Prompt template:**
```
"{brand_name}" wordmark logo, custom typography, {style_adjectives},
{color} on {background}, professional brand identity,
clean letterforms, {industry_context}
```

### Flyer and Banner Backgrounds

Build prompts for the background image only (text is added via HTML/CSS overlay):
- **Atmosphere** -- scene, mood, lighting that supports the message
- **Space for text** -- "with clear area for text overlay", "negative space in upper third"
- **Brand colors** -- incorporate brand palette into the scene
- **No text in image** -- "no text", "no words", "no typography" (text comes from overlay)

**Prompt template:**
```
{scene_description}, {mood_and_lighting}, {brand_color} color scheme,
professional {event_type} aesthetic, with clear negative space for text overlay,
no text, no words, high quality, {print|digital} ready
```

**Resolution for print flyers:**
- A4: `"width": 2480, "height": 3508` (300 DPI equivalent)
- Letter: `"width": 2550, "height": 3300`
- A5: `"width": 1748, "height": 2480`

### Avatars

Build prompts for brand-representative profile images:
- Square format (`"image_size": "square_hd"` = 1024x1024)
- Brand mark or character that works at small sizes
- High contrast for visibility in circular crops

## Iteration Strategy

**Interactive mode:** Generate 2-3 variations with slightly different prompt emphases:
1. Variation A: Core interpretation (closest to brief)
2. Variation B: More stylized/creative take
3. Variation C: Simplified/minimal take

Present all three and let user choose, then optionally refine the chosen direction.

**Headless mode:** Generate 1 image with the most direct interpretation of the brief. Use the core prompt without creative departures.

## Style Keyword Reference

Map brand voice/personality to visual style keywords:

| Brand Voice | Visual Keywords |
|-------------|----------------|
| Professional / Corporate | clean, structured, geometric, balanced, restrained palette |
| Creative / Playful | organic shapes, vibrant colors, dynamic composition, hand-drawn feel |
| Luxury / Premium | minimal, refined, serif typography, muted palette, generous whitespace |
| Tech / Modern | geometric, flat design, gradient accents, sans-serif, monospace elements |
| Natural / Organic | earth tones, botanical elements, hand-crafted feel, warm palette |
| Bold / Disruptive | high contrast, oversized typography, unconventional layout, saturated color |
