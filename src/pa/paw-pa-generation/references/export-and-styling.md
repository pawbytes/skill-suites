# Export & Styling

Turns the finalized markdown draft into branded, client-ready exports. The LLM does content; this reference + `scripts/export_proposal.py` handle plumbing.

## Brand snapshot

Before export, build `{run-folder}/brand-snapshot.json` from `brand/identity.md`:

```json
{
  "companyName": "PawBytes Studio",
  "logoPath": "relative/or/absolute/path/to/logo.png",
  "colors": {
    "primary": "#1a365d",
    "secondary": "#2b6cb0",
    "accent": "#ed8936",
    "text": "#1a202c",
    "background": "#ffffff"
  },
  "fonts": {
    "heading": "Georgia, serif",
    "body": "system-ui, -apple-system, sans-serif"
  },
  "voice": "Professional, direct, warm"
}
```

Parse hex colors, font stacks, and logo path from `identity.md`. If logo path is relative, resolve from `{memory-root}/brand/`. If logo missing, export proceeds without it.

## Export formats

| Format | Method | Always available |
|--------|--------|------------------|
| `final-proposal.html` | Script renders styled HTML with brand CSS | Yes |
| `final-proposal.md` | Copy of draft with export metadata header | Yes |
| `final-proposal.pdf` | Pandoc from HTML or MD | Requires pandoc |
| `final-proposal.docx` | Pandoc from MD | Requires pandoc |

## Run the export script

```bash
python3 scripts/export_proposal.py \
  --input "{run-folder}/draft-v1.md" \
  --brand-json "{run-folder}/brand-snapshot.json" \
  --out-dir "{run-folder}" \
  --formats html,md,pdf,docx \
  --basename final-proposal
```

Options:
- `--no-open` — skip auto-opening HTML in browser
- `--formats` — comma-separated subset: `html`, `md`, `pdf`, `docx`

Script outputs JSON to stdout:

```json
{
  "ok": true,
  "exports": {
    "html": "/path/to/final-proposal.html",
    "md": "/path/to/final-proposal.md",
    "pdf": null,
    "docx": "/path/to/final-proposal.docx"
  },
  "pandoc_available": true,
  "warnings": ["pdf: pandoc failed — missing pdflatex"]
}
```

## Pandoc check

```bash
command -v pandoc
```

If missing:
- Still produce HTML and MD.
- Note in `generation-summary.json` warnings: `"pandoc not found — PDF/DOCX skipped"`.
- Tell the seller they can install pandoc or open HTML and print-to-PDF.

If pandoc present but PDF engine missing:
- DOCX usually still works.
- PDF may fail — surface the stderr in warnings; HTML remains the primary deliverable.

## HTML styling rules

The script applies brand CSS:

- **Header band** — primary color background, logo left, company name right
- **Typography** — heading font for h1–h3, body font for paragraphs
- **Tables** — bordered, alternating row shading with secondary color tint
- **Assumptions callout** — accent color left border, light background
- **Print-friendly** — `@media print` hides nav, ensures page breaks before major sections
- **Responsive** — max-width 800px content column, readable on mobile

The LLM does not hand-craft HTML — the script wraps the markdown body.

## Manual export fallback

If the script cannot run:

1. Copy `draft-v1.md` → `final-proposal.md` with metadata header:

```markdown
---
title: {proposal title}
client: {client name}
type: {proposalType}
generated: {ISO date}
language: {language}
---

```

2. For HTML: wrap markdown content in a minimal HTML shell using brand colors from `identity.md`.
3. For PDF/DOCX: instruct seller to run pandoc manually or use HTML print-to-PDF.

## Multi-language export

Export in the proposal's target language — the draft is already translated. Do not re-translate at export time. Set `<html lang="...">` from brief language code when known.

## Revision exports

On `draft-v2+`, re-export `final-proposal.*` from the latest standard draft. Optionally archive prior finals as `final-proposal-v1.html` if the seller wants version history — ask before overwriting if a final already exists and the user didn't request replace.
