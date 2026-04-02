# SOSTAC Workflow

This reference defines the deterministic 6-phase SOSTAC pipeline, inner-loop step protocol, HITL gate requirements, cross-phase dependency rules, resumption logic, quality gates, and edit mode. It is the operating manual for executing a SOSTAC marketing plan from start to finish.

---

## Workflow Overview

SOSTAC is a **strictly sequential** 6-phase pipeline. Each phase builds on the outputs of all preceding phases. No phase may be started until the previous phase has received explicit user approval through its HITL gate.

```
Auto-Discovery
      |
      v
[Phase 1] Situation  --HITL-->  [Phase 2] Objectives  --HITL-->  [Phase 3] Strategy
                                                                        |
                                                                   HITL gate
                                                                        |
[Phase 6] Control  <--HITL--  [Phase 5] Action  <--HITL--  [Phase 4] Tactics
      |
      v
Final Plan Review (Quality Scorecard)
      |
      v
User Sign-Off
```

**Key invariant:** Every phase follows the same 5-step inner loop. Every phase ends with a mandatory HITL gate. No exceptions.

---

## Phase Sequence

### Pre-Phase: Auto-Discovery

| Property | Value |
|----------|-------|
| **Output** | `00-auto-discovery.md` |
| **Purpose** | Automated web research to ground all subsequent phases in evidence |
| **Entry Conditions** | Brand identified; brand slug established |
| **Exit Conditions** | Research findings saved; user has reviewed key findings |

Auto-Discovery runs before Phase 1 to gather competitor intelligence, market data, product positioning, customer language, and digital presence data. This is the evidence base that feeds every phase.

**Reference:** Load `./references/capability-auto-discovery.md`

---

### Phase 1: Situation Analysis

| Property | Value |
|----------|-------|
| **Output** | `01-situation.md` |
| **Phase Question** | "Where are we now?" |
| **Entry Conditions** | Auto-Discovery complete; `00-auto-discovery.md` exists |
| **Exit Conditions** | User approves via HITL gate |
| **Capability Reference** | `./references/capability-situation.md` |

#### Frameworks Applied

SWOT + TOWS, PESTLE, Porter's Five Forces, TAM/SAM/SOM, Jobs-to-be-Done, 5S Digital Baseline.

#### 5-Step Inner Loop

| Step | Action | Details |
|------|--------|---------|
| 1. Research | Consume auto-discovery data; conduct supplemental research | Draft SWOT from evidence, run PESTLE scan, assess Porter's forces, estimate TAM/SAM/SOM, build JTBD profile, score 5S baseline |
| 2. Analyze & Recommend | Generate TOWS strategic options; identify 5-8 key findings | Cross strengths with opportunities/threats; produce 2-3 concrete strategic directions with reasoning |
| 3. Present Findings | Share complete Situation Analysis draft | Executive summary, each framework section with evidence, strategic implications section, highlighted areas needing confirmation |
| 4. Validate & Refine | Ask 2-4 targeted questions to fill genuine gaps | Internal metrics (actual CVR, revenue), strategic intent (upcoming changes), corrections to estimates |
| 5. Save & Advance | Write `01-situation.md`; update `README.md`; present HITL gate | Show draft before saving; confirm with user; save only after confirmation |

#### HITL Gate Prompt

```
## Phase 1 Complete: Situation Analysis

**Saved to:** `./.pawbytes/marketing-suites/brands/{brand-slug}/sostac/01-situation.md`

### Key Decisions Made
- [Key finding 1 with evidence source]
- [Key finding 2 with evidence source]

### Cross-Phase Consistency Check
- Establishes: SWOT evidence base, TOWS strategic options, 5S baseline gaps
- Feeds into: Objectives (TOWS options drive goal-setting), Strategy (competitive landscape shapes positioning)

---

**Review Options:**
1. Approve & Continue -- Move to Objectives phase
2. Request Changes -- Tell me what to adjust
3. Deep Dive -- Walk through specific sections in detail

**What would you like to do?**
```

---

### Phase 2: Objectives Setting

| Property | Value |
|----------|-------|
| **Output** | `02-objectives.md` |
| **Phase Question** | "Where do we want to be?" |
| **Entry Conditions** | Phase 1 approved; `01-situation.md` exists and is user-approved |
| **Exit Conditions** | User approves via HITL gate |
| **Capability Reference** | `./references/capability-objectives.md` |

