# Documentation Quality Improvement Plan

> **Status:** Approved for phased implementation
> **Audience:** Contributors, maintainers, and reviewers
> **Scope:** Published documentation under `docs/` and the contributor standards that govern it

---

## Overview

This plan defines how Pawbytes Skill Suites documentation should be improved in a reusable, phased way. The audit found four recurring problems:

- cross-module structure drift between Marketing, Creative, and Tools docs
- outdated command names, paths, and behavior references in some published docs
- inconsistent Mermaid usage for workflows and routing diagrams
- no shared published-doc standard for contributors to follow

This document is the operating plan for fixing those issues without relying on one-off cleanup passes.

## Scope

### In scope

- Module READMEs under `docs/marketing`, `docs/creative`, and `docs/tools`
- Published skill pages under `docs/{module}/skills/`
- Workflow pages under `docs/{module}/workflows/`
- Technical contributor guidance under `docs/technical/`
- Cross-module documentation structure, links, terminology, and diagram usage

### Out of scope for the first pass

- Reorganizing the repository layout
- Changing skill behavior in `src/**/SKILL.md`
- Writing new product content beyond what is needed for consistency and clarity
- Deep content expansion for every doc page in one pass

## Source-of-Truth Rule

Use this rule for all future documentation work:

- `src/**/SKILL.md` is the canonical source for skill behavior, arguments, routing, names, and output paths
- `docs/**` is the explanation layer for users and contributors
- Published docs may simplify source behavior, but they must never contradict it

If a published doc disagrees with `src/**/SKILL.md`, treat that as a high-severity documentation issue.

---

## Documentation Quality Goals

1. **Accuracy** — command names, paths, and behavior match source truth
2. **Consistency** — the same doc types follow the same structure across modules
3. **Discoverability** — contributors can find standards and users can find the right entry point quickly
4. **Clarity** — markdown structure makes workflows, outputs, and next steps easy to scan
5. **Visual discipline** — Mermaid is used only where it improves understanding
6. **Maintainability** — documentation updates can be repeated using a standard workflow

---

## Quality Standard by Doc Type

### 1. Module README

Use this structure:

1. Overview
2. Who this module is for
3. Quick navigation
4. Skill inventory
5. Common workflows
6. Output or artifact model
7. Start here
8. Related technical docs

### 2. Skill Page

Use this structure:

1. Overview
2. When to use it
3. What you need to provide
4. What it does
5. What you get
6. Output location
7. Workflow overview
8. Arguments or modes
9. Related skills
10. Example prompts

### 3. Workflow Page

Use this structure:

1. Goal
2. Prerequisites
3. Workflow overview
4. Step-by-step process
5. Outputs created
6. Example dialogue
7. Next steps
8. Related docs

### 4. Reference Page

Use this structure:

1. Purpose
2. When to use it
3. Canonical rules
4. Examples
5. Related docs

---

## Markdown and Formatting Rules

### Use tables for

- comparisons
- arguments and options
- deliverables and artifact locations
- capability matrices
- taxonomy or severity summaries

### Use bullet lists for

- trigger phrases
- short preparation lists
- benefits
- caveats

### Use numbered lists for

- setup steps
- workflow procedures
- approval gates
- contributor update workflow

### Use code fences only for

- commands
- prompts and example dialogue
- file trees
- JSON, YAML, CSV, or text output
- Mermaid diagrams

Always label fences when possible:

- `bash`
- `text`
- `yaml`
- `json`
- `csv`
- `mermaid`

### Callout rules

Use callouts for important context instead of burying warnings in body text.

Recommended types:

- Note
- Tip
- Important
- Warning

### Terminology rules

- Use canonical skill IDs from source: `paw-mkt-*`, `paw-cra-*`, `paw-tools-*`
- Use one canonical path form in reference docs
- If a shorthand path is shown for readability, label it as shorthand
- Avoid mixing old command names with current names in the same doc set

---

## Mermaid Usage Policy

### Use Mermaid when

- a workflow has multiple steps, handoffs, or decision branches
- a coordinator routes work to specialists
- a lifecycle or state transition is easier to understand visually

### Prefer these diagram types

- `flowchart` for workflows, routing, and handoffs
- `sequenceDiagram` for interaction and lifecycle flow
- `stateDiagram` only when state changes are the main point

### Do not use Mermaid for

- file trees
- path examples
- static inventories
- simple linear content that reads clearly as a list

### Keep these as `text` fences

- directory trees
- output folder layouts
- CLI transcript examples

### Priority normalization targets

- `docs/marketing/README.md`
- `docs/creative/README.md`
- `docs/creative/user-guide/part-6-orchestration.md`
- `docs/tools/workflows/presentation-from-marketing-plan.md`
- `docs/tools/skills/paw-tools-presentation.md`
- `docs/tools/skills/paw-tools-release.md`

---

## Severity Model

### High

Fix first:

- incorrect command names
- wrong output paths
- contradictory workflow behavior
- published docs that disagree with `src/**/SKILL.md`
- broken links on primary navigation pages

### Medium

Fix early:

- inconsistent structure across the same doc type
- unclear audience framing
- weak cross-linking
- missing Mermaid where it would clearly help workflow comprehension

### Low

Fix during polish:

