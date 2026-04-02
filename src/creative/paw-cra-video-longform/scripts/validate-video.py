#!/usr/bin/env python3
# /// script
# requires-python = ">=3.10"
# ///
"""
Validate a video file meets long-form production specifications.

Checks: resolution (1920x1080), codec (H.264), audio (AAC, stereo),
duration within tolerance, and audio levels approximation.

Requires ffprobe (bundled with ffmpeg) to be available on PATH.
"""

import argparse
import json
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path


def run_ffprobe(video_path: str, entries: str) -> dict:
    """Run ffprobe and return parsed JSON output."""
    cmd = [
        "ffprobe",
        "-v", "quiet",
        "-print_format", "json",
        "-show_format",
        "-show_streams",
        "-select_streams", entries,
        video_path,
    ]
    try:
        result = subprocess.run(cmd, capture_output=True, text=True, timeout=30)
        if result.returncode != 0:
            return {}
        return json.loads(result.stdout)
    except (subprocess.TimeoutExpired, json.JSONDecodeError, FileNotFoundError):
        return {}


def get_video_info(video_path: str) -> dict | None:
    """Extract video stream info via ffprobe."""
    data = run_ffprobe(video_path, "v:0")
    streams = data.get("streams", [])
    fmt = data.get("format", {})
    if not streams:
        return None
    s = streams[0]
    return {
        "width": int(s.get("width", 0)),
        "height": int(s.get("height", 0)),
        "codec": s.get("codec_name", "unknown"),
        "duration": float(fmt.get("duration", s.get("duration", 0))),
        "framerate": s.get("r_frame_rate", "0/1"),
        "file_size_bytes": int(fmt.get("size", 0)),
    }


def get_audio_info(video_path: str) -> dict | None:
    """Extract audio stream info via ffprobe."""
    data = run_ffprobe(video_path, "a:0")
    streams = data.get("streams", [])
    if not streams:
        return None
    s = streams[0]
    return {
        "codec": s.get("codec_name", "unknown"),
        "channels": int(s.get("channels", 0)),
        "sample_rate": int(s.get("sample_rate", 0)),
    }


def check_audio_levels(video_path: str) -> dict | None:
    """Measure audio loudness using ffmpeg loudnorm filter (two-pass measurement)."""
    cmd = [
        "ffmpeg",
        "-i", video_path,
        "-af", "loudnorm=I=-14:TP=-1.5:LRA=11:print_format=json",
        "-f", "null",
        "-",
    ]
    try:
        result = subprocess.run(cmd, capture_output=True, text=True, timeout=300)
        # loudnorm prints JSON to stderr
        stderr = result.stderr
        # Find the JSON block in stderr
        json_start = stderr.rfind("{")
        json_end = stderr.rfind("}") + 1
        if json_start >= 0 and json_end > json_start:
            loudness_data = json.loads(stderr[json_start:json_end])
            return {
                "integrated_loudness": float(loudness_data.get("input_i", -99)),
                "true_peak": float(loudness_data.get("input_tp", -99)),
                "loudness_range": float(loudness_data.get("input_lra", 0)),
            }
    except (subprocess.TimeoutExpired, json.JSONDecodeError, FileNotFoundError, ValueError):
        pass
    return None


