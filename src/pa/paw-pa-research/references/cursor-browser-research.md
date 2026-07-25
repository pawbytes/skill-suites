# Cursor IDE Browser Research (fallback)

Loaded when browser-harness is unavailable but **cursor-ide-browser** MCP is enabled. Same research goals as `live-browser-research.md`; different tool surface.

## MCP workflow

1. `browser_tabs` with action `list` — inspect open tabs before navigating.
2. `browser_navigate` to create or open target URL.
3. `browser_lock` before longer automation on an existing tab; `browser_lock` with action `unlock` when done.
4. `browser_snapshot` for page structure; `browser_take_screenshot` for visual verification.
5. Use `browser_click`, `browser_type`, `browser_scroll` only when needed for search/navigation — not for posting or account changes.

## Research passes

Same pass table as `live-browser-research.md` — client intel, tech stack, web evidence, pricing benchmarks, competitive context. Load the flavor reference for each pass.

## Discipline

- Same honesty bar: cite URLs, never invent data, read-only posture.
- If login/captcha blocks progress, stop and report — ask seller to complete auth or paste content.
- Set findings `"mode": "cursor-ide-browser"`.
- If four interaction attempts fail on the same goal, stop and document blocker in `caveats`.

## After gathering

Append all sections to findings JSON scratch. Return to SKILL.md **Produce the dossier**.
