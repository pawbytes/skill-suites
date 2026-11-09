#!/usr/bin/env python3
# /// script
# requires-python = ">=3.11"
# dependencies = ["playwright>=1.45", "pillow>=10", "pypdf>=4"]
# ///
"""Export every approved frame of a PawBytes Graphics Suite project to its placement.

Reads layout/layout.json for the frames and compose/<frame>/design.html for each design.
Format per placement: print gets a vector PDF at trim + bleed plus a small PNG proof;
digital gets a PNG at the placement's pixel size (scaled from the design canvas when the
design was built smaller at the same aspect), switching to JPEG stepped down to the file
cap when the PNG is too heavy or the placement takes no PNG. Every export is measured and
QC-checked; results land in deliver/manifest.json and deliver/qc.json. Placements that take
only documents (LinkedIn document posts) get one PDF page per frame, merged in layout order
into deliver/<placement>/<slug>-document.pdf.

Subcommands:
  plan --project DIR [--frame ID]       what would be written, without rendering
  run  --project DIR [--frame ID] [--no-proof]   (--frame merges into the existing reports)
  zip  --project DIR                    deliver/<slug>-deliverables.zip (exports, qc.json, alt-text.md)

`run` refuses while the deliver gate is blocked (compose not approved).
Output: JSON on stdout; `run` exits 1 when any export fails QC. Errors: JSON on stderr, exit 2.
"""
from __future__ import annotations

import argparse
import json
import sys
import zipfile
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import production  # noqa: E402  (bundled beside these scripts)
import qc  # noqa: E402
import render  # noqa: E402
import specs  # noqa: E402

SKIP_IN_ZIP = (".measure.json", ".thumb.png")


class Fail(Exception):
    pass


def out(obj: dict, code: int = 0) -> None:
    print(json.dumps(obj, indent=2, ensure_ascii=False), flush=True)
    sys.exit(code)


def frames_of(project: Path, only: str | None) -> list[dict]:
    path = project / "layout" / "layout.json"
    if not path.is_file():
        raise Fail(f"no layout at {path}")
    frs = json.loads(path.read_text(encoding="utf-8")).get("frames", [])
    if only:
        frs = [f for f in frs if f.get("id") == only]
        if not frs:
            raise Fail(f"no frame '{only}' in layout.json")
    return frs


def plan_frame(project: Path, fr: dict, data: dict) -> dict:
    pid, entry = specs.resolve(fr.get("placement", ""), data)
    html = project / "compose" / fr["id"] / "design.html"
    item = {"frame": fr["id"], "placement": pid, "html": str(html), "exists": html.is_file(), "outputs": []}
    folder = project / "deliver" / pid
    if entry["unit"] == "mm":
        item["outputs"].append({"format": "pdf", "out": str(folder / f"{fr['id']}.pdf")})
        item["outputs"].append({"format": "png", "out": str(folder / f"{fr['id']}.proof.png"), "dpi": 100,
                                "proof": True})
        return item
    formats = {f.split("-")[0] for f in entry.get("formats", [])}
    if "pdf" in formats and not formats & {"png", "jpg"}:
        item["outputs"].append({"format": "pdf", "out": str(folder / f"{fr['id']}.pdf"), "document": True})
        return item
    scale = 1.0
    if html.is_file():
        geo = render.canvas_for(html, None, None)
        cw, ch = geo["viewport"]
        if abs(cw / ch - entry["w"] / entry["h"]) > 0.01:
            item["error"] = (f"design canvas {cw}x{ch} does not match the {pid} aspect "
                             f"({entry['w']}x{entry['h']}); re-layout it rather than stretching")
        scale = entry["w"] / cw
    first = "png" if "png" in formats else "jpeg"
    item["outputs"].append({"format": first, "out": str(folder / f"{fr['id']}.{'png' if first == 'png' else 'jpg'}"),
                            "scale": round(scale, 4), "max_kb": entry.get("max_kb"),
                            "fallback_jpeg": first == "png" and ("jpg" in formats)})
    return item


def cmd_plan(a) -> None:
    project = Path(a.project)
    data = specs.load()
    out({"ok": True, "plan": [plan_frame(project, fr, data) for fr in frames_of(project, a.frame)]})


