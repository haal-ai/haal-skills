---
name: execute-angular-migration
description: Executes Angular migration plans step-by-step with safety-first approach, git workflow management, and comprehensive validation. Use when asked to execute Angular migration, run Angular upgrade, or implement Angular migration plan.
license: Apache-2.0
metadata:
  olaf_tags: [angular, migration, execution, upgrade, implementation]
  copyright: Copyright (c) 2026 sahmed
  author: sahmed (on github)
  repository: https://github.com/haal-ai/haal-skills
  provider: Haal AI
---

<olaf>

if you are in need to get the date and  time, use time tools, fallback to shell command if needed

**MANDATORY**: before doing anything else, read fully the `.olaf/team-delegation.md` file and apply its requirements strictly.

# Angular Migration Execution

This skill executes Angular migration plans with a safety-first approach, proper git workflow, dependency conflict resolution, and comprehensive validation including backend integration testing.

## Migration Artifacts Directory

**Convention**: All migration artifacts are stored in `.angular-migration/` directory at project root.

**Directory Structure**:
```
.angular-migration/
├── plan.md                    # Migration plan from plan skill (REQUIRED INPUT)
├── execution-log.md           # Real-time execution log (THIS SKILL)
└── findings/                  # Optional artifacts from planning phase
```

**Workflow**:
1. Verify `.angular-migration/plan.md` exists (created by plan skill)
2. Create `.angular-migration/execution-log.md` at execution start
3. Update execution log after each phase completion
4. After successful migration: Prompt user to delete directory

**Cleanup**:
```bash
rm -rf .angular-migration/
```

## When to Use This Skill

Use this skill when you need to:
- Execute an Angular migration plan
- Run Angular version upgrade commands
- Implement Angular migration step-by-step
- Resume a partially completed Angular migration
- Validate Angular migration results

## Prerequisites

**Required**:
- Completed Angular migration plan at `.angular-migration/plan.md`
- Angular project with valid angular.json and package.json
- Git repository initialized
- User approval for execution

**Validation**:
1. Verify `.angular-migration/plan.md` exists and is complete
2. Check project structure matches plan assumptions
3. Verify required tools installed (Angular CLI, Node.js, npm/yarn)
4. Confirm git repository is clean or has backup

## Execution Phases

### Phase 0: Pre-Flight Validation (Execute FIRST)

**MANDATORY: Execute BEFORE any migration commands**

**Step 0.0: Verify Migration Plan**
```bash
# Verify plan file exists
if [ ! -f .angular-migration/plan.md ]; then
  echo "❌ Error: Migration plan not found at .angular-migration/plan.md"
  echo "Please run plan-angular-migration skill first"
  exit 1
fi

# Display plan summary
cat .angular-migration/plan.md
```

**Step 0.1: Official Angular Compatibility Matrix Access**
```bash
# Access https://angular.dev/reference/versions to verify requirements
# Confirm Node.js, npm, TypeScript versions match plan
```

**Step 0.2: Dependency Matrix Access**
```bash
# Bundled resource: references/angular-dependency-matrix.csv
# This matrix provides EXACT versions for third-party libraries:
# - Design Factory, Bootstrap CSS, Ng-Bootstrap, Ng-select
# - Ag-grid, ngx-slider, AgnosUI
# CRITICAL: Always use exact versions from matrix, never use "latest"
```

**Additional Resources**:
- See [references/compatibility-matrix.md](references/compatibility-matrix.md) for:
  - Official Node.js/TypeScript/npm requirements
  - Critical upgrade points (Angular 17→Node 18, Angular 20→Node 20)
  - MDC migration timing and requirements
  - GitHub research protocols
  - Unmaintained package handling

**Step 0.3: GitHub Research Protocol**

For ALL third-party libraries being updated:
```bash
# Research npm package compatibility BEFORE updating
# Check GitHub issues for compatibility problems
# Search: "[library-name] angular [target-version]"
# Identify unmaintained packages (>6 months no updates)
```

**Step 0.4: Environment Validation**
```bash
# Check current Node.js version
node --version

# Compare with Angular requirements:
# Angular 13-16: Node.js 16.14.0+
# Angular 17-19: Node.js 18.19.1+ (CRITICAL UPGRADE POINT)
# Angular 20+: Node.js 20.19.0+ or 22.12.0+

# If insufficient, STOP execution and guide user to upgrade
nvm install [required-version]
nvm use [required-version]
```

