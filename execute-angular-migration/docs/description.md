# Execute Angular Migration

## Overview

This competency executes Angular migration plans step-by-step with a safety-first approach, proper git workflow management, comprehensive validation including backend integration testing, and proactive environment validation to prevent reactive failures.

## Purpose

Angular migrations require careful execution to avoid breaking changes, dependency conflicts, and deployment failures. This competency implements migration plans with strict safety protocols including proactive environment validation, proper commit sequencing, root-cause dependency resolution, warning classification and fixing, backend build integration validation, and comprehensive testing to ensure successful migrations from development through production deployment.

## Usage

**Command**: `execute angular migration` (or aliases: `run angular upgrade`, `implement angular migration`, `migrate angular`)

**Protocol**: Act (with explicit user approval for each phase)

**When to Use**: Use when you have a completed Angular migration plan and are ready to execute the upgrade, when resuming a partially completed migration, or when validating migration results after implementation.

## Parameters

### Required Inputs
- **migration_plan**: Path to migration plan file or Plan ID
- **project_path**: Path to Angular project (defaults to current directory)

### Optional Inputs
- **resume_from_version**: Resume from specific Angular version if partially completed
- **skip_tests**: Skip test execution (not recommended, defaults to false)
- **auto_approve_phases**: Auto-approve all phases (not recommended, defaults to false)

### Context Requirements
- Completed Angular migration plan (from plan-angular-migration skill)
- Angular project with valid angular.json and package.json
- Git repository initialized and clean (or with backup)
- Required tools installed (Angular CLI, Node.js, npm/yarn)
- User approval for execution

## Output

Executes migration plan with comprehensive validation and generates execution log.

**Deliverables**:
- **Phase 0**: Pre-flight validation (compatibility matrix, dependency matrix, environment validation)
- **Phase 1**: Preparation (backup, branch creation, environment setup, baseline validation)
- **Phase 2**: Incremental migration execution (version-by-version upgrades with proper git workflow)
- **Phase 3**: MDC migration (Angular 17+ only)
- **Phase 4**: Production deployment validation (backend integration, CI/CD, functional testing)
- **Git commits**: Structured commits after each update with detailed messages
- **Warning resolution report**: Documentation of all warnings fixed or deferred
- **Functional test report**: Testing results for replaced libraries (if applicable)
- **Execution log**: Complete migration execution documentation

**Format**: Markdown execution log saved to `.angular-migration/execution-log.md`

## Examples

### Example 1: Complete Incremental Migration Execution

**Scenario**: Execute planned Angular 13 → 20 migration with backend integration

**Command**:
```
execute angular migration
```

**Input**:
```
migration_plan: angular-migration-enterprise-dashboard-20260123-1430
project_path: ./enterprise-dashboard
```

**Execution Steps**:
```markdown
Phase 0: Pre-Flight Validation ✅
- Compatibility matrix verified
- Node.js 16.14.0 sufficient for Angular 13-16
- Environment ready

Phase 1: Preparation ✅
- Backup created: commit SHA abc123
- Branch: feature/angular-migration-13-to-20
- Baseline build: SUCCESS
- Baseline tests: PASSED

Phase 2.1: Angular 13 → 14 ✅
- Core update: commit SHA def456
- Material update: commit SHA ghi789
- Build: SUCCESS
- Tests: PASSED
- Warnings: 3 fixed, 1 deferred (user approved)

Phase 2.2: Angular 14 → 15 ✅
[Similar steps...]

Phase 2.3: Angular 16 → 17 ✅
- NODE UPGRADE: 16.14.0 → 18.19.1 ✅
- Core update with new Node.js
- Material MDC migration
- Build: SUCCESS
- Tests: PASSED

[Continue through Angular 18, 19...]

Phase 2.6: Angular 19 → 20 ✅
- NODE UPGRADE: 18.19.1 → 20.19.0 ✅
- Core update with new Node.js
- Build: SUCCESS
- Tests: PASSED

Phase 3: MDC Migration ✅
- Visual validation completed

Phase 4: Production Validation ✅
- Backend build (Maven): SUCCESS
- Angular artifacts in correct location
- CI/CD updated: Jenkinsfile Node.js → 20
- Dockerfile updated: node:20
- Generated files removed from git
- Functional testing: All passed

✅ Migration completed successfully
```

**Result**: Successfully migrated from Angular 13 to 20 with all validation passed, ready for production deployment.

### Example 2: Migration with Dependency Conflict Resolution

**Scenario**: Execute Angular 15 → 18 migration encountering karma version conflict

**Command**:
```
execute angular migration
```

**During Phase 2.2 (Angular 16 → 17)**:
```markdown
❌ Dependency conflict detected:
   karma@^6.4.0 required by @angular-devkit/build-angular@17.0.0
   karma@~6.3.0 installed

🔍 Root cause analysis:
- karma version mismatch
- Need to update to compatible version within range

✅ Resolution applied:
npm install karma@~6.4.0

✅ Verification:
rm -rf node_modules package-lock.json
npm install  # Succeeds WITHOUT --legacy-peer-deps
npm run build  # SUCCESS

📝 Committed: "fix: update karma to v6.4.0 for Angular 17 compatibility"
```

**Result**: Dependency conflict resolved properly without using --legacy-peer-deps, migration continued successfully.

### Example 3: Resumed Partial Migration

**Scenario**: Resume migration that was interrupted at Angular 16

**Command**:
```
execute angular migration
```

**Input**:
```
migration_plan: angular-migration-app-20260120-1000
resume_from_version: 16
```

**Execution**:
```markdown
✅ Detected existing progress:
- Completed: Angular 13 → 14, 14 → 15, 15 → 16
- Current: Angular 16 (verified in package.json)
- Resuming: Angular 16 → 17

Phase 0: Pre-Flight Validation ✅
Phase 1: Skipped (already prepared)
Phase 2: Resuming from Angular 16 → 17
- NODE UPGRADE: 16.x → 18.19.1+ required
[Continue execution...]
```

**Result**: Successfully resumed and completed migration from Angular 16 to target version.

## Related Competencies

- **plan-angular-migration**: Required prerequisite competency that generates the migration plan
- **review-diff**: Can be used to review changes after each version increment
- **git-add-commit**: Generic git operations (though execute-angular-migration handles commits)

## Tips & Best Practices

- Always execute Phase 0 pre-flight validation before starting
- Never skip tests unless absolutely necessary (and document why)
- Commit after EACH version increment - never batch commits
- Commit between Core and Material updates (critical for clean git history)
- Attempt to fix ALL deprecation warnings before proceeding
- Never use --legacy-peer-deps as first solution for dependency conflicts
- Always investigate root cause of conflicts and apply proper fixes
- Validate backend integration if project is integrated with backend build
- Update CI/CD configurations proactively (Docker, Jenkinsfile, etc.)
- Test replaced library functionality thoroughly before completion
- Save execution log for documentation and troubleshooting
- Use structured commit messages for clear migration history
- Don't proceed if build fails - fix errors immediately
- Get user approval before deferring warning fixes
- Preserve runtime safety patterns unless explicitly approved to remove