def cmd_run(a) -> None:
    project = Path(a.project)
    reasons = production.stage_gate(project, "deliver")
    if reasons:
        out({"ok": False, "blocked": True, "stage": "deliver", "reasons": reasons}, 1)
    data = specs.load()
    manifest, failed = [], []
    for fr in frames_of(project, a.frame):
        item = plan_frame(project, fr, data)
        if not item["exists"]:
            raise Fail(f"{fr['id']}: no design at {item['html']}; compose it first")
        if item.get("error"):
            raise Fail(f"{fr['id']}: {item['error']}")
        pid, entry = specs.resolve(item["placement"], data)
        files = []
        for o in item["outputs"]:
            if o.get("proof") and a.no_proof:
                continue
            html = Path(item["html"])
            if o["format"] == "pdf":
                res = render.render_file(html, Path(o["out"]), "pdf", measure=True)
            elif o.get("proof"):
                res = render.render_file(html, Path(o["out"]), "png", dpi=o["dpi"])
            else:
                res = render.render_file(html, Path(o["out"]), o["format"], scale=o["scale"],
                                         max_kb=o["max_kb"], measure=True)
                if o["format"] == "png" and o.get("fallback_jpeg") and o["max_kb"] and res["kb"] > o["max_kb"]:
                    png = Path(o["out"])
                    jpg = png.with_suffix(".jpg")
                    res = render.render_file(html, jpg, "jpeg", scale=o["scale"], max_kb=o["max_kb"], measure=True)
                    png.unlink(missing_ok=True)
                    res["note"] = "PNG was over the file cap; exported as JPEG"
            entry_res = {"out": res["out"], "format": res["format"], "kb": res["kb"], "warnings": res["warnings"]}
            if not o.get("proof"):
                check = qc.check_file(Path(res["out"]), pid, entry, data, None)
                entry_res["qc"] = {"ok": check["ok"], "fails": check["fails"], "warns": check["warns"]}
                if not check["ok"]:
                    failed.append(res["out"])
            files.append(entry_res)
        manifest.append({"frame": fr["id"], "placement": pid, "files": files})
    deliver = project / "deliver"
    deliver.mkdir(parents=True, exist_ok=True)
    if a.frame and (deliver / "manifest.json").is_file():  # a single frame joins the earlier full run
        earlier = json.loads((deliver / "manifest.json").read_text(encoding="utf-8")).get("frames", [])
        done = {m["frame"] for m in manifest}
        manifest = [m for m in earlier if m["frame"] not in done] + manifest
        failed = [f["out"] for m in manifest for f in m["files"] if f.get("qc") and not f["qc"]["ok"]]
    documents = merge_documents(project, manifest)
    report = {"ok": not failed, "failed": failed, "frames": manifest, "documents": documents}
    (deliver / "manifest.json").write_text(json.dumps(report, indent=2, ensure_ascii=False), encoding="utf-8")
    try:
        qc_report = {"ok": not failed, "files": sum(len(m["files"]) for m in manifest), "failed": failed,
                     "results": [dict(file=f["out"], placement=m["placement"], **f.get("qc", {}))
                                 for m in manifest for f in m["files"] if "qc" in f]}
        (deliver / "qc.json").write_text(json.dumps(qc_report, indent=2, ensure_ascii=False), encoding="utf-8")
    except OSError as exc:
        raise Fail(f"could not write qc.json: {exc}")
    out({**report, "manifest": str(deliver / "manifest.json"), "qc": str(deliver / "qc.json")}, 0 if not failed else 1)


def merge_documents(project: Path, manifest: list[dict]) -> list[str]:
    """One multi-page PDF per document placement, pages in layout order."""
    from pypdf import PdfWriter

    data = specs.load()
    slug = json.loads((project / "production.json").read_text(encoding="utf-8")).get("slug", project.name)
    merged = []
    by_placement: dict[str, list[str]] = {}
    for m in manifest:
        _, entry = specs.resolve(m["placement"], data)
        formats = {f.split("-")[0] for f in entry.get("formats", [])}
        if "pdf" in formats and not formats & {"png", "jpg"}:
            by_placement.setdefault(m["placement"], []).extend(f["out"] for f in m["files"] if f["format"] == "pdf")
    order = [fr["id"] for fr in frames_of(project, None)]
    for pid, pages in by_placement.items():
        pages.sort(key=lambda path: order.index(Path(path).stem) if Path(path).stem in order else len(order))
        writer = PdfWriter()
        for page in pages:
            writer.append(page)
        dest = project / "deliver" / pid / f"{slug}-document.pdf"
        with open(dest, "wb") as fh:
            writer.write(fh)
        merged.append(str(dest))
    return merged


def cmd_zip(a) -> None:
    project = Path(a.project)
    deliver = project / "deliver"
    if not deliver.is_dir():
        raise Fail(f"no deliver/ folder in {project}")
    slug = json.loads((project / "production.json").read_text(encoding="utf-8")).get("slug", project.name)
    dest = deliver / f"{slug}-deliverables.zip"
    added = []
    with zipfile.ZipFile(dest, "w", zipfile.ZIP_DEFLATED) as z:
        for f in sorted(deliver.rglob("*")):
            if not f.is_file() or f == dest or f.suffix == ".zip" or f.name.endswith(SKIP_IN_ZIP):
                continue
            arc = f.relative_to(deliver).as_posix()
            z.write(f, arc)
            added.append(arc)
    out({"ok": True, "zip": str(dest), "files": added})


def main(argv=None) -> None:
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = p.add_subparsers(dest="cmd", required=True)
    for name, fn in (("plan", cmd_plan), ("run", cmd_run)):
        s = sub.add_parser(name)
        s.add_argument("--project", required=True)
        s.add_argument("--frame")
        if name == "run":
            s.add_argument("--no-proof", action="store_true")
        s.set_defaults(fn=fn)
    s = sub.add_parser("zip")
    s.add_argument("--project", required=True)
    s.set_defaults(fn=cmd_zip)
    for stream in (sys.stdout, sys.stderr):
        if hasattr(stream, "reconfigure"):
            stream.reconfigure(encoding="utf-8")
    a = p.parse_args(argv)
    try:
        a.fn(a)
    except (Fail, production.Fail, render.Fail, specs.Fail, qc.Fail) as exc:
        print(json.dumps({"ok": False, "error": str(exc)}), file=sys.stderr)
        sys.exit(2)
    except Exception as exc:  # noqa: BLE001
        print(json.dumps({"ok": False, "error": f"{type(exc).__name__}: {exc}"}), file=sys.stderr)
        sys.exit(2)


if __name__ == "__main__":
    main()
