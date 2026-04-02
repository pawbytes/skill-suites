# paw-cra-multi-platform-export

## Overview

Final-mile export workflow that converts master visual and video assets into all target platform variants. Handles both images and videos in a unified pipeline with safe-zone enforcement to ensure critical content is never cropped by platform UI overlays.

## What It Does

| Capability | Description |
|------------|-------------|
| Image resize | Scale, crop, or letterbox to platform dimensions |
| Video transcode | Re-encode for platform codec and bitrate requirements |
| Safe-zone enforcement | Protect content from platform UI overlays |
| Aspect ratio conversion | Horizontal to vertical, vertical to horizontal |
| Format optimization | JPEG quality, H.264 encoding, file size limits |
| Batch export | Process multiple assets to multiple platforms |

## When to Use It

- You need to export one asset for all platforms
- You want platform-specific variants from a master file
- You need to resize images for different aspect ratios
- You want to convert horizontal video to vertical
- You need safe-zone protected exports

## Trigger Phrases

- "export for all platforms"
- "resize assets for platforms"
- "multi-platform export"
- "create variants for all platforms"
- "export master to social formats"

## What You Get (Deliverables)

| Output | Location |
|--------|----------|
| Platform-variant files | `.pawbytes/creative-suites/brands/{brand}/exports/{campaign}/{platform}/` |
| export-manifest.json | Export folder root |

## Output Structure

```
exports/{campaign}/
  instagram/
    {brand}_{campaign}_instagram_image_feed-portrait.jpg
    {brand}_{campaign}_instagram_image_story.jpg
    {brand}_{campaign}_instagram_video_reel.mp4
  tiktok/
    {brand}_{campaign}_tiktok_video_feed.mp4
  youtube/
    {brand}_{campaign}_youtube_video_main.mp4
    {brand}_{campaign}_youtube_image_thumbnail.jpg
  export-manifest.json
```

## Supported Platforms

Instagram, TikTok, YouTube, Facebook, LinkedIn, Twitter/X, Pinterest, Google Business

## Safe-Zone Reference

| Platform | Top | Bottom | Left | Right | Notes |
|----------|-----|--------|------|-------|-------|
| Instagram Feed | 0 | 0 | 0 | 0 | Clean viewport |
| Instagram Story | 120 | 200 | 60 | 60 | Top status, bottom CTA |
| TikTok | 50 | 150 | 20 | 20 | Bottom: username, caption |
| YouTube | 0 | 40 | 0 | 0 | Bottom: progress bar |
| Facebook Feed | 0 | 60 | 0 | 0 | Bottom: reaction bar |
| LinkedIn Feed | 0 | 50 | 0 | 0 | Bottom: engagement bar |
| Twitter/X | 0 | 0 | 0 | 0 | Clean viewport |

## Tool Requirements

| Tool | Required | Purpose |
|------|----------|---------|
| ffmpeg | Yes | Image and video processing |
| ImageMagick | No | Enhanced image operations |

## Quick Example

**Input**: "Export this master video (1920x1080, 2 minutes) for Instagram Reels, TikTok, and YouTube Shorts"

**Output**:
- `brand_campaign_instagram_video_reel.mp4` (1080x1920)
- `brand_campaign_tiktok_video_feed.mp4` (1080x1920)
- `brand_campaign_youtube_video_short.mp4` (1080x1920)
- `export-manifest.json`

## Related Skills

- [paw-cra-design-social](./paw-cra-design-social.md) - Create social posts
- [paw-cra-video-shortform](./paw-cra-video-shortform.md) - Create short-form videos
- [paw-cra-video-clips](./paw-cra-video-clips.md) - Extract clips from long-form