def validate(video_path: str, target_duration: float | None = None, verbose: bool = False) -> dict:
    """Run all validation checks and return structured results."""
    findings = []
    checks = {}

    video_info = get_video_info(video_path)
    if video_info is None:
        findings.append({
            "severity": "critical",
            "category": "structure",
            "location": {"file": video_path},
            "issue": "Cannot read video stream. File may be corrupt or not a valid video.",
            "fix": "Re-encode the video or regenerate from source clips.",
        })
        return build_result(video_path, "fail", findings, checks)

    # Resolution check
    w, h = video_info["width"], video_info["height"]
    if w == 1920 and h == 1080:
        checks["resolution"] = "pass"
    else:
        checks["resolution"] = "fail"
        findings.append({
            "severity": "high",
            "category": "structure",
            "location": {"file": video_path},
            "issue": f"Resolution is {w}x{h}, expected 1920x1080.",
            "fix": f"Re-encode with: ffmpeg -i {video_path} -vf scale=1920:1080 -c:v libx264 output.mp4",
        })

    # Codec check
    if video_info["codec"] in ("h264", "libx264"):
        checks["codec"] = "pass"
    else:
        checks["codec"] = "fail"
        findings.append({
            "severity": "high",
            "category": "structure",
            "location": {"file": video_path},
            "issue": f"Video codec is '{video_info['codec']}', expected H.264 (h264).",
            "fix": f"Re-encode with: ffmpeg -i {video_path} -c:v libx264 -preset medium -crf 18 output.mp4",
        })

    # Duration check
    duration = video_info["duration"]
    if target_duration is not None:
        tolerance = target_duration * 0.10  # 10% tolerance
        if abs(duration - target_duration) <= tolerance:
            checks["duration"] = "pass"
        else:
            checks["duration"] = "fail"
            findings.append({
                "severity": "medium",
                "category": "structure",
                "location": {"file": video_path},
                "issue": f"Duration is {duration:.1f}s, target was {target_duration:.1f}s (tolerance: +/-{tolerance:.1f}s).",
                "fix": "Adjust scene durations or trim the final video to match target.",
            })
    else:
        # No target, just check it's within 1-10 min range
        if 60 <= duration <= 600:
            checks["duration"] = "pass"
        else:
            checks["duration"] = "warning"
            findings.append({
                "severity": "low",
                "category": "structure",
                "location": {"file": video_path},
                "issue": f"Duration is {duration:.1f}s, outside typical long-form range (60-600s).",
                "fix": "Verify this is the intended duration for the video.",
            })

    # Audio checks
    audio_info = get_audio_info(video_path)
    if audio_info is None:
        checks["audio_levels"] = "fail"
        findings.append({
            "severity": "high",
            "category": "structure",
            "location": {"file": video_path},
            "issue": "No audio stream found in video.",
            "fix": "Ensure voiceover audio is mixed into the final video during assembly.",
        })
    else:
        if audio_info["codec"] != "aac":
            findings.append({
                "severity": "medium",
                "category": "structure",
                "location": {"file": video_path},
                "issue": f"Audio codec is '{audio_info['codec']}', expected AAC.",
                "fix": f"Re-encode audio: ffmpeg -i {video_path} -c:v copy -c:a aac -b:a 192k output.mp4",
            })

        if audio_info["channels"] < 2:
            findings.append({
                "severity": "low",
                "category": "structure",
                "location": {"file": video_path},
                "issue": f"Audio is mono ({audio_info['channels']} channel). Stereo recommended.",
                "fix": "Re-encode with stereo: ffmpeg -i input.mp4 -c:v copy -ac 2 output.mp4",
            })

        # Loudness check
        levels = check_audio_levels(video_path)
        if levels:
            loudness = levels["integrated_loudness"]
            if -16 <= loudness <= -12:
                checks["audio_levels"] = "pass"
            else:
                checks["audio_levels"] = "warning"
                findings.append({
                    "severity": "medium",
                    "category": "structure",
                    "location": {"file": video_path},
                    "issue": f"Integrated loudness is {loudness:.1f} LUFS, target is -14 LUFS (acceptable: -16 to -12).",
                    "fix": "Normalize audio: ffmpeg -i input.mp4 -af loudnorm=I=-14:TP=-1.5:LRA=11 -c:v copy output.mp4",
                })

            if verbose and levels:
                print(f"[verbose] Loudness: {levels['integrated_loudness']:.1f} LUFS, "
                      f"True Peak: {levels['true_peak']:.1f} dBTP, "
                      f"LRA: {levels['loudness_range']:.1f} LU", file=sys.stderr)
        else:
            checks["audio_levels"] = "skip"
            findings.append({
                "severity": "info",
                "category": "structure",
                "location": {"file": video_path},
                "issue": "Could not measure audio loudness (ffmpeg loudnorm filter unavailable or timed out).",
                "fix": "Manually check audio levels in a video editor.",
            })

    # Determine overall status
    severities = [f["severity"] for f in findings]
    if "critical" in severities:
        status = "fail"
    elif "high" in severities:
        status = "fail"
    elif "medium" in severities:
        status = "warning"
    else:
        status = "pass"

    return build_result(video_path, status, findings, checks)


def build_result(video_path: str, status: str, findings: list, checks: dict) -> dict:
    """Build the standard JSON output structure."""
    summary = {
        "total": len(findings),
        "critical": sum(1 for f in findings if f["severity"] == "critical"),
        "high": sum(1 for f in findings if f["severity"] == "high"),
        "medium": sum(1 for f in findings if f["severity"] == "medium"),
        "low": sum(1 for f in findings if f["severity"] == "low"),
    }
    return {
        "script": "validate-video",
        "version": "1.0.0",
        "video_path": video_path,
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "status": status,
        "checks": checks,
        "findings": findings,
        "summary": summary,
    }


def main():
    parser = argparse.ArgumentParser(
        description="Validate a video file meets long-form production specifications (1920x1080, H.264, AAC audio, duration)."
    )
    parser.add_argument("video_path", help="Path to the video file to validate")
    parser.add_argument("--target-duration", type=float, default=None,
                        help="Expected duration in seconds (validates within 10%% tolerance)")
    parser.add_argument("-o", "--output", default=None,
                        help="Output file path (default: stdout)")
    parser.add_argument("--verbose", action="store_true",
                        help="Print diagnostic info to stderr")
    args = parser.parse_args()

    if not Path(args.video_path).exists():
        result = build_result(args.video_path, "fail", [{
            "severity": "critical",
            "category": "structure",
            "location": {"file": args.video_path},
            "issue": "Video file does not exist.",
            "fix": "Check the file path and ensure the video was exported correctly.",
        }], {})
    else:
        result = validate(args.video_path, args.target_duration, args.verbose)

    output_json = json.dumps(result, indent=2)

    if args.output:
        Path(args.output).write_text(output_json)
        print(f"Results written to {args.output}", file=sys.stderr)
    else:
        print(output_json)

    # Exit code based on status
    if result["status"] == "fail":
        sys.exit(1)
    elif result["status"] == "warning":
        sys.exit(0)
    else:
        sys.exit(0)


if __name__ == "__main__":
    main()
