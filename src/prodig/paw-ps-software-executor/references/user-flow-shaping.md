# User Flow Shaping

## Outcome

Turn product intent into experience structure by mapping the paths users take through the product. User flows translate features into screens, actions, and decisions.

## Trigger

User requests user flow, user journey, experience mapping, or "how should users move through the product?"

## Inputs Required

| Input | Source | Required |
|-------|--------|----------|
| Feature specifications | Previous artifact | Yes |
| Audience intelligence | `curated/audience-intelligence.md` | Yes |
| Product context | `curated/product-context.md` | Yes |

## Process

### 1. Identify Entry Points

Every user flow starts somewhere. Define the entry points:

| Entry Point | User State | Trigger |
|-------------|------------|---------|
| Homepage | First-time visitor | Marketing, referral, search |
| Onboarding | New signup | Account creation |
| Dashboard | Returning user | Login, notification |
| Feature page | Task-focused | Direct link, navigation |

### 2. Define Core Flows

For each major feature, define the user flow:

```
Flow Name: [Feature Name]
Entry Point: [Where user starts]
Success State: [Where user ends when successful]
Failure States: [Where user ends when something goes wrong]
```

### 3. Map Flow Steps

Break each flow into discrete steps:

```markdown
## Flow: [Name]

### Step 1: [Step Name]
- **Screen**: [Screen/page name]
- **User Action**: [What user does]
- **System Response**: [What happens]
- **Decision Point**: [Yes/No - what determines next step?]
- **Next Step**: [Where user goes next]

### Step 2: [Step Name]
...
```

### 4. Document Decision Points

Every decision point creates branching. Document each:

```markdown
### Decision: [Decision Name]
**Question**: [What determines the branch?]
**Yes Path**: [Where user goes if yes]
**No Path**: [Where user goes if no]
**Default**: [Which path is assumed]
```

### 5. Handle Error States

For each flow, define what happens when things go wrong:

| Error Type | Trigger | User Message | Recovery Path |
|------------|---------|--------------|---------------|
| Validation error | Invalid input | Specific field message | Stay on step, highlight field |
| Auth error | Session expired | "Please log in again" | Redirect to login |
| System error | Server failure | "Something went wrong" | Retry option, support contact |
| Not found | Resource missing | "Item not found" | Redirect to list, search |

### 6. Create Flow Diagram

Represent the flow visually using ASCII or text:

```
[Start] → [Step 1] → [Decision?] 
                         │
                    ┌────┴────┐
                    ↓         ↓
                  [Yes]     [No]
                    │         │
                    ↓         ↓
               [Step 2]   [Step 3]
                    │         │
                    └────┬────┘
                         ↓
                      [End]
```

### 7. Define Screen Requirements

For each step, specify what the screen needs:

```markdown
### Screen: [Name]

**Purpose**: [What this screen enables]
**URL/Route**: [If applicable]
**Key Elements**:
- [Element 1]: [Purpose]
- [Element 2]: [Purpose]
- [Element 3]: [Purpose]

**User Actions Available**:
- [Action 1]
- [Action 2]
- [Action 3]

**Data Required**:
- [Data item 1]: [Source]
- [Data item 2]: [Source]
```

## Output

**Format:** Markdown document with flow diagrams

**Structure:**
1. Entry points overview
2. Core flows (one per feature)
3. Flow step details
4. Decision point documentation
5. Error state handling
6. Screen requirements summary

**Location:** `{project-root}/.pawbytes/prodig-suites/memory/paw-ps-sidecar/artifacts/{product-slug}/user-flows.md`

**Naming:** `user-flows.md`

## Quality Checklist

Before delivery, verify:

- [ ] Every flow has defined entry and exit points
- [ ] All decision points have documented branches
- [ ] Error states have recovery paths
- [ ] Each step has a clear user action
- [ ] Screen requirements are specific
- [ ] Flows are testable (can verify with users)

## Flow Types

### Authentication Flow
Entry: Landing page
Steps: Signup/Login → Verification → Profile setup → Dashboard

### Core Task Flow
Entry: Dashboard
Steps: Initiate action → Configure → Execute → Review → Save/Share

### Onboarding Flow
Entry: First login
Steps: Welcome → Profile → Preferences → Tutorial → First action

### Recovery Flow
Entry: Error state
Steps: Acknowledge → Diagnose → Resolve → Resume

## Common Mistakes

1. **Happy path only** — Every flow has failure states; document them
2. **Missing context** — Users don't arrive at flows randomly; define triggers
3. **Too granular** — "Click button" is not a meaningful step
4. **Too abstract** — "User completes task" doesn't guide design
5. **Ignoring state** — What data/permissions does the user have at each step?

## Example Output

```markdown
## Flow: Create New Project

### Entry Point
- **Trigger**: User clicks "New Project" button on dashboard
- **User State**: Authenticated, has project creation permission
- **Prerequisites**: Account in good standing, not at project limit

### Step 1: Project Type Selection
- **Screen**: New Project Modal
- **User Action**: Select project type from options
- **System Response**: Show relevant fields for selected type
- **Decision Point**: Is project type supported?
- **Next Step**: Step 2 (yes) or Error state (no)

### Step 2: Project Details
- **Screen**: Project Details Form
- **User Action**: Enter name, description, settings
- **System Response**: Validate input in real-time
- **Decision Point**: Are all required fields valid?
- **Next Step**: Step 3 (yes) or Stay on step with errors (no)

### Step 3: Template Selection (Optional)
- **Screen**: Template Browser
- **User Action**: Choose template or skip
- **System Response**: Preview template contents
- **Decision Point**: User selects template or skips?
- **Next Step**: Step 4

### Step 4: Confirmation & Creation
- **Screen**: Review & Create
- **User Action**: Click "Create Project"
- **System Response**: Create project, redirect to project view
- **Success State**: User lands on new project overview

### Error States

| Error | Trigger | Message | Recovery |
|-------|---------|---------|----------|
| Name taken | Duplicate project name | "Project name already exists" | Change name |
| Limit reached | Project quota exceeded | "You've reached your project limit" | Upgrade or delete |
| Permission denied | Role lacks create permission | "You don't have permission to create projects" | Contact admin |
```

## Escalation

If feature specifications are incomplete or ambiguous, escalate to feature definition capability before mapping flows.