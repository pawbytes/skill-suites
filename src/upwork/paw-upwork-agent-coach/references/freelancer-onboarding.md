# Freelancer Onboarding

Create a new freelancer workspace and capture the raw material discovery and positioning build from. This is the first real conversation — make it feel like the start of a working relationship, not a form.

## Open the floor first

Before any structured questions, invite the freelancer to dump everything: who they are, what they do, the work they've actually done and enjoyed, their current Upwork profile if they have one (paste it), what's not working, what they wish a client saw in them. Most of what onboarding needs is in that dump. Then fill only the gaps.

## What the workspace needs to capture

Derive a **slug** from their name or handle (lowercase, hyphens, no special characters). The goal of onboarding is a `freelancer-context.md` that holds:

- **Identity** — name/handle, where they are now (just starting on Upwork, some history, established and pivoting).
- **Raw skills and history** — everything they can do, the projects they've actually delivered, and crucially *which work they enjoyed and which paid well*. This is the raw ore positioning mines; capture it broad and honest, don't pre-filter it into a niche yet.
- **Voice and tone** — how they sound. Pull this from how they write in the conversation and from any pasted profile; note it so the profile/proposal specialists can match it. If a pasted profile reads stiff but they talk like a real person in chat, flag that — their real voice is usually the better one.
- **Existing Upwork presence** — current title/overview/portfolio if any (paste welcome), and what they think isn't converting.

Ask but don't block on: target hourly/project rate they have in mind, portfolio pieces they could show, competitors or freelancers they admire.

## Scaffold the workspace

If `paw-upwork-setup` already scaffolded this freelancer (the slug's folder and `index.md` exist), use it. Otherwise create the skeleton:

```bash
mkdir -p "{project-root}/.pawbytes/upwork-suites/freelancers/{slug}/research"
mkdir -p "{project-root}/.pawbytes/upwork-suites/freelancers/{slug}/profile"
mkdir -p "{project-root}/.pawbytes/upwork-suites/freelancers/{slug}/proposals"
mkdir -p "{project-root}/.pawbytes/upwork-suites/freelancers/{slug}/daily"
```

Resolve `{project-root}` to the real project root for directories on disk.

## freelancer-context.md

Write to `{project-root}/.pawbytes/upwork-suites/freelancers/{slug}/freelancer-context.md`:

```markdown
# Freelancer Context — {name}

## Identity
- **Name/handle**: {name}
- **Slug**: {slug}
- **Stage**: {just starting | some history | established/pivoting}
- **Created**: {YYYY-MM-DD}

## Skills & History (raw — pre-niche)
{Everything they can do and have done. Mark enjoyed work and well-paid work.}

## Voice & Tone
{How they actually sound. Note any gap between a stiff existing profile and their real voice.}

## Current Upwork Presence
{Existing title/overview/portfolio if any, and what they think isn't working. Or "Starting fresh".}

## Rate Thinking
{What they have in mind, if anything. To be grounded against market research.}

## Notes
{Anything else worth carrying forward.}
```

## index.md

If setup didn't already create it, write `index.md` (see the setup skill for the canonical template). If it exists, leave it — you'll curate its status row as positioning and work accumulate.

## Log the session

Append a one-line entry to `{project-root}/.pawbytes/upwork-suites/freelancers/{slug}/daily/{YYYY-MM-DD}.md` tagged `[coach]` noting onboarding happened and what you captured.

## After onboarding

Move naturally into Discovery & Positioning. If their history is rich but you have no live market signal, recommend running `paw-upwork-research` first so the niche you land on is evidence-backed — but follow the freelancer's energy. Don't force research on someone who already knows their lane and just needs it sharpened.