**Phase 0 Output**:
```markdown
## Phase 0: Pre-Flight Validation - YYYYMMDD-HHmm
✅ Compatibility matrix accessed
✅ Dependency matrix validated
✅ GitHub research protocol prepared
✅ Node.js version: [version] (sufficient/needs upgrade)
✅ Angular CLI version: [version]
✅ Git repository: clean/dirty

**Status**: Ready to proceed / STOP (environment upgrade needed)
```

### Phase 1: Preparation

**Step 1.1: Project Backup**
```bash
# Create backup before starting
git add .
git commit -m "chore: backup before Angular migration

Pre-migration state:
- Angular: [current_version]
- Node.js: [current_version]
- All tests passing"

# Optional: Create backup branch
git branch backup-pre-migration-$(date +%Y%m%d)
```

**Step 1.2: Create Migration Branch**
```bash
git checkout -b feature/angular-migration-[source]-to-[target]
```

**Step 1.3: Environment Setup**
```bash
# Verify Node.js version
node --version

# If upgrade needed (from Phase 0 validation)
nvm use [required-version]
```

**Step 1.4: Initial Build Validation**
```bash
# Verify project builds successfully before migration
npm run build

# Verify tests pass
npm test

# Document baseline
echo "✅ Pre-migration build: SUCCESS"
echo "✅ Pre-migration tests: PASSED"
```

### Phase 2: Incremental Migration Execution

**CRITICAL GIT WORKFLOW RULES**:
- **Rule GIT-1**: ALWAYS commit after EACH Angular version increment
- **Rule GIT-2**: ALWAYS commit between Core and Material updates
- **Rule GIT-3**: NEVER use `git stash` - use commits for clean history
- **Rule GIT-4**: Use structured commit messages with version details
- **Rule GIT-5**: Commit BEFORE attempting next `ng update` command
- **Rule GIT-6**: One commit per logical update step

**Common Mistake Pattern (AVOID THIS)**:
```bash
ng update @angular/cli@X @angular/core@X
ng update @angular/material@X  
# ❌ FAILS with: "Repository is not clean. Please commit or stash any changes"
```

**Correct Proactive Pattern (DO THIS)**:
```bash
ng update @angular/cli@X @angular/core@X
git add . && git commit -m "feat: update Angular CLI and Core to vX"  # ✅ Commit proactively
ng update @angular/material@X  # ✅ Succeeds with clean repo
git add . && git commit -m "feat: update Angular Material to vX"  # ✅ Commit Material changes
```

**Commit Message Template**:
```bash
git commit -m "feat: update [component] to version [X]

- [Package 1]: [old version] → [new version]
- [Package 2]: [old version] → [new version]
- Migrations applied: [list key changes]
- Build status: [success/warnings/errors]
- Test status: [passed/failed/skipped]"
```

**For Each Version Increment**:

**Step 2.1: External Resource Reference**
```bash
# Reference Angular update guide for specific version
# URL: https://angular.dev/update-guide?v=[current]-[next]&l=1
# Review breaking changes and migration notes
```

**Step 2.2: Core Framework Update**
```bash
# Update Angular CLI and Core together
ng update @angular/cli@[version] @angular/core@[version]

# IMMEDIATELY commit (required for next step)
git add .
git commit -m "feat: update Angular CLI and Core to v[version]

- @angular/cli: [old] → [new]
- @angular/core: [old] → [new]
- Migrations applied by Angular CLI
- Build status: pending validation
- Test status: pending validation"
```

**Step 2.3: Build Validation**
```bash
# Validate build after core update
npm run build 2>&1 | tee build-output.log

# Classify result
# Exit code = 0: Success or warnings only
# Exit code ≠ 0: Build failure (must fix before proceeding)
```

**Step 2.4: Error vs Warning Classification**

**If build succeeds (exit code 0) with warnings**:
```markdown
✅ Build: SUCCESS
⚠️ Warnings found: [count]

Warnings to address:
1. [Warning 1] - [Deprecation/Optimization/Info]
2. [Warning 2] - [Deprecation/Optimization/Info]

Action: Attempt to fix deprecation warnings before continuing
```

**If build fails (exit code ≠ 0)**:
```markdown
❌ Build: FAILED
Errors found: [count]

Critical errors:
1. [Error 1] - [Description]
2. [Error 2] - [Description]

Action: STOP and fix errors before proceeding
```

