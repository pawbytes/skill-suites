# Scene Generation

## Purpose

Generate or acquire video clips for each scene defined in the scene plan. Choose the right tool and model for each scene's requirements.

## AI Video Generation

### Model Selection

| Model | Best For | Duration | Quality |
|-------|----------|----------|---------|
| **Veo 3.1** (fal.ai) | Cinematic quality, complex scenes, realistic humans | Up to 8s per clip | Highest |
| **Kling v3 Standard** (fal.ai) | Good quality, faster generation, motion-heavy | Up to 10s per clip | High |
| **Kling v3 Pro** (fal.ai) | Premium quality with longer coherent motion | Up to 10s per clip | Highest |

### Generation via egaki CLI

```bash
# Text-to-video with Veo 3.1
egaki video --provider fal --model veo-3.1 \
  --prompt "Scene description here" \
  --aspect-ratio 16:9 \
  --duration 8 \
  --output scene_01.mp4

# Image-to-video (use a generated still as first frame)
egaki video --provider fal --model kling-v3 \
  --image first_frame.png \
  --prompt "Camera slowly pans right revealing..." \
  --aspect-ratio 16:9 \
  --output scene_01.mp4
```

### Generation via fal.ai API (curl)

Use direct API calls when egaki CLI is unavailable or for batch submission:

```bash
# Submit generation job
curl -X POST "https://queue.fal.run/fal-ai/veo-3" \
  -H "Authorization: Key ${FAL_KEY}" \
  -H "Content-Type: application/json" \
  -d '{
    "prompt": "Scene description",
    "aspect_ratio": "16:9",
    "duration": "8s"
  }'

# Poll for result
curl "https://queue.fal.run/fal-ai/veo-3/requests/{request_id}/status" \
  -H "Authorization: Key ${FAL_KEY}"
```

### Prompting for Video Generation

Effective video prompts include:
1. **Subject:** What is in the scene (person, object, environment)
2. **Action:** What is happening (walking, rotating, assembling)
3. **Camera:** How the camera moves (static, pan left, dolly in, aerial tracking)
4. **Mood/lighting:** Atmosphere (warm golden hour, cool blue office, dramatic shadows)
5. **Style:** Visual style (cinematic, documentary, corporate, stylized)

Example: "A software developer typing at a modern desk, warm ambient office lighting, shallow depth of field, camera slowly dollies in, cinematic color grading, 4K quality"

### Handling Generation Failures

AI video generation can fail or produce unusable results. For each scene:
1. Generate and review the output
2. If quality is insufficient, refine the prompt (add specificity, adjust style keywords)
3. If the scene is consistently problematic, fall back to stock footage
4. Track retries -- cap at 3 attempts per scene before falling back

## Stock Footage (Pexels API)

```bash
# Search for stock video
curl "https://api.pexels.com/videos/search?query=modern+office&per_page=5&size=large" \
  -H "Authorization: ${PEXELS_API_KEY}"
```

Download at minimum 1080p resolution. Trim to required duration with ffmpeg:

```bash
ffmpeg -i stock_clip.mp4 -ss 00:00:02 -t 8 -c copy trimmed_clip.mp4
```

## Scene Output

Save all generated/acquired clips to the working directory with consistent naming: `scene_01.mp4`, `scene_02.mp4`, etc. Update the scene plan with actual file paths and durations.
