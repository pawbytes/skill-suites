---
stage: changelog
sequence: 3
---

# Stage 3: Changelog

Generate a changelog entry from commits and append to CHANGELOG.md.

## Commit Analysis

### Get Commits Since Last Release

```bash
git log <previous-tag>..HEAD --pretty=format:"%h %s" --no-merges
```

If no previous tag:
```bash
git log --pretty=format:"%h %s" --no-merges
```

### Parse and Group Commits

Run `./scripts/parse_commits.py --format changelog <commit-range>` to get grouped commits.

Groups follow [Keep a Changelog](https://keepachangelog.com/) categories:

| Category | Prefixes |
|----------|----------|
| Breaking Changes | `breaking:`, `!:` |
| Features | `feat:` |
| Bug Fixes | `fix:` |
| Documentation | `docs:` |
| Performance | `perf:` |
| Refactoring | `refactor:` |
| Tests | `test:` |
| Chores | `chore:`, `build:`, `ci:` |

### Handling Non-Conventional Commits

Commits without conventional prefixes:
- Group under "Other Changes" section
- Include as-is (the LLM can clean up wording if needed)

## Generate Changelog Entry

Format follows Keep a Changelog:

```markdown
## [<version>] - <date>

### Breaking Changes
- **Scope:** Description of breaking change (#pr-number)
- Description without scope (#pr-number)

### Features
- **Scope:** Description (#pr-number)

### Bug Fixes
- **Scope:** Description (#pr-number)

### Other Changes
- Commit message as-is
```

### Enhancing Commit Messages

The LLM should clean up commit messages for readability:
- Remove trivial prefixes if they don't add value
- Make descriptions more informative if the original was terse
- Add scope/context if apparent from the changes

Do NOT fabricate changes. Only enhance clarity of existing information.

## Update CHANGELOG.md

### File Exists

1. Read current CHANGELOG.md
2. Find the first version header (e.g., `## [1.2.0]`)
3. Insert new entry before it
4. Write updated file

### File Doesn't Exist

Create new CHANGELOG.md with standard header:

```markdown
# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [<version>] - <date>

<generated content>
```

## Progression

When CHANGELOG.md is updated, proceed to `./references/04-release.md`.