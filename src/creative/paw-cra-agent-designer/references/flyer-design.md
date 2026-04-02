# Flyer Design

## Outcome

Create print-ready or digital promotional materials designed to inform, persuade, and drive action—typically single-page documents with professional production specifications.

## Trigger

User requests a flyer, poster, promotional handout, or print-ready marketing material.

## Inputs Required

| Input | Source | Required |
|-------|--------|----------|
| Content/copy | Brief or user | Yes |
| Dimensions | User specification or standard | Yes |
| Output type | Print or digital | Yes |
| Brand guidelines | `.pawbytes/creative-suites/brands/{brand}/guidelines.md` | Yes |

## Process

### 1. Determine Output Type

| Output Type | Specifications |
|-------------|---------------|
| **Digital flyer** | 1080px+ width, RGB, JPG/PNG, 72-150 PPI |
| **Print flyer** | 300 DPI, CMYK, PDF with bleed, 3mm bleed + 3mm safety |

### 2. Select Size

Common sizes from `./platform-specifications.md`:

| Size | Trim | With Bleed |
|------|------|------------|
| A4 | 210×297mm | 216×303mm |
| Letter (US) | 8.5×11" | 8.75×11.25" |
| A5 | 148×210mm | 154×216mm |
| DL | 99×210mm | 105×216mm |

### 3. Establish Visual Hierarchy

Order of prominence (largest to smallest):

1. **Headline** — Largest, boldest, most prominent
2. **Key visual** — Supporting image that reinforces message
3. **Key information** — Date, time, location, price
4. **Details** — Additional information
5. **Call-to-action** — What to do next
6. **Contact/Branding** — Smallest, but present

### 4. Design Composition

**Composition Rules:**
- Clear focal point (headline or hero image)
- Balanced layout (not lopsided)
- Adequate white space (30%+ of area)
- Logical reading order (top-left to bottom-right)
- Brand elements present but not overwhelming

**Typography:**
- Headline: Bold, attention-grabbing
- Body: Readable, consistent (11-12pt minimum for print)
- Limited font families (2-3 maximum)
- High contrast with background

### 5. Print-Specific Setup (If Applicable)

```
┌─────────────────────────────────────┐
│              BLEED AREA              │  ← 3mm beyond trim
│   (background extends here)          │
│  ┌───────────────────────────────┐  │
│  │         TRIM SIZE             │  │  ← Final cut size
│  │  ┌─────────────────────────┐  │  │
│  │  │     SAFETY MARGIN       │  │  │  ← Keep content inside
│  │  │     (3mm from trim)     │  │  │
│  │  └─────────────────────────┘  │  │
│  └───────────────────────────────┘  │
└─────────────────────────────────────┘
```

### 6. Quality Verification

**Brand Alignment:**
- [ ] Colors match brand palette
- [ ] Typography follows brand specs
- [ ] Logo properly placed
- [ ] Visual style on-brand

**Technical Quality:**
- [ ] Correct dimensions including bleed
- [ ] Correct color mode (RGB/CMYK)
- [ ] Resolution appropriate (300 DPI for print)
- [ ] Images embedded, not linked
- [ ] All fonts outlined or embedded
- [ ] Critical content inside safety zone

## Output

**Digital:** PNG/JPG, RGB, `.pawbytes/creative-suites/brands/{brand}/assets/{campaign}/flyers/`
**Print:** PDF, CMYK, with bleed, same location
**Naming:** `{flyer-name}_{size}_{date}.{ext}`

## Flyer Types

| Type | Key Elements |
|------|-------------|
| Event | Event name prominent, date/time/location clear, visual reflects theme |
| Promotional | Offer/discount prominent, urgency element, clear next step |
| Informational | Organized hierarchy, easy to scan, contact info clear |

## Example Usage

> "Create an A4 print flyer for our workshop 'Introduction to AI Marketing.' Date: April 15, 10am-2pm. Location: Tech Hub, Downtown. Include QR code for registration. Brand colors, professional aesthetic."

## Escalation

If content is too dense for single page, suggest brochure format or editing content. If images are low resolution, request higher quality or recommend alternatives.