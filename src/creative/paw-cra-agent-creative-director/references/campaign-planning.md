# Campaign Planning

Orchestrate multi-asset campaigns by breaking down briefs into specialist assignments, coordinating timelines, and ensuring cohesive output.

## Goal

Transform a brief into an executed campaign where all assets work together and arrive on time.

## Planning Process

**1. Assess Scope**
- List all required deliverables from the brief
- Identify which specialist owns each
- Note dependencies (e.g., "video needs final script first")

**2. Create Execution Plan**
- Order of operations
- Parallel vs sequential work
- Review checkpoints

**3. Assign to Specialists**
For each deliverable, invoke the appropriate agent:
- `paw-cra-agent-strategist` — scripts, copy, research, SEO
- `paw-cra-agent-designer` — images, graphics, visual assets
- `paw-cra-agent-video-producer` — videos, motion graphics
- `paw-cra-agent-account-manager` — packaging, final delivery

**4. Track Progress**
- Log each assignment in memory
- Check in on completion
- Flag blockers early

## Specialist Invocation

Use the Agent tool with a prompt that includes:
- The brief context
- Specific deliverable requirements
- Brand profile reference
- Any constraints or preferences

Example invocation for Designer:
```
Create 3 social media carousel images for the "Summer Launch" campaign.
Brand: Acme Co (see brand profile at .pawbytes/creative-suites/brands/acme-co/profile.md)
Specs: 1080x1080px, PNG
Style: Bold, summer colors, product-focused
Copy on image: "Summer Sale - 50% Off"
Deadline: {date}
```

## Coordination

- Ensure all specialists reference the same brand profile
- Check that visual styles are consistent across assets
- Review copy tone across all text deliverables
- Time final reviews to catch issues before deadline

## Campaign Memory

Store campaign state in: `{project-root}/.pawbytes/creative-suites/campaigns/{campaign-name}/`

```
{campaign-name}/
├── brief.md
├── plan.md
├── assets/
│   ├── images/
│   ├── videos/
│   └── copy/
└── status.md
```