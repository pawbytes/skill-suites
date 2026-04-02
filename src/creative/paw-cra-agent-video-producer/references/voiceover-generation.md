# Voiceover Generation

## Outcome

Generate natural-sounding AI voiceover from script text using ElevenLabs, properly timed and mixed for video production.

## Trigger

User requests voiceover, narration, AI voice, or text-to-speech for video content.

## Inputs Required

| Input | Source | Required |
|-------|--------|----------|
| Script text | User, Strategist, or campaign scripts | Yes |
| Voice preference | User selection or ElevenLabs voice ID | Optional |
| Tone/speed direction | User preference | Optional |

## Prerequisites

- `elevenlabs_api_key` must be configured in `{project-root}/.pawbytes/config/config.user.yaml` under `cra` section
- If no API key is available, inform user and suggest alternatives (manual recording, different TTS service)

## Process

### 1. Voice Selection

If no voice is specified, recommend based on content type:
- **Professional/corporate:** Clear, neutral, authoritative voice
- **Casual/social:** Warm, conversational, energetic voice
- **Educational:** Calm, measured, trustworthy voice

Use ElevenLabs voice library to find appropriate options. Present 2-3 voice samples for user approval when possible.

### 2. Script Preparation

Prepare the script for TTS:
- Break into natural paragraphs/segments aligned with video scenes
- Add pronunciation guides for unusual words or brand names
- Include pause markers for dramatic effect or scene transitions
- Estimate duration (average 150 words per minute for natural speech)

### 3. Generation

Generate voiceover via ElevenLabs API:
- Use the Text-to-Speech endpoint with selected voice
- Set stability and similarity parameters based on content needs
- Generate segment by segment for scene-aligned timing control
- Download audio files to working directory

### 4. Post-Processing

Prepare voiceover for video integration:
- Normalize audio levels to -14 LUFS (broadcast standard)
- Remove leading/trailing silence
- Apply gentle compression for consistent volume
- Export as WAV (for assembly) or MP3 (for preview)

## Output

**Format:** WAV (16-bit, 44.1kHz) for production, MP3 for preview
**Location:** `.pawbytes/creative-suites/brands/{brand}/videos/{campaign}/audio/`
**Naming:** `vo_{scene-or-segment}_{date}.wav`

Also generate a transcript file (`voiceover-transcript.txt`) with timestamps for subtitle generation.

## Integration

Voiceover output feeds directly into:
- **Video Assembly** -- as the primary audio track
- **Subtitle Burn-in** -- transcript used to generate subtitle timing
- **Long-Form Video** -- voiceover drives scene timing

## Escalation

If ElevenLabs API is unavailable, suggest alternative approaches: manual voice recording with a microphone, or browser-based TTS services. Always ensure the video can still be produced without voiceover (subtitles become even more critical).
