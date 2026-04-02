# Short-Form Video

## Outcome

Produce 15-60 second vertical videos optimized for TikTok, Instagram Reels, and YouTube Shorts -- capturing attention in the first 2 seconds and driving engagement through pacing, visual hooks, and clear subtitles.

## Trigger

User requests a short-form video, reel, TikTok, YouTube Short, or vertical video content.

## Inputs Required

| Input | Source | Required |
|-------|--------|----------|
| Script or concept | Brief, user input, or Strategist output | Yes |
| Platform target(s) | User specification | Yes |
| Brand guidelines | `.pawbytes/creative-suites/brands/{brand}/guidelines.md` | Yes |
| Duration target | User specification (default: 30s) | Optional |
| Voice/music direction | User preference | Optional |

## Process

### 1. Load Context

- Read brand guidelines for visual style, colors, typography
- Check platform specifications (see `./video-platform-specs.md`)
- Load any campaign scripts from `.pawbytes/creative-suites/brands/{brand}/campaigns/{campaign}/scripts/`
- If no script exists and one is needed, request Strategist support via `paw-cra-agent-strategist`

### 2. Script & Storyboard

Break the concept into scenes. Each scene needs:
- **Visual description** -- what appears on screen (used as AI generation prompt)
- **Duration** -- seconds allocated
- **Text overlay** -- any on-screen text
- **Audio** -- voiceover line, music cue, or SFX
- **Transition** -- how this scene connects to the next

**Pacing guideline:** Short-form videos need a visual hook in the first 1-2 seconds. Cut rhythm should be 3-5 seconds per scene for high engagement.

### 3. Scene Generation

Generate each scene clip using AI video generation:

1. Build scene prompts using brand visual style as context
2. Generate via fal.ai (Veo 3.1 or Kling v3) or egaki CLI
3. Download clips to working directory
4. Review clip quality -- regenerate if motion artifacts or style inconsistencies

See `./ai-video-models.md` for model selection and CLI commands.

### 4. Audio Production

- **Voiceover:** If scripted, generate via ElevenLabs API (see `./voiceover-generation.md`)
- **Music:** Apply background music with proper ducking under voiceover
- **SFX:** Add sound effects for transitions or emphasis

### 5. Assembly

Combine all elements with ffmpeg:
- Concatenate scene clips with specified transitions (crossfade, cut, wipe)
- Overlay text elements at specified timestamps
- Mix audio tracks (voiceover primary, music secondary, SFX accent)
- Apply color grading for brand consistency

### 6. Subtitle Burn-in

Every short-form video requires burned-in subtitles. See `./subtitle-burnin.md` for styling.

Default short-form subtitle style:
- **Position:** Center, lower third
- **Font:** Bold sans-serif, 48-56px
- **Style:** Word-level highlight (current word in brand accent color)
- **Background:** Semi-transparent dark box or no background with text shadow

### 7. Final Encoding & Validation

Encode to platform specifications:

| Platform | Resolution | Codec | Bitrate | FPS |
|----------|-----------|-------|---------|-----|
| TikTok | 1080x1920 | H.264 Main | 6-10 Mbps | 30 |
| Instagram Reels | 1080x1920 | H.264 Main | 6-10 Mbps | 30 |
| YouTube Shorts | 1080x1920 | H.264 Main | 8-12 Mbps | 30 |

**Validation checklist:**
- [ ] Resolution matches target platform
- [ ] Duration within platform limits
- [ ] Subtitles present and readable
- [ ] Audio levels normalized (-14 LUFS)
- [ ] No black frames at start/end
- [ ] File size within platform limits

## Output

**Format:** MP4 (H.264, AAC audio)
**Location:** `.pawbytes/creative-suites/brands/{brand}/videos/{campaign}/short-form/`
**Naming:** `{platform}_{concept-slug}_{date}.mp4`
**Manifest:** Write `video-manifest.json` alongside output (see `./production-standards.md`)

## Escalation

If script or copy is missing, request Strategist support via `paw-cra-agent-strategist`. If brand guidelines lack video-specific direction (motion style, pacing preferences), recommend defaults and confirm with user.