#### Frameworks Applied

OKR Framework, RACE Framework, 5S Objectives, Objective Cascade Method.

#### 5-Step Inner Loop

| Step | Action | Details |
|------|--------|---------|
| 1. Research | Re-read Situation findings; gather industry benchmarks | Identify biggest gaps and opportunities from TOWS analysis; research benchmark data for target-setting |
| 2. Analyze & Recommend | Draft OKRs with benchmarked targets; map to RACE; build objective cascade | Primary OKR + 1-2 secondary OKRs; every KR has baseline, target, deadline, and benchmark comparison |
| 3. Present Findings | Share recommended OKRs with full reasoning | Benchmark validation table, RACE coverage map, risks to achievement, key decision points |
| 4. Validate & Refine | Confirm business goals, resource constraints, ambition level | Let user adjust specific KRs; confirm revenue targets and growth expectations |
| 5. Save & Advance | Write `02-objectives.md`; update `README.md`; present HITL gate | Apply SMARTA validation to every objective before saving |

#### Mandatory Cross-Phase Dependencies

- Objectives MUST reference Situation TOWS strategic options -- each objective should trace to a specific TOWS finding.
- Objectives MUST address 5S baseline gaps identified in Situation.
- Targets MUST be benchmarked against industry data, not set arbitrarily.

#### HITL Gate Prompt

```
## Phase 2 Complete: Objectives Setting

**Saved to:** `./.pawbytes/marketing-suites/brands/{brand-slug}/sostac/02-objectives.md`

### Key Decisions Made
- [Primary OKR with rationale]
- [Target ambition level chosen]

### Cross-Phase Consistency Check
- Aligns with: Situation TOWS options [specific reference], 5S gaps [specific reference]
- Supports: Strategy (segments must be reachable to hit these targets), Control (every KR needs measurement)

---

**Review Options:**
1. Approve & Continue -- Move to Strategy phase
2. Request Changes -- Tell me what to adjust
3. Deep Dive -- Walk through specific sections in detail

**What would you like to do?**
```

---

### Phase 3: Strategy Development

| Property | Value |
|----------|-------|
| **Output** | `03-strategy.md` |
| **Phase Question** | "How do we get there?" |
| **Entry Conditions** | Phase 2 approved; `01-situation.md` and `02-objectives.md` exist and are approved |
| **Exit Conditions** | User approves via HITL gate |
| **Capability Reference** | `./references/capability-strategy.md` |

#### Frameworks Applied

STP (Segmentation, Targeting, Positioning), Moore's Positioning Statement, Ansoff Matrix, Porter's Generic Strategies, Blue Ocean Strategy, Value Proposition Canvas, Online Value Proposition (OVP), Customer Journey Mapping.

#### 5-Step Inner Loop

| Step | Action | Details |
|------|--------|---------|
| 1. Research | Re-read Situation + Objectives; research customer segments and competitive positioning | Analyze customer data from reviews, forums, competitor positioning for segmentation |
| 2. Analyze & Recommend | Propose segments, build positioning map, draft positioning statements, map customer journey | Score segments on attractiveness; identify competitive white space; recommend Ansoff growth direction |
| 3. Present Findings | Share strategic recommendation with options and trade-offs | Target segments with scoring, 2-3 positioning statement options, journey map with drop-off risks, strategic phasing |
| 4. Validate & Refine | Confirm segment prioritization, choose positioning, validate journey map | 1-2 key strategic decisions (e.g., "premium vs accessible positioning") |
| 5. Save & Advance | Write `03-strategy.md`; update `README.md`; present HITL gate | Verify strategy-tactic boundary: strategy answers WHO/HOW/WHERE, not WHAT/WHEN/HOW MUCH |

#### Mandatory Cross-Phase Dependencies

- Strategy segments MUST be reachable with the resources identified in Situation.
- Strategy MUST connect to Situation TOWS options -- positioning should exploit identified opportunities and defend against threats.
- Strategy MUST show how the Objectives OKRs will be achieved at the strategic level.

#### HITL Gate Prompt

