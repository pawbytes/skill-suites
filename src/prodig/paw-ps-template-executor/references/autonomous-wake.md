# Autonomous Wake Protocol

## Overview

This protocol activates when `--headless` or `-H` is passed. The agent executes tasks without interaction, making reasonable assumptions based on available context.

## Initialization Sequence

### 1. Load Context
Read all available context files in order:

1. `{project-root}/.pawbytes/prodig-suites/memory/paw-ps-sidecar/curated/product-context.md`
2. `{project-root}/.pawbytes/prodig-suites/memory/paw-ps-sidecar/curated/audience-intelligence.md`
3. `{project-root}/.pawbytes/prodig-suites/memory/paw-ps-sidecar/curated/output-standards.md`
4. `{project-root}/.pawbytes/prodig-suites/memory/paw-ps-sidecar/curated/product-types/template-products.md`

If any file is missing, note the gap and proceed with available context.

### 2. Parse Task Intent
From the command or input, identify:
- **Asset type**: template, prompt pack, digital kit, or swipe file
- **Domain/context**: what problem space or topic
- **Scope indicators**: any hints about size, complexity, or specific requirements

### 3. Make Reasonable Assumptions
When information is incomplete, make reasonable defaults:

| Missing Element | Default Assumption |
|-----------------|-------------------|
| Target audience | General business users, intermediate skill level |
| Price point | Market median for asset type |
| Platform | Cross-platform/agnostic unless specified |
| Complexity | Standard complexity, focus on 80% use case |
| Language | English (or `{communication_language}` from config) |

### 4. Execute Build
Proceed with the appropriate build process:

- **Template** → `./template-creation.md` build process
- **Prompt Pack** → `./prompt-pack-creation.md` build process
- **Digital Kit** → `./digital-kit-assembly.md` build process

### 5. Quality Verification
Run quality checks against `./asset-quality-standards.md`.

### 6. Save Artifacts
Write outputs to:
- Artifacts: `{project-root}/.pawbytes/prodig-suites/memory/paw-ps-sidecar/artifacts/{product-slug}/`
- Daily log: `{project-root}/.pawbytes/prodig-suites/memory/paw-ps-sidecar/daily/YYYY-MM-DD.md`

### 7. Report Completion
Output a structured completion report:

```
## Template Executor Complete

**Asset Type:** [template/prompt pack/digital kit]
**Product:** [name]
**Files Created:**
- [file path 1]
- [file path 2]
- ...

**Quality Status:** [Passed/Failed with notes]
**Assumptions Made:** [list any assumptions due to missing context]
**Recommended Next Steps:** [human review, testing, specific refinements]
```

## Error Handling

### Missing Context
If critical context is missing:
1. Note the gap in the completion report
2. Proceed with reasonable defaults
3. Flag for human review

### Build Failures
If the build cannot proceed:
1. Write error report to daily log
2. Output clear error message
3. Suggest required information or actions

### Quality Failures
If output doesn't meet quality standards:
1. Note specific failures in report
2. Attempt one remediation pass
3. If still failing, flag for human review

## Headless Output Format

All output in headless mode follows this structure:

```
# [Task Summary]

## Context Loaded
- [files read]

## Assumptions
- [assumptions made]

## Build Process
[steps executed]

## Output
[primary deliverables]

## Files Created
- [path 1]
- [path 2]

## Quality Status
[checklist results]

## Next Steps
[recommended actions]
```

## Limitations

Headless mode cannot:
- Clarify ambiguous requirements
- Present options for user choice
- Handle complex customization requests
- Make judgment calls on subjective preferences

For these situations, the agent will:
1. Document the limitation in the report
2. Provide a reasonable default
3. Recommend human review for refinement