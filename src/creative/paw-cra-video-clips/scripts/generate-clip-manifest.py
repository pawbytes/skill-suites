# /// script
# requires-python = ">=3.9"
# ///
"""
Generate a clip-manifest.json from a directory of video clip files.

Scans the directory for .mp4 files, extracts metadata via ffprobe,
and produces a structured manifest for the cra-video-clips workflow.

Usage:
    python generate-clip-manifest.py <clip_directory> [-o output_file] [--source-info source.json]
"""

import argparse
import json
import os
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path


def get_ffprobe_metadata(file_path: str) -> dict:
    """Extract video metadata using ffprobe."""
    try:
        result = subprocess.run(
            [
                "ffprobe",
                "-v", "quiet",
                "-print_format", "json",
                "-show_format",
                "-show_streams",
                str(file_path),
            ],
            capture_output=True,
            text=True,
            timeout=30,
        )
        if result.returncode != 0:
            print(f"  Warning: ffprobe failed for {file_path}", file=sys.stderr)
            return {}
        return json.loads(result.stdout)
    except FileNotFoundError:
        print("Error: ffprobe not found. Install ffmpeg.", file=sys.stderr)
        sys.exit(2)
    except subprocess.TimeoutExpired:
        print(f"  Warning: ffprobe timed out for {file_path}", file=sys.stderr)
        return {}
    except json.JSONDecodeError:
        print(f"  Warning: ffprobe output not valid JSON for {file_path}", file=sys.stderr)
        return {}


def extract_clip_info(file_path: Path, base_dir: Path) -> dict:
    """Extract clip metadata from a video file."""
    probe = get_ffprobe_metadata(str(file_path))
    if not probe:
        return {
            "file": str(file_path.relative_to(base_dir)),
            "status": "error",
            "error": "ffprobe failed",
        }

    # Extract video stream info
    video_stream = None
    audio_stream = None
    for stream in probe.get("streams", []):
        if stream.get("codec_type") == "video" and video_stream is None:
            video_stream = stream
        elif stream.get("codec_type") == "audio" and audio_stream is None:
            audio_stream = stream

    format_info = probe.get("format", {})
    duration = float(format_info.get("duration", 0))
    file_size = int(format_info.get("size", 0))

    info = {
        "file": str(file_path.relative_to(base_dir)),
        "file_size_bytes": file_size,
        "file_size_mb": round(file_size / (1024 * 1024), 2),
        "duration_seconds": round(duration, 2),
        "container": format_info.get("format_name", "unknown"),
    }

    if video_stream:
        info["video"] = {
            "codec": video_stream.get("codec_name", "unknown"),
            "width": int(video_stream.get("width", 0)),
            "height": int(video_stream.get("height", 0)),
            "fps": _parse_fps(video_stream.get("r_frame_rate", "0/1")),
            "bitrate_kbps": int(video_stream.get("bit_rate", 0)) // 1000 if video_stream.get("bit_rate") else None,
        }

    if audio_stream:
        info["audio"] = {
            "codec": audio_stream.get("codec_name", "unknown"),
            "sample_rate": int(audio_stream.get("sample_rate", 0)),
            "bitrate_kbps": int(audio_stream.get("bit_rate", 0)) // 1000 if audio_stream.get("bit_rate") else None,
        }

    # Infer platform and clip ID from filename convention: {clip_id}_{platform}_{duration}s.mp4
    stem = file_path.stem
    info["platform"] = _infer_platform(stem, file_path)
    info["clip_id"] = _infer_clip_id(stem)
    info["subtitles_burned"] = "subtitled" in stem.lower() or "_sub" in stem.lower()
    info["brand_overlay"] = "branded" in stem.lower() or "_brand" in stem.lower()
    info["status"] = "pass"

    return info


def _parse_fps(rate_str: str) -> float:
    """Parse ffprobe frame rate string like '30/1' or '30000/1001'."""
    try:
        if "/" in rate_str:
            num, den = rate_str.split("/")
            return round(int(num) / int(den), 2) if int(den) != 0 else 0.0
        return float(rate_str)
    except (ValueError, ZeroDivisionError):
        return 0.0


def _infer_platform(stem: str, file_path: Path) -> str:
    """Infer target platform from filename or parent directory."""
    stem_lower = stem.lower()
    parent_lower = file_path.parent.name.lower()

    platforms = ["tiktok", "reels", "shorts", "youtube", "linkedin", "facebook", "twitter", "x"]
    for p in platforms:
        if p in stem_lower or p == parent_lower:
            return p
    return "unknown"


def _infer_clip_id(stem: str) -> str:
    """Infer clip ID from filename (e.g., M01 from M01_tiktok_30s)."""
    parts = stem.split("_")
    if parts:
        return parts[0]
    return stem


