# Local-Only Research

Loaded when `web_research_enabled` is false, `--headless` without browser tools, or neither browser-harness nor cursor-ide-browser is available.

## Notice (mandatory)

Tell the seller clearly:

> **Local-only research mode** — web intel, tech stack discovery, external benchmarks, and competitive context are limited to your brief, client history, pricing history, and case-study library. For full substantiation, enable `web_research_enabled` and install browser-harness, or paste research links inline.

Set findings `"mode": "local-only"`. The `caveats` field must state what was **not** scanned live.

## What still runs

| Section | Source |
| ------- | ------ |
| Local case-study matches | Full matching via `local-case-study-matching.md` |
| Client intel | `brief.md`, `clients/{slug}/history.md`, user-pasted links |
| Tech stack | Requirements in brief only unless user pasted stack info |
| Pricing benchmarks | `pricing-history.json` + brief budget field |
| Web evidence | User-pasted URLs only — empty array if none |
| Competitive context | Brief constraints + user input |

## User-pasted research

If the seller pastes articles, competitor names, or rate data, treat as valid sources — tag `source: seller-provided`. Same honesty rules: do not embellish pasted content.

## Optional markdown dossier emphasis

In local-only mode, the optional `research-dossier.md` companion is especially useful — generation may prefer markdown. Still render HTML via script so the UX stays consistent; empty web sections render with empty-state copy.

## After gathering

Write `recommendation` synthesizing what local proof supports and what's missing for pricing/generation to flag. Proceed to SKILL.md **Produce the dossier**.
