# Stage 2: Identify Executor

## Objective

Determine which executor type will build this product based on product family and requirements.

## Process

### Step 1: Confirm Product Family

From the brief, extract and validate the product family:

| Family | Characteristics | Examples |
|--------|-----------------|----------|
| Knowledge | Information products, educational content | Courses, guides, documentation, research reports |
| Template | Reusable assets with customization | Starter kits, frameworks, design templates |
| Software | Functional applications | SaaS tools, plugins, scripts, integrations |
| Service | Delivered expertise or work | Consulting, done-for-you, coaching programs |

### Step 2: Match to Executor

| Product Family | Executor | Responsibility |
|----------------|----------|----------------|
| Knowledge | `paw-ps-knowledge-builder` | Content structure, research, formatting |
| Template | `paw-ps-template-builder` | Component design, customization, documentation |
| Software | `paw-ps-software-builder` | Technical implementation, testing, deployment |
| Service | `paw-ps-service-builder` | Service design, process, delivery framework |

### Step 3: Validate Executor Fit

Check that the selected executor can handle:

1. **Complexity level** - Simple/standard/complex
2. **Delivery format** - Single deliverable vs. multi-component
3. **Integration needs** - Standalone vs. connected to other products
4. **Timeline** - Quick-build vs. phased delivery

### Step 4: Document Executor Requirements

For the identified executor, note:

- **Specialized skills required** (if any)
- **External dependencies** (APIs, services, assets)
- **Validation checkpoints** needed during build
- **Estimated complexity** on simple/standard/complex scale

## Executor Capability Matrix

### Knowledge Builder Capabilities

- Course design and curriculum development
- Research synthesis and documentation
- Educational content formatting
- Knowledge base structure

### Template Builder Capabilities

- Component architecture design
- Customization point definition
- Usage documentation
- Example implementations

### Software Builder Capabilities

- Technical specification creation
- Architecture design
- Implementation planning
- Testing strategy

### Service Builder Capabilities

- Service package definition
- Delivery process design
- Quality framework creation
- Client communication templates

## Output

```markdown
## Executor Selection

**Product Family:** [family]
**Selected Executor:** [executor name]

### Fit Validation
- Complexity level: [simple/standard/complex]
- Delivery format: [single/multi-component]
- Integration needs: [standalone/connected]
- Build approach: [quick-build/phased]

### Requirements for Executor
- Specialized skills: [list or "none"]
- External dependencies: [list or "none"]
- Validation checkpoints: [list]
- Estimated complexity: [rating]

### Executor Match Confidence
[High/Medium/Low] - [Brief justification]
```

## Progression Condition

Executor type identified with high confidence. All required capabilities match product needs. If confidence is low, document specific concerns for resolution in planning stage.