```
## Phase 3 Complete: Strategy Development

**Saved to:** `./.pawbytes/marketing-suites/brands/{brand-slug}/sostac/03-strategy.md`

### Key Decisions Made
- [Target segment chosen with rationale]
- [Positioning statement selected]
- [Ansoff growth direction]

### Cross-Phase Consistency Check
- Aligns with: Situation TOWS [specific options addressed], Objectives OKRs [specific KRs this strategy serves]
- Supports: Tactics (channel selection must reach target segments), Action (resource plan must support strategy)

---

**Review Options:**
1. Approve & Continue -- Move to Tactics phase
2. Request Changes -- Tell me what to adjust
3. Deep Dive -- Walk through specific sections in detail

**What would you like to do?**
```

---

### Phase 4: Tactics Planning

| Property | Value |
|----------|-------|
| **Output** | `04-tactics.md` |
| **Phase Question** | "Details of strategy" |
| **Entry Conditions** | Phase 3 approved; all prior phase documents exist and are approved |
| **Exit Conditions** | User approves via HITL gate |
| **Capability Reference** | `./references/capability-tactics.md` |

#### Frameworks Applied

AARRR Pirate Metrics, ICE Scoring, PIE Framework, Hub-Hero-Help Content Model, Pillar-Cluster SEO, TOFU/MOFU/BOFU, 7P Marketing Mix, 70/20/10 Budget Rule. **Always** read `./references/frameworks/situational-router.md` for 3-layer routing logic and all 9 playbooks.

#### 5-Step Inner Loop

| Step | Action | Details |
|------|--------|---------|
| 1. Research | Re-read Phase 1-3 data; run Situational Router to determine playbook; research competitor channel activity | Calculate brand maturity and AARRR priority gap from existing data -- do not ask, calculate |
| 2. Analyze & Recommend | ICE-score top 15 tactics; build channel plan; design content strategy; draft campaign concepts; allocate budget | Every tactic must serve the target segment and reinforce the positioning from Strategy |
| 3. Present Findings | Share tactical plan with playbook rationale, ranked backlog, channel plan, content strategy, campaigns, budget | Present as actionable plan with clear reasoning for each recommendation |
| 4. Validate & Refine | Confirm budget envelope, team capacity, channel preferences/restrictions | User may reject specific channels ("we don't do TikTok") or adjust budget allocation |
| 5. Save & Advance | Write `04-tactics.md`; update `README.md`; present HITL gate | Check every tactic: serves target segment? Reinforces positioning? Closes AARRR gap? |

#### Mandatory Cross-Phase Dependencies

- Playbook selection MUST be calculated from Phase 1-3 data (brand maturity from Situation, AARRR gaps from Objectives baseline).
- Every tactic MUST serve the positioning and target segment defined in Strategy.
- Budget allocation MUST follow 70/20/10 mapped to the ICE-prioritized tactic list.
- Content ideas MUST use customer language from Situation JTBD profile.

#### HITL Gate Prompt

```
## Phase 4 Complete: Tactics Planning

**Saved to:** `./.pawbytes/marketing-suites/brands/{brand-slug}/sostac/04-tactics.md`

### Key Decisions Made
- [Playbook selected: name and rationale]
- [Top 3 tactics by ICE score]
- [Budget allocation summary]

### Cross-Phase Consistency Check
- Aligns with: Strategy segments [specific segments targeted], Strategy positioning [reinforced by X tactics], Objectives OKRs [tactics mapped to KRs]
- Supports: Action (sprint plan will sequence these tactics), Control (every tactic needs a KPI)

---

**Review Options:**
1. Approve & Continue -- Move to Action phase
2. Request Changes -- Tell me what to adjust
3. Deep Dive -- Walk through specific sections in detail

**What would you like to do?**
```

---

### Phase 5: Action Planning

| Property | Value |
|----------|-------|
| **Output** | `05-action.md` |
| **Phase Question** | "Who does what, when?" |
| **Entry Conditions** | Phase 4 approved; all prior phase documents exist and are approved |
| **Exit Conditions** | User approves via HITL gate |
| **Capability Reference** | `./references/capability-action.md` |

#### Frameworks Applied

RACI Matrix, Agile Marketing Sprints, Objective-and-Task Budgeting, Kotter's Change Model.

#### 5-Step Inner Loop

