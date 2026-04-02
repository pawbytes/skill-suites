# Video Clipping

## Outcome

Extract the most engaging moments from long-form video content and repackage them as platform-ready short clips -- with smart reframing, subtitles, and platform-specific formatting.

## Trigger

User requests to clip a video, extract highlights, create clips from a long video, repurpose content, or find viral moments.

## Inputs Required

| Input | Source | Required |
|-------|--------|----------|
| Source video file | User provided | Yes |
| Target platform(s) | User specification | Yes |
| Target clip duration | User preference (default: 30-60s) | Optional |
| Number of clips | User preference (default: 3-5) | Optional |

## Process

### 1. Source Analysis

Analyze the source video to identify clippable moments:

**With OpenShorts (if available):**
- Run viral moment detection for AI-scored engagement predictions
- Use smart reframing for automatic horizontal-to-vertical conversion
- Extract ranked clip suggestions

**Without OpenShorts (ffmpeg fallback):**
- Analyze audio levels to detect speech segments and energy peaks
- Use scene detection (`ffprobe` scene change analysis) to find natural cut points
- Manually identify segments based on transcript or user direction

### 2. Clip Extraction

For each identified clip:
- Extract segment from source with precise timestamps
- Maintain original quality (no re-encoding during extraction when possible)
- Preserve original audio

### 3. Reframing (if needed)

When converting horizontal (16:9) to vertical (9:16):
- Center-crop with subject tracking where possible
- Add branded bars if letterboxing is preferred
- Ensure no critical content is cut off

### 4. Subtitle & Polish

Each clip gets:
- Burned-in subtitles matching the short-form style (see `./subtitle-burnin.md`)
- Brand watermark or logo overlay (if specified)
- Clean in/out points (no mid-sentence cuts)

### 5. Multi-Platform Export

Encode each clip for every target platform:

| Platform | Resolution | Codec | Max Duration |
|----------|-----------|-------|-------------|
| TikTok | 1080x1920 | H.264 | 180s |
| Instagram Reels | 1080x1920 | H.264 | 90s |
| YouTube Shorts | 1080x1920 | H.264 | 60s |
| X (Twitter) | 1080x1920 | H.264 | 140s |

## Output

**Location:** `.pawbytes/creative-suites/brands/{brand}/videos/{campaign}/clips/`
**Structure:**
```
clips/
  clip_01_{slug}/
    tiktok.mp4
    reels.mp4
    shorts.mp4
  clip_02_{slug}/
    ...
  clip-manifest.json
```
**Manifest:** `clip-manifest.json` listing all clips with source timestamps, platforms, and file paths.

## Escalation

If source video quality is poor (low resolution, heavy compression), inform user of quality limitations before proceeding. If content selection is ambiguous, present top clip candidates with timestamps for user approval before full processing.
