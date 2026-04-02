# Growth Experiment Sprint Workflow

This reference defines the standard workflow, phase gates, diagnostic questions, ethical boundaries, benchmarks, and deliverable format for all guerrilla marketing and growth hacking work.

---

## Workflow Overview

The Growth Experiment Sprint is a 7-phase lifecycle that takes unconventional marketing tactics from ideation through execution and measurement. Every phase has entry conditions, key activities, deliverables, and exit conditions.

The core principle: **Risk assessment is mandatory before execution.** A hard gate between Phase 3 (Risk/Reward Scoring) and Phase 5 (Execution Plan) ensures no tactic moves forward without documented risk evaluation and mitigation.

### Phase Summary

| Phase | Name | Purpose | Typical Duration |
|-------|------|---------|-----------------|
| 1 | Context & Objectives | Define growth goal and constraints | 1-2 hours |
| 2 | Tactic Ideation | Generate unconventional tactic candidates | 2-4 hours |
| 3 | Risk/Reward Scoring | Score and filter tactics | 1-2 hours |
| **GATE** | **Risk Assessment Gate** | **Mandatory review before proceeding** | **Blocking** |
| 4 | Experiment Design | Define hypothesis and test structure | 2-4 hours |
| 5 | Execution Plan | Build detailed execution timeline | 2-4 hours |
| 6 | Launch & Monitor | Execute with real-time monitoring | Varies (1 day - 4 weeks) |
| 7 | Measurement & Learning | Analyze, document, decide scale or kill | 1-2 days |

---

## Phase 1: Context & Objectives

### Purpose
Establish the growth goal, constraints, risk appetite, and strategic alignment before generating any tactics. Guerrilla tactics without strategic grounding are random stunts.

### Entry Conditions
- Brand context or SOSTAC plan available (or user provides equivalent context)
- User has articulated a growth need or marketing challenge

### Key Activities
1. **Define the growth goal**: Specific, measurable, time-bound. "Increase trial signups by 30% in Q2" not "grow faster."
2. **Document budget constraints**: Total available budget, cost-per-experiment ceiling, whether spend is one-time or recurring.
3. **Set timeline**: Campaign window, any hard deadlines (product launch, seasonal event, competitor move).
4. **Assess risk appetite**: Conservative (proven tactics only), moderate (calculated risks with mitigation), aggressive (high-risk/high-reward acceptable).
5. **Identify strategic alignment**: Which SOSTAC objectives does this serve? Which audience segments are targeted?
6. **Map existing channels**: What marketing is already running? Where are the gaps or underperforming areas?

### Deliverables
- Growth experiment brief with goal, constraints, timeline, and risk appetite documented

### Exit Conditions
- Growth goal is specific and measurable
- Budget ceiling is defined
- Risk appetite is explicitly stated (conservative / moderate / aggressive)
- Timeline has a clear start and end date

---

## Phase 2: Tactic Ideation

### Purpose
Generate a diverse set of unconventional tactic candidates. Quantity first, quality filtering comes in Phase 3. The goal is 10-20 raw ideas before scoring.

### Entry Conditions
- Phase 1 brief is complete with defined goal, budget, timeline, and risk appetite

### Key Activities
1. **Brainstorm unconventional tactics**: Apply frameworks from `./references/budget-guerrilla-tactics.md` and `./references/viral-stunt-campaigns.md`.
2. **Explore competitor disruption**: Reference `./references/competitive-disruption.md` for switching campaigns, comparison plays, and counter-positioning.
3. **Identify viral mechanics**: What makes this shareable? What is the viral coefficient target? Reference `./references/growth-hacking-tactics.md`.
4. **Cross-pollinate from other industries**: What unconventional tactics from unrelated industries could be adapted?
5. **Map growth loops**: Identify tactics that create compounding effects (referral loops, content flywheels, network effects).
6. **Consider channel mix**: Street-level, digital, hybrid, community-based, product-led, partnership-based.

### Ideation Frameworks
- **10x Thinking**: What would you do if the goal was 10x the target but with the same budget?
- **Competitor Inversion**: What is the opposite of what competitors are doing?
- **Constraint Creativity**: What would you do with $100? $50? $0?
- **Platform Arbitrage**: Which platforms have underpriced attention right now?
- **Cultural Moment Hijacking**: What trending conversations could be leveraged authentically?

