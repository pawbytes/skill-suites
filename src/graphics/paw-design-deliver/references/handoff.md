# Handoff: platforms, print and labels

Platform rules change; these were researched on 2026-11-04. `specs.py show <id>` carries each placement's size, cap and notes with sources.

## Upload notes

- **Instagram:** feed exports are 4:5 (1080×1350) because the publishing API and ads stop at 4:5, even though the app's profile grid now crops to 3:4. The API takes JPEG only; schedulers using it need the JPEG. Carousels take up to 20 slides in the app (some schedulers cap at 10), and every slide must share slide 1's ratio.
- **LinkedIn document posts:** upload the merged `<slug>-document.pdf`. Links inside do not click in the feed; put URLs in the post text, which should also summarise the content because documents have no per-page alt text.
- **Meta and TikTok ads:** CTAs live in the ad fields; check the creative in the ad manager's safe-zone preview, since published zones come from third-party readings of templates.
- **Google display:** static uploads cap at 150 KB (50 KB for a 320×50 on programmatic networks); responsive display images take no overlaid text over 20%, no overlaid logos and no borders, so they are photos, with the copy in the asset text fields.
- **YouTube thumbnails:** under 2 MB keeps phone uploads working even though desktop accepts more.

## Print

- The PDF is vector type at trim plus bleed with no crop marks, in RGB, because Chromium cannot write CMYK. Tell the user which applies: the printer converts RGB on request (many digital printers do), or the file needs converting to PDF/X-4 or PDF/X-1a with the printer's CMYK profile (FOGRA39 or PSO Coated v3 in Europe, GRACoL or SWOP in the US), for example with Ghostscript or the printer's prepress service, then a soft proof. Bright RGB greens, blues and oranges will print duller.
- Text is pure black; large black fields print as rich black (the printer's recipe, commonly C60 M40 Y40 K100); total ink at most 300%.
- Ask for a physical proof on anything printed in quantity, and scan-test every QR code from the proof at the real distance.

Web banners take their alt text on the `<img>` that embeds them.

## AI labels, from the provenance in assets.json

- **TikTok ads:** fully or substantially AI-generated imagery must carry TikTok's AI label or a clear disclaimer; background removal and lighting edits are exempt.
- **Meta:** auto-labels from content credentials and, since June 2026, detects third-party AI in ads; political and social-issue ads must disclose realistic AI people or events.
- **Google Ads:** election ads disclose synthetic content; since July 2026 some AI assets in ads targeting the EU, India and New York need labels.
- **YouTube:** AI-assisted thumbnails need no disclosure; realistic altered content in the video itself does.
- **LinkedIn:** synthetic media of real people must be disclosed in the post.

When unsure, recommend the label; over-disclosure carries no penalty. Keep content credentials in generated images rather than stripping them.
