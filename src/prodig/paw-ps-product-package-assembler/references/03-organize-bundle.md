# Stage 3: Organize Bundle

Structure gathered artifacts into a coherent, production-ready package with consistent organization.

## Goal

Transform the raw artifact collection into a well-organized bundle that feels like one unified product.

## Package Structure

Create the standard package directory structure:

```
{product-slug}/package/
├── manifest.json           # Package manifest (Stage 4)
├── completeness-report.md  # Completeness report (Stage 2)
├── packaging-notes.md      # Packaging notes (Stage 4)
├── artifacts/              # All gathered artifacts
│   ├── primary/            # Main deliverables
│   │   └── {main-artifact}
│   ├── supporting/         # Supporting materials
│   │   ├── research/
│   │   ├── references/
│   │   └── resources/
│   └── metadata/           # Metadata and context
│       ├── product-context.md
│       └── execution-log.json
└── source-manifests/       # Original manifests for audit
    ├── discovery-manifest.json
    ├── strategy-manifest.json
    └── executor-manifest.json
```

## Organization Rules

### Primary Artifacts

Main deliverables go in `artifacts/primary/`:

- The main output the user requested
- Final versions only (no drafts)
- Named clearly: `{product-name}-v{version}.{ext}`

### Supporting Artifacts

Supporting materials go in categorized subfolders:

- `artifacts/supporting/research/` — Research notes, source materials
- `artifacts/supporting/references/` — Reference documents, standards
- `artifacts/supporting/resources/` — Assets, data files, configs

### Metadata Files

Context and audit information:

- `artifacts/metadata/product-context.md` — Product summary and context
- `artifacts/metadata/execution-log.json` — What ran, when, results

## Artifact Processing

For each artifact, determine:

1. **Category** — Primary, supporting, or metadata
2. **Subfolder** — Where it belongs
3. **Naming** — Standardized name if needed
4. **Format** — Convert if necessary (e.g., draft to final)

### Naming Conventions

Apply consistent naming:

| Type | Pattern | Example |
|------|---------|---------|
| Document | `{name}-v{version}.md` | `product-brief-v1.md` |
| Image | `{name}-{size}.{ext}` | `hero-1920x1080.png` |
| Code | `{name}.{ext}` | `main.py` |
| Config | `{name}.yaml` | `config.yaml` |

### Version Handling

If multiple versions exist:

- Keep only the latest in `primary/`
- Archive older versions in `supporting/versions/`
- Note version history in packaging notes

## Cross-Product Consistency

Ensure all artifacts feel cohesive:

1. **Branding** — Consistent naming, headers, formatting
2. **References** — Cross-references between artifacts work
3. **Metadata** — Consistent date formats, author info
4. **Structure** — Predictable organization

## Output

Create the organized package directory. Update `packaging-status.md`:

```markdown
## Bundle Organization

### Package Structure Created
```
package/
├── artifacts/
│   ├── primary/
│   │   └── {count} files
│   ├── supporting/
│   │   └── {count} files
│   └── metadata/
│       └── {count} files
└── source-manifests/
    └── {count} files
```

### Files Organized
| Source | Destination | Type |
|--------|-------------|------|
| ... | ... | ... |

### Renames Applied
| Original | New Name | Reason |
|----------|----------|--------|
| ... | ... | ... |

### Warnings
- {any issues encountered during organization}
```

## Progression

Proceed to Stage 4 (Generate Manifest) when:

1. All artifacts are organized into the package structure
2. Directory structure is complete
3. Files are properly named and categorized

If organization fails for any artifact, log the issue and either:
- Skip and note (non-critical)
- Halt and alert (critical)