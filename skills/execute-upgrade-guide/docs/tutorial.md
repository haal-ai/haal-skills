# Execute Upgrade Guide: Step-by-Step Tutorial

## Overview

This skill takes an upgrade guide (produced by `generate-upgrade-guide`) and executes it step-by-step against a target repository. It checks version applicability before starting, creates safety checkpoints, tracks progress, and supports rollback.

## Prerequisites

- An upgrade guide file (`.md`) produced by `generate-upgrade-guide`
- Python 3.9+
- Git repository as target

## Step 1: Have an Upgrade Guide Ready

First, generate an upgrade guide using the companion skill:

```
Generate an upgrade guide from v1.0.0 to v1.1.0
```

This produces a file like:
```
.olaf/work/staging/upgrade-guide/upgrade-guide-v1.0.0-to-v1.1.0-20260309-1530.md
```

## Step 2: Run the Execute Skill

Invoke the skill in your AI assistant:

```
Execute the upgrade guide at .olaf/work/staging/upgrade-guide/upgrade-guide-v1.0.0-to-v1.1.0-20260309-1530.md
```

Or with options:

```
Execute the upgrade guide at .olaf/work/staging/upgrade-guide/upgrade-guide-v1.0.0-to-v1.1.0-20260309-1530.md
Target repo: /path/to/my-project
Dry run: true
```

## Step 3: Applicability Check

The skill automatically detects your target's current version and checks if the guide applies.

**Example — version matches:**
```
✅ VERSION CHECK PASSED

Detected version: v1.0.0 (via git tag on HEAD)
Expected version: v1.0.0
Target version:   v1.1.0

The upgrade guide is applicable to this target.
Proceed with upgrade? (yes/no)
```

**Example — version mismatch:**
```
❌ VERSION CHECK FAILED

Detected version: v0.9.0 (via package.json)
Expected version: v1.0.0
Target version:   v1.1.0

Reason: Target is at version 'v0.9.0', which is BEFORE the guide's
expected start version 'v1.0.0'. You need to first upgrade to 'v1.0.0'
before applying this guide.
```

**Example — already upgraded:**
```
❌ VERSION CHECK FAILED

Detected version: v1.1.0 (via git describe)
Expected version: v1.0.0
Target version:   v1.1.0

Reason: Target is already at version 'v1.1.0'. The upgrade has
ALREADY BEEN APPLIED.
```

## Step 4: Pre-Upgrade Safety Checkpoint

Before any changes, the skill creates a safety checkpoint:

```
Creating pre-upgrade checkpoint...
  git stash push -m "pre-upgrade-v1.0.0-to-v1.1.0-20260309-1545"
  ✅ Checkpoint created. You can rollback at any time.
```

## Step 5: Step-by-Step Execution

Each step from the guide is presented for your approval:

```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
STEP 1/5: Update dependencies
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Update the authentication library to v2.3.0:

  npm install @company/auth@2.3.0

Proceed? (yes / skip / abort)
```

Your options at each step:
- **yes** — Execute the step
- **skip** — Skip and move to the next (warning recorded)
- **abort** — Stop everything and offer rollback

## Step 6: Handling Failures

If a step fails:

```
❌ STEP 3 FAILED

Command: npm run migrate-config
Exit code: 1
Error output:
  Error: config/auth.yaml not found

Options:
1. Retry this step
2. Skip this step (may cause issues later)
3. Abort and rollback
```

## Step 7: Post-Upgrade Verification

After all steps complete, the skill runs verification checks:

```
POST-UPGRADE VERIFICATION

✅ [1] Configuration file validated
✅ [2] Application starts successfully
❌ [3] API health check — endpoint /api/health returned 503
⏭️ [4] Skipped (manual verification needed)
```

## Step 8: Final Summary

```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
UPGRADE COMPLETE
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Upgrade:        v1.0.0 → v1.1.0
Steps executed: 4/5
Steps skipped:  1
Steps failed:   0
Verifications:  3/4 passed

Progress log: .olaf/work/staging/upgrade-execution/progress-20260309-1545.md

Suggested next actions:
  git add -A && git commit -m "chore: upgrade from v1.0.0 to v1.1.0"
```

## Dry Run Mode

To preview without executing:

```
Execute the upgrade guide at .olaf/work/staging/upgrade-guide/upgrade-guide-v1.0.0-to-v1.1.0-20260309-1530.md
Dry run: true
```

This shows every step with its commands but executes nothing.

## Resume After Interruption

If execution was interrupted, resume from a specific step:

```
Execute the upgrade guide at .olaf/work/staging/upgrade-guide/upgrade-guide-v1.0.0-to-v1.1.0-20260309-1530.md
Resume from step: 3
```

## Rollback

At any point during execution, choose "abort" to trigger rollback:

```
Restoring pre-upgrade checkpoint...
  git stash pop
  ✅ Rolled back to pre-upgrade state.
```

## Tips

- **Always use dry run first** for complex upgrades to preview all steps
- **Review breaking changes** before starting — they are listed at the top of the guide
- **Keep the progress log** — it documents exactly what was done for audit purposes
- **Commit after success** — the upgrade is not committed automatically
