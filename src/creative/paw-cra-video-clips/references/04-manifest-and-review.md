---
name: 04-manifest-and-review
description: Generate clip manifest and present for review
---

# Steps 8-9: Manifest & Review Gate

## Outcome

A `clip-manifest.json` documenting every produced clip, and user approval to proceed with export.

## Step 8: Clip Manifest Generation

Run the manifest generation script against the clip output directory:

```bash
python3 ./scripts/generate-clip-manifest.py "{output_dir}" -o "{output_dir}/clip-manifest.json"
```

The script uses ffprobe to collect metadata from each clip file and produces a structured manifest. See `./scripts/generate-clip-manifest.py --help` for full interface.

The manifest captures for each clip:
- Source video reference and timecodes
- Target platform and duration
- File path, file size, resolution, codec, bitrate
- Whether subtitles are burned in
- Whether brand overlay was applied
- Encoding validation (pass/fail against platform specs)

## Step 9: Review Gate

### Interactive Mode

Present a summary table to the user:

```
Clip Production Summary
=======================
Source: podcast-ep12.mp4 (32:15)
Brand: acme-corp
Clips produced: 12

| Clip | Platform | Duration | Resolution | Size | Subtitles | Brand | Status |
|------|----------|----------|------------|------|-----------|-------|--------|
| M01  | TikTok   | 30s      | 1080x1920  | 8MB  | Yes       | Yes   | Pass   |
| M01  | YouTube  | 60s      | 1920x1080  | 15MB | Yes       | Yes   | Pass   |
| ...  | ...      | ...      | ...        | ...  | ...       | ...   | ...    |
```

Highlight any clips that failed spec validation (file too large, wrong resolution, missing subtitles).

User can:
- **Approve all** -- proceed to export
- **Reject specific clips** -- remove them from the manifest
- **Request re-encode** -- adjust quality/size for failed clips
- **Request re-cut** -- adjust timecodes and re-run production for specific moments

### Headless Mode

Auto-approve all clips that pass spec validation. Log any failures to the manifest with status `failed` and reason. Proceed to export with passing clips only.

## Progression

Proceed to `./references/05-export.md` with the approved manifest.
