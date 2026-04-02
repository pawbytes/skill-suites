# Social Post Design

## Outcome

Create single-image social posts optimized for any platform, designed to capture attention and drive engagement within seconds.

## Trigger

User requests a social post, social media image, or platform-specific visual content.

## Inputs Required

| Input | Source | Required |
|-------|--------|----------|
| Copy/text content | Brief or Strategist output | Yes |
| Platform | User specification | Yes |
| Brand guidelines | `.pawbytes/creative-suites/brands/{brand}/guidelines.md` | Yes |
| Visual references | User provided or generated | Optional |

## Process

### 1. Load Context

- Read brand guidelines for colors, typography, logo rules
- Check platform specifications (see `./platform-specifications.md`)
- Identify any existing campaign assets to maintain consistency

### 2. Define Specifications

Reference exact dimensions from `./platform-specifications.md`:

| Platform | Recommended Format |
|----------|-------------------|
| Instagram Feed | 1080×1350px (4:5 portrait) |
| Instagram Story | 1080×1920px (9:16) |
| LinkedIn | 1200×627px (1.91:1) |
| TikTok | 1080×1920px (9:16) |
| X (Twitter) | 1200×675px (16:9) |
| Facebook | 1200×630px (1.91:1) |

### 3. Design Execution

**Visual Hierarchy Checklist:**
- [ ] Primary element (headline/hero) is largest, highest contrast
- [ ] Secondary elements support without competing
- [ ] CTA is clear and actionable (if applicable)
- [ ] Text minimum 24pt for mobile readability
- [ ] Safe zones respected (60px from edges for Instagram)

**Brand Alignment Checklist:**
- [ ] Colors match brand HEX values exactly
- [ ] Typography follows brand specifications
- [ ] Logo properly placed with clear space
- [ ] Visual style consistent with brand identity

### 4. Generation Method

**Option A: AI Generation (fal.ai)**
1. Build designer-oriented prompt using `./ai-image-prompting.md` framework
2. Use FLUX schnell/dev for photorealistic content
3. Specify exact brand colors in prompt
4. Generate, review, iterate if needed

**Option B: Template-Based (loopwind/OpenPencil)**
1. Select appropriate template
2. Apply brand colors and typography
3. Insert copy content
4. Render at exact specifications

### 5. Quality Check

Before delivery, verify against `./capability-standards.md`:
- Message clarity (immediate understanding)
- Visual hierarchy (no competing elements)
- Brand alignment (on-brand aesthetic)
- Technical specs (correct dimensions, format)
- Mobile optimization (text legible on phone)

## Output

**Format:** PNG (graphics with transparency) or JPG (photos)
**Location:** `.pawbytes/creative-suites/brands/{brand}/assets/{campaign}/social/`
**Naming:** `{platform}_{post-type}_{date}.{ext}`

## Example Usage

> "Create an Instagram post for the summer sale campaign. Copy: 'Summer Savings: 40% Off Everything. Shop Now.' Use the primary brand blue with white text."

## Escalation

If copy is unclear or missing, request clarification from user. If brand guidelines don't cover a scenario, make a recommendation and ask for confirmation.