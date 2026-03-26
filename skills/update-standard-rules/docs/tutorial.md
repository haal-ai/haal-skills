# update-standard-rules

> Step-by-step tutorial for updating, adding, or deprecating standards and rules

## Prerequisites
- Existing standards in `.olaf/data/practices/standards/`
- Clear reason for the change (new convention, observed pattern, outdated rule)

## Estimated Time
5–10 minutes

## Step-by-Step Instructions

### Step 1: State Your Intent
**Explicit:**
> "Update the TypeScript testing standard to require Vitest instead of Jest"

**Proactive (from conversation):**
> "We always use structured logging now — let's add that as a rule"

### Step 2: Confirm Understanding
The skill pauses to confirm it understands your intent before analyzing files. This is a mandatory gate — no analysis happens until intent is clear.

### Step 3: Stack Detection
The skill identifies your project's languages, frameworks, and architecture to load relevant reference files.

### Step 4: Review Change Report
A numbered report shows proposed changes:
1. **UPDATE** — Rule X: changed from "..." to "..."
2. **ADD** — New rule: "Use structured logging for all service errors"
3. **DEPRECATE** — Rule Y: no longer applies after framework migration

### Step 5: Approve Changes
Confirm which changes to apply. You can approve all, some, or none.

### Step 6: Verify
Check the updated files. Backups of previous versions are preserved.

## Troubleshooting

| Issue | Solution |
|-------|----------|
| Standard not found | Check file exists in `.olaf/data/practices/standards/` |
| Wrong standard modified | Specify the exact standard name |
| Backup missing | Check `.olaf/data/practices/standards/` for backup files |
| Change too broad | Split into separate, focused updates |

## Verification Checklist
- [ ] Intent clearly understood
- [ ] Change report reviewed
- [ ] Approved changes applied
- [ ] Backups preserved
- [ ] Updated standards are accurate
