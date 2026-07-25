# Outcome Intake & Client History

Close the learning loop when proposals go out and results come back. Outcomes feed pricing calibration, client history, and orchestrator guidance for returning clients.

## Outcome intake

When the seller reports results — "we won Acme at $45k", "lost on price", "no response after two weeks" — capture structured learning.

### Write `outcome.md`

Path: `{run-folder}/outcome.md`

```markdown
# Outcome — {clientName}

## Status
won | lost | no-response

## Details
- **Date recorded:** {YYYY-MM-DD}
- **Amount:** {if won or quoted}
- **Proposal type:** {pitch | rfp | scoping}
- **Pricing mode:** {from pricing.json}

## Client feedback
{What the client said — verbatim if possible}

## Lessons learned
- {bullet}

## What worked
- {bullet}

## What didn't
- {bullet}
```

Fill from seller input. Read `pricing.json` and `brief.md` for context — don't invent feedback.

### Pricing history

Note that `paw-pa-pricing` appends to `{memory-root}/library/pricing-history.json` when pricing runs. If outcome changes the `won` flag or adds `clientFeedback`, offer to update the matching history entry or re-run library validation — do not silently edit JSON without seller confirmation.

### Update client history

Path: `{memory-root}/clients/{client-slug}/history.md` (create client folder if missing).

Append a chronological entry:

```markdown
## {YYYY-MM-DD} — {proposalType} ({status})

- **Run folder:** `proposals/{slug}-{date}/`
- **Outcome:** {won | lost | no-response}
- **Amount:** {if known}
- **Angle / pricing:** {tiers, total, key hook from brief}
- **Notes:** {what worked or didn't — distilled}

---
```

**Client slug:** lowercase, hyphenated from `clientName` in `brief.md`.

### Curate `index.md`

Update the **Recent Proposals** section — last 5 runs with client, date, status, folder path.

Append to `daily/YYYY-MM-DD.md`:

```
{HH:MM} [orchestrator] outcome recorded: {client} — {status}
```

## Returning clients

On activation or when a client name appears in a new brief:

1. Resolve `{client-slug}` from `clientName`.
2. If `{memory-root}/clients/{client-slug}/history.md` exists, load it before pipeline start.
3. Tell the seller what you found: "Acme — you pitched them in March (lost on price), sent a scoping doc in January (won). I'll factor that into research routing."
4. Research workflow may append to client history during its run; orchestrator owns outcome entries after send.

## Patterns to act on

After recording outcomes, surface actionable patterns (don't just file and forget):

- **Winning tier/price band** — "Your tiered packages around $X are winning for {industry} clients."
- **Repeated losses on price** — suggest repricing or value-based framing on the next run.
- **Silent proposals** — note if a client or proposal type consistently gets no response.
- **Returning wins** — recommend referencing prior work in the next brief (generation reads client history via research).

## When to prompt

Proactively suggest outcome intake when:

- Seller says they sent the proposal.
- Seller mentions a client by name with result language ("Acme went with someone else").
- A run folder has `final-proposal.*` but no `outcome.md` and the conversation references results.
