# Client Intelligence

Loaded when web research is enabled, or when the user pasted client context / links. Builds the **Client intelligence** section of the dossier.

## Goal

Give the proposal a factual picture of the prospect: industry, size signals, recent news, hiring/growth signals, and anything from `brief.md` `clientContext` that can be verified or expanded — never speculative psychographics.

## Sources (in priority order)

1. **`brief.md`** — `clientName`, `clientContext`, `decisionMaker` (seller-provided baseline)
2. **Client website** — about, news/press, careers (growth/hiring signals)
3. **Public profiles** — LinkedIn company page, Crunchbase, industry directories (when findable)
4. **News search** — recent announcements, funding, leadership changes (cite article URLs)
5. **`clients/{slug}/history.md`** — prior proposals to this client (returning-client context)

## What to extract

Record as `clientIntel.signals[]` entries:

| Label | Examples |
| ----- | -------- |
| Industry | NAICS-like sector, B2B/B2C |
| Size | Employee count range, revenue band if public |
| Recent news | Product launch, acquisition, leadership hire |
| Pain signals | From brief + corroborating public info |
| Relationship | Returning client? Prior proposal outcomes from history |

Each signal needs `label`, `detail`, and `source` (URL, `brief.md`, or `clients/{slug}/history.md`).

## Discipline

- **Never invent revenue, headcount, or news.** If not found, omit — do not estimate.
- **Distinguish seller-provided vs observed.** Tag source as `brief.md (seller)` vs live URL.
- **Returning clients:** Lead with `history.md` summary before web search — prior context is highest-trust.

## Local-only mode

If web is disabled, build `clientIntel` only from `brief.md`, `history.md`, and any URLs the user pasted inline. Set `summary` to note: "Based on brief and client history only; no live web intel."

## After gathering

Write `clientIntel.summary` — one paragraph tying signals to why this proposal angle fits. Append to findings JSON scratch file.
