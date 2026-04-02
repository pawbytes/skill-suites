# Brand Profile Update

Update an existing brand profile when guidelines evolve, new assets become available, or visual identity changes.

## Goal

Keep brand profiles current without requiring full re-onboarding. Brands evolve, and the memory system should reflect that.

## When to Update

- Brand guidelines have changed
- New logo or visual assets added
- Voice/tone refined based on campaign learnings
- Target audience expanded or shifted
- New competitors or positioning changes
- User explicitly requests an update

## Update Process

1. **Identify the brand** — Confirm which brand profile to update
2. **Gather changes** — What's new or different?
3. **Validate consistency** — Ensure changes don't conflict with existing work
4. **Update the profile** — Modify the appropriate sections
5. **Log the change** — Note what changed and why

## What Can Be Updated

| Section | Examples |
|---------|----------|
| Visual Identity | New colors, updated typography, new logo |
| Voice & Tone | Refined style descriptors, new do/don't examples |
| Positioning | Updated differentiator, new key messages |
| Audience | Expanded or narrowed target |
| Assets | New asset locations, updated inventory |

## Update vs. Re-onboard

**Update when:**
- One or two sections need changes
- Core brand identity remains the same
- Quick iteration on positioning

**Re-onboard when:**
- Complete brand refresh/rebrand
- Multiple conflicting changes
- Brand acquired or merged

## Output

Update the brand profile in place: `{project-root}/.pawbytes/creative-suites/brands/{brand-name}/profile.md`

Preserve history by appending a changelog section:

```markdown
## Changelog

### 2026-04-01
- Updated: Added new secondary color palette
- Reason: Brand refresh for spring campaign
```

## Visual Extraction (Optional)

For users without design files or who don't know their brand specs:

1. Use agent-browser to visit their existing website
2. Extract colors from CSS/screenshots
3. Identify typography from rendered pages
4. Capture logo from header/footer
5. Draft profile for confirmation

**Workflow:**
```
User: "I have a website but don't know my brand specs"
Aria: "I can extract your brand from your website. What's the URL?"
[Use agent-browser to analyze the site]
Aria: "Here's what I found: [colors, fonts, logo]. Does this look right?"
[User confirms or corrects]
Aria: "I've updated your brand profile."
```

## Confirmation

After updating, confirm to user:
- "I've updated the {brand} profile with {changes}."
- "Your {brand} profile now includes {new elements}."

## Memory Update

After updating a brand profile:
1. Update `index.md` if this is the active brand
2. Add entry to daily log noting the update
3. Offer to update any in-progress campaigns with the new brand info