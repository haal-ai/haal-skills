# Step-by-Step Tutorial

**Execute Angular Migration: Step-by-Step Tutorial**

**How to Execute the "Angular Migration Execution" Workflow**

This tutorial shows exactly how to execute an Angular migration plan using the execute-angular-migration competency. This workflow implements the migration with safety-first principles, proper git workflow, and comprehensive validation.

## Prerequisites

- Completed Angular migration plan (from plan-angular-migration skill)
- Angular project with valid angular.json and package.json
- Git repository initialized
- Required tools installed (Angular CLI, Node.js, npm/yarn)
- Clean working directory or backup created
- User approval to proceed with migration

## Step-by-Step Instructions

### Step 1: Initiate Migration Execution

[Brief description: Start the Angular migration execution process]

**User Action:**

1. Open your terminal or AI interface
2. Navigate to your Angular project directory
3. Have your migration plan ready (Plan ID or file path)
4. Execute the execute-angular-migration competency using one of these methods:
   - Direct invocation: `execute angular migration`
   - Via aliases: `run angular upgrade`, `implement angular migration`, `migrate angular`

**AI Response:**
The system will prompt you to provide the migration plan and confirm execution.

### Step 2: Provide Execution Parameters

**User Action:** Specify the migration execution details

```text
Required Parameters:
- migration_plan: Path to plan file or Plan ID (e.g., "angular-migration-app-20260123-1430")
- project_path: Path to Angular project (optional, defaults to current directory)

Optional Parameters:
- resume_from_version: Resume from specific version if partially completed
- skip_tests: Skip test execution (not recommended)
- auto_approve_phases: Auto-approve all phases (not recommended)
```

**Provide Requirements/Parameters:**

Example:
- **migration_plan**: angular-migration-enterprise-dashboard-20260123-1430
- **project_path**: ./enterprise-dashboard

**AI Response:**
```
✅ Migration plan loaded
✅ Project validated
📋 Source: Angular 13 → Target: Angular 20
🔢 Incremental: 7 version steps
⚠️ Environment upgrades: Node.js 18.19.1+ at Angular 17, Node.js 20.19.0+ at Angular 20

Proceed with execution? (y/n)
```

**User Action:** Confirm to proceed

### Step 3: Phase 0 - Pre-Flight Validation (AUTOMATIC)

[Brief description: AI performs mandatory pre-flight validation]

**AI Action:**
1. Accesses official Angular compatibility matrix
2. Validates dependency matrix access
3. Checks current Node.js version
4. Verifies Angular CLI version
5. Validates git repository status
6. Confirms environment readiness

**Expected Output:**
```markdown
## Phase 0: Pre-Flight Validation - 20260123-1430
✅ Compatibility matrix: Accessed
✅ Dependency matrix: Validated (references/angular-dependency-matrix.csv)
✅ Node.js: 16.14.0 (sufficient for Angular 13-16)
⚠️ Node.js upgrade: Required at Angular 17 (→ 18.19.1+)
⚠️ Node.js upgrade: Required at Angular 20 (→ 20.19.0+)
✅ Angular CLI: @angular/cli@13.3.0
✅ Git repository: Clean

**Status**: ✅ Ready to proceed
```

**User Action:** Review validation results, note environment upgrade points

### Step 4: Phase 1 - Preparation

[Brief description: AI prepares project for migration]

**AI Action:**
1. Creates backup commit with all current changes
2. Creates migration feature branch
3. Validates current environment
4. Runs baseline build
5. Runs baseline tests
6. Documents pre-migration state

**Expected Output:**
```markdown
## Phase 1: Preparation - COMPLETE

✅ Backup created:
   Commit: abc123def456 "chore: backup before Angular migration"
   
✅ Migration branch created:
   Branch: feature/angular-migration-13-to-20
   
✅ Baseline validation:
   Build: ✅ SUCCESS
   Tests: ✅ PASSED (142/142)
   
Ready to begin version increments? (y/n)
```

