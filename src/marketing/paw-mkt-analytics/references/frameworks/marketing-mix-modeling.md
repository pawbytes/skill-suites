# Marketing Mix Modeling (MMM)

### When to Use MMM
- Annual marketing budget exceeds $500K
- Running 5+ channels simultaneously
- Need to account for offline channels (TV, radio, OOH)
- Cookie deprecation concerns affecting digital attribution
- Need to quantify external factors (seasonality, economy, competitor actions)

### MMM Process
1. **Data collection**: 2-3 years of weekly data (spend by channel, revenue, external factors)
2. **Variable selection**: Marketing spend, price, promotions, seasonality, macroeconomics
3. **Model building**: Regression analysis with adstock (decay) and saturation (diminishing returns)
4. **Validation**: Out-of-sample testing, comparison to known results
5. **Optimization**: Budget allocation simulation to maximize ROI
6. **Refresh**: Update model quarterly or semi-annually

### Open Source MMM Tools
- **Meta Robyn**: R-based, automated hyperparameter tuning, well-documented
- **Google Meridian**: Python-based, Bayesian approach, newer but powerful
- **PyMC Marketing**: Python, flexible Bayesian modeling framework
- **Lightweight MMM (Google)**: Python, good for smaller datasets
