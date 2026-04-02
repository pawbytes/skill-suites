# Quick Reference: Offer Decision Tree

> Visual decision tree mapping exit survey responses to the correct retention offer.
> Use this as a quick reference when building or auditing cancel flow logic.

---

```
Customer selects exit survey reason
         |
         +-- "Too expensive"
         |         |
         |         +--> Show: Discount offer (primary)
         |         +--> Secondary: Pause option
         |         +--> Downgrade option (if multi-plan)
         |
         +-- "Not using it enough"
         |         |
         |         +--> Show: 1:1 setup session offer
         |         +--> Secondary: Pause option
         |
         +-- "Missing a feature"
         |         |
         |         +--> Feature on roadmap? YES --> Show roadmap date + pause
         |         +--> Feature on roadmap? NO  --> Honest response + notify option
         |
         +-- "Switching to competitor"
         |         |
         |         +--> Show: Comparison table + 1 month free
         |         +--> Link: Full comparison page
         |
         +-- "Technical issue"
         |         |
         |         +--> Show: Senior support escalation + credit
         |         +--> Trigger: Internal CS alert immediately
         |
         +-- "Other" (open text)
                   |
                   +--> Show: Callback request + general discount or pause
                   +--> Route: Text field response to CS team for follow-up
```
