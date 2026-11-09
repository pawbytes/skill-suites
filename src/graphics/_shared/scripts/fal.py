#!/usr/bin/env python3
# /// script
# requires-python = ">=3.11"
# dependencies = ["fal-client>=0.5"]
# ///
"""fal.ai client for PawBytes Graphics Suite: discover models, read their input
schema, price and estimate, upload, run and download.

Auth: FAL_KEY in the environment. Model discovery works without it (lower
rate limits); pricing, upload and run need it.

With --project, `run` enforces the production gate for --stage (earlier stages
approved or skipped) and the project budget, then logs the estimated cost to
production.json. Outputs are downloaded at once because fal result URLs are
not permanent; the raw result JSON is kept beside them and in {project}/fal/.

Output: one JSON object on stdout; progress on stderr; errors as JSON on
stderr with exit 2. A blocked gate or budget exits 1 with reasons.

Subcommands:
  models   [--q TEXT] [--category text-to-image] [--limit 20]
  schema   ENDPOINT                      input fields, types, defaults, enums, required
  price    ENDPOINT [ENDPOINT ...]       unit price and billing unit
  estimate --item ENDPOINT=UNITS [...]   total USD for planned usage (unit_price mode)
  upload   FILE [FILE ...]               fal CDN URLs for local files
  run      ENDPOINT --args @file.json [--units N] [--project DIR --stage S]
           [--out DIR] [--name BASE] [--timeout 1800] [--estimate-usd X]
  result   ENDPOINT REQUEST_ID [--args @file] [--project DIR --stage S --units N] [--out DIR] [--name BASE]
           [--cost-logged]

Exit codes: 0 ok; 1 blocked by gate or budget, or timed out (resume command in the output);
2 error, including a failed download after a paid request (resume command in the output).
Write --args to a file and pass @file: PowerShell strips the quotes from inline JSON.
With --project, relative paths in --out, --args @file and file-valued args resolve under the project.
"""
from __future__ import annotations

import argparse
import base64
import json
import mimetypes
import os
import re
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
from datetime import datetime, timezone
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import production  # noqa: E402  (bundled beside this script)

API = "https://api.fal.ai/v1"


class Fail(Exception):
    pass


def out(obj: dict, code: int = 0) -> None:
    print(json.dumps(obj, indent=2, ensure_ascii=False), flush=True)
    sys.exit(code)


def progress(msg: str) -> None:
    print(msg, file=sys.stderr, flush=True)


def key(required: bool = True) -> str | None:
    k = os.environ.get("FAL_KEY")
    if required and not k:
        raise Fail("FAL_KEY is not set. Get a key at https://fal.ai/dashboard/keys and set it in your shell "
                   "(PowerShell: $env:FAL_KEY='...'; bash: export FAL_KEY=...).")
    return k


def api(method: str, path: str, params: dict | list | None = None, body: dict | None = None,
        auth: bool = True) -> dict:
    url = f"{API}{path}"
    if params:
        url += "?" + urllib.parse.urlencode(params, doseq=True)
    headers = {"Accept": "application/json"}
    k = key(required=auth)
    if k:
        headers["Authorization"] = f"Key {k}"
    data = None
    if body is not None:
        data = json.dumps(body).encode()
        headers["Content-Type"] = "application/json"
    req = urllib.request.Request(url, data=data, headers=headers, method=method)
    try:
        with urllib.request.urlopen(req, timeout=60) as resp:
            return json.loads(resp.read().decode())
    except urllib.error.HTTPError as exc:
        detail = exc.read().decode(errors="replace")[:500]
        raise Fail(f"fal API {method} {path} failed: HTTP {exc.code} {detail}")
    except urllib.error.URLError as exc:
        raise Fail(f"fal API unreachable: {exc.reason}")


def cmd_models(a) -> None:
    params: dict = {"limit": a.limit, "status": "active"}
    if a.q:
        params["q"] = a.q
    if a.category:
        params["category"] = a.category
    if a.recent:
        params["sort"] = "recent"
    res = api("GET", "/models", params, auth=False)
    models = [{"endpoint_id": m["endpoint_id"], "name": m.get("metadata", {}).get("display_name"),
               "category": m.get("metadata", {}).get("category"),
               "description": (m.get("metadata", {}).get("description") or "")[:200],
               "date": m.get("metadata", {}).get("date")} for m in res.get("models", [])]
    out({"ok": True, "count": len(models), "models": models, "has_more": res.get("has_more", False)})


