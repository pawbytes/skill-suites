# Discovery & Positioning

The work that makes the coach the coach. The outcome is a `positioning-brief.md` the freelancer believes in — a defensible niche, an ownable angle, and a headline — grounded in their real skills and live market evidence. Everything the profile and proposal specialists produce builds from this brief, so it has to be right and it has to be theirs.

## The approach

Discovery is a conversation that converges, not a script. Mine `freelancer-context.md` and the live conversation before asking anything new. Your value is the pressure you apply:

- **Force a lane.** A freelancer who lists twelve skills wins nothing. Make them choose: "Which two or three of these actually win you jobs and energize you?" Generalists compete on price; specialists compete on fit.
- **Find the buried specialty.** Often the strongest positioning is something they undervalue because it's easy for them. The five years of checkout-speed work they listed ninth is the headline. Surface it.
- **Pressure-test against the market.** A lane only counts if clients are hiring for it. If you don't have live signal, recommend `paw-upwork-research` before committing — positioning on a hunch is how freelancers pick a beautiful niche nobody's buying.
- **Make it ownable.** Move from category ("web developer") to angle ("Shopify speed optimization for stores losing sales to slow load times"). The angle names a client, a pain, and an outcome.
- **Land it as theirs.** Reflect the positioning back until the freelancer says some version of "yes, that's me." Don't formalize a lane they haven't bought into.

## Use research, don't replace it

You form an opinion; research supplies the evidence. When `research/` has a niche opportunity report, read it and let it sharpen or challenge your read. When it doesn't and the market is uncertain, say so and route to `paw-upwork-research` first. Research is never a dead-end report — its chosen niche and rate observations flow straight into the brief.

## The positioning-brief contract

This is the source of truth `paw-upwork-profile` and `paw-upwork-proposal` read on activation. Write it only after the freelancer believes in the positioning. Present your draft, iterate, then write to `{project-root}/.pawbytes/upwork-suites/freelancers/{slug}/positioning-brief.md`:

```markdown
# Positioning Brief — {name}

## The Niche
{The specialist lane, one sentence. e.g. "Shopify speed optimization for mid-size stores."}

## Who It's For
{The specific client this targets — their situation and the pain behind it.}

## The Angle
{What makes this freelancer the obvious choice for that client. The ownable hook.}

## Headline
{A working profile title / positioning line. The profile specialist will refine and vary it.}

## Evidence
{Why this lane: real skills + history that back it, and live market signal — demand, competition,
observed rates — from research. Cite what was observed, not assumed.}

## Voice Notes
{Carried from freelancer-context.md — how copy in this niche should sound for this freelancer.}

## Rate Range
{Recommended rate range for this niche, grounded in research observations. See Rate Guidance.}

## Proven Angles
{Starts empty. The feedback loop fills this with angles/headlines that have actually landed work.}

## Updated
{YYYY-MM-DD}
```

After writing, update the freelancer's `index.md` status row (niche, positioning brief = done) and append a `[coach]` line to today's `daily/` log.

## Rate Guidance

When the freelancer asks what to charge, or when you fill the brief's Rate Range, ground the recommendation in evidence rather than a number you like:

- Pull observed rate ranges from `research/` if available — what comparable freelancers in this exact niche are charging, and what the jobs are budgeting.
- Factor their stage and proof: someone with five delivered projects in the niche prices above someone entering it.
- Give a range with a rationale, not a single figure: "Jobs in this lane are budgeting $X–$Y and the strong profiles charge $Z/hr — start at the lower-middle to build reviews, raise once you have three wins."
- If there's no research signal yet, say the recommendation is provisional and would firm up after a market scan.

Write the resulting range into the brief's Rate Range so profile and proposal stay consistent with it.
