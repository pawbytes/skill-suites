#!/usr/bin/env python3
# /// script
# requires-python = ">=3.9"
# dependencies = []
# ///
"""AssemblyAI transcription helper for paw-pa-intake.

Uploads local audio/video, transcribes remote URLs, polls until complete,
and writes a diarized transcript.md sidecar plus optional JSON dump.

Plumbing only — the LLM performs structured brief extraction afterward.

Usage:
  python transcribe.py --api-key KEY --input PATH_OR_URL --out transcript.md
  python transcribe.py --api-key KEY --input ./call.m4a --out t.md --json-out t.json

Stdout on success: {"ok": true, "transcript_id": "...", "md": "...", "json": "..."}
Stdout on failure: {"ok": false, "error": "..."}  (exit code 1)
"""
from __future__ import annotations

import argparse
import json
import sys
import time
import urllib.error
import urllib.request
from pathlib import Path
from typing import Any

API_BASE = "https://api.assemblyai.com/v2"


def _request(
    method: str,
    path: str,
    api_key: str,
    body: bytes | None = None,
    content_type: str = "application/json",
) -> dict[str, Any]:
    url = f"{API_BASE}{path}"
    headers = {"authorization": api_key}
    if body is not None and content_type:
        headers["content-type"] = content_type
    req = urllib.request.Request(url, data=body, headers=headers, method=method)
    try:
        with urllib.request.urlopen(req, timeout=120) as resp:
            raw = resp.read().decode("utf-8")
            return json.loads(raw) if raw else {}
    except urllib.error.HTTPError as exc:
        detail = exc.read().decode("utf-8", errors="replace")
        raise RuntimeError(f"HTTP {exc.code} {path}: {detail}") from exc


def is_url(value: str) -> bool:
    lower = value.lower()
    return lower.startswith("http://") or lower.startswith("https://")


def upload_file(path: Path, api_key: str) -> str:
    data = path.read_bytes()
    result = _request("POST", "/upload", api_key, body=data, content_type="application/octet-stream")
    upload_url = result.get("upload_url")
    if not upload_url:
        raise RuntimeError(f"Upload failed: no upload_url in response: {result}")
    return upload_url


def submit_transcription(
    audio_url: str,
    api_key: str,
    *,
    speakers_expected: int | None = None,
    language_code: str | None = None,
) -> str:
    payload: dict[str, Any] = {
        "audio_url": audio_url,
        "speaker_labels": True,
        "auto_chapters": True,
        "speech_models": ["universal-2"],
    }
    if language_code:
        payload["language_code"] = language_code
    else:
        payload["language_detection"] = True
    if speakers_expected is not None and speakers_expected > 0:
        payload["speakers_expected"] = speakers_expected

    result = _request(
        "POST",
        "/transcript",
        api_key,
        body=json.dumps(payload).encode("utf-8"),
    )
    transcript_id = result.get("id")
    if not transcript_id:
        raise RuntimeError(f"Transcription submit failed: {result}")
    return transcript_id


def poll_transcription(
    transcript_id: str,
    api_key: str,
    *,
    poll_interval: float = 3.0,
    timeout: float = 600.0,
) -> dict[str, Any]:
    deadline = time.monotonic() + timeout
    while time.monotonic() < deadline:
        result = _request("GET", f"/transcript/{transcript_id}", api_key)
        status = result.get("status")
        if status == "completed":
            return result
        if status == "error":
            raise RuntimeError(result.get("error") or "Transcription failed")
        time.sleep(poll_interval)
    raise RuntimeError(f"Transcription timed out after {timeout}s (id={transcript_id})")


def format_timestamp(ms: int | float | None) -> str:
    if ms is None:
        return "00:00:00"
    total_seconds = int(ms) // 1000
    hours, rem = divmod(total_seconds, 3600)
    minutes, seconds = divmod(rem, 60)
    if hours:
        return f"{hours:02d}:{minutes:02d}:{seconds:02d}"
    return f"{minutes:02d}:{seconds:02d}"


def count_speakers(utterances: list[dict[str, Any]] | None) -> int:
    if not utterances:
        return 0
    return len({u.get("speaker") for u in utterances if u.get("speaker") is not None})