def _resolve(ref: str, spec: dict) -> dict:
    node: dict = spec
    for part in ref.lstrip("#/").split("/"):
        node = node.get(part, {})
    return node


def cmd_schema(a) -> None:
    res = api("GET", "/models", {"endpoint_id": a.endpoint, "expand": "openapi-3.0"}, auth=False)
    models = res.get("models", [])
    if not models:
        raise Fail(f"no model '{a.endpoint}'; search with `fal.py models --q ...`")
    spec = models[0].get("openapi") or {}
    schema = None
    for path, ops in (spec.get("paths") or {}).items():
        post = ops.get("post") if isinstance(ops, dict) else None
        if not post or "requests" in path:
            continue
        content = (post.get("requestBody") or {}).get("content", {})
        js = content.get("application/json", {}).get("schema")
        if js:
            schema = _resolve(js["$ref"], spec) if "$ref" in js else js
            break
    if schema is None:
        raise Fail(f"no input schema published for {a.endpoint}")
    fields = []
    required = set(schema.get("required", []))
    for name, prop in (schema.get("properties") or {}).items():
        if "$ref" in prop:
            prop = {**_resolve(prop["$ref"], spec), **{k: v for k, v in prop.items() if k != "$ref"}}
        options = prop.get("anyOf") or prop.get("oneOf")
        ftype = prop.get("type") or ([o.get("type") or o.get("$ref", "").split("/")[-1] for o in options]
                                     if options else None)
        enum = prop.get("enum")
        if not enum and options:
            for o in options:
                if "$ref" in o:
                    enum = _resolve(o["$ref"], spec).get("enum") or enum
        field = {"name": name, "type": ftype, "required": name in required,
                 "default": prop.get("default"), "enum": enum,
                 "description": " ".join((prop.get("description") or "").split())[:400]}
        # Structured inputs (e.g. reference elements): show the shape of one item.
        items = [prop.get("items")] + [o.get("items") for o in (options or [])]
        for item in filter(None, items):
            item = _resolve(item["$ref"], spec) if "$ref" in item else item
            if item.get("properties"):
                field["item_fields"] = {
                    k: (v.get("type") or [o.get("type") for o in v.get("anyOf", [])] or
                        v.get("$ref", "").split("/")[-1])
                    for k, v in item["properties"].items()}
                break
        fields.append(field)
    out({"ok": True, "endpoint": a.endpoint, "fields": fields})


def unit_prices(endpoints: list[str]) -> dict[str, dict]:
    res = api("GET", "/models/pricing", [("endpoint_id", e) for e in endpoints])
    return {p["endpoint_id"]: p for p in res.get("prices", [])}


def cmd_price(a) -> None:
    prices = unit_prices(a.endpoints)
    missing = [e for e in a.endpoints if e not in prices]
    out({"ok": True, "prices": list(prices.values()), "missing": missing})


def cmd_estimate(a) -> None:
    endpoints: dict = {}
    for item in a.item:
        if "=" not in item:
            raise Fail(f"expected ENDPOINT=UNITS, got '{item}'")
        ep, units = item.rsplit("=", 1)
        try:
            qty = float(units)
        except ValueError:
            raise Fail(f"units must be a number in '{item}'")
        endpoints[ep] = {"unit_quantity": endpoints.get(ep, {}).get("unit_quantity", 0) + qty}
    res = api("POST", "/models/pricing/estimate", body={"estimate_type": "unit_price", "endpoints": endpoints})
    prices = unit_prices(list(endpoints))
    lines = [{"endpoint": ep, "units": v["unit_quantity"], "unit": prices.get(ep, {}).get("unit"),
              "unit_price": prices.get(ep, {}).get("unit_price"),
              "usd": round(v["unit_quantity"] * prices[ep]["unit_price"], 4) if ep in prices else None}
             for ep, v in endpoints.items()]
    out({"ok": True, "total_usd": res.get("total_cost"), "currency": res.get("currency"), "lines": lines})


