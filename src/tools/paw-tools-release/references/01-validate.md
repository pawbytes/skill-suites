---
stage: validate
sequence: 1
---

# Stage 1: Validate

Ensure the repository is in a clean, releasable state.

## Checks

Perform these checks in order. All must pass before proceeding.

### 1. Working Tree Status

```bash
git status --porcelain
```

- **Empty output** → Clean, proceed
- **Has output** → Uncommitted changes exist
  - Interactive: Warn and ask whether to abort or let user commit first
  - Headless: Abort with clear message listing changed files

### 2. Current Branch

```bash
git branch --show-current
```

- If `{release_branch}` is configured and current branch doesn't match:
  - Interactive: Warn, offer to switch or override
  - Headless: Abort with message

### 3. Sync with Remote

```bash
git fetch --tags
```

Fetch latest tags to ensure accurate version detection. Compare local and remote:

```bash
git status -uno
```

- **Behind remote** → Interactive: Warn and offer to pull first. Headless: Abort.
- **Ahead of remote** → This is fine, we'll push.
- **Diverged** → Interactive: Warn about divergence. Headless: Abort.

### 4. GitHub CLI Authentication

```bash
gh auth status
```

- **Authenticated** → Proceed
- **Not authenticated** → Guide user to run `gh auth login`, then retry

## Progression

When all checks pass, proceed to `./references/02-version.md`.

If any check fails in headless mode, output a clear error and exit. In interactive mode, offer remediation options.