# Live Browser Research

Loaded when `research_mode` is `local-browser` and browser-harness is available. You drive the freelancer's **own logged-in Chrome** via the `browser` skill (browser-harness, CDP) to gather real signal from live Upwork. This is a supervised research assistant in the user's own session — read-only, human-paced, never submitting or applying to anything.

## Before you scan

Confirm the freelancer is logged into Upwork in their Chrome and that Chrome has remote debugging on (the `browser` skill's `connection.md` / `install.md` carry the one-time `chrome://inspect/#remote-debugging` toggle if the first call can't attach). If you can't connect after one honest attempt, fall back to `references/manual-research.md` rather than fighting it — tell the freelancer you'll work from listings they paste instead.

Invoke the browser as `browser-harness -c '...'`. First navigation is `new_tab(url)`, never `goto_url` (which clobbers the freelancer's active tab). Use `capture_screenshot()` to see the page and decide the next move; drop to `js(...)` for structured extraction once you know what you're reading.

## What to gather per candidate niche

Work one candidate niche at a time so observations stay attributable. For each:

**Demand signal — from job search.** Search Upwork jobs for the niche's real query terms (e.g. "Shopify speed optimization", "Core Web Vitals Shopify"). Observe and record:
- How many jobs the search returns, and how many were posted in the last 7 days (recency = live demand, not a stale backlog).
- Whether jobs recur (the same need posted repeatedly signals an ongoing market).

**Competition signal — from each job and from profiles.** On the job listings:
- Proposals submitted per job (Upwork shows ranges like "5 to 10", "20 to 50"). Low proposals on a well-budgeted job is the gold signal: real demand, thin competition.
- Client quality where visible (spend history, hire rate, verified payment).

Then scan a handful of competing freelancer profiles in the niche (search freelancers or open profiles from similar jobs):
- Headlines and titles — the exact phrasing top profiles lead with.
- What they emphasize, their rate, how many reviews/JSS.

**Rate signal.** Record the budget ranges jobs state (hourly and fixed) and the rates competing profiles charge. This becomes the brief's Rate Range, so capture actual numbers, not impressions.

## Discipline

- **One honest pass, human-paced.** A representative sample (a few dozen jobs, a handful of profiles per niche) beats exhaustively scraping the platform. You're forming a judgment, not building a dataset.
- **Read-only, always.** Never click Apply/Submit, never send a proposal, never message a client, never change the freelancer's profile. If a flow would take an action, stop.
- **Auth wall = stop and ask.** If you hit a login screen, don't type credentials from a screenshot — ask the freelancer to log in, then continue.
- **Record as you observe.** Append the numbers per niche to your per-run scratch (`{freelancer-workspace}/research/.observations-{YYYY-MM-DD}.json`, the findings-JSON niche shape) the moment you see them — don't trust them to memory across many page loads or a mid-scan compaction. The scratch transforms straight into the findings JSON later.
- **If a niche is empty, that's a finding.** A candidate with almost no live jobs gets recorded as low-demand with the count you saw — it sharpens the ranking.

## After gathering

Return to SKILL.md's **Rank and Form the Opinion** and **Produce the Dashboard and Report** sections with your observed numbers. Set `"mode": "local-browser"` in the findings JSON and let the `caveats` line state honestly how many jobs and profiles you actually scanned.

Contribute back: if you learned something durable about how Upwork's pages work (a stable selector, a private endpoint the search calls, a pagination quirk), the `browser` skill's "always contribute back" guidance applies — file it to its `agent-workspace/domain-skills/upwork/` so the next run is faster.