def cmd_upload(a) -> None:
    import fal_client
    key()
    urls = {}
    for f in a.files:
        p = Path(f)
        if not p.is_file():
            raise Fail(f"no such file: {f}")
        urls[f] = fal_client.upload_file(str(p))
    out({"ok": True, "urls": urls})


def _resolve_path(path: str, project: Path | None) -> Path:
    """A relative path names a file under the project when one exists there, else under the cwd."""
    p = Path(path)
    if not p.is_absolute() and project is not None and (project / p).exists():
        return project / p
    return p


def _args(raw: str, project: Path | None = None) -> dict:
    if raw.startswith("@"):
        src = _resolve_path(raw[1:], project)
        if not src.is_file():
            raise Fail(f"--args file not found: {src}")
        raw = src.read_text(encoding="utf-8-sig")
    try:
        val = json.loads(raw)
    except json.JSONDecodeError as exc:
        raise Fail(f"--args is not valid JSON ({exc}); write the JSON to a file and pass --args @file, "
                   "because shells such as PowerShell strip quotes from inline JSON")
    if not isinstance(val, dict):
        raise Fail("--args must be a JSON object")
    return val


def _upload_local(args: dict, project: Path | None = None) -> dict:
    """Replace values that are existing local file paths (cwd- or project-relative) with fal CDN URLs."""
    import fal_client

    def walk(v):
        if isinstance(v, str) and not v.startswith(("http://", "https://", "data:")) and len(v) < 1024:
            p = _resolve_path(v, project)
            if p.suffix and p.is_file():
                progress(f"uploading {p.name}")
                return fal_client.upload_file(str(p))
            return v
        if isinstance(v, list):
            return [walk(x) for x in v]
        if isinstance(v, dict):
            return {k: walk(x) for k, x in v.items()}
        return v

    return walk(args)


def _write_json(path: Path, obj) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    tmp = path.with_name(f".{path.name}.tmp")
    tmp.write_text(json.dumps(obj, indent=2, ensure_ascii=False), encoding="utf-8")
    os.replace(tmp, path)


def _media(result) -> list[str]:
    found: list[str] = []

    def walk(v):
        if isinstance(v, dict):
            url = v.get("url")
            if isinstance(url, str) and url.startswith(("http", "data:")):
                found.append(url)
            for k, x in v.items():
                if k != "url":
                    walk(x)
        elif isinstance(v, list):
            for x in v:
                walk(x)

    walk(result)
    return list(dict.fromkeys(found))


def _download(urls: list[str], out_dir: Path, base: str) -> list[str]:
    out_dir.mkdir(parents=True, exist_ok=True)
    saved = []
    for i, url in enumerate(urls):
        suffix = '' if len(urls) == 1 else f'-{i + 1:02d}'
        if url.startswith("data:"):  # sync_mode results arrive inline
            header, _, payload = url.partition(",")
            ext = mimetypes.guess_extension(header[5:].split(";")[0]) or ".bin"
            dest = out_dir / f"{base}{suffix}{ext}"
            dest.write_bytes(base64.b64decode(payload) if ";base64" in header
                             else urllib.parse.unquote_to_bytes(payload))
        else:
            ext = Path(urllib.parse.urlparse(url).path).suffix or ".bin"
            dest = out_dir / f"{base}{suffix}{ext}"
            with urllib.request.urlopen(url, timeout=300) as resp, open(dest, "wb") as fh:
                while chunk := resp.read(1 << 20):
                    fh.write(chunk)
        saved.append(str(dest))
    return saved


def _strip_inline(v):
    """Drop inline data: payloads from the stored record; the files hold them."""
    if isinstance(v, str) and v.startswith("data:"):
        return v.split(",", 1)[0] + ",<saved to file>"
    if isinstance(v, list):
        return [_strip_inline(x) for x in v]
    if isinstance(v, dict):
        return {k: _strip_inline(x) for k, x in v.items()}
    return v


def _slug(s: str) -> str:
    return re.sub(r"[^a-z0-9]+", "-", s.lower()).strip("-")


def _estimate_usd(endpoint: str, units: float) -> tuple[float | None, dict | None]:
    try:
        price = unit_prices([endpoint]).get(endpoint)
    except Fail as exc:
        progress(f"warning: price lookup failed ({exc}); cost not checked")
        return None, None
    if not price:
        return None, None
    return round(price["unit_price"] * units, 4), price


