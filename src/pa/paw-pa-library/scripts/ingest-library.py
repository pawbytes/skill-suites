#!/usr/bin/env python3
# /// script
# requires-python = ">=3.9"
# dependencies = []
# ///
"""Ingest proposal library documents from inbox into structured indexes.

Scans library/inbox/ for markdown and text files, extracts structured fields
using filename and content heuristics, and updates:
  - library/case-studies-index.json
  - library/pricing-history.json
  - library/scope-templates.md
  - brand/boilerplate/*.md (when recognized)

Uses ingest-manifest.json for incremental re-index (SHA-256 per source file).

Exit codes: 0=success, 1=validation error, 2=runtime error
"""

from __future__ import annotations

import argparse
import hashlib
import json
import re
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

SUPPORTED_EXTENSIONS = {".md", ".txt", ".json"}
MANIFEST_VERSION = 1

DOC_CASE_STUDY = "case-study"
DOC_PRICING = "pricing"
DOC_BOILERPLATE_ABOUT = "boilerplate-about"
DOC_BOILERPLATE_TERMS = "boilerplate-terms"
DOC_BOILERPLATE_BIOS = "boilerplate-bios"
DOC_SCOPE = "scope-template"
DOC_UNKNOWN = "unknown"

BOILERPLATE_TARGETS = {
    DOC_BOILERPLATE_ABOUT: "about-us.md",
    DOC_BOILERPLATE_TERMS: "terms.md",
    DOC_BOILERPLATE_BIOS: "bios.md",
}


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Ingest library inbox docs into structured proposal indexes."
    )
    parser.add_argument(
        "--memory-root",
        required=True,
        help="Path to proposal-automation-suites memory root",
    )
    parser.add_argument(
        "--inbox",
        help="Path to library inbox folder (default: {memory-root}/library/inbox)",
    )
    parser.add_argument(
        "--validate",
        action="store_true",
        help="Run validation only — check indexes vs manifest and source files",
    )
    parser.add_argument(
        "--force",
        action="store_true",
        help="Re-process all inbox files regardless of manifest hashes",
    )
    parser.add_argument(
        "--report-path",
        help="Write validation report JSON to this path (with --validate)",
    )
    parser.add_argument(
        "--verbose",
        action="store_true",
        help="Print progress to stderr",
    )
    return parser.parse_args()


def log(msg: str, verbose: bool) -> None:
    if verbose:
        print(msg, file=sys.stderr)


def sha256_file(path: Path) -> str:
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(65536), b""):
            h.update(chunk)
    return h.hexdigest()


def load_json(path: Path, default: Any) -> Any:
    if not path.exists():
        return default
    with open(path, "r", encoding="utf-8") as f:
        data = json.load(f)
    return data if data is not None else default


def save_json(path: Path, data: Any, verbose: bool = False) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
        f.write("\n")
    if verbose:
        log(f"Wrote {path}", verbose)


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8", errors="replace")


def slugify(text: str) -> str:
    slug = re.sub(r"[^a-z0-9]+", "-", text.lower().strip())
    return slug.strip("-") or "doc"


def classify_document(path: Path, content: str) -> str:
    name = path.stem.lower()
    lower = content.lower()[:2000]

    if any(k in name for k in ("terms", "t-c", "tc-", "legal", "contract")):
        return DOC_BOILERPLATE_TERMS
    if any(k in name for k in ("about", "company", "overview")):
        return DOC_BOILERPLATE_ABOUT
    if any(k in name for k in ("bio", "bios", "team", "cv", "resume")):
        return DOC_BOILERPLATE_BIOS
    if any(k in name for k in ("scope", "sow", "deliverable", "statement-of-work")):
        return DOC_SCOPE
    if any(k in name for k in ("case-study", "casestudy", "case_study", "portfolio", "success")):
        return DOC_CASE_STUDY
    if any(k in name for k in ("proposal", "quote", "pricing", "estimate")):
        return DOC_PRICING

    if re.search(r"\b(case study|client success|testimonial)\b", lower):
        return DOC_CASE_STUDY
    if re.search(r"\b(total|line item|pricing|quote|estimate)\b", lower) and re.search(
        r"\$\s*[\d,]+", content
    ):
        return DOC_PRICING
    if re.search(r"\b(terms and conditions|liability|governing law)\b", lower):
        return DOC_BOILERPLATE_TERMS
    if re.search(r"\b(about us|our company|who we are)\b", lower):
        return DOC_BOILERPLATE_ABOUT
    if re.search(r"\b(deliverables|scope of work|milestones)\b", lower):
        return DOC_SCOPE

    return DOC_UNKNOWN


