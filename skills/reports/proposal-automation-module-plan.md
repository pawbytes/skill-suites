---
title: 'Proposal Automation Module Plan'
status: 'complete'
module_name: 'PawBytes Proposal Automation Suite'
module_code: 'paw-pa'
module_description: 'Turns messy multimodal briefs (text/audio/video) into polished, researched, priced proposals — end to end, for any proposal type.'
architecture: 'orchestrator agent + specialist workflows (single shared memory)'
standalone: true
expands_module: ''
skills_planned:
  - paw-pa-setup
  - paw-pa-agent-orchestrator
  - paw-pa-intake
  - paw-pa-research
  - paw-pa-pricing
  - paw-pa-generation
  - paw-pa-library
config_variables:
  - assemblyai_api_key
  - default_mode
  - default_proposal_type
  - default_language
  - default_pricing_mode
  - default_hourly_rate
  - workspace_folder
  - library_inbox_folder
  - web_research_enabled
created: '2026-07-02T15:40:00Z'
updated: '2026-07-03T06:01:00Z'
---

# Module Plan

## Vision

Turns messy multimodal briefs (text/audio/video) into polished, researched, priced proposals — end to end, for any proposal type (pitch, RFP response, scoping doc). Built for sellers only. Runs in two modes: autonomous (brief in → proposal out, no check-ins, assumptions flagged) and guided (check-ins at research, pricing, and draft stages). Case-study matching uses a local indexed library built from the user's own dropped docs; research adds deep web evidence and benchmarks. Every valuable artifact — case studies, pricing history, win/loss outcomes, client history, scope templates — persists in shared memory to make the next proposal better.

## Architecture

**Decision: Orchestrator agent + specialist workflows (Option C).** A conversational orchestrator agent for guided mode (the human-facing partner that runs the pipeline, asks clarifying questions on thin briefs, and handles check-ins) plus specialist workflows for each heavy-lifting phase (intake, research, pricing, generation), plus a library workflow and a setup workflow. All skills share a single memory pool.

**Rationale:**

- **Both modes (autonomous + guided)** require something that can either run straight through or pause for check-ins. An orchestrator agent is the natural carrier of that toggle. Pure workflows can't do guided mode well — there's nothing to converse with.
- **Ask clarifying questions on thin briefs** is conversational — must be an agent, not a workflow.
- **Single shared memory** ("anything valuable for next proposal") argues against multiple agents fragmenting memory. One shared pool, all skills read/write it.
- **Pipeline is fundamentally linear with discrete heavy phases** — workflows are the right shape for the phases (intake, research, pricing, generation). An agent per phase would be overkill; there's no distinct persona for "pricing" or "intake," just heavy work.
- **Workflows are independently invokable** — power users can re-run pricing on an old brief, re-index the library, or regenerate a proposal without running the whole pipeline.
- **Matches the `paw-*` family pattern** (`paw-upwork`, `paw-mkt`) — orchestrator agent + specialist workflows, single shared memory. Feels native in the PawBytes world.

The orchestrator is the **brain and voice**; the workflows are the **hands**. Orchestrator decides what to run, in what order, with what check-ins; workflows do the heavy lifting and write artifacts to disk. Each workflow is independently testable and maintainable.

### Memory Architecture

**Single shared memory (per seller)** — recommended for tightly coupled skills where every phase benefits from full visibility into everything the suite has learned. Every skill reads the seller's brand, library index, pricing history, win/loss record, and client history on activation. The orchestrator writes the canonical run state; workflows read inputs and append their outputs + outcomes.

Workspace layout (mirrors `paw-upwork`'s `.pawbytes/upwork-suites/` and `paw-mkt`'s `.pawbytes/marketing-suites/` conventions; single-seller v1 uses a flat suite root — no `sellers/{slug}/` tenant layer):

```
{project-root}/.pawbytes/proposal-automation-suites/
├── index.md                      # orientation — every skill reads this first
├── brand/
│   ├── identity.md               # logo, colors, fonts, voice
│   └── boilerplate/
│       ├── about-us.md
│       ├── terms.md              # T&Cs template (user-provided)
│       └── bios.md
├── library/
│   ├── case-studies-index.json   # structured index of ingested case studies
│   ├── pricing-history.json      # past quotes → calibration data
│   └── scope-templates.md        # reusable scope/deliverable clauses
├── proposals/                    # one folder per proposal run
│   └── {slug}-{date}/
│       ├── brief.md              # structured brief artifact
│       ├── research-dossier.html
│       ├── pricing.json
│       ├── draft-v1.md
│       ├── final-proposal.{pdf,docx,html}
│       └── outcome.md            # won/lost + lessons (added later)
├── clients/                      # per-client memory (returning clients)
│   └── {client-slug}/
│       └── history.md
└── daily/
    └── YYYY-MM-DD.md             # timestamped append-only log
```

**Operational model:**

