---
name: paw-cra-multi-platform-export
description: Convert master assets into platform-variant exports with safe-zone enforcement. Use when the user requests to 'export for all platforms', 'resize assets for platforms', or 'multi-platform export'.
---

# Multi-Platform Export

## Overview

This workflow converts approved master visual and video assets into all target platform variants — resized, re-encoded, and organized into a delivery-ready folder structure with a machine-readable manifest. It handles both images and videos in a single unified pipeline, enforcing safe zones so critical content (text, logos, faces) is never cropped or obscured by platform UI.

**Args:** Accepts `--headless` / `-H` for non-interactive execution. In headless mode, requires master asset path(s) and target platform list as arguments or reads them from the active campaign brief.

**Output:** Platform-variant files organized by platform in folders, plus `export-manifest.json` describing every variant with its specs.

Act as a technical export specialist who understands platform constraints, codec requirements, and safe-zone geometry. Prioritize visual integrity — a variant that preserves the master's intent at slightly lower resolution is always better than one that crops critical content to hit exact pixel dimensions.

## On Activation

Load available config from `{project-root}/.pawbytes/config/config.yaml` and `{project-root}/.pawbytes/config/config.user.yaml` (root level and `cra` section). If config is missing, let the user know `paw-cra-setup` can configure the module at any time. Resolve and apply throughout the session (defaults in parens):

- `{output_directory}` (`.pawbytes/creative-suites`) — base output path
- `{default_brand}` (null) — active brand for naming convention

Load shared agency memory from `{project-root}/.pawbytes/creative-suites/index.md` if available. If an active campaign exists, read the campaign brief for brand name and campaign name (used in file naming).

**Tool Verification:** Check for ffmpeg availability — it is required for both image and video processing. If missing, abort with install instructions (`winget install ffmpeg` / `brew install ffmpeg`). ImageMagick is optional and enhances image-specific operations.

If `--headless`, proceed directly with provided inputs. Otherwise, greet the user and ask for master asset(s) and target platforms.

---

## Pipeline

### Step 1 — Source Intake

Collect inputs:

- **Master asset(s):** One or more file paths (images or videos). Detect media type from extension and ffprobe metadata.
- **Target platforms:** Which platforms to export for. If not specified, default to all supported platforms.
- **Brand and campaign name:** For the naming convention. Infer from active campaign context or ask.

Supported platforms: Instagram, TikTok, YouTube, Facebook, LinkedIn, Twitter/X, Pinterest, Google Business.

Classify each source file:
- **Image:** `.png`, `.jpg`, `.jpeg`, `.webp`, `.tiff`, `.bmp`, `.svg`
- **Video:** `.mp4`, `.mov`, `.avi`, `.mkv`, `.webm`

### Step 2 — Platform Spec Lookup

Load `./references/platform-export-specs.md` for complete platform specifications including dimensions, aspect ratios, safe zones, file size limits, codec requirements, and duration limits.

For each source asset + target platform combination, determine:
- Target dimensions and aspect ratio
- Safe-zone insets (pixels from each edge where platform UI overlays content)
- File size ceiling
- For video: codec, bitrate, max duration, subtitle handling

### Step 3 — Image Export

For each image + platform pair:

1. **Analyze source** — get dimensions, aspect ratio, identify focal content region using ffprobe or ImageMagick identify
2. **Resize strategy** — choose the approach that best preserves the master's intent:
   - **Same aspect ratio:** Scale proportionally
   - **Minor crop needed:** Crop centered on focal point, verify critical content stays inside safe zone
   - **Major aspect change:** Prefer letterboxing/pillarboxing with brand-colored bars over aggressive cropping. If user prefers cropping, confirm focal point first.
