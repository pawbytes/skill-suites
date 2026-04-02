# Output File Conventions

This document defines naming conventions, file formats, and output patterns for deliverables produced by Pawbytes skills.

## Naming Conventions

### Brand Slugs

Brand identifiers are lowercase, hyphenated strings derived from the brand name:

| Brand Name | Slug |
|------------|------|
| Acme Corporation | `acme-corporation` |
| MyBrand | `mybrand` |
| TechStart Inc. | `techstart-inc` |
| Hello World | `hello-world` |

**Rules:**
- Lowercase only
- Spaces become hyphens
- Special characters removed
- Must be unique within module

### Campaign Slugs

Campaign identifiers combine type and descriptor:

```
{type}-{descriptor}
```

| Campaign | Slug |
|----------|------|
| Q1 Launch | `launch-q1-2024` |
| Holiday Sale | `sale-holiday-2024` |
| Brand Awareness | `awareness-brand` |
| Product XYZ Launch | `launch-product-xyz` |

**Common types:**
- `launch-` — Product/feature launches
- `sale-` — Promotional campaigns
- `awareness-` — Brand awareness
- `retention-` — Retention campaigns
- `acquisition-` — Acquisition campaigns

### Phase Files

SOSTAC phases use numbered prefixes for ordering:

```
{number}-{name}.md
```

| Number | Phase | Filename |
|--------|-------|----------|
| 00 | Auto-Discovery | `00-auto-discovery.md` |
| 01 | Situation | `01-situation.md` |
| 02 | Objectives | `02-objectives.md` |
| 03 | Strategy | `03-strategy.md` |
| 04 | Tactics | `04-tactics.md` |
| 05 | Action | `05-action.md` |
| 06 | Control | `06-control.md` |

### Date-Stamped Files

Reports and time-sensitive outputs include dates:

```
{name}-{YYYY-MM-DD}.{ext}
```

| Type | Example |
|------|---------|
| SEO Audit | `seo-audit-2024-01-15.md` |
| Analytics Report | `analytics-2024-01-15.pdf` |
| Release Notes | `release-notes-1.2.0.md` |

### Presentation Files

Presentations use slugified titles:

```
{slugified-title}.html
```

| Title | Filename |
|-------|----------|
| Q1 Marketing Strategy | `q1-marketing-strategy.html` |
| 2024 Brand Plan | `2024-brand-plan.html` |
| Product Launch Deck | `product-launch-deck.html` |

## File Formats

### Markdown Files

Most text deliverables use markdown (`.md`):

- Plans and strategies
- Reports
- Brand context
- Status tracking

**Structure:**

```markdown
# Title

## Overview
Brief summary.

## Section 1
Content...

## Section 2
Content...

## Metadata
- Created: {date}
- Updated: {date}
- Author: {skill-name}
```

### HTML Files

Presentations and interactive deliverables use HTML:

- Embedded CSS (no external dependencies)
- Chart.js for visualizations
- Print-friendly for PDF export

**Output location:** `.pawbytes/tools-output/presentations/`

### JSON Files

Configuration and structured data use JSON:

- Brand configuration
- API responses
- Structured exports

**Example: brand-config.json**

```json
{
  "name": "Brand Name",
  "colors": {
    "primary": "#3B82F6",
    "secondary": "#10B981"
  },
  "fonts": {
    "heading": "Inter",
    "body": "Inter"
  }
}
```

### Media Files

Creative outputs include various media formats:

| Type | Formats | Location |
|------|---------|----------|
| Images | `.png`, `.jpg`, `.webp` | `brands/{slug}/assets/images/` |
| Videos | `.mp4`, `.mov` | `brands/{slug}/videos/` |
| Carousels | `.pdf`, `.pptx` | `brands/{slug}/carousels/` |

## Output Patterns by Skill Type

### Agent Skills

Agents write to brand workspaces and update tracking files:

| Output | Path | Purpose |
|--------|------|---------|
| Brand context | `brands/{slug}/brand-context.md` | Brand identity |
| Status | `brands/{slug}/status.md` | Progress tracking |
| Memory | `index.md` | Session continuity |

**Example output contract:**

```markdown
## Output Contract

Every coordination deliverable includes:
- **Action type**: routing decision, team spawn, or progress update
- **Brand**: which brand workspace this applies to
- **SOSTAC status**: current phase completion (e.g., 4/6 phases complete)
- **Skills involved**: which specialists were routed to
- **Next recommended action**: what the user should do next
- **File saved to**: resolved path where the artifact was written
```

### Workflow Skills

Workflows produce structured deliverables following defined patterns:

**SOSTAC (paw-mkt-sostac):**

```
sostac/
├── README.md              # Phase tracker
├── 00-auto-discovery.md   # Research
├── 01-situation.md        # Analysis
├── 02-objectives.md       # Goals
├── 03-strategy.md         # Strategy
├── 04-tactics.md          # Tactics
├── 05-action.md           # Timeline
├── 06-control.md          # Metrics
└── plan-summary.md        # Summary
```

**Presentation (paw-tools-presentation):**

```
presentations/
└── {slugified-title}.html   # Standalone HTML
```

**Video Production (paw-cra-video-shortform):**

```
videos/shortform/{slug}/
├── script.md           # Script and storyboard
├── assets/             # Media assets
│   ├── audio/
│   └── images/
└── final.mp4          # Rendered video
```

### Utility Skills

Utilities produce single focused outputs:

| Skill | Output | Path |
|-------|--------|------|
| `paw-tools-release` | Release notes | `releases/release-notes-{version}.md` |
| `paw-tools-presentation` | HTML deck | `presentations/{title}.html` |

## Path Resolution Examples

### Marketing Skills

```markdown
## Path Resolution

**Brand workspace root**: `./.pawbytes/marketing-suites/brands/{brand-slug}/`

**SOSTAC plans**: `./.pawbytes/marketing-suites/brands/{brand-slug}/sostac/`

**Campaign coordination**: `./.pawbytes/marketing-suites/brands/{brand-slug}/campaigns/{type}-{campaign-slug}/`

**Progress tracking**: `./.pawbytes/marketing-suites/brands/{brand-slug}/status.md`
```

### Creative Skills

```markdown
## Output

**Location:** `{output_directory}` or `{project-root}/.pawbytes/creative-suites/brands/{brand-slug}/`

**Campaign outputs:** `{project-root}/.pawbytes/creative-suites/brands/{brand-slug}/campaigns/{campaign-slug}/`
```

### Tools Skills

```markdown
## Output

**Location:** `{presentation_output_folder}` or `{project-root}/.pawbytes/tools-output/presentations/{slugified-title}.html`

**Filename convention:** Slugified version of the presentation title.
```

## Validation Checklist

When creating deliverables, verify:

- [ ] Filename follows naming convention
- [ ] Path uses resolved variables (no hardcoded paths)
- [ ] Brand slug is lowercase and hyphenated
- [ ] Date stamps use ISO format (YYYY-MM-DD)
- [ ] File format matches content type
- [ ] Parent directories exist before writing
- [ ] Status files updated to reflect new content

## Error Handling

When output paths conflict:

1. **Check for existing file** — Read before overwriting
2. **Warn user** — "This will overwrite existing {filename}"
3. **Offer alternatives** — "Continue, rename, or cancel?"
4. **Backup if critical** — Create `.bak` for important files

When directories don't exist:

1. **Create parent directories** — `mkdir -p` pattern
2. **Log creation** — Inform user of new directories
3. **Initialize tracking** — Create README/status files