- **Daily files** (`daily/YYYY-MM-DD.md`) — every session, the active skill appends timestamped entries tagged by skill name (`[intake]`, `[research]`, etc.). Raw, chronological, append-only.
- **Curated files** (organized by topic) — distilled knowledge that skills load on activation. Updated through inline curation (obvious updates go straight to the file) and periodic deep curation.
- **Index** (`index.md`) — orientation document every skill reads first. Summarizes what curated files exist, when each was last updated, and recent activity. Skills selectively load only what's relevant.
- **Run artifacts** (`proposals/{slug}-{date}/`) — each pipeline run gets its own folder. Brief, research dossier, pricing breakdown, drafts, final proposal, and outcome all live here. Workflows write to this folder; the orchestrator creates the folder at run start.

### Memory Contract

| File | Purpose | Read by | Written by | Key content |
|---|---|---|---|---|
| `index.md` | Orientation — what's in memory, last-updated, recent activity | All skills on activation | Orchestrator (curation), any skill that updates curated files | Sections: brand summary, library size + last reindex, recent proposals (last 5), open client threads, recent daily entries |
| `brand/identity.md` | Seller's brand identity | Generation, orchestrator | Orchestrator (from setup / runtime edits) | Logo path, color palette (hex), fonts, voice description, default language |
| `brand/boilerplate/about-us.md` | Standard about-us copy | Generation | Orchestrator (from setup / runtime edits), library (if dropped as doc) | Markdown paragraphs |
| `brand/boilerplate/terms.md` | T&Cs templates (user-provided) | Generation | Library (ingests user docs), orchestrator (setup) | One section per deal-size/type variant; never AI-drafted |
| `brand/boilerplate/bios.md` | Team bios | Generation | Library, orchestrator | One section per person |
| `library/case-studies-index.json` | Structured index of past case studies | Research, generation | Library workflow | Array of: {id, client, industry, serviceType, deliverables[], outcome, testimonial, tags[], sourceDocPath} |
| `library/pricing-history.json` | Past quotes for rate calibration | Pricing | Pricing workflow, library | Array of: {date, client, proposalType, lineItems[], total, won, clientFeedback} |
| `library/scope-templates.md` | Reusable scope/deliverable clauses | Generation, pricing | Library, generation (curates as templates emerge) | Markdown sections keyed by service type |
| `proposals/{slug}-{date}/brief.md` | Structured brief from intake | Research, pricing, generation, orchestrator | Intake workflow | Fields: clientName, clientContext, proposalType, projectDescription, budget, timeline, requirements[], constraints[], decisionMaker, sourceInputRef (audio/video/text path), assumptions[] |
| `proposals/{slug}-{date}/research-dossier.html` | Research evidence pack | Pricing, generation, orchestrator | Research workflow | Sections: client intel, tech stack, local case-study matches, web case-study/benchmarks, pricing benchmarks, competitive context |
| `proposals/{slug}-{date}/pricing.json` | Pricing breakdown | Generation, orchestrator | Pricing workflow | Fields: mode (line-item|tiered|value-based), lineItems[] or tiers[], total, calibrationNotes, sanityCheck, discountModeling |
| `proposals/{slug}-{date}/draft-v{N}.md` | Draft proposal versions | Orchestrator, generation | Generation workflow | Full markdown proposal |
| `proposals/{slug}-{date}/final-proposal.{ext}` | Exported final proposal | (read by user, not skills) | Generation workflow | PDF / DOCX / HTML per user choice |
| `proposals/{slug}-{date}/outcome.md` | Win/loss + lessons | Orchestrator, pricing (for calibration), library (for index updates) | Orchestrator (from user feedback) | Fields: status (won|lost|no-response), amount, clientFeedback, lessonsLearned[], whatWorked[], whatDidnt[] |
| `clients/{client-slug}/history.md` | Per-client history (returning clients) | Orchestrator, research, generation | Orchestrator, research | Chronological log of proposals sent to this client + outcomes |
| `daily/YYYY-MM-DD.md` | Append-only daily log | Orchestrator (orientation) | All skills append | Timestamped entries tagged `[skillname]` |

### Cross-Agent Patterns

**Handoff model: Orchestrator-routed with workflow artifact passing.**

- **Orchestrator is the router.** The user (or autonomous mode) talks to the orchestrator. Orchestrator invokes workflows in sequence: intake → research → pricing → generation. Workflows do not call each other directly; the orchestrator coordinates.
- **Artifacts are the handoff currency.** Workflows write artifacts to `proposals/{slug}-{date}/`. Downstream workflows read upstream artifacts by path. This decouples workflows — they don't need to run in the same session, and any workflow can be re-run on an old artifact.
- **Shared memory enables cross-domain awareness.** The research workflow reads the library index (built by the library workflow) and writes to `clients/{slug}/history.md`. The pricing workflow reads `pricing-history.json` (built by the library workflow + appended by past pricing runs). The generation workflow reads the research dossier and pricing breakdown. Nothing is passed verbally; everything is on disk.
- **Direct workflow invocation (power use).** A user can invoke any workflow directly without the orchestrator — e.g., "re-run pricing on the Acme brief from last week." The workflow reads the existing brief artifact, produces a new `pricing.json`. The orchestrator is not required for re-runs.
- **Library workflow runs independently.** User drops docs in `library/inbox/`, runs `paw-pa-library`. Index files update. Other workflows read the updated index on their next activation. No orchestrator involvement needed.
- **Orchestrator handles the mode toggle.** In guided mode, orchestrator pauses after each workflow completes, presents the artifact to the user, and asks for review/approval before invoking the next. In autonomous mode, orchestrator invokes workflows back-to-back without pausing, collects flagged assumptions from the intake workflow's completeness check, and surfaces them in a single "assumptions made" callout at the top of the final proposal.

