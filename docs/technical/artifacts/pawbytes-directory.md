# .pawbytes/ Directory Structure

The `.pawbytes/` directory is the primary output location for all skill artifacts. It should be added to `.gitignore` with exceptions for shared configuration.

## Complete Structure

```
.pawbytes/
├── config/
│   ├── config.yaml              # Project configuration (committed)
│   └── config.user.yaml         # User overrides (gitignored)
│
├── marketing-suites/
│   ├── brands/
│   │   └── {brand-slug}/
│   │       ├── brand-context.md
│   │       ├── product-marketing-context.md
│   │       ├── sostac/
│   │       │   ├── README.md
│   │       │   ├── 00-auto-discovery.md
│   │       │   ├── 01-situation.md
│   │       │   ├── 02-objectives.md
│   │       │   ├── 03-strategy.md
│   │       │   ├── 04-tactics.md
│   │       │   ├── 05-action.md
│   │       │   ├── 06-control.md
│   │       │   └── plan-summary.md
│   │       ├── campaigns/
│   │       │   └── {type}-{campaign-slug}/
│   │       │       ├── README.md
│   │       │       ├── brief.md
│   │       │       └── coordination.md
│   │       ├── channels/
│   │       └── status.md
│   └── reports/
│       ├── seo-audits/
│       ├── content-audits/
│       └── analytics/
│
├── creative-suites/
│   ├── index.md                 # Memory entry point
│   ├── brands/
│   │   └── {brand-slug}/
│   │       ├── brand-context.md
│   │       ├── campaigns/
│   │       │   └── {campaign-slug}/
│   │       │       ├── brief.md
│   │       │       ├── assets/
│   │       │       └── status.md
│   │       ├── carousels/
│   │       ├── videos/
│   │       │   ├── shortform/
│   │       │   └── longform/
│   │       └── exports/
│   └── output/
│       ├── final/
│       └── drafts/
│
└── tools-output/
    ├── presentations/
    │   └── {slugified-title}.html
    ├── releases/
    │   └── release-notes-{version}.md
    └── reports/
        └── {report-type}/
```

## Configuration Directory

### config.yaml

Project-level configuration, typically committed to version control:

```yaml
version: 1.0.0
user_name: User
communication_language: English
document_output_language: English
output_folder: "{project-root}/.pawbytes/marketing-suites"

# Module-specific sections
mkt:
  default_brand: null
  api_key: ""

cra:
  fal_key: ""
  elevenlabs_api_key: ""
  pexels_api_key: ""
  default_brand: null
  output_directory: "{project-root}/output"
```

### config.user.yaml

User-specific overrides, gitignored by default:

```yaml
user_name: Your Name

mkt:
  api_key: your-actual-key

cra:
  fal_key: your-fal-key
  pexels_api_key: your-pexels-key
```

## Module Output Directories

### marketing-suites/

Outputs from `paw-mkt-*` skills:

| Subdirectory | Purpose | Created By |
|--------------|---------|------------|
| `brands/` | Brand workspaces | `paw-mkt-agency`, `paw-mkt-sostac` |
| `reports/` | Analysis reports | `paw-mkt-seo`, `paw-mkt-analytics` |

### creative-suites/

Outputs from `paw-cra-*` skills:

| Subdirectory | Purpose | Created By |
|--------------|---------|------------|
| `index.md` | Memory entry point | `paw-cra-agent-creative-director` |
| `brands/` | Brand workspaces | All creative agents |
| `output/` | Final deliverables | Production workflows |

### tools-output/

Outputs from `paw-tools-*` skills:

| Subdirectory | Purpose | Created By |
|--------------|---------|------------|
| `presentations/` | HTML presentations | `paw-tools-presentation` |
| `releases/` | Release artifacts | `paw-tools-release` |

## Path Resolution in Skills

Skills resolve paths using configuration variables:

```markdown
## Path Resolution

**Brand workspace root**: `{project-root}/.pawbytes/marketing-suites/brands/{brand-slug}/`

**SOSTAC plans**: `{project-root}/.pawbytes/marketing-suites/brands/{brand-slug}/sostac/`

**Campaign coordination**: `{project-root}/.pawbytes/marketing-suites/brands/{brand-slug}/campaigns/{type}-{campaign-slug}/`

**Progress tracking**: `{project-root}/.pawbytes/marketing-suites/brands/{brand-slug}/status.md`
```

### Variable Substitution

| Variable | Resolves To |
|----------|-------------|
| `{project-root}` | Project root directory |
| `{user_name}` | User's name from config |
| `{output_folder}` | Output directory path |
| `{brand-slug}` | Lowercase, hyphenated brand name |
| `{campaign-slug}` | Campaign identifier |

## .gitignore Configuration

Recommended `.gitignore` entries:

```gitignore
# Pawbytes output
.pawbytes/
!.pawbytes/config/
!.pawbytes/config/config.yaml

# User-specific overrides
.pawbytes/config/config.user.yaml
```

This ensures:
- Shared config is version controlled
- User secrets remain local
- Generated artifacts are not committed