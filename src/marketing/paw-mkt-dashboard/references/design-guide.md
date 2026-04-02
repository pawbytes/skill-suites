---
name: design-guide
description: Design principles and aesthetic direction for LLM-generated marketing dashboards. Anti-AI-slop, modern minimalist.
---

# Dashboard Design Guide

Aesthetic direction for generating marketing dashboards. The goal is a distinctive, sophisticated interface — not a generic AI dashboard. Every design decision should pass the question: "Could someone tell AI made this?" If yes, redesign.

## Design Philosophy

- **Commit to restraint** — Minimalism means every element earns its place
- **Asymmetry over symmetry** — Intentional visual tension creates interest
- **Data hierarchy over decoration** — The numbers tell the story, not the chrome
- **One distinctive choice** — Pick one memorable design element per dashboard

## Color System

### Use OKLCH Color Space

```css
/* Tinted neutrals — never pure gray */
--neutral-50: oklch(97% 0.01 250);
--neutral-100: oklch(94% 0.01 250);
--neutral-200: oklch(88% 0.01 250);
--neutral-300: oklch(78% 0.015 250);
--neutral-400: oklch(62% 0.015 250);
--neutral-500: oklch(50% 0.015 250);
--neutral-600: oklch(40% 0.015 250);
--neutral-700: oklch(32% 0.02 250);
--neutral-800: oklch(24% 0.02 250);
--neutral-900: oklch(16% 0.02 250);
--neutral-950: oklch(10% 0.02 250);

/* Primary — one color, adapt to brand */
--primary: oklch(55% 0.15 250);
--primary-light: oklch(90% 0.04 250);
--primary-dark: oklch(40% 0.12 250);

/* Semantic */
--success: oklch(55% 0.14 145);
--warning: oklch(70% 0.14 80);
--error: oklch(55% 0.18 25);
--info: oklch(60% 0.12 250);
```

### 60-30-10 Rule

- **60%** — Neutral backgrounds (`--neutral-50`, `--neutral-100`)
- **30%** — Text and borders (`--neutral-700`, `--neutral-300`)
- **10%** — Primary accent (`--primary`) — CTAs, active states, key indicators

### Hard Prohibitions

- No pure black `#000` or pure white `#fff` — always tint
- No cyan-on-dark, purple-to-blue gradients, neon accents
- No gradient text on metrics or headings
- No dark mode with glowing accents (the canonical AI dashboard look)
- No gray text on colored backgrounds

## Typography

### Font Selection

Avoid overused defaults: Inter, Roboto, Arial, Open Sans, Lato, Montserrat.

**Recommended alternatives:**
- Body: **Plus Jakarta Sans**, **Instrument Sans**, **Outfit**, or **Figtree**
- Display (if pairing): **Fraunces**, **Newsreader** (serif contrast)

Use Google Fonts CDN for simplicity.

### Type Scale (5 sizes)

```css
--text-xs: 0.75rem;    /* 12px — captions, metadata */
--text-sm: 0.875rem;   /* 14px — secondary UI, table cells */
--text-base: 1rem;     /* 16px — body text */
--text-lg: 1.25rem;    /* 20px — section headings */
--text-xl: 1.75rem;    /* 28px — page titles */
```

### Dashboard-Specific Rules

- **Always use `font-variant-numeric: tabular-nums`** on data tables and metrics
- Use `rem`/`em` for font sizes, never `px` for body text
- Bold (`font-weight: 600`) for headings, regular (`400`) for body — no more than 2 weights
- Line height: 1.5 for body, 1.2 for headings

## Layout

### Spacing System (4pt base)

```css
--space-1: 0.25rem;   /* 4px */
--space-2: 0.5rem;    /* 8px */
--space-3: 0.75rem;   /* 12px */
--space-4: 1rem;      /* 16px */
--space-6: 1.5rem;    /* 24px */
--space-8: 2rem;      /* 32px */
--space-12: 3rem;     /* 48px */
--space-16: 4rem;     /* 64px */
```