### Deliverables
- Tactic longlist (10-20 raw ideas) with one-line descriptions
- Initial categorization: budget tier (free / $1-500 / $500-2K / $2K+), channel, and effort level

### Exit Conditions
- Minimum 10 tactic ideas generated
- Each idea has a one-line description and estimated budget tier
- Ideas span at least 3 different channels or approaches

---

## Phase 3: Risk/Reward Scoring

### Purpose
Score each tactic on a structured framework to identify the highest-value experiments. Filter out high-risk/low-reward ideas before any resources are committed.

### Entry Conditions
- Tactic longlist from Phase 2 (minimum 10 ideas)

### Key Activities
1. **Score each tactic on the ICE-R framework** (Impact, Confidence, Ease, Risk):

| Dimension | Score 1-10 | What It Measures |
|-----------|-----------|-----------------|
| **Impact** | 1 = negligible, 10 = transformative | Expected effect on the growth metric if the tactic works |
| **Confidence** | 1 = pure guess, 10 = proven in similar context | How certain are we this will work? Based on evidence, analogies, or prior tests |
| **Ease** | 1 = months of effort, 10 = ship today | Speed and resource requirement to execute |
| **Risk** | 1 = high risk, 10 = zero risk | Legal, reputational, operational, and ethical exposure (inverted: lower risk = higher score) |

2. **Calculate composite score**: (Impact + Confidence + Ease + Risk) / 4 = ICE-R Score
3. **Apply risk filters**: Any tactic scoring below 4 on the Risk dimension requires explicit mitigation plan before proceeding.
4. **Rank and shortlist**: Select top 3-5 tactics for experiment design.
5. **Document kill reasons**: For rejected tactics, document why. This prevents re-proposing bad ideas.

### Risk Categories to Evaluate

| Risk Type | Examples | Threshold |
|-----------|----------|-----------|
| **Legal** | Trademark infringement, comparative advertising laws, platform TOS violations | Any legal risk requires legal review |
| **Reputational** | Tone-deaf messaging, cultural insensitivity, audience backlash | Score below 5 = requires brand review |
| **Operational** | Execution complexity, dependency on third parties, timing sensitivity | Score below 4 = simplify before proceeding |
| **Ethical** | Deception, manipulation, astroturfing, exploiting vulnerable audiences | Any ethical violation = automatic kill |
| **Financial** | Budget overrun risk, sunk cost if killed early, opportunity cost | Must stay within defined budget ceiling |

### Deliverables
- Scored tactic matrix with ICE-R scores
- Shortlist of top 3-5 tactics with rationale
- Kill list with documented reasons for rejected tactics

### Exit Conditions
- All tactics scored on all 4 dimensions
- Top 3-5 tactics identified
- No tactic with Risk score below 4 proceeds without documented mitigation plan
- Ethical violations result in automatic removal

---

## Risk Assessment Gate (Mandatory)

This is the single most important quality control in the guerrilla workflow. No tactic advances without passing this gate.

### Gate Criteria

A tactic passes the gate if ALL of the following are true:

1. **ICE-R composite score >= 5.0** (out of 10)
2. **Risk score >= 4** OR a written mitigation plan exists and has been reviewed
3. **No ethical violations** identified (automatic kill if present)
4. **Legal review completed** for any tactic involving: competitor references, user-generated content at scale, public stunts, platform TOS edge cases, or regulated industries
5. **Budget confirmed** within the defined ceiling from Phase 1
6. **Strategic alignment confirmed** with SOSTAC objectives

### When to Escalate at the Gate
- Legal uncertainty -> recommend legal counsel review before proceeding
- Brand risk -> route to brand stakeholder for approval
- Cross-channel coordination -> coordinate with relevant skill leads (paw-mkt-social, paw-mkt-pr, paw-mkt-paid-ads)
- Budget exceeds ceiling -> return to Phase 1 to renegotiate constraints

