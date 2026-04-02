# Motion Graphics

## Outcome

Produce animated graphics -- intros, outros, title cards, data visualizations, and animated brand elements -- as standalone assets or components for larger video projects.

## Trigger

User requests motion graphics, animated intro, animated logo, kinetic typography, or animated graphics for video.

## Inputs Required

| Input | Source | Required |
|-------|--------|----------|
| Concept or description | User input or brief | Yes |
| Brand guidelines | Shared memory | Yes |
| Duration | User specification (default: 5s) | Optional |
| Output format | User preference (MP4 or MOV) | Optional |

## Process

### 1. Approach Selection

Choose the best tool for the motion graphics type:

| Type | Recommended Tool | Why |
|------|-----------------|-----|
| **Logo animation** | Remotion or fal.ai (image-to-video) | Precise control over brand elements |
| **Title cards** | Remotion (React components) | Exact typography and layout control |
| **Data visualization** | Remotion | Programmatic animation of numbers/charts |
| **Kinetic typography** | Remotion | Word-by-word animation with precise timing |
| **Abstract/cinematic** | fal.ai (Veo 3.1) | AI excels at organic, cinematic motion |
| **Transitions** | ffmpeg xfade filters | Built-in transition library |

### 2. Creation

**For Remotion-based motion graphics:**
- Build React component with animation sequences
- Render via Remotion CLI at target resolution
- Export with alpha channel if needed (MOV ProRes 4444)

**For AI-generated motion graphics:**
- Use image-to-video to animate static brand assets
- Specify motion direction and style in prompt
- Generate multiple takes and select best

**For ffmpeg-based elements:**
- Use filter graphs for text animations, overlays, transitions
- Combine static assets with motion using overlay and fade filters

### 3. Quality Check

- Smooth animation at target framerate (30fps minimum)
- Brand colors exact throughout
- No motion artifacts or jitter
- Clean alpha channel (if transparency needed)
- Loopable if intended for repeated use

## Output

**Format:** MP4 (H.264) for standard use, MOV (ProRes 4444) for alpha channel
**Location:** `.pawbytes/creative-suites/brands/{brand}/videos/motion-graphics/`
**Naming:** `{type}_{description-slug}_{date}.{ext}`
