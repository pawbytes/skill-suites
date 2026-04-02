---
name: paw-wbc-setup
description: Sets up Webinar Creator Suite module in a project. Use when the user requests to 'install webinar module', 'configure Webinar Creator Suite', or 'setup webinar tools'.
---

# Webinar Creator Suite Setup

## Overview

Installs and configures the Webinar Creator Suite module into a project. This module is a guided pipeline that takes solo creators from a vague webinar idea to a production-ready slide deck outline and script.

Creates the output directory structure and orientation files:

- **`{project-root}/.pawbytes/webinar-suites/`** — module root
- **`{project-root}/.pawbytes/webinar-suites/index.md`** — orientation file tracking webinars and status
- **`{project-root}/.pawbytes/webinar-suites/webinars/`** — webinar workspaces
- **`{project-root}/.pawbytes/webinar-suites/daily/`** — daily activity logs

`{project-root}` is a **literal token** in config values — never substitute it with an actual path. It signals to the consuming LLM that the value is relative to the project root.

## Principles

- **Idempotent setup**: Running setup multiple times should not destroy existing work
- **Minimal configuration**: Only collect essential config; inherit from core Pawbytes settings where possible
- **Clear confirmation**: Always show what was created before completing
- **Respect existing config**: Never overwrite user preferences without explicit consent

## On Activation

1. Read `./assets/module.yaml` for module metadata
2. Check if `{project-root}/.pawbytes/webinar-suites/` exists — if present, inform the user this is an update
3. Check for core Pawbytes config at `{project-root}/.pawbytes/config/config.yaml`

If the user provides arguments (e.g. `accept all defaults`, `--headless`), skip interactive prompting and use defaults.

## Collect Configuration

This module has no custom configuration variables beyond core Pawbytes settings. Only collect core config if not already present:

**Core config** (only if no core keys exist yet):
- `user_name` (default: Pawbytes)
- `communication_language` (default: English)
- `document_output_language` (default: English — same as communication_language)

These values are written to `{project-root}/.pawbytes/config/config.user.yaml`.

Ask using prompts with defaults in brackets. Present all values together so the user can respond once with only the values they want to change.

## Create Output Directories

Create the module directory structure:

```bash
mkdir -p "{project-root}/.pawbytes/webinar-suites/webinars"
mkdir -p "{project-root}/.pawbytes/webinar-suites/daily"
```

## Create Orientation File

Create `{project-root}/.pawbytes/webinar-suites/index.md` with initial content:

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
webinars/{webinar-slug}/
  ├── brief.md              # Initial brief + audience context
  ├── research-context.md   # Compressed research findings
  ├── hook-selected.md      # Chosen hook + reasoning
  ├── slide-deck-outline.md # LLM-ready slide structure
  ├── script.md             # Full + partial script
  └── recommendations.md    # Surfaced insights to consider

daily/
  └── YYYY-MM-DD.md         # Daily activity log
```
```

## Write Config

If core config was collected, write to:

- `{project-root}/.pawbytes/config/config.yaml` — if core section doesn't exist
- `{project-root}/.pawbytes/config/config.user.yaml` — for user_name and communication_language

Register module in `{project-root}/.pawbytes/config/module-help.csv` if it exists.

## Confirm

Display what was created — directories, orientation file, fresh install vs update. Then display the `greeting` from `./assets/module.yaml` to the user.

## Outcome

Once the user's `user_name` and `communication_language` are known (from collected input, arguments, or existing config), use them consistently for the remainder of the session: address the user by their configured name and communicate in their configured language.

## Output Contract

Once setup completes, the following are guaranteed:

- **Action type**: Module installation/configuration
- **Files created**:
  - `{project-root}/.pawbytes/webinar-suites/` directory
  - `{project-root}/.pawbytes/webinar-suites/index.md` orientation file
  - `{project-root}/.pawbytes/webinar-suites/webinars/` directory
  - `{project-root}/.pawbytes/webinar-suites/daily/` directory
  - `{project-root}/.pawbytes/config/config.user.yaml` (if core config collected)
- **Recommendations**: Suggest running `paw-wbc-webinar-creation` to start first webinar