def _preflight(a) -> tuple[Path | None, float | None, dict | None]:
    project = Path(a.project) if a.project else None
    if project and not a.stage:
        raise Fail("--project needs --stage so the gate and cost log are correct")
    est, price = _estimate_usd(a.endpoint, a.units)
    if est is None and a.estimate_usd is not None:
        est = round(a.estimate_usd, 4)
    if project:
        reasons = production.stage_gate(project, a.stage)
        if est is None:
            reasons.append(f"no price for {a.endpoint}, so the budget cannot be checked; pass --estimate-usd "
                           "with the cost from the model page")
        else:
            reasons += production.budget_check(project, est)
        if reasons:
            out({"ok": False, "blocked": True, "endpoint": a.endpoint, "stage": a.stage,
                 "estimate_usd": est, "reasons": reasons}, 1)
    return project, est, price


def _out_dir(a, project: Path | None) -> Path:
    if a.out:
        p = Path(a.out)
        return project / p if project is not None and not p.is_absolute() else p
    return project / "fal" if project is not None else Path.cwd()


def _base(a) -> str:
    stamp = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
    return a.name or f"{_slug(a.endpoint.split('/')[-1])}-{stamp}"


def _resume_hint(a, rid: str, out_dir: Path, base: str, est, cost_logged: bool) -> str:
    hint = [f"fal.py result {a.endpoint} {rid} --units {a.units}"]
    args_file = out_dir / f"{base}.args.json"
    if args_file.is_file():
        hint.append(f'--args "@{args_file}"')
    for flag, val in (("--project", a.project), ("--stage", a.stage), ("--out", str(out_dir)),
                      ("--name", base), ("--estimate-usd", est)):
        if val is not None:
            hint.append(f'{flag} "{val}"')
    if cost_logged:
        hint.append("--cost-logged")
    return " ".join(hint)


def _finish(a, project, est, price, request_id: str, result: dict, args: dict | None,
            out_dir: Path, base: str, cost_logged: bool) -> None:
    spent = None
    if project and est is not None and not cost_logged:
        spent = production.log_cost(project, a.stage, a.endpoint, est, a.units, request_id,
                                    note="estimate from unit price")
        cost_logged = True
    try:
        saved = _download(_media(result), out_dir, base)
    except Exception as exc:  # the request is paid for; never make the user pay twice to get the files
        out({"ok": False, "download_failed": True, "endpoint": a.endpoint, "request_id": request_id,
             "error": str(exc), "cost_logged": cost_logged,
             "resume": _resume_hint(a, request_id, out_dir, base, est, cost_logged)}, 2)
    record = {"endpoint": a.endpoint, "request_id": request_id, "args": _strip_inline(args), "units": a.units,
              "estimate_usd": est, "unit": price.get("unit") if price else None, "files": saved,
              "result": _strip_inline(result)}
    sidecar = out_dir / f"{base}.json"
    _write_json(sidecar, record)
    if project and sidecar.parent.resolve() != (project / "fal").resolve():
        _write_json(project / "fal" / f"{base}-{_slug(a.endpoint)}.json", record)
    out({"ok": True, "endpoint": a.endpoint, "request_id": request_id, "files": saved, "record": str(sidecar),
         "estimate_usd": est, "spent_usd": spent})


def cmd_run(a) -> None:
    import fal_client
    key()
    project, est, price = _preflight(a)
    out_dir, base = _out_dir(a, project), _base(a)
    args = _upload_local(_args(a.args, project), project)
    _write_json(out_dir / f"{base}.args.json", args)
    handle = fal_client.submit(a.endpoint, arguments=args)
    rid = handle.request_id
    progress(f"submitted {a.endpoint} request_id={rid}" + (f" (~${est:.2f})" if est is not None else ""))
    deadline = time.time() + a.timeout
    seen = 0
    while True:
        st = handle.status(with_logs=True)
        if isinstance(st, fal_client.Queued):
            progress(f"queued, position {st.position}")
        elif isinstance(st, fal_client.InProgress):
            for line in (st.logs or [])[seen:]:
                progress(line.get("message", ""))
            seen = len(st.logs or [])
        elif isinstance(st, fal_client.Completed):
            break
        if time.time() > deadline:
            out({"ok": False, "timeout": True, "endpoint": a.endpoint, "request_id": rid,
                 "resume": _resume_hint(a, rid, out_dir, base, est, False)}, 1)
        time.sleep(3)
    try:
        result = handle.get()
    except Exception as exc:  # fal reports failed requests as COMPLETED; the error surfaces here
        raise Fail(f"{a.endpoint} request {rid} failed: {exc}")
    _finish(a, project, est, price, rid, result, args, out_dir, base, cost_logged=False)