def extract_field(patterns: list[str], content: str, default: str = "") -> str:
    for pattern in patterns:
        match = re.search(pattern, content, re.IGNORECASE | re.MULTILINE)
        if match:
            return match.group(1).strip()
    return default


def extract_tags(content: str) -> list[str]:
    tag_match = re.search(
        r"(?:tags?|keywords?)\s*:\s*(.+)$", content, re.IGNORECASE | re.MULTILINE
    )
    if not tag_match:
        return []
    raw = tag_match.group(1)
    return [t.strip() for t in re.split(r"[,;|]", raw) if t.strip()]


def extract_deliverables(content: str) -> list[str]:
    items: list[str] = []
    in_section = False
    for line in content.splitlines():
        if re.match(r"^#+\s*deliverables?\b", line, re.IGNORECASE):
            in_section = True
            continue
        if in_section and re.match(r"^#+\s", line):
            break
        if in_section:
            bullet = re.match(r"^[-*]\s+(.+)", line.strip())
            if bullet:
                items.append(bullet.group(1).strip())
    return items


def extract_line_items(content: str) -> list[dict[str, Any]]:
    items: list[dict[str, Any]] = []
    for line in content.splitlines():
        match = re.match(
            r"^[-*]\s+(.+?)\s*\$\s*([\d,]+(?:\.\d{2})?)", line.strip()
        )
        if match:
            items.append(
                {
                    "description": re.sub(r"\s*[-–—:]+\s*$", "", match.group(1)).strip(),
                    "amount": float(match.group(2).replace(",", "")),
                }
            )
    return items


def extract_total(content: str) -> float | None:
    patterns = [
        r"total\s*[:=]\s*\$?\s*([\d,]+(?:\.\d{2})?)",
        r"grand\s+total\s*[:=]?\s*\$?\s*([\d,]+(?:\.\d{2})?)",
        r"\$\s*([\d,]+(?:\.\d{2})?)\s*(?:total|usd)?",
    ]
    for pattern in patterns:
        match = re.search(pattern, content, re.IGNORECASE)
        if match:
            return float(match.group(1).replace(",", ""))
    return None


def make_case_study_entry(
    rel_path: str, content: str, doc_id: str
) -> dict[str, Any]:
    client = extract_field(
        [r"^client\s*:\s*(.+)$", r"^#+\s*client\s*:\s*(.+)$"],
        content,
        default=Path(rel_path).stem.replace("-", " ").title(),
    )
    return {
        "id": doc_id,
        "client": client,
        "industry": extract_field(
            [r"^industry\s*:\s*(.+)$", r"^#+\s*industry\s*:\s*(.+)$"], content
        ),
        "serviceType": extract_field(
            [
                r"^service(?:\s*type)?\s*:\s*(.+)$",
                r"^#+\s*service\s*:\s*(.+)$",
            ],
            content,
        ),
        "deliverables": extract_deliverables(content),
        "outcome": extract_field(
            [r"^outcome\s*:\s*(.+)$", r"^#+\s*outcome\s*:\s*(.+)$"], content
        ),
        "testimonial": extract_field(
            [r"^testimonial\s*:\s*(.+)$", r'^>\s*"(.+)"'], content
        ),
        "tags": extract_tags(content),
        "sourceDocPath": rel_path,
        "ingestedAt": datetime.now(timezone.utc).isoformat(),
    }


