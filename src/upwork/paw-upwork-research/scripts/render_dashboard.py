#!/usr/bin/env python3
# /// script
# requires-python = ">=3.9"
# dependencies = []
# ///
"""Render a self-contained niche-opportunity dashboard from ranked findings JSON.

Plumbing only: the LLM does the judgment (scanning, ranking, evidence synthesis,
rate observation) and hands this script a fully-decided findings document. This
script renders it to a single inline-styled HTML file and opens it in the OS
default browser. No analysis happens here.

Input JSON shape (all evidence fields are strings the LLM already wrote):
{
  "freelancer": "Alex Rivera",
  "generated": "2026-06-23",
  "mode": "local-browser" | "manual",
  "recommendation": "Shopify speed optimization ...",   # the lead opinion, one paragraph
  "niches": [
    {
      "name": "Shopify speed optimization",
      "rank": 1,                       # 1 = top recommendation
      "fit": 9,                        # 0-10 ints
      "demand": 8,
      "competition": 3,                # lower = less crowded (less competition)
      "rate_range": "$60-$95/hr",
      "evidence": "Scanned 40 live jobs; 12 posted this week ...",  # cites observed data
      "sample_jobs": ["Speed up Shopify store losing sales", "..."]  # optional
    }
  ],
  "rate_notes": "Across all niches, budgets cluster ...",            # optional
  "caveats": "Manual mode: based on 18 pasted listings ..."          # optional
}

Usage:
  python render_dashboard.py --findings findings.json --out dashboard.html [--no-open]
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


def bar(value, max_value=10, invert=False):
    """Return a 0-100 width pct. invert=True means a low raw value is 'good' (wide)."""
    try:
        v = float(value)
    except (TypeError, ValueError):
        v = 0.0
    pct = max(0.0, min(1.0, v / max_value)) * 100
    return (100 - pct) if invert else pct


def score_class(pct):
    if pct >= 66:
        return "good"
    if pct >= 33:
        return "mid"
    return "weak"


def render(data: dict) -> str:
    freelancer = esc(data.get("freelancer", "Freelancer"))
    generated = esc(data.get("generated", ""))
    mode = esc(data.get("mode", ""))
    mode_label = {
        "local-browser": "Live market scan",
        "manual": "Pasted-listing analysis",
    }.get(data.get("mode", ""), mode or "Research")
    recommendation = esc(data.get("recommendation", ""))
    rate_notes = esc(data.get("rate_notes", ""))
    caveats = esc(data.get("caveats", ""))

    niches = sorted(data.get("niches", []), key=lambda n: n.get("rank", 999))

    cards = []
    for n in niches:
        rank = n.get("rank", "")
        is_top = rank == 1
        fit_pct = bar(n.get("fit"))
        demand_pct = bar(n.get("demand"))
        # competition: low raw value = good, so a wide bar = "open lane"
        comp_open_pct = bar(n.get("competition"), invert=True)
        samples = n.get("sample_jobs") or []
        sample_html = ""
        if samples:
            items = "".join(f"<li>{esc(s)}</li>" for s in samples)
            sample_html = f'<div class="samples"><div class="samples-label">Sample jobs observed</div><ul>{items}</ul></div>'
        rate = esc(n.get("rate_range", ""))
        rate_html = f'<span class="rate">{rate}</span>' if rate else ""
        top_badge = '<span class="badge">★ Recommended lane</span>' if is_top else ""

        cards.append(f"""
        <article class="card{' top' if is_top else ''}">
          <header>
            <span class="rank">#{esc(rank)}</span>
            <h2>{esc(n.get('name', ''))}</h2>
            {rate_html}
            {top_badge}
          </header>
          <div class="metrics">
            <div class="metric">
              <div class="metric-head"><span>Fit</span><span>{esc(n.get('fit', ''))}/10</span></div>
              <div class="track"><div class="fill {score_class(fit_pct)}" style="width:{fit_pct:.0f}%"></div></div>
            </div>
            <div class="metric">
              <div class="metric-head"><span>Demand</span><span>{esc(n.get('demand', ''))}/10</span></div>
              <div class="track"><div class="fill {score_class(demand_pct)}" style="width:{demand_pct:.0f}%"></div></div>
            </div>
            <div class="metric">
              <div class="metric-head"><span>Open lane</span><span>{esc(n.get('competition', ''))}/10 comp.</span></div>
              <div class="track"><div class="fill {score_class(comp_open_pct)}" style="width:{comp_open_pct:.0f}%"></div></div>
            </div>
          </div>
          <p class="evidence">{esc(n.get('evidence', ''))}</p>
          {sample_html}
        </article>""")

    cards_html = "\n".join(cards) if cards else '<p class="empty">No niches in findings.</p>'
    rate_block = f'<section class="panel"><h3>Rate observations</h3><p>{rate_notes}</p></section>' if rate_notes else ""
    caveat_block = f'<aside class="caveats"><strong>Evidence basis:</strong> {caveats}</aside>' if caveats else ""

    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Niche Opportunity Report — {freelancer}</title>
<style>
  :root {{
    --bg:#0f1115; --surface:#181b22; --surface2:#1f232c; --line:#2a2f3a;
    --text:#e8eaf0; --muted:#9aa3b2; --accent:#5b8cff; --good:#3ecf8e;
    --mid:#f6c453; --weak:#e8705c; --top:#5b8cff;
  }}
  * {{ box-sizing:border-box; }}
  body {{ margin:0; background:var(--bg); color:var(--text);
    font:15px/1.5 -apple-system,BlinkMacSystemFont,"Segoe UI",Roboto,sans-serif; }}
  .wrap {{ max-width:920px; margin:0 auto; padding:40px 24px 64px; }}
  .top-bar {{ display:flex; justify-content:space-between; align-items:baseline;
    flex-wrap:wrap; gap:8px; color:var(--muted); font-size:13px; }}
  h1 {{ font-size:28px; margin:6px 0 4px; letter-spacing:-0.02em; }}
  .sub {{ color:var(--muted); margin:0 0 28px; }}
  .lead {{ background:linear-gradient(135deg,#1c2331,#181b22); border:1px solid var(--line);
    border-left:3px solid var(--accent); border-radius:12px; padding:20px 22px; margin:0 0 32px; }}
  .lead h3 {{ margin:0 0 8px; font-size:13px; text-transform:uppercase; letter-spacing:.08em; color:var(--accent); }}
  .lead p {{ margin:0; font-size:16px; }}
  .card {{ background:var(--surface); border:1px solid var(--line); border-radius:12px;
    padding:20px 22px; margin:0 0 16px; }}
  .card.top {{ border-color:var(--top); box-shadow:0 0 0 1px var(--top); }}
  .card header {{ display:flex; align-items:center; gap:12px; flex-wrap:wrap; margin-bottom:14px; }}
  .rank {{ font-size:13px; color:var(--muted); font-weight:600; background:var(--surface2);
    border-radius:6px; padding:2px 8px; }}
  .card h2 {{ font-size:19px; margin:0; flex:1 1 auto; }}
  .rate {{ font-size:14px; color:var(--good); font-weight:600; white-space:nowrap; }}
  .badge {{ font-size:12px; color:#0f1115; background:var(--top); border-radius:20px;
    padding:3px 10px; font-weight:700; }}
  .metrics {{ display:grid; grid-template-columns:repeat(3,1fr); gap:14px; margin-bottom:14px; }}
  .metric-head {{ display:flex; justify-content:space-between; font-size:12px; color:var(--muted); margin-bottom:5px; }}
  .track {{ height:7px; background:var(--surface2); border-radius:20px; overflow:hidden; }}
  .fill {{ height:100%; border-radius:20px; }}
  .fill.good {{ background:var(--good); }}
  .fill.mid {{ background:var(--mid); }}
  .fill.weak {{ background:var(--weak); }}
  .evidence {{ margin:0; color:var(--text); font-size:14.5px; }}
  .samples {{ margin-top:12px; padding-top:12px; border-top:1px solid var(--line); }}
  .samples-label {{ font-size:12px; color:var(--muted); text-transform:uppercase; letter-spacing:.06em; margin-bottom:6px; }}
  .samples ul {{ margin:0; padding-left:18px; color:var(--muted); font-size:13.5px; }}
  .samples li {{ margin:2px 0; }}
  .panel {{ background:var(--surface); border:1px solid var(--line); border-radius:12px; padding:18px 22px; margin:24px 0 0; }}
  .panel h3 {{ margin:0 0 8px; font-size:15px; }}
  .panel p {{ margin:0; color:var(--muted); }}
  .caveats {{ margin-top:28px; padding:14px 18px; background:var(--surface2); border-radius:10px;
    color:var(--muted); font-size:13px; }}
  .empty {{ color:var(--muted); }}
  @media (max-width:560px) {{ .metrics {{ grid-template-columns:1fr; }} }}
</style>
</head>
<body>
  <div class="wrap">
    <div class="top-bar"><span>{mode_label}</span><span>{generated}</span></div>
    <h1>Niche Opportunity Report</h1>
    <p class="sub">{freelancer} · ranked by fit × demand × open lane</p>
    {f'<section class="lead"><h3>The recommendation</h3><p>{recommendation}</p></section>' if recommendation else ''}
    {cards_html}
    {rate_block}
    {caveat_block}
  </div>
</body>
</html>"""


def main():
    ap = argparse.ArgumentParser(description="Render a niche-opportunity dashboard from findings JSON.")
    ap.add_argument("--findings", required=True, help="path to findings JSON")
    ap.add_argument("--out", required=True, help="path to write the HTML dashboard")
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
