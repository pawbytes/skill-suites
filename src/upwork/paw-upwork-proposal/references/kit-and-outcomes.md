# Kit & Outcomes

Two jobs that make every future proposal faster and sharper: maintaining the reusable proposal kit, and feeding real results back so the kit and proposals learn what actually wins. This is the compounding layer — session one builds the kit, session two's proposals take minutes because the wins are saved. You have `kit.md` and `outcomes.md` in context from activation (or create them on first use).

## The kit

`{project-root}/.pawbytes/upwork-suites/freelancers/{slug}/kit.md` holds the freelancer's reusable, proven proposal building blocks — not generic templates, but the specific phrasing that fits their voice and niche and has earned replies. Save a block to the kit when a proposal element is strong and reusable: a hook angle that landed, a tight case-study blurb, a clean way to frame the rate, a CTA that pulls calls.

Structure it so the proposal-craft path can pull from it fast:

```markdown
# Proposal Kit — {name}

## Hooks
{Proven opening angles by job type, e.g. "Speed-loss hook for slow-store posts: ..."}

## Case-Study Blurbs
{Short, specific proof snippets — a result, a metric, a comparable project. Reusable across proposals.}

## Outcome Promises
{Concrete result statements that resonate in this niche.}

## Rate Framing
{How this freelancer frames their rate against value, pulled from the brief's Rate Range.}

## CTAs
{Low-friction next-step lines that have pulled calls.}

## Reply Scripts
{Saved client-handling responses that converted — from references/client-handling.md.}
```

Keep it curated, not a junk drawer. A block earns its place by being proven and reusable; prune what stopped working. When the proposal-craft path runs, it reads this file, so a well-kept kit is the difference between a one-hour proposal and a five-minute one.

## Outcomes refinement

The feedback loop is what makes the suite *learn*. The coach (`paw-upwork-agent-coach`) is the primary intake for results — "sent 10, got 2 replies on the Shopify ones" lands in `outcomes.md` via the coach's progress-and-feedback path. This skill's job is to *act on* that signal when writing and scoring:

- On activation you read `outcomes.md`. When it shows a winning pattern — an angle, hook, or rate point that pulls replies — lean on it in `proposal-craft.md` and promote it into the kit and the brief's **Proven Angles**.
- When it shows what's going silent, stop repeating it. Don't reuse a hook the data says is cold.
- If the freelancer reports a result directly to *you* mid-session (a proposal you wrote got a reply, or a job converted), capture it: append a row to `outcomes.md`'s log and update **What's Landing** / **What's Not** so the signal isn't lost. Keep `outcomes.md`'s format consistent with what the coach maintains:

```markdown
| Date | What went out | Sent | Replies | Wins | Angle / headline used | Notes |
```

Then route the durable lesson into the kit: a winning angle becomes a saved hook; a converting reply becomes a saved reply script.

## Keep it light

Both files are working memory, not deliverables — short, current, and curated. After updating either, append a `[proposal]` line to today's `daily/` log noting what was saved or refined, and update `index.md` if outcomes changed the proposals-sent or wins count.
