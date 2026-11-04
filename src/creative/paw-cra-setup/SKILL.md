---
name: paw-cra-setup
description: Sets up Pawbytes Creative Suites module in a project. Use when the user requests to 'install creative suites', 'configure creative suites', 'setup creative suites', or 'paw-cra setup'.
---

# Pawbytes Creative Suites Setup

## Overview

Installs and configures the Pawbytes Creative Suites module into a project. Module identity (name, code, version) comes from `./assets/module.yaml`. Collects user preferences and writes them to the Pawbytes ecosystem config:

- **`{project-root}/.pawbytes/config/config.yaml`** — shared project config: core settings at root plus a `cra:` section with module-specific values.
- **`{project-root}/.pawbytes/config/config.user.yaml`** — personal settings intended to be gitignored: API keys and any variable marked `user_setting: true` in `./assets/module.yaml`. These values live exclusively here.
- **`{project-root}/.pawbytes/config/module-help.csv`** — registers module capabilities for the help system.

Both config scripts use an anti-zombie pattern — existing entries for this module are removed before writing fresh ones, so stale values never persist.

`{project-root}` is a **literal token** in config values — never substitute it with an actual path. It signals to the consuming LLM that the value is relative to the project root, not the skill root.

## On Activation

1. Read `./assets/module.yaml` for module metadata and variable definitions (the `code` field `cra` is the module identifier)
2. Check if `{project-root}/.pawbytes/config/config.yaml` exists — if a `cra:` section is already present, inform the user this is an update
3. Run `uv run ./scripts/paw-paths.py --project-root {project-root} detect`. If it reports `mode: legacy` or `both`, tell the user their files are still in the old `.pawbytes/creative-suites/` tree; the migration step below moves them to `paw-suites/creative/`.

If the user provides arguments (e.g. `accept all defaults`, `--headless`, or inline values like `user name is Alice, fal key is abc123`), map any provided values to config keys, use defaults for the rest, and skip interactive prompting. Still display the full confirmation summary at the end.

## Collect Configuration

Ask the user for values. Show defaults in brackets. Present all values together so the user can respond once with only the values they want to change (e.g. "change fal_key to abc123, rest are fine"). Never tell the user to "press enter" or "leave blank" — in a chat interface they must type something to respond.

**Default priority** (highest wins): existing config values > `./assets/module.yaml` defaults.

**Core config** (only if no core keys exist yet): `user_name` (default: user), `communication_language` and `document_output_language` (default: English — ask as a single language question, both keys get the same answer). Of these, `user_name` and `communication_language` are written exclusively to `config.user.yaml`.

**Module config**: Read each variable in `./assets/module.yaml` that has a `prompt` field. Ask using that prompt with its default value.

**API Keys** (stored in `config.user.yaml`, not committed):
- `fal_key` — **Required** for image/video generation
- `elevenlabs_api_key` — Optional, for AI voiceover
- `pexels_api_key` — Optional, for stock media research

## Write Files

Write a temp JSON file with the collected answers structured as `{"core": {...}, "module": {...}}`. Then run the config merge script:

```bash
python3 ./scripts/merge-config.py --config-path "{project-root}/.pawbytes/config/config.yaml" --user-config-path "{project-root}/.pawbytes/config/config.user.yaml" --module-yaml ./assets/module.yaml --answers {temp-file}
```

Then register capabilities with the help CSV merge:

```bash
python3 ./scripts/merge-help-csv.py --target "{project-root}/.pawbytes/config/module-help.csv" --source ./assets/module-help.csv --module-code cra
```

Both scripts output JSON to stdout with results. If either exits non-zero, surface the error and stop.

## Migrate Legacy Files

When `detect` reports `legacy` or `both`, run `uv run ./scripts/paw-paths.py --project-root {project-root} plan` and show its `summary` along with any `conflicts`. Explain the messy spots in one line each: root `campaigns/`, `briefs/` and unbranded `output/clips/` go to `brands/unassigned/` (ask the user to move them under the right brand); `brands/{b}/videos/{x}/` folders with `short-form/`, `long-form/`, `clips/`, `audio/` or `series/` inside are treated as campaign `{x}`, any other `videos/{x}/` as a long-form video. Run `uv run ./scripts/paw-paths.py --project-root {project-root} apply` once the user confirms. Report what moved and what stayed (`MOVED.md` in the old folder lists it); `apply` also rewrites `cra.output_directory` when it still holds the old default. Legacy campaign folders keep their names; only new campaigns get the `YYYY-MM-` prefix. Give each migrated brand without a `README.md` one: `# {Brand}`, `Status: migrated`, `Next: {ask the user}`, and relative links to `profile.md`, `guidelines.md` and its campaigns.

## Create Output Directories

After writing config (and any migration), create the suite folders. `{suite-root}` is `cra.output_directory`, default `{project-root}/paw-suites/creative`; resolve the `{project-root}` token for filesystem operations:

```bash
mkdir -p "{suite-root}/brands"
mkdir -p "{suite-root}/_memory/knowledge"
mkdir -p "{suite-root}/_memory/daily"
mkdir -p "{project-root}/.pawbytes/creative/.auth"
```

Then run `uv run ./scripts/paw-paths.py --project-root {project-root} index` to write the suite `README.md`.

## Confirm

Use the script JSON output to display what was written — config values set, user settings written to `config.user.yaml`, help entries added, fresh install vs update. Then display the `greeting` from `./assets/module.yaml`.

## Outcome

Once the user's `user_name` and `communication_language` are known, use them consistently for the remainder of the session: address the user by their configured name and communicate in their configured language.

## File Structure After Setup

```
{project-root}/
  .pawbytes/
    config/
      config.yaml           # Shared config (committed)
      config.user.yaml      # User settings (gitignored)
      module-help.csv       # Capability registry
    creative/.auth/         # Browser sessions (secret, gitignored)
  paw-suites/
    creative/
      README.md             # Suite index (paw-paths.py index)
      _memory/
        index.md            # Agency memory index
        knowledge/          # Research and references
        daily/              # Activity logs
      brands/{brand}/       # Brand dashboards, guidelines, assets, campaigns, designs, videos
```