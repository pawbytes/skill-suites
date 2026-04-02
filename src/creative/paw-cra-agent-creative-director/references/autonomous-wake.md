# Autonomous Wake

Headless mode activation for scheduled or automated execution.

## Trigger Conditions

- `--headless` or `-H` flag passed
- No interactive user present

## Named Tasks

| Task | Flag | Behavior |
|------|------|----------|
| Discover | `--headless:discover` | Run tool discovery, output JSON status |
| Status | `--headless:status` | Output campaign/brand overview from memory |
| Execute | `--headless:execute` | Fast-path execution with provided specs (requires JSON input) |

## Default Wake Behavior

When `--headless` is passed without a named task:

1. **Load config and memory**
2. **Run tool discovery** — verify all expected tools are available
3. **Check active campaigns** — review status of any in-progress work
4. **Output status report** — JSON format to stdout

## Execute Mode (--headless:execute)

For automation and CI/CD integration:

1. **Load JSON input** — Read specs from stdin or file
2. **Validate specs** — Check brand exists, deliverables defined
3. **Route directly to specialists** — Skip validation gates
4. **Execute and deliver** — Return asset paths in JSON

**Input format (stdin):**
```json
{
  "brand": "brand-name",
  "deliverables": [
    {
      "type": "image",
      "format": "instagram-post",
      "quantity": 5,
      "specs": {"dimensions": "1080x1080"}
    }
  ]
}
```

**Output format:**
```json
{
  "status": "complete",
  "assets": ["path/to/asset1.png", "path/to/asset2.png"]
}
```

Combine with `--yolo` for maximum speed (no safety checks).

## Output Format

```json
{
  "timestamp": "ISO-8601",
  "tools": {
    "fal": "available|unavailable",
    "elevenlabs": "available|unavailable",
    "pexels": "available|unavailable",
    "ffmpeg": "available|unavailable"
  },
  "active_brand": "brand-name or null",
  "active_campaigns": [
    {
      "name": "campaign-name",
      "status": "in_progress|blocked|complete",
      "deliverables": {
        "total": 5,
        "complete": 3,
        "pending": 2
      }
    }
  ],
  "pending_actions": ["list of recommended next steps"]
}
```

## Error Handling

If headless mode cannot complete:
- Output error JSON to stdout
- Include actionable message in `error` field
- Exit with non-zero status code

```json
{
  "error": "Memory not initialized. Run interactive mode first.",
  "suggestion": "Invoke Aria without --headless to complete onboarding."
}
```