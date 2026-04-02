# Video Assembly

## Outcome

Combine multiple video clips, audio tracks, transitions, and overlays into a single cohesive video -- the core composition step in every video production pipeline.

## Trigger

User requests to combine clips, add transitions, merge videos, or assemble a final video from components.

## Inputs Required

| Input | Source | Required |
|-------|--------|----------|
| Video clips | Generated scenes, B-roll, user footage | Yes |
| Clip sequence/order | Storyboard or user specification | Yes |
| Transition preferences | User or default | Optional |
| Audio tracks | Voiceover, music, SFX | Optional |
| Overlay assets | Logos, lower thirds, text cards | Optional |

## Process

### 1. Inventory

Catalog all input assets:
- List all video clips with resolution, duration, codec
- List all audio tracks with duration and type (VO, music, SFX)
- List overlay assets with intended placement and timing
- Verify all clips match target resolution (rescale if not)

### 2. Timeline Construction

Build the assembly timeline:
- Order clips per storyboard/sequence
- Place transitions between clips (type and duration)
- Align voiceover to visual timeline
- Place music track with ducking points
- Position overlays at specified timestamps

### 3. Transitions

Common transitions via ffmpeg xfade filter:

| Transition | Duration | Best For |
|-----------|----------|----------|
| **Cut** | 0s | Fast-paced content, news style |
| **Crossfade (dissolve)** | 0.3-1.0s | General purpose, scene changes |
| **Fade to black** | 0.5-1.0s | Section breaks, dramatic pauses |
| **Wipe** | 0.3-0.5s | Energetic content, before/after |
| **Slide** | 0.3-0.5s | Tutorial steps, list items |

**ffmpeg xfade syntax:**
```
ffmpeg -i clip1.mp4 -i clip2.mp4 -filter_complex \
  "[0][1]xfade=transition=dissolve:duration=0.5:offset={clip1_duration-0.5}" \
  -c:v libx264 -preset medium output.mp4
```

For multi-clip assembly, chain xfade filters or concatenate with the concat demuxer for cut-only assembly.

### 4. Audio Mixing

Layer audio tracks with proper levels:

| Track | Target Level | Processing |
|-------|-------------|-----------|
| **Voiceover** | -14 LUFS | Compression, normalization |
| **Music (under VO)** | -26 to -30 LUFS | Sidechain ducking under VO |
| **Music (no VO)** | -16 to -20 LUFS | Full level during non-speech |
| **SFX** | -18 to -22 LUFS | Spot placement, short duration |

### 5. Overlays

Apply visual overlays via ffmpeg overlay filter:
- **Logo watermark:** Corner placement with padding and opacity
- **Lower thirds:** Position at bottom with fade in/out
- **Text cards:** Full-frame or partial overlay at specified time
- **Brand colors:** Color grade or LUT application for consistency

### 6. Final Render

Export assembled video at target specifications:
- Resolution and aspect ratio per platform
- H.264 encoding with appropriate bitrate
- AAC audio at 128-256 kbps
- Proper metadata tags

## Output

**Format:** MP4 (H.264, AAC)
**Location:** Working directory for pipeline, or `.pawbytes/creative-suites/brands/{brand}/videos/{campaign}/`

## Integration

Video Assembly is the central composition step. It receives inputs from scene generation and voiceover, and its output feeds into subtitle burn-in and final encoding/validation.
