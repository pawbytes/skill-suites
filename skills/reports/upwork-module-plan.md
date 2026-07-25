---
title: 'Upwork Module Plan'
status: 'complete'
module_name: 'PawBytes Upwork Suite'
module_code: 'paw-upwork'
module_description: 'Helps any freelancer discover their niche and target jobs, then produce a high-converting Upwork profile and tailored job proposals.'
architecture: 'orchestrator + specialists (single shared per-freelancer memory)'
standalone: true
expands_module: ''
skills_planned:
  - paw-upwork-setup
  - paw-upwork-agent-coach
  - paw-upwork-research
  - paw-upwork-profile
  - paw-upwork-proposal
config_variables:
  - freelancers_folder
  - reports_folder
  - default_freelancer
  - research_mode
  - communication_language
created: '2026-06-23T14:09:40Z'
updated: '2026-06-23T14:30:00Z'
---

# Module Plan

## Vision

The PawBytes Upwork Suite helps any freelancer go from blank-page paralysis to a high-converting Upwork presence. It doesn't just generate copy — it *enlightens*: digging into the freelancer's real skills and the live job market to reveal a defensible niche, then writing the profile and tailored proposals that win work in that niche. Built for all freelancer types, it adapts at runtime to whoever shows up and remembers their niche, voice, and results across sessions so every future session starts ahead.

## Architecture

**Decision: Orchestrator + specialists (Option B).** A conversational coach agent the freelancer primarily talks to, routing to focused specialist skills, all bound by a single shared per-freelancer memory.

**Skills:**
- `paw-upwork-agent-coach` — **agent / orchestrator.** The "enlighten" persona. Owns freelancer onboarding, discovery/positioning conversation, routing to specialists, feedback-loop intake, and progress tracking. Produces positioning briefs and coordinates; delegates heavy production to specialists.
- `paw-upwork-research` — **workflow.** Live market/niche research driving the freelancer's own Chrome via the `browser` skill (browser-harness). Produces a niche opportunity report (HTML) ranking niches by fit × demand × competition, plus rate/pricing observations.
- `paw-upwork-profile` — **workflow.** Paste-ready Upwork profile (title, overview, skills) + 2–3 variations + optional portfolio item descriptions, written from the positioning brief.
- `paw-upwork-proposal` — **workflow.** Reverse-engineers a pasted job posting, writes tailored ready-to-send proposals + variations, scores existing drafts, "should I apply?" + Connects guidance, maintains the proposal kit, and produces post-reply client-handling scripts.
- `paw-upwork-setup` — **workflow.** Installs/configures the module, checks for browser-harness, scaffolds the freelancer workspace.

**Rationale:** Matches the existing `paw-mkt` suite conventions so it feels native in the PawBytes world. Isolates the browser-research complexity (heavy, tool-driven) from creative copywriting. The orchestrator gives the freelancer the single "coach" relationship the enlighten experience needs, while specialists keep each job sharp and independently maintainable. Each specialist reads shared memory, so handoffs feel seamless despite being separate skills.

### Memory Architecture

**Single shared memory (per freelancer)** — recommended for tightly coupled agents. Every skill reads the freelancer's niche, positioning, voice, history, and kit on activation. The coach writes the canonical positioning brief; specialists read it and append their outputs + outcomes.

