# Asset Resizing

## Outcome

Adapt existing visual assets to different platform dimensions while maintaining visual integrity and brand consistency—no quality loss, no off-brand modifications.

## Trigger

User requests resizing, reformatting, or adapting assets for different platforms.

## Inputs Required

| Input | Source | Required |
|-------|--------|----------|
| Source asset | User provided or existing | Yes |
| Target platform(s) | User specification | Yes |
| Brand guidelines | `.pawbytes/creative-suites/brands/{brand}/guidelines.md` | If exists |

## Process

### 1. Analyze Source Asset

- Original dimensions and aspect ratio
- Critical content that must remain visible
- Focal point location
- Quality/resolution of source

### 2. Determine Resize Strategy

| Scenario | Strategy | Approach |
|----------|----------|----------|
| Same aspect ratio | Direct resize | Scale proportionally, no cropping |
| Landscape to portrait | Recompose | Crop to focal point, extend background, or add elements |
| Portrait to landscape | Recompose | Extend sides, add background, or restack elements |
| Square to vertical | Extend | Add to top/bottom with brand elements |
| Print to digital | Convert | Adjust resolution, convert CMYK to RGB |

### 3. Execute Resize

**Direct Resize (Same Aspect Ratio):**
```
Source: 1080×1080 (1:1)
Target: 1200×1200 (1:1)
Action: Scale up, verify quality
```

**Recompose (Different Aspect Ratio):**
```
Source: 1080×1350 (4:5 portrait)
Target: 1200×675 (16:9 landscape)
Action:
1. Identify focal point
2. Extend background color/gradient
3. Reposition elements
4. Add brand elements to fill space
```

### 4. Quality Preservation Rules

- Never upscale beyond 150% without AI enhancement
- Check for artifacts after resize
- Verify text remains legible
- Confirm brand elements intact
- Maintain visual hierarchy

### 5. Multi-Platform Export

**One Design → Multiple Platforms:**

```
Master Design (1080×1350 portrait)
    │
    ├─→ Instagram Portrait: No change
    ├─→ Instagram Square: Crop top/bottom
    ├─→ Instagram Story: Extend background top/bottom
    ├─→ LinkedIn: Add side panels or restack
    ├─→ Twitter: Crop to focal point 16:9
    └─→ Facebook: Same as LinkedIn
```

### 6. Batch Resize Workflow

When user needs one asset across multiple platforms:

1. Create master composition with all critical content centered
2. Define safe zones for each target platform
3. Export each variant at exact specifications
4. Verify each output meets platform requirements

## Output

**Location:** `.pawbytes/creative-suites/brands/{brand}/assets/{campaign}/resized/`
**Naming:** `{original-name}_{platform}_{dimensions}.{ext}`

## Common Platform Targets

| From | To | Action |
|------|-----|--------|
| Instagram Square (1080×1080) | Instagram Portrait | Extend top/bottom |
| Instagram Square | Instagram Story | Extend top/bottom significantly |
| Instagram Square | LinkedIn | Add side panels |
| Instagram Square | Twitter | Crop to 16:9 |
| Instagram Portrait | Square | Crop top/bottom equally |

## Quality Check

- [ ] Critical content visible in all variants
- [ ] No important elements cropped
- [ ] Text still legible
- [ ] Brand elements intact
- [ ] Colors consistent across variants
- [ ] Resolution maintained
- [ ] Correct file format

## Example Usage

> "Take this Instagram post and resize it for LinkedIn and Twitter. Make sure the headline and logo stay visible on all versions."

## Escalation

If source quality is too low, inform user and offer AI enhancement options. If content cannot be preserved across aspect ratios, recommend creating platform-specific designs.