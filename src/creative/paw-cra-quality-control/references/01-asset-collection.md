# Stage 1: Asset Collection

Scan the campaign folder to discover all produced assets and their manifests. This stage builds the inventory that all subsequent QC checks operate against.

## Goal

Produce a complete asset inventory --- every file that needs checking, grouped by type, with its metadata from the manifest.

## Discovery Process

Scan the campaign folder recursively for manifest files:

- `design-manifest.json` --- visual assets from Designer workflows
- `video-manifest.json` --- video assets from Video Producer workflows
- `clip-manifest.json` --- clips from the repurposing workflow
- `batch-manifest.json` --- batch-produced visual assets

For each manifest found, extract the asset list with metadata (file paths, intended platform, dimensions, format, codec, duration, etc.). Verify each referenced asset file actually exists on disk.

Also scan for orphan assets --- files in the campaign output folder that are not referenced by any manifest. These may be intermediate files, abandoned drafts, or assets that were never manifested.

## Expected Manifest Structure

Manifests are JSON files produced by production workflows. They vary by type but share common fields:

```json
{
  "campaign": "campaign-name",
  "brand": "brand-name",
  "produced_by": "paw-cra-design-social",
  "produced_at": "2026-04-01T12:00:00Z",
  "assets": [
    {
      "file": "relative/path/to/asset.png",
      "platform": "instagram-feed",
      "dimensions": "1080x1080",
      "format": "png",
      "status": "complete"
    }
  ]
}
```

If a manifest is malformed or unreadable, log a critical issue for that manifest and continue with other manifests.

## Output

Write the asset inventory to the `qa-report.md` front matter and first section:

```markdown
---
title: 'QA Report: {campaign-name}'
status: 'in-progress'
campaign: '{campaign-name}'
brand: '{brand-name}'
campaign_folder: '{campaign-folder-path}'
started: '{timestamp}'
updated: '{timestamp}'
total_assets: {count}
manifests_found: {count}
---

# QA Report: {campaign-name}

## Asset Inventory

### Visual Assets ({count})
| Asset | Platform | Dimensions | Format | Manifest |
|-------|----------|------------|--------|----------|
| ... | ... | ... | ... | ... |

### Video Assets ({count})
| Asset | Platform | Resolution | Codec | Duration | Manifest |
|-------|----------|------------|-------|----------|----------|
| ... | ... | ... | ... | ... | ... |

### Orphan Files ({count})
- {file path} --- not referenced in any manifest

### Missing Files ({count})
- {file path} --- referenced in {manifest} but not found on disk
```

## Progression

Proceed to Stage 2 when the inventory is complete. If zero assets are found, report that and ask the user whether to continue (in interactive mode) or exit with an empty report (in headless mode).
