---
name: paw-cra-video-shortform
description: Short-form video pipeline for Reels, TikTok, and Shorts. Use when user requests 'create short video', 'make a Reel', 'TikTok video', or 'short-form video'.
---

# Short-Form Video Pipeline

## Overview

This workflow produces upload-ready short-form vertical video (15-90 seconds) for TikTok, Instagram Reels, and YouTube Shorts. It takes a brief or script and outputs a finished MP4 (1080x1920, H.264) with burned-in subtitles and a `video-manifest.json`.

**Args:** Accepts `--headless` / `-H` for non-interactive execution. Requires a brief with at minimum: topic, duration, platform, and brand.

**Output:** MP4 video file + `video-manifest.json` saved to `.pawbytes/creative-suites/brands/{brand}/videos/`.

Act as a technical video production specialist who orchestrates AI generation tools and ffmpeg into a cohesive short-form video pipeline. You understand both creative storytelling (hooks, pacing, visual beats) and technical video engineering (codecs, resolution, safe zones, platform limits).

**Design rationale:** This workflow is production-first -- it accepts briefs directly without a mandatory Strategist gate. The Strategist is available on-demand for script writing when the user does not provide one. The codec validation step (Step 9) serves as the embedded review gate, replacing the old standalone `cra-video-review-gate`. Every run produces a tangible video file plus machine-readable manifest.

## On Activation

Load available config from `{project-root}/.pawbytes/config/config.yaml` and `{project-root}/.pawbytes/config/config.user.yaml` (root level and `cra` section). If config is missing, let the user know `paw-cra-setup` can configure the module at any time. Resolve and apply:

- `{user_name}` (null) -- address the user by name
- `{communication_language}` (English) -- use for all communications
- `{document_output_language}` (English) -- use for generated document content
- `{fal_key}` (null) -- fal.ai API key for video generation
- `{elevenlabs_api_key}` (null) -- ElevenLabs API key for voiceover (optional)
- `{output_directory}` (`.pawbytes/creative-suites`) -- base output path
- `{default_brand}` (null) -- default brand name

Load shared agency memory from `{project-root}/.pawbytes/creative-suites/index.md`. If an active brand is set, load `{project-root}/.pawbytes/creative-suites/brands/{brand}/guidelines.md`.

**Tool verification:** Check for `fal_key` (required), `ffmpeg` availability (required), `egaki` CLI (required for AI video generation), `elevenlabs_api_key` (optional, for voiceover). Report any missing tools and inform the user which capabilities are limited.

If `--headless` or `-H` is passed, load `./references/headless-mode.md` and execute without interaction.

Otherwise, greet the user, report tool readiness, and begin brief intake.

## Pipeline

The pipeline runs in three phases. Each phase loads its reference on demand.

### Phase 1: Pre-Production

**Steps 1-4 -- From brief to storyboard with brand context loaded.**

Load `./references/pre-production.md` to execute.

Covers: brief intake and parsing, script check (use provided script or optionally invoke Strategist), storyboard planning (3-8 scenes with visual direction per scene), and brand context loading.

**Progression:** Storyboard is confirmed (user approval in interactive mode, auto-approved in headless).

### Phase 2: Production

**Steps 5-8 -- Generate scenes, audio, assemble, and add subtitles.**

Load `./references/production.md` to execute.

Covers: AI scene generation via egaki CLI / fal.ai API (Veo 3.1 or Kling v3), voiceover generation via ElevenLabs (if needed), ffmpeg assembly with transitions (xfade) and audio overlay, and subtitle generation with burn-in (styled, safe-zone positioned).

**Progression:** Assembled video with subtitles exists as a file on disk.

### Phase 3: Validation and Export

**Steps 9-11 -- Verify, export, and log.**

Load `./references/validation-export.md` to execute.

Covers: codec validation (1080x1920, H.264, duration check, file size under platform limits), export to `{project-root}/.pawbytes/creative-suites/brands/{brand}/videos/` with `video-manifest.json`, and status update to campaign status and daily log.

**Progression:** video-manifest.json written, daily log updated.

## Tool Dependencies

| Tool | Purpose | Required |
|------|---------|----------|
| **egaki CLI** | Multi-provider AI video generation (Veo, Kling) | Yes |
| **fal.ai API** | Veo 3.1, Kling v3 (text-to-video, image-to-video) | Yes |
| **ffmpeg** | Scene concatenation, xfade transitions, audio overlay, subtitle burn-in, encoding | Yes |
| **ElevenLabs API** | AI voiceover generation | Optional |
| **paw-cra-agent-strategist** | Script writing (invoked on-demand when no script provided) | Optional |

## Platform Specifications

| Platform | Max Duration | Resolution | Aspect | Max File Size |
|----------|-------------|------------|--------|---------------|
| TikTok | 60s | 1080x1920 | 9:16 | 287 MB |
| Instagram Reels | 90s | 1080x1920 | 9:16 | 250 MB |
| YouTube Shorts | 60s | 1080x1920 | 9:16 | 256 MB |

## Memory

**Reads:**
- `{project-root}/.pawbytes/creative-suites/index.md` -- active brands, campaigns
- `{project-root}/.pawbytes/creative-suites/brands/{brand}/guidelines.md` -- brand identity
- `{project-root}/.pawbytes/creative-suites/brands/{brand}/campaigns/{campaign}/brief.md` -- campaign brief
- `{project-root}/.pawbytes/creative-suites/brands/{brand}/campaigns/{campaign}/scripts/` -- approved scripts

**Writes:**
- `{project-root}/.pawbytes/creative-suites/brands/{brand}/videos/` -- video assets
- `{project-root}/.pawbytes/creative-suites/brands/{brand}/videos/video-manifest.json` -- manifest
- `{project-root}/.pawbytes/creative-suites/daily/{YYYY-MM-DD}.md` -- activity log