### Gate Decision
- **PASS**: Proceed to Phase 4 (Experiment Design)
- **CONDITIONAL PASS**: Proceed with documented conditions (e.g., "legal review must clear before launch")
- **FAIL**: Return to Phase 2 for alternative tactics or Phase 3 for re-scoring with modifications

---

## Phase 4: Experiment Design

### Purpose
Transform each shortlisted tactic into a structured experiment with a testable hypothesis, defined control/variant, success metric, and minimum sample size.

### Entry Conditions
- Tactic has passed the Risk Assessment Gate
- ICE-R score and risk mitigation plan documented

### Key Activities
1. **Write the hypothesis**: "If we [do X], then [metric Y] will [change Z] because [reason]."
   - Bad: "If we run a guerrilla campaign, we will get more signups."
   - Good: "If we place comparison landing pages targeting [competitor] keywords with a $500 Google Ads budget, trial signups from competitor-aware traffic will increase by 25% because switchers need a clear side-by-side comparison to overcome inertia."

2. **Define control and variant**:
   - Control: Current state (no intervention) or existing tactic performance
   - Variant: The guerrilla tactic being tested
   - For tactics without a natural control (e.g., street campaigns), use before/after comparison with a defined baseline period

3. **Set success metrics**:
   - **Primary metric**: The single number that determines success or failure
   - **Secondary metrics**: Guard rails to ensure the primary metric is not achieved at the expense of something else
   - **Leading indicators**: Early signals to monitor during execution (engagement rate, click-through, share rate)

4. **Calculate minimum sample size**: Reference `./references/measurement.md`. For most guerrilla experiments:
   - Digital tactics: Standard A/B test calculator (Evan Miller). Target 95% confidence, 80% power.
   - Offline tactics: Define minimum exposure threshold (e.g., "1,000 QR scans needed for statistical relevance")
   - Viral tactics: Define viral coefficient target (K > 0.7 for meaningful amplification, K > 1.0 for true virality)

5. **Set experiment duration**: Minimum 2 business cycles (typically 2 weeks). Account for day-of-week and time-of-day variation.

6. **Define kill criteria**: What conditions trigger an early stop?
   - Negative brand sentiment exceeding threshold
   - Legal or compliance issue discovered
   - Cost per result exceeding 3x projected CPA
   - Engagement below 10% of minimum viable threshold after 25% of duration

### Deliverables
- Experiment brief for each shortlisted tactic (hypothesis, control/variant, metrics, sample size, duration, kill criteria)

### Exit Conditions
- Each experiment has a written hypothesis in "If/then/because" format
- Primary metric is defined and measurable
- Kill criteria are documented
- Minimum sample size or exposure threshold is calculated

---

## Phase 5: Execution Plan

### Purpose
Build the detailed execution timeline with resources, channels, dependencies, and coordination requirements.

### Entry Conditions
- Experiment brief from Phase 4 is complete
- Risk Assessment Gate has been passed

### Key Activities
1. **Build the timeline**: Day-by-day or week-by-week execution schedule with milestones.
2. **Assign resources**: Who does what? Budget allocation per activity. Tool and platform requirements.
3. **Map channel execution**:
   - Digital channels: Platform setup, creative assets, targeting, tracking (UTM, pixels, custom parameters)
   - Offline channels: Location scouting, permits, materials production, logistics
   - Hybrid: How offline drives to digital (QR codes, vanity URLs, hashtags, promo codes)
4. **Set up tracking infrastructure**: UTM parameters, unique promo codes, dedicated landing pages, event tracking, attribution model.
5. **Coordinate with other skills**:
   - Social amplification -> brief paw-mkt-social on timing and messaging
   - PR angle -> brief paw-mkt-pr if the tactic has earned media potential
   - Paid amplification -> brief paw-mkt-paid-ads if paid spend supports the experiment
   - Email follow-up -> brief paw-mkt-email if the tactic generates leads requiring nurture
6. **Prepare contingency plan**: What happens if the tactic gets unexpected attention (positive or negative)?

### Deliverables
- Execution timeline with milestones and owners
- Resource and budget allocation
- Tracking setup documentation
- Cross-skill coordination briefs
- Contingency plan

