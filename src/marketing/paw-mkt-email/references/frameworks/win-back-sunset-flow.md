# Win-Back / Sunset Flow

**Goal:** Re-engage inactive subscribers or gracefully remove them. **Trigger:** No opens/clicks in 60-90 days. **Emails:** 4 over 30 days.

### Email 1: "We Miss You" (Day 0)
- **Subjects:** "It's been a while, [Name]" | "A lot has changed since you've been away"
- **Elements:** Acknowledge absence without guilt, highlight 2-3 changes, reinstate value, simple re-engagement CTA
- **CTA:** "See what's new" (low commitment)

### Email 2: Value Reminder (Day 7)
- **Subjects:** "Here's what you've been missing" | "An exclusive offer, just for you"
- **Elements:** Win-back offer (15-20% off or special access), personalized recommendations, customer testimonial, clear deadline
- **CTA:** "Claim your [X]% off"

### Email 3: Preference Check (Day 14)
- **Subjects:** "Want to hear from us differently?" | "Too many emails? Let's fix that"
- **Elements:** Acknowledge email fatigue, preference center link, offer alternatives (SMS, monthly digest, launches only)
- **CTA:** "Update my preferences"

### Email 4: Final Goodbye (Day 28-30)
- **Subjects:** "Should we part ways?" | "Last email from us (unless you say otherwise)"
- **Elements:** Clear "We'll stop emailing on [date]" statement, single CTA to stay, no-guilt tone, brief reminder of what they'll miss. No engagement = suppress from all marketing sends.
- **CTA:** "Keep me subscribed" (single unmissable button)

### Branching Logic
- Engages at any point --> stop sunset, return to active segment
- Opens but no clicks --> extend by one email before purging
- Clicks preference center --> move to selected frequency/topics
- No engagement after Email 4 --> suppress (do NOT delete; keep for exclusion audiences and compliance)
