# AI Video Models Guide

## Overview

Reference for AI video generation models available through fal.ai and egaki CLI. Use this guide to select the right model for each production scenario.

## Model Comparison

### Veo 3.1 (Google via fal.ai)

| Attribute | Value |
|-----------|-------|
| **Provider** | fal.ai (`fal-ai/veo3`) |
| **Best for** | Cinematic quality, complex camera movements, realistic scenes |
| **Duration** | 5-17 seconds per clip |
| **Resolution** | Up to 1080p |
| **Strengths** | Film-quality motion, physical realism, complex scenes |
| **Weaknesses** | Slower generation, higher cost per clip |

**When to use:** Hero scenes, opening shots, cinematic B-roll, any clip where visual quality is the priority.

**CLI (curl):**
```bash
curl -X POST "https://queue.fal.run/fal-ai/veo3" \
  -H "Authorization: Key $FAL_KEY" \
  -H "Content-Type: application/json" \
  -d '{"prompt": "...", "aspect_ratio": "9:16", "duration": "8s"}'
```

### Kling v3 Standard (via fal.ai)

| Attribute | Value |
|-----------|-------|
| **Provider** | fal.ai (`fal-ai/kling-video/v3/standard`) |
| **Best for** | Fast iteration, social content, bulk generation |
| **Duration** | 5-10 seconds per clip |
| **Resolution** | Up to 1080p |
| **Strengths** | Fast generation, good motion quality, cost-effective |
| **Weaknesses** | Less cinematic than Veo for complex scenes |

**When to use:** Social media content, rapid prototyping, bulk scene generation, iterative refinement.

### Kling v3 Pro (via fal.ai)

| Attribute | Value |
|-----------|-------|
| **Provider** | fal.ai (`fal-ai/kling-video/v3/pro`) |
| **Best for** | High-quality branded content, precise motion |
| **Duration** | 5-10 seconds per clip |
| **Resolution** | Up to 1080p |
| **Strengths** | Better quality than Standard, more controlled motion |
| **Weaknesses** | Slower and more expensive than Standard |

**When to use:** Final production clips, brand videos, content where quality matters more than speed.

### Kling Image-to-Video (via fal.ai)

| Attribute | Value |
|-----------|-------|
| **Provider** | fal.ai (`fal-ai/kling-video/v3/standard/image-to-video`) |
| **Best for** | Animating still images, brand assets, product shots |
| **Input** | Static image + motion prompt |
| **Duration** | 5-10 seconds |

**When to use:** Animating brand logos, bringing product images to life, creating motion from existing visual assets.

## Model Selection Matrix

| Scenario | Recommended Model | Reasoning |
|----------|------------------|-----------|
| Short-form social content | Kling v3 Standard | Speed and cost for iteration |
| YouTube hero scene | Veo 3.1 | Maximum visual quality |
| Brand intro animation | Kling Image-to-Video | Starts from brand assets |
| Bulk scene generation | Kling v3 Standard | Cost-effective at volume |
| Cinematic B-roll | Veo 3.1 | Realistic motion and lighting |
| Product showcase | Kling v3 Pro | Controlled, precise motion |

## Generation Workflow

1. **Submit job** via curl to fal.ai queue endpoint
2. **Poll for completion** -- video generation takes 30-120 seconds
3. **Download result** to local working directory
4. **Verify quality** -- check for motion artifacts, style consistency
5. **Retry if needed** -- adjust prompt and regenerate

## Prompting Best Practices

- **Be specific about camera:** "slow dolly in", "static wide shot", "handheld tracking"
- **Describe lighting:** "golden hour", "studio lit", "neon-lit urban"
- **Specify motion:** "person walks left to right", "camera pans slowly right"
- **Include style:** "cinematic", "documentary", "commercial quality"
- **Brand context:** Reference brand colors and visual style in prompts

## egaki CLI Alternative

For multi-provider access when configured:

```bash
# Text-to-video
egaki video generate --prompt "..." --provider veo --duration 8s --output scene_01.mp4

# Image-to-video
egaki video animate --image brand_logo.png --prompt "logo reveals with particle effect" --output intro.mp4
```

egaki abstracts provider differences and handles queue polling automatically.