### Exit Conditions
- Timeline is day-level specific with named owners
- All creative assets and materials are identified (not necessarily produced yet)
- Tracking infrastructure is defined
- Contingency plan covers both success and failure scenarios

---

## Phase 6: Launch & Monitor

### Purpose
Execute the experiment with real-time monitoring and predefined intervention triggers.

### Entry Conditions
- Execution plan from Phase 5 is complete
- Tracking infrastructure is live and verified
- All creative assets and materials are ready
- Team members are briefed on their roles

### Key Activities
1. **Pre-launch checklist**:
   - [ ] Tracking verified (test conversion, check UTM parameters, verify pixel fires)
   - [ ] Creative assets approved and loaded
   - [ ] Team briefed on timeline and responsibilities
   - [ ] Kill criteria documented and accessible to all team members
   - [ ] Monitoring dashboard set up with real-time alerts
   - [ ] Contingency plan reviewed

2. **Execute according to timeline**: Follow the Phase 5 plan. Document any deviations.

3. **Real-time monitoring cadence**:
   - **First 24 hours**: Check every 2-4 hours for leading indicators and anomalies
   - **Days 2-7**: Daily check on primary and secondary metrics
   - **Week 2+**: Twice-weekly check unless anomalies are detected

4. **Monitor for kill criteria triggers**:
   - Negative sentiment spikes on social monitoring
   - Cost per result exceeding 3x threshold
   - Legal or compliance flags
   - Engagement below minimum viable threshold after 25% of duration

5. **Document everything**: Real-time notes on what is happening, unexpected outcomes, user reactions, operational issues.

### Kill Decision Framework

| Signal | Severity | Action |
|--------|----------|--------|
| Negative press or social backlash | High | Immediate pause. Assess damage. Decide kill or modify. |
| Legal/compliance flag | Critical | Immediate kill. No exceptions. |
| CPA exceeding 3x projected | Medium | Pause after 48 hours. Investigate cause. Decide optimize or kill. |
| Engagement below 10% of target after 25% of duration | Medium | Investigate. If root cause is fixable, optimize. If structural, kill. |
| No signal at all after 50% of duration | Low-Medium | Investigate distribution. Amplify or kill. |

### Deliverables
- Launch confirmation with tracking verification
- Daily/weekly monitoring reports
- Kill decision documentation (if triggered)
- Real-time observation log

### Exit Conditions
- Experiment has run for the planned duration OR kill criteria triggered
- All data is captured and accessible
- Observation log is complete

---

## Phase 7: Measurement & Learning

### Purpose
Analyze results, extract learnings, and make a scale-or-kill decision. This phase is where guerrilla experiments generate compounding value through documented institutional knowledge.

### Entry Conditions
- Experiment has completed its planned duration or been intentionally killed
- All tracking data is accessible

### Key Activities
1. **Results analysis**:
   - Primary metric: Did we hit the target? What was the actual lift?
   - Secondary metrics: Were guard rails maintained?
   - Statistical confidence: Is the result statistically significant? (95% confidence minimum for digital experiments)
   - Cost analysis: Actual CPA vs. projected. ROI calculation.

2. **Attribution analysis**:
   - Direct attribution: Conversions directly tracked to the experiment
   - Assisted attribution: Touchpoints where the experiment contributed but was not last-click
   - Halo effects: Unexpected positive outcomes (brand search volume increase, social mentions, PR pickup)

3. **Document learnings** (the most important output):
   - What worked and why?
   - What did not work and why?
   - What surprised us?
   - What would we do differently?
   - What is the replicability score? (1-10: Can this be repeated? Scaled? Applied to other segments?)

4. **Scale or kill decision**:

| Result | Confidence | Decision |
|--------|-----------|----------|
| Primary metric exceeded target | High (95%+ confidence) | Scale: increase budget, expand to new segments, automate |
| Primary metric met target | High | Maintain: continue at current level, optimize incrementally |
| Primary metric near target | Medium | Iterate: modify hypothesis, run refined experiment |
| Primary metric below target | High | Kill: document learnings, move to next experiment |
| Inconclusive | Low | Extend: run longer if sample size was insufficient, or redesign |

