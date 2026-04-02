# Production (Steps 5-8)

This phase generates the raw video scenes, audio, assembles them into a single video, and burns in subtitles.

## Step 5: Scene Generation

For each scene in the storyboard, generate a video clip using AI video generation.

### Tool Selection

Use egaki CLI as the primary interface to fal.ai video models:

| Model | Best For | Duration | Command Pattern |
|-------|----------|----------|-----------------|
| **Veo 3.1** | Realistic scenes, complex motion, natural lighting | 5-8s per clip | `egaki video --model veo-3.1 --prompt "{visual_description}" --duration {seconds} --aspect-ratio 9:16` |
| **Kling v3** | Stylized content, character animation, creative looks | 5-10s per clip | `egaki video --model kling-v3 --prompt "{visual_description}" --duration {seconds} --aspect-ratio 9:16` |

**Model selection logic:**
- Default to Veo 3.1 for realistic/professional content
- Use Kling v3 for stylized, animated, or creative content
- Respect user preference if specified in the brief

### Prompt Engineering for Video Generation

Each scene's `visual_description` from the storyboard becomes the generation prompt. Enhance it with:

- **Camera direction** -- "slow zoom in", "tracking shot left to right", "static close-up"
- **Lighting** -- "golden hour lighting", "studio lit", "dramatic shadows"
- **Style anchors** -- from brand guidelines (e.g., "clean minimalist aesthetic", "vibrant street style")
- **Aspect ratio** -- always 9:16 for short-form vertical
- **Negative prompts** -- "no text, no watermark, no UI elements" (unless text overlay is intentional)

### Generation Workflow

For each scene:

1. Construct the prompt from storyboard + brand context
2. Run egaki CLI with the selected model
3. Verify the output clip exists and is playable
4. If generation fails, retry once with a simplified prompt. If still failing, log the error and continue with remaining scenes.

Save clips to a temporary working directory: `{project-root}/.pawbytes/creative-suites/brands/{brand}/videos/.work/{timestamp}/`

Name clips sequentially: `scene-01.mp4`, `scene-02.mp4`, etc.

### Image-to-Video Alternative

If the user provides reference images for any scene, use image-to-video mode:

```
egaki video --model veo-3.1 --image {path} --prompt "{motion_description}" --duration {seconds} --aspect-ratio 9:16
```

## Step 6: Audio / Voiceover

**If voiceover is requested:**

Generate voiceover using ElevenLabs API. For each scene that has a voiceover line in the storyboard:

```bash
curl -X POST "https://api.elevenlabs.io/v1/text-to-speech/{voice_id}" \
  -H "xi-api-key: {elevenlabs_api_key}" \
  -H "Content-Type: application/json" \
  -d '{"text": "{voiceover_line}", "model_id": "eleven_multilingual_v2"}' \
  --output "{work_dir}/vo-scene-{N}.mp3"
```

Voice selection: Use a voice that matches the brand tone. If no voice preference exists, use a clear, neutral voice appropriate for the platform audience.

**If background music is requested:**

Note the music direction from the brief. Music sourcing options:
- User-provided audio file
- Stock music from Pexels (if available)
- Generation via external music tools (if available)

Save audio assets to the working directory alongside scene clips.

**If neither voiceover nor music is needed,** proceed directly to assembly.

## Step 7: Assembly

Use ffmpeg to assemble all scene clips into a single video with transitions and audio.

### Concatenation with Transitions

For smooth scene transitions, use ffmpeg's xfade filter. Standard approach for N scenes:

```bash
ffmpeg -i scene-01.mp4 -i scene-02.mp4 -i scene-03.mp4 \
  -filter_complex \
  "[0][1]xfade=transition=fade:duration=0.3:offset={scene1_duration-0.3}[v01]; \
   [v01][2]xfade=transition=fade:duration=0.3:offset={cumulative-0.3}[vout]" \
  -map "[vout]" -c:v libx264 -pix_fmt yuv420p assembled.mp4
```

**Transition guidance:**
- Default transition: `fade` (0.2-0.5s) -- universally safe
- Fast-paced content: `wipeleft` or `slideright` (0.2s)
- Dramatic content: `fade` (0.5s)
- Keep transitions consistent throughout the video
- Account for transition overlap in total duration calculation

### Audio Overlay

If voiceover or music exists, overlay onto the assembled video:

```bash
ffmpeg -i assembled.mp4 -i voiceover.mp3 -i music.mp3 \
  -filter_complex \
  "[1]volume=1.0[vo]; [2]volume=0.3[bg]; [vo][bg]amix=inputs=2[aout]" \
  -map 0:v -map "[aout]" -c:v copy -c:a aac -shortest with-audio.mp4
```

If only voiceover: mix at full volume.
If only music: mix at appropriate level (typically 0.4-0.6).
If both: voiceover at 1.0, music ducked to 0.2-0.3.

## Step 8: Subtitle Generation

Generate and burn in subtitles for accessibility and engagement. Short-form video subtitles are a critical engagement driver -- most viewers watch with sound off.

### Subtitle Creation

If a script/voiceover exists, use it as the subtitle source. Time-align subtitles to match scene boundaries from the storyboard.

Generate an SRT file with these constraints:
- Maximum 2 lines per subtitle
- Maximum 35 characters per line
- Minimum 1 second display duration
- No subtitle should span a scene transition

### Subtitle Burn-In with ffmpeg

```bash
ffmpeg -i with-audio.mp4 \
  -vf "subtitles=subs.srt:force_style='FontName={brand_font},FontSize=22,PrimaryColour=&HFFFFFF,OutlineColour=&H000000,Outline=2,Shadow=1,Alignment=2,MarginV=120'" \
  -c:v libx264 -preset medium -crf 18 -pix_fmt yuv420p \
  -c:a copy subtitled.mp4
```

**Subtitle styling rules:**
- Position in the lower-third safe zone (MarginV=100-150px from bottom)
- Use brand font if available, otherwise use a clean sans-serif (Arial, Montserrat)
- White text with black outline for readability against any background
- Font size: 20-24px for 1080px width
- Bold weight for emphasis words (if supported)

**Safe zone consideration:** Keep subtitles above the platform UI overlay zones:
- TikTok: bottom 150px reserved for UI
- Reels: bottom 120px reserved
- Shorts: bottom 100px reserved

## Working Files

All intermediate files live in `{work_dir}`. At the end of production, the working directory contains:
- `scene-01.mp4` through `scene-N.mp4` -- raw clips
- `voiceover.mp3` / `music.mp3` -- audio (if generated)
- `assembled.mp4` -- concatenated video
- `with-audio.mp4` -- video with audio overlay
- `subs.srt` -- subtitle file
- `subtitled.mp4` -- final video with burned subtitles

The `subtitled.mp4` is the candidate for validation.
