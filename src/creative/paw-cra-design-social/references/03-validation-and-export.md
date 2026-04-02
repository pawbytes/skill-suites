# Stage 3: Validation & Export

## Outcome

Assets verified against brand guidelines and platform specifications, exported to the correct location with proper naming, manifest written, and status logs updated. The user receives upload-ready files.

## Brand Validation

Verify every generated asset against brand guidelines from `.pawbytes/creative-suites/brands/{brand}/guidelines.md`:

**Color check:**
- Primary, secondary, and accent colors match brand HEX values
- No off-brand colors introduced by AI generation
- If AI generation shifted colors, flag in manifest as `color_accuracy: "approximate"` with a note

**Typography check (for template-rendered assets):**
- Font families match brand specifications
- Headline/body/accent weights correct
- Minimum sizes met (24px body, 32px headlines)

**Logo placement check:**
- Logo present if required by brief
- Clear space rules respected
- Logo not distorted or cropped

**Visual style check:**
- Overall aesthetic consistent with brand identity
- Photography/illustration style matches brand direction

**If validation fails:**
- **Headless:** Log the failure, attempt one regeneration with reinforced brand parameters. If second attempt fails, export with validation warnings in manifest.
- **Interactive:** Present the issue to the user with options: regenerate, adjust, or accept with note.

## Platform Spec Validation

Verify technical specifications match the target platform:

**Dimension check:**
- Width and height match platform specifications exactly
- Carousel: all slides have identical dimensions

**Format check:**
- PNG for graphics with transparency needs
- JPG for photographic content (quality 90+)
- File size reasonable for platform (under 8MB for most platforms)

**Safe zone check:**
- No critical content (text, logos, faces) within the platform's safe zone margins
- Instagram: 60px from edges
- LinkedIn: 50px from edges
- TikTok: 50px top, 150px bottom
- X: 40px from edges

**If spec validation fails:**
- Resize/re-render to correct dimensions
- Shift content within safe zones
- Re-export at correct format/quality

## Export

### File Organization

Save final validated assets to:

```
{output_directory}/brands/{brand}/assets/{campaign}/social/
```

If no campaign is specified, use a date-based folder:

```
{output_directory}/brands/{brand}/assets/social/{YYYY-MM-DD}/
```

### Design Manifest

Write `design-manifest.json` alongside the asset files:

```json
{
  "workflow": "paw-cra-design-social",
  "version": "1.0",
  "created": "{ISO-8601 timestamp}",
  "brand": "{brand-name}",
  "campaign": "{campaign-name or null}",
  "platform": "{target platform}",
  "format": "{single-post or carousel}",
  "assets": [
    {
      "file": "{filename}",
      "type": "{post or slide}",
      "slide_number": null,
      "dimensions": "{WxH}",
      "format": "{png or jpg}",
      "file_size_bytes": 0
    }
  ],
  "specifications": {
    "target_dimensions": "{WxH}",
    "aspect_ratio": "{ratio}",
    "safe_zone_px": 0,
    "platform": "{platform name}"
  },
  "generation": {
    "model": "{fal.ai model used}",
    "method": "{ai-only or hybrid-template}",
    "template": "{template name if used, null otherwise}"
  },
  "validation": {
    "brand_check": "pass",
    "platform_spec_check": "pass",
    "color_accuracy": "exact",
    "notes": []
  },
  "copy_source": "{user-provided, strategist, or auto-generated}",
  "headless": false
}
```

Fill `file_size_bytes` from actual file size after export. Add entries to `validation.notes` for any warnings or approximate matches.

## Status Update

### Daily Log

Append to `{project-root}/.pawbytes/creative-suites/daily/{YYYY-MM-DD}.md`:

```markdown
## {HH:MM} [Designer:cra-design-social]
**Task:** {format} for {platform}
**Brand:** {brand}
**Campaign:** {campaign or "standalone"}
**Output:** {file paths}
**Validation:** {pass/pass-with-notes/fail}
**Mode:** {interactive or headless}
```

### Campaign Status

If working within a campaign, update the campaign status file if it exists at `.pawbytes/creative-suites/brands/{brand}/campaigns/{campaign}/status.md`.

## Delivery Summary

Present the final output to the user (or log in headless mode):

```
## Design Complete

**Platform:** {platform}
**Format:** {format} ({slide count} slides if carousel)
**Dimensions:** {WxH}
**Location:** {full path to asset directory}

**Files:**
- {file1.png} ({file size})
- {file2.png} ({file size})

**Manifest:** {path to design-manifest.json}

**Validation:** {pass summary}
**Notes:** {any warnings or recommendations}
```
