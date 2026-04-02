# Customer LTV Calculation Methods

### Method 1: Historical LTV (Simple)
```
LTV = Average Revenue per User (ARPU) x Average Customer Lifespan
```
- **Example**: $50/month x 24 months = $1,200
- **Pros**: Simple, easy to calculate
- **Cons**: Backward-looking, ignores churn trends

### Method 2: Predictive LTV (Retention-based)
```
LTV = ARPU x Gross Margin / Monthly Churn Rate
```
- **Example**: $50 x 0.80 / 0.05 = $800
- **Pros**: Forward-looking, accounts for churn
- **Cons**: Assumes constant churn rate (rarely true)

### Method 3: Cohort-based LTV
- Calculate cumulative revenue per cohort over time
- Plot revenue curves, extrapolate to steady state
- **Pros**: Most accurate, accounts for cohort differences
- **Cons**: Requires historical cohort data, complex

### Method 4: DCF LTV (Discounted Cash Flow)
```
LTV = Sum of [ (ARPU x Gross Margin x Retention Rate^n) / (1 + Discount Rate)^n ]
for n = 0 to infinity
```
- **Pros**: Accounts for time value of money, most financially rigorous
- **Cons**: Requires discount rate assumption, complex to implement

### LTV:CAC Ratio Benchmarks
| Ratio    | Interpretation                                       |
|----------|------------------------------------------------------|
| < 1:1    | Losing money on every customer                       |
| 1:1-2:1  | Barely break-even; improve retention or reduce CAC   |
| 3:1      | Healthy SaaS benchmark; standard target              |
| 5:1+     | Excellent, but may be under-investing in growth      |

### CAC Payback Period Benchmarks
| Payback     | Rating    | Notes                                     |
|-------------|-----------|-------------------------------------------|
| < 6 months  | Excellent | Aggressive growth is viable                |
| 6-12 months | Good      | Standard for most SaaS                     |
| 12-18 months| Okay      | Monitor closely; look for improvements     |
| 18+ months  | Concerning| Cash flow risk; reduce CAC or improve ARPU |
