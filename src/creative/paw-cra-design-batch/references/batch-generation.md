# Batch Generation Loop

Execute the production queue. Generate each asset, validate, and export.

## Loop Protocol

Process queue items sequentially. For each item:

### 1. Confirm Platform Specs

Double-check dimensions, safe zones, and format requirements from the queue item spec. This is a sanity check — specs were resolved in queue building but confirm before committing to generation.

### 2. Generate AI Imagery

**Prompt construction:**
- Start with the visual direction from the brief
- Include brand style keywords from guidelines (e.g., "minimalist", "bold", "corporate")
- Specify composition requirements (e.g., "leave space for text overlay at bottom third")
- Include the campaign theme for visual consistency across the batch
- Add platform-appropriate framing (e.g., "vertical composition" for Instagram portrait)

**Generation via fal.ai CLI:**
```bash
curl -X POST "https://queue.fal.run/{model}" \
  -H "Authorization: Key {fal_key}" \
  -H "Content-Type: application/json" \
  -d '{"prompt": "...", "image_size": {"width": W, "height": H}}'
```

Poll for completion. Download result to local path.

**Consistency strategy for batches:**
- Use the same style seed or prompt prefix across same-platform assets
- Reference the campaign theme in every prompt
- If using FLUX models, consider consistent negative prompts across the batch

### 3. Apply Template / Text Overlay

**If using code-based template:**
- Render the HTML/CSS template with the generated image as background
- Insert content (headline, body, CTA) into template slots
- Apply brand typography and colors
- Capture the rendered template as the final image (element screenshot, not full page)

**If pure AI generation with text:**
- Use a model with strong text rendering (Nano Banana Pro, FLUX.2 [flex])
- Include text in the generation prompt
- Verify text rendered correctly — re-generate if garbled

**If AI background + separate text overlay:**
- Generate background image without text
- Composite text overlay using HTML/CSS rendering or image processing
- This gives maximum control over typography

### 4. Brand Validate

Check the generated asset against brand guidelines:
- **Colors:** Do the dominant colors align with brand palette?
- **Typography:** If text is present, does it use brand fonts (or close equivalents)?
- **Logo:** If logo placement was specified, is it correct?
- **Style:** Does the overall aesthetic match brand identity?
- **Safe zones:** Is critical content within platform safe zones?

Mark each asset: `brand_validated: true` or `brand_validated: false` with notes.

### 5. Export with Sequential Naming

Save the final asset to the generation output folder using the filename from the queue spec. Verify file was written successfully and record file size.

## Progress Tracking

After each asset completes:
- Log: `[{queue_position}/{total}] {filename} — {status}`
- Track running totals: successes, failures, skips

## Failure Handling

If an asset fails at any step:
- Log the failure with the step that failed and the error reason
- Record in the generation log as `status: "failed"`
- Continue to the next queue item — never halt the batch
- Common failures: API timeout, content policy rejection, template render error

## Batch Size Considerations

- **Small batch (1-5 assets):** Process sequentially, no special handling
- **Medium batch (6-20 assets):** Group by platform for style consistency
- **Large batch (20+ assets):** Consider using FLUX.1 [schnell] for speed, upgrade selectively for hero assets
