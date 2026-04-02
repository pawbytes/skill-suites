---
name: paw-ps-concept-to-product-plan
description: "Transform an accepted product brief into an executor-ready product plan. Triggers: 'create product plan', 'product plan from brief', 'prepare for executor', 'plan for building', 'handoff to builder'."
---

# Concept to Product Plan

## Overview

Transforms an accepted product brief into a detailed, executor-ready product plan. This workflow bridges product decisions and execution by producing specific instructions for the correct builder type.

**Args:** Accepts `--headless` / `-H` for non-interactive execution.

**Output:** Product plan/spec package and executor handoff bundle.

## Inputs

- Product brief (from `product-decisions.md` or brief file)
- Chosen product family (knowledge, template, software, service)
- Scope and packaging decisions

## Outputs

| Output | Location |
|--------|----------|
| Product plan | `.pawbytes/prodig-suites/plans/{product-slug}/plan.md` |
| Executor handoff | `.pawbytes/prodig-suites/plans/{product-slug}/handoff.md` |
| Product context update | `.pawbytes/prodig-suites/brands/{brand-slug}/products/{product-slug}/product-context.md` |

## Pipeline

### Stage 1: Load Brief

Load `./references/01-load-brief.md`

**Inputs:** Product brief location or product-decisions.md

**Progression:** Brief is loaded and completeness verified. All required sections present.

### Stage 2: Identify Executor

Load `./references/02-identify-executor.md`

**Inputs:** Product family selection, product type

**Progression:** Executor type determined and validated against product requirements.

### Stage 3: Create Plan

Load `./references/03-create-plan.md`

**Inputs:** Brief, executor type, scope decisions

**Progression:** Detailed execution plan created with all sections populated.

### Stage 4: Prepare Handoff

Load `./references/04-prepare-handoff.md`

**Inputs:** Product plan, executor type

**Progression:** Executor handoff bundle formatted and saved. Product context updated with plan reference.

## On Activation

1. Load shared context from `{project-root}/.pawbytes/prodig-suites/index.md`
2. Check for active brand: `.pawbytes/prodig-suites/brands/{brand-slug}/brand-context.md`
3. Load product context: `.pawbytes/prodig-suites/brands/{brand-slug}/products/{product-slug}/product-context.md`
4. If no product slug provided, list available products for selection

## Path Resolution

**Plans root:** `{project-root}/.pawbytes/prodig-suites/plans/{product-slug}/`

**Product context:** `{project-root}/.pawbytes/prodig-suites/brands/{brand-slug}/products/{product-slug}/product-context.md`

**Handoff bundle:** `{project-root}/.pawbytes/prodig-suites/plans/{product-slug}/handoff.md`

## Executor Types

| Product Family | Executor | Plan Focus |
|----------------|----------|------------|
| Knowledge | Knowledge Builder | Content structure, research scope, deliverable format |
| Template | Template Builder | Component structure, customization points, usage patterns |
| Software | Software Builder | Technical specs, architecture, implementation phases |
| Service | Service Builder | Service definition, delivery process, quality criteria |

## Output Contract

Every product plan includes:
- **Plan type:** Which executor will use it
- **Source brief:** Reference to original decisions
- **Scope:** What is included and excluded
- **Deliverables:** Specific outputs expected
- **Success criteria:** Measurable completion conditions
- **File saved to:** Resolved path

## Non-Negotiables

1. Plan must be specific enough for executor to act without clarification
2. All scope decisions must be explicitly stated
3. Executor type must be clearly identified
4. Handoff bundle must be self-contained