# Voiceover Generation

## Purpose

Generate narration audio that aligns with scene timing using ElevenLabs text-to-speech API.

## Voice Selection

ElevenLabs offers pre-made voices and custom voice cloning. For brand consistency:
- Check if the brand has a designated voice ID in guidelines
- If not, select a voice that matches the brand's tone (professional, conversational, energetic, authoritative)
- Preview 2-3 voice options before committing to full generation (in interactive mode)

## Generation Process

### Per-Scene Generation

Generate voiceover for each scene individually to maintain timing control:

```bash
curl -X POST "https://api.elevenlabs.io/v1/text-to-speech/{voice_id}" \
  -H "xi-api-key: ${ELEVENLABS_API_KEY}" \
  -H "Content-Type: application/json" \
  -d '{
    "text": "Scene narration text here...",
    "model_id": "eleven_multilingual_v2",
    "voice_settings": {
      "stability": 0.5,
      "similarity_boost": 0.75,
      "style": 0.0,
      "use_speaker_boost": true
    }
  }' \
  --output scene_01_vo.mp3
```

### Full-Script Generation

For videos where natural flow across scenes matters more than per-scene timing:

1. Generate the entire narration as one audio file
2. Use silence detection to identify natural breakpoints
3. Split at breakpoints and align to scenes
4. Adjust scene video durations to match voiceover timing

## Timing Alignment

The voiceover drives the video's pacing. When voiceover and scene durations don't match:

- **VO shorter than scene:** Extend the scene clip (loop, slow motion, or hold last frame)
- **VO longer than scene:** Extend scene duration or split into two visual segments
- **Target:** Voiceover should fill 70-85% of each scene's duration, leaving room for breathing space and transitions

## Audio Quality

- Output format: WAV (highest quality) or MP3 at 320kbps minimum
- Sample rate: 44100 Hz or 48000 Hz
- Normalize audio levels to -14 LUFS (podcast/YouTube standard)
- Apply light compression if dynamic range is too wide

```bash
# Normalize audio with ffmpeg
ffmpeg -i scene_01_vo.mp3 -af loudnorm=I=-14:TP=-1.5:LRA=11 scene_01_vo_norm.wav
```

## Output

Save voiceover files alongside scene clips: `scene_01_vo.wav`, `scene_02_vo.wav`, etc. Also save the complete concatenated voiceover as `full_voiceover.wav` for assembly reference.
