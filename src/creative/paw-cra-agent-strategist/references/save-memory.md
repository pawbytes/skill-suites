# Save Memory

Explicitly save work to the shared agency memory.

## When to Save

Save memory after completing:
- Research reports (competitor, content, trends)
- Scripts and copy drafts
- Content calendars
- Any strategic artifact

## Save Process

1. Determine the correct output path from the memory structure
2. Write the artifact with proper frontmatter:
   ```markdown
   ---
   created: YYYY-MM-DDTHH:MM:SSZ
   brand: {brand-name}
   campaign: {campaign-name} (if applicable)
   type: research | script | copy | calendar
   ---
   ```
3. Append to daily activity log: `{project-root}/.pawbytes/creative-suites/daily/YYYY-MM-DD.md`
4. If this completes a campaign milestone, update `index.md`

## Artifact Quality

Before saving, ensure:
- Research is cited (include source URLs)
- Scripts have scene/take structure
- Copy is platform-optimized
- Calendars have dates and themes

## No Redundant Saves

If an artifact exists, consider whether to:
- Append new findings
- Create a dated version
- Update in place (with change notes)