def cmd_result(a) -> None:
    import fal_client
    key()
    project = Path(a.project) if a.project else None
    if project and not a.stage:
        raise Fail("--project needs --stage so the cost lands on the right stage")
    est, price = _estimate_usd(a.endpoint, a.units) if project else (None, None)
    if est is None and a.estimate_usd is not None:
        est = round(a.estimate_usd, 4)
    try:
        result = fal_client.result(a.endpoint, a.request_id)
    except Exception as exc:
        raise Fail(f"could not fetch {a.request_id}: {exc}")
    _finish(a, project, est, price, a.request_id, result, _args(a.args, project) if a.args else None,
            _out_dir(a, project), _base(a), cost_logged=a.cost_logged)


def main(argv=None) -> None:
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = p.add_subparsers(dest="cmd", required=True)

    s = sub.add_parser("models", help="search active fal models")
    s.add_argument("--q")
    s.add_argument("--category", help="e.g. text-to-image, image-to-video, text-to-video, text-to-speech")
    s.add_argument("--limit", type=int, default=20)
    s.add_argument("--recent", action="store_true", help="newest first")
    s.set_defaults(fn=cmd_models)

    s = sub.add_parser("schema", help="input schema of an endpoint")
    s.add_argument("endpoint")
    s.set_defaults(fn=cmd_schema)

    s = sub.add_parser("price", help="unit price per endpoint")
    s.add_argument("endpoints", nargs="+")
    s.set_defaults(fn=cmd_price)

    s = sub.add_parser("estimate", help="estimate planned usage")
    s.add_argument("--item", action="append", required=True, help="ENDPOINT=UNITS, repeatable")
    s.set_defaults(fn=cmd_estimate)

    s = sub.add_parser("upload", help="upload local files to the fal CDN")
    s.add_argument("files", nargs="+")
    s.set_defaults(fn=cmd_upload)

    for name, fn in (("run", cmd_run), ("result", cmd_result)):
        s = sub.add_parser(name, help="submit, wait, download" if name == "run" else "download a finished request")
        s.add_argument("endpoint")
        if name == "run":
            s.add_argument("--args", required=True,
                           help="@file.json (preferred; inline JSON loses its quotes in PowerShell) or a JSON "
                                "object; local file paths, cwd- or project-relative, are uploaded")
            s.add_argument("--timeout", type=int, default=1800)
        else:
            s.add_argument("request_id")
            s.add_argument("--args", help="the @file originally sent, to keep in the record")
            s.add_argument("--cost-logged", action="store_true",
                           help="the cost was already logged (set by the resume hint after a failed download)")
        s.add_argument("--units", type=float, default=1.0,
                       help="billing units for the cost estimate (images, megapixels, characters...)")
        s.add_argument("--estimate-usd", type=float,
                       help="cost to log and check when the pricing API has no price for the endpoint")
        s.add_argument("--project")
        s.add_argument("--stage", choices=production.STAGES)
        s.add_argument("--out", help="output folder; relative paths are under --project when given")
        s.add_argument("--name")
        s.set_defaults(fn=fn)

    for stream in (sys.stdout, sys.stderr):
        if hasattr(stream, "reconfigure"):
            stream.reconfigure(encoding="utf-8")
    a = p.parse_args(argv)
    try:
        a.fn(a)
    except (Fail, production.Fail) as exc:
        print(json.dumps({"ok": False, "error": str(exc)}), file=sys.stderr)
        sys.exit(2)
    except Exception as exc:  # exit 1 means "blocked"; an unexpected failure must not look like one
        print(json.dumps({"ok": False, "error": f"{type(exc).__name__}: {exc}"}), file=sys.stderr)
        sys.exit(2)


if __name__ == "__main__":
    main()