- minor formatting inconsistencies
- shallow examples where the behavior is still accurate
- non-blocking wording improvements

---

## Contributor Update Workflow

Use this workflow for future documentation updates:

1. Classify the document type
2. Compare the page to the standard for that doc type
3. Compare it against source truth when applicable
4. Fix structure, terminology, links, and diagram usage
5. Validate the page with the contributor checklist
6. Confirm that related hub pages still point to the right destination

### Definition of done for one page

A page is done when:

- names and paths are accurate
- required sections are present
- formatting follows the standard
- Mermaid usage follows the policy
- links resolve correctly
- next-step navigation is clear

---

## Phased Rollout Plan

## Phase 1 — Create the reusable plan and link it

Goal: make the standard discoverable before broader cleanup begins.

Files:
- `docs/technical/contributing/documentation-quality-improvement-plan.md`
- `docs/technical/contributing/README.md`
- `docs/technical/README.md`

Done when:
- the plan exists
- contributor docs link to it
- the technical docs hub exposes it as part of contributor guidance

## Phase 2 — Align contributor standards

Goal: make the standards and checklist reflect the same quality model.

Files:
- `docs/technical/contributing/conventions.md`
- `docs/technical/contributing/validation-checklist.md`
- `docs/technical/contributing/naming-conventions.md`

Done when:
- contributor standards reference the published-doc rules clearly
- Mermaid policy is documented consistently
- checklist criteria match the quality goals in this plan

## Phase 3 — Fix high-risk Marketing drift

Goal: remove the highest trust-risk inconsistencies first.

Priority files:
- `docs/marketing/README.md`
- `docs/marketing/skills/paw-mkt-dashboard.md`
- `docs/marketing/skills/paw-mkt-setup.md`
- `docs/marketing/workflows/sostac-planning.md`
- `docs/marketing/workflows/new-brand-onboarding.md`
- `docs/marketing/workflows/implementation-after-sostac.md`
- selected user-guide pages still using stale command names or paths

Done when:
- canonical `paw-mkt-*` naming is used consistently
- published paths match source truth
- primary workflow docs follow the shared workflow structure

## Phase 4 — Standardize Creative workflow and skill docs

Goal: keep Creative’s strong coverage while normalizing structure and diagram usage.

Priority files:
- `docs/creative/README.md`
- `docs/creative/user-guide/part-6-orchestration.md`
- `docs/creative/skills/paw-cra-agent-creative-director.md`
- `docs/creative/skills/paw-cra-agent-designer.md`
- `docs/creative/skills/paw-cra-agent-video-producer.md`
- `docs/creative/skills/paw-cra-setup.md`

Done when:
- routing and orchestration visuals use Mermaid where appropriate
- high-value skill pages reflect important source behavior without overloading readers
- page structure matches the shared standard

## Phase 5 — Normalize Tools docs

Goal: finish the cross-module pass with the smallest module.

Priority files:
- `docs/tools/README.md`
- `docs/tools/workflows/presentation-from-marketing-plan.md`
- `docs/tools/skills/paw-tools-presentation.md`
- `docs/tools/skills/paw-tools-release.md`
- `docs/tools/skills/paw-tools-setup.md`

Done when:
- setup is clearly discoverable
- workflow and utility pages follow the shared template
- Mermaid is used only where it helps multi-step understanding

## Phase 6 — Re-audit and maintain

Goal: make the process reusable for future work.

Done when:
- representative docs from each module pass the standard
- link validation passes across `docs/`
- future doc updates can use this plan and the checklist without a new audit

---

## File-Level Rollout Map

### Governance files

- `docs/technical/contributing/documentation-quality-improvement-plan.md`
- `docs/technical/contributing/README.md`
- `docs/technical/contributing/conventions.md`
- `docs/technical/contributing/validation-checklist.md`
- `docs/technical/README.md`

### High-priority user-facing files

- `docs/marketing/README.md`
- `docs/creative/README.md`
- `docs/tools/README.md`
- `docs/marketing/skills/paw-mkt-dashboard.md`
- `docs/marketing/skills/paw-mkt-setup.md`
- `docs/creative/user-guide/part-6-orchestration.md`
- `docs/tools/workflows/presentation-from-marketing-plan.md`

---

## Reusable References

Use these docs as structural references when carrying out later phases:

- `docs/sostac-gap-analysis.md`
- `docs/technical/contributing/README.md`
- `docs/technical/contributing/conventions.md`
- `docs/technical/contributing/validation-checklist.md`
- `docs/technical/contributing/naming-conventions.md`
- `docs/technical/README.md`

---

## Verification

### Plan verification

- The plan lives under `docs/technical/contributing/`
- It is linked from contributor-facing docs
- It defines standards, rollout phases, and done criteria clearly
- It does not contradict existing repo conventions

### Future implementation verification

- canonical names and paths match `src/**/SKILL.md`
- pages follow the shared doc-type structure
- Mermaid appears only where it improves workflow or routing clarity
- typed code fences are used consistently
- hub pages and related-doc links resolve correctly

### End-to-end validation later

- read updated technical and contributor hubs to confirm discoverability
- spot-check representative Marketing, Creative, and Tools pages against this plan
- re-run markdown link validation across `docs/`
- re-compare updated published docs against `src/*/SKILL.md` for names, paths, and behavior