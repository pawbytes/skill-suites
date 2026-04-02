# paw-cra-video-clips

## Overview

Video repurposing pipeline that extracts short, platform-ready clips from long-form content. Analyzes source video for high-value moments, extracts clips at target durations, reframes for vertical platforms, adds subtitles and brand overlays, and encodes for each platform's specifications.

## What It Does

| Capability | Description |
|------------|-------------|
| Moment detection | Identify high-value segments in source video |
| Clip extraction | Extract segments at target durations |
| Smart reframing | Focus on speaker/action, not blind center-crop |
| Subtitle burn-in | Styled subtitles positioned in safe zones |
| Brand overlays | Watermarks, intros, end cards per guidelines |
| Platform encoding | Codec, bitrate, resolution per platform |

## When to Use It

- You have long-form video to repurpose for social
- You need to extract highlights from a longer video
- You want TikTok/Reels clips from YouTube content
- You need to reframe horizontal video to vertical
- You want platform-ready clips without manual editing

## Trigger Phrases

- "extract clips"
- "repurpose video"
- "create clips from video"
- "clip video for social"
- "make clips from my YouTube video"

## What You Get (Deliverables)

| Output | Location |
|--------|----------|
| Clip MP4 files | `.pawbytes/creative-suites/brands/{brand}/videos/clips/` |
| clip-manifest.json | Same folder |

## Pipeline Stages

| Stage | Description |
|-------|-------------|
| Source Intake | Collect source video, target platforms, brand name |
| Analysis | Detect high-value moments, auto-detect in headless |
| Clip Production | Extract, reframe, subtitle, overlay, encode |
| Manifest & Review | Generate manifest, approve or auto-approve |
| Export | Save to brand folder, write daily log |

## Key Principles

- **Production-first** - Every clip must be immediately uploadable
- **Subtitles always** - Burned-in for accessibility and engagement
- **Brand consistency** - Watermarks, intros, end cards per guidelines
- **Smart reframing** - Focus on speaker/action, not blind center-crop
- **Manifest everything** - Track timestamps, source timecodes, platform, specs

## Tool Requirements

| Tool | Required | Purpose |
|------|----------|---------|
| ffmpeg | Yes | All video processing |
| ffprobe | Yes | Source video analysis |
| OpenShorts | No | Enhances moment detection (ffmpeg fallback) |
| fal.ai | No | Optional AI upscaling |

## Quick Example

**Input**: "Extract 5 clips from this 15-minute interview video for TikTok, brand is TechStart"

**Output**:
- `techstart_tiktok_clip_001.mp4` (1080x1920, 45s)
- `techstart_tiktok_clip_002.mp4` (1080x1920, 30s)
- `techstart_tiktok_clip_003.mp4` (1080x1920, 60s)
- `techstart_tiktok_clip_004.mp4` (1080x1920, 38s)
- `techstart_tiktok_clip_005.mp4` (1080x1920, 52s)
- `clip-manifest.json`

## Related Skills

- [paw-cra-video-shortform](./paw-cra-video-shortform.md) - Create new short-form videos
- [paw-cra-video-longform](./paw-cra-video-longform.md) - Long-form video production
- [paw-cra-multi-platform-export](./paw-cra-multi-platform-export.md) - Export variants for all platforms