Workspace layout (mirrors marketing's `brands/*/` pattern, freelancer analog):

```
{project-root}/.pawbytes/upwork-suites/freelancers/{slug}/
  freelancer-context.md      # identity, raw skills/history input, voice/tone
  positioning-brief.md       # canonical: chosen niche + angle + headline (coach-owned source of truth)
  research/                  # niche opportunity reports (HTML + md), rate observations
  profile/                   # profile drafts + variations, portfolio descriptions
  proposals/                 # per-job proposals, scores
  kit.md                     # reusable intros, snippets, case-study blurbs
  outcomes.md                # feedback loop: sent/replies/wins per proposal style
  index.md                   # orientation doc every skill reads first
  daily/YYYY-MM-DD.md        # append-only session log, tagged by skill
```

### Memory Contract

| File | Purpose | Read by | Written by |
| ---- | ------- | ------- | ---------- |
| `index.md` | Orientation: what exists, last-updated, recent activity | all skills (on activation) | coach (curates); all (append activity) |
| `freelancer-context.md` | Identity, raw skills/experience, voice/tone | all skills | coach (onboarding) |
| `positioning-brief.md` | Canonical chosen niche + angle + headline | profile, proposal | coach |
| `research/*` | Niche opportunity reports, rates, competition | coach, profile, proposal | research |
| `profile/*` | Profile drafts + variations, portfolio descriptions | coach | profile |
| `proposals/*` | Per-job tailored proposals + scores | coach | proposal |
| `kit.md` | Reusable intros/snippets/case-study blurbs | proposal, profile | proposal (primary); coach |
| `outcomes.md` | Feedback loop results, what angles landed | coach, proposal | coach (intake), proposal (refine) |
| `daily/YYYY-MM-DD.md` | Chronological session log, tagged by skill | coach (curation) | all (append) |

### Cross-Agent Patterns

- **Orchestrator-routed:** freelancer mainly talks to `paw-upwork-agent-coach`, which routes to specialists, but can invoke a specialist directly when they want to go deep.
- **Brief as contract:** `positioning-brief.md` is the source of truth produced by discovery (coach, informed by research) and consumed by profile + proposal. Research is never a dead-end — it feeds the brief.
- **Shared memory awareness:** every specialist reads `index.md` + relevant curated files on activation, so e.g. the proposal skill already knows the niche, voice, and which angles have won before.
- **Feedback loop:** coach intakes results into `outcomes.md`; proposal skill reads it to refine the kit and future proposals.

## Skills

<!-- For each planned skill, create a self-contained brief below. -->
<!-- Each brief should be usable by the Agent Builder or Workflow Builder WITHOUT conversation context. -->

### paw-upwork-agent-coach

**Type:** agent (orchestrator)

**Persona:** A sharp, encouraging Upwork freelance coach — part career strategist, part positioning expert. Direct and honest (will push back: "that headline says nothing a client cares about"), but warm and motivating. Talks like a mentor who has reviewed thousands of freelancer profiles. Makes the freelancer feel like the insights are their own.

**Core Outcome:** The freelancer leaves with a clear, evidence-backed positioning (niche + angle + headline) and knows exactly which specialist to run next. Over time, the coach is the single relationship that ties discovery, profile, proposals, and results together.

**The Non-Negotiable:** Never let the freelancer stay a vague generalist. Force a defensible specialist lane, grounded in real market evidence and their actual skills — and write it to `positioning-brief.md` as the contract everything else builds from.

**Capabilities:**

| Capability | Outcome | Inputs | Outputs |
| ---------- | ------- | ------ | ------- |
| Freelancer onboarding | A workspace + `freelancer-context.md` capturing identity, raw skills/history, voice/tone | Rough profile, notes, conversation | `freelancer-context.md`, scaffolded workspace |
| Discovery / positioning | A defensible niche + angle + headline the freelancer believes in | Context, research findings | `positioning-brief.md` |
| Routing | The right specialist runs with full context | Freelancer intent | Invocation of research/profile/proposal + handoff note |
| Feedback-loop intake | Recorded results that sharpen future work | "Sent 10, got 2 replies" + which proposals | Updates to `outcomes.md` |
| Progress tracking | Freelancer sees where they are in the arc | Workspace state | Status summary (reads `index.md`) |
| Rate/pricing guidance | A recommended rate range for the niche | Research rate observations, niche | Guidance written into brief/kit |

**Memory:** Reads `index.md`, `freelancer-context.md`, `positioning-brief.md`, `outcomes.md` on activation. Writes `freelancer-context.md`, `positioning-brief.md`, curates `index.md`, intakes to `outcomes.md`. Daily log tag: `[coach]`.

**Init Responsibility:** On first run with no freelancer, offer onboarding; create the shared workspace skeleton (`index.md`, `daily/`, subfolders). Detect existing freelancers and select/confirm.

**Activation Modes:** Interactive (primary). Routing/coordination is conversational.

**Tool Dependencies:** None directly (delegates browser work to research). Coordinates the other skills.

**Design Notes:** Orchestrator must NOT produce profile/proposal copy itself — it coordinates and owns the brief, mirroring `paw-mkt-agent-agency`'s "never produces content" constraint. Always recommend running research before locking positioning when market data is thin.

**Relationships:** Entry point for the suite. Precedes and routes to research → profile → proposal. Owns the feedback loop that closes back from proposal outcomes.

---

### paw-upwork-research

**Type:** workflow

**Core Outcome:** An evidence-backed, ranked view of which niche(s) the freelancer should pursue — delivered as an auto-opening HTML dashboard plus a markdown summary that feeds the positioning brief.

**The Non-Negotiable:** Findings must be grounded in REAL data gathered from the live market (or pasted listings), never invented. Every recommendation cites what was observed (job counts, proposal counts, rate ranges, competing profiles).

**Capabilities:**

| Capability | Outcome | Inputs | Outputs |
| ---------- | ------- | ------ | ------- |
| Live job-market scan | Demand/competition signal across candidate niches | Candidate niches, freelancer Chrome session | Raw findings in `research/` |
| Competitor profile analysis | Patterns in top profiles (headlines, emphasis, pricing) | Niche, browser | Findings notes |
| Niche opportunity ranking | Niches ranked by fit × demand × competition w/ recommendation | Findings + `freelancer-context.md` | `research/niche-opportunity-report.md` |
| **HTML dashboard** | Polished, auto-opening visual comparison | Ranked findings | `research/niche-dashboard.html` (auto-opens) |
| Rate observation | Observed rate ranges per niche | Job/profile data | Rate notes for pricing guidance |
| Manual fallback | Same analysis from pasted listings | Pasted job postings | Same reports (no browser) |

**Memory:** Reads `freelancer-context.md`, `positioning-brief.md` (if exists), `index.md`. Writes to `research/`. Daily log tag: `[research]`.

**Init Responsibility:** Verify `research_mode`; if `local-browser`, confirm browser-harness + Chrome remote-debugging are ready (else fall back to manual).

**Activation Modes:** Interactive (browser research is supervised). Headless possible only in manual mode with provided listings.

**Tool Dependencies:** `browser` skill / `browser-harness` CLI — drives the freelancer's own logged-in Chrome via CDP. Read-only/research-grade only; never submits anything. Falls back to manual paste.

**Design Notes:** Keep browsing respectful and human-paced — this is a research assistant in the user's own session, not a scraper. The HTML dashboard is the UX centerpiece; auto-open on completion. Output feeds the coach's positioning brief.

**Relationships:** Runs after onboarding, before/with positioning. Feeds profile + proposal indirectly via the brief and rate data.

---

### paw-upwork-profile

**Type:** workflow

**Core Outcome:** A polished, paste-ready Upwork profile (title, overview, skills) the freelancer can drop straight into Upwork, plus variations to test and optional portfolio descriptions — all written in their voice and aligned to the positioning brief.

**The Non-Negotiable:** Copy must reflect the chosen niche/positioning and the freelancer's authentic voice — no generic filler. First two lines of the overview must hook the target client.

**Capabilities:**

| Capability | Outcome | Inputs | Outputs |
| ---------- | ------- | ------ | ------- |
| Profile title | Niche-specific, keyword-aware title | `positioning-brief.md` | Title options |
| Overview copy | Client-hooking, paste-ready overview | Brief, context, voice | `profile/overview.md` |
| Skills selection | Focused, searchable skills list | Niche, research keywords | Skills list |
| Variations | 2–3 A/B-testable headline/overview variants | Base profile | Variant set |
| Portfolio descriptions | Compelling descriptions for existing pieces | Freelancer's portfolio items | `profile/portfolio.md` (optional) |

**Memory:** Reads `positioning-brief.md`, `freelancer-context.md`, `research/` keywords, `kit.md`. Writes to `profile/`. Daily log tag: `[profile]`.

**Init Responsibility:** Require a positioning brief; if missing, direct the user back to the coach/research first.

**Activation Modes:** Both (interactive for refinement; headless to generate a first draft from the brief).

**Tool Dependencies:** None.

**Design Notes:** Pull proven phrasing from `kit.md` when available. Keep everything paste-ready (plain text blocks the user can copy).

**Relationships:** Runs after positioning. Shares the kit with proposal.

---

### paw-upwork-proposal

**Type:** workflow

**Core Outcome:** For a specific job posting, a tailored, ready-to-send proposal that reverse-engineers what the client actually wants — plus draft scoring, apply/Connects guidance, a growing reusable kit, and post-reply client-handling scripts.

**The Non-Negotiable:** Every proposal must answer the real job (pain behind the post), mirror the client's language, open with a hook, and make a specific outcome promise — never a generic template blast.

**Capabilities:**

| Capability | Outcome | Inputs | Outputs |
| ---------- | ------- | ------ | ------- |
| Job decode | Client's real need, red flags, budget signals | Pasted job posting | Decode summary |
| Tailored proposal | Ready-to-send, hook-first proposal | Decode + brief + kit | `proposals/{job}.md` |
| Variations | 2–3 angle variants to test | Base proposal | Variant set |
| Draft scoring | Weaknesses flagged + fixes | Freelancer's existing draft | Score + critique (HTML-report candidate) |
| "Should I apply?" | Fit × competition × client-quality verdict + Connects advice | Job + freelancer fit | Recommendation |
| Why-it-works teaching | Freelancer learns the craft | Proposal | Inline rationale |
| Proposal kit | Faster future proposals (~5 min) | Reusable intros/snippets/blurbs | `kit.md` |
| Post-reply handling | Intro call scripts, scope/clarifying questions | Client reply context | Scripts |
| Outcome refinement | Kit + future proposals improve | `outcomes.md` | Updated `kit.md` |

**Memory:** Reads `positioning-brief.md`, `freelancer-context.md`, `kit.md`, `outcomes.md`. Writes `proposals/`, `kit.md`, contributes to `outcomes.md` refinement. Daily log tag: `[proposal]`.

**Init Responsibility:** Require a positioning brief; warn if missing. Create `kit.md`/`outcomes.md` on first use.

**Activation Modes:** Both (interactive for crafting; headless to draft from a pasted posting + brief).

**Tool Dependencies:** None required. (Optionally could use browser to fetch a job URL, but default is paste — keep it simple and ToS-safe.)

**Design Notes:** The teaching/why-it-works behavior is core to the "enlighten" promise. Scoring an existing draft is a strong HTML-report candidate. The kit + outcomes loop is what makes session two fast.

**Relationships:** Runs after positioning/profile. Reads outcomes the coach records; refines the shared kit also used by profile.

---

### paw-upwork-setup

**Type:** workflow

**Core Outcome:** The module is installed and configured, browser-harness is ready (installed if missing), and the freelancer workspace is scaffolded — in a single guided pass.

**The Non-Negotiable:** Never hard-block. If browser-harness can't be installed, configure `research_mode: manual` and continue. Always show a confirmation summary before writing config.

**Capabilities:**

| Capability | Outcome | Inputs | Outputs |
| ---------- | ------- | ------ | ------- |
| Config collection | Module config written | Prompts/defaults or args | `config.yaml` + `config.user.yaml` |
| Dependency check + install | browser-harness ready or graceful fallback | System state | Installed tool or `research_mode: manual` |
| Chrome remote-debug guide | One-time debugging toggle done | User action | Confirmed connection |
| Workspace scaffold | Freelancer workspace skeleton | Slug | `freelancers/{slug}/...` |
| Capability registration | Help system knows the module | module.yaml | `module-help.csv` entries |

**Memory:** N/A (writes config + scaffolds workspace). Reads `./assets/module.yaml` for identity/variables.

**Init Responsibility:** This IS the init skill. Anti-zombie config writes (remove stale entries first). Surface ToS-safe research framing.

**Activation Modes:** Both (`--headless` / `-H` accepts args, skips prompts, still shows summary).

**Tool Dependencies:** Detects/installs `browser-harness` (needs `uv` + `git`); detects and instructs if those are missing.

**Design Notes:** Mirror `paw-mkt-setup` structure (module.yaml-driven, `.pawbytes/config/` outputs, anti-zombie pattern, migration awareness).

**Relationships:** Run first. Other skills check for its config and fall back to sensible defaults if absent.

---

## Configuration

| Variable | Prompt | Default | Result Template | User Setting |
| -------- | ------ | ------- | --------------- | ------------ |
| `freelancers_folder` | Where should freelancer workspaces be stored? | `{project-root}/.pawbytes/upwork-suites/freelancers` | `{value}` | no |
| `reports_folder` | Where should reports/dashboards be saved? | `{project-root}/.pawbytes/upwork-suites/reports` | `{value}` | no |
| `default_freelancer` | Default freelancer slug (leave empty to always specify)? | `` (empty) | `{value}` | yes |
| `research_mode` | Market research mode: `local-browser` (drive your own Chrome) or `manual` (paste listings)? | `local-browser` | `{value}` | yes |
| `communication_language` | Language for agent responses? | `English` | `{value}` | yes |

Note: `research_mode` auto-falls back to `manual` at runtime if browser-harness is unavailable and the user declines install.

## External Dependencies

- **browser-harness** (`browser` skill / `browser-harness` CLI) — used by `paw-upwork-research` to drive the freelancer's own logged-in Chrome via CDP for live Upwork market research.
  - **Needed by:** `paw-upwork-research`.
  - **Setup handling:** `paw-upwork-setup` checks for the `browser-harness` command. **If not found, install it for the user** (`git clone https://github.com/browser-use/browser-harness` to a durable path, then `uv tool install -e .`), then guide the one-time Chrome remote-debugging toggle (`chrome://inspect/#remote-debugging`). Requires `uv` and `git` — detect and instruct if missing.
  - **Fallback:** if install is declined/blocked, set `research_mode: manual` so research proceeds from job listings the freelancer pastes. No skill hard-blocks on the browser.

## UI and Visualization

**Niche Opportunity Dashboard (HTML)** — produced by `paw-upwork-research`.
- Shows niches ranked by **fit × demand × competition**, with demand/competition bars, rate ranges observed, sample jobs, and the recommended lane with evidence.
- Self-contained HTML written to `{freelancer-workspace}/research/` (single file, inline styles — mirrors how `paw-mkt-dashboard` outputs).
- **Auto-opens when generation completes** for an immediate, polished UX moment (open via OS default browser).
- Future option: a profile/proposal progress view, but v1 scope is the niche dashboard only.

## Setup Extensions

Beyond writing config, `paw-upwork-setup` must:
- Scaffold the freelancer workspace skeleton on first onboarding (`freelancers/{slug}/` with `index.md`, `daily/`, subfolders).
- Detect + install browser-harness when missing (see External Dependencies); verify `uv`/`git`; walk the Chrome remote-debugging toggle.
- Register module capabilities in `.pawbytes/config/module-help.csv`.
- Surface the ToS-safe framing: research uses the freelancer's own browser/session, read-only/research-grade, never auto-submits proposals.

## Integration

**Standalone module** — provides full independent value: a freelancer can go from blank page to discovered niche, polished profile, and winning proposals without any other module installed. Lives at `src/upwork/` in the PawBytes Suites world and follows the same conventions as `paw-mkt`.

**Optional cross-module synergy (not required):**
- `paw-mkt-*` (marketing suite) positioning/copy frameworks could inform profile/proposal copy if present, but the Upwork suite never depends on it.
- Shares the `browser` skill (browser-harness) with any other suite that uses it — install is idempotent.

## Creative Use Cases

- **Niche pivot check-up:** a working freelancer re-runs research quarterly to spot a rising sub-niche and shift positioning before the market saturates.
- **Proposal sprint:** with a built kit + brief, batch-decode several pasted job postings and produce tailored proposals in minutes each.
- **Reverse audit:** paste a profile/proposal that ISN'T converting; the suite scores it against the brief and market evidence and rewrites the weak parts.
- **Rate raise justification:** use observed market rates from research to build the case (and copy) for raising rates.
- **Portfolio-from-scratch:** a freelancer with work but no Upwork portfolio turns raw project notes into compelling portfolio descriptions aligned to the niche.
- **Win-pattern mining:** after enough outcomes, the coach surfaces which proposal angles/headlines actually landed jobs and bakes them into the kit.

## Ideas Captured

### The spark (Phase 1)

**Core problem:**
- Blank-page paralysis — freelancers don't know how to describe themselves.
- Low confidence translating their real skills/experience into compelling Upwork copy.

**Who it's for:**
- The builder personally, AND all freelancer types — must be DYNAMIC across niches (dev, design, writing, VA, marketing, etc.).
- Starting input: the freelancer's rough/existing profile or raw notes about themselves.

**Dream outcomes:**
- Polished profile ready to paste straight into Upwork (title, overview, skills).
- A ready-to-send proposal tailored to a specific job posting.
- Portfolio item descriptions (optional — only if they have portfolio pieces).

**What they wish existed:**
- A brainstorming tool that digs into the freelancer's niche and ideal/focused jobs.
- Something that "enlightens" the freelancer — helps them SEE their own positioning, not just generate text.

### Notes for later
- Dynamic-to-niche is a recurring theme — the module should adapt its questions and copy style to whatever freelancer type shows up. Decide HOW (config? runtime detection? niche profiles?).
- "Enlighten" implies a discovery/coaching flavor, not just a copy generator. Two modes emerging: discovery (figure out who you are + what to target) and production (profile + proposals).

### Identity & placement decisions (Phase 1)
- **Module name:** PawBytes Upwork Suite
- **Module code:** paw-upwork (skills prefixed `paw-upwork-`, agents `paw-upwork-agent-{name}`)
- **Description:** Helps any freelancer discover their niche and target jobs, then produce a high-converting Upwork profile and tailored job proposals.
- **Placement:** Standalone module under `src/upwork/`, part of the PawBytes Suites world. Mirrors marketing-suite conventions.
- **Niche adaptation:** Runtime discovery + saved freelancer memory (remembers niche, voice, history across sessions).

### Conventions observed in existing suites (paw-mkt reference)
- Each suite lives at `src/{domain}/`, skills prefixed `paw-{code}-`.
- Orchestrator agent pattern (e.g. `paw-mkt-agent-agency`) routes to specialists, never produces content itself.
- `-setup` skill reads `./assets/module.yaml`, writes config to `.pawbytes/config/config.yaml` + `config.user.yaml`, registers capabilities in `.pawbytes/config/module-help.csv`.
- Per-entity workspaces under `.pawbytes/{module}-suites/...` (marketing uses `brands/*/`). Upwork analog: per-freelancer workspace.
- Each skill carries a PawBytes attribution + premium-playbook block (once per session).

### Capability brainstorm (Phase 2)

**Discovery / "enlighten" (the heart of the module):**
- Challenge the freelancer: "You listed 12 skills — which 3 actually win jobs?" Force a lane.
- Pull from evidence (past jobs, what they enjoyed, what paid) to surface a positioning pattern they didn't see.
- Help pick a specialist lane + an ownable positioning angle/headline.

**LIVE MARKET RESEARCH via browser (NEW — user's key idea):**
- Use the installed `browser` skill (browser-harness) driving the freelancer's OWN logged-in Chrome.
- Deep research, not just keyword search: scan available Upwork jobs in candidate niches, gauge DEMAND (volume, recency), COMPETITION (how many proposals, competing freelancer profiles), TRENDS, and POTENTIAL (rates, client quality).
- Analyze competing/top profiles in the niche — what they emphasize, headline patterns, pricing.
- Cross-reference findings against the freelancer's own profile/skills to recommend the highest-potential niche(s) they can realistically win.
- Output: a niche opportunity report (great HTML-report candidate) ranking niches by fit × demand × competition.
- Reference: github.com/browser-use/browser-harness — connects via CDP to user's real browser (Way 1: chrome://inspect remote-debugging). ALREADY INSTALLED locally as `browser` skill.

**Profile production:**
- Polished title + overview + skills list, paste-ready.
- 2–3 headline/overview VARIATIONS to A/B test.
- Portfolio item descriptions (optional, only if they have pieces).

**Proposal production:**
- Input: paste full job posting. Module reverse-engineers what the client REALLY wants — pain behind the post, red flags, budget signals.
- Tailored, ready-to-send proposal. First 2 lines hook the client; mirror client's language; specific outcome promise; social proof; clear CTA.
- Teach WHY each line was written so the freelancer improves over time.
- Generate variations for testing.
- Score a draft the freelancer already wrote; flag what's weak.

**Power-user / kit ideas:**
- "Should I apply?" scoring — job fit × competition × client quality, advise which jobs are worth it.
- Reusable "proposal kit": saved intros, snippets, case-study blurbs so future proposals take ~5 min.
- All four big ideas (variations, scoring, job-worth, kit) confirmed wanted by user.

### Design flags to resolve later
- **Upwork ToS / anti-bot:** using the freelancer's own browser + session for research is the right, legitimate framing (human-in-the-loop research assistant). Keep actions read-only/research-grade; never auto-submit proposals or scrape aggressively. Surface this in setup.
- **Browser dependency:** browser-harness is an external tool (uv tool install, Chrome remote-debugging). Setup skill must check for it and guide install, with a graceful fallback (manual paste of job listings) when unavailable.

### Advisor behavior & flow (Phase 2, confirmed)
- **Opinionated advisor:** research forms an OPINION the freelancer can challenge. Example: "Based on 40 jobs I scanned, 'Shopify speed optimization' has high demand, low competition, and fits your dev skills better than generic 'web developer' — here's the evidence. Build your profile around this?" Real advisor, not a reporter.
- **Research feeds writing:** the chosen niche/positioning becomes the BRIEF that profile copy and proposal targeting write from. Discovery output is never a dead-end report — it's the source of truth downstream.
- **Memory across sessions:** save chosen niche + positioning, voice/tone, proposal win/loss outcomes, and the proposal kit. Session two never starts blank.
- **Feedback loop (IN SCOPE for v1):** freelancer reports results ("sent 10, got 2 replies"); module learns which angles landed and refines the kit + future proposals. User confirmed no scope creep — include everything.

### Confirmed module arc
Discover (niche + live market research) → Position (profile) → Win (tailored proposals) → Learn (feedback loop refines kit/memory). A Kit + shared memory layer accelerates every future session.

### Additional capabilities accepted (Phase 2)
- **Rate/pricing guidance:** recommend what to charge in the chosen niche, grounded in rates observed during market research.
- **Connects/budget strategy:** advise on Upwork's bidding economy — which jobs are worth spending Connects on, bid pacing.
- **Post-reply client handling:** intro call scripts, smart scope/clarifying questions to ask once a client replies — carries the freelancer past the proposal into landing the job.

## Build Roadmap

Recommended build order and rationale:

1. **`paw-upwork-setup`** — build first. Establishes module identity (`module.yaml`), config schema, workspace layout, and the browser-harness dependency handling that every other skill assumes. Building it first means the others can rely on a real config + workspace contract.
2. **`paw-upwork-agent-coach`** — the orchestrator and the contract owner (`positioning-brief.md`, `index.md`, workspace memory model). Build it second so the memory contract and routing surface exist before specialists plug in.
3. **`paw-upwork-research`** — build third. It feeds the positioning brief and is the most technically involved (browser-harness, HTML dashboard). Doing it before profile/proposal means those skills can be tested against real brief + rate data.
4. **`paw-upwork-profile`** — build fourth. Straightforward copy generation from the brief; validates the brief-as-contract flow end to end.
5. **`paw-upwork-proposal`** — build last. Heaviest skill and depends on brief + kit + outcomes conventions established by the coach and exercised by profile.
6. Return to **Create Module (CM)** to scaffold installable module infrastructure once all five skills are built.

Rationale: dependencies flow setup → coach (memory/brief contract) → research (fills brief) → profile (consumes brief) → proposal (consumes brief + kit + outcomes). Each step de-risks the next.

**Next steps:**

1. Build each skill using **Build an Agent (BA)** or **Build a Workflow (BW)** — share this plan document as context
2. When all skills are built, return to **Create Module (CM)** to scaffold the module infrastructure