| Step | Action | Details |
|------|--------|---------|
| 1. Research | Re-read ICE backlog from Tactics; assess team capacity from Situation; identify dependencies | Pull highest-ease, high-impact items for quick wins |
| 2. Analyze & Recommend | Build 90-day sprint plan; draft RACI; calculate bottom-up budget; build risk register | Break tactics into 2-week sprints; flag resource bottlenecks; identify top 5-7 risks |
| 3. Present Findings | Share execution roadmap with quick wins, sprint plan, resource requirements, budget, risks | Quick wins first (this week / month 1), then phased sprint plan |
| 4. Validate & Refine | Confirm team capacity, tool access, hard deadlines, outsourcing appetite | User may adjust sprint scope or ownership assignments |
| 5. Save & Advance | Write `05-action.md`; update `README.md`; present HITL gate | Verify: no person has >2 sprint items; budget within 20% of allocation; dependencies in correct sequence |

#### Mandatory Cross-Phase Dependencies

- Sprint plan MUST sequence tactics from the Phase 4 ICE backlog in priority order.
- RACI roles MUST be feasible given the team size and capabilities identified in Situation.
- Bottom-up budget MUST be reconciled against the allocation from Tactics -- gaps or surpluses must be flagged with recommendations.
- Risk register MUST reference known vulnerabilities from all prior phases.

#### HITL Gate Prompt

```
## Phase 5 Complete: Action Planning

**Saved to:** `./.pawbytes/marketing-suites/brands/{brand-slug}/sostac/05-action.md`

### Key Decisions Made
- [Quick wins identified for Week 1]
- [90-day sprint plan scope]
- [Budget reconciliation result]

### Cross-Phase Consistency Check
- Aligns with: Tactics ICE backlog [prioritized correctly], Situation team capacity [resource constraints respected], Objectives KRs [sprint milestones map to target deadlines]
- Supports: Control (every major action needs a measurement checkpoint)

---

**Review Options:**
1. Approve & Continue -- Move to Control phase
2. Request Changes -- Tell me what to adjust
3. Deep Dive -- Walk through specific sections in detail

**What would you like to do?**
```

---

### Phase 6: Control Setup

| Property | Value |
|----------|-------|
| **Output** | `06-control.md` |
| **Phase Question** | "How do we monitor and improve?" |
| **Entry Conditions** | Phase 5 approved; all prior phase documents exist and are approved |
| **Exit Conditions** | User approves via HITL gate; then triggers Final Plan Review |
| **Capability Reference** | `./references/capability-control.md` |

#### Frameworks Applied

North Star Metric, Attribution Models, Leading vs Lagging Indicators, PDCA Cycle, Balanced Scorecard, OKR Review Cadence.

#### 5-Step Inner Loop

| Step | Action | Details |
|------|--------|---------|
| 1. Research | Re-read all OKR Key Results from Objectives; assess data maturity from Situation; review action cadence | Match attribution model to brand's channel mix, purchase cycle, and data maturity |
| 2. Analyze & Recommend | Recommend North Star Metric; select attribution model; build leading/lagging framework; design optimization triggers; draft dashboard spec | Every OKR KR must have both a leading and lagging indicator; triggers must be specific "if X then Y" rules |
| 3. Present Findings | Share measurement and optimization framework | North Star with reasoning, attribution model, trigger rules, review cadence, dashboard spec |
| 4. Validate & Refine | Confirm data sources available, team analytics capacity, existing dashboard tools | User may flag tools they already have or constraints on data collection |
| 5. Save & Advance | Write `06-control.md`; update `README.md`; present HITL gate; then trigger Final Plan Review | Verify: every KR has a metric; dashboard max 7 metrics per view; review rhythm matches action cadence |

#### Mandatory Cross-Phase Dependencies

- Control MUST measure every OKR Key Result from Objectives -- no KR left unmeasured.
- Attribution model MUST match the data maturity level identified in Situation.
- Optimization triggers MUST reference specific metrics and thresholds from the Tactics channel plan.
- Review cadence MUST align with the sprint cadence from Action.
- Feedback loop MUST describe how learnings feed the next Situation Analysis cycle.

#### HITL Gate Prompt

```
## Phase 6 Complete: Control Setup

**Saved to:** `./.pawbytes/marketing-suites/brands/{brand-slug}/sostac/06-control.md`

### Key Decisions Made
- [North Star Metric selected with rationale]
- [Attribution model chosen]
- [Key optimization triggers defined]

### Cross-Phase Consistency Check
- Aligns with: Objectives KRs [every KR has measurement], Action cadence [review rhythm matches sprints], Tactics channels [triggers reference channel metrics]
- Completes: Full SOSTAC pipeline -- all 6 phases documented

---

All 6 phases are now complete. Proceeding to Final Plan Review.
```

