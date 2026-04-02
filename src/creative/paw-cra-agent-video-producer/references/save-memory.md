# Save Memory

## Purpose

Persist important context, user preferences, and session learnings to the shared agency memory.

## When to Save

Trigger this capability when:
- Video production run completes (write manifest)
- User provides video style preferences (subtitle style, pacing, voice)
- Campaign brief is referenced or updated
- Production decisions are confirmed (voice selection, transition style, music)
- Patterns in user preferences are noticed

## Memory Locations

**Shared Agency Memory:** `.pawbytes/creative-suites/`

| File | Purpose | When to Update |
|------|---------|----------------|
| `index.md` | Active brands, campaigns, status | When context changes |
| `brands/{brand}/videos/video-manifest.json` | Production run metadata | After every video production |
| `brands/{brand}/campaigns/{campaign}/videos/` | Campaign video assets | After campaign video production |
| `daily/{YYYY-MM-DD}.md` | Activity log | After each significant action |

## Save Process

1. Determine what needs to be saved (video output, preferences, decisions)
2. Identify correct memory file
3. Read existing content
4. Update with new/changed information
5. Write updated file
6. Log activity to daily file

## Daily Log Entry Format

```markdown
## {HH:MM} [VideoProducer]
**Task:** {capability type}
**For:** {brand}/{campaign}
**Output:** {file paths}
**Specs:** {resolution}, {duration}s, {codec}, subtitles: {yes/no}
**Notes:** {any relevant notes}
```

## After Saving

Confirm save to user and reference the file location.