5. **Feed back into the system**:
   - Update the growth experiment playbook with new learnings
   - Share cross-skill insights (e.g., messaging that worked can inform paw-mkt-content, paw-mkt-social)
   - Update risk assessment baselines based on actual outcomes

### Deliverables
- Experiment results report (metrics, attribution, ROI)
- Learnings document (what worked, what failed, surprises, recommendations)
- Scale/kill/iterate decision with rationale
- Updated growth experiment playbook

### Exit Conditions
- Results report is complete with statistical analysis
- Learnings are documented in a reusable format
- Scale/kill decision is made with clear rationale
- Playbook is updated

---

## Diagnostic Questions

Ask these before producing any guerrilla marketing or growth hacking recommendation. Recommendations without this context are guesses.

1. **Growth metric**: What specific metric are you trying to move? What is the current baseline?
2. **Budget**: What is the total experimentation budget? What is the maximum per-experiment spend?
3. **Timeline**: When does this need to produce results? Are there external deadlines (launch, event, funding round)?
4. **Risk appetite**: On a scale of conservative to aggressive, where does the brand sit? Has the brand experienced backlash before?
5. **Prior experiments**: What growth tactics have been tried? What worked? What bombed?
6. **Competitive landscape**: Who are the main competitors? What are they doing in marketing? Where are the gaps?
7. **Channel presence**: Which channels are already active? Which are underutilized?
8. **Audience**: Who is the target? Where do they spend attention? What motivates sharing?
9. **Legal constraints**: Any industry regulations? Platform restrictions? Geographic limitations?
10. **Measurement capability**: What tracking is in place? GA4? Event tracking? Attribution model?

If the user cannot answer questions 1, 2, and 10, recommend establishing baseline measurement and budget allocation before running experiments. Growth hacking without measurement is gambling.

---

## Ethics: Bold Without Crossing the Line

Guerrilla marketing operates in unconventional spaces. The line between creative disruption and manipulation must be respected. Every tactic must pass the ethics check.

### Ethical Guerrilla Practices

- **Authentic engagement**: Real conversations, real value, real products. No fake accounts, fake reviews, or astroturfing.
- **Transparent identity**: The brand behind the tactic should be discoverable. Stealth marketing is deception.
- **Respectful disruption**: Disrupting competitor messaging is fair game. Disrupting public spaces, exploiting tragedies, or targeting vulnerable populations is not.
- **Honest claims**: Growth hacks that rely on misleading claims (fake scarcity, fabricated social proof, bait-and-switch) destroy trust and invite regulatory action.
- **Consent-based virality**: Viral mechanics should work because people want to share, not because they are tricked into sharing.

### Tactics That Are Always Off-Limits

| Tactic | Why It Is Banned |
|--------|-----------------|
| Astroturfing (fake grassroots) | Deception; FTC enforcement risk; trust destruction |
| Fake reviews or testimonials | Illegal in most jurisdictions; platforms actively detect and penalize |
| Spam (email, social, SMS) | CAN-SPAM, GDPR, platform violations; brand damage |
| Impersonating competitors | Trademark infringement; legal liability; ethical violation |
| Exploiting crises or tragedies | Reputational catastrophe; deeply unethical |
| Targeting children or vulnerable populations | Regulatory risk; ethical violation |
| Platform TOS violations at scale | Account bans; legal exposure; unsustainable |
| Deceptive redirects or clickjacking | User trust destruction; platform penalties |

### The Ethics Test

Before executing any guerrilla tactic, ask:

1. **If a journalist wrote about this tactic, would the article be positive or negative?**
2. **If a customer discovered how this worked behind the scenes, would they feel respected or manipulated?**
3. **Would we be comfortable if a competitor did this to us?**
4. **Does this create genuine value for the people who encounter it?**

If any answer raises doubt, rethink the tactic. Bold creativity does not require deception.

---

## Industry Benchmarks

Use these benchmarks to set realistic expectations and evaluate experiment results.

### Viral Coefficient Benchmarks

