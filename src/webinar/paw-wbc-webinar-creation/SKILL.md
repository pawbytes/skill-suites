---
name: paw-wbc-webinar-creation
description: "Guided webinar creation pipeline from vague idea to production-ready deliverables. Use when creating a webinar from scratch. Triggers: 'create a webinar', 'build a webinar', 'webinar creation', 'new webinar', 'help me make a webinar'."
---

# Webinar Creation Pipeline

## Overview

The Webinar Creation Pipeline is a guided workflow that takes solo creators from a vague webinar idea to production-ready deliverables. Users experience one continuous journey through discovery research and production — no agent selection required.

**Args:** Interactive only. This workflow is designed for guided conversation.

**Output:** Complete webinar package including slide deck outline, script, and recommendations saved to `.pawbytes/webinar-suites/webinars/{webinar-slug}/`.

## Principles

- **One continuous conversation** — User never needs to decide "which agent do I need"
- **Clear progress indication** — Always show "Stage X of 4" status
- **Gates between phases** — User confirms readiness before proceeding
- **Resumable** — If user pauses, workflow can resume from last checkpoint
- **Transparent handoffs** — When calling agents, briefly explain what's happening
- **Output-focused** — Every step serves the final deliverable

## Pipeline

### Stage 1: Brief Intake

Load `./references/01-brief-intake.md`

**Purpose:** Capture the user's initial idea, audience context, and goals. Create the foundation for discovery research.

**Progression:** Brief is captured and saved to `brief.md`. User confirms readiness to proceed to discovery.

---

### Stage 2: Discovery Phase

Load `./references/02-discovery-phase.md`

**Purpose:** Transform vague idea into clear, defensible hook backed by research.

**Activities:**
1. Invoke `paw-wbc-agent-discovery`
2. Brief expansion and enrichment
3. Webinar kind detection (auto-detect + user approval)
4. Deep research on topic landscape
5. Research compression for production use
6. Hook generation (5-10 distinct angles)
7. Hook selection with user
8. Gate assessment: "Ready for production?"

**Progression:** User selects hook and confirms readiness for production phase. Discovery outputs saved to `research-context.md` and `hook-selected.md`.

---

### Stage 3: Production Phase

Load `./references/03-production-phase.md`

**Purpose:** Transform research and hook into production-ready deliverables.

**Activities:**
1. Invoke `paw-wbc-agent-producer`
2. Load discovery context (brief, research, hook)
3. Structure the webinar narrative
4. Generate slide deck outline (detailed, LLM-ready)
5. Write script (full script for key moments, talking points elsewhere)
6. Surface recommendations for Q&A or backup

**Progression:** All production outputs generated and saved. User reviews deliverables.

---

### Stage 4: Output Delivery

Load `./references/04-output-delivery.md`

**Purpose:** Present final deliverables clearly and guide next steps.

**Activities:**
1. Summarize what was created
2. List all files and their purposes
3. Provide next-step recommendations
4. Log completion to daily activity

**Progression:** Workflow complete. User has everything needed to build and deliver their webinar.

---

## Path Resolution

**Module root:** `{project-root}/.pawbytes/webinar-suites/`

**Webinar workspace:** `{project-root}/.pawbytes/webinar-suites/webinars/{webinar-slug}/`

**Output files:**

| File | Purpose | Created By |
|------|---------|------------|
| `brief.md` | Initial brief + audience context | Stage 1 |
| `research-context.md` | Compressed research findings | Stage 2 |
| `hook-selected.md` | Chosen hook + reasoning | Stage 2 |
| `slide-deck-outline.md` | LLM-ready slide structure | Stage 3 |
| `script.md` | Full script + talking points | Stage 3 |
| `recommendations.md` | Surfaced insights | Stage 3 |

**Daily log:** `{project-root}/.pawbytes/webinar-suites/daily/{YYYY-MM-DD}.md`

If no webinar slug exists, generate one using the slug generation algorithm.

> **See:** `paw-wbc-agent-discovery` SKILL.md "Slug Generation Algorithm" section for full specification including unicode normalization (NFKD), keyword extraction, punctuation removal, truncation (41-char base for 50-char final), and uniqueness checks.

## Reference Lookup Protocol

Each stage loads its detailed guidance from `./references/` on demand:

1. Stage begins → Load corresponding reference file
2. Follow guidance for that stage
3. Complete progression criteria → Move to next stage

## Escalation Routes

| Signal | Routes To |
|--------|-----------|
| User wants visual slide design | paw-cra-agent-designer |
| User wants webinar promotion strategy | paw-mkt-agent-agency |
| User wants to run discovery only | paw-wbc-agent-discovery |
| User wants to run production only (has research) | paw-wbc-agent-producer |

## Output Contract

Every completed webinar creation includes:

- **Action type:** Full webinar creation pipeline
- **Webinar slug:** Identifier for this webinar project
- **Webinar kind:** Detected and approved type
- **Selected hook:** Chosen angle with reasoning
- **Files saved:**
  - `brief.md` — enriched brief and audience context
  - `research-context.md` — compressed research findings
  - `hook-selected.md` — chosen hook and reasoning
  - `slide-deck-outline.md` — detailed slide-by-slide with content points and visual direction
  - `script.md` — full script for key moments, talking points elsewhere
  - `recommendations.md` — research insights for Q&A or backup
- **File saved to:** `{project-root}/.pawbytes/webinar-suites/webinars/{webinar-slug}/`
- **Next recommended actions:** Rehearse, design slides, refine sections, promote

## Resumption Support

If user returns mid-pipeline:

1. Check for existing files in `{webinar-slug}/` directory
2. Identify last completed stage by presence of outputs:
   - `brief.md` only → Resume at Stage 2
   - `brief.md` + `research-context.md` + `hook-selected.md` → Resume at Stage 3
   - All outputs present → Offer to start new webinar or review existing
3. Acknowledge resumption: "Welcome back! You're in Stage X of 4 (Stage Name) of your webinar on [topic]. Let's continue."