# Autonomous Execution

## Purpose

Enable headless execution of service packaging tasks without user interaction.

## Headless Mode

### Activation

```
/paw-ps-service-executor --headless
/paw-ps-service-executor -H
/paw-ps-service-executor --headless:package
/paw-ps-service-executor --headless:delivery
/paw-ps-service-executor --headless:assets
```

### Named Tasks

| Task | Description | Required Context |
|------|-------------|------------------|
| `package` | Structure a complete service offer | Product context with service concept |
| `delivery` | Design fulfillment model | Service offer structure |
| `assets` | Define deliverable list | Service offer + delivery model |
| `all` | Complete service packaging | Full product context |

## Execution Protocol

### Step 1: Load Context

Read from sidecar memory:
```
{project-root}/.pawbytes/prodig-suites/memory/paw-ps-sidecar/
├── index.md                      # Current state
├── curated/
│   ├── product-context.md        # Active product
│   ├── audience-intelligence.md  # Target audience
│   ├── output-standards.md       # Quality bar
│   └── product-types/
│       └── service-products.md   # Service patterns
└── daily/
    └── YYYY-MM-DD.md            # Session log
```

If context is insufficient, log the gap and exit with specific requirements.

### Step 2: Execute Task

#### `--headless:package`

1. Read product-context.md for service concept
2. Read audience-intelligence.md for target client
3. Load offer-packaging.md reference
4. Generate complete offer structure:
   - Service name and tagline
   - Core promise
   - Target client profile
   - Scope boundaries (in/out)
   - Delivery phases
   - Deliverables per phase
   - Timeline estimate
5. Save to artifacts/{product-slug}/service/offer-structure.md
6. Log completion to daily/YYYY-MM-DD.md

**Output file structure:**
```markdown
# [Service Name]

## Service Identity
- **Name:** [Name]
- **Tagline:** [One-line description]
- **Core Promise:** [Transformation statement]

## Target Client
- **Who it's for:** [Profile]
- **Who it's NOT for:** [Exclusions]

## Scope
### Included
- [Deliverable 1]
- [Deliverable 2]

### Not Included
- [Exclusion 1]
- [Exclusion 2]

## Delivery Phases
### Phase 1: [Name] (Week X-X)
- Activities: [List]
- Deliverables: [List]

### Phase 2: [Name] (Week X-X)
- Activities: [List]
- Deliverables: [List]

## Timeline
Total duration: [X weeks]

## Team Requirements
- [Role 1]: [Responsibility]
- [Role 2]: [Responsibility]
```

#### `--headless:delivery`

1. Read offer-structure.md (from previous package task or existing)
2. Load delivery-design.md reference
3. Generate delivery model:
   - Delivery type (milestone/retainer/sprint)
   - Client touchpoints
   - Team roles
   - Tools required
   - Communication channels
   - Revision policy
   - Quality checkpoints
4. Save to artifacts/{product-slug}/service/delivery-model.md
5. Log completion to daily/YYYY-MM-DD.md

#### `--headless:assets`

1. Read offer-structure.md and delivery-model.md
2. Load asset-definition.md reference
3. Generate comprehensive deliverable list:
   - Tangible deliverables by phase
   - Intangible outcomes
   - Templates needed
   - Quality standards per deliverable
   - Value stack
4. Save to artifacts/{product-slug}/service/deliverables/deliverable-list.md
5. Log completion to daily/YYYY-MM-DD.md

#### `--headless:all` or `--headless`

Execute in sequence:
1. package
2. delivery
3. assets
4. pricing (using pricing-frameworks.md)

Generate complete service package documentation.

## Error Handling

### Insufficient Context

```
ERROR: Insufficient context for autonomous execution.

Required but missing:
- [Specific missing element 1]
- [Specific missing element 2]

Action required:
Provide [missing elements] via:
- Update curated/product-context.md
- Run paw-ps-strategist to generate missing context
- Re-run with --headless after context is complete
```

### Missing Dependencies

```
ERROR: Cannot execute [task] - missing dependencies.

Required:
- [Dependency file] not found

Previous step required:
Run --headless:[previous task] first.
```

### Validation Failure

```
WARNING: Output validation failed.

Issues:
- [Issue 1]
- [Issue 2]

Output saved to: [path]
Review and correct manually, or re-run with updated context.
```

## Output Logging

### Daily Log Format

```markdown
# YYYY-MM-DD

## Service Executor — Autonomous

### Task: [package/delivery/assets/all]
**Time:** [HH:MM]
**Product:** [product-slug]

**Actions:**
- Loaded context from [files]
- Executed [task]
- Generated [outputs]

**Output Files:**
- [path 1]
- [path 2]

**Status:** [Complete/Partial/Failed]
**Notes:** [Any observations or issues]

---
```

## Completion Signal

On successful completion:
```
SERVICE EXECUTOR — COMPLETE

Task: [name]
Product: [product-slug]

Outputs generated:
- [output 1 path]
- [output 2 path]
- [output 3 path]

Next recommended steps:
1. Review generated offer structure
2. Run paw-ps-strategist for refinement
3. Create client-facing materials

Files saved to:
{project-root}/.pawbytes/prodig-suites/artifacts/{product-slug}/service/
```

## Quality Checks

Before saving any output, verify:

- [ ] All required sections present
- [ ] Scope is specific (not vague)
- [ ] Deliverables are tangible and named
- [ ] Timeline is realistic
- [ ] File naming follows convention
- [ ] Format matches template structure