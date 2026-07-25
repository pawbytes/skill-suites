# Live Browser Research (browser-harness)

Loaded when `web_research_enabled` is true and browser-harness is available (`command -v browser-harness`). Preferred web-research path — drives the seller's own Chrome via CDP.

## Before you browse

Confirm Chrome is running with remote debugging if needed (browser-harness `install.md`). If connection fails after one honest attempt, fall back to `references/cursor-browser-research.md` if Cursor browser MCP is available, else `references/local-only-research.md`.

Invoke as `browser-harness -c '...'`. First navigation is `new_tab(url)`, never `goto_url`. Use `capture_screenshot()` to orient; use `js(...)` for structured extraction once you know the page structure.

## Research passes

Run passes aligned with the flavor references — load each when doing that pass:

| Pass | Reference | Typical targets |
| ---- | --------- | ---------------- |
| Client intel | `client-intel.md` | Client site, news, LinkedIn public pages |
| Tech stack | `tech-stack-research.md` | Site source, careers/JDs, integrations page |
| Web evidence | `web-evidence.md` | Google/web search for case studies, reports |
| Pricing benchmarks | `pricing-benchmarks.md` | Clutch, agency sites, rate listings |
| Competitive | `competitive-context.md` | Competitor sites, comparison articles |

Work one pass at a time; append findings to `{run-folder}/.research-findings-{date}.json` after each pass.

## Discipline

- **Read-only, human-paced.** Never submit forms, post content, or log in with credentials from screenshots — auth wall = stop and ask seller to log in.
- **Cite URLs** for every fact extracted live.
- **Record as you observe** — do not batch-remember across dozens of tabs.
- Set findings `"mode": "local-browser"` and document scan scope in `caveats`.

## After gathering

Return to SKILL.md **Produce the dossier**. If any pass was skipped (auth, timeout), note which sections are incomplete in `caveats`.