**Step 2.5: Warning Resolution Protocol**

**MANDATORY: Attempt to fix ALL deprecation warnings**

For each deprecation warning:
```markdown
1. Research recommended fix:
   - Check Angular update guide
   - Search for migration pattern
   - Review official documentation

2. Implement fix in isolation:
   - Apply the fix
   - Test build

3. Decision:
   IF build succeeds with fix:
     - Keep the fix
     - Commit with clear message
   
   IF build fails with fix:
     - Revert the fix
     - Document why warning persists
     - Get user approval to defer

4. Documentation (MANDATORY):
   ✅ Fixed: [warning] - [solution applied]
   ⚠️ Deferred: [warning] - [reason why fix not possible]
   📝 Ignored: [warning] - [explicit justification with user approval]
```

**Example: Sass @import Deprecation**:
```scss
// Warning: Sass @import is deprecated
// FROM:
@import "variables.scss";

// TO:
@use "variables.scss" as vars;

// Update variable references:
// FROM: $primary-color
// TO: vars.$primary-color
```

**Step 2.6: Material Update (After Core is Committed)**
```bash
# CRITICAL: Only run this after Core update is committed
ng update @angular/material@[version]

# IMMEDIATELY commit
git add .
git commit -m "feat: update Angular Material to v[version]

- @angular/material: [old] → [new]
- @angular/cdk: [old] → [new]
- Material migrations applied
- Build status: pending validation
- Test status: pending validation"
```

**Step 2.7: Dependency Conflict Resolution (If Occurs)**

**CRITICAL: NEVER use --legacy-peer-deps as first solution**

**Root Cause Identification (MANDATORY)**:
```bash
# Capture full error
npm install 2>&1 | tee npm-error.log

# Parse specific conflict
grep "ERESOLVE" npm-error.log
# Identify:
# - Which package is causing the conflict?
# - What version does it require?
# - What version is currently installed?
```

**Conflict Analysis**:
| Conflict Type | Solution | Example |
|---------------|----------|---------|
| Version mismatch within range | Update to compatible version | karma ~6.3.0 → ~6.4.0 |
| Major version incompatibility | Update parent package first | Update Angular first, then RxJS |
| Transitive dependency | Update root dependency | Update @angular-eslint |

**Proper Fix Application**:
```bash
# ❌ WRONG (masks problem):
npm install --legacy-peer-deps

# ✅ RIGHT (fixes root cause):
# If karma conflict: "karma@^6.4.0" required but "~6.3.0" installed
npm install karma@~6.4.0  # Update to compatible version
npm install  # Now succeeds without flags
```

**Verification (MANDATORY)**:
```bash
# Remove lock file and node_modules
rm -rf node_modules package-lock.json

# Clean install to verify resolution
npm install  # Must succeed WITHOUT --legacy-peer-deps

# Verify build
npm run build  # Must succeed
```

**WHEN --legacy-peer-deps is ACCEPTABLE (rare)**:
1. ✅ Root cause fully investigated and documented
2. ✅ Proper fix attempted and proven impossible
3. ✅ Technical justification documented
4. ✅ Risk assessment completed
5. ✅ Explicit user approval obtained
6. ✅ **NEVER in production build files** (pom.xml, build.gradle)

**Step 2.8: Test Execution**
```bash
# Run tests after update
npm test

# Document results
# All passed: ✅ Tests: PASSED
# Some failed: ⚠️ Tests: [X] failed - investigate and fix
```

**Step 2.9: Third-Party Library Research (If Needed)**

For libraries showing compatibility issues:
```bash
# Research library on GitHub
# Search: "[library-name] angular [version]"
# Check: Last commit date, open issues, Angular compatibility

# Decision tree:
IF library maintained AND compatible:
  - Update to compatible version
  
IF library unmaintained (>6 months):
  - Research alternatives
  - Propose replacement
  - Get user approval
  
IF no alternative exists:
  - Check if functionality can be implemented in-house
  - Propose custom implementation
  - Get user approval
```

