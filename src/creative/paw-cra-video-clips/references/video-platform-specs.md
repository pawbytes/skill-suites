---
name: video-platform-specs
description: Authoritative encoding specifications for each video platform
---

# Video Platform Encoding Specifications

Use these exact specifications when encoding clips. Do not approximate -- platforms reject or re-compress uploads that deviate.

## Platform Specs

### TikTok

| Parameter | Value |
|-----------|-------|
| **Resolution** | 1080 x 1920 |
| **Aspect Ratio** | 9:16 |
| **Codec** | H.264 (AVC) |
| **Container** | MP4 |
| **Frame Rate** | 30 fps (24-60 accepted) |
| **Bitrate** | 6-10 Mbps |
| **Max File Size** | 287 MB (mobile), 500 MB (web) |
| **Max Duration** | 10 minutes |
| **Audio Codec** | AAC |
| **Audio Bitrate** | 128-192 kbps |
| **Audio Sample Rate** | 44100 Hz |

**ffmpeg encode:**
```bash
ffmpeg -i input.mp4 -vf "scale=1080:1920:force_original_aspect_ratio=decrease,pad=1080:1920:-1:-1" -c:v libx264 -profile:v high -level:v 4.1 -crf 20 -preset medium -r 30 -c:a aac -b:a 192k -ar 44100 -movflags +faststart output_tiktok.mp4
```

### Instagram Reels

| Parameter | Value |
|-----------|-------|
| **Resolution** | 1080 x 1920 |
| **Aspect Ratio** | 9:16 |
| **Codec** | H.264 (AVC) |
| **Container** | MP4 |
| **Frame Rate** | 30 fps |
| **Bitrate** | 5-8 Mbps |
| **Max File Size** | 250 MB |
| **Max Duration** | 90 seconds |
| **Audio Codec** | AAC |
| **Audio Bitrate** | 128 kbps |
| **Audio Sample Rate** | 44100 Hz |

**ffmpeg encode:**
```bash
ffmpeg -i input.mp4 -vf "scale=1080:1920:force_original_aspect_ratio=decrease,pad=1080:1920:-1:-1" -c:v libx264 -profile:v high -level:v 4.0 -crf 22 -preset medium -r 30 -c:a aac -b:a 128k -ar 44100 -movflags +faststart output_reels.mp4
```

### YouTube Shorts

| Parameter | Value |
|-----------|-------|
| **Resolution** | 1080 x 1920 |
| **Aspect Ratio** | 9:16 |
| **Codec** | H.264 (AVC) or H.265 (HEVC) |
| **Container** | MP4 |
| **Frame Rate** | 30 fps (24-60 accepted) |
| **Bitrate** | 8-12 Mbps |
| **Max File Size** | 256 GB (YouTube limit) |
| **Max Duration** | 3 minutes |
| **Audio Codec** | AAC |
| **Audio Bitrate** | 192 kbps |
| **Audio Sample Rate** | 48000 Hz |

**ffmpeg encode:**
```bash
ffmpeg -i input.mp4 -vf "scale=1080:1920:force_original_aspect_ratio=decrease,pad=1080:1920:-1:-1" -c:v libx264 -profile:v high -level:v 4.2 -crf 18 -preset medium -r 30 -c:a aac -b:a 192k -ar 48000 -movflags +faststart output_shorts.mp4
```

### YouTube (Standard / Horizontal)

| Parameter | Value |
|-----------|-------|
| **Resolution** | 1920 x 1080 (1080p) or 3840 x 2160 (4K) |
| **Aspect Ratio** | 16:9 |
| **Codec** | H.264 (AVC) preferred, H.265 (HEVC) accepted |
| **Container** | MP4 |
| **Frame Rate** | 30 fps (24-60 accepted) |
| **Bitrate** | 8-12 Mbps (1080p), 35-45 Mbps (4K) |
| **Max File Size** | 256 GB |
| **Max Duration** | 12 hours |
| **Audio Codec** | AAC |
| **Audio Bitrate** | 192-320 kbps |
| **Audio Sample Rate** | 48000 Hz |

