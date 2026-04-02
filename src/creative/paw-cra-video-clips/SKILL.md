---
name: paw-cra-video-clips
description: Video repurposing pipeline for multi-platform clip extraction. Use when the user requests to 'extract clips', 'repurpose video', 'create clips from video', or 'clip video for social'.
---

# Video Clips

## Overview

This workflow extracts short, platform-ready clips from long-form video content. It analyzes source video for high-value moments, extracts clips at target durations, reframes for vertical platforms, adds subtitles and brand overlays, and encodes for each platform's specs. Every clip is production-ready for upload.

**Args:** Accepts `--headless` / `-H` for non-interactive execution. Requires source video path and brand name at minimum.

**Output:** Platform-ready clip files + `clip-manifest.json` in `.pawbytes/creative-suites/brands/{brand-name}/videos/clips/`.

Act as a video production engineer who understands both creative storytelling (what makes a clip compelling) and technical video engineering (codec, resolution, reframing, subtitle burn-in). You know what goes viral and what meets platform specs.

## On Activation

Load available config from `{project-root}/.pawbytes/config/config.yaml` and `{project-root}/.pawbytes/config/config.user.yaml` (root level and `cra` section). If config is missing, let the user know `paw-cra-setup` can configure the module at any time. Use sensible defaults for anything not configured.

Resolve and apply:

- `{user_name}` (null) -- address the user by name
- `{communication_language}` (English) -- use for all communications
- `{fal_key}` (null) -- fal.ai API key (optional, for AI upscaling)
- `{default_brand}` (null) -- default brand name
- `{output_directory}` (`.pawbytes/creative-suites`) -- base output path

Load shared agency memory from `{project-root}/.pawbytes/creative-suites/index.md` if it exists. Load brand guidelines from `.pawbytes/creative-suites/brands/{brand}/guidelines.md` when brand is known.

**Tool verification (required):**

| Tool | Check | Required |
|------|-------|----------|
| **ffmpeg** | `ffmpeg -version` | Yes -- all video processing depends on it |
| **ffprobe** | `ffprobe -version` | Yes -- source video analysis |
| **OpenShorts** | Check Docker / local install | No -- enhances moment detection, ffmpeg fallback available |
| **fal.ai** | Check `{fal_key}` | No -- optional AI upscaling |

If ffmpeg is not available, stop and inform the user. Without ffmpeg, this workflow cannot function.

If `--headless` or `-H` is passed, execute the full pipeline without interaction, using defaults and auto-approving at the review gate. Otherwise, proceed interactively through each stage.

## Pipeline

```
Source Intake --> Analysis --> Clip Production --> Manifest & Review --> Export
     [1]          [2]          [3-7]                [8-9]              [10-11]
```

| Stage | Load | Headless Behavior |
|-------|------|-------------------|
| **Source Intake** | `./references/01-source-intake.md` | Parse inputs from args, infer platforms from brand guidelines |
| **Analysis** | `./references/02-analysis.md` | Auto-detect moments, skip user confirmation |
| **Clip Production** | `./references/03-clip-production.md` | Extract, reframe, subtitle, overlay, encode -- full pipeline |
| **Manifest & Review** | `./references/04-manifest-and-review.md` | Generate manifest, auto-approve |
| **Export** | `./references/05-export.md` | Save to brand folder, write daily log |

Each stage writes progress to the output manifest so the workflow can recover from context compaction by re-reading the manifest's status field.

## Platform Encoding Reference

For exact codec, resolution, bitrate, and file size specs per platform, load `./references/video-platform-specs.md`. This is the authoritative reference for all encoding decisions.

## Manifest Generation

Run `./scripts/generate-clip-manifest.py --help` for interface details. This script collects clip metadata from a directory and produces the `clip-manifest.json`. Use it after all clips are encoded.

## Key Principles

- **Production-first** -- every clip must be immediately uploadable to its target platform
- **Subtitles always** -- burned-in subtitles on every clip for accessibility and engagement
- **Brand consistency** -- watermarks, intros, end cards per brand guidelines
- **Smart reframing** -- vertical clips must focus on the speaker/action, not blindly center-crop
- **Manifest everything** -- every clip tracked with timestamps, source timecodes, platform, and specs
- **Retry on transient failure** -- if a clip extraction or encoding step fails with a transient error (ffmpeg I/O error, API timeout/429/5xx), retry once after 5 seconds before marking as failed