## Configuration

| Variable | Prompt | Default | Result Template | User Setting |
| -------- | ------ | ------- | --------------- | ------------ |
| `assemblyai_api_key` | Your AssemblyAI API key (used for audio/video transcription). Get one at assemblyai.com | `''` (empty — prompts at runtime if missing) | `assemblyai_api_key: {value}` | yes |
| `default_mode` | Default pipeline mode: autonomous or guided? | `guided` | `default_mode: {value}` | yes |
| `default_proposal_type` | Default proposal type: pitch, rfp, or scoping? | `pitch` | `default_proposal_type: {value}` | yes |
| `default_language` | Default proposal output language? | `{communication_language}` from core config | `default_language: {value}` | yes |
| `default_pricing_mode` | Default pricing mode: line-item, tiered, or value-based? | `tiered` | `default_pricing_mode: {value}` | yes |
| `default_hourly_rate` | Your default hourly rate (USD, used for line-item estimates before pricing history exists)? | `100` | `default_hourly_rate: {value}` | yes |
| `workspace_folder` | Where should proposal run artifacts be stored? | `{project-root}/.pawbytes/proposal-automation-suites/proposals` | `workspace_folder: {value}` | yes |
| `library_inbox_folder` | Folder where you'll drop case studies / past proposals / boilerplate docs for ingestion? | `{project-root}/.pawbytes/proposal-automation-suites/library/inbox` | `library_inbox_folder: {value}` | yes |
| `web_research_enabled` | Enable deep web research for case studies and benchmarks? (requires browser-harness MCP) | `true` | `web_research_enabled: {value}` | yes |

**Runtime fallbacks:** Every skill checks config first, then asks at runtime if a value is missing. E.g., if `assemblyai_api_key` is empty, intake prompts: "Paste your AssemblyAI API key, or skip transcription and paste text instead." `default_hourly_rate` is a first-run fallback; once `pricing-history.json` has entries, pricing calibrates from history first.

## External Dependencies

| Dependency | What it is | Which skills need it | How setup handles it |
| ---------- | ---------- | -------------------- | -------------------- |
| **AssemblyAI API** | Cloud transcription (audio + video; speaker diarization, timestamps, chapter detection) | `paw-pa-intake` | Checks for `assemblyai_api_key`. If missing, warns: text briefs still work; audio/video need manual transcription or a key. Does not block install. |
| **Browser-harness MCP** | PawBytes `browser-harness` skill for live web research via user's Chrome | `paw-pa-research` (web research only) | Checks availability. If missing, warns: research falls back to local case-study matching only. Does not block install. |
| **Cursor IDE browser MCP** | Fallback web research when browser-harness unavailable | `paw-pa-research` | Runtime prefers browser-harness; falls back to `cursor-ide-browser` if configured. |
| **Pandoc** (optional) | Document converter for PDF/DOCX export | `paw-pa-generation` | Checks PATH. If missing, warns: HTML/Markdown export only. Does not block install. |
| **`paw-cra-agent-designer`** (optional, cross-module) | Creative Suite designer for serious visual production beyond bounded AI visuals | `paw-pa-generation` | Notes optional integration. Generation can hand off; otherwise skips with a note in the proposal. |

**No hard-required CLI tools.** Module degrades gracefully at each layer.

## UI and Visualization

**v1:** No dedicated dashboard skill. Pipeline artifacts (HTML research dossier, pricing JSON, draft/final proposals) are the primary visual outputs. Each run folder is self-contained and inspectable.

**Deferred (Phase 2 of build roadmap): `paw-pa-dashboard`** — optional 8th skill. Lightweight static HTML or SvelteKit dashboard showing: pipeline runs table, library stats, win/loss metrics, open clients, per-run drill-down. Fed by reading `proposals/`, `library/*.json`, `clients/`. Module works fully without it.

## Setup Extensions

Beyond config collection, `paw-pa-setup` should:

1. **Scaffold workspace folders** — create full memory tree (`brand/`, `library/inbox/`, `proposals/`, `clients/`, `daily/`) under `.pawbytes/proposal-automation-suites/`.
2. **Initialize `index.md`** — orientation file with empty/placeholder sections.
3. **Seed `brand/identity.md` template** — fill-in-the-blanks (logo path, colors, fonts, voice).
4. **Seed `brand/boilerplate/` templates** — `about-us.md`, `terms.md`, `bios.md` with guidance comments.
5. **Check AssemblyAI API key** — prompt and write to config if provided; note degradation if skipped.
6. **Check browser-harness** — warn if missing; note web-research degradation.
7. **Check pandoc** — warn if missing; note PDF/DOCX degradation.
8. **Optional first-run library ingest** — if docs already exist in `library/inbox/`, invoke library ingestion as final setup step.
9. **Print next steps** — drop case studies in inbox → run `paw-pa-library` → invoke `paw-pa-agent-orchestrator` for first proposal.

