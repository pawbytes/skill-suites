# Stage 05: Quality Gate & Completion

Run quality control across all produced assets, generate the campaign completion report, and finalize.

## Objective

Invoke cross-skill quality control, generate the campaign summary, route for delivery or export, and finalize the campaign status.

## Quality Gate

Invoke `paw-cra-quality-control` via Agent tool with:
- Campaign path: the campaign folder containing all produced assets
- `design-manifest.json` and `video-manifest.json` as inputs
- Brand guidelines path for brand consistency checks
- `--headless` flag for autonomous QC

**Expected output from QC:** `qa-report.md` with pass/fail per asset, brand compliance status, platform spec validation, and an overall campaign verdict.

### QC Result Handling

- **All pass:** Proceed to campaign summary and delivery routing
- **Some failures:** 
  - If not headless: present failures and ask whether to revise, accept, or escalate to Aria
  - If headless: log failures, mark those assets as `qc-failed` in status, proceed with passing assets
- **Critical failures:** If >50% of assets fail QC, flag the campaign for review regardless of headless mode

## Campaign Summary

Generate the **campaign completion report** — a section in `status.md` that provides a human-readable summary:

```markdown
## Campaign Completion Report

**Campaign:** {campaign-name}
**Brand:** {brand-name}
**Completed:** {date}
**Overall QC:** PASS | PARTIAL | FAIL

### Summary
- Total deliverables: {n}
- Completed: {n}
- QC passed: {n}
- QC failed: {n}
- Skipped/failed: {n}

### Produced Assets
[Organized list of all assets with file paths, platforms, dimensions/duration, and QC status]

### QC Notes
[Summary of any QC findings or revision recommendations]
```

## Delivery Routing

Based on QC results, suggest next steps:

- **If all QC passes and multi-platform variants are needed:** Suggest invoking `paw-cra-multi-platform-export` to generate platform-specific variants (resized images, re-encoded videos with safe zones)
- **If all QC passes and no variants needed:** Campaign is ready for manual delivery — provide the asset folder path and manifest locations
- **If partial QC pass:** Recommend addressing failures before export, or proceeding with passing assets only

If not headless, present options. If headless, log the recommendation in status and daily log.

## Status Finalization

1. Update `status.md` frontmatter:
   - `status: 'complete'` (or `'partial'` if failures exist)
   - `current_stage: '05-quality-completion'`
   - `qc_status: 'pass'` | `'partial'` | `'fail'`
   - `updated: [current ISO-8601]`

2. Append to daily log:
   ```
   [Campaign] Campaign '{campaign-name}' complete. {n}/{total} deliverables passed QC. Assets at: {campaign-folder-path}
   ```

3. Update `{project-root}/.pawbytes/creative-suites/index.md` to reflect campaign completion status.

## Final Output

Present the campaign completion report to the user (or log it if headless). The campaign is now complete.
