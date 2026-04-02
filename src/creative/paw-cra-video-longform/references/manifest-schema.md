# Video Manifest Schema

## Purpose

The `video-manifest.json` file is the machine-readable record of a produced video. It enables downstream workflows (quality control, multi-platform export, campaign orchestration) to understand what was produced without re-inspecting the video file.

## Schema

```json
{
  "version": "1.0",
  "type": "longform",
  "brand": "brand-name",
  "campaign": "campaign-name or null",
  "video": {
    "title": "Video Title",
    "slug": "video-slug",
    "description": "Brief description",
    "duration_seconds": 180,
    "resolution": "1920x1080",
    "codec": "H.264",
    "audio_codec": "AAC",
    "framerate": 30,
    "file_size_mb": 45.2,
    "file_path": "relative/path/to/video.mp4"
  },
  "production": {
    "scene_count": 15,
    "ai_generated_scenes": 10,
    "stock_footage_scenes": 3,
    "motion_graphic_scenes": 2,
    "voiceover_voice_id": "elevenlabs-voice-id",
    "voiceover_model": "eleven_multilingual_v2",
    "video_models_used": ["veo-3.1", "kling-v3"],
    "background_music": true,
    "subtitles": true,
    "intro_included": true,
    "outro_included": true
  },
  "files": {
    "video": "video-slug.mp4",
    "subtitles": "subtitles.srt",
    "thumbnail": "thumbnail.jpg",
    "scene_plan": "scene-plan.json"
  },
  "validation": {
    "passed": true,
    "checks": {
      "resolution": "pass",
      "codec": "pass",
      "duration": "pass",
      "audio_levels": "pass"
    },
    "validated_at": "2026-04-01T12:00:00Z"
  },
  "episodic": {
    "is_episode": false,
    "series_slug": null,
    "episode_number": null,
    "total_episodes": null
  },
  "created_at": "2026-04-01T12:00:00Z",
  "workflow": "paw-cra-video-longform"
}
```

## Required Fields

All top-level fields are required. Within `episodic`, fields are null for single (non-episodic) videos.

## Series Manifest

For episodic content, a series-level manifest is also generated at the series root:

```json
{
  "version": "1.0",
  "type": "series",
  "series_slug": "series-name",
  "brand": "brand-name",
  "total_episodes": 5,
  "episodes": [
    {
      "episode_number": 1,
      "title": "Episode 1 Title",
      "manifest_path": "ep01/video-manifest.json"
    }
  ],
  "style_guide": {
    "voice_id": "consistent-voice-id",
    "intro_asset": "path/to/intro",
    "outro_asset": "path/to/outro",
    "color_palette": ["#hex1", "#hex2"]
  },
  "created_at": "2026-04-01T12:00:00Z"
}
```
