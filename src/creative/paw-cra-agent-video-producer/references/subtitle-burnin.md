# Subtitle Burn-in

## Outcome

Add styled, burned-in subtitles to any video for accessibility and engagement -- matching platform conventions and brand aesthetics.

## Trigger

User requests subtitles, captions, or wants to add text to video. Also triggered as a mandatory step in every video production pipeline.

## Inputs Required

| Input | Source | Required |
|-------|--------|----------|
| Video file | Production pipeline or user provided | Yes |
| Transcript or subtitle file | Voiceover transcript, SRT, or manual | Yes |
| Style preference | User or platform convention | Optional |

## Subtitle Styles

### Short-Form Style (TikTok, Reels, Shorts)

The high-engagement subtitle format for vertical video:

- **Position:** Center of frame, lower third (Y offset ~70% from top)
- **Font:** Bold sans-serif (e.g., Montserrat Bold, Inter Bold)
- **Size:** 48-56px for 1080x1920
- **Color:** White with brand accent highlight
- **Effect:** Word-level highlight -- current spoken word changes to brand accent color
- **Background:** Optional semi-transparent dark pill behind text, or drop shadow
- **Max words per line:** 3-4
- **Alignment:** Center

### Long-Form Style (YouTube, Web)

Clean, readable subtitles for horizontal video:

- **Position:** Bottom center with 80px margin from bottom edge
- **Font:** Clean sans-serif (e.g., Inter, Roboto)
- **Size:** 36-42px for 1920x1080
- **Color:** White
- **Background:** Semi-transparent dark box (#000000 at 60% opacity)
- **Max characters per line:** 42
- **Max lines:** 2
- **Alignment:** Center

### Minimal Style

For cinematic or premium content:

- **Position:** Bottom center
- **Font:** Light sans-serif
- **Size:** 32-36px
- **Color:** White with slight text shadow
- **Background:** None (text shadow only)
- **Timing:** Sentence-level display

## Process

### 1. Subtitle Source

Determine where subtitles come from:
- **Voiceover transcript** -- use timestamps from TTS generation
- **Existing SRT/VTT file** -- parse and apply
- **Manual transcript** -- generate timing using audio analysis
- **Auto-transcription** -- use whisper or similar if no transcript exists

### 2. Timing Alignment

Ensure subtitle timing matches audio:
- Each subtitle segment aligns with spoken words
- No subtitle displays during silence
- Word-level timing for highlight style requires per-word timestamps

### 3. Burn-in via ffmpeg

Use ffmpeg's subtitle filter for burning in:

**From SRT file:**
```
ffmpeg -i input.mp4 -vf "subtitles=subs.srt:force_style='FontName=Montserrat Bold,FontSize=48,PrimaryColour=&HFFFFFF,OutlineColour=&H40000000,BorderStyle=3,Outline=2,Shadow=0,Alignment=2,MarginV=150'" -c:a copy output.mp4
```

**From ASS file (for styled subtitles):**
```
ffmpeg -i input.mp4 -vf "ass=subs.ass" -c:a copy output.mp4
```

For word-level highlight style, generate ASS subtitle file with per-word color transitions.

### 4. Validation

- [ ] Subtitles readable at intended viewing size (phone screen for short-form)
- [ ] No text cut off by platform UI elements (check safe zones)
- [ ] Timing synced with audio -- no early/late display
- [ ] Consistent styling throughout video
- [ ] No overlapping subtitle segments

## Output

Video file with burned-in subtitles, replacing or alongside the source video. Subtitle source file (SRT or ASS) preserved alongside for future editing.

## Integration

This capability is called as the final processing step in both Short-Form Video and Long-Form Video pipelines. It runs after assembly and before final encoding.