**Activation modes:** Both interactive and `--headless` / `-H` (accepts args, skips prompts, still shows summary). Never hard-block install.

## Integration

**Standalone module.** Provides independent value without `paw-upwork`, `paw-mkt`, or `paw-cra`. Seller-focused proposal automation for any vertical.

**Optional cross-module handoffs:**

- **`paw-cra-agent-designer`** — serious mockups/wireframes beyond bounded AI visuals in generation.
- **`paw-upwork-proposal`** — complementary but distinct: Upwork is job-posting-specific; `paw-pa` is general proposal automation from multimodal briefs. No hard dependency.

**Pattern alignment:** Mirrors `paw-upwork` (orchestrator + workflows + shared memory) and `paw-mkt` (workspace folders, HTML reports, setup skill).

## Creative Use Cases

- **Voice memo → proposal in 20 minutes** — client call recording dropped in; AssemblyAI transcribes; pipeline produces a pitch with matched case studies and tiered pricing.
- **RFP fast response** — paste RFP PDF into library inbox once; on new RFP brief, research pulls compliance-relevant case studies + web benchmarks; generation produces compliance matrix + structured response.
- **Returning client** — orchestrator recalls `clients/{slug}/history.md`; research emphasizes prior work; pricing calibrates from past quotes to that client.
- **Re-price an old brief** — invoke `paw-pa-pricing` directly on an existing `brief.md` with updated rates or a new tier structure.
- **Library-only refresh** — drop 10 new case studies in inbox; run `paw-pa-library`; next proposal automatically surfaces better matches.
- **Multi-language pitch** — same brief, generate French and English versions from `default_language` override at intake.
- **Autonomous batch** — seller drops 3 voice briefs; runs orchestrator in autonomous mode; reviews 3 complete proposal folders the next morning.
- **Win-rate learning** — after recording outcomes, pricing history and orchestrator guidance improve ("tiered packages at $X win more than line-item at $Y for this client type").

## Skills

<!-- Self-contained briefs for Agent Builder / Workflow Builder — zero conversation context required. -->

### paw-pa-setup

**Type:** workflow

**Core Outcome:** The module is installed, configured, workspace scaffolded, and optional dependencies checked — in a single guided pass.

**The Non-Negotiable:** Never hard-block. If AssemblyAI key, browser-harness, or pandoc are missing, configure graceful degradation and continue. Always show a confirmation summary before writing config.

**Capabilities:**

| Capability | Outcome | Inputs | Outputs |
| ---------- | ------- | ------ | ------- |
| Config collection | Module config written | Prompts/defaults or headless args | `config.yaml` + `config.user.yaml` entries |
| Workspace scaffold | Full memory tree created | Config paths | `.pawbytes/proposal-automation-suites/**` |
| Brand templates seeded | Fill-in-the-blanks brand/boilerplate files | — | `brand/identity.md`, `brand/boilerplate/*.md` |
| Dependency check | AssemblyAI, browser-harness, pandoc status known | System state | Warnings + degradation notes in summary |
| Optional library ingest | Inbox docs indexed on first run | Files in `library/inbox/` | Updated `case-studies-index.json` etc. |
| Capability registration | Help system knows the module | `module.yaml` | `module-help.csv` entries |

**Memory:** N/A (writes config + scaffolds workspace). Reads `./assets/module.yaml` for identity/variables.

**Init Responsibility:** This IS the init skill. Anti-zombie config writes. Surface degradation paths clearly.

**Activation Modes:** Both (`--headless` / `-H` accepts args, skips prompts, still shows summary).

**Tool Dependencies:** None directly. Checks for browser-harness skill, pandoc on PATH.

**Design Notes:** Mirror `paw-upwork-setup` patterns. Optional first-run library ingest is a strong onboarding moment.

**Relationships:** Run once before any other skill. May invoke `paw-pa-library` if inbox has docs.

---

### paw-pa-agent-orchestrator

**Type:** agent (orchestrator)

**Persona:** A sharp, efficient proposal strategist — part deal desk lead, part senior sales engineer. Direct and practical ("your brief is missing budget — I need that before pricing"). Warm but doesn't waste time. Makes the seller feel in control of a complex pipeline. Celebrates when evidence and pricing align.

**Core Outcome:** The seller goes from messy multimodal input to a polished, researched, priced proposal — with the right check-ins (guided) or zero friction (autonomous). Over time, the orchestrator is the single relationship that ties intake, research, pricing, generation, outcomes, and client history together.

