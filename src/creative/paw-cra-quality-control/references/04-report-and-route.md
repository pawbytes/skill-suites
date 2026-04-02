# Stage 4: Report & Route

Compile the final QA report, create revision tickets for failed assets, update campaign status, and log the results.

## Goal

Produce a clear, actionable report and ensure failures get routed back to the right production workflow for rework.

## Finalize QA Report

Update the `qa-report.md` that has been built progressively through stages 1-3. Add the summary section at the top (after front matter) and the revision tickets section at the bottom.

### Summary Section

```markdown
## Summary

| Metric | Value |
|--------|-------|
| Total Assets | {count} |
| Passed | {count} |
| Failed | {count} |
| Critical Issues | {count} |
| Warnings | {count} |
| Info Notes | {count} |
| Cross-Asset Cohesion | {STRONG / ACCEPTABLE / WEAK} |
| **Campaign Verdict** | **QC-APPROVED / REVISIONS-REQUIRED** |
```

### Revision Tickets

For each asset that failed (has critical issues), generate a revision ticket:

```markdown
## Revision Tickets

### REV-001: {asset-filename}
- **Owner:** {producing workflow, e.g., cra-design-social}
- **Asset:** {file path}
- **Platform:** {target platform}
- **Issues:**
  - [CRITICAL] {specific issue with actionable fix description}
  - [WARNING] {specific issue with recommendation}
- **Action Required:** {clear description of what needs to change}
- **Priority:** {HIGH if multiple criticals, MEDIUM if single critical, LOW if warnings only}
```

Revision tickets should contain enough context for the production workflow to fix the issue without re-reading the full report. Be specific: "headline text overflows the safe zone by ~40px on the right side" not "text overflow detected."

### Update Front Matter

Set the final status in the report front matter:

```yaml
status: 'complete'
verdict: 'approved' # or 'revisions-required'
completed: '{timestamp}'
updated: '{timestamp}'
passed: {count}
failed: {count}
critical_count: {count}
warning_count: {count}
```

## Save Report

Write `qa-report.md` to the campaign folder:
`{campaign-folder}/qa-report.md`

## Approval Routing

**If all assets pass (verdict: approved):**
1. Update campaign `status.md` to reflect QC-approved state
2. Note in the report that the campaign is ready for the next step (multi-platform export or delivery)
3. In interactive mode, inform the user and suggest invoking `paw-cra-multi-platform-export` or `paw-cra-agent-account-manager` for packaging

**If any assets fail (verdict: revisions-required):**
1. Update campaign `status.md` to reflect revisions-required state with ticket count
2. In interactive mode, present the revision tickets and ask whether to route them back now
3. In headless mode, write the tickets and log the routing instruction

Routing revision tickets means documenting which production workflow needs to re-process which asset. The revision ticket's `Owner` field identifies the workflow. In practice, the user or Aria will re-invoke that workflow with the revision context.

## Status Update

Append QC results to:

1. **Campaign status** --- `{campaign-folder}/status.md`
   ```markdown
   ## {timestamp} - Quality Control
   - Verdict: {approved / revisions-required}
   - Passed: {count}/{total}
   - Revision tickets: {count}
   - Report: qa-report.md
   ```

2. **Daily log** --- `{project-root}/.pawbytes/creative-suites/daily/{YYYY-MM-DD}.md`
   ```markdown
   ## {timestamp} [QC] Campaign: {campaign-name}
   - Verdict: {verdict}
   - Assets checked: {total}
   - Issues: {critical} critical, {warning} warnings
   ```

## Completion

Present the results to the user (interactive) or exit cleanly (headless). Include:
- Campaign verdict (approved or revisions-required)
- Count summary (passed/failed/issues)
- Location of the full report
- Next recommended action