def make_pricing_entry(rel_path: str, content: str) -> dict[str, Any]:
    line_items = extract_line_items(content)
    total = extract_total(content)
    if total is None and line_items:
        total = sum(item["amount"] for item in line_items)

    won_raw = extract_field([r"^won\s*:\s*(.+)$", r"^status\s*:\s*(.+)$"], content)
    won: bool | None = None
    if won_raw:
        lower = won_raw.lower()
        if lower in ("yes", "true", "won"):
            won = True
        elif lower in ("no", "false", "lost"):
            won = False

    return {
        "date": extract_field(
            [r"^date\s*:\s*(.+)$", r"^#+\s*date\s*:\s*(.+)$"],
            content,
            default=datetime.now(timezone.utc).strftime("%Y-%m-%d"),
        ),
        "client": extract_field(
            [r"^client\s*:\s*(.+)$", r"^#+\s*client\s*:\s*(.+)$"],
            content,
            default=Path(rel_path).stem.replace("-", " ").title(),
        ),
        "proposalType": extract_field(
            [r"^proposal\s*type\s*:\s*(.+)$", r"^type\s*:\s*(.+)$"],
            content,
            default="pitch",
        ),
        "lineItems": line_items,
        "total": total,
        "won": won,
        "clientFeedback": extract_field(
            [r"^client\s*feedback\s*:\s*(.+)$", r"^feedback\s*:\s*(.+)$"],
            content,
        ),
        "sourceDocPath": rel_path,
        "ingestedAt": datetime.now(timezone.utc).isoformat(),
    }


def upsert_by_source(
    entries: list[dict[str, Any]], new_entry: dict[str, Any], key: str = "sourceDocPath"
) -> list[dict[str, Any]]:
    source = new_entry.get(key)
    filtered = [e for e in entries if e.get(key) != source]
    filtered.append(new_entry)
    return filtered


def upsert_case_study_by_id(
    entries: list[dict[str, Any]], new_entry: dict[str, Any]
) -> list[dict[str, Any]]:
    doc_id = new_entry["id"]
    filtered = [e for e in entries if e.get("id") != doc_id]
    filtered.append(new_entry)
    return filtered


def append_boilerplate(
    target_path: Path, rel_path: str, content: str, verbose: bool
) -> None:
    target_path.parent.mkdir(parents=True, exist_ok=True)
    section_title = Path(rel_path).stem.replace("-", " ").title()
    block = (
        f"\n\n<!-- ingested from {rel_path} -->\n\n"
        f"## {section_title}\n\n{content.strip()}\n"
    )
    if target_path.exists():
        existing = read_text(target_path)
        marker = f"<!-- ingested from {rel_path} -->"
        if marker in existing:
            log(f"Skipping duplicate boilerplate section for {rel_path}", verbose)
            return
        target_path.write_text(existing.rstrip() + block, encoding="utf-8")
    else:
        target_path.write_text(f"# {target_path.stem.replace('-', ' ').title()}\n{block}", encoding="utf-8")
    log(f"Appended boilerplate to {target_path}", verbose)


def append_scope_template(
    scope_path: Path, rel_path: str, content: str, verbose: bool
) -> None:
    scope_path.parent.mkdir(parents=True, exist_ok=True)
    section_key = slugify(Path(rel_path).stem)
    marker = f"<!-- scope-source: {rel_path} -->"
    block = f"\n\n{marker}\n\n## {section_key.replace('-', ' ').title()}\n\n{content.strip()}\n"

    if scope_path.exists():
        existing = read_text(scope_path)
        if marker in existing:
            log(f"Skipping duplicate scope section for {rel_path}", verbose)
            return
        scope_path.write_text(existing.rstrip() + block, encoding="utf-8")
    else:
        scope_path.write_text(
            "# Scope Templates\n\n<!-- Reusable scope/deliverable clauses -->\n" + block,
            encoding="utf-8",
        )
    log(f"Appended scope template from {rel_path}", verbose)


def list_inbox_files(inbox: Path) -> list[Path]:
    if not inbox.exists():
        return []
    files: list[Path] = []
    for path in sorted(inbox.rglob("*")):
        if path.is_file() and path.suffix.lower() in SUPPORTED_EXTENSIONS:
            if path.name.startswith("."):
                continue
            files.append(path)
    return files


def load_manifest(manifest_path: Path) -> dict[str, Any]:
    data = load_json(manifest_path, {"version": MANIFEST_VERSION, "files": {}})
    if "files" not in data:
        data["files"] = {}
    return data


