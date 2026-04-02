---
name: ai-models-guide
description: AI model selection guide with CLI commands for fal.ai image generation
---

# AI Models Guide for Designer

This reference provides model recommendations and CLI commands for image generation using fal.ai. Use MCP for discovery, CLI for generation.

---

## Workflow: MCP for Discovery, CLI for Generation

### Why This Hybrid Approach?

| Task | Tool | Why |
|------|------|-----|
| **Model search** | MCP `search_models` | AI-assisted discovery |
| **Schema lookup** | MCP `get_model_schema` | Understand parameters |
| **Pricing check** | MCP `get_pricing` | Cost estimation |
| **Image generation** | CLI `curl` | Faster, more reliable for long jobs |
| **File download** | CLI `curl` | Save to workspace, not just URL |

**Generation takes 10-30+ seconds.** CLI with polling handles this better than MCP, which can timeout on long-running operations.

---

## fal.ai CLI Commands

### Environment Setup

```bash
# Set your API key (from config.user.yaml or environment)
export FAL_KEY="your-fal-key-here"
```

### Generate Image (Sync - Wait for Result)

```bash
curl -X POST "https://queue.fal.run/fal-ai/flux-pro/v1.1" \
  -H "Authorization: Key $FAL_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "prompt": "Your prompt here",
    "image_size": "landscape_16_9",
    "num_inference_steps": 28
  }' \
  --output result.json

# Extract image URL and download
IMAGE_URL=$(cat result.json | jq -r '.images[0].url')
curl -o "output.png" "$IMAGE_URL"
```

### Generate Image (Async - Submit & Poll)

For long-running generations (FLUX.2 pro, high-res):

```bash
# 1. Submit job
REQUEST_ID=$(curl -s -X POST "https://queue.fal.run/fal-ai/flux-pro/v1.1/requests" \
  -H "Authorization: Key $FAL_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "prompt": "Your prompt here",
    "image_size": "landscape_16_9"
  }' | jq -r '.request_id')

# 2. Poll for completion
STATUS="IN_PROGRESS"
while [ "$STATUS" != "COMPLETED" ]; do
  sleep 2
  RESPONSE=$(curl -s "https://queue.fal.run/fal-ai/flux-pro/v1.1/requests/$REQUEST_ID/status" \
    -H "Authorization: Key $FAL_KEY")
  STATUS=$(echo "$RESPONSE" | jq -r '.status')
  echo "Status: $STATUS"
done

# 3. Get result and download
RESULT=$(curl -s "https://queue.fal.run/fal-ai/flux-pro/v1.1/requests/$REQUEST_ID" \
  -H "Authorization: Key $FAL_KEY")
IMAGE_URL=$(echo "$RESULT" | jq -r '.images[0].url')
curl -o "output.png" "$IMAGE_URL"
```

### Helper Function for Bash

Add to your workflow:

```bash
fal_generate() {
  local MODEL="$1"
  local PROMPT="$2"
  local OUTPUT="$3"
  local SIZE="${4:-landscape_16_9}"

  # Submit and wait
  RESULT=$(curl -s -X POST "https://queue.fal.run/$MODEL" \
    -H "Authorization: Key $FAL_KEY" \
    -H "Content-Type: application/json" \
    -d "{\"prompt\": \"$PROMPT\", \"image_size\": \"$SIZE\"}")

  # Download image
  IMAGE_URL=$(echo "$RESULT" | jq -r '.images[0].url')
  curl -s -o "$OUTPUT" "$IMAGE_URL"
  echo "Saved to: $OUTPUT"
}

# Usage:
fal_generate "fal-ai/flux-pro/v1.1" "A mountain lake at sunset" "output.png"
```

---

## Model Endpoints

### Primary Models

| Model | Endpoint | Best For |
|-------|----------|----------|
| **FLUX.2 [pro]** | `fal-ai/flux-pro/v1.1` | Premium quality, detailed imagery |
| **FLUX.2 [flex]** | `fal-ai/flux/dev` | Balanced quality/speed, typography |
| **FLUX.1 [schnell]** | `fal-ai/flux/schnell` | Rapid prototyping, 4-step generation |
| **FLUX Kontext** | `fal-ai/flux-context` | Image editing, style transfer |
| **Nano Banana Pro** | `fal-ai/nano-banana-pro` | Text-heavy designs, marketing posts |
| **Recraft V4** | `fal-ai/recraft-v4` | Vector logos, icons, brand assets |

### Model Selection by Capability

---

## Social Post Design

### Recommended Models

| Priority | Model | Why |
|----------|-------|-----|
| **1st Choice** | Nano Banana Pro | Best text rendering, marketing copy |
| **2nd Choice** | FLUX.2 [flex] | Enhanced typography, good balance |
| **Fast/Prototype** | FLUX.1 [schnell] | Rapid iteration, 4-step |

### CLI Example

```bash
curl -X POST "https://queue.fal.run/fal-ai/nano-banana-pro" \
  -H "Authorization: Key $FAL_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "prompt": "Marketing post for tech startup. Young professional using laptop in modern cafe. Brand colors: deep blue #1a365d. Text overlay: Work Anywhere. Instagram 4:5 ratio, lifestyle photography.",
    "image_size": "portrait_4_5"
  }' \
  --output result.json

# Download
curl -o "social-post.png" "$(cat result.json | jq -r '.images[0].url')"
```

---

## Carousel Design

### Recommended Models

| Priority | Model | Why |
|----------|-------|-----|
| **1st Choice** | FLUX.2 [flex] | Consistent style across slides |
| **2nd Choice** | Nano Banana Pro | Text rendering for educational content |

### Consistency Strategy

Use **same seed** or **LoRA** for carousel slides:

```bash
# Generate all slides with same core prompt
CORE_PROMPT="Modern minimalist design, clean white background, forest green #2C5F2D primary, amber #D4A574 accent, geometric shapes, sans-serif typography"

# Slide 1
curl -X POST "https://queue.fal.run/fal-ai/flux/dev" \
  -H "Authorization: Key $FAL_KEY" \
  -H "Content-Type: application/json" \
  -d "{\"prompt\": \"5 Productivity Tips headline slide. $CORE_PROMPT\", \"image_size\": \"square_hd\"}" \
  --output slide1.json

# Slide 2-N: Keep same style prompt, change content
```

---

## Flyer Design

### Recommended Models

| Priority | Model | Why |
|----------|-------|-----|
| **1st Choice** | FLUX.2 [pro] | Maximum detail, print quality |
| **2nd Choice** | Nano Banana Pro | Text for event info |

### High-Resolution Generation

```bash
# For print (300 DPI A4 = 2480×3508px)
curl -X POST "https://queue.fal.run/fal-ai/flux-pro/v1.1" \
  -H "Authorization: Key $FAL_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "prompt": "Event flyer for tech conference AI Summit 2026. Main visual: futuristic cityscape. Modern tech aesthetic, blue purple gradient.",
    "width": 2480,
    "height": 3508,
    "num_inference_steps": 40
  }' \
  --output flyer.json

curl -o "flyer-a4.png" "$(cat flyer.json | jq -r '.images[0].url')"
```

---

## Brand Asset Generation

### Recommended Models

| Asset Type | Model | Endpoint |
|------------|-------|----------|
| **Logos** | Recraft V4 | `fal-ai/recraft-v4` |
| **Icons** | Recraft V4 SVG | `fal-ai/recraft-v4` |
| **Wordmarks** | Ideogram | Use MCP to discover |

### Logo Generation

```bash
curl -X POST "https://queue.fal.run/fal-ai/recraft-v4" \
  -H "Authorization: Key $FAL_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "prompt": "GreenTech Solutions logo, minimalist leaf with circuit pattern, forest green #2C5F2D, tech-meets-nature aesthetic, vector style",
    "image_size": "square_hd"
  }' \
  --output logo.json

curl -o "logo.png" "$(cat logo.json | jq -r '.images[0].url')"
```

---

## Image Editing

### Models

| Task | Model | Endpoint |
|------|-------|----------|
| **Background removal** | Bria RMBG | `fal-ai/bria/rmbg` |
| **Outpainting** | FLUX Kontext | `fal-ai/flux-context` |
| **Upscaling** | SeedVR | `fal-ai/seedvr-upscale` |

### Background Removal

```bash
curl -X POST "https://queue.fal.run/fal-ai/bria/rmbg" \
  -H "Authorization: Key $FAL_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "image_url": "https://example.com/input.jpg"
  }' \
  --output removed.json

curl -o "no-bg.png" "$(cat removed.json | jq -r '.image.url')"
```

---

## Image Size Options

### Preset Sizes

| Preset | Dimensions | Aspect Ratio |
|--------|------------|--------------|
| `square_hd` | 1024×1024 | 1:1 |
| `square` | 512×512 | 1:1 |
| `portrait_4_3` | 768×1024 | 4:3 |
| `portrait_16_9` | 576×1024 | 16:9 |
| `landscape_4_3` | 1024×768 | 4:3 |
| `landscape_16_9` | 1024×576 | 16:9 |
| `portrait_4_5` | 864×1080 | 4:5 (Instagram) |
| `portrait_9_16` | 1080×1920 | 9:16 (Stories) |

### Custom Dimensions

```bash
"width": 1080,
"height": 1350
```

---

## Pricing Reference (2026)

| Model | Cost per Image | Speed |
|-------|---------------|-------|
| FLUX.1 [schnell] | $0.003-0.01 | ~2s |
| FLUX.1 [dev] | $0.02-0.04 | ~5s |
| FLUX.2 [pro] | $0.04-0.08 | ~10s |
| FLUX.2 [flex] | $0.02-0.05 | ~5s |
| Nano Banana Pro | $0.02-0.05 | ~5s |
| FLUX Kontext | $0.05-0.10 | ~8s |

*Check current pricing with MCP `get_pricing` tool.*

---

## Download to Workspace

**Always download generated images to the workspace:**

```bash
# Save to creative-suites
OUTPUT_DIR=".pawbytes/creative-suites/brands/{brand}/assets/{campaign}/social"
mkdir -p "$OUTPUT_DIR"

# Download with timestamp
TIMESTAMP=$(date +%Y%m%d_%H%M%S)
curl -o "$OUTPUT_DIR/post_$TIMESTAMP.png" "$IMAGE_URL"

echo "Saved: $OUTPUT_DIR/post_$TIMESTAMP.png"
```

---

## MCP Tools Reference

When you need to discover models or check schemas, use MCP:

| Tool | Purpose |
|------|---------|
| `search_models` | Find models by capability |
| `get_model_schema` | Get parameters for a model |
| `get_pricing` | Check current pricing |
| `search_docs` | Search fal.ai documentation |
| `recommend_model` | Get model recommendation for use case |
| `upload_file` | Upload image for editing |

**Example:** "Use fal.ai MCP to find the best model for logo generation" → Agent will use `search_models` and `recommend_model`.

---

## Best Practices

1. **Discovery via MCP** — Let AI help you find the right model and parameters
2. **Generation via CLI** — Faster, more reliable for long-running jobs
3. **Always download** — Save images to workspace, don't just return URLs
4. **Batch similar requests** — Use same session for consistency
5. **Cache good prompts** — Store prompts that produce desired results
6. **Use appropriate steps** — Higher steps for pro, lower for schnell