**The Non-Negotiable:** Never let a thin brief silently become a weak proposal. In guided mode, ask clarifying questions. In autonomous mode, make explicit flagged assumptions visible at the top of the final proposal. Always route through the specialist workflows — never substitute for their heavy lifting.

**Capabilities:**

| Capability | Outcome | Inputs | Outputs |
| ---------- | ------- | ------ | ------- |
| Pipeline orchestration | Full intake → research → pricing → generation run | Multimodal brief or run resume | `proposals/{slug}-{date}/` artifact set |
| Mode toggle | Guided (check-ins) or autonomous (no pauses) per run | User preference / `default_mode` | Mode applied for session |
| Thin-brief clarification | Missing fields surfaced and resolved | Incomplete `brief.md` | Updated brief (guided) or flagged assumptions (autonomous) |
| Check-in gates | User reviews research, pricing, draft before next phase | Workflow artifacts | Approval / revision notes |
| Direct workflow routing | Invoke any workflow with context | User intent ("re-price Acme brief") | Workflow invocation + handoff |
| Outcome intake | Win/loss recorded for future calibration | User feedback | `outcome.md`, updates to `pricing-history.json` via library |
| Client history | Returning clients recognized | Client name/slug | Loads `clients/{slug}/history.md` |
| Progress tracking | Seller sees pipeline state | Workspace state | Status summary from `index.md` + run folder |

**Memory:** Reads `index.md`, `brand/`, `library/`, `proposals/`, `clients/`, `outcomes` on activation. Writes run folders, curates `index.md`, intakes outcomes, appends `clients/` history. Daily log tag: `[orchestrator]`.

**Init Responsibility:** On first run with no workspace, direct to `paw-pa-setup`. Create `proposals/{slug}-{date}/` at run start. Detect in-progress runs and offer resume.

**Activation Modes:** Interactive (primary). Autonomous mode is a per-run toggle, not headless-only.

**Tool Dependencies:** None directly — delegates to workflows.

**Design Notes:** Must NOT produce research, pricing math, or proposal copy itself — coordinates and owns run state. Mirrors `paw-upwork-agent-coach` "never produces content" constraint for specialist domains. Recommend running `paw-pa-library` if case-study index is empty before first research run.

**Relationships:** Entry point for the suite. Routes to intake → research → pricing → generation. Owns outcome feedback loop. Library runs independently.

---

### paw-pa-intake

**Type:** workflow

**Core Outcome:** A structured, completeness-checked brief artifact from any multimodal input (text, audio, video, or link).

**The Non-Negotiable:** Every brief must land as structured `brief.md` with explicit fields — never a raw transcript dump. Completeness gaps must be flagged (for guided clarification or autonomous assumption flagging).

**Capabilities:**

| Capability | Outcome | Inputs | Outputs |
| ---------- | ------- | ------ | ------- |
| Text intake | Brief from pasted/typed text | Raw text | `brief.md` |
| Audio transcription | Transcript from audio file | Audio file + AssemblyAI key | Transcript + `brief.md` |
| Video transcription | Transcript from video file or link | Video file/URL + AssemblyAI key | Transcript + `brief.md` |
| Structured extraction | Client, type, scope, budget, timeline, requirements parsed | Transcript or text | Populated `brief.md` fields |
| Proposal type detection | pitch / rfp / scoping inferred or confirmed | Brief content | `proposalType` field |
| Completeness check | Missing fields flagged | `brief.md` | `completenessReport` (gaps list) + `assumptions[]` if autonomous |
| Source preservation | Original input referenced | Input file/path | `sourceInputRef` in brief |

**Memory:** Reads config (`assemblyai_api_key`, `default_proposal_type`, `default_language`). Writes `proposals/{slug}-{date}/brief.md`. Daily log tag: `[intake]`.

**Init Responsibility:** Verify run folder exists (orchestrator creates it). Prompt for AssemblyAI key at runtime if missing and input is audio/video.

**Activation Modes:** Both. Interactive for clarification loops; headless when text brief + all fields provided.

**Tool Dependencies:** AssemblyAI API (HTTP). Optional: local file read for audio/video upload.

**Design Notes:** AssemblyAI supports speaker diarization and chapter detection — preserve timestamps in a sidecar `transcript.md` for audit. Never silently drop failed transcription — offer manual paste fallback.

**Relationships:** First workflow in pipeline. Output consumed by research, pricing, generation. Can be re-run to update brief after orchestrator clarification.

---

### paw-pa-research

**Type:** workflow

**Core Outcome:** An evidence-backed research dossier that substantiates the proposal — local proof ("we've done this") plus web proof ("here's the industry benchmark").

**The Non-Negotiable:** Findings must be grounded in real data — local index matches and web sources cited. Never invent case studies, client facts, or pricing benchmarks.

**Capabilities:**

