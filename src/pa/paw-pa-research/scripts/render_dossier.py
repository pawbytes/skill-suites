#!/usr/bin/env python3
# /// script
# requires-python = ">=3.9"
# dependencies = []
# ///
"""Render a self-contained proposal research dossier from findings JSON.

Plumbing only: the LLM gathers evidence, scores local case-study matches, and
synthesizes sections; this script renders the decided findings document to HTML
and opens it in the OS default browser. No analysis happens here.

Input JSON shape (evidence fields are strings the LLM already wrote):
{
  "clientName": "Acme Corp",
  "proposalSlug": "acme-corp-2026-07-03",
  "generated": "2026-07-03",
  "mode": "local-browser" | "cursor-ide-browser" | "local-only",
  "briefSummary": "One-paragraph scope recap from brief.md",
  "recommendation": "Lead synthesis — how to substantiate the proposal",
  "clientIntel": {
    "summary": "...",
    "signals": [{"label": "Industry", "detail": "...", "source": "URL or note"}]
  },
  "techStack": {
    "summary": "...",
    "technologies": [{"name": "React", "evidence": "...", "source": "..."}]
  },
  "localCaseStudyMatches": [
    {
      "id": "cs-001",
      "client": "Prior Client",
      "relevanceScore": 0.92,
      "matchReasons": ["Same industry", "Similar deliverables"],
      "sourceDocPath": "library/inbox/case-study.pdf",
      "highlights": "Outcome and proof point"
    }
  ],
  "webEvidence": {
    "summary": "...",
    "examples": [{"title": "...", "url": "https://...", "relevance": "...", "keyTakeaway": "..."}]
  },
  "pricingBenchmarks": {
    "summary": "...",
    "observations": [{"workType": "...", "range": "$X-$Y", "source": "...", "notes": "..."}]
  },
  "competitiveContext": {
    "summary": "...",
    "alternatives": [{"name": "...", "differentiator": "...", "source": "..."}]
  },
  "caveats": "Evidence basis — what was scanned vs local-only"
}

Usage:
  python render_dossier.py --findings findings.json --out research-dossier.html [--no-open]
Outputs JSON to stdout: {"ok": true, "html": "<path>", "opened": true}
"""
import argparse
import html
import json
import sys
import webbrowser
from pathlib import Path


def esc(value) -> str:
    return html.escape(str(value if value is not None else ""))


def score_pct(score) -> float:
    try:
        v = float(score)
    except (TypeError, ValueError):
        return 0.0
    if v <= 1.0:
        v *= 100
    return max(0.0, min(100.0, v))


def score_class(pct):
    if pct >= 75:
        return "high"
    if pct >= 50:
        return "mid"
    return "low"


def render_list(items, empty_msg="None recorded."):
    if not items:
        return f'<p class="empty">{esc(empty_msg)}</p>'
    return "\n".join(items)


def render_signals(signals):
    if not signals:
        return ""
    rows = []
    for s in signals:
        src = s.get("source", "")
        src_html = f' <span class="source">({esc(src)})</span>' if src else ""
        rows.append(
            f'<tr><td class="label">{esc(s.get("label", ""))}</td>'
            f'<td>{esc(s.get("detail", ""))}{src_html}</td></tr>'
        )
    return f'<table class="signals">{"".join(rows)}</table>'


def render_tech(technologies):
    if not technologies:
        return ""
    cards = []
    for t in technologies:
        src = t.get("source", "")
        src_html = f'<div class="source">{esc(src)}</div>' if src else ""
        cards.append(
            f'<div class="chip"><strong>{esc(t.get("name", ""))}</strong>'
            f'<p>{esc(t.get("evidence", ""))}</p>{src_html}</div>'
        )
    return f'<div class="chips">{"".join(cards)}</div>'


