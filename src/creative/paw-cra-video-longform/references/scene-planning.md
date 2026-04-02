# Scene Planning

## Purpose

Transform a script into a concrete scene plan that drives all downstream production -- generation, B-roll, assembly, and timing.

## Scene Breakdown Process

Read the full script and identify natural scene boundaries based on:
- Topic shifts or narrative beats
- Location/setting changes
- Speaker or perspective changes
- Visual mood transitions

For a 1-minute video, expect 3-8 scenes. For 10 minutes, expect 25-40+ scenes. Each scene should be 5-30 seconds to keep visual interest high.

## Scene Plan Structure

For each scene, define:

```json
{
  "scene_id": "s01",
  "description": "Brief description of what happens",
  "visual_approach": "ai_generated | stock | motion_graphic | hybrid",
  "prompt_direction": "Detailed visual description for AI generation",
  "camera": "static | slow_pan_right | zoom_in | tracking | aerial",
  "duration_seconds": 8,
  "transition_to_next": "crossfade | cut | xfade | fade_to_black",
  "voiceover_text": "The narration for this scene...",
  "broll_keywords": ["keyword1", "keyword2"],
  "broll_needed": false,
  "overlay_text": null
}
```

## Visual Approach Selection

- **AI-Generated:** Use for unique, specific scenes that stock footage cannot cover. Hero moments, abstract concepts, branded environments.
- **Stock Footage:** Use for generic establishing shots, cityscapes, nature, people in everyday settings. Faster and often more realistic than AI for common subjects.
- **Motion Graphics:** Use for data/stats displays, text animations, process diagrams, branded transitions.
- **Hybrid:** AI-generated background with text/graphic overlay, or stock footage with branded lower third.

## Pacing Guidelines

- **Opening hook:** First 5-10 seconds must grab attention -- start with the most compelling visual or statement
- **Educational content:** Alternate between talking-head-style scenes and visual demonstrations every 15-30 seconds
- **Narrative content:** Follow story beats -- setup, tension, resolution with visual variety
- **Promotional content:** Keep cuts faster (5-10 second scenes), build energy toward CTA

## Transition Strategy

- **Cuts** for same-topic scene changes (fast, keeps energy)
- **Crossfade** (0.5-1s) for topic transitions or time passage
- **xfade** effects for stylistic transitions (wipe, slide, fade)
- **Fade to black** only for major section breaks or ending

## Output

Write the scene plan as `scene-plan.json` to the video's working directory. This file is the single source of truth for all downstream stages.