---

## Cross-Phase Consistency Rules

These are hard rules. Violations must be flagged and resolved before a phase can be approved.

### Dependency Map

| Phase | Must Reference From | Must Feed Into |
|-------|---------------------|----------------|
| 1. Situation | Auto-Discovery data | All subsequent phases |
| 2. Objectives | Situation TOWS options, 5S gaps | Strategy, Control |
| 3. Strategy | Situation competitive landscape, Objectives OKRs | Tactics, Action |
| 4. Tactics | Strategy segments and positioning, Objectives baselines | Action, Control |
| 5. Action | Tactics ICE backlog, Situation team capacity | Control |
| 6. Control | Objectives KRs, Action cadence, Tactics channel metrics | Next planning cycle |

### Specific Consistency Checks

| Rule | Check | Violation Response |
|------|-------|--------------------|
| Objectives trace to TOWS | Every objective references a specific TOWS strategic option | Flag untraceable objectives; ask user to justify or revise |
| Strategy serves Objectives | Each OKR has a strategic pathway showing how it will be achieved | Flag orphaned OKRs with no strategic support |
| Segments are reachable | Target segments can be reached with available resources from Situation | Flag segments that require capabilities the brand does not have |
| Tactics serve positioning | Every tactic reinforces the positioning statement from Strategy | Remove or adjust tactics that dilute positioning |
| Budget is reconciled | Bottom-up Action budget is within 20% of Tactics allocation | Flag gap with recommendations to adjust scope or budget |
| Control covers all KRs | Every OKR Key Result has a corresponding metric in Control | Flag unmeasured KRs as critical gaps |
| Content uses customer language | Content topics and messaging use JTBD language from Situation | Flag generic messaging that ignores customer research |
| Triggers are actionable | Every optimization trigger has a specific threshold, action, and owner | Flag vague triggers ("monitor closely") as incomplete |

---

## Resumption Protocol

When returning to an in-progress SOSTAC plan -- whether in a new session or after an interruption:

### Step 1: Discover State

```bash
# Check SOSTAC status
cat ./.pawbytes/marketing-suites/brands/{brand-slug}/sostac/README.md
```

The `README.md` is the state machine tracker. It records which phases are complete, in-progress, or pending.

### Step 2: Re-Ground on All Completed Phases

Read **every completed phase document** in order. Do not skip phases. The agent must re-internalize the full context before resuming work.

| If README shows... | Then... |
|--------------------|---------|
| All phases complete | Load `./references/capability-edit.md`; present edit menu |
| Phase N complete, Phase N+1 not started | Read phases 0 through N; begin Phase N+1 inner loop at Step 1 (Research) |
| Phase N in-progress | Read phases 0 through N-1; read any partial draft of Phase N; resume at the appropriate inner-loop step |
| No phases complete | Begin with Auto-Discovery |

### Step 3: Resume at First Incomplete Phase

Present the user with a status summary before resuming:

```
## Resuming SOSTAC Plan: {brand-name}

**Completed:** Phases 0-{N} ({phase names})
**Resuming:** Phase {N+1} -- {phase name}

I've re-read all completed phases to ensure consistency. Here's where we left off:

[Brief summary of what was established in prior phases]

Ready to begin Phase {N+1}: {phase question}?
```

### Step 4: Never Skip Ahead

Even if the user requests jumping to a later phase, all intermediate phases must be completed first. If the user insists, explain the dependency:

> "Phase {X} depends on outputs from Phase {Y}, which hasn't been completed yet. I'd recommend completing Phase {Y} first so we have the foundation for {X}. Want to start there?"

---

## Quality Gates

### Per-Phase Quality (During Inner Loop)

Each phase has specific success criteria defined in its capability reference. Before the Save step, verify:

| Phase | Key Quality Checks |
|-------|-------------------|
| Situation | Every SWOT entry has specific evidence; TOWS produces actionable options; JTBD uses customer language |
| Objectives | Every KR has baseline, target, deadline, and benchmark; RACE coverage is complete or gaps are deliberate; cascade connects business goals to channel targets |
| Strategy | Segments are specific (not "businesses"); positioning is differentiated; journey map has intervention points |
| Tactics | Playbook matches maturity and AARRR gap; ICE scores have reasoning; content ideas are specific; budget follows 70/20/10 |
| Action | Quick wins can genuinely ship in Week 1; sprint plan has realistic WIP limits; RACI exposes bottlenecks; budget reconciled |
| Control | North Star measures customer value; attribution matches data maturity; every KR has leading indicators; triggers are specific with thresholds |

