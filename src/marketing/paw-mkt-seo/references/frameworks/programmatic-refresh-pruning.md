# Refresh and Pruning

pSEO is a portfolio. Weak cohorts should not remain indexed forever.

### Refresh triggers
- data fields changed materially
- rankings decayed for high-value pages
- new FAQs, comparisons, or proof available
- competitor templates improved significantly

### Prune triggers
- page remains unindexed after repeated crawl opportunities
- page gets indexed but earns no meaningful impressions over a defined review window
- entity is outdated, discontinued, unsupported, or empty
- page falls below the minimum uniqueness threshold after data decay

### Prune actions
- enrich and keep indexed
- merge into a stronger page and 301 redirect
- noindex but keep live for UX reasons
- remove and return 410/301 if no longer useful

Document prune logic in the monitoring plan so the page system does not grow unchecked.
