# Template Creation

## Overview

Templates are reusable frameworks that help customers achieve specific outcomes faster. A good template removes friction, provides clear structure, and works immediately with minimal customization.

## Template Types

| Type | Description | Example |
|------|-------------|---------|
| **Document Template** | Structured documents with placeholder content | Notion databases, Google Docs, Word templates |
| **Project Template** | Pre-configured project structures with views, tasks, and workflows | Asana projects, Trello boards, Linear projects |
| **Code Template** | Boilerplate code with best practices built in | React components, API scaffolds, config files |
| **Design Template** | Visual layouts with consistent styling | Figma files, Canva templates, presentation decks |
| **System Template** | Process documentation with checklists and decision trees | SOPs, playbooks, decision frameworks |

## Template Structure

Every template must include:

### 1. Core Asset
The primary reusable file(s) that customers import or copy.

**Requirements:**
- Works immediately after import
- Uses clear, descriptive naming
- Includes placeholder content that demonstrates structure
- Has sensible defaults that work for 80% of use cases

### 2. Instructions Document
A separate guide that explains how to use the template.

**Required sections:**
- **Quick Start** — Get results in under 5 minutes
- **Customization Guide** — What to change and how
- **Examples** — 2-3 completed examples showing the template in action
- **Troubleshooting** — Common issues and solutions
- **Boundaries** — What this template doesn't do

### 3. Support Assets
Additional files that enhance adoption.

**Common support assets:**
- Preview images or screenshots
- Video walkthrough script (for product listing or onboarding)
- Changelog or version history
- Example data or demo content

## Quality Criteria

### Anti-Patterns (Avoid These)

| Anti-Pattern | Why It Fails |
|--------------|--------------|
| **Thin templates** | Empty structure with no guidance, examples, or demonstration |
| **Kitchen sink** | Every possible option included; overwhelming and unfocused |
| **No context** | Template assumes user knows how to use it |
| **Fragile structure** | Breaks when user customizes or deletes sections |
| **Hidden complexity** | Requires extensive setup before first use |

### Quality Checklist

- [ ] Template imports/copies without errors
- [ ] Clear naming throughout (no "Untitled" or "Copy of")
- [ ] Placeholder content demonstrates intended use
- [ ] Instructions cover setup in under 5 minutes
- [ ] At least 2 completed examples included
- [ ] Boundaries explicitly stated (what it doesn't do)
- [ ] Works for the 80% use case without modification
- [ ] Gracefully handles edge cases or user errors

## Build Process

### Step 1: Define the Outcome
Write a single sentence: "After using this template, the customer can [specific outcome] in [timeframe]."

**Example:** "After using this template, the customer can launch a weekly content calendar in under 15 minutes."

### Step 2: Identify the 80% Use Case
What do most users need? Build for that first. Advanced customization comes later.

**Example:** Most users need: content types, publishing schedule, and status tracking. Advanced users might want: automation, analytics integration, team assignments. Build the first set as core, second as optional.

### Step 3: Build the Core Asset
Create the template with:
- Clear structure
- Placeholder content that teaches by example
- Sensible defaults
- Clear naming

### Step 4: Write Instructions
Start with Quick Start (under 5 minutes). Add deeper customization guidance as separate sections.

### Step 5: Create Examples
Build 2-3 completed examples showing realistic use. These demonstrate value and reduce support burden.

### Step 6: Quality Check
Run through the quality checklist. Fix any issues before packaging.

### Step 7: Package
Organize files with clear structure:
```text
{product-slug}/
├── template-files/
│   └── [core template files]
├── instructions/
│   └── quick-start-guide.md
├── examples/
│   ├── example-1-[name]/
│   └── example-2-[name]/
└── support/
    ├── preview-images/
    └── video-script.md
```

## Pricing Guidance

| Template Complexity | Suggested Price Range |
|---------------------|----------------------|
| Simple (single file, clear use) | $9 - $29 |
| Moderate (multiple files, some customization) | $29 - $79 |
| Complex (full system, extensive documentation) | $79 - $199 |

Higher prices require proportionally more value demonstration through examples, case studies, and clear outcome articulation.