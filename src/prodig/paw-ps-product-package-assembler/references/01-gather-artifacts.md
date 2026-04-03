# Stage 1: Gather Artifacts

Collect all execution artifacts from the various executor outputs and manifests. This stage builds the artifact inventory that subsequent stages will verify and organize.

## Goal

Produce a complete artifact inventory — every file produced during execution, grouped by source, with metadata from the manifests.

## Discovery Process

Scan the product workspace for manifest files:

- `discovery-manifest.json` — outputs from discovery agents
- `strategy-manifest.json` — strategy documents from strategist
- `executor-manifest.json` — primary execution outputs
- `synthesis-manifest.json` — integrated deliverables from synthesis workflows

For each manifest found, extract:

1. **Artifact list** — file paths, types, descriptions
2. **Metadata** — created timestamp, version, dependencies
3. **Source info** — which agent/workflow produced it
4. **Status** — complete, partial, draft

Verify each referenced artifact file exists on disk.

## Manifest Structure

Manifests follow a consistent structure:

```json
{
  "product": "product-slug",
  "produced_by": "paw-ps-{agent-or-workflow}",
  "produced_at": "2026-04-02T12:00:00Z",
  "artifacts": [
    {
      "file": "relative/path/to/artifact.md",
      "type": "document",
      "description": "Main product brief",
      "status": "complete",
      "dependencies": []
    }
  ]
}
```

## Orphan Detection

Scan for orphan artifacts — files in the product output folder not referenced by any manifest:

- Intermediate files from executor runs
- Abandoned drafts
- Files produced outside the normal workflow

These may need to be included or flagged for review.

## Output

Write the artifact inventory to `packaging-status.md`:

```markdown
---
product: '{product-slug}'
status: 'in-progress'
current_stage: '01-gather-artifacts'
created: '{timestamp}'
updated: '{timestamp}'
artifacts_found: {count}
missing_items: []
---

# Packaging Status: {product-slug}

## Artifact Inventory

### Discovery Artifacts ({count})
| Artifact | Type | Source | Status |
|----------|------|--------|--------|
| ... | ... | ... | ... |

### Strategy Artifacts ({count})
| Artifact | Type | Source | Status |
|----------|------|--------|--------|
| ... | ... | ... | ... |

### Execution Artifacts ({count})
| Artifact | Type | Source | Status |
|----------|------|--------|--------|
| ... | ... | ... | ... |

### Synthesis Artifacts ({count})
| Artifact | Type | Source | Status |
|----------|------|--------|--------|
| ... | ... | ... | ... |

### Orphan Files ({count})
- {file path} — not referenced in any manifest

### Missing Files ({count})
- {file path} — referenced in {manifest} but not found on disk
```

## Progression

Proceed to Stage 2 (Check Completeness) when:

1. All manifests have been scanned
2. Artifact inventory is complete
3. Missing files are identified

If zero artifacts are found, report that and ask whether to:
- Wait for execution to complete (interactive)
- Exit with empty report (headless)
- Trigger re-execution via orchestrator