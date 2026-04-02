# Autonomous Wake

When invoked with `--headless` or `-H`, complete the task without interaction.

## Wake Behavior

1. Load config and resolve values
2. Load `{project-root}/.pawbytes/creative-suites/index.md`
3. Determine task from args or default behavior

## Named Tasks

| Task | Trigger | Maps To | Behavior |
|------|---------|---------|----------|
| `--headless:research` | Explicit | Competitor Research | Run competitor scan for active brand |
| `--headless:trends` | Explicit | Trend Spotting | Analyze trends for active brand's industry |
| `--headless` (no task) | Default | Context-dependent | Check for pending research tasks in active campaigns |

## Research Task Flow

For competitor research:

1. Identify active brand from memory
2. Extract industry and competitor names from brand guidelines
3. Run `web_search_exa` for each competitor's recent content
4. Synthesize findings into `{brand-name}/research/competitor-analysis.md`
5. Log activity and update campaign status if applicable

For trend analysis:

1. Extract industry keywords from brand guidelines
2. Run `web_search_exa` for "{industry} trends 2026" and variations
3. Synthesize findings into `{brand-name}/research/trend-analysis.md`
4. Log activity

## Output Convention

All headless outputs:
- Use `{document_output_language}` for content
- Follow standard report structure
- Include timestamp in activity log
- Do not prompt for user input