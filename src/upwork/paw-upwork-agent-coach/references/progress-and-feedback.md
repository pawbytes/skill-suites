# Progress & Feedback

Two jobs that share the same workspace: closing the learning loop when results come in, and orienting the freelancer when they ask where they are. Both run off `index.md` and the workspace files — read before you summarize.

## Feedback-loop intake

When the freelancer reports results — "sent 10 proposals, got 2 replies, both on the Shopify ones" — turn that into learning the next round of work uses. The point of the loop is that session two's proposals are sharper than session one's because you know what landed.

Capture into `{project-root}/.pawbytes/upwork-suites/freelancers/{slug}/outcomes.md` (create it if absent):

```markdown
# Outcomes — {name}

## Log
| Date | What went out | Sent | Replies | Wins | Angle / headline used | Notes |
|------|---------------|------|---------|------|------------------------|-------|
| {date} | {e.g. 5 proposals, Shopify niche} | 5 | 2 | 1 | {the hook/angle} | {what the client responded to} |

## What's Landing
{Patterns you can see: which angles, headlines, niches, and rate points pull replies and wins.
This is the distilled signal — keep it short and current.}

## What's Not
{Angles or niches that consistently go silent, so future work stops repeating them.}
```

Then act on the pattern, don't just record it:

- If an angle is winning, promote it into the brief's **Proven Angles** section so profile and proposal lean on it.
- If the freelancer's positioning is getting silence across the board, that's a signal the lane or the rate may be wrong — raise it honestly and consider re-running research.
- When the proposal specialist next runs, it reads `outcomes.md`, so the kit and future proposals inherit what worked.

Update `index.md` (proposals sent count, last updated) and append a `[coach]` line to today's `daily/` log.

## Progress tracking

When the freelancer asks where they are or what's next, read `index.md` first, then the relevant files, and place them in the arc. Don't dump file contents — give them their position and the single highest-value next move.

Read and summarize:
- `index.md` — the status row (niche, brief, profile, proposals sent).
- `positioning-brief.md` — is the lane locked, or still open?
- `research/` — has a market scan run? what did it recommend?
- `profile/` — drafts done, or not started?
- `proposals/` and `outcomes.md` — what's gone out and what's coming back.

Present it as position + next step:

```
# {name} — Upwork Progress

**Where you are:** {one line — e.g. "Niche locked (Shopify speed), profile drafted, no proposals out yet."}

- Niche & positioning: {locked / open / not started}
- Market research: {done {date} / not run}
- Profile: {drafted ({N} variations) / not started}
- Proposals: {N sent, {N} replies, {N} wins / none yet}

**Highest-value next step:** {the one thing that moves them forward most — e.g. "Run paw-upwork-proposal
on 3–5 live postings in your niche. Your brief and kit are ready, so each should take a few minutes."}
```

The arc — Discover → Position → Win → Learn — tells you the next step: no brief → discovery/research; brief but no profile → profile; profile but no proposals → proposals; proposals out → feedback intake and refinement.
