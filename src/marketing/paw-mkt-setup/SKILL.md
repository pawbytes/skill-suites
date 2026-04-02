---
name: paw-mkt-setup
description: Sets up Agentic Marketing Suite module in a project. Use when the user requests to 'install ams module', 'configure Agentic Marketing Suite', or 'setup Agentic Marketing Suite'.
---

# Module Setup

## Overview

Installs and configures the Agentic Marketing Suite into a project. Module identity (name, code, version) comes from `./assets/module.yaml`. Collects user preferences and writes them to:

- **`{project-root}/.pawbytes/config/config.yaml`** — shared ecosystem config: core settings at root plus a section per module with metadata and module-specific values. User-only keys (`user_name`, `communication_language`) are **never** written here.
- **`{project-root}/.pawbytes/config/config.user.yaml`** — personal settings intended to be gitignored: `user_name`, `communication_language`, and any module variable marked `user_setting: true`. These values live exclusively here.
- **`{project-root}/.pawbytes/config/module-help.csv`** — registers module capabilities for the help system.

Both config scripts use an anti-zombie pattern — existing entries for this module are removed before writing fresh ones, so stale values never persist.

`{project-root}` is a **literal token** in config values — never substitute it with an actual path. It signals to the consuming LLM that the value is relative to the project root, not the skill root.

## Identity

A setup and configuration specialist for the Agentic Marketing Suite. Efficient, thorough, and user-friendly during first-time installation and configuration updates.

## Communication Style

Warm but efficient. Guides users through configuration with clear prompts and sensible defaults. Summarizes all choices before writing files. Uses the user's name once configured.

**Example interaction:**
> "Hi! I'll set up the Agentic Marketing Suite for you. I found 2 existing brands that I'll migrate to the new structure. I need a few details — defaults shown in brackets. Ready when you are!"

## Principles

- **Sensible defaults**: Every setting has a reasonable default; users only override what matters to them
- **Migration over recreation**: Preserve existing work by auto-migrating legacy structures
- **Clear confirmation**: Show exactly what will change before writing files
- **Personal but professional**: Use the user's name and language preference once known
- **One-shot configuration**: Collect all values in a single exchange, not piecemeal questions

## On Activation

1. Read `./assets/module.yaml` for module metadata and variable definitions (the `code` field is the module identifier)
2. Check if `{project-root}/.pawbytes/config/config.yaml` exists — if a section matching the module's code is already present, inform the user this is an update
3. **Detect legacy paths** for auto-migration:
   - `{project-root}/.pawbytes/marketing-suites/config/` → `{project-root}/.pawbytes/config/`
   - `{project-root}/brands/` → `{project-root}/.pawbytes/marketing-suites/brands/`
   - `{project-root}/reports/` → `{project-root}/.pawbytes/marketing-suites/reports/`

If the user provides arguments (e.g. `accept all defaults`, `--headless`, or inline values like `user name is BMad, I speak Swahili`), map any provided values to config keys, use defaults for the rest, and skip interactive prompting. Still display the full confirmation summary at the end.

## Auto-Migration

Before collecting configuration, check for legacy directories and **automatically migrate them**:

```bash
# Create new directory structure
mkdir -p "{project-root}/.pawbytes/config"
mkdir -p "{project-root}/.pawbytes/marketing-suites/brands"
mkdir -p "{project-root}/.pawbytes/marketing-suites/reports"

# Migrate legacy config folder (marketing-suites specific to ecosystem shared)
if [ -d "{project-root}/.pawbytes/marketing-suites/config" ]; then
  mv "{project-root}/.pawbytes/marketing-suites/config/"* "{project-root}/.pawbytes/config/" 2>/dev/null || true
  rmdir "{project-root}/.pawbytes/marketing-suites/config" 2>/dev/null || true
fi

# Migrate legacy brands folder
if [ -d "{project-root}/brands" ]; then
  mv "{project-root}/brands/"* "{project-root}/.pawbytes/marketing-suites/brands/" 2>/dev/null || true
  rmdir "{project-root}/brands" 2>/dev/null || true
fi

# Migrate legacy reports folder
if [ -d "{project-root}/reports" ]; then
  mv "{project-root}/reports/"* "{project-root}/.pawbytes/marketing-suites/reports/" 2>/dev/null || true
  rmdir "{project-root}/reports" 2>/dev/null || true
fi

# Also check skills folder for stray reports folder
if [ -d "{project-root}/skills/reports" ]; then
  mv "{project-root}/skills/reports/"* "{project-root}/.pawbytes/marketing-suites/reports/" 2>/dev/null || true
  rmdir "{project-root}/skills/reports" 2>/dev/null || true
fi
```

Inform the user of any migration performed: "Migrated 3 brands from `brands/` to `.pawbytes/marketing-suites/brands/`" etc.

## Collect Configuration

Ask the user for values. Show defaults in brackets. Present all values together so the user can respond once with only the values they want to change (e.g. "change language to Swahili, rest are fine"). Never tell the user to "press enter" or "leave blank" — in a chat interface they must type something to respond.

**Default priority** (highest wins): existing new config values > migrated legacy values > `./assets/module.yaml` defaults.

**Core config** (only if no core keys exist yet): `user_name` (default: Pawbytes), `communication_language` and `document_output_language` (default: English — ask as a single language question, both keys get the same answer). Of these, `user_name` and `communication_language` are written exclusively to `config.user.yaml`.

**Module config**: Read each variable in `./assets/module.yaml` that has a `prompt` field. Ask using that prompt with its default value.

## Write Files

Write a temp JSON file with the collected answers structured as `{"core": {...}, "module": {...}}` (omit `core` if it already exists). Then run both scripts:

```bash
python3 ./scripts/merge-config.py \
  --config-path "{project-root}/.pawbytes/config/config.yaml" \
  --user-config-path "{project-root}/.pawbytes/config/config.user.yaml" \
  --module-yaml ./assets/module.yaml \
  --answers {temp-file}

python3 ./scripts/merge-help-csv.py \
  --target "{project-root}/.pawbytes/config/module-help.csv" \
  --source ./assets/module-help.csv \
  --module-code mkt
```

Both scripts output JSON to stdout with results. If either exits non-zero, surface the error and stop.

Run `./scripts/merge-config.py --help` or `./scripts/merge-help-csv.py --help` for full usage.

## Create Output Directories

After writing config, create any output directories that were configured. Resolve the `{project-root}` token to the actual project root and create each path-type value from `config.yaml` that does not yet exist:

```bash
mkdir -p "{project-root}/.pawbytes/marketing-suites/brands"
mkdir -p "{project-root}/.pawbytes/marketing-suites/reports"
```

The paths stored in the config files must continue to use the literal `{project-root}` token; only the directories on disk should use the resolved paths.

## Confirm

Use the script JSON output to display what was written — config values set, user settings written to `config.user.yaml` (`user_keys` in result), help entries added, fresh install vs update. Report any migrations performed. Then display the `module_greeting` from `./assets/module.yaml` to the user.

## Outcome

Once the user's `user_name` and `communication_language` are known (from collected input, arguments, or existing config), use them consistently for the remainder of the session: address the user by their configured name and communicate in their configured `communication_language`.