# test-skill

> Step-by-step tutorial for using the test-skill fixture

## Prerequisites
- Access to the `test` branch of the haal-skills repository
- HAAL installer configured with multi-registry support

## Estimated Time
2 minutes (validation only)

## Step-by-Step Instructions

### Step 1: Configure Multi-Registry
Add the `test` branch as a secondary registry source in the installer settings.

### Step 2: Load Skills
Run the installer and let it load both `main` and `test` branches.

### Step 3: Verify Presence
Check the skill catalog in the installer UI. The "test-skill" should appear alongside regular skills from the `main` branch.

### Step 4: Confirm Merge
If test-skill appears, multi-registry merging is working correctly.

## Troubleshooting

| Issue | Solution |
|-------|----------|
| Skill not appearing | Verify the `test` branch is configured as a registry source |
| Duplicate entries | Check merge deduplication logic |
| Branch not loaded | Confirm git can access the `test` branch |

## Verification Checklist
- [ ] `test` branch configured as secondary registry
- [ ] Installer loads both branches
- [ ] test-skill appears in catalog
- [ ] No merge errors in installer logs