| K-Factor | Classification | Example |
|----------|---------------|---------|
| K < 0.3 | Not viral | Standard paid acquisition |
| K = 0.3-0.7 | Amplified reach | Good referral program, shareable content |
| K = 0.7-1.0 | Strong amplification | Viral mechanics working well |
| K > 1.0 | True virality | Exponential growth (rare and usually temporary) |

### Growth Experiment Success Rates

| Experiment Type | Typical Success Rate | Notes |
|----------------|---------------------|-------|
| Landing page tests | 20-30% produce lift | Higher with strong hypothesis |
| Referral programs | 10-15% adoption rate | Among existing customers |
| Competitive switching campaigns | 2-5% conversion from competitor traffic | Higher with strong comparison content |
| Viral stunts | 5-10% achieve meaningful amplification | High variance; most underperform |
| Growth loops (product-led) | 15-25% produce measurable impact | Compound over time |

### Cost Benchmarks (Guerrilla Tactics)

| Tactic Category | Typical Cost Range | Expected Reach |
|----------------|-------------------|----------------|
| Street-level (stickers, chalk, posters) | $50-500 | 1,000-10,000 impressions |
| QR-driven campaigns | $100-1,000 | 500-5,000 scans |
| Micro-influencer seeding | $200-2,000 | 10,000-100,000 impressions |
| Comparison/switching pages + SEM | $500-5,000/month | 1,000-10,000 clicks/month |
| Viral content production | $200-2,000 | Highly variable (1K-1M+) |
| Community-based campaigns | $0-500 | 500-5,000 engaged interactions |

---

## Deliverables

All guerrilla marketing work saves to the resolved path (see Path Resolution below).

| Deliverable | Filename | Key Sections |
|---|---|---|
| Growth Experiment Brief | `experiment-brief-{slug}-{YYYY-MM-DD}.md` | Goal, constraints, risk appetite, timeline, strategic alignment |
| Tactic Longlist | `tactic-longlist-{YYYY-MM-DD}.md` | Raw ideas, budget tiers, channel categorization |
| ICE-R Scoring Matrix | `scoring-matrix-{YYYY-MM-DD}.md` | All tactics scored, shortlist, kill list with reasons |
| Experiment Design | `experiment-design-{slug}-{YYYY-MM-DD}.md` | Hypothesis, control/variant, metrics, sample size, kill criteria |
| Execution Plan | `execution-plan-{slug}-{YYYY-MM-DD}.md` | Timeline, resources, tracking setup, coordination briefs, contingency |
| Monitoring Report | `monitoring-{slug}-{YYYY-MM-DD}.md` | Daily/weekly metrics, observations, kill decision log |
| Results Report | `results-{slug}-{YYYY-MM-DD}.md` | Metrics, attribution, ROI, learnings, scale/kill decision |
| Growth Playbook Update | `playbook-update-{YYYY-MM-DD}.md` | Cumulative learnings, replicable tactics, updated benchmarks |
| Campaign Concept | `campaign-concept-{name}-{YYYY-MM-DD}.md` | Pitch, concept, execution plan, risk assessment, amplification strategy |
| Stunt Brief | `stunt-brief-{name}-{YYYY-MM-DD}.md` | Concept, logistics, risk assessment, content capture, budget |
| Competitive Disruption Analysis | `competitive-disruption-{competitor}-{YYYY-MM-DD}.md` | Vulnerabilities, conquesting opportunities, switching strategy |

File structure:

```
# Campaign mode:
./.pawbytes/marketing-suites/brands/{brand-slug}/campaigns/{type}-{campaign-slug}/guerrilla/
  experiment-brief-{slug}-{YYYY-MM-DD}.md
  tactic-longlist-{YYYY-MM-DD}.md
  scoring-matrix-{YYYY-MM-DD}.md
  experiment-design-{slug}-{YYYY-MM-DD}.md
  execution-plan-{slug}-{YYYY-MM-DD}.md
  monitoring-{slug}-{YYYY-MM-DD}.md
  results-{slug}-{YYYY-MM-DD}.md
  playbook-update-{YYYY-MM-DD}.md
  campaign-concept-{name}-{YYYY-MM-DD}.md
  stunt-brief-{name}-{YYYY-MM-DD}.md
  competitive-disruption-{competitor}-{YYYY-MM-DD}.md

# Standalone mode:
./.pawbytes/marketing-suites/brands/{brand-slug}/operations/guerrilla/
  (same structure as above)
```

