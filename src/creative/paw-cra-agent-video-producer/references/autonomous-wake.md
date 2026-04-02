# Autonomous Wake for Video Producer

Headless mode activated. Executing video production task without interaction.

## Wake Sequence

1. **Load Configuration**
   - Read `{project-root}/.pawbytes/config/config.yaml` and `{project-root}/.pawbytes/config/config.user.yaml`
   - Extract: user_name, communication_language, fal_key, elevenlabs_api_key, output_directory

2. **Load Shared Memory**
   - Read `.pawbytes/creative-suites/index.md` for active brands/campaigns
   - Load active brand guidelines from `.pawbytes/creative-suites/brands/{brand}/guidelines.md`
   - Load campaign scripts if applicable

3. **Verify Tools**
   - Check ffmpeg availability (required)
   - Check fal_key availability (required for AI generation)
   - Check elevenlabs_api_key availability (optional)

4. **Process Task**
   - Analyze task requirements from input
   - Determine capability needed (short-form, long-form, clips, etc.)
   - Execute video production pipeline
   - Burn subtitles
   - Validate against platform specifications
   - Write video-manifest.json
   - Save outputs to correct location
   - Log activity to daily file

5. **Return Results**
   - Output file paths
   - Brief summary of what was produced
   - Video specifications (resolution, duration, codec)
   - Any issues encountered

## Task Input Format

Headless tasks should include:
- Task type (short-form, long-form, episodic, motion-graphics, clips, voiceover, subtitle, assembly)
- Script or concept description
- Platform target(s)
- Duration target
- Brand reference (if applicable)
- Any specific style or voice requirements

## Output Format

```
## Video Production Complete

**Created:** {count} video(s)
**Location:** {path}
**Files:**
- {file1} ({resolution}, {duration}s, {codec})
- {file2} ({resolution}, {duration}s, {codec})

**Manifest:** {manifest-path}

**Validation:**
- Specs: {pass/fail}
- Subtitles: {present/missing}
- Audio: {normalized/raw}

**Notes:** {any relevant notes}
```

## Error Handling

If task cannot be completed:
- Return clear error message with the specific failure point in the pipeline
- Specify missing requirements (tools, API keys, input files)
- Suggest what is needed to proceed
- If partial output was produced, list what was completed and where it was saved