**ffmpeg encode:**
```bash
ffmpeg -i input.mp4 -vf "scale=1920:1080:force_original_aspect_ratio=decrease,pad=1920:1080:-1:-1" -c:v libx264 -profile:v high -level:v 4.2 -crf 18 -preset medium -r 30 -c:a aac -b:a 192k -ar 48000 -movflags +faststart output_youtube.mp4
```

### LinkedIn Video

| Parameter | Value |
|-----------|-------|
| **Resolution** | 1920 x 1080 (horizontal) or 1080 x 1920 (vertical) |
| **Aspect Ratio** | 16:9 or 9:16 or 1:1 |
| **Codec** | H.264 (AVC) |
| **Container** | MP4 |
| **Frame Rate** | 30 fps |
| **Bitrate** | 5-10 Mbps |
| **Max File Size** | 5 GB |
| **Max Duration** | 10 minutes (native), 15 minutes (ads) |
| **Audio Codec** | AAC |
| **Audio Bitrate** | 128-192 kbps |
| **Audio Sample Rate** | 44100 Hz |

**ffmpeg encode:**
```bash
ffmpeg -i input.mp4 -vf "scale=1920:1080:force_original_aspect_ratio=decrease,pad=1920:1080:-1:-1" -c:v libx264 -profile:v high -level:v 4.1 -crf 20 -preset medium -r 30 -c:a aac -b:a 192k -ar 44100 -movflags +faststart output_linkedin.mp4
```

### Facebook Video

| Parameter | Value |
|-----------|-------|
| **Resolution** | 1920 x 1080 (horizontal) or 1080 x 1920 (vertical) |
| **Aspect Ratio** | 16:9 or 9:16 or 1:1 |
| **Codec** | H.264 (AVC) |
| **Container** | MP4 |
| **Frame Rate** | 30 fps |
| **Bitrate** | 5-8 Mbps |
| **Max File Size** | 10 GB |
| **Max Duration** | 240 minutes |
| **Audio Codec** | AAC |
| **Audio Bitrate** | 128 kbps |
| **Audio Sample Rate** | 44100 Hz |

**ffmpeg encode:**
```bash
ffmpeg -i input.mp4 -vf "scale=1920:1080:force_original_aspect_ratio=decrease,pad=1920:1080:-1:-1" -c:v libx264 -profile:v high -level:v 4.0 -crf 22 -preset medium -r 30 -c:a aac -b:a 128k -ar 44100 -movflags +faststart output_facebook.mp4
```

### X (Twitter) Video

| Parameter | Value |
|-----------|-------|
| **Resolution** | 1920 x 1080 (max), 720 x 1280 (vertical) |
| **Aspect Ratio** | 16:9 or 1:1 or 9:16 |
| **Codec** | H.264 (AVC) |
| **Container** | MP4 |
| **Frame Rate** | 30-60 fps |
| **Bitrate** | 5-8 Mbps |
| **Max File Size** | 512 MB |
| **Max Duration** | 140 seconds (free), 10 min (Premium+) |
| **Audio Codec** | AAC |
| **Audio Bitrate** | 128 kbps |
| **Audio Sample Rate** | 44100 Hz |

**ffmpeg encode:**
```bash
ffmpeg -i input.mp4 -vf "scale=1920:1080:force_original_aspect_ratio=decrease,pad=1920:1080:-1:-1" -c:v libx264 -profile:v high -level:v 4.0 -crf 22 -preset medium -r 30 -c:a aac -b:a 128k -ar 44100 -movflags +faststart output_x.mp4
```

## Safe Zones

Vertical platforms overlay UI elements on the video. Keep critical content (text, subtitles, faces) inside these safe zones:

| Platform | Top | Bottom | Left | Right |
|----------|-----|--------|------|-------|
| **TikTok** | 150px | 270px | 40px | 40px |
| **Instagram Reels** | 120px | 250px | 40px | 40px |
| **YouTube Shorts** | 120px | 200px | 40px | 40px |

## Encoding Validation Checklist

After encoding each clip, verify with ffprobe:

- Resolution matches target platform
- Codec is H.264 (or H.265 where accepted)
- Container is MP4
- Frame rate is within platform range
- File size is under platform maximum
- Audio codec is AAC
- `faststart` moov atom is at file start (for streaming)
