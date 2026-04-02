# Save Memory

## Purpose

Persist important context, user preferences, and session learnings to the shared agency memory.

## When to Save

Trigger this capability when:
- User provides brand preferences or guidelines
- New campaign brief is approved
- Design decisions are confirmed
- User feedback on style/aesthetic is given
- Patterns in user preferences are noticed

## Memory Locations

**Shared Agency Memory:** `.pawbytes/creative-suites/`

| File | Purpose | When to Update |
|------|---------|----------------|
| `index.md` | Active brands, campaigns, status | When context changes |
| `brands/{brand}/guidelines.md` | Brand identity, colors, fonts | When brand is created or updated |
| `brands/{brand}/campaigns/{campaign}/brief.md` | Campaign brief | When brief is approved |
| `daily/{YYYY-MM-DD}.md` | Activity log | After each significant action |

## Save Process

1. Determine what needs to be saved (brand info, preferences, decisions)
2. Identify correct memory file
3. Read existing content
4. Update with new/changed information
5. Write updated file
6. Log activity to daily file

## Format

**Brand Guidelines:**
```markdown
# {Brand Name} Guidelines

## Colors
- Primary: {HEX}
- Secondary: {HEX}
- Accent: {HEX}

## Typography
- Headlines: {Font Family}
- Body: {Font Family}

## Logo Rules
- Clear space: {measurement}
- Minimum size: {measurement}

## Visual Style
- Photography style: {description}
- Illustration style: {description}
- Overall aesthetic: {description}
```

**Daily Log Entry:**
```markdown
## {Timestamp}
[Designer] {Action taken}
- Created: {asset list}
- For: {campaign/platform}
- Notes: {any relevant notes}
```

## Example Usage

> "Save these brand colors: primary is #2C5F2D forest green, secondary is #D4A574 warm amber"

## After Saving

Confirm save to user and reference the file location.