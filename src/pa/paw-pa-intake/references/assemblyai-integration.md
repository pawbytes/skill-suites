# AssemblyAI Integration

Audio and video briefs transcribe through AssemblyAI. The LLM extracts structured fields; the script handles upload, polling, and sidecar formatting.

## Prerequisites

- `assemblyai_api_key` in config **or** passed at runtime / `--api-key` flag
- Python 3.9+ (stdlib HTTP — no `assemblyai` package required for the helper script)
- Network access to `api.assemblyai.com`

**Runtime fallback:** If the key is missing and input is audio/video, stop and say:

> Paste your AssemblyAI API key (get one at assemblyai.com), or skip transcription and paste the transcript text instead.

Never fail silently. Never write `brief.md` from a failed transcription without user-provided text.

## When to use the script

Use `scripts/transcribe.py` for local files and public URLs. The skill agent runs it; the agent does the extraction afterward.

```bash
python3 scripts/transcribe.py \
  --api-key "$ASSEMBLYAI_API_KEY" \
  --input "/path/to/call-recording.m4a" \
  --out "{run-folder}/transcript.md" \
  --json-out "{run-folder}/transcript.json"
```

Optional flags:

| Flag | Purpose |
|------|---------|
| `--speakers N` | `speakers_expected` hint when known |
| `--language en` | Force language code (default: auto-detect) |
| `--poll-interval 3` | Seconds between status polls (default 3) |
| `--timeout 600` | Max wait seconds (default 600) |

Stdout JSON on success: `{"ok": true, "transcript_id": "...", "md": "...", "json": "..."}`

## Transcription config (via script)

The helper submits with:

- `speaker_labels: true` — diarization
- `language_detection: true` — unless `--language` set
- `speech_models: ["universal-2"]` — stable default

Chapters are included in JSON when the API returns them; the markdown sidecar lists them under `## Chapters`.

## Sidecar: `transcript.md`

Format written by the script (agent may append extraction notes below the fold):

```markdown
# Transcript

- **Source:** `audio:/path/to/file.m4a`
- **Transcript ID:** `abc123`
- **Duration:** 1842 ms → formatted as MM:SS
- **Language:** en
- **Speakers:** 2

## Diarized transcript

[00:00:12] **Speaker A:** Thanks for joining today...
[00:00:45] **Speaker B:** We're looking for a mobile rebuild...

## Chapters

| Start | Headline | Summary |
|-------|----------|---------|
| 00:00 | Introduction | ... |

## Full text

{Plain concatenated text for quick search}
```

**Agent responsibility after transcription:**

1. Read `transcript.md` (and optionally `transcript.json` for precise timestamps).
2. Extract brief fields per `brief-schema.md` — do **not** paste the diarized block into `brief.md`.
3. Set `sourceInputRef` to `audio:{path}`, `video:{path}`, or `url:{url}`.

## Supported inputs

| Input | Handling |
|-------|----------|
| Local audio | Upload via `POST /v2/upload` then transcribe |
| Local video | Same upload path (AssemblyAI extracts audio) |
| `https://` URL | Pass URL directly as `audio_url` |
| `http://` URL | Allowed; warn if not TLS |

## Error handling

| Error | Action |
|-------|--------|
| 401 / invalid key | Ask user to verify key; offer manual paste |
| Upload failure | Retry once; then manual paste |
| `status: error` on poll | Show API error message; manual paste |
| Timeout | Offer to increase `--timeout` or paste partial notes |
| File not found | Ask for correct path |

## Security

- Never write the API key into `brief.md`, `transcript.md`, or daily logs.
- Do not commit `transcript.json` to public repos if it contains sensitive client speech (warn user).

## Manual transcript path

When skipping AssemblyAI:

1. User pastes transcript text (with or without speaker labels).
2. Write `{run-folder}/transcript.md` manually with header `Source: text:manual-paste`.
3. Proceed with extraction as text intake.

## Alternative: AssemblyAI Python SDK

Power users may install `assemblyai` and transcribe outside the helper. The sidecar format above still applies so downstream tools stay consistent. The bundled script avoids an extra dependency.
