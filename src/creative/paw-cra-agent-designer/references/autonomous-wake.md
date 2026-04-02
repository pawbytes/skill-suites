# Autonomous Wake for Designer

Headless mode activated. Executing design task without interaction.

## Wake Sequence

1. **Load Configuration**
   - Read `.pawbytes/config/config.yaml` and `.pawbytes/config/config.user.yaml`
   - Extract: user_name, communication_language, fal_key, output_directory

2. **Load Shared Memory**
   - Read `.pawbytes/creative-suites/index.md` for active brands/campaigns
   - Load active brand guidelines from `.pawbytes/creative-suites/brands/{brand}/guidelines.md`

3. **Verify Tools**
   - Check fal_key availability
   - Check ffmpeg availability (optional)

4. **Process Task**
   - Analyze task requirements from input
   - Determine capability needed
   - Execute design workflow
   - Save outputs to correct location
   - Log activity to daily file

5. **Return Results**
   - Output file paths
   - Brief summary of what was created
   - Any issues encountered

## Task Input Format

Headless tasks should include:
- Task type (social-post, carousel, flyer, brand-asset, resize)
- Content/copy
- Platform(s) or dimensions
- Brand reference (if applicable)
- Any specific style requirements

## Output Format

```
## Design Complete

**Created:** {count} asset(s)
**Location:** {path}
**Files:**
- {file1}
- {file2}

**Notes:** {any relevant notes}
```

## Error Handling

If task cannot be completed:
- Return clear error message
- Specify missing requirements
- Suggest what's needed to proceed