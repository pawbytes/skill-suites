# Configuration Variables

## Overview

Variables enable portable, user-specific configuration across different environments. They use a token substitution system that resolves at runtime.

## Variable Syntax

Variables are enclosed in curly braces:

```yaml
output_folder: "{project-root}/.pawbytes/marketing-suites"
user_greeting: "Hello, {user_name}!"
```

---

## Built-in Tokens

### Path Tokens

| Token | Description | Example Resolution |
|-------|-------------|-------------------|
| `{project-root}` | Project root directory | `/home/user/my-project` |
| `{output_folder}` | Configured output folder | `/home/user/my-project/.pawbytes/marketing-suites` |
| `{brands_folder}` | Brand storage location | `/home/user/my-project/.pawbytes/marketing-suites/brands` |
| `{reports_folder}` | Report output location | `/home/user/my-project/.pawbytes/marketing-suites/reports` |

### User Tokens

| Token | Description | Source |
|-------|-------------|--------|
| `{user_name}` | User's name | `config.user.yaml` or `config.yaml` |
| `{communication_language}` | Interaction language | `config.yaml` |
| `{document_output_language}` | Document output language | `config.yaml` |
| `{default_brand}` | Default brand slug | `config.yaml` |

### Module Tokens

| Token | Description | Example |
|-------|-------------|---------|
| `{module}` | Module short code | `mkt`, `cra`, `paw` |
| `{module_version}` | Module version | `0.3.7` |

---

## Variable Resolution

### Resolution Order

Variables are resolved in this order:

1. **Built-in tokens** — `{project-root}`, `{module}`
2. **Config values** — Referenced from `config.yaml`
3. **User overrides** — Referenced from `config.user.yaml`

### Example Resolution Chain

```yaml
# config.yaml
output_folder: "{project-root}/.pawbytes/marketing-suites"
brands_folder: "{output_folder}/brands"
```

Resolution:

```
{project-root}           →  /home/user/my-project
{output_folder}          →  /home/user/my-project/.pawbytes/marketing-suites
{brands_folder}          →  /home/user/my-project/.pawbytes/marketing-suites/brands
```

---

## Using Variables in Skills

### Path Construction

Skills use variables to construct output paths:

```markdown
## Path Resolution

- Brand context: `{brands_folder}/{brand-slug}/`
- Campaigns: `{brands_folder}/{brand-slug}/campaigns/{campaign}/`
- Reports: `{reports_folder}/{report-type}-{slug}.md`
```

### Runtime Resolution

When a skill needs an actual path:

1. Read configuration from `.pawbytes/config/config.yaml`
2. Read user overrides from `.pawbytes/config/config.user.yaml`
3. Resolve tokens recursively:
   - Replace `{project-root}` with actual project root
   - Replace other tokens with config values
4. Use resolved path for file operations

---

## Variable Definition in module.yaml

Variables are defined in the `module.yaml` file:

### Simple Variable

```yaml
output_folder:
  prompt: "Where should output be saved?"
  default: "{project-root}/.pawbytes/marketing-suites"
```

### Full Variable Definition

```yaml
brands_folder:
  prompt: "Where should brand contexts be stored?"
  default: "{project-root}/.pawbytes/marketing-suites/brands"
  result: "{value}"
  directories: true      # Create directories during setup
  user_setting: false    # Save to config.yaml (not user config)
```

### Sensitive Variable

```yaml
api_key:
  prompt: "Enter your API key"
  default: ""
  result: "{value}"
  user_setting: true     # Save to config.user.yaml
  sensitive: true        # Don't log the value
```

---

## Variable Fields Reference

| Field | Type | Purpose |
|-------|------|---------|
| `prompt` | string | Question shown to user during setup |
| `default` | any | Default value (can contain tokens) |
| `result` | string | How value is stored (usually `{value}`) |
| `directories` | boolean | Create directories at this path during setup |
| `user_setting` | boolean | Save to `config.user.yaml` instead of `config.yaml` |
| `sensitive` | boolean | Don't log value (for API keys) |
| `required` | boolean | Value must be provided |

---

## Common Patterns

### Output Path Pattern

```yaml
output_folder:
  prompt: "Output directory"
  default: "{project-root}/.pawbytes/{module}"
  directories: true
```

### API Key Pattern

```yaml
fal_api_key:
  prompt: "fal.ai API key (optional)"
  default: ""
  user_setting: true
  sensitive: true
  required: false
```

### User Preference Pattern

```yaml
communication_language:
  prompt: "Language for responses"
  default: "English"
  user_setting: true
```

---

## Token Reference Table

| Category | Token | Example Value |
|----------|-------|---------------|
| **Path** | `{project-root}` | `/home/user/project` |
| **Path** | `{output_folder}` | `{project-root}/.pawbytes/marketing-suites` |
| **Path** | `{brands_folder}` | `{output_folder}/brands` |
| **User** | `{user_name}` | `Jane` |
| **User** | `{communication_language}` | `English` |
| **Module** | `{module}` | `mkt` |
| **Module** | `{module_version}` | `0.3.7` |
| **Brand** | `{default_brand}` | `acme-corp` |

---

## Best Practices

1. **Use tokens for all paths** — Never hardcode absolute paths
2. **Keep tokens in defaults** — Use `{project-root}` in default values
3. **Chain tokens wisely** — `{output_folder}/subdir` inherits portability
4. **Mark sensitive data** — Use `sensitive: true` for API keys
5. **Separate user settings** — Use `user_setting: true` for personal preferences

---

## See Also

- [Config Files](./config-files.md)
- [Module YAML Format](./module-yaml.md)