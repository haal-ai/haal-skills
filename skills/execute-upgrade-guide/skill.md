---
name: execute-upgrade-guide
description: Execute an upgrade guide step-by-step with version applicability checks, safety gates, and progress tracking. Consumes upgrade guides produced by generate-upgrade-guide.
license: Apache-2.0
metadata:
  olaf_tags: [upgrade, migration, execution, git, version-management, safety]
  copyright: Copyright (c) 2026 pjmp020564
  author: pjmp020564 (on github)
  repository: https://github.com/haal-ai/haal-skills
  provider: Haal AI
---

if you are in need to get the date and time, use time tools, fallback to shell command if needed

# Execute Upgrade Guide

Consume and execute an upgrade guide produced by `generate-upgrade-guide`. Before executing any step, validate that the guide is applicable to the target based on version detection. Execute each step with user confirmation, track progress, and provide rollback support.

## Input Parameters

You MUST request these parameters if not provided by the user:

**REQUIRED**:
- `guide_path`: string — Path to the upgrade guide Markdown file (e.g., `.olaf/work/staging/upgrade-guide/upgrade-guide-v1.0.0-to-v1.1.0-20260309-1530.md`)

**OPTIONAL**:
- `target_repo_path`: string — Path to the target repository where the upgrade will be applied. Default: current working directory.
- `target_branch`: string — The branch to base the upgrade on (e.g., `main`, `develop`, `release/1.0`). Default: current branch. The skill will checkout this branch before starting.
- `upgrade_branch_name`: string — Name for the new branch created for the upgrade work. Default: `upgrade/{start_version}-to-{end_version}`. All upgrade changes are committed on this branch, keeping `target_branch` clean.
- `dry_run`: boolean — If true, only show what would be done without executing. Default: false.
- `skip_applicability_check`: boolean — Skip version applicability check. Default: false. Use only if you have manually verified the version.
- `resume_from_step`: integer — Resume execution from a specific step number. Default: 1 (start from beginning).

## User Interaction

- **Applicability check**: Run without approval (read-only).
- **Each upgrade step**: MUST ask for explicit user approval before executing.
- **Destructive operations** (file modifications, config changes, database migrations): MUST show exactly what will change and require confirmation.
- **Rollback steps**: MUST be confirmed before executing.

## Process

### Phase 1: Load and Parse the Upgrade Guide

1. Read the upgrade guide file at `guide_path`.
2. Validate the file exists and is a valid Markdown document.
3. Extract from the guide:
   - **start_version**: The version being upgraded FROM (from the guide header)
   - **end_version**: The version being upgraded TO (from the guide header)
   - **project_name**: Name of the project
   - **complexity**: SIMPLE, MODERATE, or COMPLEX (from Executive Summary)
   - **prerequisites**: List of prerequisite checks
   - **breaking_changes**: List of breaking changes with actions
   - **upgrade_steps**: Ordered list of step-by-step instructions
   - **verification_steps**: Post-upgrade verification checklist
   - **rollback_procedure**: Rollback steps if needed
4. Present a summary to the user:
   ```
   📋 UPGRADE GUIDE LOADED

   Project:     {project_name}
   Upgrade:     {start_version} → {end_version}
   Complexity:  {complexity}
   Steps:       {count}
   Breaking:    {breaking_change_count} breaking change(s)
   ```

### Phase 2: Version Applicability Check

**This is CRITICAL. Do NOT skip unless `skip_applicability_check` is explicitly true.**

Run the applicability check script:

```bash
python skills/execute-upgrade-guide/tools/check_version_applicability.py \
  "{start_version}" "{end_version}" \
  --repo "{target_repo_path}" \
  -o ".olaf/work/staging/upgrade-execution/applicability-{timestamp}.json"
```

Read the JSON output and act based on the `recommendation` field:

| Recommendation | Action |
|---------------|--------|
| `PROCEED` | Version matches. Continue to Phase 3. |
| `ALREADY_UPGRADED` | Target is already at end_version. Inform user and STOP. |
| `UPGRADE_TO_START_FIRST` | Target is at an earlier version. Inform user they need to upgrade to start_version first. STOP. |
| `NOT_APPLICABLE_PAST_TARGET` | Target is past end_version. This guide does not apply. STOP. |
| `PARTIAL_UPGRADE_REVIEW` | Target is between start and end version. Warn user and ask if they want to continue (may be a partial/interrupted upgrade). |
| `MANUAL_CHECK_REQUIRED` | Could not detect version. Ask user to confirm their current version before proceeding. |

