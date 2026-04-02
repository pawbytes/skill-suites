# Episodic Series

## Outcome

Produce multi-episode video content with consistent visual style, branding, and production quality across all episodes -- maintaining series identity while varying content per episode.

## Trigger

User requests a video series, episodic content, multi-part video, or recurring video format.

## Inputs Required

| Input | Source | Required |
|-------|--------|----------|
| Series outline | Brief or user input | Yes |
| Episode scripts | Strategist or user | Yes (per episode) |
| Brand guidelines | Shared memory | Yes |
| Episode count | User specification | Yes |
| Format (short/long) | User specification | Yes |

## Process

### 1. Series Bible

Establish consistency anchors before producing any episode:

- **Visual template:** Consistent intro, outro, lower thirds, title cards
- **Color grading:** Same LUT or color treatment across all episodes
- **Music theme:** Consistent intro/outro music, recurring motifs
- **Typography:** Same font family, sizes, and positioning
- **Pacing pattern:** Consistent episode structure and rhythm
- **Numbering:** Episode naming convention (e.g., "Episode 01: {title}")

### 2. Template Creation

Build reusable elements for the series:
- Intro sequence (3-5s with series title and episode number)
- Outro sequence (5-10s with CTA and next episode teaser)
- Lower third template for speaker/topic identification
- Transition style between sections

### 3. Per-Episode Production

Each episode follows the appropriate production path:
- **Short-form series** -- follow Short-Form Video capability per episode
- **Long-form series** -- follow Long-Form Video capability per episode

Apply series bible constraints to every episode to maintain consistency.

### 4. Series-Level QC

After producing all episodes, verify cross-episode consistency:
- Visual style consistent across all episodes
- Audio levels matched
- Intro/outro identical (except episode number)
- Naming convention followed

## Output

**Location:** `.pawbytes/creative-suites/brands/{brand}/videos/{campaign}/series/{series-name}/`
**Naming:** `ep{NN}_{title-slug}.mp4`
**Manifest:** Series-level `video-manifest.json` listing all episodes with metadata

## Escalation

If the series exceeds 5 episodes, recommend planning all scripts upfront via Strategist before starting production to maintain narrative coherence.
