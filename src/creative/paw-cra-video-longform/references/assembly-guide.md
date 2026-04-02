# Assembly Guide

## Purpose

Combine all produced assets -- scene clips, voiceover, B-roll, music, overlays -- into a finished video using ffmpeg.

## Assembly Pipeline

### Step 1: Normalize Scene Clips

Ensure all clips have consistent properties before concatenation:

```bash
# Normalize each clip to 1920x1080, 30fps, H.264
ffmpeg -i scene_01.mp4 \
  -vf "scale=1920:1080:force_original_aspect_ratio=decrease,pad=1920:1080:(ow-iw)/2:(oh-ih)/2" \
  -r 30 -c:v libx264 -preset medium -crf 18 \
  -an \
  scene_01_norm.mp4
```

### Step 2: Apply Transitions

For simple cuts, use concat demuxer:

```bash
# Create concat list
echo "file 'scene_01_norm.mp4'" > concat_list.txt
echo "file 'scene_02_norm.mp4'" >> concat_list.txt
# ...

ffmpeg -f concat -safe 0 -i concat_list.txt -c copy assembled_raw.mp4
```

For crossfade transitions between scenes:

```bash
# Crossfade between two clips (1 second transition)
ffmpeg -i scene_01_norm.mp4 -i scene_02_norm.mp4 \
  -filter_complex "xfade=transition=fade:duration=1:offset=7" \
  -c:v libx264 -preset medium -crf 18 \
  transition_01_02.mp4
```

For complex multi-scene assembly with varying transitions, chain xfade filters:

```bash
ffmpeg -i s01.mp4 -i s02.mp4 -i s03.mp4 \
  -filter_complex \
  "[0][1]xfade=transition=fade:duration=0.5:offset=7[v01]; \
   [v01][2]xfade=transition=wipeleft:duration=0.5:offset=14[vout]" \
  -map "[vout]" -c:v libx264 -preset medium -crf 18 \
  assembled.mp4
```

### Step 3: Audio Mixing

Layer voiceover as primary audio, with optional background music:

```bash
# Voiceover only
ffmpeg -i assembled.mp4 -i full_voiceover.wav \
  -c:v copy -c:a aac -b:a 192k \
  -map 0:v:0 -map 1:a:0 \
  assembled_with_vo.mp4

# Voiceover + background music (music at -20dB)
ffmpeg -i assembled.mp4 -i full_voiceover.wav -i background_music.mp3 \
  -filter_complex \
  "[1:a]volume=1.0[vo]; \
   [2:a]volume=0.1[music]; \
   [vo][music]amix=inputs=2:duration=first[aout]" \
  -map 0:v:0 -map "[aout]" \
  -c:v copy -c:a aac -b:a 192k \
  assembled_with_audio.mp4
```

### Step 4: Overlay Graphics

Add lower thirds, watermarks, or on-screen text:

```bash
# Brand watermark (bottom-right corner, semi-transparent)
ffmpeg -i assembled_with_audio.mp4 -i brand_logo.png \
  -filter_complex "overlay=W-w-20:H-h-20:format=auto,format=yuv420p" \
  -c:v libx264 -preset medium -crf 18 -c:a copy \
  assembled_branded.mp4
```

## Common Transition Types

| Transition | ffmpeg xfade name | Best For |
|-----------|-------------------|----------|
| Fade | `fade` | Topic changes, gentle transitions |
| Dissolve | `dissolve` | Similar to fade, smoother blend |
| Wipe Left | `wipeleft` | Sequential/progressive content |
| Wipe Right | `wiperight` | Flashback or reversal |
| Slide Left | `slideleft` | Modern, dynamic feel |
| Circle Open | `circleopen` | Dramatic reveals |

## Checkpoint Recovery

After assembly, save the intermediate video as a checkpoint. If later stages fail (subtitles, intro/outro), resume from this checkpoint rather than re-assembling from scratch.

## Output

The assembled video with audio should be saved as `assembled_final.mp4` in the working directory, ready for subtitle burn-in and intro/outro addition.
