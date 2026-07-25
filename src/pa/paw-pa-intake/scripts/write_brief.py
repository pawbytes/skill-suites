#!/usr/bin/env python3
# /// script
# requires-python = ">=3.9"
# dependencies = []
# ///
"""Write structured brief.md from JSON and run completeness check.

Plumbing for paw-pa-intake — the LLM performs extraction; this script renders
the canonical brief format and computes completeness metadata.

Usage:
  python write_brief.py --brief brief.json --out brief.md
  python write_brief.py --brief brief.json --out brief.md --summary-out .intake-summary.json

Stdout JSON: {"ok": true, "briefPath": "...", "completeness": {...}}
Exit codes: 0=success, 1=validation error
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from datetime import date
from pathlib import Path
from typing import Any

VALID_TYPES = {"pitch", "rfp", "scoping"}
TBD_PATTERNS = re.compile(r"^(tbd|not stated|unknown|n/a|none)$", re.I)

SEVERITY_WEIGHTS = {"critical": 0.25, "high": 0.15, "medium": 0.10, "low": 0.05}


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Render brief.md from structured JSON.")
    parser.add_argument("--brief", required=True, help="Path to brief JSON file")
    parser.add_argument("--out", required=True, help="Output brief.md path")
    parser.add_argument("--summary-out", help="Optional .intake-summary.json path")
    return parser.parse_args()


def load_brief(path: Path) -> dict:
    with open(path, "r", encoding="utf-8") as f:
        data = json.load(f)
    if not isinstance(data, dict):
        raise ValueError("Brief JSON must be an object")
    return data


def is_empty(value: Any) -> bool:
    if value is None:
        return True
    if isinstance(value, str):
        s = value.strip()
        return not s or bool(TBD_PATTERNS.match(s))
    if isinstance(value, list):
        return len(value) == 0
    return False


def as_list(value: Any) -> list:
    if value is None:
        return []
    if isinstance(value, list):
        return [str(v).strip() for v in value if str(v).strip()]
    if isinstance(value, str) and value.strip():
        return [value.strip()]
    return []


def yaml_scalar(value: Any) -> str:
    if value is None:
        return "null"
    if isinstance(value, bool):
        return "true" if value else "false"
    if isinstance(value, (int, float)):
        return str(value)
    s = str(value).strip()
    if not s:
        return '""'
    if any(c in s for c in ':"\\#{}[],&*?|>-') or s[0] in "-?":
        escaped = s.replace("\\", "\\\\").replace('"', '\\"')
        return f'"{escaped}"'
    return s


def yaml_list(items: list) -> list[str]:
    if not items:
        return ["  []"]
    lines = []
    for item in items:
        lines.append(f"  - {yaml_scalar(item)}")
    return lines


def compute_completeness(data: dict) -> dict:
    gaps: list[dict] = []
    ptype = str(data.get("proposalType", "")).lower()

    def add_gap(field: str, severity: str, message: str, suggestion: str = "") -> None:
        entry = {"field": field, "severity": severity, "message": message, "resolved": False}
        if suggestion:
            entry["suggestion"] = suggestion
        gaps.append(entry)

    if is_empty(data.get("clientName")):
        add_gap("clientName", "critical", "Missing client name", "Ask who the proposal is for")

    if is_empty(data.get("projectDescription")) or len(str(data.get("projectDescription", "")).strip()) < 40:
        add_gap("projectDescription", "critical", "Scope summary missing or too thin")

    reqs = as_list(data.get("requirements"))
    if not reqs:
        add_gap("requirements", "critical", "No requirements extracted")

    if is_empty(data.get("sourceInputRef")):
        add_gap("sourceInputRef", "critical", "Original input reference not set")

    if is_empty(ptype) or ptype not in VALID_TYPES:
        add_gap("proposalType", "critical", "Missing or invalid proposal type")

    if is_empty(data.get("clientContext")):
        add_gap("clientContext", "medium", "No client context provided")

    if is_empty(data.get("budget")):
        add_gap("budget", "high", "Budget not stated — pricing cannot calibrate",
                "Ask for budget range or approval band")

    if is_empty(data.get("timeline")):
        add_gap("timeline", "medium", "Timeline not stated")

    if is_empty(data.get("decisionMaker")):
        add_gap("decisionMaker", "medium", "Decision maker not identified")

    if ptype == "rfp":
        timeline = str(data.get("timeline", "")).lower()
        if is_empty(data.get("timeline")) or "deadline" not in timeline and "due" not in timeline:
            if not any(g["field"] == "timeline" for g in gaps):
                add_gap("timeline", "critical", "RFP submission deadline not found in timeline")
        if not as_list(data.get("complianceRequirements")) and "compliance" in str(data.get("projectDescription", "")).lower():
            add_gap("complianceRequirements", "high", "Compliance mentioned but not extracted")

    if ptype == "scoping":
        if not as_list(data.get("deliverables")):
            add_gap("deliverables", "high", "No deliverables listed for scoping doc")
        if not as_list(data.get("milestones")):
            add_gap("milestones", "medium", "No milestones listed")

    score = 1.0
    for gap in gaps:
        score -= SEVERITY_WEIGHTS.get(gap["severity"], 0.05)
    score = max(0.0, round(score, 2))

    assumptions = data.get("assumptions") or []
    if isinstance(assumptions, list) and assumptions and isinstance(assumptions[0], str):
        assumptions = [{"field": "misc", "assumedValue": a, "rationale": "User/agent assumption"} for a in assumptions]

    mode = str(data.get("intakeMode", "guided")).lower()
    autonomous = mode in ("autonomous", "headless")

    critical = [g for g in gaps if g["severity"] == "critical"]
    high = [g for g in gaps if g["severity"] == "high"]

    high_covered = all(
        any(a.get("field") == g["field"] for a in assumptions) for g in high
    ) if autonomous and high else len(high) == 0

    ready = not critical and score >= 0.60 and high_covered

    if autonomous:
        for gap in gaps:
            if any(a.get("field") == gap["field"] for a in assumptions):
                gap["assumedInAutonomous"] = True

    thin = (
        len(str(data.get("_sourceWordCount", ""))) > 0
        and int(data.get("_sourceWordCount", 999)) < 100
        and score < 0.70
    ) or len([g for g in gaps if g["severity"] in ("high", "critical")]) > 3

    counts = {s: len([g for g in gaps if g["severity"] == s]) for s in ("critical", "high", "medium", "low")}

    return {
        "score": score,
        "readyForPipeline": ready,
        "thinBrief": thin,
        "gapCount": len(gaps),
        "criticalCount": counts["critical"],
        "highCount": counts["high"],
        "mediumCount": counts["medium"],
        "lowCount": counts["low"],
        "gaps": gaps,
        "readyForResearch": not any(g["field"] in ("clientName", "projectDescription") for g in critical),
        "readyForPricing": ready and bool(reqs),
        "blockers": [g["field"] for g in critical],
    }


def render_brief_md(data: dict, completeness: dict) -> str:
    client = str(data.get("clientName", "")).strip()
    proposal_type = str(data.get("proposalType", "pitch")).strip().lower()
    if proposal_type not in VALID_TYPES:
        proposal_type = "pitch"

    lines = ["---"]
    scalar_fields = [
        ("clientName", client),
        ("clientContext", data.get("clientContext", "")),
        ("proposalType", proposal_type),
        ("proposalTypeConfidence", data.get("proposalTypeConfidence", "medium")),
        ("proposalTypeDetectionNotes", data.get("proposalTypeDetectionNotes", "")),
        ("budget", data.get("budget") or None),
        ("timeline", data.get("timeline") or None),
        ("decisionMaker", data.get("decisionMaker") or None),
        ("sourceInputRef", data.get("sourceInputRef", "")),
        ("language", data.get("language", "English")),
        ("intakeDate", data.get("intakeDate") or data.get("generated") or date.today().isoformat()),
        ("intakeMode", data.get("intakeMode", "guided")),
        ("inputType", data.get("inputType", "text")),
        ("industry", data.get("industry") or None),
        ("companySize", data.get("companySize") or None),
        ("urgency", data.get("urgency") or None),
    ]
    for key, val in scalar_fields:
        if val is not None and str(val).strip():
            lines.append(f"{key}: {yaml_scalar(val)}")

    lines.append("requirements:")
    lines.extend(yaml_list(as_list(data.get("requirements"))))

    lines.append("constraints:")
    lines.extend(yaml_list(as_list(data.get("constraints"))))

    for list_key in ("deliverables", "milestones", "successCriteria", "complianceRequirements", "stakeholders", "competitorsMentioned"):
        items = as_list(data.get(list_key))
        if items:
            lines.append(f"{list_key}:")
            lines.extend(yaml_list(items))

    lines.append("completenessReport:")
    lines.append(f"  score: {completeness['score']}")
    lines.append(f"  readyForPipeline: {str(completeness['readyForPipeline']).lower()}")
    lines.append(f"  thinBrief: {str(completeness.get('thinBrief', False)).lower()}")
    lines.append(f"  gapCount: {completeness['gapCount']}")
    lines.append("  gaps:")
    for gap in completeness.get("gaps") or []:
        lines.append(f"    - field: {yaml_scalar(gap.get('field', ''))}")
        lines.append(f"      severity: {yaml_scalar(gap.get('severity', ''))}")
        lines.append(f"      message: {yaml_scalar(gap.get('message', ''))}")
        lines.append(f"      resolved: false")

    assumptions = data.get("assumptions") or []
    if isinstance(assumptions, list) and assumptions and isinstance(assumptions[0], str):
        assumptions = [{"field": "misc", "assumedValue": a, "rationale": ""} for a in assumptions]

    lines.append("assumptions:")
    if assumptions:
        for a in assumptions:
            lines.append("  - field: " + yaml_scalar(a.get("field", "")))
            lines.append("    assumedValue: " + yaml_scalar(a.get("assumedValue", "")))
            lines.append("    rationale: " + yaml_scalar(a.get("rationale", "")))
    else:
        lines.append("  []")

    lines.extend(["---", ""])
    lines.append(f"# Brief: {client or 'Unknown client'}")
    lines.append("")

    desc = str(data.get("projectDescription") or "").strip()
    lines.append("## Problem & context")
    lines.append("")
    lines.append(desc if desc else "_Not provided — see completeness gaps._")
    lines.append("")

    lines.append("## Scope summary")
    lines.append("")
    for req in as_list(data.get("requirements")):
        lines.append(f"- {req}")
    if not as_list(data.get("requirements")):
        lines.append("- _None extracted_")
    lines.append("")

    open_gaps = [g for g in completeness.get("gaps", []) if not g.get("resolved")]
    lines.append("## Open questions")
    lines.append("")
    if open_gaps:
        for g in open_gaps:
            lines.append(f"- **{g.get('field')}:** {g.get('message')}")
    else:
        lines.append("_No open gaps._")
    lines.append("")

    return "\n".join(lines)


def emit(payload: dict, exit_code: int = 0) -> None:
    print(json.dumps(payload, ensure_ascii=False))
    raise SystemExit(exit_code)


def main() -> None:
    args = parse_args()
    try:
        data = load_brief(Path(args.brief))
        completeness = compute_completeness(data)
        md = render_brief_md(data, completeness)

        out_path = Path(args.out)
        out_path.parent.mkdir(parents=True, exist_ok=True)
        out_path.write_text(md, encoding="utf-8")

        summary_path = None
        if args.summary_out:
            summary_path = Path(args.summary_out)
            summary_path.parent.mkdir(parents=True, exist_ok=True)
            summary_payload = {
                "clientName": data.get("clientName"),
                "proposalType": data.get("proposalType"),
                "completeness": completeness,
                "typeDetection": {
                    "confidence": data.get("proposalTypeConfidence"),
                    "notes": data.get("proposalTypeDetectionNotes"),
                },
            }
            summary_path.write_text(json.dumps(summary_payload, indent=2), encoding="utf-8")

        emit(
            {
                "ok": True,
                "briefPath": str(out_path.resolve()),
                "summaryPath": str(summary_path.resolve()) if summary_path else None,
                "completeness": completeness,
            }
        )
    except (OSError, json.JSONDecodeError, ValueError) as exc:
        emit({"ok": False, "error": str(exc)}, exit_code=1)


if __name__ == "__main__":
    main()