| Capability | Outcome | Inputs | Outputs |
| ---------- | ------- | ------ | ------- |
| Local case-study matching | Ranked matches from seller's library | `brief.md` + `case-studies-index.json` | Match list with relevance scores |
| Client intelligence | Prospect context (industry, size, news, signals) | Client name/context from brief | Client intel section |
| Tech stack research | Client/prospect technology footprint | Client domain/name | Tech stack section |
| Web case-study/benchmark research | External industry examples and proof points | Brief scope + web search | Web evidence section |
| Pricing benchmarks | Market rate observations for this work type | Brief scope + web/local history | Pricing benchmark section |
| Competitive context | Differentiators vs likely alternatives | Brief + web findings | Competitive section (power-user) |
| **HTML research dossier** | Polished, auto-opening evidence pack | All findings | `research-dossier.html` (auto-opens) |
| Client history update | Returning client context appended | `clients/{slug}/history.md` | Updated client history |

**Memory:** Reads `brief.md`, `case-studies-index.json`, `clients/`, `index.md`. Writes `research-dossier.html` + optional `research-dossier.md`. Daily log tag: `[research]`.

**Init Responsibility:** Require `brief.md`. If `web_research_enabled` and browser-harness unavailable, fall back to local-only with clear notice.

**Activation Modes:** Interactive (web research supervised). Headless possible with local-only or pre-provided research notes.

**Tool Dependencies:** Browser-harness MCP (preferred) or cursor-ide-browser MCP (fallback) for web research. Local index requires no external tools.

**Design Notes:** HTML dossier is the UX centerpiece — auto-open on completion. Local matches are the differentiator; web research adds industry substantiation. Keep browsing respectful and human-paced.

**Relationships:** Runs after intake. Feeds pricing (benchmarks) and generation (case studies, intel). Updates client history.

---

### paw-pa-pricing

**Type:** workflow

**Core Outcome:** A defensible pricing breakdown — line-item, tiered, or value-based — calibrated against history and market benchmarks, with sanity check.

**The Non-Negotiable:** Pricing must be explainable. Every number ties to scope, rate, benchmark, or strategic choice — never a random round number.

**Capabilities:**

| Capability | Outcome | Inputs | Outputs |
| ---------- | ------- | ------ | ------- |
| Line-item estimate | Hours × rate breakdown | `brief.md` + scope | `pricing.json` (line-item mode) |
| Tier packaging | Good/Better/Best (or custom tiers) with anchoring | `brief.md` + research benchmarks | `pricing.json` (tiered mode) |
| Value-based pricing | Price tied to client outcome/value | `brief.md` + client intel | `pricing.json` (value-based mode) |
| Rate calibration | Rates informed by `pricing-history.json` + benchmarks | History + `default_hourly_rate` | `calibrationNotes` in pricing |
| Sanity check | Defensibility vs market (too cheap / too expensive signals) | Pricing + benchmarks | `sanityCheck` section |
| Discount modeling | Impact of discount scenarios | Base pricing + discount % | `discountModeling` section |
| History append | This quote added for future calibration | Final pricing | Entry in `pricing-history.json` |

**Memory:** Reads `brief.md`, `research-dossier.html`, `pricing-history.json`, config (`default_hourly_rate`, `default_pricing_mode`). Writes `pricing.json`. Daily log tag: `[pricing]`.

**Init Responsibility:** Require `brief.md`. Warn if research dossier missing (pricing still possible but less calibrated).

**Activation Modes:** Both. Interactive for tier/value decisions; headless for line-item from brief + defaults.

**Tool Dependencies:** None.

**Design Notes:** `default_hourly_rate` is first-run fallback; history takes precedence once populated. Sanity check should cite benchmark sources from research dossier.

**Relationships:** Runs after research (ideal) or directly on brief (power use). Feeds generation. Appends pricing history.

---

### paw-pa-generation

**Type:** workflow

**Core Outcome:** A polished, branded, export-ready proposal document — type-adaptive (pitch / RFP / scoping), with matched case studies, pricing, risk register, T&Cs, optional visuals, and multi-language support.

**The Non-Negotiable:** The proposal must read like the seller wrote it for this specific client — not a generic template. First section must hook the client's actual problem from the brief and research.

**Capabilities:**

| Capability | Outcome | Inputs | Outputs |
| ---------- | ------- | ------ | ------- |
| Type-adaptive assembly | Correct sections/tone for pitch, RFP, or scoping | `brief.md` + `proposalType` | `draft-v1.md` |
| Case study integration | Matched local + web evidence woven in | Research dossier + library index | Embedded proof in draft |
| Pricing presentation | Pricing formatted per type (tiers, line-items, milestones) | `pricing.json` | Pricing section in draft |
| Risk register | Risk → likelihood → impact → mitigation table | Brief scope + research | Risk section (RFP/scoping emphasis) |
| T&Cs inclusion | User boilerplate pulled by type/deal size | `brand/boilerplate/terms.md` | T&Cs section (never AI-drafted) |
| AI visuals (bounded) | Hero images, process diagrams, pricing charts | Brief + pricing data | Image files referenced in draft |
| Multi-language | Proposal in specified language | `default_language` or intake override | Translated `draft-v1.md` / final |
| Brand styling | Logo, colors, fonts applied | `brand/identity.md` | Styled HTML export |
| Variations | Short punchy + detailed long versions | Base draft | `draft-v1-short.md`, `draft-v1-long.md` |
| Objection pre-brief | Anticipated objections pre-empted in copy | Research + brief | Woven into draft |
| Export | PDF, DOCX, HTML, Markdown | Styled draft | `final-proposal.{pdf,docx,html,md}` |
| CRA handoff (optional) | Serious mockups delegated | Visual brief | Handoff note to `paw-cra-agent-designer` |

