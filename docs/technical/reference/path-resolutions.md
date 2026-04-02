# Path Resolutions

Output path patterns and conventions for Pawbytes skills. All skills should follow these patterns to ensure consistent output locations across the ecosystem.

---

## Path Token System

Skills use tokens instead of hardcoded paths. These tokens are resolved at runtime:

| Token | Resolves To |
|-------|-------------|
| `{project-root}` | The root directory of the user's project |
| `{brand-slug}` | Lowercase, hyphenated brand name (e.g., `acme-corp`) |
| `{campaign-slug}` | Lowercase, hyphenated campaign name |
| `{module}` | Module output folder name |

**Important:** Write tokens literally in SKILL.md. Do not substitute actual paths. The consuming LLM resolves tokens at runtime.

---

## Standard Path Structure

```
{project-root}/.pawbytes/
├── config/
│   ├── config.yaml              # Shared ecosystem config
│   └── config.user.yaml         # User-specific settings (gitignored)
│
├── marketing-suites/            # Marketing module outputs
│   ├── brands/
│   │   └── {brand-slug}/
│   │       ├── brand-context.md
│   │       ├── sostac/
│   │       └── campaigns/
│   └── reports/
│
├── creative-suites/             # Creative module outputs
│   ├── index.md                 # Memory entry point
│   ├── brands/
│   │   └── {brand-slug}/
│   │       ├── guidelines.md
│   │       ├── campaigns/
│   │       ├── videos/
│   │       └── exports/
│   └── output/
│
└── tools-output/                # Tools module outputs
    ├── presentations/
    └── releases/
```

---

## Path Patterns by Module

### Marketing (`paw-mkt-*`)

| Output Type | Path Pattern |
|-------------|--------------|
| Brand workspace | `.pawbytes/marketing-suites/brands/{brand-slug}/` |
| Brand context | `.pawbytes/marketing-suites/brands/{brand-slug}/brand-context.md` |
| SOSTAC plans | `.pawbytes/marketing-suites/brands/{brand-slug}/sostac/` |
| Campaigns | `.pawbytes/marketing-suites/brands/{brand-slug}/campaigns/{type}-{campaign-slug}/` |
| Channel content | `.pawbytes/marketing-suites/brands/{brand-slug}/campaigns/{type}-{campaign-slug}/channels/{channel}/` |
| Standalone content | `.pawbytes/marketing-suites/brands/{brand-slug}/channels/{channel}/content/` |
| Status tracking | `.pawbytes/marketing-suites/brands/{brand-slug}/status.md` |
| Reports | `.pawbytes/marketing-suites/reports/` |

**Campaign mode vs Standalone mode:**

Skills should detect or ask whether work is part of a campaign:

```markdown
## Path Resolution

**Campaign mode** -- working within a named campaign:
  - Save to `./.pawbytes/marketing-suites/brands/{brand-slug}/campaigns/{type}-{campaign-slug}/channels/seo/content/`

**Standalone mode** -- evergreen or independent work:
  - Save to `./.pawbytes/marketing-suites/brands/{brand-slug}/channels/seo/content/`

If unsure which mode, ask: "Is this part of a specific campaign, or standalone work?"
```

### Creative (`paw-cra-*`)

| Output Type | Path Pattern |
|-------------|--------------|
| Memory index | `.pawbytes/creative-suites/index.md` |
| Brand workspace | `.pawbytes/creative-suites/brands/{brand-slug}/` |
| Brand guidelines | `.pawbytes/creative-suites/brands/{brand-slug}/guidelines.md` |
| Campaign briefs | `.pawbytes/creative-suites/brands/{brand-slug}/campaigns/{campaign}/brief.md` |
| Social posts | `.pawbytes/creative-suites/brands/{brand-slug}/carousels/` |
| Videos | `.pawbytes/creative-suites/brands/{brand-slug}/videos/` |
| Video manifest | `.pawbytes/creative-suites/brands/{brand-slug}/videos/video-manifest.json` |
| Exports | `.pawbytes/creative-suites/brands/{brand-slug}/exports/` |
| Daily log | `.pawbytes/creative-suites/daily/{YYYY-MM-DD}.md` |
| Knowledge base | `.pawbytes/creative-suites/knowledge/index.md` |

### Tools (`paw-tools-*`)

| Output Type | Path Pattern |
|-------------|--------------|
| Presentations | `.pawbytes/tools-output/presentations/{slugified-title}.html` |
| Releases | `.pawbytes/tools-output/releases/` |
| Reports | `.pawbytes/tools-output/reports/` |

---

## Configuration Paths

### Config File Locations

| File | Path | Purpose |
|------|------|---------|
| Shared config | `.pawbytes/config/config.yaml` | Project-level settings |
| User config | `.pawbytes/config/config.user.yaml` | Personal settings (gitignored) |
| Module help | `.pawbytes/config/module-help.csv` | CLI help entries |

### Config Loading Pattern

Skills should load config in this order (later overrides earlier):

1. Module defaults (from `assets/module.yaml` in setup skill)
2. Project config (`.pawbytes/config/config.yaml`)
3. User overrides (`.pawbytes/config/config.user.yaml`)

**Example On Activation:**
```markdown
## On Activation

Load available config from `{project-root}/.pawbytes/config/config.yaml` and `{project-root}/.pawbytes/config/config.user.yaml` if present. Resolve and apply throughout the session (defaults in parens):

- `{user_name}` (null) -- address the user by name
- `{communication_language}` (English) -- use for all communications
- `{output_directory}` (`.pawbytes/creative-suites`) -- base output path
```

