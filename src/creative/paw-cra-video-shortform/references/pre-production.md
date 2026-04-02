# Pre-Production (Steps 1-4)

This phase takes raw input and produces a confirmed storyboard ready for scene generation.

## Step 1: Brief Intake

Parse the incoming brief. Extract and validate these fields:

| Field | Required | Default | Notes |
|-------|----------|---------|-------|
| topic/concept | Yes | -- | What the video is about |
| duration | Yes | 30s | 15-60 seconds |
| platform | Yes | TikTok | TikTok, Reels, or Shorts |
| brand | Yes | `{default_brand}` | Must have guidelines in memory |
| style/tone | No | Infer from brand | Energetic, calm, dramatic, etc. |
| script | No | -- | If provided, skip Step 2 |
| storyboard | No | -- | If provided, skip Steps 2-3 |
| voiceover | No | false | Whether to include AI voiceover |
| music_style | No | -- | Background music direction |

If the brief is incomplete, ask for missing required fields (interactive) or fail with a clear error listing what is needed (headless).

## Step 2: Script Check

**If a script was provided** -- validate it fits the target duration. A rough guide: 2-3 words per second for voiceover-driven content, fewer for visual-driven. If it runs long, suggest cuts. Use it directly.

**If no script was provided** -- two paths:

1. **Invoke Strategist (recommended for campaigns):** Call `paw-cra-agent-strategist` in headless mode with the brief context and request a short-form video script. The Strategist will produce a script with hook, body, and CTA structure optimized for the target platform.

2. **Generate inline (for quick tasks):** If the user declines Strategist involvement or this is a simple concept, draft a minimal script structure: hook (first 3s), body (middle), CTA/closer (last 3-5s).

**In headless mode:** If no script is provided, generate inline -- do not invoke Strategist unless explicitly requested in the brief.

## Step 3: Storyboard Planning

Break the script into 3-8 discrete scenes. For each scene, define:

| Field | Description |
|-------|-------------|
| scene_number | Sequential (1-N) |
| duration | Seconds allocated to this scene |
| visual_description | What the viewer sees -- specific, concrete, prompt-ready |
| camera/motion | Camera movement or visual transition style |
| text_overlay | Any on-screen text for this scene |
| audio_note | Voiceover line, music cue, or SFX |

**Scene count guidance:**
- 15s video: 3-4 scenes
- 30s video: 4-6 scenes
- 60s video: 6-8 scenes

**First scene is critical** -- it must hook within 1-3 seconds. Design the visual to stop the scroll: bold motion, surprising image, direct eye contact, or pattern interrupt.

Present the storyboard for user approval. In headless mode, auto-approve and proceed.

## Step 4: Brand Context Load

Load brand guidelines from `{project-root}/.pawbytes/creative-suites/brands/{brand}/guidelines.md`. Extract and apply to all subsequent generation:

- **Colors** -- use brand palette in text overlays and any generated graphics
- **Typography** -- font family and weights for subtitle styling
- **Visual style** -- photography style, aesthetic direction
- **Voice/tone** -- influences script delivery and visual mood

If brand guidelines do not exist, warn the user and proceed with neutral defaults. Suggest running brand onboarding through Aria (`paw-cra-agent-creative-director`).

## Progression Gate

Before moving to Production, confirm:
- Script exists and fits duration
- Storyboard has 3-8 scenes with visual descriptions
- Brand context is loaded (or defaults acknowledged)
- All scene durations sum to approximately the target duration

In interactive mode, present the storyboard summary and ask for approval. In headless mode, validate programmatically and proceed.
