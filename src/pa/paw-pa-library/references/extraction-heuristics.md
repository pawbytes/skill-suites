# Extraction Heuristics

The `ingest-library.py` script uses filename patterns first, then content keywords.

## Classification Order

1. Filename keywords (see `inbox-conventions.md`)
2. Content keywords in first ~2000 characters
3. Fallback: case study with warning

## Field Extraction

| Field | Patterns |
|-------|----------|
| `client` | `Client:` line or `## Client` heading |
| `industry` | `Industry:` line |
| `serviceType` | `Service:` or `Service type:` |
| `outcome` | `Outcome:` line |
| `testimonial` | `Testimonial:` or blockquote |
| `tags` | `Tags:` or `Keywords:` comma-separated |
| `deliverables` | Bullets under `## Deliverables` section |
| `lineItems` | `- Description — $amount` lines |
| `total` | `Total:` or `Grand total:` or largest `$` amount |
| `won` | `Won:` or `Status:` (yes/no/won/lost) |

## Limits

- Heuristic extraction is a bootstrap — not a substitute for LLM review on complex PDFs.
- JSON inbox files are classified by filename; content is not parsed as structured JSON in v1.
- Duplicate boilerplate sections are skipped via `<!-- ingested from {path} -->` markers.

## Improving Quality

1. Rename files to match conventions.
2. Add explicit `Client:` / `Industry:` lines at the top.
3. Re-run with `--force` after editing source docs.