### Final Plan Review (After Phase 6)

After all 6 phases are complete and approved, run a structured review session. Load `./references/quality-scorecard.md` for full criteria.

#### Quality Scorecard

Score each phase on a 10-point scale against Must Have criteria and Red Flag checks:

| Phase | Score | Strengths | Gaps |
|-------|-------|-----------|------|
| Situation | X/10 | | |
| Objectives | X/10 | | |
| Strategy | X/10 | | |
| Tactics | X/10 | | |
| Action | X/10 | | |
| Control | X/10 | | |
| **Total** | **X/60** | | |

#### Quality Thresholds

| Score | Status | Action |
|-------|--------|--------|
| 50-60 | Excellent | Approve and execute |
| 40-49 | Good | Minor revisions, then approve |
| 30-39 | Adequate | Address gaps before execution |
| Below 30 | Needs Work | Major revision required |

#### Cross-Phase Consistency Audit

Verify all rules from the Cross-Phase Consistency Rules section above. Present findings as:

```
### Cross-Phase Consistency
- [PASS/FAIL] Objectives address Situation gaps: [specific reference]
- [PASS/FAIL] Strategy segments are reachable: [specific reference]
- [PASS/FAIL] Tactics serve Strategy: [specific reference]
- [PASS/FAIL] Control measures all OKRs: [specific reference]
- [PASS/FAIL] Budget is reconciled: [specific reference]
```

#### Industry Standard Checklist

| Standard | Check |
|----------|-------|
| Evidence-Based | All major claims have sources; benchmarks cited for targets; competitor claims verified |
| Measurable | Every objective has a number; every tactic has a KPI; every action has a deadline |
| Actionable | Someone can execute from this document; dependencies are clear; next 30 days are explicit |
| Realistic | Budget matches ambitions; timeline accounts for capacity; resource constraints acknowledged |
| Coherent | Strategy explains how objectives are achieved; tactics deliver the strategy; control measures what matters |

#### Final Plan Review Gate Prompt

```
## SOSTAC Plan Review: {brand-name}

### Overall Quality Score: X/60

### Strengths
1. [Specific strength with evidence]
2. [Specific strength with evidence]

### Gaps to Address
1. [Specific gap with recommendation]
2. [Specific gap with recommendation]

### Cross-Phase Consistency
- [PASS/FAIL] [Each check with specific reference]

### Industry Standard Checklist
- [PASS/FAIL] [Each standard with notes]

### Recommendation
[Approve / Needs Revision / Major Rework]

---

**What would you like to do?**
1. Approve Plan -- Mark as final and generate plan-summary.md
2. Request Changes -- Specify which phases need adjustment
3. Walk Through -- Detailed review of specific sections
```

---

## State Tracking

### README.md as State Machine

The file `./.pawbytes/marketing-suites/brands/{brand-slug}/sostac/README.md` is the single source of truth for plan state. It is updated after every phase save.

#### README.md Format

```markdown
# SOSTAC Plan: {Brand Name}

**Created:** {date}
**Last Updated:** {date}
**Status:** {In Progress | Complete | Final}

## Phase Status

| Phase | Status | File | Last Updated |
|-------|--------|------|--------------|
| 00 - Auto-Discovery | [Complete/In Progress/Pending] | `00-auto-discovery.md` | {date} |
| 01 - Situation | [Complete/In Progress/Pending] | `01-situation.md` | {date} |
| 02 - Objectives | [Complete/In Progress/Pending] | `02-objectives.md` | {date} |
| 03 - Strategy | [Complete/In Progress/Pending] | `03-strategy.md` | {date} |
| 04 - Tactics | [Complete/In Progress/Pending] | `04-tactics.md` | {date} |
| 05 - Action | [Complete/In Progress/Pending] | `05-action.md` | {date} |
| 06 - Control | [Complete/In Progress/Pending] | `06-control.md` | {date} |

## Key Decisions Log

- {date}: [Decision made during Phase X]
- {date}: [Decision made during Phase Y]
```

#### State Transitions

