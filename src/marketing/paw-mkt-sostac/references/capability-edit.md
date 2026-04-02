# Capability: Edit Existing SOSTAC Plan

## When to Use

Use this capability when:
- User wants to revise a specific phase of an existing SOSTAC plan
- User wants to update the plan based on new information or changed circumstances
- User explicitly says "edit", "update", "revise", or "change" a phase

## Activation Flow

### 1. Discovery

First, check what exists:

```bash
# List available brands
ls ./.pawbytes/marketing-suites/brands/

# Check SOSTAC status for specific brand
cat ./.pawbytes/marketing-suites/brands/{brand-slug}/sostac/README.md
```

### 2. Present Edit Options

When an existing SOSTAC plan is found, present the edit menu:

```
## 📋 SOSTAC Plan Found: {brand-name}

**Status:** {X}/6 phases complete

| Phase | Status | Last Updated |
|-------|--------|--------------|
| 00 - Auto-Discovery | ✅ Complete | [date] |
| 01 - Situation | ✅ Complete | [date] |
| 02 - Objectives | ✅ Complete | [date] |
| 03 - Strategy | ✅ Complete | [date] |
| 04 - Tactics | ✅ Complete | [date] |
| 05 - Action | ✅ Complete | [date] |
| 06 - Control | ✅ Complete | [date] |

---

**What would you like to do?**

1. ✏️ **Edit a Phase** — Revise a specific phase with new information
2. ➕ **Continue Plan** — Resume from first incomplete phase
3. 🔄 **Full Plan Review** — Run quality scorecard and consistency audit
4. 📖 **View Phase** — Read and discuss a specific phase in detail
5. 🆕 **Start Fresh** — Archive existing plan and create new one

**Which option?**
```

### 3. Phase Edit Flow

If user selects "Edit a Phase":

```
**Which phase would you like to edit?**

1. 00 - Auto-Discovery (research findings)
2. 01 - Situation (market analysis, SWOT, competitors)
3. 02 - Objectives (OKRs, KPIs, targets)
4. 03 - Strategy (positioning, segments, channels)
5. 04 - Tactics (channel plans, priorities)
6. 05 - Action (roadmap, owners, timeline)
7. 06 - Control (measurement, dashboards, reviews)

**Enter phase number:**
```

### 4. Execute Edit

When editing a phase:

1. **Read the current phase document** — Show the user what exists
2. **Ask what needs to change** — "What would you like to update in this phase?"
3. **Research if needed** — Conduct fresh research for the changes
4. **Present revision** — Show the proposed changes with diff or summary
5. **Validate** — "Does this capture your changes correctly?"
6. **Save** — Update the phase document
7. **Propagate changes** — Check if downstream phases need updates

### 5. Cross-Phase Impact Check

After editing a phase, check downstream impact:

```
## ✅ Phase Updated: 02 - Objectives

**Changes saved to:** `sostac/02-objectives.md`

### Cross-Phase Impact Check

The following changes may affect downstream phases:

| Affected Phase | Impact | Action Needed |
|----------------|--------|---------------|
| 03 - Strategy | OKR targets changed | Review segment priorities |
| 04 - Tactics | New KPIs added | Add tracking setup |
| 06 - Control | Targets updated | Update dashboard metrics |

---

**Would you like to:**
1. ✅ **Propagate Changes** — Walk through affected phases and update them
2. 📋 **Review Later** — Mark phases for review, continue with other work
3. 🔒 **Keep Isolated** — Only this phase changes, downstream phases remain as-is

**What would you like to do?**
```

## Edit Scenarios

### Scenario A: New Competitor Information

User: "A new competitor just launched and I need to update our Situation analysis."

Flow:
1. Load `01-situation.md`
2. Conduct fresh competitor research
3. Update competitive landscape section
4. Re-run SWOT/TOWS if positioning changed
5. Check if Strategy phase needs adjustment

### Scenario B: Changed Business Goals

User: "We pivoted our product focus. Need to update Objectives and Strategy."

Flow:
1. Load `02-objectives.md` and `03-strategy.md`
2. Understand the pivot through questions
3. Revise objectives to align with new direction
4. Update strategy positioning and segments
5. Flag Tactics for review (channel priorities may change)

### Scenario C: Add Missing Measurement

User: "Our Control phase is weak. Help us add proper tracking."

Flow:
1. Load `06-control.md`
2. Read all objectives from `02-objectives.md`
3. Design measurement framework for each OKR
4. Add dashboard specifications and review cadences
5. Ensure every Key Result has a metric

### Scenario D: Quarterly Refresh

User: "It's Q2. Let's refresh our Tactics based on Q1 learnings."

Flow:
1. Load `04-tactics.md`
2. Ask about Q1 performance and learnings
3. Update channel priorities based on results
4. Adjust ICE scores with new confidence data
5. Update Action timeline if needed

## Behaviors

### DO
- Always read the current phase before editing
- Show the user what exists before asking for changes
- Research changes just like a new phase (Research-Recommend-Validate)
- Check cross-phase consistency after every edit
- Offer to propagate changes to affected phases

### DO NOT
- Edit without showing the current state first
- Allow edits that break cross-phase consistency without warning
- Skip the validation step even for "small" changes
- Forget to update the README.md completion tracker

## Output Contract

When editing a phase:
- **Phase loaded**: which phase was read
- **Current state summary**: key points from existing document
- **Changes requested**: what the user wants to update
- **Research conducted**: any new information gathered
- **Revision presented**: proposed changes shown
- **User validation**: confirmation received before saving
- **File updated**: path where revision was saved
- **Cross-phase impact**: affected phases identified
- **Propagation offered**: option to update downstream phases