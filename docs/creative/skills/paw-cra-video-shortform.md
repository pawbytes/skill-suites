# paw-cra-video-shortform

## Overview

Short-form vertical video production pipeline for TikTok, Instagram Reels, and YouTube Shorts. Takes a brief or script and outputs finished MP4 files (1080x1920, H.264) with burned-in subtitles and platform-compliant encoding.

## What It Does

| Capability | Description |
|------------|-------------|
| Vertical video | 9:16 aspect ratio at 1080x1920 resolution |
| AI scene generation | Veo 3.1 or Kling v3 via fal.ai API |
| Voiceover synthesis | ElevenLabs integration for narration |
| Subtitle burn-in | Styled, safe-zone positioned subtitles |
| Assembly | ffmpeg concatenation with xfade transitions |
| Platform validation | Duration, resolution, codec, file size checks |

## When to Use It

- You need a TikTok video (up to 60 seconds)
- You want an Instagram Reel (up to 90 seconds)
- You need a YouTube Short (up to 60 seconds)
- You have a brief or script ready for production
- You need upload-ready vertical video

## Trigger Phrases

- "create short video"
- "make a Reel"
- "TikTok video"
- "short-form video"
- "create a Short"

## What You Get (Deliverables)

| Output | Location |
|--------|----------|
| MP4 video (1080x1920) | `.pawbytes/creative-suites/brands/{brand}/videos/` |
| video-manifest.json | Same folder |
| subtitles.srt | Same folder |

## Platform Specifications

| Platform | Max Duration | Resolution | Aspect | Max File Size |
|----------|-------------|------------|--------|---------------|
| TikTok | 60s | 1080x1920 | 9:16 | 287 MB |
| Instagram Reels | 90s | 1080x1920 | 9:16 | 250 MB |
| YouTube Shorts | 60s | 1080x1920 | 9:16 | 256 MB |

## Tool Dependencies

| Tool | Purpose | Required |
|------|---------|----------|
| egaki CLI | Multi-provider AI video generation | Yes |
| fal.ai API | Veo 3.1, Kling v3 generation | Yes |
| ffmpeg | Assembly, transitions, encoding | Yes |
| ElevenLabs API | AI voiceover | Optional |

## Pipeline Phases

**Phase 1: Pre-Production**
- Brief intake and parsing
- Script check (use provided or invoke Strategist)
- Storyboard planning (3-8 scenes)
- Brand context loading

**Phase 2: Production**
- AI scene generation via egaki/fal.ai
- Voiceover via ElevenLabs (if needed)
- ffmpeg assembly with transitions
- Subtitle generation and burn-in

**Phase 3: Validation & Export**
- Codec validation (1080x1920, H.264)
- Export with manifest
- Status update to logs

## Quick Example

**Input**: "Create a 45-second TikTok for 'EcoBottle' brand about sustainability, upbeat tone, call to action at end"

**Output**:
- `ecobottle_tiktok_2026-04-02.mp4` (1080x1920, H.264)
- `video-manifest.json`
- `subtitles.srt`

## Related Skills

- [paw-cra-video-longform](./paw-cra-video-longform.md) - YouTube/web videos (1-10 min)
- [paw-cra-video-clips](./paw-cra-video-clips.md) - Clip extraction from long-form
- [paw-cra-multi-platform-export](./paw-cra-multi-platform-export.md) - Export for all platforms