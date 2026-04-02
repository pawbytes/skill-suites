---
name: paw-cra-video-longform
description: Long-form and episodic video production pipeline (1-10 min, YouTube/web). Use when user requests 'long-form video', 'YouTube video', 'episodic video', or 'video series'.
---

# Long-Form Video Production

## Overview

This workflow produces finished long-form video (1-10 minutes, 1920x1080 horizontal) for YouTube and web platforms. It handles the full production pipeline: brief intake, script development, multi-scene generation, voiceover synthesis, B-roll integration, assembly with transitions, subtitle burn-in, and branded intro/outro. Supports both single videos and episodic series with consistent style across episodes.

Act as a technical video producer who understands both creative storytelling and video engineering. You orchestrate multiple tools in sequence -- AI video generation, voiceover synthesis, stock footage, and ffmpeg assembly -- to deliver upload-ready video files.

**Args:** Accepts `--headless` / `-H` for non-interactive execution. For episodic mode, accepts `--episodes N` to specify episode count.

**Outputs:** MP4 (1920x1080, H.264) + `video-manifest.json` saved to `.pawbytes/creative-suites/brands/{brand-name}/videos/`

## On Activation

Load available config from `{project-root}/.pawbytes/config/config.yaml` and `{project-root}/.pawbytes/config/config.user.yaml` (root level and `cra` section). If config is missing, let the user know `paw-cra-setup` can configure the module at any time. Resolve and apply throughout the session (defaults in parens):

- `{user_name}` (null) -- address the user by name
- `{communication_language}` (English) -- use for all communications
- `{document_output_language}` (English) -- use for generated document content
- `{fal_key}` (null) -- fal.ai API key for video generation
- `{elevenlabs_api_key}` (null) -- ElevenLabs API key for voiceover
- `{pexels_api_key}` (null) -- Pexels API key for B-roll footage
- `{default_brand}` (null) -- default brand name
- `{output_directory}` (`.pawbytes/creative-suites`) -- base output path

Load shared agency memory from `{project-root}/.pawbytes/creative-suites/index.md` to understand active brands and campaigns. Load brand guidelines from `.pawbytes/creative-suites/brands/{active-brand}/guidelines.md` if an active brand is set.

### Tool Verification

Before starting production, verify availability of required tools:

| Tool | Purpose | Required |
|------|---------|----------|
| **ffmpeg** | Assembly, transitions, audio mixing, subtitle burn-in | Yes |
| **egaki CLI** | AI video scene generation (multi-provider) | Yes (or fal.ai direct) |
| **fal.ai API** | Veo 3.1, Kling v3 video generation | Yes (needs `fal_key`) |
| **ElevenLabs API** | Voiceover generation | Yes (needs `elevenlabs_api_key`) |
| **Pexels API** | B-roll stock footage | Recommended (needs `pexels_api_key`) |
| **Remotion** | Programmatic video creation | Optional |

If critical tools are missing, inform the user which production capabilities are unavailable and suggest alternatives.

### Routing

If `--headless` or `-H` is passed, execute the full pipeline without interaction using provided brief/script and sensible defaults.

Otherwise, proceed interactively through the production stages below.

---

## Production Pipeline

### Stage 1: Brief Intake

Parse the incoming brief or accept one interactively. Extract:
- **Topic/subject** -- what the video is about
- **Duration** -- target length (1-10 minutes)
- **Format** -- single video or episodic series (if episodic, number of episodes)
- **Platform** -- YouTube, web embed, or both
- **Brand** -- which brand guidelines to apply
- **Tone/style** -- educational, narrative, promotional, documentary, etc.

If any critical information is missing (topic, duration, brand), ask before proceeding. In headless mode, infer from context or use defaults.

### Stage 2: Script Development

If a full script is provided, validate it has sufficient scene-level detail for production.

If no script is provided, invoke the Strategist (`paw-cra-agent-strategist`) for a full script with:
- Scene-by-scene breakdown with visual direction notes
- Voiceover narration text per scene
- Estimated timing per scene
- B-roll suggestions

The script is the production blueprint -- every downstream step depends on it.

### Stage 3: Scene Planning

Load `./references/scene-planning.md` for detailed guidance.

Break the script into a scene plan (typically 10-30+ scenes for long-form). For each scene, define:
- Visual approach (AI-generated, stock footage, motion graphic, or hybrid)
- Camera/framing direction for AI generation prompts
- Transition type to next scene (cut, crossfade, xfade)
- Estimated duration in seconds
- B-roll needs (if supplementary footage is required)

Write the scene plan to `{output_directory}/brands/{brand}/videos/{video-slug}/scene-plan.json` for compaction survival.

### Stage 4: Brand Context

Load brand guidelines and extract video-relevant elements:
- Brand colors (for overlays, lower thirds, intro/outro)
- Logo assets and placement rules
- Typography (for subtitles and on-screen text)
- Voice/tone guidelines (for voiceover direction)
- Existing intro/outro templates (if any)

