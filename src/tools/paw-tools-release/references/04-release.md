---
stage: release
sequence: 4
---

# Stage 4: Release

Create git tag, push to remote, and create GitHub release.

## Pre-Release Summary

Before proceeding, present a summary to the user (or log in headless):

```
Release Summary
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Version:         {previous_version} → {new_version}
Branch:          {current_branch}
Version files:   {count} file(s) updated
Changelog:       {commit_count} commits documented
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

Interactive: Ask for confirmation to proceed.
Headless: Proceed automatically.

## Create Git Tag

```bash
git tag -a v{new_version} -m "Release v{new_version}"
```

For pre-release versions:
```bash
git tag -a v{new_version} -m "Pre-release v{new_version}"
```

## Push Changes

Push in this order:

1. **Version file changes and changelog:**
   ```bash
   git add -A
   git commit -m "chore: release v{new_version}"
   git push origin {current_branch}
   ```

2. **Tag:**
   ```bash
   git push origin v{new_version}
   ```

If push fails (e.g., remote changed), abort and inform user to resolve.

## Create GitHub Release

### Gather Release Notes

Extract the changelog entry for this version (the content between `## [v{new_version}]` and the next version header or end of file).

### Create Draft Release

```bash
gh release create v{new_version} \
  --draft \
  --title "v{new_version}" \
  --notes-file - << 'EOF'
{changelog_content}
EOF
```

For pre-release:
```bash
gh release create v{new_version} \
  --draft \
  --prerelease \
  --title "v{new_version}" \
  --notes-file - << 'EOF'
{changelog_content}
EOF
```

### Verify Release Created

```bash
gh release view v{new_version}
```

### Get Draft URL

Extract and display the draft release URL:

```bash
gh release view v{new_version} --json url --jq .url
```

Present the URL prominently so the user can review:

```
📝 Draft Release Ready for Review
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

{draft_url}

Open this URL to review before publishing.
```

Interactive: Pause and ask if the user wants to open the URL in browser.
Headless: Continue without prompt.

## Completion

Report success:

```
✓ Release v{new_version} created successfully

  • Version files updated
  • Changelog appended
  • Tag pushed to origin
  • Draft ready for review

To publish: gh release edit v{new_version} --draft=false
```

Interactive: Offer to publish the release immediately or keep as draft.
Headless: Leave as draft (safer default).