**User Action:** Confirm to proceed to migration increments

### Step 5: Phase 2.1 - First Version Increment (Angular 13 → 14)

[Brief description: AI executes first version upgrade]

**AI Action:**
1. Runs `ng update @angular/cli@14 @angular/core@14`
2. Reviews changes and commits immediately
3. Runs `ng update @angular/material@14`
4. Reviews changes and commits immediately
5. Runs build validation
6. Classifies errors vs warnings
7. Attempts to fix deprecation warnings
8. Runs tests
9. Documents increment completion

**Expected Output:**
```markdown
## Phase 2.1: Angular 13 → 14 Migration

Step 1: Core Framework Update
```bash
$ ng update @angular/cli@14 @angular/core@14
```
✅ Update applied successfully
✅ Committed: def456abc "feat: update Angular CLI and Core to v14"

Step 2: Material Update
```bash
$ ng update @angular/material@14
```
✅ Update applied successfully
✅ Committed: ghi789def "feat: update Angular Material to v14"

Step 3: Build Validation
✅ Build: SUCCESS
⚠️ Warnings: 3 found

Step 4: Warning Resolution
- ⚠️ Sass @import deprecated
  🔧 Attempting fix: Convert to @use syntax
  ✅ Fixed in 5 files
  ✅ Build: SUCCESS with fix
  ✅ Committed: jkl012ghi "fix: migrate Sass @import to @use syntax"
  
- ⚠️ TypeScript target recommendation
  📝 Deferred: Informational only, current target works
  
Step 5: Test Execution
✅ Tests: PASSED (142/142)

✅ Increment complete: Angular 13 → 14

Continue to next increment? (y/n)
```

**User Action:** Review results, approve to continue

### Step 6: Phase 2.2-2.3 - Continue Increments (Angular 14 → 15 → 16)

[Brief description: AI continues with additional version increments]

**AI Action:**
Repeats the process for each version:
- Update Core → Commit
- Update Material → Commit
- Validate build
- Fix warnings
- Run tests
- Request approval to continue

**Expected Output:**
```markdown
## Phase 2.2: Angular 14 → 15 - COMPLETE
✅ Core and Material updated
✅ Build: SUCCESS
✅ Tests: PASSED

## Phase 2.3: Angular 15 → 16 - COMPLETE
✅ Core and Material updated
✅ Build: SUCCESS
✅ Tests: PASSED
```

**User Action:** Review each increment, approve to continue

### Step 7: Phase 2.4 - Critical Node.js Upgrade (Angular 16 → 17)

[Brief description: AI handles critical environment upgrade before Angular 17]

**AI Action:**
1. **STOPS execution before Angular 17 update**
2. Detects Node.js upgrade requirement
3. Guides user through Node.js upgrade
4. Validates new Node.js version
5. Proceeds with Angular 17 update
6. Handles MDC migration

**Expected Output:**
```markdown
## Phase 2.4: Angular 16 → 17 Migration

⚠️ CRITICAL: Node.js upgrade required BEFORE this step
   Current: Node.js 16.14.0
   Required: Node.js 18.19.1+
   
STOP: Please upgrade Node.js before proceeding

Recommended:
```bash
nvm install 18.19.1
nvm use 18.19.1
node --version  # Verify 18.19.1+
```

Ready to continue after Node.js upgrade? (y/n)
```

**User Action:** Upgrade Node.js as instructed, verify version, confirm

**AI Continues:**
```markdown
✅ Node.js verified: 18.19.1

Step 1: Core Framework Update (with Node.js 18)
$ ng update @angular/cli@17 @angular/core@17
✅ Update applied successfully
✅ Committed: "feat: update Angular CLI and Core to v17"

Step 2: MDC Migration
$ ng generate @angular/material:mdc-migration
✅ MDC migration schematic applied
✅ Legacy Material components migrated to MDC

Step 3: Material Update
$ ng update @angular/material@17
✅ Update applied successfully
✅ Committed: "feat: update Angular Material to v17 with MDC"

Step 4: Build Validation
✅ Build: SUCCESS
✅ Tests: PASSED

Continue to next increment? (y/n)
```

