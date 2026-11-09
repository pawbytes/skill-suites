# Intake

The outcome is an open project, `{project}/production.json` from `production.py init`, and `{project}/brief.md`. The brief is read by every stage skill without this conversation in the room, so it carries everything the user told you and everything you decided.

Mine first: a content brief usually names the format, the platform, the message and often the brand. Ask only for the gaps.

## Pick the profile and placements

`production.py profiles` prints each profile's defaults. Signals:

| The user describes | Profile |
|---|---|
| One feed image for Instagram, Facebook, LinkedIn, X, Threads | `social-post` |
| Several slides, "carousel", "document post", a listicle or guide | `carousel` |
| Vertical full-screen, Stories, TikTok photo, Pinterest idea pin | `story` |
| A printed or digital poster, event poster, gig poster | `poster` |
| A handout or leaflet, front and back | `flyer` |
| Website hero, email header, LinkedIn/X/YouTube cover, OG image | `banner` |
| Display ads in many sizes, a Meta/Google ad set | `ad-set` |
| YouTube thumbnail | `thumbnail` |

When the signals are thin, propose config `design.default_profile` (default `social-post`) and say why in a line.

Placements come from the catalog: `uv run {skill-root}/scripts/specs.py list` (`--q linkedin`, `--class display`), and `show <id>` for size, safe zone, file cap and print bleed. The first placement is the master the layout is designed for; list every other size the user needs now, because the layout stage re-lays out each one rather than stretching the master. Instagram feed defaults to 4:5 (1080×1350), because the API and ads stop there even though the app grid now crops to 3:4; keep key content in the central band.

`--pieces` is the number of distinct canvases per placement: slides in a carousel (default 7; 8–12 is the sweet spot for engagement, up to 20 when every slide earns its swipe), 2 for a two-sided flyer.

## What the brief holds

`brief.md`, short and in plain prose or a small table:

- Goal (awareness, engagement, conversion, event, announcement) and audience: what the viewer should feel, know or do.
- The content, in the user's words, plus anything already written. Mandatory copy (legal lines, prices, dates, sponsor names) listed verbatim under a "Mandatory copy" heading, because concept copies it into the deck's `mandatory` list and the validator checks it word for word.
- Profile, placements (master first), pieces, medium (digital or print). For print: the printer if known, paper and finish, quantity, and whether the printer converts RGB to CMYK.
- Brand: logo files, guideline PDF, fonts, colours, tone. Copy the user's files into `{project}/brand/` and leave the originals untouched. No brand: say style will propose one.
- Imagery: user photos (product shots must be real photos; the product itself is never regenerated), or generated, or type only.
- Image provider: propose config `design.image_provider` (`fal` or `codex-cli`) and record the user's choice with `init --image-provider`, because style and imagery read it from `production.py status` and fall back to config only when it is unset.
- Budget for fal.ai spend in USD: propose config `design.default_budget_usd`. Graphics are cheap next to video (cents per image), but the cap still guards runaway retries.
- Deadline, and where the files go after delivery (scheduler, printer, ad manager).
- Open questions you could not settle.

Push back at intake on two messages in one asset, a headline longer than the format allows (a poster read in three seconds carries about seven words), or a placement list that silently doubles the work.

## Open it

Slug from the title, lowercase and hyphenated. `production.py init --root {projects-folder} --slug ... --title ... --profile ... --placements ... --pieces ... --budget ... --image-provider ...`; write `brief.md` into the project; tell the user the project path. Then route to the manifest's `next_stage`: concept → `paw-design-concept`, and so on.