**Step 2.10: Increment Complete - User Review**
```markdown
## Version Increment Complete: Angular [old] → [new]

### Status Summary
- ✅ Core framework updated and committed
- ✅ Material updated and committed (if applicable)
- ✅ Build: SUCCESS / FAILED
- ✅ Tests: PASSED / FAILED
- ⚠️ Warnings: [count] - [X] fixed, [Y] deferred

### Commits Created
- [commit SHA]: feat: update Angular CLI and Core to v[version]
- [commit SHA]: feat: update Angular Material to v[version]

### Ready to proceed to next increment? (y/n)
```

### Phase 3: Material Design Components (MDC) Migration

**Only for Angular 17+ migrations**

**Step 3.1: Run MDC Migration Schematic**
```bash
ng update @angular/material --migrate-only

# Review changes
git diff

# Commit
git add .
git commit -m "feat: migrate to Material Design Components (MDC)

- Migrated legacy Material components to MDC
- Updated component usage patterns
- Theme configuration updated"
```

**Step 3.2: Visual Validation**
```bash
# Start development server
npm start

# Manual testing checklist:
# - [ ] Buttons render correctly
# - [ ] Forms work as expected
# - [ ] Dialogs appear properly
# - [ ] Tables display correctly
# - [ ] Custom theming applied
```

### Phase 4: Production Deployment Validation

**CRITICAL: This phase prevents deployment failures**

**Step 4.1: Build Integration Validation (CONDITIONAL)**

**Only execute if backend integration exists**

**Detect Backend Integration**:
```bash
# Check for backend build system integration
find . -name "pom.xml" -o -name "build.gradle" -o -name "Makefile" -o -name "CMakeLists.txt"
grep -r "dist/" . --include="*.xml" --include="*.gradle" --include="Makefile" 2>/dev/null
```

**IF Backend Integration Detected, Validate Angular Output Path**:
```bash
# Check if Angular output path changed
cat angular.json | grep outputPath
# Common changes:
# - Old: "outputPath": "dist/"
# - New (Angular 17+): "outputPath": "dist/[project-name]/browser/"
```

**Validate Build Configuration Based on System**:

**IF Maven detected** (pom.xml):
```bash
# Check Maven resource copying
grep -r "dist/" */pom.xml
# Look for <resources> or <resource> tags
# Verify path matches angular.json outputPath

# Test Maven build
mvn clean compile -pl [module-name] -am

# Validate artifacts
find . -type d -name "static" -o -name "resources" | xargs ls -la
```

**IF Gradle detected** (build.gradle):
```bash
# Check Gradle copy tasks
grep -r "dist/" */build.gradle

# Test Gradle build
./gradlew clean build

# Validate artifacts
find . -path "*/build/resources/*" -type d | xargs ls -la
```

**IF npm scripts detected**:
```bash
# Check package.json for build integration
cat package.json | grep -A5 "scripts"
grep -E "cp|copy|mv|move|dist" package.json
```

**IF Mismatch Detected, Fix**:
```markdown
1. Identify build configuration file (pom.xml, build.gradle, etc.)
2. Locate Angular output directory references
3. Update path to match angular.json outputPath
4. Test backend build process
5. Verify Angular artifacts in expected location
```

**IF No Backend Integration**:
```markdown
✅ No backend integration detected - Skipping build integration validation
   Angular is standalone or backend build is independent
```

**Step 4.2: CI/CD Configuration Validation (CONDITIONAL)**

**Only execute if CI/CD or Docker exists**

**Detect CI/CD and Docker**:
```bash
# Search for CI/CD configuration
find . \( -name "Dockerfile" -o \
         -name "Dockerfile.*" -o \
         -name "Jenkinsfile" -o \
         -name ".github" -o \
         -name ".gitlab-ci.yml" -o \
         -name "azure-pipelines.yml" -o \
         -name ".circleci" \) -type f -o -type d 2>/dev/null
```

**IF Dockerfile Found, Validate Node.js Version**:
```bash
# Check Node.js version
find . -name "Dockerfile*" -exec grep -H "FROM node" {} \;

# Required versions:
# Angular 17-19: node:18 or node:18-alpine
# Angular 20+: node:20 or node:20-alpine or node:22
```

**Update Dockerfile** (if mismatch):
```dockerfile
# FROM:
FROM node:16

# TO:
FROM node:20  # or node:18 for Angular 17-19
```

**IF CI/CD Configuration Found**:

**Detect Node.js version in CI/CD**:
```bash
# Search for Node.js references
grep -r "node.*[0-9][0-9]" . \
  --include="Jenkinsfile" \
  --include="*.yml" \
  --include="*.yaml" \
  2>/dev/null | grep -E "node|nodejs|nvm"
```

