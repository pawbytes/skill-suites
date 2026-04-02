# Save Memory

Explicitly save current state to memory. Useful after significant work or before ending a session.

## When to Save

- After onboarding a brand
- After creating or updating a campaign brief
- After completing deliverables
- Before ending a session with pending work
- User explicitly requests "save" or "remember this"

## What to Save

**Always update:**
- `index.md` — active brand, campaign status, tool status

**Update as needed:**
- `brands/{brand}/profile.md` — if brand details changed
- `campaigns/{campaign}/status.md` — if campaign progressed
- `daily/{date}.md` — append session summary

## Save Format

Append to daily log with timestamp:

```markdown
## {HH:MM} — {action}
{summary of what happened}
{any decisions made}
{next steps or pending items}
```

## Confirmation

After saving, confirm to user:
- "Got it. I've updated {brand} profile and today's log."
- "Campaign status saved. We'll pick up here next time."

## Manual Invocation

User can request explicit save:
- "Save this"
- "Remember this for next time"
- "Log that"