**User Action:** Review MDC migration changes, approve to continue

### Step 8: Phase 2.5-2.6 - Continue to Angular 18, 19

[Brief description: AI continues through remaining increments]

**Expected Output:**
```markdown
## Phase 2.5: Angular 17 → 18 - COMPLETE
✅ All updates applied
✅ Build: SUCCESS
✅ Tests: PASSED

## Phase 2.6: Angular 18 → 19 - COMPLETE
✅ All updates applied
✅ Build: SUCCESS
✅ Tests: PASSED
```

### Step 9: Phase 2.7 - Final Increment with Second Node.js Upgrade (Angular 19 → 20)

[Brief description: AI handles second critical environment upgrade]

**AI Action:**
1. **STOPS execution before Angular 20 update**
2. Detects second Node.js upgrade requirement
3. Guides user through Node.js 20 upgrade
4. Proceeds with final Angular update

**Expected Output:**
```markdown
## Phase 2.7: Angular 19 → 20 Migration

⚠️ CRITICAL: Node.js upgrade required BEFORE this step
   Current: Node.js 18.19.1
   Required: Node.js 20.19.0+ or 22.12.0+

STOP: Please upgrade Node.js before proceeding

Recommended:
```bash
nvm install 20.19.0
nvm use 20.19.0
node --version  # Verify 20.19.0+
```

Ready to continue after Node.js upgrade? (y/n)
```

**User Action:** Upgrade Node.js to v20, verify, confirm

**AI Completes:**
```markdown
✅ Node.js verified: 20.19.0

$ ng update @angular/cli@20 @angular/core@20
$ ng update @angular/material@20

✅ Final version update complete
✅ Build: SUCCESS
✅ Tests: PASSED

All version increments complete! Proceeding to Phase 3...
```

### Step 10: Phase 3 - MDC Visual Validation

[Brief description: AI requests visual validation of Material components]

**AI Action:**
1. Starts development server
2. Provides checklist for visual testing
3. Waits for user confirmation

**Expected Output:**
```markdown
## Phase 3: MDC Migration Visual Validation

Please perform visual validation:

```bash
npm start
```

Visual Testing Checklist:
- [ ] Buttons render correctly
- [ ] Forms work as expected
- [ ] Dialogs appear properly
- [ ] Tables display correctly
- [ ] Custom theming applied
- [ ] Navigation components functional

Have you completed visual validation? (y/n)
```

**User Action:** Test Material components, confirm completion

### Step 11: Phase 4 - Production Deployment Validation

[Brief description: AI performs comprehensive production readiness validation]

**AI Action:**
1. Detects project integration patterns
2. Validates backend build integration (if applicable)
3. Updates CI/CD configurations (if applicable)
4. Validates git configuration
5. Generates warning resolution report
6. Runs production build
7. Creates validation checklist

**Expected Output (with Backend Integration):**
```markdown
## Phase 4: Production Deployment Validation

### Step 4.1: Backend Build Integration
✅ Maven integration detected
✅ Checking Angular output path...
   angular.json: "dist/enterprise-dashboard/browser/"
✅ Validating Maven pom.xml...
   Found: <directory>dist/enterprise-dashboard/browser/</directory>
   Status: ✅ Matches

✅ Testing Maven build:
$ mvn clean compile -pl frontend -am
   Status: ✅ SUCCESS
   Angular artifacts: ✅ Found in target/classes/static/

### Step 4.2: CI/CD Configuration
✅ Jenkinsfile detected
✅ Current Node.js: node:16
⚠️ Update required: node:20
✅ Updated: Jenkinsfile → nodejs('NodeJS 20')
✅ Committed: "chore: update Jenkinsfile Node.js to v20"

✅ Dockerfile detected
✅ Updated: FROM node:16 → FROM node:20
✅ Committed: "chore: update Dockerfile Node.js to v20"

### Step 4.3: Warning Resolution Report
Generated: warning-resolution-report-20260123-1430.md
- ✅ Fixed: 12 deprecation warnings
- 📝 Deferred: 2 optimization suggestions (user approved)

### Step 4.4: Production Build
$ npm run build --prod
✅ Build: SUCCESS
✅ Bundle sizes: Within acceptable range

### Step 4.5: Final Validation Checklist
✅ Build succeeds without errors
✅ All tests pass
✅ Warnings documented
✅ Application runs in development
✅ Production build succeeds
✅ Backend integration validated
✅ CI/CD updated
✅ Generated files not tracked

Migration validation complete!
```

