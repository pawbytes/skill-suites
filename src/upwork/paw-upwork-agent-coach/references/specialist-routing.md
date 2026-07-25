# Specialist Routing

The coach coordinates; the specialists produce. When the freelancer is ready to make something, hand off with full context rather than doing the work yourself. Each specialist reads the shared workspace on activation, so the handoff is mostly confirming the prerequisite is met and telling the freelancer what they'll get and where it lands.

## The specialists

| Intent | Specialist | What it produces | Reads from workspace |
|--------|-----------|------------------|----------------------|
| Scan the market, find/validate a niche, "is there demand", rate observations | `paw-upwork-research` | Ranked niche opportunity dashboard (HTML, auto-opens) + report + rate observations | `freelancer-context.md`, `positioning-brief.md` if it exists |
| Build/rewrite the Upwork profile — title, overview, skills, portfolio descriptions, variations | `paw-upwork-profile` | Paste-ready profile drafts + 2–3 variations in `profile/` | `positioning-brief.md`, `freelancer-context.md`, `research/` keywords, `kit.md` |
| Decode a job posting, write a tailored proposal, score a draft, "should I apply" | `paw-upwork-proposal` | Tailored ready-to-send proposals + scoring + growing `kit.md` in `proposals/` | `positioning-brief.md`, `freelancer-context.md`, `kit.md`, `outcomes.md` |

## Prerequisites and the right order

The arc is **Discover → Position → Win → Learn**, and the brief is the hinge:

- **Research** can run anytime, and *should* run before locking positioning when market signal is thin. It's the one specialist that doesn't need a brief first — it helps create one.
- **Profile and proposal both require a positioning brief.** If `positioning-brief.md` doesn't exist when the freelancer wants one of these, don't block — explain why positioning comes first ("the profile is only as sharp as the lane it's selling") and offer to do discovery now, optionally with research first.

## How to hand off

1. Confirm the prerequisite. If a brief is missing for profile/proposal, route to discovery/research first.
2. Tell the freelancer which specialist runs, what it produces, and where it saves — so the handoff feels deliberate, not a dead end.
3. Hand off cleanly: "Run `paw-upwork-profile` — it already reads your positioning brief and voice notes, so it'll come in knowing your lane. It'll give you a paste-ready title and overview plus a couple of variations to test." The freelancer invokes the specialist; the shared workspace carries the context, so you don't need to restate the brief.
4. The freelancer can also go straight to a specialist without you. That's fine — the workspace is the contract, and the specialist reads it on its own. You're the relationship that ties it together, not a required gateway.

## After a specialist runs

When the freelancer comes back from a specialist, you close the loop: read what landed in the workspace, update `index.md`, and point them at the next highest-value step in the arc. After research → positioning. After positioning → profile and the first proposals. After proposals go out → the feedback loop (see `references/progress-and-feedback.md`).