def render_transcript_md(data: dict[str, Any], source_ref: str) -> str:
    utterances = data.get("utterances") or []
    chapters = data.get("chapters") or []
    lines = [
        "# Transcript",
        "",
        f"- **Source:** `{source_ref}`",
        f"- **Transcript ID:** `{data.get('id', '')}`",
        f"- **Duration:** {format_timestamp(data.get('audio_duration'))}",
        f"- **Language:** {data.get('language_code') or data.get('language') or 'unknown'}",
        f"- **Speakers:** {count_speakers(utterances)}",
        "",
        "## Diarized transcript",
        "",
    ]
    if utterances:
        for u in utterances:
            start = format_timestamp(u.get("start"))
            speaker = u.get("speaker", "?")
            text = (u.get("text") or "").strip()
            lines.append(f"[{start}] **Speaker {speaker}:** {text}")
    else:
        lines.append("_(No speaker diarization segments returned.)_")
        text = (data.get("text") or "").strip()
        if text:
            lines.append("")
            lines.append(text)

    lines.extend(["", "## Chapters", ""])
    if chapters:
        lines.append("| Start | Headline | Summary |")
        lines.append("|-------|----------|---------|")
        for ch in chapters:
            start = format_timestamp(ch.get("start"))
            headline = (ch.get("headline") or "").replace("|", "\\|")
            summary = (ch.get("summary") or "").replace("|", "\\|")
            lines.append(f"| {start} | {headline} | {summary} |")
    else:
        lines.append("_No chapters returned._")

    lines.extend(["", "## Full text", ""])
    lines.append((data.get("text") or "").strip())
    lines.append("")
    return "\n".join(lines)


def resolve_audio_url(input_value: str, api_key: str) -> tuple[str, str]:
    """Return (audio_url, source_ref) for markdown header."""
    if is_url(input_value):
        kind = "url"
        return input_value, f"{kind}:{input_value}"

    path = Path(input_value).expanduser().resolve()
    if not path.is_file():
        raise FileNotFoundError(f"Input file not found: {path}")

    suffix = path.suffix.lower()
    video_ext = {".mp4", ".mov", ".webm", ".mkv", ".avi"}
    kind = "video" if suffix in video_ext else "audio"
    upload_url = upload_file(path, api_key)
    return upload_url, f"{kind}:{path}"


def transcribe(
    api_key: str,
    input_value: str,
    *,
    speakers_expected: int | None = None,
    language_code: str | None = None,
    poll_interval: float = 3.0,
    timeout: float = 600.0,
) -> tuple[dict[str, Any], str]:
    audio_url, source_ref = resolve_audio_url(input_value, api_key)
    transcript_id = submit_transcription(
        audio_url,
        api_key,
        speakers_expected=speakers_expected,
        language_code=language_code,
    )
    data = poll_transcription(
        transcript_id,
        api_key,
        poll_interval=poll_interval,
        timeout=timeout,
    )
    return data, source_ref


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Transcribe audio/video via AssemblyAI")
    parser.add_argument("--api-key", required=True, help="AssemblyAI API key")
    parser.add_argument("--input", required=True, help="Local file path or https URL")
    parser.add_argument("--out", required=True, help="Output transcript.md path")
    parser.add_argument("--json-out", help="Optional raw API JSON path")
    parser.add_argument("--speakers", type=int, default=None, help="Expected speaker count")
    parser.add_argument("--language", default=None, help="Language code (e.g. en)")
    parser.add_argument("--poll-interval", type=float, default=3.0)
    parser.add_argument("--timeout", type=float, default=600.0)
    args = parser.parse_args(argv)

    try:
        data, source_ref = transcribe(
            args.api_key,
            args.input,
            speakers_expected=args.speakers,
            language_code=args.language,
            poll_interval=args.poll_interval,
            timeout=args.timeout,
        )
        md = render_transcript_md(data, source_ref)
        out_path = Path(args.out)
        out_path.parent.mkdir(parents=True, exist_ok=True)
        out_path.write_text(md, encoding="utf-8")

        json_path_str = None
        if args.json_out:
            json_path = Path(args.json_out)
            json_path.parent.mkdir(parents=True, exist_ok=True)
            json_path.write_text(json.dumps(data, indent=2), encoding="utf-8")
            json_path_str = str(json_path)

        print(
            json.dumps(
                {
                    "ok": True,
                    "transcript_id": data.get("id"),
                    "md": str(out_path),
                    "json": json_path_str,
                }
            )
        )
        return 0
    except Exception as exc:  # noqa: BLE001 — CLI surfaces message to agent
        print(json.dumps({"ok": False, "error": str(exc)}))
        return 1


if __name__ == "__main__":
    sys.exit(main())