---

## Variable Substitution

### Path Variables

Skills can use these variables in path construction:

| Variable | Source | Example Value |
|----------|--------|---------------|
| `{user_name}` | config.user.yaml | `John` |
| `{communication_language}` | config.user.yaml | `English` |
| `{output_folder}` | config.yaml | `.pawbytes/marketing-suites` |
| `{default_brand}` | config.yaml | `acme-corp` |
| `{fal_key}` | config.user.yaml | API key (sensitive) |

### Substitution Example

In SKILL.md, write:
```markdown
Save outputs to `{project-root}/.pawbytes/marketing-suites/brands/{brand-slug}/`
```

At runtime, the LLM resolves:
```
/path/to/user/project/.pawbytes/marketing-suites/brands/acme-corp/
```

---

## Brand Slug Convention

Brand slugs are used throughout the path system:

**Format:** lowercase, hyphenated, no special characters

| Brand Name | Slug |
|------------|------|
| Acme Corp | `acme-corp` |
| MyBrand | `mybrand` |
| 123 Company | `123-company` |
| Tech & Co. | `tech-co` |

**Implementation:**
```markdown
## Path Resolution

Brand workspace root: `./.pawbytes/marketing-suites/brands/{brand-slug}/`

If no brand slug is known, prompt for brand selection first.
```

---

## Campaign Path Convention

Campaigns follow a structured naming pattern:

**Format:** `{type}-{campaign-slug}`

| Type | Example |
|------|---------|
| Launch | `launch-q1-product` |
| Evergreen | `evergreen-seo-basics` |
| Seasonal | `seasonal-holiday-2024` |
| Event | `event-webinar-series` |

**Path example:**
```
.pawbytes/marketing-suites/brands/acme-corp/campaigns/launch-q1-product/
├── strategy.md
├── channels/
│   ├── seo/
│   ├── email/
│   └── social/
└── reports/
```

---

## Path Resolution Documentation

Every skill should document its output paths in a Path Resolution section:

### Minimum Documentation

```markdown
## Path Resolution

**Brand workspace root**: `./.pawbytes/marketing-suites/brands/{brand-slug}/`

**Campaign coordination**: `./.pawbytes/marketing-suites/brands/{brand-slug}/campaigns/{type}-{campaign-slug}/`

If no brand slug is known, prompt for brand selection first.
```

### Comprehensive Documentation

```markdown
## Path Resolution

**Campaign mode** -- working within a named campaign:
  - Save to `./.pawbytes/marketing-suites/brands/{brand-slug}/campaigns/{type}-{campaign-slug}/channels/seo/content/`
  - Read campaign strategy at `./.pawbytes/marketing-suites/brands/{brand-slug}/campaigns/{type}-{campaign-slug}/strategy.md`

**Standalone mode** -- evergreen or independent work:
  - Save to `./.pawbytes/marketing-suites/brands/{brand-slug}/channels/seo/content/`

**Legacy fallback** -- old directory structure detected:
  - Save to `./.pawbytes/marketing-suites/brands/{brand-slug}/content/seo/`
  - Suggest migration to new structure

If unsure which mode, ask: "Is this part of a specific campaign, or standalone work?"
```

---

## Common Path Patterns

### Coordinator Skills

Coordinator skills manage brand workspaces:

```markdown
## Path Resolution

**Brand workspace root**: `./.pawbytes/marketing-suites/brands/{brand-slug}/`

**SOSTAC plans**: `./.pawbytes/marketing-suites/brands/{brand-slug}/sostac/`

**Campaign coordination**: `./.pawbytes/marketing-suites/brands/{brand-slug}/campaigns/{type}-{campaign-slug}/`

**Progress tracking**: `./.pawbytes/marketing-suites/brands/{brand-slug}/status.md`
```

### Production Skills

Production skills output specific deliverables:

```markdown
## Output

**Location:** `{project-root}/.pawbytes/creative-suites/brands/{brand}/videos/`

**Filename convention:** `{platform}-{topic-slug}-{timestamp}.mp4`

**Manifest:** `video-manifest.json` in same directory
```

### Utility Skills

Utility skills output to tools-output:

```markdown
## Output Artifacts

| Artifact | Location |
|----------|----------|
| Updated version files | Project root (package.json, Cargo.toml, etc.) |
| Changelog entry | `{project-root}/CHANGELOG.md` |
| Release report | `{project-root}/.pawbytes/tools-output/releases/` |
```

---

## Migration Patterns

Skills may encounter legacy directory structures. Document fallback paths:

```markdown
## Path Resolution

**Campaign mode** -- working within a named campaign:
  - Save to `./.pawbytes/marketing-suites/brands/{brand-slug}/campaigns/{type}-{campaign-slug}/channels/seo/content/`

**Standalone mode** -- evergreen or independent work:
  - Save to `./.pawbytes/marketing-suites/brands/{brand-slug}/channels/seo/content/`

**Legacy fallback** -- old directory structure detected:
  - Save to `./.pawbytes/marketing-suites/brands/{brand-slug}/content/seo/`
  - Suggest migration to new structure
```

Setup skills should auto-migrate legacy directories:

```markdown
## Auto-Migration

Before collecting configuration, check for legacy directories and **automatically migrate them**:

- `{project-root}/.pawbytes/marketing-suites/config/` -> `{project-root}/.pawbytes/config/`
- `{project-root}/brands/` -> `{project-root}/.pawbytes/marketing-suites/brands/`
```