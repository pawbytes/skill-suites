#!/usr/bin/env python3
# /// script
# requires-python = ">=3.9"
# dependencies = []
# ///
"""Unit tests for transcribe.py — stdlib unittest, no external deps."""
import importlib.util
import json
import tempfile
import unittest
from pathlib import Path
from unittest.mock import MagicMock, patch

_spec = importlib.util.spec_from_file_location(
    "transcribe", Path(__file__).resolve().parent.parent / "transcribe.py"
)
tx = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(tx)


class TestFormatTimestamp(unittest.TestCase):
    def test_seconds_only(self):
        self.assertEqual(tx.format_timestamp(45_000), "00:45")

    def test_minutes_seconds(self):
        self.assertEqual(tx.format_timestamp(125_000), "02:05")

    def test_with_hours(self):
        self.assertEqual(tx.format_timestamp(3_661_000), "01:01:01")

    def test_none(self):
        self.assertEqual(tx.format_timestamp(None), "00:00:00")


class TestIsUrl(unittest.TestCase):
    def test_https(self):
        self.assertTrue(tx.is_url("https://example.com/a.mp3"))

    def test_http(self):
        self.assertTrue(tx.is_url("http://example.com/a.mp3"))

    def test_local_path(self):
        self.assertFalse(tx.is_url("/tmp/audio.mp3"))


class TestCountSpeakers(unittest.TestCase):
    def test_unique_speakers(self):
        utterances = [
            {"speaker": "A", "text": "hi"},
            {"speaker": "B", "text": "hey"},
            {"speaker": "A", "text": "again"},
        ]
        self.assertEqual(tx.count_speakers(utterances), 2)

    def test_empty(self):
        self.assertEqual(tx.count_speakers(None), 0)
        self.assertEqual(tx.count_speakers([]), 0)


class TestRenderTranscriptMd(unittest.TestCase):
    def test_renders_diarized_and_chapters(self):
        data = {
            "id": "tid-1",
            "audio_duration": 90_000,
            "language_code": "en",
            "text": "Hello world full text.",
            "utterances": [
                {"start": 1000, "speaker": "A", "text": "Hello"},
                {"start": 5000, "speaker": "B", "text": "World"},
            ],
            "chapters": [
                {"start": 0, "headline": "Intro", "summary": "Opening"},
            ],
        }
        md = tx.render_transcript_md(data, "audio:/tmp/call.m4a")
        self.assertIn("# Transcript", md)
        self.assertIn("**Speaker A:** Hello", md)
        self.assertIn("**Speaker B:** World", md)
        self.assertIn("| Intro |", md)
        self.assertIn("Hello world full text.", md)
        self.assertIn("audio:/tmp/call.m4a", md)

    def test_fallback_without_utterances(self):
        data = {"id": "t2", "text": "Plain only."}
        md = tx.render_transcript_md(data, "text:manual")
        self.assertIn("Plain only.", md)
        self.assertIn("No speaker diarization", md)


class TestResolveAudioUrl(unittest.TestCase):
    def test_url_passthrough(self):
        url, ref = tx.resolve_audio_url("https://cdn.example.com/brief.mp3", "key")
        self.assertEqual(url, "https://cdn.example.com/brief.mp3")
        self.assertEqual(ref, "url:https://cdn.example.com/brief.mp3")

    def test_local_upload(self):
        with tempfile.NamedTemporaryFile(suffix=".wav", delete=False) as f:
            f.write(b"RIFFfake")
            path = f.name
        try:
            with patch.object(tx, "upload_file", return_value="https://cdn.asm/uploaded") as mock_up:
                url, ref = tx.resolve_audio_url(path, "key")
            mock_up.assert_called_once()
            self.assertEqual(url, "https://cdn.asm/uploaded")
            self.assertTrue(ref.startswith("audio:"))
        finally:
            Path(path).unlink(missing_ok=True)

    def test_video_kind(self):
        with tempfile.NamedTemporaryFile(suffix=".mp4", delete=False) as f:
            f.write(b"fake")
            path = f.name
        try:
            with patch.object(tx, "upload_file", return_value="https://cdn.asm/vid"):
                _, ref = tx.resolve_audio_url(path, "key")
            self.assertTrue(ref.startswith("video:"))
        finally:
            Path(path).unlink(missing_ok=True)


class TestTranscribeFlow(unittest.TestCase):
    def test_end_to_end_mocked(self):
        sample = {
            "id": "abc",
            "status": "completed",
            "text": "Done.",
            "utterances": [{"start": 0, "speaker": "A", "text": "Done."}],
        }
        with patch.object(tx, "resolve_audio_url", return_value=("https://audio", "url:x")):
            with patch.object(tx, "submit_transcription", return_value="abc"):
                with patch.object(tx, "poll_transcription", return_value=sample):
                    data, ref = tx.transcribe("key", "https://x.com/a.mp3")
        self.assertEqual(data["id"], "abc")
        self.assertEqual(ref, "url:x")


class TestMainCli(unittest.TestCase):
    def test_main_success(self):
        sample = {
            "id": "cli-1",
            "text": "CLI test",
            "utterances": [],
        }
        with tempfile.TemporaryDirectory() as tmp:
            out = Path(tmp) / "t.md"
            with patch.object(tx, "transcribe", return_value=(sample, "url:u")):
                rc = tx.main(
                    [
                        "--api-key",
                        "k",
                        "--input",
                        "https://example.com/a.mp3",
                        "--out",
                        str(out),
                    ]
                )
            self.assertEqual(rc, 0)
            self.assertTrue(out.is_file())
            self.assertIn("CLI test", out.read_text(encoding="utf-8"))

    def test_main_failure(self):
        with tempfile.TemporaryDirectory() as tmp:
            out = Path(tmp) / "t.md"
            with patch.object(tx, "transcribe", side_effect=RuntimeError("boom")):
                rc = tx.main(
                    ["--api-key", "k", "--input", "x", "--out", str(out)]
                )
            self.assertEqual(rc, 1)


if __name__ == "__main__":
    unittest.main()
