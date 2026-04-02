---
name: 05-export
description: Save clips to brand folder and update daily log
---

# Steps 10-11: Export & Status Update

## Outcome

Approved clips saved to the brand's video clip folder with a clean manifest, and daily activity log updated.

## Step 10: Export

Copy (or move) approved clips from the working directory to the final export location:

```
{project-root}/.pawbytes/creative-suites/brands/{brand-name}/videos/clips/{session-id}/
```

Structure:
```
{session-id}/
  clip-manifest.json
  tiktok/
    M01_tiktok_30s.mp4
    M03_tiktok_15s.mp4
  reels/
    M01_reels_30s.mp4
    M03_reels_15s.mp4
  shorts/
    M01_shorts_30s.mp4
  youtube/
    M01_youtube_60s.mp4
    M03_youtube_60s.mp4
  source-metadata.json    # ffprobe output from original source
```

Organize clips into platform subdirectories for easy bulk upload. The manifest at the root references all clips with their relative paths.

If clips were produced without a brand (unbranded), export to:
```
{project-root}/.pawbytes/creative-suites/output/clips/{session-id}/
```

## Step 11: Status Update

Append to the daily log at `{project-root}/.pawbytes/creative-suites/daily/{YYYY-MM-DD}.md`:

```markdown
### [VideoProducer] Clip Extraction Complete

- **Source:** {source_filename} ({duration})
- **Brand:** {brand-name}
- **Clips produced:** {count} across {platform_count} platforms
- **Output:** `brands/{brand-name}/videos/clips/{session-id}/`
- **Manifest:** `clip-manifest.json`
- **Timestamp:** {ISO-8601}
```

Create the daily log file if it does not exist. Append, never overwrite.

## Final Output

Present to the user:
1. Total clips produced and their locations
2. Per-platform breakdown (count and total file size)
3. Path to the clip manifest
4. Any clips that were excluded and why

If called by another workflow (e.g., `paw-cra-campaign-orchestration`), return the manifest path for downstream consumption.
