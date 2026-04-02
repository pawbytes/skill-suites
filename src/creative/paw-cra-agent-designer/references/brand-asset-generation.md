# Brand Asset Generation

## Outcome

Create logos, icons, and visual elements that represent a brand's identity across applications—scalable, versatile, and brand-appropriate.

## Trigger

User requests logo, icon, brand mark, visual identity element, or brand graphics.

## Inputs Required

| Input | Source | Required |
|-------|--------|----------|
| Description | Brief or user | Yes |
| Style direction | Brand guidelines or user | Yes |
| Use case | User specification | Yes |
| Existing brand context | `.pawbytes/creative-suites/brands/{brand}/guidelines.md` | If exists |

## Process

### 1. Understand Requirements

**Logo Types:**
| Type | Best For |
|------|----------|
| Wordmark | Brand names with distinctive typography |
| Lettermark | Brands with long names (initials) |
| Pictorial | Recognizable symbols |
| Abstract | Unique visual representation |
| Mascot | Character-based branding |
| Combination | Wordmark + symbol |

**Icon Types:**
| Type | Best For |
|------|----------|
| Outlined | Minimal, modern interfaces |
| Filled | Bold, high visibility |
| Duotone | Stylistic, on-brand |
| Colored | Distinctive, expressive |

### 2. Design Principles

Every logo/icon must be:

1. **Simple** — Recognizable at any size
2. **Memorable** — Distinctive and unique
3. **Timeless** — Won't look dated in 5 years
4. **Versatile** — Works across all applications
5. **Appropriate** — Fits the brand/industry

### 3. Generation Method

**Option A: AI Generation (fal.ai)**
1. Build prompt using `./ai-image-prompting.md`
2. Specify exact style, color palette, aesthetic
3. Generate multiple variations
4. Select and refine best option

**Prompt Template for Logo:**
```
[Brand name/concept] logo, [logo type] style, [color palette], [aesthetic direction], clean design, scalable, professional quality, transparent background, vector style
```

**Option B: Design Tool (OpenPencil/loopwind)**
1. Create vector-based design
2. Apply brand colors
3. Export in multiple formats

### 4. Export Variations

Every logo requires multiple outputs:

| Variation | Purpose |
|-----------|---------|
| Full color PNG | Digital use, white background |
| Transparent PNG | Versatile placement |
| SVG | Scalable vector |
| Monochrome | Single-color applications |
| Reversed (white) | Dark backgrounds |

**Size Variants:**
- 16px, 32px, 64px (favicons, small UI)
- 256px, 512px (standard digital)
- 1024px+ (large format)

### 5. Quality Verification

- [ ] Works at business card size AND billboard size
- [ ] Clear space rule defined (no elements within X distance)
- [ ] Minimum size specified for legibility
- [ ] Multiple formats exported
- [ ] All variations consistent

### 6. Icon-Specific Standards

| Requirement | Standard |
|-------------|----------|
| Format | SVG (preferred), PNG at multiple sizes |
| Style | Consistent stroke weight, corner radius |
| Grid | Pixel-aligned for crisp rendering |
| Sizes | 16, 24, 32, 48, 64, 128px |
| Naming | Clear, descriptive file names |

## Output

**Location:** `.pawbytes/creative-suites/brands/{brand}/assets/brand-identity/`
**Structure:**
```
brand-identity/
├── logo/
│   ├── logo-full-color.png
│   ├── logo-full-color.svg
│   ├── logo-monochrome.png
│   ├── logo-reversed.png
│   └── sizes/
│       ├── logo-16.png
│       ├── logo-32.png
│       └── ...
└── icons/
    ├── icon-{name}-16.png
    ├── icon-{name}-24.png
    └── ...
```

## Example Usage

> "Create a logo for 'GreenTech Solutions' — a sustainable technology company. Style: Modern, minimalist. Colors: Forest green (#2C5F2D) and teal (#0D9488). Should work as both a wordmark and a simple icon."

## Escalation

If brand direction is unclear, ask clarifying questions about brand personality, target audience, and industry. If AI generation doesn't achieve brand-appropriate results, iterate on prompt or recommend professional design.