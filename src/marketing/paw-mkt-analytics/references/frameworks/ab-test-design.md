# A/B Test Design Framework

### Step 1: Hypothesis Formation
**Template**: "If we [change], then [metric] will [improve/increase/decrease] by [expected amount] because [rationale]."

**Example**: "If we change the CTA button from 'Learn More' to 'Start Free Trial', then the signup rate will increase by 15% because it sets a clearer expectation of the next step."

### Step 2: Test Parameters

#### Minimum Sample Size Calculation
| Baseline Rate | MDE (5%)  | MDE (10%) | MDE (20%) |
|---------------|-----------|-----------|-----------|
| 1%            | 62,000    | 15,700    | 4,000     |
| 2%            | 30,500    | 7,700     | 2,000     |
| 5%            | 11,800    | 3,000     | 780       |
| 10%           | 5,600     | 1,400     | 380       |
| 20%           | 2,500     | 640       | 170       |

*Per variation, at 80% power and 95% significance level.*
*MDE = Minimum Detectable Effect (relative change you want to detect).*

#### Test Duration Guidelines
- **Minimum**: 7 days (capture day-of-week effects)
- **Recommended**: 14-28 days
- **Maximum**: 42 days (avoid novelty effect decay)
- **Traffic calculation**: Required sample / daily traffic = minimum days
- **Always run full weeks**: End on the same day you started

### Step 3: Test Execution Checklist
- [ ] Define primary metric (one metric, one hypothesis)
- [ ] Define secondary metrics (guardrail metrics)
- [ ] Calculate required sample size
- [ ] Estimate test duration based on traffic
- [ ] Implement tracking for all metrics
- [ ] QA both variations across devices and browsers
- [ ] Verify random traffic allocation
- [ ] Set up monitoring for technical issues
- [ ] Document the test in a test log
- [ ] Do NOT peek at results before the test is complete

### Step 4: Analysis & Decision
- **Statistical significance**: p < 0.05 (95% confidence)
- **Practical significance**: Is the effect size meaningful for the business?
- **Segment analysis**: Check if the effect holds across key segments
- **Revenue impact**: Calculate expected annual revenue impact of the change
- **Decision framework**:
  - **Clear winner (significant + practical)**: Implement winner
  - **Significant but small effect**: Consider cost of implementation vs. benefit
  - **Not significant**: Keep control; test a bolder variation
  - **Negative result**: Valuable learning; document and move on

### Common A/B Testing Mistakes
1. Stopping tests early when results look good ("peeking")
2. Testing too many variations with insufficient traffic
3. Not accounting for seasonality or external events
4. Testing trivial changes (button color) instead of meaningful ones (value proposition)
5. Running overlapping tests that interact with each other
6. Ignoring secondary metrics and guardrails
7. No documentation of test learnings
