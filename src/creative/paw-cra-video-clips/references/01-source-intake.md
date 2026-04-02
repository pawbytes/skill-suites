---
name: 01-source-intake
description: Parse source video and establish clip extraction parameters
---

# Step 1: Source Intake

## Outcome

A validated source video with clear extraction parameters: target platforms, target durations, and brand context loaded.

## Inputs to Gather

| Input | Required | Default | Source |
|-------|----------|---------|--------|
| **Source video** | Yes | -- | File path or URL provided by user/caller |
| **Target platforms** | No | All vertical (TikTok, Reels, Shorts) + YouTube | User preference or brand guidelines |
| **Target durations** | No | 15s, 30s, 60s | User preference |
| **Brand name** | No | `{default_brand}` | Config or user input |

## Source Validation

Use ffprobe to extract source video metadata:

```bash
ffprobe -v quiet -print_format json -show_format -show_streams "{source_path}"
```

Confirm these are usable before proceeding:
- **Duration** -- source must be longer than the longest target clip duration
- **Resolution** -- note whether horizontal (16:9) or vertical (9:16) to determine reframing needs
- **Codec** -- note for extraction compatibility
- **Audio** -- confirm audio track exists (needed for subtitle generation)

If the source is a URL, download it first using ffmpeg or curl to a temp location within the output directory.

## Brand Context

If a brand name is provided or defaulted, load:
- `{project-root}/.pawbytes/creative-suites/brands/{brand-name}/guidelines.md` -- for colors, fonts, watermark paths, intro/outro assets
- Check for existing brand video assets (intro bumpers, end cards, watermarks) in `brands/{brand-name}/assets/video/`

If no brand guidelines exist, proceed without brand overlay. Inform the user that clips will be unbranded.

## Output

A mental model (or status note in the manifest) capturing:
- Source video path and metadata (duration, resolution, codec)
- Target platforms list
- Target durations list
- Brand name and available brand assets
- Output directory: `{project-root}/.pawbytes/creative-suites/brands/{brand-name}/videos/clips/{session-id}/`

Create the output directory. Use a session ID based on date and source filename (e.g., `2026-04-01-podcast-ep12`).

## Progression

Proceed to `./references/02-analysis.md` when source is validated and parameters are set.
