---
name: paw-wbc-setup
description: Sets up Webinar Creator Suite module in a project. Use when the user requests to 'install webinar module', 'configure Webinar Creator Suite', or 'setup webinar tools'.
---

# Webinar Creator Suite Setup

## Overview

Installs and configures the Webinar Creator Suite module into a project. This module is a guided pipeline that takes solo creators from a vague webinar idea to a production-ready slide deck outline and script.

Creates the output directory structure and orientation files:

- **`{project-root}/paw-suites/webinars/`** — module root (`{suite-root}`), with a generated `README.md` listing every webinar
- **`_memory/index.md`** — orientation file tracking webinars and status (agent memory)
- **`_memory/daily/`** — daily activity logs
- **`{webinar-slug}/`** — one workspace per webinar, directly under the root, each with a `README.md` dashboard

`{suite-root}` is config `wbc.output_folder`, default `{project-root}/paw-suites/webinars`; older releases used `{project-root}/.pawbytes/webinar-suites/` with a `webinars/` layer (see Migrate Legacy Files).

`{project-root}` is a **literal token** in config values — never substitute it with an actual path. It signals to the consuming LLM that the value is relative to the project root. `{skill-root}` is this skill's folder; run its scripts as `uv run {skill-root}/scripts/<name>.py`.

## Principles

- **Idempotent setup**: Running setup multiple times should not destroy existing work
- **Minimal configuration**: Only collect essential config; inherit from core Pawbytes settings where possible
- **Clear confirmation**: Always show what was created before completing
- **Respect existing config**: Never overwrite user preferences without explicit consent

## On Activation

1. Read `./assets/module.yaml` for module metadata
2. Run `uv run {skill-root}/scripts/paw-paths.py detect` — mode `new`, `legacy` or `both` means this is an update; inform the user
3. Check for core Pawbytes config at `{project-root}/.pawbytes/config/config.yaml`

If the user provides arguments (e.g. `accept all defaults`, `--headless`), skip interactive prompting and use defaults.

**Inline value mapping:** Users can also provide specific values inline using natural language (following Pawbytes convention). Parse key-value pairs from the invocation and apply them directly:

- "my name is Alice" → `user_name: Alice`
- "use Indonesian" → `communication_language: Indonesian`
- "user name is Alice, language is Indonesian" → Apply both values

This allows non-interactive setup with custom values without requiring full flag syntax.

## Collect Configuration

This module has no prompted variables beyond core Pawbytes settings; `output_folder` keeps its `./assets/module.yaml` default (`{project-root}/paw-suites/webinars`) unless the user names another folder. Only collect core config if not already present:

**Core config** (only if no core keys exist yet):
- `user_name` (default: Pawbytes)
- `communication_language` (default: English)
- `document_output_language` (default: English — same as communication_language)

These values are written to `{project-root}/.pawbytes/config/config.user.yaml` (user_name, communication_language, and document_output_language).

Ask using prompts with defaults in brackets. Present all values together so the user can respond once with only the values they want to change.

## Create Output Directories

Create the module directory structure:

```bash
mkdir -p "{project-root}/paw-suites/webinars/_memory/daily"
```

## Create Orientation File

If `_memory/index.md` does not exist yet (and none is about to be migrated), create `{project-root}/paw-suites/webinars/_memory/index.md` with initial content:

```markdown
# Webinar Creator Suite

## Active Webinars

| Webinar | Status | Last Updated |
|---------|--------|--------------|
| (none)  |        |              |

## Quick Reference

- **Workflow:** `paw-wbc-webinar-creation` — Guided pipeline from idea to deliverables
- **Discovery Agent:** `paw-wbc-agent-discovery` — Research, hooks, angle selection
- **Producer Agent:** `paw-wbc-agent-producer` — Slide deck outline, script writing

## Directory Structure

```
{webinar-slug}/
  ├── README.md             # Dashboard: Status, Next, file links
  ├── brief.md              # Initial brief + audience context
  ├── research-context.md   # Compressed research findings
  ├── hook-selected.md      # Chosen hook + reasoning
  ├── slide-deck-outline.md # LLM-ready slide structure
  ├── script.md             # Full + partial script
  └── recommendations.md    # Surfaced insights to consider

_memory/
  ├── index.md              # This file
  └── daily/YYYY-MM-DD.md   # Daily activity log
```
```

## Write Config

If core config was collected, write to:

- `{project-root}/.pawbytes/config/config.yaml` — core keys if they don't exist, plus `output_folder` in the `wbc` section
- `{project-root}/.pawbytes/config/config.user.yaml` — for user_name, communication_language, and document_output_language

Register module in `{project-root}/.pawbytes/config/module-help.csv` if it exists.

## Migrate Legacy Files

When `detect` reports `legacy` or `both`, run `uv run {skill-root}/scripts/paw-paths.py plan`, show its `summary` along with any conflicts, and run `paw-paths.py apply` once the user confirms. It moves `index.md` and `daily/` into `_memory/`, lifts each `webinars/{webinar-slug}/` to `{webinar-slug}/`, and rewrites the old default `wbc.output_folder`. Report what moved and what stayed (`MOVED.md` in the old folder lists it). Give each moved webinar that lacks a `README.md` a dashboard (title, `Status:` from its brief's status checklist, `Next:`, file links), then run `paw-paths.py index`.

## Confirm

Display what was created — directories, orientation file, fresh install vs update, and any migration. Then display the `greeting` from `./assets/module.yaml` to the user.

## Outcome

Once the user's `user_name` and `communication_language` are known (from collected input, arguments, or existing config), use them consistently for the remainder of the session: address the user by their configured name and communicate in their configured language.

## Output Contract

Once setup completes, the following are guaranteed:

- **Action type**: Module installation/configuration
- **Files created**:
  - `{project-root}/paw-suites/webinars/` directory and its generated `README.md`
  - `_memory/index.md` orientation file
  - `_memory/daily/` directory
  - `{project-root}/.pawbytes/config/config.user.yaml` (if core config collected)
- **Recommendations**: Suggest running `paw-wbc-webinar-creation` to start first webinar