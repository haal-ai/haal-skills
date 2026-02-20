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
