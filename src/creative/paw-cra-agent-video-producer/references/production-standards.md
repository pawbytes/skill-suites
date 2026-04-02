# Production Standards

## Overview

Quality standards and validation rules for every video produced. These apply regardless of video type, platform, or production method.

## Encoding Standards

### H.264 Encoding Profiles

| Content Type | Profile | Level | Bitrate | Notes |
|-------------|---------|-------|---------|-------|
| Short-form (1080x1920) | Main | 4.0 | 6-10 Mbps | Maximum compatibility |
| Long-form (1920x1080) | High | 4.1 | 10-16 Mbps | Better compression at quality |
| 4K (3840x2160) | High | 5.1 | 35-45 Mbps | YouTube/Vimeo 4K |

### Audio Standards

| Parameter | Standard | Notes |
|-----------|----------|-------|
| **Codec** | AAC | Universal compatibility |
| **Loudness** | -14 LUFS integrated | Broadcast/streaming standard |
| **True peak** | -1.0 dBTP | Prevent clipping |
| **Sample rate** | 44.1kHz or 48kHz | 48kHz preferred for YouTube |
| **Bitrate** | 128-256 kbps | 256 for long-form, 128 for short |

### Container Settings

- **Format:** MP4 (MPEG-4 Part 14)
- **Moov atom:** Always use `-movflags +faststart` for web streaming
- **Metadata:** Include title, artist, description tags

## Subtitle Standards

### Universal Rules

- Every shipped video includes burned-in subtitles
- Subtitle text must be readable at target viewing size (phone for short-form, desktop for long-form)
- No subtitle segment longer than 7 seconds
- No more than 2 lines displayed simultaneously
- Subtitle background must provide sufficient contrast against any video content behind it

### Platform-Specific Placement

| Platform | Subtitle Y Position | Reason |
|----------|-------------------|--------|
| TikTok | 60-75% from top | Below UI overlay area |
| Instagram Reels | 60-75% from top | Below UI overlay area |
| YouTube Shorts | 60-75% from top | Below UI overlay area |
| YouTube | 85-90% from top | Standard TV subtitle zone |
| LinkedIn | 85-90% from top | Standard TV subtitle zone |

## Audio Mixing Standards

### Level Hierarchy

| Track | Level (LUFS) | Priority |
|-------|-------------|----------|
| Voiceover | -14 | Highest -- always audible |
| Dialogue | -14 | Same as voiceover |
| Music (under speech) | -26 to -30 | Duck significantly under VO |
| Music (no speech) | -16 to -20 | Full presence during non-speech |
| Sound effects | -18 to -22 | Accent, never dominate |
| Ambient | -30 to -36 | Subtle background layer |

### Music Ducking

When voiceover or dialogue is present:
- Reduce music by 12-18 dB
- Apply ducking 0.3s before speech starts
- Release ducking 0.5s after speech ends
- Use smooth exponential curve for natural fade

## Transition Guidelines

| Transition | Duration | Use Case |
|-----------|----------|----------|
| Hard cut | 0 frames | Fast-paced, energetic, information-dense |
| Crossfade | 0.3-0.5s | Standard scene change |
| Dissolve | 0.5-1.0s | Emotional, contemplative transitions |
| Fade to black | 0.5-1.0s | Section breaks, act breaks |
| Wipe (directional) | 0.3-0.5s | Energetic, tutorial, before/after |
| Zoom | 0.3s | Dynamic, modern social content |

**Short-form default:** Hard cut or 0.3s crossfade
**Long-form default:** 0.5s crossfade between scenes, fade to black between sections

## Video Manifest Schema

Every production run writes a `video-manifest.json`:

```json
{
  "version": "1.0",
  "produced_at": "2026-04-01T12:00:00Z",
  "brand": "{brand-name}",
  "campaign": "{campaign-name}",
  "videos": [
    {
      "file": "tiktok_summer-sale_2026-04-01.mp4",
      "platform": "tiktok",
      "type": "short-form",
      "resolution": "1080x1920",
      "aspect_ratio": "9:16",
      "codec": "H.264",
      "duration_seconds": 45,
      "fps": 30,
      "bitrate_mbps": 8,
      "audio_codec": "AAC",
      "audio_bitrate_kbps": 128,
      "subtitles": true,
      "subtitle_style": "word-highlight",
      "voiceover": true,
      "file_size_mb": 12.4,
      "status": "pass"
    }
  ],
  "validation": {
    "all_specs_met": true,
    "subtitles_present": true,
    "audio_normalized": true,
    "issues": []
  }
}
```

## Pre-Delivery Checklist

Before marking any video as complete:

- [ ] **Resolution** matches target platform exactly
- [ ] **Aspect ratio** is correct (9:16 for vertical, 16:9 for horizontal)
- [ ] **Duration** is within platform limits
- [ ] **Codec** is H.264 (Main or High profile)
- [ ] **Subtitles** are burned in, readable, and synced
- [ ] **Audio** is normalized to -14 LUFS
- [ ] **No black frames** at start or end
- [ ] **No encoding artifacts** (blocking, banding, dropped frames)
- [ ] **Brand consistency** -- colors, style, typography match guidelines
- [ ] **Moov atom** is at start of file (faststart)
- [ ] **Manifest written** with accurate metadata
- [ ] **File size** is within platform limits