def update_index_md(memory_root: Path, case_count: int, pricing_count: int, verbose: bool) -> None:
    index_path = memory_root / "index.md"
    if not index_path.exists():
        return

    now = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")
    content = read_text(index_path)
    table_row = f"| Case studies | {case_count} | {now} |\n| Pricing history | {pricing_count} | {now} |"

    if "| Case studies |" in content:
        content = re.sub(
            r"\| Case studies \|[^\n]+\n\| Pricing history \|[^\n]+\n",
            table_row + "\n",
            content,
        )
    else:
        content = content.replace(
            "## Library\n",
            f"## Library\n| Index | Entries | Last re-index |\n|-------|---------|---------------|\n{table_row}\n",
        )

    index_path.write_text(content, encoding="utf-8")
    log(f"Updated {index_path} library stats", verbose)


def validate_indexes(
    memory_root: Path, manifest: dict[str, Any], verbose: bool
) -> dict[str, Any]:
    library = memory_root / "library"
    inbox = library / "inbox"
    case_index = load_json(library / "case-studies-index.json", [])
    pricing_index = load_json(library / "pricing-history.json", [])

    issues: list[dict[str, str]] = []
    manifest_files = manifest.get("files", {})

    for entry in case_index:
        source = entry.get("sourceDocPath", "")
        full = inbox / source if source else None
        if not source or not full or not full.exists():
            issues.append(
                {
                    "type": "orphaned_case_study",
                    "id": entry.get("id", ""),
                    "sourceDocPath": source,
                    "message": "Case study index entry references missing inbox file",
                }
            )

    for entry in pricing_index:
        source = entry.get("sourceDocPath", "")
        full = inbox / source if source else None
        if not source or not full or not full.exists():
            issues.append(
                {
                    "type": "orphaned_pricing",
                    "sourceDocPath": source,
                    "message": "Pricing history entry references missing inbox file",
                }
            )

    indexed_sources = set()
    for entry in case_index:
        if entry.get("sourceDocPath"):
            indexed_sources.add(entry["sourceDocPath"])
    for entry in pricing_index:
        if entry.get("sourceDocPath"):
            indexed_sources.add(entry["sourceDocPath"])

    for rel, meta in manifest_files.items():
        full = inbox / rel
        if not full.exists():
            issues.append(
                {
                    "type": "stale_manifest",
                    "sourceDocPath": rel,
                    "message": "Manifest references file no longer in inbox",
                }
            )
        elif rel not in indexed_sources and meta.get("doc_type") not in (
            DOC_BOILERPLATE_ABOUT,
            DOC_BOILERPLATE_TERMS,
            DOC_BOILERPLATE_BIOS,
            DOC_SCOPE,
        ):
            issues.append(
                {
                    "type": "unindexed",
                    "sourceDocPath": rel,
                    "message": "Inbox file in manifest but not represented in JSON indexes",
                }
            )

    for path in list_inbox_files(inbox):
        rel = path.relative_to(inbox).as_posix()
        if rel not in manifest_files:
            issues.append(
                {
                    "type": "not_ingested",
                    "sourceDocPath": rel,
                    "message": "Inbox file has never been ingested",
                }
            )

    report = {
        "status": "ok" if not issues else "issues_found",
        "validatedAt": datetime.now(timezone.utc).isoformat(),
        "caseStudyCount": len(case_index),
        "pricingHistoryCount": len(pricing_index),
        "manifestFileCount": len(manifest_files),
        "issueCount": len(issues),
        "issues": issues,
    }
    log(f"Validation: {len(issues)} issue(s)", verbose)
    return report


