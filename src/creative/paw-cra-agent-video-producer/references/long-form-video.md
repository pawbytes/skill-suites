# Long-Form Video

## Outcome

Produce 1-10 minute horizontal videos for YouTube, web embeds, or presentations -- with professional pacing, multi-scene composition, voiceover, and complete subtitle coverage.

## Trigger

User requests a YouTube video, long-form video, explainer video, tutorial, or horizontal video content.

## Inputs Required

| Input | Source | Required |
|-------|--------|----------|
| Script or detailed brief | Brief, Strategist output, or user input | Yes |
| Platform target | User specification (default: YouTube) | Yes |
| Brand guidelines | `.pawbytes/creative-suites/brands/{brand}/guidelines.md` | Yes |
| Duration target | User specification | Yes |
| Voice direction | User preference or ElevenLabs voice ID | Optional |
| B-roll references | User provided or stock footage | Optional |

## Process

### 1. Load Context

- Read brand guidelines for visual style, colors, typography
- Check platform specifications (see `./video-platform-specs.md`)
- Load campaign scripts from `.pawbytes/creative-suites/brands/{brand}/campaigns/{campaign}/scripts/`
- If no script exists, request Strategist support via `paw-cra-agent-strategist`

### 2. Script & Scene Planning

Long-form requires structured scene planning:

- **Introduction** (5-15s) -- hook and topic framing
- **Body sections** -- each major point as a scene group with visual variety
- **Transitions** -- scene-to-scene bridges (visual, audio, or text)
- **Conclusion** (10-20s) -- summary and CTA

Each scene needs: visual description, duration, voiceover text, on-screen text, transition type.

**Pacing guideline:** Long-form scenes run 5-15 seconds each. Alternate between talking-head style, B-roll, text cards, and motion graphics to maintain visual interest. Never let a single visual hold for more than 15 seconds without a cut or overlay change.

### 3. Voiceover Production

Long-form videos typically need continuous voiceover:

1. Generate full voiceover via ElevenLabs API (see `./voiceover-generation.md`)
2. Split into scene-aligned segments or generate as one continuous track
3. Time scenes to match voiceover pacing
4. Export voiceover transcript for subtitle generation

### 4. Scene Generation

Generate visuals for each scene:

- Use AI video generation for primary scenes (Veo 3.1 for cinematic quality)
- Generate motion graphics for title cards, transitions, data visualizations
- Source B-roll for supplementary footage if available
- Ensure visual consistency across all scenes (color palette, style, lighting)

### 5. Assembly

Build the complete video with ffmpeg:

- Concatenate scenes in script order with specified transitions
- Sync voiceover to visual timeline
- Layer background music with proper ducking (reduce by 12-18dB under voiceover)
- Add lower thirds, title cards, and text overlays at scripted timestamps
- Apply intro and outro sequences
- Normalize audio to broadcast standards (-14 LUFS integrated)

### 6. Subtitle Burn-in

Burn subtitles from voiceover transcript. See `./subtitle-burnin.md`.

Default long-form subtitle style:
- **Position:** Bottom center with safe margin
- **Font:** Clean sans-serif, 36-42px
- **Style:** Sentence-level display (2-3 words per line max)
- **Background:** Semi-transparent dark box for readability over varied backgrounds

### 7. Final Encoding & Validation

| Platform | Resolution | Codec | Bitrate | FPS |
|----------|-----------|-------|---------|-----|
| YouTube | 1920x1080 | H.264 High | 10-16 Mbps | 30 |
| Web Embed | 1920x1080 | H.264 Main | 8-12 Mbps | 30 |
| LinkedIn | 1920x1080 | H.264 Main | 8-10 Mbps | 30 |

**Validation checklist:**
- [ ] Resolution is 1920x1080 (or 3840x2160 for 4K)
- [ ] Duration matches script target
- [ ] Subtitles present and synced to voiceover
- [ ] Audio normalized to -14 LUFS
- [ ] No dropped frames or encoding artifacts
- [ ] Intro and outro present
- [ ] File size reasonable for platform

## Output

**Format:** MP4 (H.264, AAC audio)
**Location:** `.pawbytes/creative-suites/brands/{brand}/videos/{campaign}/long-form/`
**Naming:** `{platform}_{title-slug}_{date}.mp4`
**Manifest:** Write `video-manifest.json` alongside output

## Escalation

If script is missing or incomplete, request Strategist support. For complex multi-segment videos exceeding 10 minutes, break into episodes and use the Episodic Series capability.
