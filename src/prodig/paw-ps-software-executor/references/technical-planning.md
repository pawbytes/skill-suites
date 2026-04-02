# Technical Planning

## Outcome

Prepare technical execution context that enables developers to build efficiently. This is not full architecture—it's the technical foundation needed to start development.

## Trigger

User requests technical planning, tech stack decisions, architecture overview, or when preparing for developer handoff.

## Inputs Required

| Input | Source | Required |
|-------|--------|----------|
| MVP definition | Previous artifact | Yes |
| Feature specifications | Previous artifact | Yes |
| PRD-lite | Previous artifact | Yes |

## Process

### 1. Define Tech Stack

Document the technical foundation:

```markdown
## Tech Stack

### Frontend
- **Framework**: [React/Vue/Svelte/etc.]
- **Styling**: [Tailwind/CSS Modules/styled-components]
- **State Management**: [Context/Redux/Zustand/etc.]
- **Build Tool**: [Vite/Next.js/etc.]

### Backend
- **Framework**: [Express/FastAPI/Django/etc.]
- **API Style**: [REST/GraphQL/tRPC]
- **Authentication**: [JWT/Session/OAuth provider]

### Data
- **Database**: [PostgreSQL/MongoDB/etc.]
- **ORM**: [Prisma/TypeORM/etc.]
- **Cache**: [Redis/Memory/etc.]

### Infrastructure
- **Hosting**: [Vercel/AWS/GCP/etc.]
- **CI/CD**: [GitHub Actions/etc.]
- **Monitoring**: [Sentry/DataDog/etc.]
```

### 2. Identify Technical Decisions

Document decisions that affect implementation:

```markdown
## Technical Decisions

### Decision: [Topic]
**Context**: [Why this decision matters]
**Options Considered**:
1. [Option A] - [Pros/Cons]
2. [Option B] - [Pros/Cons]
**Decision**: [Chosen option]
**Rationale**: [Why this option]
**Implications**: [What this means for development]
```

### 3. Create Data Model Overview

Define the core data entities:

```markdown
## Data Model

### Entities

#### [Entity Name]
- **Purpose**: [What this represents]
- **Key Fields**:
  - `id`: [type] - [description]
  - `field1`: [type] - [description]
  - `field2`: [type] - [description]
- **Relationships**:
  - Has many [Other Entity]
  - Belongs to [Other Entity]
```

### 4. Define API Contracts (High-Level)

Outline the API structure:

```markdown
## API Overview

### Authentication Endpoints
| Method | Endpoint | Purpose |
|--------|----------|---------|
| POST | /auth/signup | Create account |
| POST | /auth/login | Authenticate |
| POST | /auth/logout | End session |

### Resource Endpoints
| Method | Endpoint | Purpose |
|--------|----------|---------|
| GET | /resources | List resources |
| POST | /resources | Create resource |
| GET | /resources/:id | Get single resource |
| PUT | /resources/:id | Update resource |
| DELETE | /resources/:id | Delete resource |
```

### 5. Identify Technical Risks

```markdown
## Technical Risks

| Risk | Impact | Likelihood | Mitigation |
|------|--------|------------|------------|
| [Risk 1] | [H/M/L] | [H/M/L] | [How to address] |
| [Risk 2] | [H/M/L] | [H/M/L] | [How to address] |
```

### 6. Define Third-Party Integrations

```markdown
## Integrations

### [Service Name]
- **Purpose**: [What it enables]
- **Tier**: [Free/Paid tier]
- **Fallback**: [What if it fails]
- **Setup Required**: [Configuration steps]

### [Service Name]
...
```

## Output

**Format:** Markdown document

**Structure:**
1. Tech stack decisions
2. Data model overview
3. API contracts (high-level)
4. Technical risks
5. Integration requirements

**Location:** `{project-root}/.pawbytes/prodig-suites/memory/paw-ps-sidecar/artifacts/{product-slug}/technical-context.md`

**Naming:** `technical-context.md`

## Quality Checklist

Before delivery, verify:

- [ ] Tech stack choices have rationale
- [ ] Data model covers core entities
- [ ] API structure is consistent
- [ ] Risks have mitigations
- [ ] Integrations have fallbacks

## Common Mistakes

1. **Over-engineering** — This is MVP tech planning, not enterprise architecture
2. **Missing rationale** — Decisions without reasons create confusion later
3. **Ignoring constraints** — Budget, timeline, and skill constraints matter
4. **No fallbacks** — Every third-party dependency needs a backup plan