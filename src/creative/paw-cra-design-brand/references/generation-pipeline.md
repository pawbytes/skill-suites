# Generation Pipeline

fal.ai CLI commands, async generation patterns, and download workflow. Loaded during Step 4 of the pipeline.

## Environment

```bash
# API key from config
export FAL_KEY="$fal_key"
```

## Sync Generation (Wait for Result)

For fast models (Recraft V4, FLUX Schnell) or when latency is acceptable:

```bash
curl -X POST "https://queue.fal.run/{MODEL_ENDPOINT}" \
  -H "Authorization: Key $FAL_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "prompt": "{generation_prompt}",
    "image_size": "{size_preset_or_custom}"
  }' \
  --output result.json

# Extract and download
IMAGE_URL=$(cat result.json | jq -r '.images[0].url')
curl -o "{output_path}" "$IMAGE_URL"
```

## Async Generation (Submit & Poll)

For slow models (FLUX.2 Pro at high resolution, print-quality flyers):

```bash
# 1. Submit job
REQUEST_ID=$(curl -s -X POST "https://queue.fal.run/{MODEL_ENDPOINT}/requests" \
  -H "Authorization: Key $FAL_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "prompt": "{generation_prompt}",
    "width": {width},
    "height": {height},
    "num_inference_steps": {steps}
  }' | jq -r '.request_id')

# 2. Poll for completion
STATUS="IN_PROGRESS"
while [ "$STATUS" != "COMPLETED" ]; do
  sleep 3
  RESPONSE=$(curl -s "https://queue.fal.run/{MODEL_ENDPOINT}/requests/$REQUEST_ID/status" \
    -H "Authorization: Key $FAL_KEY")
  STATUS=$(echo "$RESPONSE" | jq -r '.status')
done

# 3. Get result and download
RESULT=$(curl -s "https://queue.fal.run/{MODEL_ENDPOINT}/requests/$REQUEST_ID" \
  -H "Authorization: Key $FAL_KEY")
IMAGE_URL=$(echo "$RESULT" | jq -r '.images[0].url')
curl -o "{output_path}" "$IMAGE_URL"
```

## Model Endpoints

| Model | Endpoint | Typical Latency |
|-------|----------|-----------------|
| Recraft V4 Pro | `fal-ai/recraft-v4` | ~5-10s |
| FLUX.2 Pro | `fal-ai/flux-pro/v1.1` | ~10-20s |
| FLUX.2 Flex | `fal-ai/flux/dev` | ~5-8s |
| FLUX.1 Schnell | `fal-ai/flux/schnell` | ~2-4s |
| Nano Banana Pro | `fal-ai/nano-banana-pro` | ~5-8s |

**Ideogram V3:** Use fal.ai MCP `search_models` to discover the current endpoint, as it may be listed under a different provider path. Fall back to Recraft V4 for wordmarks if Ideogram is unavailable.

## Model-Specific Parameters

### Recraft V4 Pro (Logos/Icons)

```json
{
  "prompt": "...",
  "image_size": "square_hd"
}
```

Best results with: clear subject descriptions, "vector style", brand colors as hex values in prompt, "transparent background".

### FLUX.2 Pro (Flyer Backgrounds/Banners)

```json
{
  "prompt": "...",
  "width": 2480,
  "height": 3508,
  "num_inference_steps": 28
}
```

Use `num_inference_steps: 28-40` for print quality. Higher steps = more detail but slower. Use custom width/height for print dimensions instead of presets.

### Image Size Presets

| Preset | Dimensions | Use For |
|--------|------------|---------|
| `square_hd` | 1024x1024 | Logos, icons, avatars |
| `portrait_4_5` | 864x1080 | Instagram-format banners |
| `landscape_16_9` | 1024x576 | Web banners |
| `portrait_9_16` | 1080x1920 | Story-format banners |

## Download and File Management

Always download to the WIP directory first, then move to final location after validation:

```bash
# WIP directory for in-progress generation
WIP_DIR="{project-root}/.pawbytes/creative-suites/brands/{brand}/assets/wip"
mkdir -p "$WIP_DIR"

# Download with descriptive name
TIMESTAMP=$(date +%Y%m%d_%H%M%S)
curl -o "$WIP_DIR/{asset_type}_v{variation}_{TIMESTAMP}.png" "$IMAGE_URL"
```

After brand validation passes, move from `wip/` to the appropriate final subdirectory (`brand-identity/logo/`, `flyers/`, `banners/`, `avatars/`).

## Multi-Variation Generation

For interactive mode, generate variations by modifying prompt emphasis:

```bash
# Core prompt stays the same, style emphasis shifts
PROMPTS=(
  "Core interpretation: {base_prompt}"
  "Stylized take: {base_prompt}, more artistic, creative interpretation"
  "Minimal take: {base_prompt}, ultra-minimalist, essential elements only"
)

for i in "${!PROMPTS[@]}"; do
  curl -X POST "https://queue.fal.run/{MODEL}" \
    -H "Authorization: Key $FAL_KEY" \
    -H "Content-Type: application/json" \
    -d "{\"prompt\": \"${PROMPTS[$i]}\", \"image_size\": \"square_hd\"}" \
    --output "variation_$((i+1)).json"
done
```

## Error Handling

- **API key missing:** Abort with clear message -- generation requires `fal_key` in config
- **Rate limit:** Wait 10 seconds and retry once, then report failure
- **Generation failure:** Log the error, try once more with simplified prompt
- **Download failure:** Retry download up to 3 times with 2-second intervals
- **Invalid response:** Check if `.images[0].url` exists in response; if not, log full response for debugging
