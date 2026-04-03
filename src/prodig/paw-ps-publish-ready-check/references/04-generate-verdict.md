# Stage 4: Generate Verdict

## Purpose

Make the final determination on readiness status. Apply the appropriate threshold based on target readiness level and issue a clear, justified verdict.

---

## Verdict Options

| Verdict | Meaning |
|---------|---------|
| **Production-ready** | Complete, functional, usable by intended audience |
| **Publish-ready** | Production-ready + formatted, polished, platform-ready |
| **Sellable-ready** | Publish-ready + marketing assets, pricing, support materials |
| **Not Ready** | Gaps exist that must be addressed before any release |

---

## Decision Matrix

### For Production-Ready Target

```
VERDICT: Production-ready
IF:
  - No critical gaps
  - No important gaps in Functionality or Completeness
  - Overall quality status is Pass or Partial

VERDICT: Not Ready
IF:
  - Any critical gap exists
  - Multiple important gaps in core dimensions
```

### For Publish-Ready Target

```
VERDICT: Publish-ready
IF:
  - Production-ready criteria met
  - No critical or important gaps in Presentation
  - Platform requirements verified
  - Professional appearance confirmed

VERDICT: Production-ready (not publish-ready)
IF:
  - Production-ready criteria met
  - Gaps exist in Presentation or Platform Compliance

VERDICT: Not Ready
IF:
  - Production-ready criteria not met
```

### For Sellable-Ready Target

```
VERDICT: Sellable-ready
IF:
  - Publish-ready criteria met
  - No critical or important gaps in Selling Assets
  - Marketing materials complete
  - Pricing defined
  - Support plan documented

VERDICT: Publish-ready (not sellable-ready)
IF:
  - Publish-ready criteria met
  - Gaps exist in Selling Assets

VERDICT: Not Ready
IF:
  - Publish-ready criteria not met
```

---

## Verdict Generation Process

### Step 1: Review Assessment Results

From Stage 2 and 3:
- Overall quality status
- Dimension statuses
- Gap counts by severity
- Gap categories affected

### Step 2: Apply Decision Matrix

Match results to the appropriate matrix based on target readiness level.

### Step 3: Write Verdict Statement

Structure the verdict:

```
VERDICT: {status}

SUMMARY:
{1-2 sentence explanation of why this verdict was reached}

EVIDENCE:
- {key piece of evidence 1}
- {key piece of evidence 2}
- {key piece of evidence 3}

BLOCKERS (if Not Ready):
- {blocking gap 1}
- {blocking gap 2}

NEXT STEPS:
- {recommended action 1}
- {recommended action 2}
```

### Step 4: Generate Report

Create the full readiness report including:
- Verdict and summary
- Quality assessment summary
- Gap analysis
- Fix list (if applicable)
- Recommendations

---

## Report Formats