**Update Based on Detected System**:

**GitHub Actions** (.github/workflows/):
```yaml
# Update node-version in workflow files
- uses: actions/setup-node@v3
  with:
    node-version: '20'  # Update to required version
```

**GitLab CI** (.gitlab-ci.yml):
```yaml
# Update image
image: node:20  # Update to required version
```

**Azure Pipelines** (azure-pipelines.yml):
```yaml
# Update NodeVersion
- task: NodeTool@0
  inputs:
    versionSpec: '20.x'  # Update to required version
```

**Jenkins** (Jenkinsfile):
```groovy
// Update nodejs version
nodejs('NodeJS 20')  // Update to required version
```

**CircleCI** (.circleci/config.yml):
```yaml
# Update docker image
docker:
  - image: cimg/node:20.0  # Update to required version
```

**IF No CI/CD or Docker**:
```markdown
✅ No CI/CD or Docker detected - Skipping CI/CD validation
   Deployment may be manual or use different method
```

**Step 4.3: Git Configuration Validation (CONDITIONAL)**

**Only if generated files are tracked by git**

**Detect Tracked Generated Files**:
```bash
# Find Angular build artifacts in git
git ls-files | grep -E "dist/.*\.(js|css|html|ico)|build/.*\.(js|css|html)"

# Check backend integration patterns
git ls-files | grep -E "resources/static.*\.(js|css|html)|wwwroot/.*\.(js|css)|public/static.*\.(js|css)"
```

**IF Generated Files Found, Update .gitignore**:
```bash
# Check current .gitignore
cat .gitignore | grep -E "dist/|build/|static/"

# Add to .gitignore if needed
echo "" >> .gitignore
echo "# Angular build artifacts (added during migration)" >> .gitignore
echo "/dist/" >> .gitignore
echo "/build/" >> .gitignore

# For backend-integrated projects:
echo "[path-to-backend-static]/*" >> .gitignore
echo "![path-to-backend-static]/.gitkeep" >> .gitignore
```

**Remove Tracked Files**:
```bash
# Remove from git tracking (keep files locally)
git rm --cached [detected-generated-files]
git add .gitignore
git commit -m "chore: ignore generated Angular build artifacts

- Add build artifacts to .gitignore
- Remove tracked generated files
- Prevents merge conflicts on generated files"
```

**IF No Generated Files Tracked**:
```markdown
✅ No generated files tracked - .gitignore already correct
   Build artifacts properly ignored
```

**Step 4.4: Warning Resolution Report**

**Document all warning resolutions**:
```markdown
## Build Warnings Resolution - YYYYMMDD-HHmm

### Deprecation Warnings
- ✅ **Sass @import**: Converted to @use syntax (30 files)
  - Solution: Replaced @import with @use and namespaced variables
  - Files: styles.scss, [components].scss
  - Commit: [SHA]

- ⚠️ **TypeScript target**: Recommended browserslist config
  - Status: Deferred
  - Reason: Current ES2020 target works correctly
  - Risk: Low - informational only
  - User approved: [date]

### Optimization Suggestions
- 📝 **Optional chaining removal**: 25 occurrences
  - Decision: Keep optional chaining for runtime safety
  - Rationale: Prioritizing safety over performance
  - User approved: [date]
```

**Step 4.5: Functional Testing Requirements**

**For any replaced library or major functionality**:

**Identify Affected Features**:
```markdown
## Feature Testing Plan: [Library Name] Replacement
Component | Feature | Test Steps | Expected Result | Status
----------|---------|------------|-----------------|-------
[name] | Export | Click export button | File downloads | ⏸️ Pending
[name2] | Filter | Apply filter | Data filtered | ⏸️ Pending
```

**Execute Tests**:
```markdown
IF backend required for testing:
  - Document backend setup steps
  - Mark tests as "Pending - Requires Backend"
  - Provide user with testing checklist

IF frontend-only testing possible:
  - Execute tests manually or automated
  - Document results
  - Fix failures before marking complete
```

**Test Report**:
```markdown
## Test Execution Report - YYYYMMDD-HHmm
### Library Replaced: [old] → [new]

- ✅ Passed: Export functionality
- ✅ Passed: Filter functionality
- ⏸️ Pending: Search (requires backend)
- ❌ Failed: Pagination - Fixed in commit [SHA]

### User Testing Required:
1. Start backend: npm run backend
2. Test export in: ComponentA, ComponentB
3. Verify file format matches
```