**Memory:** Reads `brief.md`, `research-dossier.html`, `pricing.json`, `brand/`, `library/scope-templates.md`. Writes `draft-v*.md`, `final-proposal.*`. May curate `scope-templates.md`. Daily log tag: `[generation]`.

**Init Responsibility:** Require `brief.md` and `pricing.json`. Warn if research dossier missing. Create draft v1; increment version on revision.

**Activation Modes:** Both. Interactive for revision loops; headless for first draft from complete artifacts.

**Tool Dependencies:** Pandoc (optional, PDF/DOCX). Image generation (model-native or tool). Optional: `paw-cra-agent-designer` cross-module.

**Design Notes:** T&Cs are always user-provided boilerplate — never AI-generated legal text. AI visuals bounded to hero images, simple diagrams, data charts — not mockups/wireframes. Assumptions from autonomous mode surfaced as callout at top of final proposal.

**Relationships:** Final workflow in pipeline. Consumes all upstream artifacts. Can be re-run for revisions (v2, v3) without re-running research/pricing.

---

### paw-pa-library

**Type:** workflow

**Core Outcome:** Seller's dropped docs become a searchable, structured library — case studies, pricing history, boilerplate, scope templates — that makes every future proposal faster and better.

**The Non-Negotiable:** Ingestion must extract structured, matchable fields — not just file copies. Every indexed item must be traceable to its source doc.

**Capabilities:**

| Capability | Outcome | Inputs | Outputs |
| ---------- | ------- | ------ | ------- |
| Inbox scan | New/modified docs detected | `library/inbox/` folder | Processing queue |
| Case-study extraction | Structured index entries from past proposals/case studies | PDF/DOCX/MD files | `case-studies-index.json` entries |
| Pricing history extraction | Past quote data from proposal docs | Proposal files with pricing | `pricing-history.json` entries |
| Boilerplate extraction | About-us, bios, T&Cs routed to brand folder | Recognized boilerplate docs | `brand/boilerplate/*.md` updates |
| Scope template extraction | Reusable scope/deliverable clauses | Proposal docs | `scope-templates.md` sections |
| Incremental re-index | Only new/changed docs processed | File hashes / timestamps | Updated indexes |
| Index validation | Orphaned entries, missing source files flagged | Index + inbox | Validation report (HTML candidate) |

**Memory:** Reads `library/inbox/`, existing indexes. Writes `case-studies-index.json`, `pricing-history.json`, `scope-templates.md`, `brand/boilerplate/`. Updates `index.md` (library stats). Daily log tag: `[library]`.

**Init Responsibility:** Create `library/inbox/` if missing. On first run with empty inbox, print guidance on what to drop in.

**Activation Modes:** Both. Headless for scheduled/cron re-index; interactive for first-time onboarding.

**Tool Dependencies:** None required (reads local files). Optional: pandoc for exotic doc formats.

**Design Notes:** Incremental re-index is critical — user keeps dropping docs, library keeps growing. Extraction quality is the module's moat. Validation report helps when source docs are moved/deleted.

**Relationships:** Runs independently or from setup. Feeds research (case-study index), pricing (history), generation (templates, boilerplate). Orchestrator recommends running when index is stale or empty.

## Build Roadmap

Recommended build order — each skill unlocks the next:

| Order | Skill | Rationale |
| ----- | ----- | --------- |
| 1 | `paw-pa-setup` | Foundation: config, workspace, templates. Nothing else runs without it. |
| 2 | `paw-pa-library` | Case-study index and pricing history must exist before research/pricing can shine. Build early so test data is available. |
| 3 | `paw-pa-intake` | First pipeline stage. Testable in isolation with text briefs before AssemblyAI integration. |
| 4 | `paw-pa-research` | Depends on intake output + library index. HTML dossier is a strong milestone. |
| 5 | `paw-pa-pricing` | Depends on brief + research benchmarks + pricing history. |
| 6 | `paw-pa-generation` | Depends on all upstream artifacts. Largest skill — build last among workflows. |
| 7 | `paw-pa-agent-orchestrator` | Ties everything together. Build after workflows exist so routing is real, not stubbed. |
| — | `paw-pa-dashboard` (deferred) | Optional Phase 2. Build when pipeline produces enough data to visualize. |

**After all skills built:** Return to **Create Module (CM)** to scaffold module infrastructure (`module.yaml`, help CSV, install wiring).

**Next steps:**

1. Build each skill using **Build an Agent (BA)** or **Build a Workflow (BW)** — share this plan document as context
2. When all skills are built, return to **Create Module (CM)** to scaffold the module infrastructure

