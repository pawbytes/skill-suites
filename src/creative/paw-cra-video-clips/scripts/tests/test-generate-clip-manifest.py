# /// script
# requires-python = ">=3.9"
# ///
"""Tests for generate-clip-manifest.py"""

import json
import sys
from pathlib import Path
from unittest.mock import MagicMock, patch

# Add parent directory to path
sys.path.insert(0, str(Path(__file__).parent.parent))

from importlib import import_module

# Import the module with hyphens in name
import importlib.util
spec = importlib.util.spec_from_file_location(
    "generate_clip_manifest",
    Path(__file__).parent.parent / "generate-clip-manifest.py"
)
gcm = importlib.util.module_from_spec(spec)
spec.loader.exec_module(gcm)


class TestParseFps:
    def test_simple_fraction(self):
        assert gcm._parse_fps("30/1") == 30.0

    def test_ntsc_fraction(self):
        result = gcm._parse_fps("30000/1001")
        assert 29.9 < result < 30.0

    def test_zero_denominator(self):
        assert gcm._parse_fps("30/0") == 0.0

    def test_plain_number(self):
        assert gcm._parse_fps("24") == 24.0

    def test_invalid(self):
        assert gcm._parse_fps("abc") == 0.0


class TestInferPlatform:
    def test_tiktok_in_filename(self):
        p = Path("/clips/M01_tiktok_30s.mp4")
        assert gcm._infer_platform("M01_tiktok_30s", p) == "tiktok"

    def test_reels_in_filename(self):
        p = Path("/clips/M01_reels_30s.mp4")
        assert gcm._infer_platform("M01_reels_30s", p) == "reels"

    def test_platform_from_parent_dir(self):
        p = Path("/clips/youtube/M01_60s.mp4")
        assert gcm._infer_platform("M01_60s", p) == "youtube"

    def test_unknown(self):
        p = Path("/clips/M01_raw.mp4")
        assert gcm._infer_platform("M01_raw", p) == "unknown"


class TestInferClipId:
    def test_standard_format(self):
        assert gcm._infer_clip_id("M01_tiktok_30s") == "M01"

    def test_simple_name(self):
        assert gcm._infer_clip_id("clip1") == "clip1"

    def test_with_underscores(self):
        assert gcm._infer_clip_id("M03_youtube_60s") == "M03"


class TestValidateClipSpecs:
    def test_pass_tiktok(self):
        clip = {
            "platform": "tiktok",
            "video": {"width": 1080, "height": 1920, "codec": "h264"},
            "file_size_mb": 8.0,
        }
        issues = gcm.validate_clip_specs(clip, gcm.PLATFORM_SPECS)
        assert issues == []

    def test_wrong_resolution(self):
        clip = {
            "platform": "tiktok",
            "video": {"width": 720, "height": 1280, "codec": "h264"},
            "file_size_mb": 5.0,
        }
        issues = gcm.validate_clip_specs(clip, gcm.PLATFORM_SPECS)
        assert len(issues) == 2  # width and height mismatch

    def test_file_too_large(self):
        clip = {
            "platform": "reels",
            "video": {"width": 1080, "height": 1920, "codec": "h264"},
            "file_size_mb": 300.0,
        }
        issues = gcm.validate_clip_specs(clip, gcm.PLATFORM_SPECS)
        assert any("exceeds" in i for i in issues)

    def test_unknown_platform_no_validation(self):
        clip = {
            "platform": "unknown",
            "video": {"width": 500, "height": 500, "codec": "mpeg4"},
            "file_size_mb": 1.0,
        }
        issues = gcm.validate_clip_specs(clip, gcm.PLATFORM_SPECS)
        assert issues == []


class TestManifestStructure:
    @patch.object(gcm, "get_ffprobe_metadata")
    def test_manifest_has_required_fields(self, mock_ffprobe):
        """Test manifest output contains all required top-level fields."""
        import tempfile
        import os

        # Create a temp dir with a fake mp4
        with tempfile.TemporaryDirectory() as tmpdir:
            fake_mp4 = Path(tmpdir) / "M01_tiktok_30s.mp4"
            fake_mp4.write_bytes(b"\x00" * 100)

            mock_ffprobe.return_value = {
                "format": {"duration": "30.0", "size": "8000000", "format_name": "mp4"},
                "streams": [
                    {
                        "codec_type": "video",
                        "codec_name": "h264",
                        "width": 1080,
                        "height": 1920,
                        "r_frame_rate": "30/1",
                    },
                    {
                        "codec_type": "audio",
                        "codec_name": "aac",
                        "sample_rate": "44100",
                    },
                ],
            }

            manifest = gcm.generate_manifest(tmpdir)

            assert "schema_version" in manifest
            assert "generated_at" in manifest
            assert "summary" in manifest
            assert "clips" in manifest
            assert manifest["summary"]["total_clips"] == 1
            assert manifest["clips"][0]["platform"] == "tiktok"
            assert manifest["clips"][0]["clip_id"] == "M01"


if __name__ == "__main__":
    # Simple test runner
    import traceback

    test_classes = [
        TestParseFps,
        TestInferPlatform,
        TestInferClipId,
        TestValidateClipSpecs,
        TestManifestStructure,
    ]

    passed = 0
    failed = 0

    for cls in test_classes:
        instance = cls()
        for method_name in dir(instance):
            if method_name.startswith("test_"):
                try:
                    getattr(instance, method_name)()
                    passed += 1
                    print(f"  PASS: {cls.__name__}.{method_name}")
                except Exception as e:
                    failed += 1
                    print(f"  FAIL: {cls.__name__}.{method_name}: {e}")
                    traceback.print_exc()

    print(f"\n{passed} passed, {failed} failed")
    sys.exit(1 if failed else 0)
