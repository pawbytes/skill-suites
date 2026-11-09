#!/usr/bin/env python3
# /// script
# requires-python = ">=3.11"
# dependencies = ["pillow>=10"]
# ///
"""Image asset register for PawBytes Graphics Suite: {project}/imagery/assets.json.

Every image a design uses is named once (hero, plate, product, logo, texture) and picked
here; layout elements point at the name, compose reads the path. Provenance travels with
each pick, because ad platforms label AI imagery and the alt text and disclosure come from it.

Subcommands:
  import --project DIR --file PATH --name N --kind K [--note T]
         copy a user image into imagery/source/ (the original is never modified) and pick it
  pick   --project DIR --name N --path REL --kind K --source fal|codex|user|stock
         [--frames a,b] [--copy-space TEXT] [--provenance TEXT] [--licence TEXT]
  reject --project DIR --name N --take REL --reason TEXT
  list   --project DIR
  check  --project DIR [--scale 1]
         every image and logo element in layout/layout.json has a pick whose file exists, is
         big enough for its box (print boxes at the placement's dpi) and is not cropped away

Kinds: plate, hero, cutout, texture, logo, photo, illustration. Paths are project-relative.
Output: JSON on stdout; `check` exits 1 on problems. Errors: JSON on stderr, exit 2.
"""
from __future__ import annotations

import argparse
import json
import shutil
import sys
from datetime import datetime, timezone
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import frames  # noqa: E402  (bundled beside this script)
import specs  # noqa: E402

KINDS = ["plate", "hero", "cutout", "texture", "logo", "photo", "illustration"]
SOURCES = ["fal", "codex", "user", "stock"]


class Fail(Exception):
    pass


def out(obj: dict, code: int = 0) -> None:
    print(json.dumps(obj, indent=2, ensure_ascii=False), flush=True)
    sys.exit(code)


def now() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat()


def reg_path(project: Path) -> Path:
    return project / "imagery" / "assets.json"


def load(project: Path) -> dict:
    p = reg_path(project)
    if not p.is_file():
        return {"assets": {}, "rejected": {}}
    return json.loads(p.read_text(encoding="utf-8"))


def save(project: Path, data: dict) -> None:
    p = reg_path(project)
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")


def _size(path: Path) -> tuple[int, int] | None:
    if path.suffix.lower() == ".svg":
        return None
    from PIL import Image

    with Image.open(path) as im:
        return im.size


def record(project: Path, name: str, rel: str, kind: str, source: str, **extra) -> dict:
    path = project / rel
    if not path.is_file():
        raise Fail(f"no file at {path}")
    size = _size(path)
    data = load(project)
    entry = {"path": Path(rel).as_posix(), "kind": kind, "source": source,
             "w": size[0] if size else None, "h": size[1] if size else None, "picked_at": now()}
    entry.update({k: v for k, v in extra.items() if v})
    data["assets"][name] = entry
    save(project, data)
    return entry


def cmd_import(a) -> None:
    project = Path(a.project)
    src = Path(a.file)
    if not src.is_file():
        raise Fail(f"no such file: {src}")
    dest = project / "imagery" / "source" / src.name
    dest.parent.mkdir(parents=True, exist_ok=True)
    if dest.exists() and dest.read_bytes() != src.read_bytes():
        dest = dest.with_name(f"{dest.stem}-{datetime.now().strftime('%H%M%S')}{dest.suffix}")
    shutil.copyfile(src, dest)
    rel = dest.relative_to(project).as_posix()
    entry = record(project, a.name, rel, a.kind, "user", note=a.note, original=str(src),
                   provenance="user-supplied original")
    out({"ok": True, "name": a.name, **entry})


def cmd_pick(a) -> None:
    project = Path(a.project)
    entry = record(project, a.name, a.path, a.kind, a.source,
                   frames=[f for f in (a.frames or "").split(",") if f], copy_space=a.copy_space,
                   provenance=a.provenance or ("AI-generated" if a.source in ("fal", "codex") else None),
                   licence=a.licence)
    out({"ok": True, "name": a.name, **entry})


def cmd_reject(a) -> None:
    project = Path(a.project)
    data = load(project)
    data.setdefault("rejected", {}).setdefault(a.name, []).append(f"{a.take}: {a.reason}")
    save(project, data)
    out({"ok": True, "name": a.name, "rejected": data["rejected"][a.name]})


def cmd_list(a) -> None:
    out({"ok": True, **load(Path(a.project))})


