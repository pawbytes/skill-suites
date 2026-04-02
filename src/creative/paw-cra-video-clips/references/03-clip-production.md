---
name: 03-clip-production
description: Extract clips, reframe, add subtitles, brand overlays, and encode for platforms
---

# Steps 3-7: Clip Production Pipeline

## Outcome

For each approved moment, produce platform-ready clip files: extracted, reframed (if vertical), subtitled, branded, and encoded to platform specs.

## Step 3: Clip Extraction

Extract each candidate clip from the source video:

```bash
ffmpeg -ss {start_time} -i "{source}" -t {duration} -c copy -avoid_negative_ts make_zero "{output_dir}/{clip_id}_raw.mp4"
```

Use `-c copy` for fast extraction when the source codec is compatible. Fall back to re-encoding if the cut points are not on keyframes (visible as artifacts at clip start):

```bash
ffmpeg -ss {start_time} -i "{source}" -t {duration} -c:v libx264 -crf 18 -preset fast -c:a aac -b:a 192k "{output_dir}/{clip_id}_raw.mp4"
```

For each target duration (15s, 30s, 60s), trim the moment to fit. If the moment is longer than the target, select the strongest subsegment. If shorter, use the natural duration.

## Step 4: Smart Reframing

For vertical platforms (TikTok, Instagram Reels, YouTube Shorts), reframe horizontal clips to 9:16.

**Priority: speaker/action focus, not blind center-crop.**

### If OpenShorts is available:
Use its AI reframe feature for speaker-tracking crop.

### ffmpeg reframing (default):

Detect the primary region of interest and crop accordingly. For talking-head content, center on the speaker. For action content, follow the motion.

Basic center crop (fallback):
```bash
ffmpeg -i "{clip_id}_raw.mp4" -vf "crop=ih*9/16:ih:(iw-ih*9/16)/2:0,scale=1080:1920" -c:v libx264 -crf 20 -preset medium -c:a copy "{clip_id}_vertical.mp4"
```

For better results, use cropdetect or manual offset based on content analysis:
- **Talking head** -- crop centered on the speaker (usually center or slightly off-center)
- **Two speakers** -- alternate focus or use a wider crop that includes both
- **Presentation/demo** -- keep the screen content visible, crop speaker area

Name each reframed clip with platform suffix: `{clip_id}_tiktok.mp4`, `{clip_id}_reels.mp4`, etc.

## Step 5: Subtitle Generation

Generate subtitles for every clip. Subtitles are non-negotiable -- they increase engagement 40%+ and are required for accessibility.

### Generate SRT

If no transcript exists, generate one:

```bash
ffmpeg -i "{clip_file}" -ar 16000 -ac 1 -f wav - | whisper --model small --output_format srt --output_dir "{output_dir}" -
```

If whisper is not available, use any available speech-to-text tool. As a last resort, provide a placeholder SRT and flag for manual review.

### Burn-in subtitles

Platform-appropriate subtitle styling:

| Platform | Style | Font Size | Position |
|----------|-------|-----------|----------|
| TikTok / Reels / Shorts | Bold, centered, word-by-word highlight | 48-56px | Center-bottom (above UI safe zone) |
| YouTube | Standard lower-third | 36-42px | Bottom 15% |
| LinkedIn / Facebook | Clean, readable | 32-40px | Bottom 10% |

Burn subtitles using ffmpeg ASS/SRT filter:

```bash
ffmpeg -i "{clip_file}" -vf "subtitles={srt_file}:force_style='FontSize=24,FontName=Arial Bold,PrimaryColour=&H00FFFFFF,OutlineColour=&H00000000,Outline=2,Alignment=2,MarginV=60'" -c:v libx264 -crf 20 -preset medium -c:a copy "{clip_id}_subtitled.mp4"
```

Adjust `MarginV` and `FontSize` per platform specs above.

## Step 6: Brand Overlay

Apply brand elements per brand guidelines. Skip if no brand context is loaded.

| Asset | Application | ffmpeg approach |
|-------|-------------|-----------------|
| **Intro bumper** | Prepend 2-3s branded intro | `ffmpeg -i intro.mp4 -i clip.mp4 -filter_complex "[0:v][0:a][1:v][1:a]concat=n=2:v=1:a=1"` |
| **End card** | Append 2-3s branded outro | Same concat approach |
| **Watermark** | Semi-transparent logo overlay | `overlay=W-w-20:H-h-20` filter with opacity |
| **Lower third** | Brand name/handle bar | Overlay with fade-in/out |

Watermark positioning by platform:
- **TikTok** -- top-left (bottom-right obscured by UI)
- **YouTube** -- bottom-right (standard)
- **Reels** -- top-left (bottom obscured by UI)

## Step 7: Platform-Specific Encoding

Load `./references/video-platform-specs.md` for exact encoding parameters.

Encode each clip to its target platform's specifications. Every clip gets a platform-specific encode even if the source matches -- this guarantees spec compliance.

The encoding step produces the final deliverable files. Name them clearly:

```
{clip_id}_{platform}_{duration}s.mp4
```

Example: `M01_tiktok_30s.mp4`, `M03_youtube_60s.mp4`

## Progression

Proceed to `./references/04-manifest-and-review.md` when all clips are encoded.