def render_matches(matches):
    if not matches:
        return '<p class="empty">No local case studies matched. Run paw-pa-library to index your portfolio.</p>'
    cards = []
    sorted_matches = sorted(matches, key=lambda m: m.get("relevanceScore", 0), reverse=True)
    for i, m in enumerate(sorted_matches):
        pct = score_pct(m.get("relevanceScore", 0))
        reasons = m.get("matchReasons") or []
        reason_html = ""
        if reasons:
            tags = "".join(f'<span class="tag">{esc(r)}</span>' for r in reasons)
            reason_html = f'<div class="tags">{tags}</div>'
        path = m.get("sourceDocPath", "")
        path_html = f'<div class="source">Source: {esc(path)}</div>' if path else ""
        top = '<span class="badge">Top match</span>' if i == 0 else ""
        cards.append(f"""
        <article class="match-card">
          <header>
            <span class="score {score_class(pct)}">{pct:.0f}%</span>
            <h3>{esc(m.get("client", m.get("id", "Case study")))}</h3>
            {top}
          </header>
          {reason_html}
          <p>{esc(m.get("highlights", ""))}</p>
          {path_html}
        </article>""")
    return "\n".join(cards)


def render_web_examples(examples):
    if not examples:
        return ""
    items = []
    for ex in examples:
        url = ex.get("url", "")
        title = esc(ex.get("title", "Example"))
        link = f'<a href="{esc(url)}" target="_blank" rel="noopener">{title}</a>' if url else title
        items.append(
            f'<li><div class="ex-title">{link}</div>'
            f'<p>{esc(ex.get("keyTakeaway", ""))}</p>'
            f'<span class="muted">{esc(ex.get("relevance", ""))}</span></li>'
        )
    return f'<ul class="examples">{"".join(items)}</ul>'


def render_benchmarks(observations):
    if not observations:
        return ""
    rows = []
    for o in observations:
        rows.append(
            f'<tr><td>{esc(o.get("workType", ""))}</td>'
            f'<td class="rate">{esc(o.get("range", ""))}</td>'
            f'<td>{esc(o.get("notes", ""))}</td>'
            f'<td class="source">{esc(o.get("source", ""))}</td></tr>'
        )
    return (
        '<table class="bench"><thead><tr><th>Work type</th><th>Range</th>'
        '<th>Notes</th><th>Source</th></tr></thead><tbody>'
        + "".join(rows)
        + "</tbody></table>"
    )


def render_competitive(alternatives):
    if not alternatives:
        return ""
    items = []
    for a in alternatives:
        src = a.get("source", "")
        src_html = f' <span class="source">({esc(src)})</span>' if src else ""
        items.append(
            f'<li><strong>{esc(a.get("name", ""))}</strong> — '
            f'{esc(a.get("differentiator", ""))}{src_html}</li>'
        )
    return f'<ul class="comp">{"".join(items)}</ul>'


def section(title, body, anchor):
    if not body.strip():
        return ""
    return f"""
    <section id="{anchor}" class="panel">
      <h2>{esc(title)}</h2>
      {body}
    </section>"""


def render(data: dict) -> str:
    client = esc(data.get("clientName", "Client"))
    generated = esc(data.get("generated", ""))
    mode = data.get("mode", "")
    mode_label = {
        "local-browser": "Live web research (browser-harness)",
        "cursor-ide-browser": "Live web research (Cursor browser)",
        "local-only": "Local library only",
    }.get(mode, esc(mode) or "Research")
    brief = esc(data.get("briefSummary", ""))
    recommendation = esc(data.get("recommendation", ""))
    caveats = esc(data.get("caveats", ""))

    intel = data.get("clientIntel") or {}
    tech = data.get("techStack") or {}
    web = data.get("webEvidence") or {}
    bench = data.get("pricingBenchmarks") or {}
    comp = data.get("competitiveContext") or {}

    intel_body = ""
    if intel.get("summary") or intel.get("signals"):
        intel_body = f'<p>{esc(intel.get("summary", ""))}</p>{render_signals(intel.get("signals") or [])}'

    tech_body = ""
    if tech.get("summary") or tech.get("technologies"):
        tech_body = f'<p>{esc(tech.get("summary", ""))}</p>{render_tech(tech.get("technologies") or [])}'

    matches_html = render_matches(data.get("localCaseStudyMatches") or [])

    web_body = ""
    if web.get("summary") or web.get("examples"):
        web_body = f'<p>{esc(web.get("summary", ""))}</p>{render_web_examples(web.get("examples") or [])}'

    bench_body = ""
    if bench.get("summary") or bench.get("observations"):
        bench_body = f'<p>{esc(bench.get("summary", ""))}</p>{render_benchmarks(bench.get("observations") or [])}'

    comp_body = ""
    if comp.get("summary") or comp.get("alternatives"):
        comp_body = f'<p>{esc(comp.get("summary", ""))}</p>{render_competitive(comp.get("alternatives") or [])}'

    sections = [
        section("Client intelligence", intel_body, "intel"),
        section("Technology footprint", tech_body, "tech"),
        section("Local case-study matches", matches_html, "local"),
        section("Web evidence & benchmarks", web_body, "web"),
        section("Pricing benchmarks", bench_body, "pricing"),
        section("Competitive context", comp_body, "competitive"),
    ]
    sections_html = "\n".join(s for s in sections if s.strip())

    lead = ""
    if recommendation:
        lead = f'<section class="lead"><h3>Research synthesis</h3><p>{recommendation}</p></section>'
    caveat_block = ""
    if caveats:
        caveat_block = f'<aside class="caveats"><strong>Evidence basis:</strong> {caveats}</aside>'

    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Research Dossier — {client}</title>
