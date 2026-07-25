# Manual Research

Loaded when `research_mode` is `manual`, when browser-harness isn't available, or in `--headless`. The analysis is identical to live mode — same signals, same ranking, same outputs — but the evidence comes from job listings the freelancer pastes rather than a live scan. The honesty bar is the same: rank on what's actually in front of you, and say so in the caveats.

## Get the raw material

Ask the freelancer to paste real Upwork job listings for the candidate niches — the more complete, the better. The richest paste includes, per job: the title and description, the proposals-submitted range Upwork shows, the budget (hourly range or fixed), and client info (spend, hire rate). Competing freelancer profiles they paste (headline, rate, reviews) sharpen the competition read further.

Guide them toward a representative sample per niche, not one job — a single listing can't carry demand or competition signal. A dozen across two or three candidate niches is enough to rank. If they only have a couple, work with them but make the thin basis explicit in the caveats and treat the ranking as provisional.

## Extract the same signals

From the pasted listings, derive per candidate niche:

- **Demand** — how many jobs they found, posting recency if shown, whether the same need repeats.
- **Competition** — proposals-per-job ranges, how many strong competing profiles, client quality.
- **Rates** — stated budgets and any competing-profile rates → the brief's Rate Range.
- **Fit** — from the workspace (`freelancer-context.md`), the half the paste can't supply.
- **Competing-profile patterns** — headlines and emphasis from any profiles pasted.

If a niche has no pasted jobs, you can't rank it on real data — say so rather than inferring demand from general knowledge. Offer to rank only the niches with evidence, or ask for more listings. Record what you extract per niche to a per-run scratch (`{freelancer-workspace}/research/.observations-{YYYY-MM-DD}.json`, the findings-JSON niche shape) so it survives compaction and transforms straight into the findings JSON later.

## After gathering

Return to SKILL.md's **Rank and Form the Opinion** and **Produce the Dashboard and Report** sections. Set `"mode": "manual"` in the findings JSON and make the `caveats` line state the basis plainly — e.g. "Based on 18 listings the freelancer pasted across 3 niches; provisional until a live scan confirms demand." A reader must never mistake a pasted-sample ranking for a full live-market scan.

When the freelancer later enables live research (browser-harness installed, or `research_mode` set to `local-browser` in setup), a fresh run can confirm and deepen these findings.