def cmd_check(a) -> None:
    project = Path(a.project)
    layout_path = project / "layout" / "layout.json"
    if not layout_path.is_file():
        raise Fail(f"no layout at {layout_path}")
    layout = json.loads(layout_path.read_text(encoding="utf-8"))
    data = load(project)
    cat = specs.load()
    problems, warns, needs = [], [], []
    for fr in layout.get("frames", []):
        _, entry = specs.resolve(fr.get("placement", ""), cat)
        g = frames.geometry(entry)
        px_per_css = (entry.get("dpi", 300) / 96) if entry["unit"] == "mm" else a.scale
        for el in fr.get("elements", []):
            if el.get("role") not in ("image", "logo") or el.get("src"):
                continue
            name = el.get("asset")
            where = f"{fr.get('id')}/{el.get('id')}"
            if not name:
                problems.append(f"{where}: {el['role']} element names no asset")
                continue
            pick = data["assets"].get(name)
            if not pick:
                problems.append(f"{where}: asset '{name}' is not picked")
                continue
            path = project / pick["path"]
            if not path.is_file():
                problems.append(f"{where}: picked file {pick['path']} is missing")
                continue
            box = frames.box_px(el, g)
            need_w, need_h = box[2] * px_per_css, box[3] * px_per_css
            needs.append({"frame": fr.get("id"), "element": el.get("id"), "asset": name,
                          "need_px": [round(need_w), round(need_h)], "have_px": [pick.get("w"), pick.get("h")]})
            if not pick.get("w"):
                continue  # vector
            fit = el.get("fit", "cover" if el["role"] == "image" else "contain")
            scale_needed = max(need_w / pick["w"], need_h / pick["h"]) if fit == "cover" else \
                min(need_w / pick["w"], need_h / pick["h"])
            if scale_needed > 1.5:
                problems.append(f"{where}: {name} is {pick['w']}x{pick['h']}; the box needs about "
                                f"{need_w:.0f}x{need_h:.0f}px, so it would be upscaled {scale_needed:.1f}x "
                                "(generate larger or run an upscaler)")
            elif scale_needed > 1.05:
                warns.append(f"{where}: {name} is upscaled {scale_needed:.2f}x; check softness at 100%")
            if fit == "cover":
                box_ar, img_ar = need_w / need_h, pick["w"] / pick["h"]
                kept = min(box_ar, img_ar) / max(box_ar, img_ar)
                if kept < 0.6:
                    warns.append(f"{where}: {name} keeps only {kept:.0%} of its {'width' if img_ar > box_ar else 'height'}"
                                 " at this crop; generate at the box's aspect or set a focal point")
    for name, pick in data["assets"].items():
        if pick.get("source") in ("fal", "codex") and not pick.get("provenance"):
            warns.append(f"{name}: AI-generated with no provenance note; ad platforms may require a label")
    out({"ok": not problems, "problems": problems, "warnings": warns, "slots": needs}, 0 if not problems else 1)


def main(argv=None) -> None:
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = p.add_subparsers(dest="cmd", required=True)
    s = sub.add_parser("import")
    s.add_argument("--project", required=True)
    s.add_argument("--file", required=True)
    s.add_argument("--name", required=True)
    s.add_argument("--kind", required=True, choices=KINDS)
    s.add_argument("--note")
    s.set_defaults(fn=cmd_import)
    s = sub.add_parser("pick")
    s.add_argument("--project", required=True)
    s.add_argument("--name", required=True)
    s.add_argument("--path", required=True)
    s.add_argument("--kind", required=True, choices=KINDS)
    s.add_argument("--source", required=True, choices=SOURCES)
    s.add_argument("--frames")
    s.add_argument("--copy-space")
    s.add_argument("--provenance")
    s.add_argument("--licence")
    s.set_defaults(fn=cmd_pick)
    s = sub.add_parser("reject")
    s.add_argument("--project", required=True)
    s.add_argument("--name", required=True)
    s.add_argument("--take", required=True)
    s.add_argument("--reason", required=True)
    s.set_defaults(fn=cmd_reject)
    s = sub.add_parser("list")
    s.add_argument("--project", required=True)
    s.set_defaults(fn=cmd_list)
    s = sub.add_parser("check")
    s.add_argument("--project", required=True)
    s.add_argument("--scale", type=float, default=1.0, help="device scale the digital renders use")
    s.set_defaults(fn=cmd_check)
    for stream in (sys.stdout, sys.stderr):
        if hasattr(stream, "reconfigure"):
            stream.reconfigure(encoding="utf-8")
    a = p.parse_args(argv)
    try:
        a.fn(a)
    except (Fail, specs.Fail, frames.Fail) as exc:
        print(json.dumps({"ok": False, "error": str(exc)}), file=sys.stderr)
        sys.exit(2)
    except Exception as exc:  # noqa: BLE001
        print(json.dumps({"ok": False, "error": f"{type(exc).__name__}: {exc}"}), file=sys.stderr)
        sys.exit(2)


if __name__ == "__main__":
    main()
