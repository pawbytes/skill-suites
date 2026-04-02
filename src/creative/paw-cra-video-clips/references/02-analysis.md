---
name: 02-analysis
description: Analyze source video to identify clip-worthy moments
---

# Step 2: Source Video Analysis

## Outcome

A ranked list of clip-worthy moments from the source video, each with a timecode range and reason for selection.

## Analysis Strategy

Two paths depending on available tools:

### Path A: OpenShorts Available

Use OpenShorts for AI-powered moment detection:
- Viral moment scoring (identifies high-engagement segments)
- Speaker detection (identifies who is on screen)
- Energy/pace analysis

OpenShorts provides richer moment analysis but is optional. Fall back to Path B if unavailable.

### Path B: ffmpeg + LLM Analysis (Default)

Use ffmpeg scene detection to identify visual transitions and energy changes:

```bash
ffmpeg -i "{source}" -filter:v "select='gt(scene,0.3)',showinfo" -f null - 2>&1
```

This identifies scene changes. Combine with:

1. **Audio energy analysis** -- detect loud/energetic segments:
   ```bash
   ffmpeg -i "{source}" -af "astats=metadata=1:reset=1,ametadata=print:key=lavfi.astats.Overall.RMS_level" -f null - 2>&1
   ```

2. **If transcript available** -- analyze text for quotable moments, key points, hooks, and punchlines. Generate transcript using ffmpeg + whisper if available, or accept a provided transcript/SRT file.

3. **LLM judgment** -- given scene boundaries and audio energy peaks, identify the most compelling segments. Consider:
   - **Hook potential** -- does it grab attention in the first 2 seconds?
   - **Self-contained story** -- does the clip make sense without the full video?
   - **Emotional peak** -- high energy, laughter, surprise, insight
   - **Quotability** -- a complete, shareable thought
   - **Visual interest** -- action, gestures, demonstrations

## Candidate Moment Format

For each identified moment, capture:

| Field | Description |
|-------|-------------|
| `moment_id` | Sequential identifier (M01, M02, ...) |
| `start_time` | Timecode (HH:MM:SS.mmm) |
| `end_time` | Timecode |
| `duration` | Seconds |
| `reason` | Why this moment is clip-worthy |
| `energy_score` | High / Medium / Low |
| `suggested_durations` | Which target durations (15s, 30s, 60s) this moment fits |

## Moment Selection

Aim for 2-3x more candidate moments than final clips needed. For a 30-minute source, expect 8-15 candidate moments. Rank by:
1. Hook strength (will it stop the scroll?)
2. Completeness (standalone comprehension)
3. Duration fit (matches target durations without awkward cuts)

## Interactive Gate

If not headless: present the ranked moment list to the user. Allow them to:
- Approve all
- Remove specific moments
- Adjust timecodes
- Add moments they spotted

If headless: proceed with the top-ranked moments.

## Progression

Proceed to `./references/03-clip-production.md` with the approved moment list.
