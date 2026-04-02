---
name: paw-tools-setup
description: Sets up Pawbytes Tools module in a project. Use when the user requests to 'install paw tools', 'configure Pawbytes Tools', or 'setup utility tools'.
---

# Pawbytes Tools Setup

## Overview

Installs and configures Pawbytes Tools module into a project. Collects user preferences and writes them to:

- **`{project-root}/.pawbytes/config/config.yaml`** — shared Pawbytes ecosystem configuration
- **`{project-root}/.pawbytes/config/config.user.yaml`** — personal settings (gitignored, contains API keys)

`{project-root}` is a **literal token** in config values — never substitute it with an actual path. It signals to the consuming LLM that the value is relative to the project root.

## On Activation

1. Read `./assets/module.yaml` for module metadata and variable definitions
2. Check if `{project-root}/.pawbytes/config/config.yaml` exists — if present, inform the user this is an update

If the user provides arguments (e.g. `accept all defaults`, `--headless`, or inline values), map provided values to config keys, use defaults for the rest, and skip interactive prompting.

## Collect Configuration

Ask the user for values. Show defaults in brackets. Present all values together so the user can respond once with only the values they want to change (e.g. "change language to Swahili, rest are fine"). Never tell the user to "press enter" or "leave blank" — in a chat interface they must type something to respond.

**Default priority** (highest wins): existing config values > `./assets/module.yaml` defaults.

**Module config**: Read each variable in `./assets/module.yaml` that has a `prompt` field. Ask using that prompt with its default value (or existing value if available).

## Write Files

Write the collected configuration to:

```
{project-root}/.pawbytes/config/config.yaml
```

User-specific settings (API keys) go to:

```
{project-root}/.pawbytes/config/config.user.yaml
```

Create directories if they don't exist.

## Create Output Directories

After writing config, create any output directories that were configured. Resolve the `{project-root}` token to the actual project root and create each path-type value that does not yet exist. Use `mkdir -p` or equivalent.

## Confirm

Display what was written — config values set, fresh install vs update. Then display the `greeting` from `./assets/module.yaml` to the user.

## Outcome

Once the user's `communication_language` is known (from collected input, arguments, or existing config), use it consistently for the remainder of the session.