### HTML Report Structure

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>Readiness Report: {product-name}</title>
  <style>
    body { font-family: system-ui, sans-serif; max-width: 800px; margin: 0 auto; padding: 2rem; }
    .verdict { font-size: 1.5rem; font-weight: bold; padding: 1rem; border-radius: 0.5rem; margin: 1rem 0; }
    .verdict.ready { background: #d1fae5; color: #065f46; }
    .verdict.not-ready { background: #fee2e2; color: #991b1b; }
    .verdict.partial { background: #fef3c7; color: #92400e; }
    .section { margin: 2rem 0; }
    table { width: 100%; border-collapse: collapse; }
    th, td { border: 1px solid #e5e7eb; padding: 0.5rem; text-align: left; }
    th { background: #f9fafb; }
    .pass { color: #059669; }
    .fail { color: #dc2626; }
    .partial { color: #d97706; }
    .gap-critical { background: #fee2e2; }
    .gap-important { background: #fef3c7; }
    .gap-minor { background: #f3f4f6; }
  </style>
</head>
<body>
  <h1>Readiness Report</h1>
  
  <div class="meta">
    <p><strong>Product:</strong> {name}</p>
    <p><strong>Type:</strong> {type}</p>
    <p><strong>Target:</strong> {target-readiness}</p>
    <p><strong>Evaluated:</strong> {date}</p>
  </div>

  <div class="verdict {status-class}">
    VERDICT: {verdict}
  </div>

  <div class="section">
    <h2>Summary</h2>
    <p>{summary}</p>
  </div>

  <div class="section">
    <h2>Quality Assessment</h2>
    <table>
      <tr><th>Dimension</th><th>Status</th><th>Notes</th></tr>
      <tr><td>Functionality</td><td class="{status}">{status}</td><td>{notes}</td></tr>
      ...
    </table>
  </div>

  <div class="section">
    <h2>Gap Summary</h2>
    <table>
      <tr><th>Severity</th><th>Count</th></tr>
      <tr><td>Critical</td><td>{count}</td></tr>
      <tr><td>Important</td><td>{count}</td></tr>
      <tr><td>Minor</td><td>{count}</td></tr>
    </table>
  </div>

  <!-- Gap details and fix list if applicable -->

  <div class="section">
    <h2>Next Steps</h2>
    <ul>
      <li>{step 1}</li>
      <li>{step 2}</li>
    </ul>
  </div>
</body>
</html>
```

### Markdown Report Structure

```markdown
# Readiness Report: {product-name}

**Type:** {type}
**Target:** {target-readiness}
**Evaluated:** {date}

---

## VERDICT: {status}

{summary}

---

## Quality Assessment

| Dimension | Status | Notes |
|-----------|--------|-------|
| Functionality | {status} | {notes} |
| Completeness | {status} | {notes} |
| Clarity | {status} | {notes} |
| Usability | {status} | {notes} |
| Documentation | {status} | {notes} |
| Presentation | {status} | {notes} |
| Selling Assets | {status} | {notes} |

---

## Gap Summary

| Severity | Count |
|----------|-------|
| Critical | {count} |
| Important | {count} |
| Minor | {count} |

---

## Next Steps

1. {step 1}
2. {step 2}
```

---

## Memory Updates

### Update product-decisions.md

Append verdict to decision log:

```markdown
## Readiness Check — {date}

**Target:** {readiness-level}
**Verdict:** {verdict}

**Summary:** {1-2 sentence summary}

**Gaps:** {count} ({critical} critical, {important} important)

**Next:** {immediate next step}
```

### Update daily log

Write to `.pawbytes/prodig-suites/memory/paw-ps-sidecar/daily/YYYY-MM-DD.md`:

```markdown
## Readiness Check: {product-name}

- **Verdict:** {verdict}
- **Gaps:** {count} total
- **Effort to fix:** {estimate}
- **Report:** {path to report}
```

---

## Verdict Communication

### For Ready Verdicts

```
The product is {verdict}.

Key strengths:
- {strength 1}
- {strength 2}

Recommendations:
- Proceed with {next step}
- Monitor for {potential concern}
```

### For Not Ready Verdicts

```
The product is NOT READY for {target}.

Blocking issues:
1. {critical gap 1}
2. {critical gap 2}

To reach {target}:
1. Fix {count} critical gaps ({effort} estimated)
2. Address {count} important gaps ({effort} estimated)

See fix-list.md for detailed action items.
```

---

## Quality Gate

Before completing:

- [ ] Verdict determined using decision matrix
- [ ] Verdict justified with evidence
- [ ] HTML report generated
- [ ] Markdown report generated
- [ ] Gap analysis documented
- [ ] Fix list created (if not ready)
- [ ] product-decisions.md updated
- [ ] Daily log updated

---

## Final Checklist

Complete workflow is done when:

- [ ] All 4 stages completed
- [ ] Reports saved to product workspace
- [ ] Memory updated
- [ ] User notified of verdict
- [ ] Next steps clear