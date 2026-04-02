# ROI Calculator Detailed Formulas

Extended input/output variable lists, Google Sheet layout specs, embedded calculator specs, and the in-meeting whiteboard script with detailed guidance.

---

### 13.1 Input Variables

Build a calculator that the prospect fills in with their own numbers. Their numbers are always more credible than yours.

**Inputs**:
- Current time spent on [specific task] per week (hours)
- Number of team members doing this work
- Average fully-loaded hourly cost (salary + benefits -- typically $50-$150/hr for knowledge workers)
- Current tool or vendor cost (annual)
- Error rate or rework percentage (if applicable)
- Number of [specific events -- deals, tickets, campaigns] per month

**Outputs**:
- Time saved per year: `(hours/week x team members x 52 weeks) x efficiency gain %`
- Labor cost saved per year: `time saved x hourly rate`
- Tool cost delta: `current cost - new cost`
- Error/rework cost eliminated: `(events x error rate x cost per error)`
- Total annual value: `labor savings + tool delta + error elimination`
- Annual investment (your price)
- Net ROI: `(total annual value - investment) / investment x 100`
- Payback period: `investment / (total annual value / 12)` months
- 3-year cumulative value: `(total annual value x 3) - investment`

### 13.2 Formats

**Google Sheet (preferred for async sharing)**:
- Column A: Input label
- Column B: Their number (light blue fill -- editable)
- Column C: Your assumption (used if they leave blank)
- Outputs section with formulas and a summary table
- Share as "Edit" access so they can plug in their numbers
- Include a "Your results" section that formats the output in plain language

**Embedded calculator on pricing page**:
- 3-5 sliders maximum (team size, time spent, hourly rate)
- Instant calculation as they adjust
- Output: "Teams like yours save $[X] in year one."
- CTA below the output: "See how -- book a demo"

**In-meeting whiteboard version**:
```
"Let me build this with your numbers.

How many people on your team do [specific task]? [Answer: X]
How many hours a week does each person spend on it? [Answer: Y]
What's a rough hourly cost for that role? [Answer: $Z]

So today you're spending roughly [X x Y x Z x 52] per year on [task].

We typically reduce that by [efficiency gain %]. That's [savings amount] per year.

Our annual cost for a team your size is [$price].

That's a payback period of about [months]."
```

### 13.3 Common Mistakes to Avoid

- Do not use your own assumptions without their input. Always anchor to their numbers.
- Do not be overly precise. Round numbers to the nearest $1,000 -- false precision reduces credibility.
- Do not stack every benefit category. Pick 2-3 most compelling drivers and build the case on those.
- Do present the ROI as "conservative" -- tell them what assumptions you made and that the real number is likely higher.
