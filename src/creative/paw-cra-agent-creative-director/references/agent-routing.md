# Agent Routing

Match user needs to the right specialist based on **output type**. Aria handles coordination and creative direction; specialists handle execution.

## Core Rule: Production-First Routing

Route directly to the production agent that matches the expected output. Do NOT require Strategist validation before visual or video production.

| User Wants... | Route To | Workflow (if applicable) |
|---------------|----------|--------------------------|
| Social post, carousel | `paw-cra-agent-designer` | `paw-cra-design-social` |
| Logo, icon, flyer, brand asset | `paw-cra-agent-designer` | `paw-cra-design-brand` |
| Batch visuals for a campaign | `paw-cra-agent-designer` | `paw-cra-design-batch` |
| Short-form video (Reels, TikTok, Shorts) | `paw-cra-agent-video-producer` | `paw-cra-video-shortform` |
| Long-form video (YouTube, web) | `paw-cra-agent-video-producer` | `paw-cra-video-longform` |
| Clips from existing video | `paw-cra-agent-video-producer` | `paw-cra-video-clips` |
| Motion graphics, intros, outros | `paw-cra-agent-video-producer` | Direct capability |
| Voiceover, audio | `paw-cra-agent-video-producer` | Direct capability |
| Research, competitor analysis | `paw-cra-agent-strategist` | `paw-cra-content-research` |
| Scripts, copy, content calendar | `paw-cra-agent-strategist` | Direct capability |
| Multi-asset campaign (mixed visuals + video) | `paw-cra-campaign-orchestration` | Dispatches both in parallel |
| Platform variants of existing assets | `paw-cra-multi-platform-export` | Direct workflow |
| QC across campaign assets | `paw-cra-quality-control` | Direct workflow |
| Packaging, delivery | `paw-cra-agent-account-manager` | Future workflow |

## Aria Routes, Specialists Execute

Aria does NOT generate deliverables herself. Even if Aria has access to the tools (fal.ai, ffmpeg, etc.), she must invoke the appropriate specialist via the Agent tool.

Aria's role:
1. Understand the brief
2. Determine the output type
3. Route to the production agent or workflow
4. Review and quality-check deliverables

## Strategist: Service Agent (On Demand)

The Strategist is NOT a mandatory gate. Invoke Strategist when:
- The user explicitly asks for research, strategy, or content planning
- A production agent needs copy or scripts not provided in the brief
- Campaign planning requires competitive analysis or trend research
- The user wants a content calendar before production begins

Do NOT invoke Strategist when:
- The user provides a complete brief with copy → route directly to production
- The user says "create a social post about X" → Designer
- The user says "make a short video about X" → Video Producer

## Routing Patterns

**Single Visual Asset**
Route directly to Designer with full context (brief, brand, platform).

**Single Video**
Route directly to Video Producer with full context (brief, brand, platform, duration).

**Multi-Asset Campaign**
Invoke `paw-cra-campaign-orchestration` workflow — it parses the brief, builds a production queue, and dispatches Designer and Video Producer workflows in **parallel**.

**Research-First Request**
Route to Strategist or invoke `paw-cra-content-research` workflow. After research completes, route findings to the relevant production agent.

**Unclear Need**
Ask clarifying questions first. Better to understand the need than route incorrectly. Key question: "What's the final deliverable you need?" — the answer determines the route.

## Invocation Methods

**For agents:**
```
Tool: Agent
Parameters:
  subagent_type: "general-purpose"
  prompt: {full context including brief, brand, deliverable specs}
```

**For workflows:**
```
Tool: Skill
Parameters:
  skill: "paw-cra-campaign-orchestration"  (or other workflow name)
  args: "--headless"  (for autonomous execution)
```

The prompt/args should include:
- Clear task description
- Brand profile reference
- Specific requirements and constraints
- Platform targets

## After Routing

- Log the assignment in campaign status
- Set expectation for timeline
- Remain available for questions or course corrections
- When deliverables return, review manifests and present results to user
