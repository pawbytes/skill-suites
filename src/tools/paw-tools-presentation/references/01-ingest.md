# Stage 1: Ingest

**Goal:** Fully understand the input material and brand context before generating anything.

## Input Resolution

Accept input in any of these forms:
- **File path** — read the file
- **Pasted text** — use as-is
- `--from-skill <skill-name>` — locate the most recent output from that skill under `{project-root}/.pawbytes/tools-output/<skill-name>/` and read it

If the input is a paw-mkt-* skill output (SOSTAC plan, analytics report, campaign brief, etc.), recognize its structure and extract the relevant strategic content.

## Brand Context

Attempt to load brand context from `{project-root}/.pawbytes/tools-output/paw-mkt-setup/brand-config.json`:

1. If found, extract: brand name, primary/secondary colors, logo path, tone of voice
2. If not found, use neutral defaults (deep navy + white palette, professional tone)

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