Use `gap` for sibling spacing, not margins.

### Dashboard Shell

- **Fixed sidebar** (240px) with main content area
- Sidebar: brand name, navigation links with active indicator
- Main: padded content area with max-width for readability

### Content Layout

- Use **varied card sizes** — not identical grids
- Self-adjusting grid: `repeat(auto-fit, minmax(280px, 1fr))`
- Break the grid intentionally for emphasis (span 2 columns for key metrics)
- Generous whitespace between sections

### Hard Prohibitions

- No identical card grids (same-sized cards with icon+heading+text repeated)
- No "hero metric layout" (big number, small label, gradient accent)
- No centering everything — left-align by default
- No same spacing everywhere — vary rhythm (tight groups, generous gaps)
- No nested cards (cards inside cards)
- No glassmorphism or decorative blur

## Components

### Status Badges

Use semantic colors with subtle backgrounds. No gradient badges.

```css
/* Success states: active, published, completed */
.badge-success { background: oklch(92% 0.05 145); color: oklch(35% 0.1 145); }

/* Warning states: planning, review, pending */
.badge-warning { background: oklch(92% 0.06 80); color: oklch(40% 0.1 80); }

/* Neutral states: draft, paused, inactive */
.badge-neutral { background: oklch(94% 0.01 250); color: oklch(45% 0.02 250); }

/* Error states: failed, blocked, cancelled */
.badge-error { background: oklch(92% 0.05 25); color: oklch(40% 0.12 25); }
```

### Tables

- Left-align text, right-align numbers
- Subtle horizontal dividers only (no vertical lines, no zebra stripes)
- Sortable columns with minimal indicator (small arrow)
- Action buttons in last column, text-only (Edit, Delete), not icon buttons

### Forms / Modals

- Use visible `<label>` elements — never placeholder-only
- Standard SvelteKit `<form method="POST">` with `action="?/create"`, `action="?/update"`, etc.
- Modal overlay for add/edit — simple white panel, no fancy animations
- Validate on blur, not on keystroke
- Error messages below fields, specific and blame-free

### Empty States

Every empty section needs:
1. Brief acknowledgment ("No campaigns yet")
2. Value explanation ("Track campaign progress, deadlines, and channel distribution")
3. Clear action button ("Add your first campaign")

Not just "No data" with an icon.

### Buttons

- One primary style (filled, primary color) — used sparingly
- One secondary style (border only)
- One text/link style (for table row actions)
- Destructive actions name the destruction: "Delete campaign" not "Delete"
- All buttons need hover, focus-visible, and disabled states

## Interaction & Motion

### Transitions

- Button hover/focus: 150ms ease-out
- Modal enter: 200ms ease-out
- Modal exit: 150ms ease-in
- Tab/page transitions: none (SvelteKit handles this natively)

### Motion Principles

- Only animate `transform` and `opacity`
- Respect `prefers-reduced-motion`
- Focus on page-load stagger for first impression, not scattered micro-interactions
- No bounce, elastic, or spring animations

## Responsive

### Breakpoints

- Mobile: < 768px — sidebar collapses to hamburger menu
- Tablet: 768px–1024px — sidebar visible, single-column content
- Desktop: > 1024px — full layout

### Tables on Mobile

- Horizontal scroll with sticky first column
- Or card-based layout below 640px

## Anti-Patterns Checklist

Before generating, verify the design avoids:

- [ ] Identical card grids
- [ ] Hero metric layout (big number + small label + gradient)
- [ ] Cyan-on-dark color scheme
- [ ] Purple-to-blue gradients
- [ ] Gradient text on numbers/headings
- [ ] Glassmorphism / frosted glass
- [ ] Dark mode with neon accents
- [ ] Large rounded icons above every heading
- [ ] Inter/Roboto as the only font
- [ ] Centering everything
- [ ] Same spacing everywhere
- [ ] Monospace typography as "technical" aesthetic
- [ ] Decorative animations with no purpose