def validate_clip_specs(clip: dict, platform_specs: dict) -> list:
    """Validate a clip against platform specs. Returns list of issues."""
    issues = []
    platform = clip.get("platform", "unknown")
    specs = platform_specs.get(platform)

    if not specs or "video" not in clip:
        return issues

    video = clip["video"]

    if specs.get("width") and video.get("width") != specs["width"]:
        issues.append(f"Width {video['width']} != expected {specs['width']}")
    if specs.get("height") and video.get("height") != specs["height"]:
        issues.append(f"Height {video['height']} != expected {specs['height']}")
    if specs.get("max_file_size_mb") and clip.get("file_size_mb", 0) > specs["max_file_size_mb"]:
        issues.append(f"File size {clip['file_size_mb']}MB exceeds {specs['max_file_size_mb']}MB limit")
    if specs.get("codec") and video.get("codec") not in specs["codec"]:
        issues.append(f"Codec {video['codec']} not in accepted: {specs['codec']}")

    return issues


# Platform spec thresholds for validation
PLATFORM_SPECS = {
    "tiktok": {"width": 1080, "height": 1920, "max_file_size_mb": 287, "codec": ["h264", "avc"]},
    "reels": {"width": 1080, "height": 1920, "max_file_size_mb": 250, "codec": ["h264", "avc"]},
    "shorts": {"width": 1080, "height": 1920, "max_file_size_mb": 256000, "codec": ["h264", "hevc", "avc"]},
    "youtube": {"width": 1920, "height": 1080, "max_file_size_mb": 256000, "codec": ["h264", "hevc", "avc"]},
    "linkedin": {"width": None, "height": None, "max_file_size_mb": 5000, "codec": ["h264", "avc"]},
    "facebook": {"width": None, "height": None, "max_file_size_mb": 10000, "codec": ["h264", "avc"]},
}


def generate_manifest(clip_dir: str, source_info_path: str = None) -> dict:
    """Generate the full clip manifest from a directory."""
    clip_path = Path(clip_dir)
    if not clip_path.is_dir():
        print(f"Error: {clip_dir} is not a directory", file=sys.stderr)
        sys.exit(1)

    # Find all mp4 files recursively
    mp4_files = sorted(clip_path.rglob("*.mp4"))
    if not mp4_files:
        print(f"Warning: No .mp4 files found in {clip_dir}", file=sys.stderr)

    clips = []
    for mp4 in mp4_files:
        print(f"  Scanning: {mp4.name}", file=sys.stderr)
        clip = extract_clip_info(mp4, clip_path)

        # Validate against platform specs
        issues = validate_clip_specs(clip, PLATFORM_SPECS)
        if issues:
            clip["validation_issues"] = issues
            clip["status"] = "warning"

        clips.append(clip)

    # Load source info if provided
    source = {}
    if source_info_path and Path(source_info_path).exists():
        with open(source_info_path) as f:
            source = json.load(f)

    # Build manifest
    manifest = {
        "schema_version": "1.0",
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "generator": "cra-video-clips/generate-clip-manifest",
        "source": source,
        "clip_directory": str(clip_path),
        "summary": {
            "total_clips": len(clips),
            "platforms": list(set(c.get("platform", "unknown") for c in clips)),
            "total_size_mb": round(sum(c.get("file_size_mb", 0) for c in clips), 2),
            "passed": sum(1 for c in clips if c.get("status") == "pass"),
            "warnings": sum(1 for c in clips if c.get("status") == "warning"),
            "errors": sum(1 for c in clips if c.get("status") == "error"),
        },
        "clips": clips,
    }

    return manifest


def main():
    parser = argparse.ArgumentParser(
        description="Generate clip-manifest.json from a directory of video clips.",
        epilog="Part of the cra-video-clips workflow. Requires ffprobe.",
    )
    parser.add_argument("clip_directory", help="Directory containing .mp4 clip files")
    parser.add_argument("-o", "--output", help="Output file path (default: stdout)", default=None)
    parser.add_argument("--source-info", help="Path to source-metadata.json", default=None)
    parser.add_argument("--verbose", action="store_true", help="Enable verbose output")

    args = parser.parse_args()

    manifest = generate_manifest(args.clip_directory, args.source_info)

    output_json = json.dumps(manifest, indent=2)

    if args.output:
        Path(args.output).parent.mkdir(parents=True, exist_ok=True)
        with open(args.output, "w") as f:
            f.write(output_json)
        print(f"Manifest written to {args.output}", file=sys.stderr)
    else:
        print(output_json)

    # Exit code based on results
    if manifest["summary"]["errors"] > 0:
        sys.exit(1)
    sys.exit(0)


if __name__ == "__main__":
    main()
