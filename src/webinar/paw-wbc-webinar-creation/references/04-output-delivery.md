# Stage 4: Output Delivery

## Purpose

Present final deliverables clearly, confirm everything is saved, and guide user on next steps.

## Duration

5-10 minutes

## Process

### 1. Completion Announcement

Mark the successful completion:

> "**Webinar Creation Complete**
> 
> Congratulations! Your webinar is ready. Let me walk you through what we've created."

### 2. Deliverables Summary

Present the complete package:

> "Here's your webinar package for **[Webinar Topic]**:
> 
> ---
> 
> **1. Webinar Brief** (`brief.md`)
> Your enriched brief with audience context, goals, and expertise notes.
> 
> **2. Research Context** (`research-context.md`)
> Compressed research findings: key data points, competitive landscape, audience insights, and opportunity gaps we identified.
> 
> **3. Selected Hook** (`hook-selected.md`)
> Your chosen angle and why it will resonate with your audience.
> 
> **4. Slide Deck Outline** (`slide-deck-outline.md`)
> [X] slides with:
> - Clear titles and content points
> - Visual direction for each slide
> - Timing estimates
> - Speaker notes references
> 
> **5. Script** (`script.md`)
> - Full script for opener, close, and [X] key moments
> - Talking points for other sections
> - Timing markers and delivery notes
> 
> **6. Recommendations** (`recommendations.md`)
> [X] insights for Q&A, backup slides, and deeper dives.
> 
> ---"

### 3. File Locations

Confirm where everything is saved:

> "All files are saved to:
> ```
> .pawbytes/webinar-suites/webinars/{webinar-slug}/
> ```
> 
> You can access them anytime from your project."

### 4. Structure Preview

Optionally walk through the narrative structure:

> "Your webinar follows this structure:
> 
> **Opener** ([X] min)
> - [Hook slide]
> - [Problem/promise slide]
> 
> **Body** ([X] min)
> - Section 1: [Title]
> - Section 2: [Title]
> - Section 3: [Title]
> 
> **Close** ([X] min)
> - [Key takeaway]
> - [Call to action]
> 
> Total estimated runtime: [X] minutes"

### 5. Next Steps Recommendations

Guide the user on what to do next:

> "**Recommended Next Steps:**
> 
> 1. **Review the slide deck outline** — Make sure the flow feels right for your audience
> 2. **Rehearse the script** — Practice the full-script sections until they feel natural
> 3. **Design your slides** — Use the visual direction notes to create actual slides
> 4. **Prepare for Q&A** — Review recommendations for potential audience questions
> 
> **Optional:**
> - Use `paw-cra-agent-designer` to create visual slide designs
> - Use `paw-mkt-agency` to plan webinar promotion strategy"

### 6. Daily Log Entry

Log the completion:

Write to `daily/{YYYY-MM-DD}.md`:

```markdown
## {YYYY-MM-DD}

### [workflow] Webinar: "{Webinar Name}"
- Pipeline completed successfully
- Brief captured, discovery complete, production delivered
- [X] slides, [X]-minute script
- Hook: "[Selected hook]"
```

### 7. Final Confirmation

Close the workflow positively:

> "Your webinar is ready to build and deliver. If you need to make adjustments or create additional webinars, just let me know. Good luck with your presentation!"

## Output Summary

| Deliverable | File | Purpose |
|-------------|------|---------|
| Brief | `brief.md` | Audience context, goals, expertise |
| Research | `research-context.md` | Compressed findings and insights |
| Hook | `hook-selected.md` | Chosen angle with reasoning |
| Slide Outline | `slide-deck-outline.md` | Detailed slide-by-slide structure |
| Script | `script.md` | Full script + talking points |
| Recommendations | `recommendations.md` | Q&A insights and backup content |
| Daily Log | `daily/{date}.md` | Activity record |

## Quality Checklist

Before marking complete, verify:

- [ ] All 6 files are saved to the webinar workspace
- [ ] Slide deck outline has 20-30 slides (or appropriate for webinar length)
- [ ] Script has full copy for opener, close, and key moments
- [ ] Recommendations include at least 3-5 actionable insights
- [ ] Daily log entry is written
- [ ] User has received clear next-step guidance

## Escalation Options

Offer these at the end:

| User Need | Route To |
|-----------|----------|
| Visual slide design | `paw-cra-agent-designer` |
| Webinar promotion strategy | `paw-mkt-agency` |
| Create another webinar | Start new pipeline |
| Revise this webinar | Return to appropriate stage |

## Handling Follow-Up Requests

### User Wants Revisions

If user requests changes:

1. Identify which stage the change belongs to
2. Return to that stage or invoke the appropriate agent
3. Save updated files
4. Re-deliver summary

### User Wants Another Webinar

If user wants to create another:

1. Confirm completion of current webinar
2. Start new pipeline: "Let's start a new webinar. What's the topic?"
3. Create new webinar slug
4. Begin Stage 1

### User Needs Help Promoting

If user asks about promotion:

1. Route to `paw-mkt-agency` for marketing strategy
2. Note the webinar context they can use
3. Offer to share the brief and hook for promotional copy

## Archive Consideration

After delivery, the webinar workspace remains active. Future considerations:

- User may create a series and reference previous webinars
- User may return to revise or iterate
- User may want to share workspace with collaborators

No automatic archival — user controls when/if to archive.