**Step 4.6: Final Production Build**
```bash
# Run production build
npm run build --prod

# Verify build succeeds
echo "Exit code: $?"

# Check bundle sizes
ls -lh dist/[project-name]/browser/

# Document results
```

**Step 4.7: Complete Validation Checklist**
```markdown
## Migration Validation Checklist

### Core Validation
- [ ] Build succeeds without errors
- [ ] All tests pass
- [ ] No blocking warnings (or all documented with approval)
- [ ] Application runs in development mode
- [ ] Production build succeeds

### Integration Validation (Conditional)
- [ ] Backend build integration tested (IF APPLICABLE)
- [ ] Docker build succeeds (IF APPLICABLE)
- [ ] CI/CD pipeline updated and tested (IF APPLICABLE)
- [ ] Generated files not tracked by git (IF APPLICABLE)

### Quality Validation
- [ ] Deprecation warnings addressed or documented
- [ ] Replaced library functionality tested
- [ ] Performance acceptable
- [ ] No security vulnerabilities introduced

### Documentation
- [ ] All commits follow structured format
- [ ] Warning resolution report complete
- [ ] Test report complete (or pending with user)
- [ ] Migration log generated
```

## Execution Output Format

**Primary Output**: `.angular-migration/execution-log.md` (MANDATORY)

**Creation**:
```bash
# Create execution log at start
cat > .angular-migration/execution-log.md << 'EOF'
[Execution log content]
EOF
```

**Log File Structure**: `.angular-migration/execution-log.md`

```markdown
# Angular Migration Execution Log
**Started**: YYYYMMDD-HHmm
**Completed**: YYYYMMDD-HHmm
**Status**: Completed / In Progress / Failed

## Environment
- **Angular CLI**: [version]
- **Node.js**: [version]
- **Package Manager**: npm/yarn/pnpm
- **TypeScript**: [version]
- **Angular Material**: [version]
- **RxJS**: [version]

## Migration Summary
- **Source**: Angular [source]
- **Target**: Angular [target]
- **Incremental**: YES/NO
- **Increments Completed**: [X] of [Y]

## Phase 0: Pre-Flight Validation
[Phase 0 results]

## Phase 1: Preparation
[Phase 1 results]

## Phase 2: Version Increments
### Increment 1: Angular [X] → [Y]
**Status**: ✅ Completed
**Commits**: [commit SHAs]
**Build**: SUCCESS
**Tests**: PASSED
**Warnings**: [count] - [fixed/deferred]

## Phase 3: MDC Migration
[Phase 3 results if applicable]

## Phase 4: Validation
### Build Integration (IF APPLICABLE)
[Results]

### CI/CD Updates (IF APPLICABLE)
[Results]

### Warning Resolution
[Summary]

### Functional Testing
[Results]

## Issues and Resolutions
[Any problems and solutions]

## Final Status
✅ Migration completed successfully
✅ All validation passed
✅ Ready for deployment

## Next Steps
1. Merge migration branch
2. Deploy to staging environment
3. Perform user acceptance testing
4. Deploy to production
```

## Critical Execution Rules

### Pre-Flight Rules
- **Rule 0-1**: ALWAYS execute Phase 0 validation BEFORE any migration commands
- **Rule 0-2**: ALWAYS access official compatibility matrix and dependency matrix
- **Rule 0-3**: ALWAYS validate Node.js version before starting
- **Rule 0-4**: STOP execution if environment insufficient - guide user to upgrade

### Git Workflow Rules
- **Rule GIT-1**: ALWAYS commit after EACH Angular version increment
- **Rule GIT-2**: ALWAYS commit between Core and Material updates
- **Rule GIT-3**: NEVER use git stash - use commits only
- **Rule GIT-4**: Use structured commit messages
- **Rule GIT-5**: Commit BEFORE attempting next ng update

### Safety Rules
- **Rule SAF-1**: NEVER remove runtime safety patterns without explicit user approval
- **Rule SAF-2**: NEVER use --force flags without explaining risks and getting approval
- **Rule SAF-3**: ALWAYS classify errors vs warnings correctly
- **Rule SAF-4**: ALWAYS attempt to fix deprecation warnings before proceeding

