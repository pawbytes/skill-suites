# Stage 4: Generate Manifest

Create the package manifest and packaging notes to complete the bundle.

## Goal

Generate comprehensive documentation of the package contents, completeness status, and special considerations.

## Manifest Generation

Create `manifest.json` at the package root:

```json
{
  "manifest_version": "1.0",
  "product": {
    "slug": "{product-slug}",
    "name": "{product-name}",
    "type": "{product-type}",
    "version": "{version}"
  },
  "packaging": {
    "packaged_at": "{ISO-8601}",
    "packaged_by": "paw-ps-product-package-assembler",
    "completeness": "complete|partial|incomplete",
    "completeness_score": 95
  },
  "artifacts": {
    "primary": [
      {
        "path": "artifacts/primary/{filename}",
        "type": "{type}",
        "size_bytes": {size},
        "checksum": "{sha256}",
        "description": "{description}"
      }
    ],
    "supporting": [
      {
        "path": "artifacts/supporting/{category}/{filename}",
        "type": "{type}",
        "size_bytes": {size},
        "checksum": "{sha256}",
        "description": "{description}"
      }
    ],
    "metadata": [
      {
        "path": "artifacts/metadata/{filename}",
        "type": "{type}",
        "description": "{description}"
      }
    ]
  },
  "sources": {
    "discovery_manifest": "source-manifests/discovery-manifest.json",
    "strategy_manifest": "source-manifests/strategy-manifest.json",
    "executor_manifest": "source-manifests/executor-manifest.json"
  },
  "requirements": {
    "required_present": 3,
    "required_total": 3,
    "recommended_present": 2,
    "recommended_total": 3,
    "missing_required": [],
    "missing_recommended": ["user-guide"]
  }
}
```

## Completeness Report

Create `completeness-report.md` (or finalize from Stage 2):

```markdown
# Completeness Report: {product-name}

**Generated:** {timestamp}
**Status:** {status}
**Score:** {percentage}%

## Summary

| Category | Present | Total | Status |
|----------|---------|-------|--------|
| Required | {n} | {n} | {status} |
| Recommended | {n} | {n} | {status} |
| Optional | {n} | {n} | {status} |

## Artifacts Inventory

### Primary Artifacts
| Artifact | Type | Size | Checksum |
|----------|------|------|----------|
| ... | ... | ... | ... |

### Supporting Artifacts
| Artifact | Type | Category | Size |
|----------|------|----------|------|
| ... | ... | ... | ... |

## Missing Items

### Required (Blockers)
{none or list with impact}

### Recommended (Warnings)
{none or list with impact}

## Recommendations

1. {recommendation-1}
2. {recommendation-2}
```

## Packaging Notes

Create `packaging-notes.md` for special considerations:

```markdown
# Packaging Notes: {product-name}

## Package Overview

{brief description of what was packaged}

## Special Considerations

### File Handling
- {any special handling applied}
- {conversions performed}
- {version decisions made}

### Known Issues
- {any known issues with the package}
- {limitations or caveats}

### Dependencies
- {external dependencies if any}
- {runtime requirements}

### Validation Notes
- {what was validated}
- {what needs manual review}

## Execution Trace

| Stage | Status | Timestamp | Notes |
|-------|--------|-----------|-------|
| Gather Artifacts | complete | {ts} | {notes} |
| Check Completeness | complete | {ts} | {notes} |
| Organize Bundle | complete | {ts} | {notes} |
| Generate Manifest | complete | {ts} | {notes} |

## Next Steps

1. {recommended-next-step-1}
2. {recommended-next-step-2}

Common next steps:
- Run quality review (`/paw-ps-quality-reviewer`)
- Export to target format (`/paw-ps-export-handler`)
- Archive package version
```

## Audit Trail

Create `metadata/audit-trail.json`:

```json
{
  "product": "{product-slug}",
  "packaging_session": {
    "started": "{ISO-8601}",
    "completed": "{ISO-8601}",
    "duration_seconds": {seconds},
    "stages": [
      {
        "stage": "gather-artifacts",
        "started": "{ISO-8601}",
        "completed": "{ISO-8601}",
        "artifacts_found": {count}
      },
      {
        "stage": "check-completeness",
        "started": "{ISO-8601}",
        "completed": "{ISO-8601}",
        "completeness_score": {score}
      },
      {
        "stage": "organize-bundle",
        "started": "{ISO-8601}",
        "completed": "{ISO-8601}",
        "files_organized": {count}
      },
      {
        "stage": "generate-manifest",
        "started": "{ISO-8601}",
        "completed": "{ISO-8601}",
        "manifests_created": {count}
      }
    ]
  },
  "source_manifests": [
    "{manifest-path-1}",
    "{manifest-path-2}"
  ],
  "checksums": {
    "manifest.json": "{sha256}",
    "completeness-report.md": "{sha256}",
    "packaging-notes.md": "{sha256}"
  }
}
```

## Final Status Update

Update `packaging-status.md` to complete:

```yaml
---
product: '{product-slug}'
status: 'complete'
current_stage: '04-generate-manifest'
created: '{timestamp}'
updated: '{timestamp}'
artifacts_found: {count}
artifacts_packaged: {count}
completeness_score: {percentage}
missing_items: []
---
```

## Completion Actions

1. **Write daily log entry** to `.pawbytes/prodig-suites/daily/{date}.md`:

```markdown
## [Packaging] {product-slug}

- Status: complete
- Artifacts packaged: {count}
- Completeness: {percentage}%
- Package location: {path}
```

2. **Return summary** to user:

```markdown
# Packaging Complete: {product-name}

**Package Location:** `{package-path}`

**Summary:**
- {count} artifacts packaged
- {percentage}% complete
- {status}

**Files Created:**
- `manifest.json` — Package manifest
- `completeness-report.md` — Completeness details
- `packaging-notes.md` — Special considerations

**Next Steps:**
1. Run quality review: `/paw-ps-quality-reviewer`
2. Export if needed: `/paw-ps-export-handler`
```

## Progression

This is the final stage. The workflow is complete when:

1. `manifest.json` is created
2. `completeness-report.md` is finalized
3. `packaging-notes.md` is written
4. `packaging-status.md` shows complete
5. Daily log entry is written

The package is now ready for quality review.