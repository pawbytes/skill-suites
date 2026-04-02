# Validation and Export (Steps 9-11)

This phase validates the video meets platform specifications, exports it to the correct location with a manifest, and logs the activity.

## Step 9: Codec Validation (Embedded Review Gate)

This step replaces the old standalone `cra-video-review-gate`. Run ffprobe to verify the candidate video meets all platform requirements.

### Validation Command

```bash
ffprobe -v quiet -print_format json -show_format -show_streams subtitled.mp4
```

### Validation Checks

| Check | Expected | Action on Failure |
|-------|----------|-------------------|
| Resolution | 1080x1920 | Re-encode with `-vf scale=1080:1920` |
| Codec | H.264 (libx264) | Re-encode with `-c:v libx264` |
| Pixel format | yuv420p | Re-encode with `-pix_fmt yuv420p` |
| Duration | Within 1s of target | Warn -- may need scene adjustment |
| File size | Under platform limit | Re-encode at lower bitrate or CRF |
| Audio codec | AAC | Re-encode audio with `-c:a aac` |
| Frame rate | 30fps | Re-encode with `-r 30` |

### Platform File Size Limits

| Platform | Max Size | Recommended Bitrate |
|----------|----------|-------------------|
| TikTok | 287 MB | 8-12 Mbps |
| Reels | 250 MB | 8-10 Mbps |
| Shorts | 256 MB | 8-10 Mbps |

For 60s at 10 Mbps, the file is ~75 MB -- well within all limits. Only intervene if the file is unexpectedly large.

### Re-encode if Needed

If any check fails, re-encode with corrective flags:

```bash
ffmpeg -i subtitled.mp4 \
  -c:v libx264 -preset medium -crf 18 -pix_fmt yuv420p \
  -vf "scale=1080:1920" -r 30 \
  -c:a aac -b:a 192k \
  final.mp4
```

### Validation Report

Produce a brief validation summary:

```
Codec: H.264 -- PASS
Resolution: 1080x1920 -- PASS
Duration: 28.3s (target: 30s) -- PASS
File size: 12.4 MB (limit: 287 MB) -- PASS
Audio: AAC 192kbps -- PASS
Subtitles: Burned in -- PASS
```

If all checks pass, the video is ready for export. If any checks required re-encoding, validate again after the fix.

In interactive mode, show the validation report and ask for final approval before export. In headless mode, auto-approve if all checks pass; fail the run if any check cannot be fixed automatically.

## Step 10: Export

### File Placement

Move the final video to the brand's video directory:

```
{project-root}/.pawbytes/creative-suites/brands/{brand}/videos/{filename}.mp4
```

**Filename convention:** `{platform}-{topic-slug}-{YYYYMMDD}-{HHmm}.mp4`

Example: `tiktok-product-launch-20260401-1430.mp4`

### Video Manifest

Write `video-manifest.json` alongside the video (or append to existing manifest array):

```json
{
  "id": "{uuid}",
  "filename": "{filename}.mp4",
  "path": ".pawbytes/creative-suites/brands/{brand}/videos/{filename}.mp4",
  "created": "{ISO-8601}",
  "brand": "{brand}",
  "platform": "{platform}",
  "type": "short-form",
  "duration_seconds": {actual_duration},
  "resolution": "1080x1920",
  "codec": "H.264",
  "audio_codec": "AAC",
  "file_size_bytes": {size},
  "has_subtitles": true,
  "has_voiceover": {true|false},
  "has_music": {true|false},
  "topic": "{topic}",
  "scene_count": {N},
  "generation_model": "{model_used}",
  "storyboard": {storyboard_object},
  "script_source": "{user|strategist|inline}",
  "campaign": "{campaign_name|null}",
  "status": "ready"
}
```

### Working Directory Cleanup

After successful export, the working directory (`{work_dir}`) can be cleaned up. Keep it if the user might want to re-edit individual scenes. In headless mode, clean up by default.

## Step 11: Status Update

### Daily Activity Log

Append to `{project-root}/.pawbytes/creative-suites/daily/{YYYY-MM-DD}.md`:

```markdown
## {HH:MM} [VideoProducer]
**Task:** Short-form video production
**For:** {brand}{/campaign if applicable}
**Platform:** {platform}
**Duration:** {duration}s
**Output:** .pawbytes/creative-suites/brands/{brand}/videos/{filename}.mp4
**Model:** {generation_model}
**Scenes:** {scene_count}
**Status:** Complete
```

### Campaign Status (if applicable)

If this video is part of a campaign, update `{project-root}/.pawbytes/creative-suites/brands/{brand}/campaigns/{campaign}/status.md` to reflect the new deliverable.

### Final Output Summary

Present to the user (or return in headless mode):

```
## Video Complete

**File:** {filename}.mp4
**Location:** .pawbytes/creative-suites/brands/{brand}/videos/
**Duration:** {duration}s
**Platform:** {platform}
**Resolution:** 1080x1920 (H.264)
**File size:** {size} MB
**Subtitles:** Burned in
**Voiceover:** {Yes/No}

Manifest updated: video-manifest.json
```
