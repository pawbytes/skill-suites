# paw-cra-video-longform

## Overview

Long-form and episodic video production pipeline for YouTube and web platforms. Produces finished videos (1-10 minutes, 1920x1080 horizontal) with full production pipeline including script development, multi-scene generation, voiceover synthesis, B-roll integration, and branded intro/outro.

## What It Does

| Capability | Description |
|------------|-------------|
| Horizontal video | 16:9 aspect ratio at 1920x1080 resolution |
| AI scene generation | Veo 3.1 for cinematic, Kling v3 for motion-heavy |
| Voiceover synthesis | ElevenLabs with timing alignment |
| B-roll integration | Pexels stock footage for supplementary shots |
| Multi-scene assembly | ffmpeg with transitions (cut, crossfade, xfade) |
| Episodic series | Consistent style across multiple episodes |
| Branded elements | Intro/outro, lower thirds, watermarks |

## When to Use It

- You need a YouTube video (1-10 minutes)
- You want an episodic video series
- You need web-embeddable video content
- You have a script or need script development
- You want professional multi-scene production

## Trigger Phrases

- "long-form video"
- "YouTube video"
- "episodic video"
- "video series"
- "create a 5-minute video"

## What You Get (Deliverables)

| Output | Location |
|--------|----------|
| MP4 video (1920x1080) | `.pawbytes/creative-suites/brands/{brand}/videos/{video-slug}/` |
| video-manifest.json | Same folder |
| scene-plan.json | Same folder |
| subtitles.srt | Same folder |
| thumbnail.jpg | Same folder |

## Tool Dependencies

| Tool | Purpose | Required |
|------|---------|----------|
| ffmpeg | Assembly, transitions, audio, subtitles | Yes |
| egaki CLI | AI video scene generation | Yes (or fal.ai direct) |
| fal.ai API | Veo 3.1, Kling v3 generation | Yes |
| ElevenLabs API | Voiceover generation | Yes |
| Pexels API | B-roll stock footage | Recommended |
| Remotion | Programmatic video | Optional |

## Production Pipeline

**Stages 1-4: Pre-Production**
1. Brief intake (topic, duration, format, platform, brand, tone)
2. Script development (invoke Strategist if needed)
3. Scene planning (10-30+ scenes with visual direction)
4. Brand context (colors, logos, typography, voice)

**Stages 5-9: Production**
5. Scene generation (AI, stock, or motion graphics)
6. Voiceover generation with timing alignment
7. B-roll integration from Pexels
8. Assembly with transitions and audio mixing
9. Subtitle generation and burn-in

**Stages 10-14: Finishing**
10. Intro/outro addition
11. Validation (resolution, codec, audio levels)
12. Export with manifest
13. Episodic mode (repeat for each episode)
14. Status update

## Quick Example

**Input**: "Create a 5-minute YouTube video about 'Morning Routines' for brand 'WellnessCo', educational tone, 3 episodes"

**Output** (per episode):
- `wellnessco-morning-routines-ep01.mp4`
- `video-manifest.json`
- `scene-plan.json`
- `subtitles.srt`
- `thumbnail.jpg`

## Related Skills

- [paw-cra-video-shortform](./paw-cra-video-shortform.md) - TikTok/Reels/Shorts
- [paw-cra-video-clips](./paw-cra-video-clips.md) - Clip extraction and repurposing
- [paw-cra-agent-strategist](./paw-cra-agent-strategist.md) - Script development