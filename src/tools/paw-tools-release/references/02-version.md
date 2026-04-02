---
stage: version
sequence: 2
---

# Stage 2: Version

Determine the new version and update all version files.

## Determine Version

### If User Specified Version

Use the version from `--version` argument directly. Validate it's valid semver.

### If Auto-Detecting

1. Get the latest tag:
   ```bash
   git describe --tags --abbrev=0 2>/dev/null || echo "NO_TAGS"
   ```

2. If `NO_TAGS`:
   - Interactive: Ask user for initial version (default: `0.1.0`)
   - Headless: Use `0.1.0`

3. If tag exists, analyze commits since that tag:
   ```bash
   git log <previous-tag>..HEAD --oneline
   ```

4. Run `./scripts/parse_commits.py` to analyze commit types.

5. Apply version bump logic:
   | Commit Type | Bump |
   |-------------|------|
   | `breaking:` or `!:` | Major (1.0.0 → 2.0.0) |
   | `feat:` | Minor (1.0.0 → 1.1.0) |
   | `fix:`, `docs:`, `chore:`, etc. | Patch (1.0.0 → 1.0.1) |

6. If multiple commit types, use highest bump level.

### Pre-Release Versions

If `--pre-release <label>` specified:
- Append label to version: `1.2.0-beta.1`
- Auto-increment pre-release number if same label exists

## Detect and Update Version Files

Run `./scripts/detect_version_files.py {project-root}` to find all version files.

For each detected file, update the version:

| File Type | Field/Pattern |
|-----------|---------------|
| `package.json` | `"version": "x.x.x"` |
| `Cargo.toml` | `version = "x.x.x"` |
| `pyproject.toml` | `version = "x.x.x"` |
| `VERSION` | entire file content |
| `__version__.py` | `__version__ = "x.x.x"` |
| `setup.py` | `version="x.x.x"` |

### Verification

After updates, verify all files were updated correctly:
```bash
grep -r "<new-version>" --include="package.json" --include="Cargo.toml" ...
```

## Output

Set `{new_version}` and `{previous_version}` variables for subsequent stages.

## Progression

When version is determined and files updated, proceed to `./references/03-changelog.md`.