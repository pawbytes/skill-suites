# Setup Process

## Purpose

First-run setup for Prodig Suites module. This reference guides the setup skill through the initialization process.

## Setup Flow

```
1. Check Prerequisites
   └─> Read module.yaml
   └─> Check for existing config
   └─> Detect headless mode

2. Collect Configuration
   └─> Core settings (if needed)
   └─> Module-specific settings
   └─> Validate responses

3. Create Directory Structure
   └─> Main module directories
   └─> Sidecar memory structure
   └─> Product and artifact directories

4. Scaffold Sidecar Files
   └─> Orientation index
   └─> Curated starter files
   └─> Product type guides

5. Verify Capabilities
   └─> Research tools
   └─> Reporting tools
   └─> Note availability

6. Write Configuration
   └─> config.yaml
   └─> config.user.yaml
   └─> module-help.csv

7. Confirm and Report
   └─> Summary of created items
   └─> Capability status
   └─> Next steps
```

## Headless Mode

When `--headless` or `-H` flag is provided:

1. Skip all interactive prompts
2. Use all default values from `module.yaml`
3. Still perform all setup steps
4. Output machine-readable confirmation

Example:
```bash
/paw-ps-setup --headless
```

## Update vs Fresh Install

### Fresh Install

- No existing `.pawbytes/prodig-suites/` directory
- No `ps:` section in config.yaml
- Create all files from scratch

### Update

- Existing directory detected
- Preserve all curated files with content
- Update config if new variables added
- Re-create any missing starter files

**Never overwrite:**
- `product-context.md` if it has user content
- `market-intelligence.md` if populated
- `audience-intelligence.md` if populated
- `product-decisions.md` if has entries
- Any files in `products/` or `artifacts/`

## Directory Verification

After setup, verify this structure exists:

```
.pawbytes/prodig-suites/
├── config.yaml                    # Suite configuration
├── memory/
│   └── paw-ps-sidecar/
│       ├── index.md               # Orientation file
│       ├── daily/                 # Session logs
│       └── curated/
│           ├── product-context.md
│           ├── market-intelligence.md
│           ├── audience-intelligence.md
│           ├── product-decisions.md
│           ├── output-standards.md
│           └── product-types/
│               ├── knowledge-products.md
│               ├── template-products.md
│               ├── software-products.md
│               └── service-products.md
├── products/                      # Product workspaces
└── artifacts/                     # Generated outputs
```

## File Content Guidelines

### Starter Files

Starter files should:

1. **Have clear headings** — Structure is visible at a glance
2. **Include brief instructions** — How the file will be used
3. **Show expected sections** — What content will go where
4. **Be ready to populate** — Clear placeholders, not empty

### Product Type Files

Product type files should:

1. **Define the category** — What products fit this type
2. **List sub-types** — Common variations
3. **Show output structure** — Expected file organization
4. **Include quality checklist** — What "done" looks like

## Capability Detection

### Research Capabilities

Check for tools that enhance research:

| Capability | Tool Pattern | Enhancement |
|------------|--------------|-------------|
| Web Search | WebSearch, mcp__exa__* | Market research, competitor analysis |
| Code Context | mcp__CodeGraphContext__* | Software product research |

### Reporting Capabilities

Check for tools that enhance output:

| Capability | Tool Pattern | Enhancement |
|------------|--------------|-------------|
| Presentations | paw-tools-presentation | Slide decks from research |
| Releases | paw-tools-release | Version management |

**Note:** Missing capabilities are informational only — the suite functions without them but with reduced power.

## Error Handling

### Directory Creation Fails

1. Report the error clearly
2. Suggest manual creation
3. Continue with other setup steps

### File Write Fails

1. Report the specific file
2. Show the content that would have been written
3. Offer to retry or skip

### Config Write Fails

1. Preserve collected values in memory
2. Report the error
3. Offer to write to alternative location

## Post-Setup Recommendations

After successful setup, suggest:

1. **Immediate next step**: "Run `paw-ps-agent-product-builder` to create your first product"
2. **Explore capabilities**: "Try `paw-ps-discovery` to explore product ideas"
3. **Review standards**: "Check `output-standards.md` to understand quality expectations"