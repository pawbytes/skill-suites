# Stage 1: Ingest

**Goal:** Fully understand the input material and brand context before generating anything.

## Input Resolution

Accept input in any of these forms:
- **File path** — read the file
- **Pasted text** — use as-is
- `--from-skill <skill-name>` — find the most recent file that skill wrote in the brand's workspace (`{brands-folder}/{brand}/`, e.g. `sostac/` for `paw-mkt-sostac`) and read it; ask for the path if none is obvious

If the input is a paw-mkt-* skill output (SOSTAC plan, analytics report, campaign brief, etc.), recognize its structure and extract the relevant strategic content.

## Brand Context

Attempt to load brand context from `{brands-folder}/{brand}/brand-context.md` (see SKILL.md for picking the brand), then `{suite-root}/brand-config.json` if it exists:

1. If found, extract: brand name, audience, tone of voice, and any primary/secondary colors, fonts and logo path; `brand-config.json` values win for colors and fonts
2. If neither is found, use neutral defaults (deep navy + white palette, professional tone)

## What to Extract

From the input, identify and note:
- **Core strategic message** — the single most important thing this presentation must convey
- **Key sections** that warrant slides (objectives, situation, data points, recommendations, next steps)
- **Data/metrics present** — numbers, percentages, timelines that should become charts
- **Audience** — who will see this (exec, client, team)
- **Tone signals** — formal, confident, urgent, optimistic

## Headless Behavior

If headless: infer audience as "executive/client," tone as "professional and confident," and proceed to Stage 2.

## Confirmation (interactive only)

Surface a one-line read: "I see a [type] covering [core message] for [audience]. Generating outline now..." — then load `./references/02-outline.md`.

If anything critical is ambiguous (no discernible topic, empty input), ask one targeted question before proceeding.