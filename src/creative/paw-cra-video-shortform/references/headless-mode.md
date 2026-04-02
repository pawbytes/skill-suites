# Headless Mode

Headless mode activated. Execute the full short-form video pipeline without user interaction.

## Requirements

The input must contain at minimum:
- **topic** -- what the video is about
- **duration** -- target length in seconds (15-60)
- **platform** -- TikTok, Reels, or Shorts
- **brand** -- brand name (must exist in memory)

Optional but valuable:
- **script** -- pre-written script (skips script generation)
- **storyboard** -- pre-planned scenes (skips storyboard planning)
- **style** -- visual style direction
- **voiceover** -- true/false
- **music_style** -- background music direction

## Execution

1. **Validate inputs** -- if any required field is missing, fail immediately with a clear error listing what is needed
2. **Load brand context** -- if brand does not exist in memory, fail with instructions to run brand onboarding
3. **Verify tools** -- confirm egaki, ffmpeg, and fal_key are available. Fail early if required tools are missing.
4. **Generate script inline** if not provided (do not invoke Strategist in headless unless explicitly requested)
5. **Auto-approve storyboard** -- no user gate
6. **Run full production pipeline** -- scene generation, audio (if requested), assembly, subtitles
7. **Auto-approve validation** -- if all codec checks pass, proceed. If any check fails and cannot be auto-fixed, fail with details.
8. **Export and log** -- write files, manifest, and daily log
9. **Return summary** -- file paths, duration, validation results

## Error Handling

Return structured error output on failure:

```
## Video Failed

**Stage:** {which step failed}
**Error:** {description}
**Required:** {what is needed to fix}
```

## Defaults in Headless Mode

| Decision | Headless Default |
|----------|-----------------|
| Script source | Generate inline |
| Storyboard approval | Auto-approved |
| Generation model | Veo 3.1 |
| Transition style | fade (0.3s) |
| Subtitle font | Arial Bold |
| Validation approval | Auto-approved if all pass |
| Working directory cleanup | Yes |
