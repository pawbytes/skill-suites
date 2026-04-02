# Video Platform Specifications

## Short-Form Vertical Video

| Platform | Resolution | Aspect | Duration | Codec | Bitrate | FPS | Max Size |
|----------|-----------|--------|----------|-------|---------|-----|----------|
| **TikTok** | 1080x1920 | 9:16 | 15-180s | H.264 | 6-10 Mbps | 30 | 287 MB |
| **Instagram Reels** | 1080x1920 | 9:16 | 15-90s | H.264 | 6-10 Mbps | 30 | 250 MB |
| **YouTube Shorts** | 1080x1920 | 9:16 | 15-60s | H.264 | 8-12 Mbps | 30 | 256 MB |
| **Facebook Reels** | 1080x1920 | 9:16 | 3-90s | H.264 | 6-10 Mbps | 30 | 250 MB |
| **Pinterest Idea Pin** | 1080x1920 | 9:16 | 3-60s | H.264 | 6-8 Mbps | 30 | 250 MB |

### Short-Form Safe Zones

```
┌────────────────────┐
│   TOP SAFE ZONE    │  50px - System UI (time, battery)
│                    │
│                    │
│                    │
│   CONTENT ZONE     │  Main visual content area
│                    │
│                    │
│                    │
│  SUBTITLE ZONE     │  70% from top - Subtitle placement
│                    │
│  BOTTOM SAFE ZONE  │  150px - Platform UI (username, caption, buttons)
└────────────────────┘
```

**Critical:** TikTok and Reels overlay UI elements at the bottom 150px and right side 50px. Keep critical content within the safe zone.

## Long-Form Horizontal Video

| Platform | Resolution | Aspect | Duration | Codec | Bitrate | FPS | Max Size |
|----------|-----------|--------|----------|-------|---------|-----|----------|
| **YouTube** | 1920x1080 | 16:9 | No limit | H.264 High | 10-16 Mbps | 30 | 256 GB |
| **YouTube 4K** | 3840x2160 | 16:9 | No limit | H.265/VP9 | 35-45 Mbps | 30 | 256 GB |
| **LinkedIn Video** | 1920x1080 | 16:9 | 3s-10min | H.264 Main | 8-10 Mbps | 30 | 5 GB |
| **Facebook Video** | 1920x1080 | 16:9 | 1s-240min | H.264 | 8-12 Mbps | 30 | 10 GB |
| **X (Twitter) Video** | 1920x1080 | 16:9 | 0.5-140s | H.264 | 6-10 Mbps | 30 | 512 MB |
| **Vimeo** | 1920x1080 | 16:9 | No limit | H.264 High | 10-20 Mbps | 30 | 500 MB+ |

### Long-Form Safe Zones

```
┌─────────────────────────────────────────────┐
│  10px margin all sides for platform UI      │
│  ┌───────────────────────────────────────┐  │
│  │                                       │  │
│  │          CONTENT ZONE                 │  │
│  │                                       │  │
│  │                                       │  │
│  │                                       │  │
│  │  ┌─────────────────────────────────┐  │  │
│  │  │   SUBTITLE ZONE (bottom 15%)   │  │  │
│  │  │   80px margin from bottom       │  │  │
│  │  └─────────────────────────────────┘  │  │
│  └───────────────────────────────────────┘  │
└─────────────────────────────────────────────┘
```

## Audio Specifications

| Platform | Audio Codec | Sample Rate | Bitrate | Channels |
|----------|------------|-------------|---------|----------|
| **YouTube** | AAC | 48kHz | 256 kbps | Stereo |
| **TikTok** | AAC | 44.1kHz | 128-256 kbps | Stereo |
| **Instagram** | AAC | 44.1kHz | 128 kbps | Stereo |
| **LinkedIn** | AAC | 44.1kHz | 128 kbps | Stereo |
| **Facebook** | AAC | 44.1kHz | 128-256 kbps | Stereo |

## Encoding Quick Reference

### Standard Short-Form Encode

```bash
ffmpeg -i input.mp4 \
  -vf "scale=1080:1920:force_original_aspect_ratio=decrease,pad=1080:1920:(ow-iw)/2:(oh-ih)/2" \
  -c:v libx264 -preset medium -profile:v main -level 4.0 \
  -b:v 8M -maxrate 10M -bufsize 16M \
  -c:a aac -b:a 128k -ar 44100 \
  -movflags +faststart \
  -r 30 \
  output.mp4
```

### Standard Long-Form Encode

```bash
ffmpeg -i input.mp4 \
  -vf "scale=1920:1080:force_original_aspect_ratio=decrease,pad=1920:1080:(ow-iw)/2:(oh-ih)/2" \
  -c:v libx264 -preset medium -profile:v high -level 4.1 \
  -b:v 12M -maxrate 16M -bufsize 24M \
  -c:a aac -b:a 256k -ar 48000 \
  -movflags +faststart \
  -r 30 \
  output.mp4
```
