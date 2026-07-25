# Inbox Conventions

Drop files in `library/inbox/`. Supported formats: `.md`, `.txt`, `.json`. PDF/DOCX may be converted to markdown manually or via pandoc before ingest.

## Filename Hints

| Pattern in filename | Routed as |
|---------------------|-----------|
| `case-study`, `casestudy`, `portfolio`, `success` | Case study index |
| `proposal`, `quote`, `pricing`, `estimate` | Pricing history |
| `terms`, `legal`, `contract` | `brand/boilerplate/terms.md` |
| `about`, `company`, `overview` | `brand/boilerplate/about-us.md` |
| `bio`, `bios`, `team` | `brand/boilerplate/bios.md` |
| `scope`, `sow`, `deliverable` | `scope-templates.md` |

Unclassified files are indexed as case studies with a warning.

## Recommended Frontmatter / Fields

Use plain markdown lines (case-insensitive):

```markdown
Client: Acme Corp
Industry: Healthcare
Service: Patient portal MVP
Outcome: Launched in 12 weeks, 99.9% uptime
Tags: healthcare, portal, react

## Deliverables
- Requirements workshop
- MVP build
- Handover documentation

Testimonial: "Exceeded expectations."
```

For pricing docs:

```markdown
Client: Acme Corp
Date: 2026-06-01
Proposal type: pitch
Won: yes

- Discovery — $5,000
- Build — $20,000
Total: $25,000
```

## Subfolders

Subfolders under `inbox/` are supported. `sourceDocPath` stores the relative path (e.g. `healthcare/acme-case.md`).

## After Moving or Deleting Source Files

Run validation to find orphans:

```bash
python3 scripts/ingest-library.py --memory-root ... --validate
```

Re-ingest or manually remove stale index entries.