Present the result clearly:

**If applicable:**
```
✅ VERSION CHECK PASSED

Detected version: {detected_version} (via {method})
Expected version: {start_version}
Target version:   {end_version}

The upgrade guide is applicable to this target.
Proceed with upgrade? (yes/no)
```

**If NOT applicable:**
```
❌ VERSION CHECK FAILED

Detected version: {detected_version} (via {method})
Expected version: {start_version}
Target version:   {end_version}

Reason: {details}

{recommendation-specific guidance}
```

**If MANUAL CHECK needed:**
```
⚠️ VERSION CHECK INCONCLUSIVE

Could not automatically detect the current version.
Expected version: {start_version}

Please confirm: Is your target currently at version {start_version}?
Provide the version number or confirm to proceed.
```

### Phase 3: Branch Setup and Pre-Upgrade Safety

1. **Checkout the target branch**:
   ```bash
   git -C "{target_repo_path}" checkout {target_branch}
   git -C "{target_repo_path}" pull --ff-only
   ```
   If the checkout fails (uncommitted changes, etc.), inform the user and STOP.

2. **Detect version files in the target**:
   Scan the repository root for version-bearing files. Report what was found:
   ```
   📁 VERSION FILES DETECTED

   - package.json      → version: "1.0.0"
   - pom.xml           → version: 1.0.0
   - pyproject.toml    → (not found)
   - build.gradle      → (not found)
   - VERSION           → (not found)
   ```
   These files may need updating as part of the upgrade. The upgrade guide's steps should cover them, but if they don't, warn the user:
   ```
   ⚠️ The upgrade guide does not mention updating {file}.
      Current version in {file}: {current_version}
      Expected target version: {end_version}
      You may need to update this file manually after the upgrade.
   ```

3. **Create a new upgrade branch from target_branch**:
   ```bash
   git -C "{target_repo_path}" checkout -b {upgrade_branch_name}
   ```
   Default branch name: `upgrade/{start_version}-to-{end_version}`

   Present to user:
   ```
   🌿 UPGRADE BRANCH CREATED

   Base branch:    {target_branch}
   Upgrade branch: {upgrade_branch_name}

   All upgrade changes will be committed on this branch.
   After completion, you can merge or create a PR back to {target_branch}.
   ```

4. **Create progress tracker**:
   Create `.olaf/work/staging/upgrade-execution/progress-{timestamp}.md` with:
   ```markdown
   # Upgrade Execution Progress

   - **Guide**: {guide_path}
   - **Upgrade**: {start_version} → {end_version}
   - **Started**: {timestamp}
   - **Status**: IN PROGRESS

   ## Steps

   | # | Step | Status | Started | Completed | Notes |
   |---|------|--------|---------|-----------|-------|
   | 1 | ... | PENDING | | | |
   | 2 | ... | PENDING | | | |
   ```

3. **Run prerequisites**:
   Execute each prerequisite from the guide. If any fails, STOP and inform the user.

### Phase 4: Execute Upgrade Steps

For EACH step in the upgrade guide, in order:

1. **Present the step**:
   ```
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
   STEP {n}/{total}: {step_title}
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

   {step_description}

   Commands to execute:
   {commands}

   Proceed? (yes / skip / abort)
   ```

2. **Wait for user confirmation**:
   - `yes` → Execute the step
   - `skip` → Mark as SKIPPED, move to next step, add warning
   - `abort` → Stop execution, provide rollback guidance

3. **Execute the step**:
   - Run each command from the step
   - Capture stdout and stderr
   - Check exit codes

4. **Verify the step** (if verification commands are provided in the guide):
   - Run verification command
   - Report pass/fail

5. **Update progress tracker**:
   - Mark step as COMPLETED, SKIPPED, or FAILED
   - Record timestamp and any notes

6. **If a step FAILS**:
   ```
   ❌ STEP {n} FAILED

   Command: {command}
   Exit code: {code}
   Error output:
   {stderr}

   Options:
   1. Retry this step
   2. Skip this step (may cause issues later)
   3. Abort and rollback
   ```

### Phase 5: Post-Upgrade Verification

1. Execute each verification step from the guide.
2. Present results as a checklist:
   ```
   POST-UPGRADE VERIFICATION

   ✅ [1] Configuration file validated
   ✅ [2] Application starts successfully
   ❌ [3] API health check failed
   ⏭️ [4] Skipped (manual verification needed)
   ```

