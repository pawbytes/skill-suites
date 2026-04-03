# Configuration Variables

This reference documents all configuration variables for Prodig Suites.

## Module Settings

These settings control default behavior across all Prodig Suites skills.

### product_default_mode

| Property | Value |
|----------|-------|
| Prompt | "What product family should Prodig Suites assume by default when the user is vague?" |
| Default | `knowledge` |
| Options | `knowledge`, `template`, `software`, `service` |
| User Setting | No |

**Purpose:** When a user says "I want to create a product about X" without specifying the type, this default is used to route to the appropriate executor.

**When to change:**
- If you primarily create one type of product (e.g., you're a course creator → set to `knowledge`)
- If you're building a SaaS studio → set to `software`
- If you productize services → set to `service`

**Example values:**
- `knowledge` — Assume courses, ebooks, memberships
- `template` — Assume templates, prompt packs, digital kits
- `software` — Assume SaaS, apps, AI tools
- `service` — Assume productized services, consulting packages

---

### product_quality_bar

| Property | Value |
|----------|-------|
| Prompt | "What quality bar should the suite optimize for by default?" |
| Default | `production-ready` |
| Options | `draft`, `production-ready`, `publish-ready`, `sellable-ready` |
| User Setting | No |

**Purpose:** Sets the default quality standard for all generated outputs. Skills will aim for this level unless overridden per product.

**Quality Bar Definitions:**

| Level | Definition |
|-------|------------|
| `draft` | Complete structure with placeholder content — good for early iteration |
| `production-ready` | Complete, no placeholders, usable by intended audience |
| `publish-ready` | Polished, formatted, ready for publication without editing |
| `sellable-ready` | Complete, polished, ready to sell immediately |

**When to change:**
- Set to `draft` for rapid prototyping and iteration
- Set to `publish-ready` if you publish directly without review
- Set to `sellable-ready` if you sell products immediately after creation

**Impact on behavior:**
- Higher bars trigger more review cycles
- Higher bars generate more complete initial drafts
- Lower bars allow faster iteration

---

### product_output_style

| Property | Value |
|----------|-------|
| Prompt | "What output style should generated product artifacts default to?" |
| Default | `structured-practical` |
| Options | `structured-practical`, `narrative-engaging`, `technical-detailed` |
| User Setting | No |

**Purpose:** Controls the default voice and structure of generated content.

**Style Definitions:**

| Style | Description | Best For |
|-------|-------------|----------|
| `structured-practical` | Clear sections, actionable, ready to use | Courses, templates, guides |
| `narrative-engaging` | Story-driven, conversational, engaging | Ebooks, courses, memberships |
| `technical-detailed` | Comprehensive, thorough, documentation-heavy | Software, technical guides |

**When to change:**
- Set to `narrative-engaging` for consumer-facing content
- Set to `technical-detailed` for developer tools, APIs, software docs
- Keep `structured-practical` for most business products

**Impact on behavior:**
- Affects how content is structured
- Changes tone and language complexity
- Influences depth vs. breadth trade-offs

---

### research_depth

| Property | Value |
|----------|-------|
| Prompt | "How deep should research runs be by default?" |
| Default | `standard` |
| Options | `quick`, `standard`, `deep` |
| User Setting | No |

**Purpose:** Controls the thoroughness of research operations.

**Depth Definitions:**

| Depth | Description | Time Impact |
|-------|-------------|-------------|
| `quick` | Fast surface scan, top results only | Fastest |
| `standard` | Balanced depth, multiple sources | Moderate |
| `deep` | Comprehensive, exhaustive coverage | Slowest |

**When to change:**
- Set to `quick` for well-known markets or rapid iteration
- Set to `deep` for new markets, high-stakes products, or competitive spaces
- Keep `standard` for most products

**Impact on behavior:**
- Affects how many sources are consulted
- Changes depth of competitor analysis
- Influences validation thoroughness

---

## Core Settings (Inherited)

These settings come from the Pawbytes ecosystem core config and are shared across all modules.

### user_name

| Property | Value |
|----------|-------|
| Prompt | "What should I call you?" |
| Default | `Pawbytes` |
| User Setting | Yes (in config.user.yaml) |

**Purpose:** Personalizes interactions. The orchestrator and all agents will address you by name.

---

### communication_language

| Property | Value |
|----------|-------|
| Prompt | "Language for agent responses?" |
| Default | `English` |
| User Setting | Yes (in config.user.yaml) |

**Purpose:** All agent responses will be in this language.

---

## Path Variables

These paths are automatically configured but can be overridden.

### Output Paths

| Variable | Default |
|----------|---------|
| Sidecar Memory | `{project-root}/.pawbytes/prodig-suites/memory/paw-ps-sidecar/` |
| Products | `{project-root}/.pawbytes/prodig-suites/products/` |
| Artifacts | `{project-root}/.pawbytes/prodig-suites/artifacts/` |

**Note:** `{project-root}` is a literal token resolved at runtime.

---

## Configuration Priority

When collecting configuration, values are resolved in this order (highest priority first):

1. **User-provided values** — From command arguments or interactive input
2. **Existing config values** — From previous setup (for updates)
3. **Module defaults** — From `module.yaml`

## Updating Configuration

To change configuration after initial setup:

1. Run `/paw-ps-setup` again
2. Provide only the values you want to change
3. Confirm the update

Or manually edit:
- `{project-root}/.pawbytes/config/config.yaml` for module settings
- `{project-root}/.pawbytes/config/config.user.yaml` for personal settings