---

## Path Resolution: Campaign vs Standalone

**Campaign mode** -- working within a named campaign:
  -> Save to `./.pawbytes/marketing-suites/brands/{brand-slug}/campaigns/{type}-{campaign-slug}/guerrilla/`
  -> Read campaign strategy at `./.pawbytes/marketing-suites/brands/{brand-slug}/campaigns/{type}-{campaign-slug}/strategy.md`

**Standalone mode** -- evergreen or independent work:
  -> Save to `./.pawbytes/marketing-suites/brands/{brand-slug}/operations/guerrilla/`

**Legacy fallback** -- old directory structure detected:
  -> Save to `./.pawbytes/marketing-suites/brands/{brand-slug}/campaigns/guerrilla/`
  -> Suggest migration to new structure

If unsure which mode, ask: "Is this part of a specific campaign, or standalone work?"

---

## Response Protocol

When the user requests guerrilla marketing or growth hacking work:

1. **Route the starting context** (see `./references/shared-patterns.md` for Starting Context Router). Decide whether this is strategy, experiment design, or active monitoring work.
2. **Read the strongest available context** (Pre-Flight): brand and SOSTAC first when available; otherwise use the existing codebase, competitor data, or user-provided context.
3. **Ask diagnostic questions** if the user has not already provided growth metric, budget, and measurement capability.
4. **Identify the guerrilla domain**. Read the appropriate reference file before producing recommendations:
   - Budget tactics -> `./references/budget-guerrilla-tactics.md`
   - Viral campaigns -> `./references/viral-stunt-campaigns.md`
   - Competitive disruption -> `./references/competitive-disruption.md`
   - Growth hacking -> `./references/growth-hacking-tactics.md`
   - Risk assessment -> `./references/risk-assessment.md`
5. **Run the full workflow**: Context -> Ideation -> Scoring -> **Risk Gate** -> Design -> Plan -> Launch -> Measure. Do not skip the Risk Assessment Gate.
6. **Deliver structured output**: Experiment brief, scored tactic matrix, experiment design, execution plan.
7. **Save deliverables** to the resolved path (see Path Resolution).
8. **Recommend next steps**: Which experiment to run first, what to monitor, when to review.

### When to Escalate

| Scenario | Route To |
|---|---|
| Paid advertising beyond keyword conquesting | paw-mkt-paid-ads |
| Influencer seeding beyond micro-creator outreach | paw-mkt-influencer |
| PR stunts requiring media relations | paw-mkt-pr |
| Social media calendars and community management | paw-mkt-social |
| SEO beyond competitor keyword targeting | paw-mkt-seo |
| Email automation for referral and switching campaigns | paw-mkt-email |
| Content creation for comparison pages | paw-mkt-content |
| Legal uncertainty on any tactic | Recommend legal counsel review |

---

## Research Mode

Use agent-browser for live competitive research, SERP analysis, and viral pattern identification. Check `./.pawbytes/marketing-suites/brands/{brand-slug}/sostac/00-auto-discovery.md` for data already collected.

**Setup**: See `./references/shared-patterns.md` for agent-browser installation instructions.

**Guerrilla Research Commands**:

```bash
# Google Trends - category virality potential
agent-browser --session guerrilla-research open "https://trends.google.com/trends/explore?q={category-keyword}&gprop=youtube"

# YouTube Trending in category
agent-browser --session guerrilla-research open "https://www.youtube.com/results?search_query={category}+viral&sp=CAMSAhAB"

# Reddit - community research for guerrilla opportunities
agent-browser --session guerrilla-research open "https://www.reddit.com/search/?q={category-keyword}&sort=top&t=month"

# TikTok Creative Center
agent-browser --session guerrilla-research open "https://ads.tiktok.com/business/creativecenter/inspiration/topads/pc/en"

# Product Hunt - launch strategies
agent-browser --session guerrilla-research open "https://www.producthunt.com/topics/{category}"
```

Close session when done: `agent-browser --session guerrilla-research close`