**User Action:** Review validation results

### Step 12: Review Execution Log and Complete

[Brief description: AI generates final execution log]

**AI Action:**
Generates comprehensive execution log with all details

**Expected Output:**
```markdown
## Migration Execution Summary

✅ Migration completed successfully!

**Details:**
- Source: Angular 13
- Target: Angular 20
- Increments: 7 completed
- Node.js upgrades: 2 (16 → 18 → 20)
- Total commits: 18
- Build: SUCCESS
- Tests: PASSED
- Backend integration: VALIDATED
- CI/CD: UPDATED

**Generated Files:**
- Execution log: .angular-migration/execution-log.md
- Migration plan: .angular-migration/plan.md

**Next Steps:**
1. ✅ Merge migration branch to main
2. ✅ Deploy to staging environment
3. ⏸️ Perform user acceptance testing
4. ⏸️ Deploy to production
5. ⏸️ After verification, cleanup: `rm -rf .angular-migration/`

Would you like to proceed with merging the branch? (y/n)
```

**User Action:** Review execution log, decide on next steps, cleanup after successful deployment

## Common Scenarios

### Scenario A: Dependency Conflict During Execution
```markdown
❌ npm install failed with peer dependency conflict

🔍 Analyzing root cause...
   karma@^6.4.0 required by @angular-devkit/build-angular@17
   karma@~6.3.0 currently installed

✅ Applying proper fix:
$ npm install karma@~6.4.0

✅ Verifying resolution:
$ rm -rf node_modules package-lock.json
$ npm install  # Succeeds without --legacy-peer-deps
```

### Scenario B: Build Failure After Update
```markdown
❌ Build failed with compilation errors

Errors:
1. Property 'value' does not exist on AbstractControl
2. Cannot find module '@angular/common/http'

🔧 Fixing errors before proceeding...
[AI analyzes and fixes each error]

✅ Build: SUCCESS after fixes
✅ Committed: "fix: resolve compilation errors from Angular 17 update"
```

### Scenario C: Unmaintained Library Detected
```markdown
⚠️ Third-party library compatibility issue:
   ngx-charts: Last update 18 months ago
   No Angular 20 compatibility confirmed

📋 Proposing alternatives:
1. @swimlane/ngx-charts-ported (community fork)
2. chart.js with ng2-charts (official wrapper)
3. D3.js with custom components

User decision required before proceeding.
```

## Tips for Success

1. **Don't Skip Pre-Flight Validation**: Phase 0 prevents many issues
2. **Review Each Commit**: Commits show exactly what changed
3. **Note Environment Upgrades**: Node.js upgrades are critical points
4. **Test Between Increments**: Don't skip validation steps
5. **Fix Warnings Early**: Deprecation warnings become errors later
6. **Document Decisions**: Especially for deferred warnings
7. **Save Execution Log**: Valuable for troubleshooting and documentation
8. **Validate Backend Integration**: Critical for successful deployment
9. **Update CI/CD Proactively**: Prevents deployment failures
10. **Get User Approval**: Especially for deferring fixes or risky changes

## Next Steps

After completing migration execution:
1. Review all generated files (execution log, warning reports)
2. Merge migration branch to main/develop
3. Deploy to staging environment for UAT
4. Monitor for runtime issues
5. Deploy to production when validated
6. Archive migration documentation