3. **Safe-zone enforcement** — after resize/crop, verify no critical content (text overlays, logos, key subjects) falls outside the safe zone. Critical content must have at least the platform's safe-zone inset from every edge.
4. **Re-encode** — JPEG (quality 90) for photographs, PNG for graphics with transparency. Keep under the platform's file size limit. If over limit, reduce JPEG quality progressively (85 → 80 → 75) until compliant.
5. **Verify** — confirm final dimensions match spec, file size is under limit.

**ffmpeg examples for image resize:**
```bash
# Scale to fit within dimensions, maintaining aspect ratio
ffmpeg -i master.png -vf "scale=1080:1350:force_original_aspect_ratio=decrease,pad=1080:1350:(ow-iw)/2:(oh-ih)/2:color=#000000" output.jpg

# Crop to exact dimensions centered on focal point
ffmpeg -i master.png -vf "scale=1080:-1,crop=1080:1080" output.jpg
```

### Step 4 — Video Export

For each video + platform pair:

1. **Probe source** — get resolution, duration, codec, bitrate, subtitle tracks using ffprobe
2. **Duration check** — if source exceeds platform max duration, warn the user (do not auto-trim in headless mode — flag it in the manifest as `duration_exceeded`)
3. **Aspect ratio adjustment:**
   - **Horizontal to vertical (e.g., 16:9 to 9:16):** Smart crop centered on the action area. Prefer cropping over letterboxing for vertical video platforms (TikTok, Reels).
   - **Vertical to horizontal:** Pillarbox with blurred background or brand-colored bars.
   - **Same ratio, different resolution:** Scale directly.
4. **Re-encode** — H.264 (libx264), AAC audio, platform-appropriate bitrate. Target CRF 18-23 depending on platform ceiling.
5. **Subtitle repositioning** — if source has subtitle tracks and aspect ratio changed, re-position to stay within the new safe zone. For burned-in subtitles, re-render at adjusted coordinates.
6. **Verify** — confirm resolution, codec, duration, and file size meet platform requirements.

**ffmpeg examples for video:**
```bash
# Horizontal to vertical (smart center crop)
ffmpeg -i master.mp4 -vf "scale=1920:-1,crop=1080:1920" -c:v libx264 -crf 20 -c:a aac -b:a 128k output.mp4

# Scale to platform resolution
ffmpeg -i master.mp4 -vf "scale=1920:1080:force_original_aspect_ratio=decrease,pad=1920:1080:(ow-iw)/2:(oh-ih)/2" -c:v libx264 -crf 20 -c:a aac output.mp4
```

### Step 5 — Naming Convention

Apply consistent naming to all exported files:

```
{brand}_{campaign}_{platform}_{asset-type}_{variant}.{ext}
```

| Component | Source | Example |
|-----------|--------|---------|
| `brand` | Active brand (lowercase, hyphens) | `acme-corp` |
| `campaign` | Campaign name (lowercase, hyphens) | `spring-launch` |
| `platform` | Target platform (lowercase) | `instagram`, `tiktok`, `youtube` |
| `asset-type` | `image` or `video` | `image` |
| `variant` | Platform-specific format descriptor | `feed-portrait`, `story`, `thumbnail` |
| `ext` | Platform-optimal format | `jpg`, `png`, `mp4` |

Example: `acme-corp_spring-launch_instagram_image_feed-portrait.jpg`

If brand or campaign is unknown, omit those segments: `instagram_image_feed-portrait.jpg`

### Step 6 — Export Organization

Organize all variants into platform-specific folders under the export directory:

```
{output_directory}/brands/{brand}/exports/{campaign}/
  instagram/
    acme-corp_spring-launch_instagram_image_feed-portrait.jpg
    acme-corp_spring-launch_instagram_image_story.jpg
    acme-corp_spring-launch_instagram_video_reel.mp4
  tiktok/
    acme-corp_spring-launch_tiktok_video_feed.mp4
  youtube/
    acme-corp_spring-launch_youtube_video_main.mp4
    acme-corp_spring-launch_youtube_image_thumbnail.jpg
  ...
  export-manifest.json
```

### Step 7 — Export Manifest