| Event | README Update |
|-------|---------------|
| Phase started | Mark phase as "In Progress"; update Last Updated |
| Phase saved and approved via HITL gate | Mark phase as "Complete"; update Last Updated; log key decisions |
| Phase edited (Edit Mode) | Keep phase as "Complete"; update Last Updated; log changes |
| Final Plan Review passed | Set overall Status to "Final" |

---

## Edit Mode

After phases are complete, users may need to revise them based on new information, changed circumstances, or quarterly refresh cycles. Load `./references/capability-edit.md` for full edit protocol.

### Entry Points

Edit Mode activates when:
- An existing SOSTAC plan is detected on activation (all or some phases complete)
- User explicitly requests to edit, update, revise, or change a phase

### Edit Menu

When an existing plan is found, present:

```
## SOSTAC Plan Found: {brand-name}

**Status:** {X}/6 phases complete

| Phase | Status | Last Updated |
|-------|--------|--------------|
| [each phase with status] |

---

**What would you like to do?**

1. Edit a Phase -- Revise a specific phase with new information
2. Continue Plan -- Resume from first incomplete phase
3. Full Plan Review -- Run quality scorecard and consistency audit
4. View Phase -- Read and discuss a specific phase in detail
5. Start Fresh -- Archive existing plan and create new one
```

### Edit Flow

When editing a completed phase:

1. **Read** the current phase document and show the user what exists.
2. **Ask** what needs to change.
3. **Research** if needed -- conduct fresh research for the changes using the same Research-Recommend-Validate pattern.
4. **Present** the proposed revision with summary of what changed.
5. **Validate** -- "Does this capture your changes correctly?"
6. **Save** the updated phase document.
7. **Check cross-phase impact** -- identify which downstream phases may be affected.

### Cross-Phase Impact Propagation

After editing a phase, present an impact assessment:

```
## Phase Updated: {Phase Name}

**Changes saved to:** {file path}

### Cross-Phase Impact Check

| Affected Phase | Impact | Action Needed |
|----------------|--------|---------------|
| [downstream phase] | [what changed] | [recommended action] |

---

**Would you like to:**
1. Propagate Changes -- Walk through affected phases and update them
2. Review Later -- Mark phases for review, continue with other work
3. Keep Isolated -- Only this phase changes, downstream phases remain as-is
```

### Edit Impact Reference

| Phase Edited | Potentially Affected Phases |
|-------------|----------------------------|
| Situation | Objectives (TOWS options), Strategy (competitive landscape), Tactics (market data), Action (team capacity), Control (data maturity) |
| Objectives | Strategy (OKR alignment), Tactics (KPI targets), Control (measurement targets) |
| Strategy | Tactics (segment/positioning alignment), Action (resource implications), Control (strategic metrics) |
| Tactics | Action (sprint plan, budget), Control (channel metrics, triggers) |
| Action | Control (review cadence, milestone triggers) |
| Control | Generally self-contained; may trigger next planning cycle |

---

## Common Quality Issues and Fixes

These are the most frequent problems encountered during SOSTAC execution and how to resolve them.

| Issue | Symptom | Phase(s) | Fix |
|-------|---------|----------|-----|
| Assumption stated as fact | "We know customers want..." | Situation | Add research source or reframe as hypothesis needing validation |
| Strategy-tactic confusion | "Our strategy is content marketing" | Strategy, Tactics | Content marketing is a tactic (Phase 4); strategy is WHO/HOW/WHERE (Phase 3) |
| Missing funnel balance | All tactics are TOFU | Tactics | Rebalance TOFU/MOFU/BOFU using situational router playbook weights |
| Vanity metrics | "Grow followers" as an objective | Objectives | Link every metric to a business outcome; apply SMARTA validation |
| No pivot triggers | "We'll see how it goes" in Control | Control | Define specific thresholds with "if X then Y" rules for every key metric |
| Generic segments | "Our target is businesses" | Strategy | Use Situation data to define specific segments ("VP Engineering at 50-200 person SaaS companies") |
| Budget-scope mismatch | Bottom-up budget 40% over allocation | Action, Tactics | Reconcile by cutting lowest-ICE tactics or increasing budget; flag the gap explicitly |
| Orphaned objectives | OKR not connected to any strategy or tactic | Objectives, Strategy | Trace every objective to a TOWS option and a strategic pathway |