<style>
  :root {{
    --bg:#0f1115; --surface:#181b22; --surface2:#1f232c; --line:#2a2f3a;
    --text:#e8eaf0; --muted:#9aa3b2; --accent:#7c6cff; --good:#3ecf8e;
    --mid:#f6c453; --low:#e8705c;
  }}
  * {{ box-sizing:border-box; }}
  body {{ margin:0; background:var(--bg); color:var(--text);
    font:15px/1.55 -apple-system,BlinkMacSystemFont,"Segoe UI",Roboto,sans-serif; }}
  .wrap {{ max-width:960px; margin:0 auto; padding:40px 24px 64px; }}
  .top-bar {{ display:flex; justify-content:space-between; flex-wrap:wrap; gap:8px;
    color:var(--muted); font-size:13px; margin-bottom:8px; }}
  h1 {{ font-size:28px; margin:0 0 6px; letter-spacing:-0.02em; }}
  .sub {{ color:var(--muted); margin:0 0 24px; font-size:15px; }}
  .lead {{ background:linear-gradient(135deg,#1e1a2e,#181b22); border:1px solid var(--line);
    border-left:3px solid var(--accent); border-radius:12px; padding:20px 22px; margin:0 0 28px; }}
  .lead h3 {{ margin:0 0 8px; font-size:13px; text-transform:uppercase;
    letter-spacing:.08em; color:var(--accent); }}
  .lead p {{ margin:0; font-size:16px; }}
  .panel {{ background:var(--surface); border:1px solid var(--line); border-radius:12px;
    padding:22px 24px; margin:0 0 18px; }}
  .panel h2 {{ margin:0 0 14px; font-size:18px; }}
  .panel > p {{ margin:0 0 14px; color:var(--text); }}
  .signals {{ width:100%; border-collapse:collapse; font-size:14px; }}
  .signals td {{ padding:8px 0; border-bottom:1px solid var(--line); vertical-align:top; }}
  .signals .label {{ width:140px; color:var(--muted); font-weight:600; padding-right:16px; }}
  .source {{ color:var(--muted); font-size:12.5px; }}
  .chips {{ display:flex; flex-wrap:wrap; gap:10px; }}
  .chip {{ background:var(--surface2); border:1px solid var(--line); border-radius:10px;
    padding:12px 14px; flex:1 1 200px; max-width:100%; }}
  .chip p {{ margin:6px 0 0; font-size:13.5px; color:var(--muted); }}
  .match-card {{ background:var(--surface2); border:1px solid var(--line); border-radius:10px;
    padding:16px 18px; margin:0 0 12px; }}
  .match-card header {{ display:flex; align-items:center; gap:12px; flex-wrap:wrap; margin-bottom:10px; }}
  .match-card h3 {{ margin:0; font-size:17px; flex:1; }}
  .score {{ font-size:13px; font-weight:700; border-radius:20px; padding:4px 10px; }}
  .score.high {{ background:rgba(62,207,142,.15); color:var(--good); }}
  .score.mid {{ background:rgba(246,196,83,.15); color:var(--mid); }}
  .score.low {{ background:rgba(232,112,92,.15); color:var(--low); }}
  .badge {{ font-size:11px; background:var(--accent); color:#0f1115; border-radius:20px;
    padding:3px 10px; font-weight:700; }}
  .tags {{ display:flex; flex-wrap:wrap; gap:6px; margin-bottom:10px; }}
  .tag {{ font-size:12px; background:var(--bg); border:1px solid var(--line);
    border-radius:6px; padding:2px 8px; color:var(--muted); }}
  .examples {{ margin:0; padding-left:20px; }}
  .examples li {{ margin:0 0 14px; }}
  .ex-title {{ font-weight:600; margin-bottom:4px; }}
  .examples a {{ color:var(--accent); }}
  .muted {{ color:var(--muted); font-size:13px; }}
  .bench {{ width:100%; border-collapse:collapse; font-size:13.5px; margin-top:8px; }}
  .bench th {{ text-align:left; color:var(--muted); font-size:12px; text-transform:uppercase;
    letter-spacing:.05em; padding:8px 10px 8px 0; border-bottom:1px solid var(--line); }}
  .bench td {{ padding:10px 10px 10px 0; border-bottom:1px solid var(--line); vertical-align:top; }}
  .bench .rate {{ color:var(--good); font-weight:600; white-space:nowrap; }}
  .comp {{ margin:0; padding-left:20px; }}
  .comp li {{ margin:0 0 10px; }}
  .caveats {{ margin-top:28px; padding:14px 18px; background:var(--surface2);
    border-radius:10px; color:var(--muted); font-size:13px; }}
  .empty {{ color:var(--muted); font-style:italic; }}
  nav.toc {{ display:flex; flex-wrap:wrap; gap:8px; margin:0 0 24px; }}
  nav.toc a {{ font-size:13px; color:var(--accent); text-decoration:none;
    background:var(--surface); border:1px solid var(--line); border-radius:20px; padding:4px 12px; }}
</style>
</head>
<body>
  <div class="wrap">
    <div class="top-bar"><span>{esc(mode_label)}</span><span>{generated}</span></div>
    <h1>Research Dossier</h1>
    <p class="sub">{client} · evidence pack for proposal substantiation</p>
    {f'<p class="sub">{brief}</p>' if brief else ''}
    {lead}
    <nav class="toc">
      <a href="#intel">Client intel</a>
      <a href="#tech">Tech stack</a>
      <a href="#local">Local matches</a>
      <a href="#web">Web evidence</a>
      <a href="#pricing">Pricing benchmarks</a>
      <a href="#competitive">Competitive</a>
    </nav>
    {sections_html}
    {caveat_block}
  </div>
</body>
</html>"""


def main():
    ap = argparse.ArgumentParser(description="Render a research dossier from findings JSON.")
    ap.add_argument("--findings", required=True, help="path to findings JSON")
    ap.add_argument("--out", required=True, help="path to write research-dossier.html")
    ap.add_argument("--no-open", action="store_true", help="do not open the file after writing")
    args = ap.parse_args()

    findings_path = Path(args.findings)
    try:
        data = json.loads(findings_path.read_text(encoding="utf-8"))
    except FileNotFoundError:
        print(json.dumps({"ok": False, "error": f"findings not found: {findings_path}"}))
        return 1
    except json.JSONDecodeError as e:
        print(json.dumps({"ok": False, "error": f"invalid JSON: {e}"}))
        return 1

    out_path = Path(args.out)
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(render(data), encoding="utf-8")

    opened = False
    if not args.no_open:
        try:
            opened = webbrowser.open(out_path.resolve().as_uri())
        except Exception:
            opened = False

    print(json.dumps({"ok": True, "html": str(out_path), "opened": opened}))
    return 0


if __name__ == "__main__":
    sys.exit(main())