Generate `export-manifest.json` at the root of the export directory:

```json
{
  "brand": "acme-corp",
  "campaign": "spring-launch",
  "exported_at": "2026-04-01T14:30:00Z",
  "source_assets": [
    {
      "path": "path/to/master.png",
      "type": "image",
      "dimensions": "2400x3000",
      "file_size_bytes": 4500000
    }
  ],
  "variants": [
    {
      "platform": "instagram",
      "variant": "feed-portrait",
      "type": "image",
      "filename": "acme-corp_spring-launch_instagram_image_feed-portrait.jpg",
      "path": "instagram/acme-corp_spring-launch_instagram_image_feed-portrait.jpg",
      "dimensions": "1080x1350",
      "aspect_ratio": "4:5",
      "file_size_bytes": 245000,
      "format": "jpeg",
      "status": "ok"
    },
    {
      "platform": "tiktok",
      "variant": "feed",
      "type": "video",
      "filename": "acme-corp_spring-launch_tiktok_video_feed.mp4",
      "path": "tiktok/acme-corp_spring-launch_tiktok_video_feed.mp4",
      "dimensions": "1080x1920",
      "aspect_ratio": "9:16",
      "duration_seconds": 45,
      "codec": "h264",
      "file_size_bytes": 12000000,
      "status": "ok"
    }
  ],
  "warnings": [],
  "total_variants": 8,
  "total_size_bytes": 45000000
}
```

Status values: `ok`, `duration_exceeded`, `size_exceeded`, `quality_reduced`, `skipped`.

Include any warnings (e.g., "TikTok variant exceeds 60s duration limit — manual trim needed").

### Step 8 — Status Update

Append to the daily log at `{project-root}/.pawbytes/creative-suites/daily/YYYY-MM-DD.md`:

```markdown
[Export] Multi-platform export complete for {campaign}
- Source: {N} master asset(s)
- Exported: {M} variants across {P} platforms
- Warnings: {W} (or "none")
- Manifest: {path-to-export-manifest.json}
```

---

## Safe-Zone Reference

Safe zones protect content from being hidden by platform UI (buttons, captions, navigation bars). These are the minimum pixel insets from each edge where no critical content should appear.

| Platform | Top | Bottom | Left | Right | Notes |
|----------|-----|--------|------|-------|-------|
| Instagram Feed | 0 | 0 | 0 | 0 | Clean viewport |
| Instagram Story | 120 | 200 | 60 | 60 | Top status bar, bottom CTA |
| TikTok | 50 | 150 | 20 | 20 | Bottom: username, caption, music |
| YouTube | 0 | 40 | 0 | 0 | Bottom: progress bar and controls overlay |
| Facebook Feed | 0 | 60 | 0 | 0 | Bottom: reaction bar and captions overlay |
| Facebook Story | 120 | 200 | 60 | 60 | Same as Instagram Story |
| LinkedIn Feed | 0 | 50 | 0 | 0 | Bottom: engagement bar overlay on video |
| Twitter/X | 0 | 0 | 0 | 0 | Clean viewport |
| Pinterest | 0 | 50 | 0 | 0 | Bottom: pin info overlay |
| Google Business | 0 | 0 | 0 | 0 | Clean viewport |

For video platforms with vertical content (TikTok, Reels, Stories), safe zones are critical — the bottom 10-15% of the frame is typically covered by UI elements.

---

## Error Handling

- **ffmpeg not found:** Abort with install instructions. Do not attempt Python-only fallback for video.
- **Source file missing:** Skip with warning in manifest, continue with remaining files.
- **Source too low resolution:** Warn if upscaling exceeds 150%. Proceed but note `quality_reduced` in manifest.
- **File size over limit after compression:** Note `size_exceeded` in manifest. Suggest manual optimization.
- **Duration over limit:** Note `duration_exceeded` in manifest. Do not auto-trim.
- **Unsupported format:** Skip with warning, suggest conversion first.
