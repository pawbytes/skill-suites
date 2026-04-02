# paw-cra-agent-video-producer

## Overview

The Video Producer is a technical video production specialist who orchestrates the full video pipeline -- from AI generation through voiceover, assembly, subtitles, and final encoding. Produces platform-ready video files for short-form, long-form, episodic, and motion graphics content.

## What It Does

| Capability | Description |
|------------|-------------|
| Short-Form Video | TikTok, Reels, Shorts (1080x1920 vertical) |
| Long-Form Video | YouTube, web (1920x1080 horizontal) |
| Episodic Series | Multi-episode video series with consistent branding |
| Motion Graphics | Animated graphics, overlays, transitions |
| Video Clipping | Clip extraction and repurposing |
| Voiceover Generation | AI voiceover via ElevenLabs |
| Subtitle Burn-in | Word-level highlighted subtitles |
| Video Assembly | Scene assembly, transitions, encoding |

## When to Use It

- Creating TikTok, Reels, or YouTube Shorts
- Producing YouTube videos or web content
- Adding AI voiceover to videos
- Burning subtitles into existing videos
- Extracting clips from longer content
- Creating motion graphics or animations

## Trigger Phrases

- "Create a video for..."
- "Make a Reel about..."
- "TikTok video for..."
- "YouTube video for..."
- "Add subtitles to..."
- "Generate voiceover for..."
- "Clip this video..."

## What You Get (Deliverables)

| Output | Location |
|--------|----------|
| Production-ready MP4 | `.pawbytes/creative-suites/brands/{brand}/campaigns/{campaign}/` |
| Video manifest | `video-manifest.json` in campaign folder |

## Arguments

| Arg | Description |
|-----|-------------|
| `--headless` or `-H` | Non-interactive execution |

## AI Video Models (2026)

| Model | Best For | Duration |
|-------|----------|----------|
| Veo 3.1 | Cinematic quality, complex scenes | 5-17s per clip |
| Kling v3 Standard | Fast iteration, social content | 5-10s per clip |
| Kling v3 Pro | High quality, precise motion | 5-10s per clip |
| Kling Image-to-Video | Animating stills, brand assets | 5-10s per clip |

## Tool Dependencies

| Tool | Purpose | Required |
|------|---------|----------|
| ffmpeg | Assembly, encoding, subtitles | Yes |
| fal.ai API | AI video generation | Yes |
| egaki CLI | Multi-provider video generation | Optional |
| ElevenLabs API | AI voiceover | Optional |
| Remotion | Programmatic React-based video | Optional |

## Platform Specifications

| Platform | Resolution | Aspect | Duration | Codec |
|----------|------------|--------|----------|-------|
| TikTok | 1080x1920 | 9:16 | 15-180s | H.264 |
| Instagram Reels | 1080x1920 | 9:16 | 15-90s | H.264 |
| YouTube Shorts | 1080x1920 | 9:16 | 15-60s | H.264 |
| YouTube | 1920x1080 | 16:9 | No limit | H.264/H.265 |
| LinkedIn Video | 1920x1080 | 16:9 | 3s-10min | H.264 |

## Quick Example

**Input**: "Create a 30-second TikTok about our new product, energetic style with subtitles"

**Output**: Production-ready 1080x1920 MP4 at 30fps with 6 scenes, 0.5s crossfades, word-level highlight subtitles at bottom third, H.264 main profile at 8Mbps, plus `video-manifest.json` with codec, resolution, duration, and subtitle status.

## Companion Workflows

| Workflow | Purpose |
|----------|---------|
| `paw-cra-video-shortform` | Short-form vertical pipeline |
| `paw-cra-video-longform` | Long-form horizontal pipeline |
| `paw-cra-video-clips` | Clip extraction and repurposing |

## Related Skills

- [paw-cra-agent-creative-director](./paw-cra-agent-creative-director.md) -- Orchestrator
- [paw-cra-agent-designer](./paw-cra-agent-designer.md) -- Visual assets
- [paw-cra-campaign-orchestration](./paw-cra-campaign-orchestration.md) -- Multi-deliverable campaigns
- [paw-cra-quality-control](./paw-cra-quality-control.md) -- Campaign-level QC