3. If any verification fails, present options:
   - Investigate and fix
   - Rollback to pre-upgrade state
   - Mark as known issue and continue

### Phase 6: Finalize

1. **Update progress tracker**: Mark overall status as COMPLETED or COMPLETED_WITH_WARNINGS.

2. **Present final summary**:
   ```
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
   UPGRADE COMPLETE
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

   Upgrade:        {start_version} → {end_version}
   Steps executed: {completed}/{total}
   Steps skipped:  {skipped}
   Steps failed:   {failed}
   Verifications:  {passed}/{total_verifications} passed

   Progress log: {progress_file_path}
   ```

3. **Version file check**:
   If version files were detected in Phase 3, verify they now reflect `{end_version}`:
   ```
   📁 VERSION FILE STATUS (post-upgrade)

   - package.json      → version: "1.1.0" ✅
   - pom.xml           → version: 1.1.0   ✅
   ```
   If any version file still shows `{start_version}`, warn the user and offer to update it:
   ```
   ⚠️ {file} still shows version {start_version}.
      Update to {end_version}? (yes/no)
   ```

4. **Commit all changes on the upgrade branch**:
   ```bash
   git -C "{target_repo_path}" add -A
   git -C "{target_repo_path}" commit -m "chore: upgrade from {start_version} to {end_version}"
   ```

5. **Suggest next actions**:
   - Create a pull request from `{upgrade_branch_name}` to `{target_branch}`:
     ```bash
     git push origin {upgrade_branch_name}
     # Then create PR via your platform (GitHub, GitLab, Bitbucket, etc.)
     ```
   - Or merge directly (if policy allows):
     ```bash
     git -C "{target_repo_path}" checkout {target_branch}
     git -C "{target_repo_path}" merge --no-ff {upgrade_branch_name} -m "chore: merge upgrade {start_version} to {end_version}"
     ```
   - Run full test suite on the upgrade branch before merging
   - Update documentation if needed
   - Delete the upgrade branch after merge:
     ```bash
     git branch -d {upgrade_branch_name}
     ```

## Rollback Procedure

If the user chooses to abort or rollback at any point:

1. Read the rollback section from the upgrade guide.
2. Present the rollback steps for confirmation.
3. Execute any guide-specific rollback steps.
4. **Discard the upgrade branch and return to target_branch**:
   ```bash
   # Discard all uncommitted changes
   git -C "{target_repo_path}" checkout -- .
   git -C "{target_repo_path}" clean -fd
   # Switch back to the original target branch
   git -C "{target_repo_path}" checkout {target_branch}
   # Delete the upgrade branch
   git -C "{target_repo_path}" branch -D {upgrade_branch_name}
   ```
   Present to user:
   ```
   🔄 ROLLBACK COMPLETE

   Returned to branch: {target_branch}
   Deleted branch:     {upgrade_branch_name}
   Target is back at:  {start_version}
   ```
5. Update progress tracker to mark status as ROLLED_BACK.

## Error Handling

- **Guide file not found**: Ask user for correct path, list available guides in `.olaf/work/staging/upgrade-guide/`
- **Guide format invalid**: Report what's missing, suggest regenerating with `generate-upgrade-guide`
- **Version detection failed**: Offer manual version input
- **Step execution failure**: Provide retry, skip, abort options with clear guidance
- **Network errors** (for steps requiring downloads): Retry with backoff, offer offline alternatives
- **Permission errors**: Suggest running with elevated permissions or fixing ownership

## Domain-Specific Rules

- Rule 1: NEVER execute any upgrade step without explicit user confirmation
- Rule 2: ALWAYS run applicability check before executing any step (unless explicitly skipped)
- Rule 3: ALWAYS create a new upgrade branch from target_branch before modifying anything — never commit directly to target_branch
- Rule 4: ALWAYS update progress tracker after each step
- Rule 5: NEVER skip breaking change steps silently — they require explicit acknowledgment
- Rule 6: If dry_run is true, show all steps but execute NONE
- Rule 7: On any failure, present rollback as the first option
- Rule 8: Track and report all skipped steps in the final summary

## Success Criteria

You WILL consider the task complete when:
- [ ] Upgrade guide loaded and parsed successfully
- [ ] Version applicability verified (or manually confirmed)
- [ ] Pre-upgrade checkpoint created
- [ ] All steps executed, skipped (with acknowledgment), or intentionally deferred
- [ ] Post-upgrade verification completed
- [ ] Progress tracker finalized
- [ ] User presented with completion summary and next steps