## Ideas Captured

<!-- Raw ideas from brainstorming — preserved for context even if not all made it into the plan -->

### The spark (Phase 1)

- **User's words:** "Create a workflow to automate a proposal, from brief intake, the research, pricing to proposal generation etc. The brief intake will be short-form text/audio/video that we can use AssemblyAI to get the transcription."
- Core pipeline: **Intake → Transcription → Research → Pricing → Proposal Generation**.
- Brief intake accepts multimodal input: short text, audio, or video.
- AssemblyAI is the chosen transcription engine for audio/video.
- The output is a finished proposal, not just a draft outline.

### Phase 1 answers (clarifying questions)

1. **Who's the user?** Horizontal — any user. No vertical lock-in. Routing/specialization can come later based on proposal type or industry signal.
2. **What's a "proposal" here?** All of: pitch to win work (pre-sale) AND RFP/tender response AND project plan/scoping doc (post-yes). User picks the proposal type at intake; pipeline adapts.
3. **What's the "research" step doing?** User is unsure — wants my ideas. Initial read: research surfaces **case studies, the client's tech stack, and pricing benchmarks** to inform and substantiate the proposal. Research = substantiation + evidence, not just "what's the work."
4. **The "pricing" step** — both: generating a quote/estimate (hours, rates, line items, total) AND pricing strategy (tier packaging, value-based).
5. **Inspiration** — none specific. Built from the user's own experience/want.

### Phase 2 answers (round 1 — capability provocation)

1. **Case-study/portfolio library** lives in a **folder + uploaded docs** — user drops files in, module reads them. Matches the `paw-*` "workspace folder" convention (like `paw-mkt`'s `brands/*/` and `paw-upwork`'s freelancer workspace). No external source integration needed at v1.
2. **Automation mode: both (c)** — fully autonomous fast-mode AND guided check-in mode. Toggle. The user decides per-run.
3. **User role: seller only.** Module stays focused on the seller's side. No RFP-authoring for buyers.
4. **Routing dimension: by proposal type** — pitch / RFP response / scoping doc. The pipeline adapts internal sections and emphasis based on type. Type is detected from the brief or chosen at intake.
5. **Thin-brief handling: (a) ask clarifying questions back to the user.** Never refuse, never silently assume.
6. **Surprise capabilities: yes, all good** — AI-generated visuals/mockups, risk register, T&Cs auto-included, multi-language proposals all in scope.

### Tensions to resolve (Phase 3 will settle, flagging now)

- **Autonomous mode vs. "ask clarifying questions"** — autonomous mode can't pause mid-pipeline to ask the user. Likely resolution: autonomous mode makes *explicit, flagged* assumptions and notes them at the top of the proposal; guided mode asks interactively. Surface this when we hit architecture.
- **Routing by proposal type** — could mean three separate sub-flows (pitch flow, RFP flow, scoping flow) OR one adaptive flow with type-conditional sections. Defer to Phase 3.
- **AI visuals scope** — could be mood-board / wireframe mockups / hero images / data charts. Need to bound this or it becomes a rabbit hole. Will scope in Phase 5.
- **T&Cs** — almost certainly user-provided boilerplate template (legal liability), not AI-drafted terms. Will confirm.

### Phase 2 answers (round 2 — deepening)

1. **Case-study library: indexed local library (option 2).** User drops docs in a folder; one-time ingestion pass extracts structured fields (client, industry, service type, deliverables, outcome, testimonial, tags) into a searchable index. User keeps dropping new docs; module re-indexes. No template-filling by the user.
2. **+ Deep web research for case studies (new addition).** In addition to matching the seller's local library, the research step does deep web research to find external case studies / industry examples / benchmarks relevant to the brief. Local = "we've done this"; web = "here's the industry proof/benchmark."
3. **Routing: one adaptive pipeline with type-conditional sections** (not three separate flows). Proposal type is a variable selecting sections/tone/pricing style. Shared bones (problem, approach, scope, pricing, about).
4. **AI visuals scope: hero images, simple diagrams (process/architecture), data charts from pricing model.** NOT mockups/wireframes — those hand off to the Creative Suite `paw-cra-agent-designer`.
5. **Risk register:** yes — standard risk → likelihood → impact → mitigation section. Seeded from research + scope analysis. Especially useful for RFP and scoping types.
6. **T&Cs:** user-provided boilerplate template, pulled in based on proposal type / deal size. Module never drafts legal terms from scratch.
7. **Multi-language:** module generates proposals in any language specified at intake (default: communication language from config). Translation, not rewriting.
8. **Pipeline execution in autonomous mode:** no pausing, but every intermediate artifact (research dossier, pricing breakdown, draft sections) is saved as a file so the user can audit/reuse.
9. **Memory: persist anything valuable for the next proposal.** Confirmed scope: brand (logo/colors/fonts/voice/boilerplate), case-study library index, pricing history, win/loss outcomes, client history (same client returning → recall prior proposals), reusable scope/deliverable templates (extracted from past proposals). Single shared memory.
