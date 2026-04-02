---
name: ai-image-prompting
description: Designer-oriented prompting framework for AI image generation
---

# AI Image Prompting for Designers

Structure prompts like creative briefs for consistent, brand-aligned results.

## The Prompt Framework

```
[Subject] + [Context/Environment] + [Style/Aesthetic] + [Technical Specs] + [Mood/Atmosphere]
```

| Component | Example |
|-----------|---------|
| **Subject** | "A barista crafting latte art" |
| **Context** | "in a minimalist coffee shop, morning light" |
| **Style** | "product photography, shallow depth of field" |
| **Technical** | "50mm lens, close-up, 8K resolution" |
| **Mood** | "warm, inviting, artisanal feeling" |

---

## Designer's Vocabulary

### Lighting Terms

| Term | Effect | Best For |
|------|--------|----------|
| **Golden hour** | Warm, soft, directional | Lifestyle, portraits |
| **Soft diffused** | Even, shadowless | Product photography |
| **Dramatic side lighting** | Strong shadows, depth | Editorial, luxury |
| **Studio lighting** | Controlled, professional | Product shots, portraits |
| **Natural window light** | Soft, authentic | Lifestyle, interiors |

### Camera Terms

| Term | When to Use |
|------|-------------|
| **Close-up / Macro** | Products, textures, food |
| **Overhead / Flat lay** | Products, food, workspace |
| **Shallow depth of field** | Subject isolation, bokeh |
| **Wide angle** | Interiors, landscapes |

### Style Descriptors

| Style | Best For |
|-------|----------|
| **Minimalist** | Modern brands, tech |
| **Editorial** | Fashion, lifestyle |
| **Lifestyle** | Social content, ads |
| **Product photography** | E-commerce, catalogs |
| **Cinematic** | Storytelling, campaigns |

### Mood Descriptors

| Mood | Color Temperature |
|------|-------------------|
| **Professional** | Cool neutral |
| **Warm/Inviting** | Warm tones |
| **Luxurious** | Deep, metallic |
| **Playful** | Vibrant, varied |
| **Bold/Energetic** | Saturated, contrasting |
| **Natural/Organic** | Earth tones |

---

## Platform-Specific Notes

### FLUX (fal.ai)

**Strengths:** Photorealistic outputs, strong text rendering, complex compositions

**Prompt Format:**
```
[Detailed scene description], [technical specs], [style modifiers], [quality boosters]
```

**Quality Boosters:** "highly detailed", "professional photography", "4K", "sharp focus"

### Recraft V4 Pro

**Best For:** Vector logos, icons, brand assets

### Ideogram V3

**Best For:** Logos, wordmarks, text-heavy graphics

---

## Prompt Templates

### Product Photography
```
[Product], [setting/background], [lighting], [camera angle], [mood]
```
> "Ceramic coffee dripper on textured wood, soft window light, overhead angle, warm artisanal mood"

### Lifestyle/Contextual
```
[Person] [action] in [environment], [time of day], [mood]
```
> "Young professional at laptop, modern coworking space, afternoon golden hour, focused mood"

### Illustration/Graphic
```
[Subject], [art style], [color palette], [composition]
```
> "Mountain landscape, flat vector illustration, earth tone palette, centered composition"

### Abstract/Conceptual
```
[Concept] as [visual metaphor], [color treatment], [texture]
```
> "Digital transformation as flowing data streams, blue to teal gradient, glass-like textures"

---

## Common Issues & Fixes

| Issue | Fix |
|-------|-----|
| **Too generic** | Add concrete details: "red leather armchair" not "chair" |
| **Wrong style** | Add style reference: "minimalist Scandinavian style" |
| **Poor lighting** | Specify: "golden hour light from the left" |
| **Off-brand colors** | Specify exact palette: "#2C5F2D forest green and #97BC62 sage" |
| **Low quality** | Add quality terms: "sharp focus, highly detailed" |

---

## Brand-Consistent Generation

**Extract brand DNA into prompt elements:**

| Brand Element | Prompt Translation |
|---------------|-------------------|
| Brand colors | Specify exact HEX values |
| Typography style | "clean sans-serif aesthetic" |
| Photography style | "lifestyle with natural light" |
| Visual mood | "approachable and modern" |

**Brand Prompt Template:**
```
[Subject], [brand color palette], [brand photography style], [brand mood], consistent with [brand name] aesthetic
```

**Consistency Tips:**
1. Use consistent style phrases across generations
2. Reference the same color palette each time
3. Use seed values when available for reproducibility
4. Iterate from a base image for variations

---

## Practical Examples

**Social Media Background:**
> "Abstract gradient from teal to coral, subtle geometric shapes, modern and clean, suitable for text overlay, 1080x1350"

**Product Hero:**
> "Smartphone floating at slight angle, clean white environment, soft studio lighting, premium tech aesthetic, 4K"

**Lifestyle Brand:**
> "Woman at sunlit cafe table, shallow depth of field, morning golden hour, natural authentic expression, warm and approachable"