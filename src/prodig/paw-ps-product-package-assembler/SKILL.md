---
name: paw-ps-product-package-assembler
description: Bundle product artifacts into a coherent, production-ready package. Use when the user requests 'package product', 'bundle artifacts', 'assemble deliverables', 'create product package', or 'finalize outputs'.
---

# Product Package Assembler

## Overview

This workflow bundles product artifacts from the execution phase into a coherent, production-ready package. It ensures outputs feel like one unified product, not scattered drafts, by gathering executor outputs, verifying completeness against product-type requirements, organizing into a structured bundle, and generating a comprehensive manifest.

**Args:** Accepts `--headless` / `-H` for non-interactive execution.

**Output:** Packaged product bundle with organized directory structure, completeness report, and packaging manifest.

## Principles

- **Unified output**: Ensure outputs feel like one product, not scattered drafts
- **Completeness verification**: Validate against product-type requirements before packaging
- **Traceability**: Maintain clear lineage from source artifacts to final package
- **Recovery-first design**: Use document-as-cache pattern for compaction survival
- **Graceful gaps**: Document missing items clearly rather than failing

## On Activation

Load available config from `{project-root}/.pawbytes/config/config.yaml` and `{project-root}/.pawbytes/config/config.user.yaml` (root level and `ps` section). If config is missing, let the user know `paw-ps-setup` can configure the module at any time. Resolve:

- `{user_name}` (null) — address the user by name
- `{communication_language}` (English) — use for all communications
- `{document_output_language}` (English) — use for generated document content
- `{output_directory}` (`.pawbytes/prodig-suites`) — base output path

Load shared memory from `{project-root}/.pawbytes/prodig-suites/index.md`. Load output standards from `{project-root}/.pawbytes/prodig-suites/output-standards.md`.

**Product context resolution:** Identify the active product from memory or accept a product slug as argument. The product workspace is expected at `.pawbytes/prodig-suites/products/{product-slug}/`. If no product can be resolved, ask the user.

If `--headless` or `-H` is passed, run the full pipeline without interaction: gather artifacts, check completeness, organize bundle, generate manifest.

Otherwise, greet the user, confirm the target product, and proceed through the stages below.

## Pipeline

This workflow progresses through four stages. Each stage updates the packaging status file using the document-as-cache pattern for compaction survival.

| Stage | Purpose | Reference |
|-------|---------|-----------|
| 1. Gather Artifacts | Collect all execution artifacts from executors | Load `./references/01-gather-artifacts.md` |
| 2. Check Completeness | Verify against product-type requirements | Load `./references/02-check-completeness.md` |
| 3. Organize Bundle | Structure into coherent package | Load `./references/03-organize-bundle.md` |
| 4. Generate Manifest | Create package manifest and notes | Load `./references/04-generate-manifest.md` |

**Progression:** Each stage updates `packaging-status.md` with its results before loading the next stage. If interrupted, resume from the last completed stage by reading `packaging-status.md`.

## Packaging Status File

All progress is written to `{project-root}/.pawbytes/prodig-suites/products/{product-slug}/packaging-status.md`. This file is both the output artifact and the recovery cache.

```yaml
---
product: '{product-slug}'
status: 'in-progress'  # pending | in-progress | complete | incomplete
current_stage: '01-gather-artifacts'
created: 'ISO-8601'
updated: 'ISO-8601'
artifacts_found: 0
artifacts_packaged: 0
missing_items: []
---
```

## Artifact Sources

Artifacts are collected from executor outputs:

| Source | Contains | Manifest File |
|--------|----------|---------------|
| Discovery agents | Research reports, briefs, specs | `discovery-manifest.json` |
| Strategist | Strategy documents, plans | `strategy-manifest.json` |
| Executor agents | Content, code, designs, media | `executor-manifest.json` |
| Synthesis workflows | Integrated deliverables | `synthesis-manifest.json` |

## Product Types & Completeness Criteria

Different product types have different required artifacts:

| Product Type | Required Artifacts |
|--------------|-------------------|
| Document | Main document, outline, research notes |
| Application | Code package, README, documentation |
| Campaign | Creative assets, copy, strategy brief |
| Report | Report document, data sources, methodology |
| Presentation | Slide deck, speaker notes, handouts |

## Output Structure

```
.pawbytes/prodig-suites/products/{product-slug}/package/
├── manifest.json           # Package manifest
├── completeness-report.md  # What's present, what's missing
├── packaging-notes.md      # Special considerations
├── artifacts/              # All gathered artifacts
│   ├── {artifact-1}
│   ├── {artifact-2}
│   └── ...
└── metadata/               # Supporting metadata
    ├── source-manifests/
    └── audit-trail.json
```

## Memory Contract

**Reads:**
- `{project-root}/.pawbytes/prodig-suites/index.md` — module state
- `{project-root}/.pawbytes/prodig-suites/output-standards.md` — output standards
- `{project-root}/.pawbytes/prodig-suites/products/{product-slug}/context.md` — product context
- Executor manifests from execution phase

**Writes:**
- `{project-root}/.pawbytes/prodig-suites/products/{product-slug}/packaging-status.md` — packaging progress
- `{project-root}/.pawbytes/prodig-suites/products/{product-slug}/package/` — packaged bundle
- `{project-root}/.pawbytes/prodig-suites/daily/{date}.md` — daily log (append, tagged `[Packaging]`)

## Escalation Routes

| Signal | Routes To |
|--------|-----------|
| Missing executor outputs | paw-ps-orchestrator (to rerun execution) |
| Incomplete artifacts | Appropriate executor agent |
| Quality issues | paw-ps-quality-reviewer |
| Export needs | paw-ps-export-handler |

## Output Contract

Every packaging deliverable includes:

- **Action type:** bundling, completeness-check, organizing
- **Files saved:** paths to all created files
- **Completeness status:** what's present vs. missing
- **Recommendations:** next steps (quality review, re-execution, etc.)
- **Package location:** resolved path to bundle