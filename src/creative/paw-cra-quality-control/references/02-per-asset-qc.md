# Stage 2: Per-Asset QC

Run quality checks on every asset in the inventory. Visual assets and video assets have different check profiles.

## Goal

Evaluate each asset against brand guidelines, platform specifications, and technical quality standards. Record per-asset pass/fail with specific issues.

## Visual Asset Checks

For each image/design asset (from `design-manifest.json`, `batch-manifest.json`):

**Brand Compliance**
- Colors used match brand palette from `guidelines.md` (allow minor variance for photography/gradients, flag solid UI elements that deviate)
- Typography matches brand fonts (if detectable from the asset or manifest metadata)
- Logo usage follows brand guidelines (placement, clear space, minimum size)
- Overall style consistent with brand personality

**Platform Specifications**
- Dimensions match the intended platform requirements (e.g., 1080x1080 for Instagram feed, 1080x1350 for Instagram portrait, 1080x1920 for Stories)
- Aspect ratio is correct for the target platform
- File is within platform size limits

**Technical Quality**
- File format matches spec (PNG, JPG, PDF as specified)
- Resolution is adequate (not upscaled/blurry)
- No rendering artifacts --- white gaps, text overflow outside safe zones, cut-off elements
- Text is readable at expected viewing size (not too small for mobile)

**Common Mistakes** (check for these specifically)
- White gaps from incorrect HTML rendering (common with template-based generation)
- Text outside safe zones (platform-specific margins where content may be cropped)
- Transparent backgrounds where solid was expected (or vice versa)
- Incorrect color space (CMYK exported for web, RGB for print)

## Video Asset Checks

For each video asset (from `video-manifest.json`, `clip-manifest.json`):

**Codec & Format**
- Container format is MP4
- Video codec is H.264 (or H.265 if spec explicitly allows)
- Audio codec is AAC
- Bitrate is reasonable for the resolution

**Resolution & Dimensions**
- Matches intended platform: 1080x1920 (vertical/short-form), 1920x1080 (horizontal/long-form), or as specified
- No black bars or incorrect aspect ratio

**Duration**
- Duration matches spec from brief/manifest (within 2-second tolerance)
- Platform constraints met (e.g., Reels max 90s, TikTok max 10min)

**Subtitles**
- Subtitle track present (burned in or as separate file)
- Subtitles are readable (contrast against background, reasonable font size)
- Subtitle timing is synchronized (not leading/lagging noticeably)

**Audio**
- Audio levels normalized (peak around -1dB to -3dB, average around -14 LUFS for social)
- No clipping or distortion
- Voiceover clear and audible above background music

**Note on technical checks:** Where possible, use `ffprobe` (part of ffmpeg) to extract codec, resolution, duration, and audio metadata programmatically. If ffprobe is not available, rely on manifest metadata and visual inspection.

## Recording Findings

Append findings to the `qa-report.md` per-asset section:

```markdown
## Per-Asset Results

### {asset-filename}
- **Verdict:** PASS / FAIL
- **Platform:** {target-platform}
- **Issues:**
  - [CRITICAL] {description}
  - [WARNING] {description}
  - [INFO] {description}
```

Update the front matter `status` to reflect progress. Update `updated` timestamp.

## Progression

Proceed to Stage 3 when all assets have been checked individually. The cross-asset consistency stage builds on these per-asset findings.