### Dependency Rules
- **Rule DEP-1**: ALWAYS use EXACT versions from dependency matrix
- **Rule DEP-2**: NEVER use "latest" or numerically matching versions
- **Rule DEP-3**: NEVER use --legacy-peer-deps as first solution
- **Rule DEP-4**: ALWAYS investigate root cause of peer dependency conflicts
- **Rule DEP-5**: NEVER add --legacy-peer-deps to production build files

### Environment Rules
- **Rule ENV-1**: NEVER update global Angular CLI
- **Rule ENV-2**: ALWAYS validate Node.js proactively in Phase 0
- **Rule ENV-3**: STOP if Node.js upgrade needed - guide user first

### Validation Rules (Phase 4)
- **Rule VAL-1**: ALWAYS detect project integration pattern
- **Rule VAL-2**: IF backend integration detected, validate build configuration
- **Rule VAL-3**: IF CI/CD detected, update configurations
- **Rule VAL-4**: IF generated files tracked, update .gitignore
- **Rule VAL-5**: ALWAYS attempt to fix deprecation warnings
- **Rule VAL-6**: ALWAYS test replaced library functionality

### User Interaction Rules
- **Rule UI-1**: NEVER execute without user approval for each phase
- **Rule UI-2**: ALWAYS provide clear status after each step
- **Rule UI-3**: ALWAYS get approval before major changes
- **Rule UI-4**: ALWAYS explain risks for high-risk operations

## Error Handling

**Build Failures (Exit Code ≠ 0)**:
- Stop execution immediately
- Analyze error messages
- Provide specific fix recommendations
- Do not proceed until fixed

**Dependency Conflicts**:
- Investigate root cause first
- Apply proper fix (update to compatible version)
- Verify with clean install
- Document resolution

**Test Failures**:
- Identify failing tests
- Analyze failure reasons
- Fix or document why deferring
- Get user approval if deferring

**Environment Issues**:
- Stop execution if Node.js insufficient
- Guide user to upgrade environment
- Resume after environment ready

**Backend Integration Failures**:
- Identify misconfiguration
- Provide generic fix approach
- Test backend build
- Verify artifacts

## Success Criteria

Execution is complete when:
- [ ] Phase 0 pre-flight validation completed
- [ ] All version increments executed successfully
- [ ] All updates committed with proper git workflow
- [ ] Build succeeds without errors
- [ ] Tests pass (or failures documented with user approval)
- [ ] Deprecation warnings addressed or documented
- [ ] Backend integration validated (IF APPLICABLE)
- [ ] CI/CD updated (IF APPLICABLE)
- [ ] Generated files not tracked (IF APPLICABLE)
- [ ] Functional testing complete or user plan provided
- [ ] Production build succeeds
- [ ] Execution log generated at `.angular-migration/execution-log.md`
- [ ] User approval obtained for completion
- [ ] User prompted to delete `.angular-migration/` directory after verification

## Bundled Resources

This skill includes reference documentation to support Angular migration execution:

### references/angular-dependency-matrix.csv
Exact compatible versions for third-party libraries across Angular versions:
- Design Factory, Bootstrap CSS, Ng-Bootstrap, Ng-select
- Ag-grid, ngx-slider, AgnosUI

**Usage**: MANDATORY consultation in Phase 0 pre-flight validation and for EVERY third-party library update.

**Critical Rule**: Always use EXACT versions from this matrix. Never use "latest", "^" ranges, or numerically matching versions without matrix verification.

**Example Usage**:
```bash
# Correct: Use exact version from matrix
npm install @design-factory/design-factory@17.0.1

# Wrong: Using "latest" without matrix verification
npm install @design-factory/design-factory@latest  # ❌ NEVER DO THIS
```

### references/compatibility-matrix.md
Comprehensive Angular version compatibility reference:
- Official Angular version support matrix (Node.js, npm, TypeScript, RxJS)
- Critical environment upgrade points
- Angular Material MDC migration timing and procedures
- GitHub compatibility research protocols
- npm registry verification commands
- Unmaintained package detection and handling
- Version selection priority rules

**Usage**: Load this reference when:
- Executing Phase 0 pre-flight validation
- Validating environment sufficiency
- Planning environment upgrades (Node.js, npm)
- Researching third-party library compatibility on GitHub
- Handling dependency conflicts
- Determining version selection priority

</olaf>