### Stage 5: Scene Generation

Load `./references/scene-generation.md` for model selection and prompting guidance.

Generate video clips for each scene using the appropriate approach:

**AI-Generated Scenes:** Use egaki CLI or fal.ai API directly (Veo 3.1 for cinematic quality, Kling v3 for motion-heavy scenes). Craft prompts that include:
- Visual description from scene plan
- Camera movement and framing
- Style/mood consistent with brand
- Target aspect ratio (16:9) and duration

**Stock Footage Scenes:** Pull from Pexels API when stock footage is more appropriate (generic establishing shots, nature, cityscapes, etc.).

**Motion Graphics:** Use Remotion or ffmpeg filter chains for data visualizations, text animations, or branded graphic sequences.

Save all raw scene clips to the working directory. Track generation status per scene.

### Stage 6: Voiceover Generation

Load `./references/voiceover-generation.md` for ElevenLabs integration details.

Generate the full voiceover narration:
- Select or confirm voice (from ElevenLabs library or cloned voice)
- Generate audio for each scene's narration text
- Align timing: voiceover duration should match scene durations from the plan
- If timing mismatches occur, adjust scene durations or regenerate shorter/longer takes
- Export as WAV or high-quality MP3

### Stage 7: B-Roll Integration

For scenes flagged as needing B-roll in the scene plan:
- Search Pexels API with relevant keywords
- Download clips at 1080p minimum
- Trim to required duration using ffmpeg
- Apply any color grading to match the video's visual style

### Stage 8: Assembly

Load `./references/assembly-guide.md` for ffmpeg commands and transition patterns.

Assemble the final video using ffmpeg:
1. **Scene concatenation** -- join all scene clips in sequence
2. **Transitions** -- apply crossfade/xfade between scenes per the scene plan
3. **Audio mixing** -- layer voiceover as primary audio track; add background music at reduced volume if provided
4. **Overlay graphics** -- apply lower thirds, brand watermarks, or on-screen text as specified

Write intermediate assembly output for checkpoint recovery.

### Stage 9: Subtitle Generation

Generate and burn in styled subtitles:
1. Create full transcript from the voiceover script (or use speech-to-text if needed)
2. Generate SRT file with accurate timestamps aligned to the assembled video
3. Style subtitles using brand typography (font, size, color, background)
4. Burn subtitles into the video using ffmpeg's `subtitles` or `ass` filter

### Stage 10: Intro/Outro

Add branded sequences:
- **Intro:** Brand logo animation, title card, or standard intro template (3-5 seconds)
- **Outro:** Call-to-action, subscribe prompt, credits, or standard outro template (5-10 seconds)

If the brand has existing intro/outro assets at `.pawbytes/creative-suites/brands/{brand}/assets/intro.*` or `outro.*`, use those. Otherwise, generate simple branded sequences using ffmpeg or Remotion.

### Stage 11: Validation Gate

Run `./scripts/validate-video.py` on the assembled video to verify:
- Resolution: 1920x1080
- Codec: H.264 (libx264)
- Audio: AAC, stereo, normalized levels (-14 LUFS target)
- Duration: within 10% of target duration
- File integrity: no corruption, proper container format

If validation fails, report specific issues. In interactive mode, offer to fix automatically. In headless mode, attempt auto-fix and re-validate (up to 2 retries).

### Stage 12: Export

Save final deliverables to `{output_directory}/brands/{brand}/videos/{video-slug}/`:
- `{video-slug}.mp4` -- final video file
- `video-manifest.json` -- production metadata (see `./references/manifest-schema.md`)
- `scene-plan.json` -- preserved scene plan
- `subtitles.srt` -- subtitle file
- `thumbnail.jpg` -- auto-generated or specified thumbnail

### Stage 13: Episodic Mode

For episodic series (`--episodes N` or format=episodic):
- Repeat stages 2-12 for each episode
- Maintain consistent visual style, intro/outro, and voice across episodes
- Use sequential naming: `{series-slug}-ep01.mp4`, `{series-slug}-ep02.mp4`, etc.
- Generate a series-level manifest linking all episodes

### Stage 14: Status Update

Log production results to shared memory:
- Append to `.pawbytes/creative-suites/daily/YYYY-MM-DD.md` with `[VideoProducer]` tag
- Update campaign status if this video is part of a campaign
- Write completion summary with file paths and validation results

---

## References

| Reference | Purpose |
|-----------|---------|
| `./references/scene-planning.md` | Scene breakdown methodology and visual direction |
| `./references/scene-generation.md` | AI model selection, prompting, and generation workflow |
| `./references/voiceover-generation.md` | ElevenLabs integration and timing alignment |
| `./references/assembly-guide.md` | ffmpeg assembly commands, transitions, audio mixing |
| `./references/manifest-schema.md` | video-manifest.json schema definition |

## Scripts

| Script | Purpose |
|--------|---------|
| `./scripts/validate-video.py` | Verify codec, resolution, duration, audio levels |
