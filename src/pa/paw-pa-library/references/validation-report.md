# Validation Report

Run validation without re-ingesting:

```bash
python3 scripts/ingest-library.py \
  --memory-root "{project-root}/.pawbytes/proposal-automation-suites" \
  --validate \
  --report-path "{project-root}/.pawbytes/proposal-automation-suites/library/validation-report.json"
```

## Issue Types

| Type | Meaning | Remediation |
|------|---------|-------------|
| `orphaned_case_study` | Index entry points to missing inbox file | Restore file or remove entry from `case-studies-index.json` |
| `orphaned_pricing` | Pricing entry points to missing inbox file | Restore file or remove entry from `pricing-history.json` |
| `stale_manifest` | Manifest lists file no longer in inbox | Re-run ingest with `--force` or edit manifest |
| `unindexed` | Manifest has file not in JSON indexes | Re-run ingest; check classification |
| `not_ingested` | Inbox file never processed | Run ingest |

## Report Fields

- `status`: `ok` or `issues_found`
- `caseStudyCount`, `pricingHistoryCount`, `manifestFileCount`
- `issueCount`, `issues[]` with `type`, `sourceDocPath`, `message`

Present a concise summary to the user. For large libraries, offer the JSON report path for drill-down.

## HTML Report (Optional)

For interactive review, the agent may render `validation-report.html` from the JSON — not required for v1.
