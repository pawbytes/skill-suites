# Autonomous Batch Production

Headless mode activated. Execute the full batch pipeline without interaction.

## Wake Sequence

1. **Load Configuration**
   - Read `.pawbytes/config/config.yaml` and `.pawbytes/config/config.user.yaml`
   - Extract: user_name, communication_language, fal_key, output_directory

2. **Load Shared Memory**
   - Read `.pawbytes/creative-suites/index.md` for active brands/campaigns
   - Load brand guidelines from `.pawbytes/creative-suites/brands/{brand}/guidelines.md`

3. **Verify Tools**
   - Confirm fal_key — abort if missing
   - Check ffmpeg (optional)
   - Check Puppeteer/Playwright (optional)

4. **Execute Pipeline**
   - Parse input (content calendar or campaign brief)
   - Build production queue
   - Run batch generation loop — all assets, no pauses
   - Organize bundle
   - Generate batch-manifest.json
   - Skip review gate
   - Write status update

5. **Return Results**

```
## Batch Production Complete

**Campaign:** {campaign}
**Brand:** {brand}
**Produced:** {N}/{total} assets
**Failed:** {F} assets
**Bundle:** {bundle path}
**Manifest:** {manifest path}

**By Platform:**
- Instagram: {count} assets
- LinkedIn: {count} assets
- {platform}: {count} assets

**Issues:** {list any failures or warnings}
```

## Error Protocol

- If fal_key is missing: return error immediately, do not attempt generation
- If individual assets fail: continue batch, log failures in manifest
- If brand guidelines are missing: generate with best-effort, mark all as `brand_validated: false`
- At completion: always produce manifest even if some assets failed