def process_inbox(
    memory_root: Path,
    inbox: Path,
    force: bool,
    verbose: bool,
) -> dict[str, Any]:
    library = memory_root / "library"
    brand_boilerplate = memory_root / "brand" / "boilerplate"
    manifest_path = library / "ingest-manifest.json"
    case_path = library / "case-studies-index.json"
    pricing_path = library / "pricing-history.json"
    scope_path = library / "scope-templates.md"

    inbox.mkdir(parents=True, exist_ok=True)
    manifest = load_manifest(manifest_path)
    case_index: list[dict[str, Any]] = load_json(case_path, [])
    pricing_index: list[dict[str, Any]] = load_json(pricing_path, [])

    processed = 0
    skipped = 0
    warnings: list[str] = []
    results: list[dict[str, Any]] = []

    for path in list_inbox_files(inbox):
        rel = path.relative_to(inbox).as_posix()
        file_hash = sha256_file(path)
        prev = manifest["files"].get(rel)

        if not force and prev and prev.get("sha256") == file_hash:
            skipped += 1
            log(f"Skipping unchanged: {rel}", verbose)
            continue

        content = read_text(path)
        doc_type = classify_document(path, content)
        doc_id = slugify(f"{path.stem}-{file_hash[:8]}")

        entry_result: dict[str, Any] = {
            "sourceDocPath": rel,
            "docType": doc_type,
            "action": "processed",
        }

        if doc_type == DOC_CASE_STUDY:
            cs = make_case_study_entry(rel, content, doc_id)
            case_index = upsert_case_study_by_id(case_index, cs)
            entry_result["caseStudyId"] = cs["id"]
        elif doc_type == DOC_PRICING:
            pe = make_pricing_entry(rel, content)
            pricing_index = upsert_by_source(pricing_index, pe)
            entry_result["pricingClient"] = pe.get("client")
        elif doc_type in BOILERPLATE_TARGETS:
            append_boilerplate(
                brand_boilerplate / BOILERPLATE_TARGETS[doc_type],
                rel,
                content,
                verbose,
            )
            entry_result["boilerplateTarget"] = BOILERPLATE_TARGETS[doc_type]
        elif doc_type == DOC_SCOPE:
            append_scope_template(scope_path, rel, content, verbose)
            entry_result["scopeSection"] = slugify(path.stem)
        else:
            # Default thin briefs / general docs → case study with minimal fields
            cs = make_case_study_entry(rel, content, doc_id)
            case_index = upsert_case_study_by_id(case_index, cs)
            entry_result["docType"] = DOC_CASE_STUDY
            entry_result["caseStudyId"] = cs["id"]
            warnings.append(
                f"Unclassified doc '{rel}' indexed as case study — add Client:/Industry: fields or rename for better routing"
            )

        manifest["files"][rel] = {
            "sha256": file_hash,
            "ingestedAt": datetime.now(timezone.utc).isoformat(),
            "docType": entry_result["docType"],
        }
        processed += 1
        results.append(entry_result)
        log(f"Processed {rel} as {entry_result['docType']}", verbose)

    save_json(case_path, case_index, verbose)
    save_json(pricing_path, pricing_index, verbose)
    save_json(manifest_path, manifest, verbose)
    update_index_md(memory_root, len(case_index), len(pricing_index), verbose)

    return {
        "status": "success",
        "processed": processed,
        "skipped": skipped,
        "caseStudyCount": len(case_index),
        "pricingHistoryCount": len(pricing_index),
        "warnings": warnings,
        "results": results,
    }


def main() -> None:
    args = parse_args()
    memory_root = Path(args.memory_root).resolve()
    inbox = Path(args.inbox).resolve() if args.inbox else memory_root / "library" / "inbox"

    if not memory_root.exists() and not args.validate:
        print(
            f"Error: memory root does not exist: {memory_root}. Run paw-pa-setup first.",
            file=sys.stderr,
        )
        sys.exit(1)

    manifest_path = memory_root / "library" / "ingest-manifest.json"
    manifest = load_manifest(manifest_path)

    if args.validate:
        report = validate_indexes(memory_root, manifest, args.verbose)
        if args.report_path:
            report_path = Path(args.report_path)
            report_path.parent.mkdir(parents=True, exist_ok=True)
            save_json(report_path, report, args.verbose)
            report["reportPath"] = str(report_path.resolve())
        print(json.dumps(report, indent=2))
        sys.exit(1 if report["issueCount"] else 0)

    summary = process_inbox(memory_root, inbox, args.force, args.verbose)
    print(json.dumps(summary, indent=2))


if __name__ == "__main__":
    main()
