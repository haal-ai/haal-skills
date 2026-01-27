---
name: plan-angular-migration
description: Creates comprehensive Angular migration plans with chapter-based analysis (Discovery, Compatibility, Planning, Roadmap). Use when asked to plan Angular version upgrades, analyze migration feasibility, or create migration strategies for Angular projects.
license: Apache-2.0
metadata:
  olaf_tags: [angular, migration, planning, upgrade, compatibility]
  copyright: Copyright (c) 2026 sahmed
  author: sahmed (on github)
  repository: https://github.com/haal-ai/haal-skills
  provider: Haal AI
---

<olaf>

if you are in need to get the date and  time, use time tools, fallback to shell command if needed

**MANDATORY**: before doing anything else, read fully the `.olaf/team-delegation.md` file and apply its requirements strictly.

# Angular Migration Planning

This skill creates detailed, chapter-based migration plans for Angular version upgrades. It performs comprehensive discovery, compatibility analysis, planning, and generates actionable implementation roadmaps.

## Migration Artifacts Directory

**Convention**: All migration artifacts are stored in `.angular-migration/` directory at project root.

**Directory Structure**:
```
.angular-migration/
├── plan.md                    # Generated migration plan (THIS SKILL)
├── execution-log.md           # Real-time execution progress (execute skill)
└── findings/                  # Optional: Chapter analysis artifacts
    ├── current-state.json
    ├── dependencies.json
    └── breaking-changes.md
```

**Workflow**:
1. Planning skill creates `.angular-migration/` and saves `plan.md`
2. User reviews plan: `cat .angular-migration/plan.md`
3. User commits plan: `git add .angular-migration/ && git commit -m "docs: add migration plan"`
4. Execute skill reads from `.angular-migration/plan.md`
5. After successful migration: Delete `.angular-migration/` directory

## When to Use This Skill

Use this skill when you need to:
- Plan an Angular version upgrade (e.g., Angular 13 → Angular 20)
- Analyze Angular migration feasibility and risks
- Create a comprehensive migration strategy
- Generate a detailed implementation roadmap
- Assess Angular project dependencies and compatibility

## Chapter-Based Planning Process

The planning follows a 4-chapter workflow. Each chapter builds on the previous one:

### Chapter 0: Pre-Planning Validation (Execute BEFORE Chapter 1)

**CRITICAL: This chapter prevents reactive failures during execution**

**Step 0.1: Official Angular Compatibility Matrix Access (MANDATORY)**
```bash
# Access https://angular.dev/reference/versions BEFORE generating migration plan
# Extract Node.js, npm, TypeScript requirements for target Angular version
# Document environment upgrade points (e.g., Angular 17 requires Node.js 18.19.1+)
# Validation: Current environment vs. requirements matrix
```

**Purpose**: Prevents reactive environment validation failures during execution

**Step 0.2: Architecture Pattern Detection (CONDITIONAL)**

Only execute if micro-frontend patterns are suspected:
```bash
# Check for Native Federation (CRITICAL for version alignment)
grep -r "native-federation" package.json package-lock.json 2>/dev/null
find . -name "federation.config.js" -o -name "federation.manifest.json" 2>/dev/null

# Check for Module Federation  
grep -r "module-federation" package.json package-lock.json 2>/dev/null

# Check for ADF (Amadeus Design Factory)
grep -r "@design-factory/design-factory" package.json 2>/dev/null
```

**Step 0.3: Dependency Matrix Access**

Access bundled dependency matrix for third-party library versions:
```bash
# Bundled resource: references/angular-dependency-matrix.csv
# Contains exact compatible versions for Design Factory, Bootstrap CSS, Ng-Bootstrap,
# Ng-select, Ag-grid, ngx-slider, and AgnosUI for each Angular version
# CRITICAL: Always use EXACT versions from this matrix, never "latest"
```

**Additional Compatibility Resources**:
- See [references/compatibility-matrix.md](references/compatibility-matrix.md) for:
  - Official Angular version support matrix
  - Node.js/npm/TypeScript requirements per Angular version
  - Critical upgrade points (Angular 17, 20)
  - MDC migration requirements
  - Research protocols for unmaintained packages

**Chapter 0 Output Requirements**:
```markdown
## Chapter 0: Pre-Planning Validation Summary
**Timestamp**: YYYYMMDD-HHmm

### Official Compatibility Matrix Results
- **Source**: https://angular.dev/reference/versions
- **Target Angular Version**: [target_version]
- **Node.js Required**: [version]
- **npm Required**: [version]
- **TypeScript Required**: [version]
- **Environment Upgrade Needed**: YES/NO
- **Upgrade Point**: [At which Angular version]

### Architecture Detection
- **Native Federation**: Detected/Not Detected
- **Module Federation**: Detected/Not Detected
- **ADF Integration**: Detected/Not Detected
- **Micro-Frontend Pattern**: YES/NO

### Dependency Matrix Access
- **Status**: Bundled (references/angular-dependency-matrix.csv)
- **Compatibility Guide**: references/compatibility-matrix.md
```

### Chapter 1: Discovery and Current State Analysis

**Objective**: Comprehensive analysis of current Angular project

**Process**:
1. **Angular Project Structure Analysis**
   - Analyze `angular.json` and workspace configuration
   - Document current Angular version from `package.json`
   - Identify Angular CLI version
   - Map project structure (apps, libraries)

2. **Framework Dependency Discovery**
   - Angular Material usage and version
   - Angular CDK, Flex Layout, Animations
   - RxJS version
   - TypeScript version
   - Current Node.js version

3. **Angular-Specific Features**
   - Routing configuration and lazy loading
   - Services, guards, interceptors, resolvers
   - Forms patterns (reactive vs template-driven)
   - State management (services, NgRx, Akita)
   - Testing setup (Jasmine, Karma, Protractor)
   - Build configuration (webpack, esbuild)
   - Angular Universal (SSR) implementation
   - PWA features and service workers
   - i18n setup and locales
   - Animations usage

4. **Third-Party Library Inventory**
   - Comprehensive catalog of all non-Angular dependencies with versions
   - Identify critical libraries for compatibility research

5. **Micro-Frontend Architecture Discovery (CONDITIONAL)**

   Only if patterns detected in Chapter 0:
   - Native Federation configuration analysis
   - Module Federation webpack configuration
   - ADF component usage and SCSS integration
   - Shared dependency mapping across micro-frontends
   - Inter-MF communication patterns

6. **Environment Assessment**
   - Document current Node.js version
   - Check for previous migration attempts
   - Assess current build and deployment setup

### Chapter 2: Compatibility Assessment and Gap Analysis

**Objective**: Detailed compatibility analysis between source and target versions

**Process**:
1. **Incremental Version Analysis**

   If incremental upgrade requested, analyze each intermediate version:
   ```
   Example: Angular 13 → 20
   Analyze: 13→14, 14→15, 15→16, 16→17, 17→18, 18→19, 19→20
   ```

2. **Breaking Changes Assessment**
   - Use Angular update guide URLs for each version:
     `https://angular.dev/update-guide?v=[current]-[next]&l=1`
   - Reference Angular LLM documentation: `https://angular.dev/llms.txt`
   - Identify API changes, deprecated features, removed functionality

3. **Angular Material Compatibility**
   - Check Material Design Components (MDC) migration requirements (Angular 17+)
   - Verify Material version compatibility for each step
   - Plan theming and component migration

4. **RxJS Compatibility**
   - Analyze RxJS version requirements
   - Identify deprecated operators
   - Plan operator migration patterns

5. **TypeScript Compatibility**
   - Check TypeScript version requirements for target Angular
   - Assess strict mode implications
   - Plan TypeScript upgrades

6. **Node.js Version Compatibility (CRITICAL)**

   **Environment Upgrade Planning**:
   ```markdown
   ### Node.js Version Requirements by Angular Version
   - **Angular 13-16**: Node.js 16.14.0+ required
   - **Angular 17-19**: Node.js 18.19.1+ required (CRITICAL UPGRADE POINT)
   - **Angular 20+**: Node.js 20.19.0+ or 22.12.0+ required (CRITICAL UPGRADE POINT)
   
   ### Decision Tree
   Current Node.js version < Required for target Angular?
     ↓ YES
     Plan Node.js upgrade BEFORE that Angular version increment
     Document: "Node.js upgrade to [version] required before Angular [version]"
     ↓ NO
     Continue with current Node.js version
   ```

7. **Build System Changes**
   - Webpack → esbuild transition assessment
   - Build configuration impacts
   - Bundle optimization opportunities

8. **Testing Framework Migration**
   - Karma → Web Test Runner migration needs
   - Test framework compatibility

9. **Third-Party Library Research Strategy**
   - Plan external npm package research workflow
   - Identify potentially incompatible libraries
   - Research alternatives for unmaintained packages

10. **Build Integration Assessment (CONDITIONAL)**

    Only if backend integration detected:
    ```markdown
    ### Build Tool Integration Assessment
    **Purpose**: Only applicable if Angular is integrated with a backend build system
    
    **Step 1: Detect Integration Pattern**
    - Check if Angular is part of a larger build (monorepo, polyrepo, standalone)
    - Identify if backend build consumes Angular artifacts
    
    **Step 2: IF Backend Integration Detected, Assess:**
    - **Build System Type**: Maven / Gradle / npm scripts / Make / CMake / other
    - **Current Angular Output Path**: dist/ or dist/[project]/browser/
    - **Potential Output Path Changes**: Angular 17+ may change output structure
    - **Integration Points**: Where build artifacts are consumed
    - **Plan Validation**: Include validation in Phase 4 roadmap
    
    **Step 3: Document Integration Context:**
    - Integration Type: Monorepo / Polyrepo / Standalone / Backend-integrated
    - Backend Technology: Java / .NET / Node.js / Python / None
    - Build Artifact Flow: Angular → Backend build → Final artifact
    ```

11. **CI/CD Configuration Assessment (CONDITIONAL)**

    Only if CI/CD configuration exists:
    ```markdown
    ### CI/CD Configuration Planning
    **Purpose**: Only applicable if CI/CD configuration files exist
    
    **Step 1: Detect CI/CD Presence**
    - Search for: Jenkinsfile, .github/workflows, .gitlab-ci.yml, azure-pipelines.yml, etc.
    - IF NOT FOUND: Skip CI/CD planning
    
    **Step 2: IF CI/CD Detected, Assess:**
    - **CI/CD System**: Jenkins / GitHub Actions / GitLab CI / Azure Pipelines / CircleCI
    - **Current Node.js Version in CI/CD**: [version]
    - **Node.js Update Required**: YES/NO at [Angular version]
    - **Docker Usage**: Check Dockerfile, assess Node.js version
    - **Plan Updates**: Include configuration updates in roadmap
    ```

### Chapter 3: Migration Planning and Strategy

**Objective**: Comprehensive migration strategy and execution plan

**Process**:
1. **Generate Plan ID for State Management**
   - **Format**: `angular-migration-[project_name]-[YYYYMMDD-HHmm]`
   - **Usage**: For state file management during execution
   - **Example**: `angular-migration-qcp-dashboard-20250925-1530`

2. **Migration Approach Decision**
   - Incremental (version-by-version) vs. Direct upgrade
   - Big-bang vs. Feature-flag based migration
   - Parallel development strategy

3. **Incremental Migration Strategy (If Selected)**
   - Create step-by-step plan for each version increment
   - Define validation checkpoints between versions
   - Plan rollback procedures for each step

4. **Angular CLI Migration Command Sequence**
   ```bash
   # Example for incremental Angular 13 → 14
   ng update @angular/cli@14 @angular/core@14
   ng update @angular/material@14
   # ... additional commands
   ```

5. **Version-Specific Planning**
   - For each intermediate version:
     - Specific upgrade tasks
     - Validation steps
     - Testing requirements
     - Risk mitigation

6. **Dependency Upgrade Sequencing**
   - Plan Core framework updates
   - Plan Material updates (must come after core)
   - Plan third-party library updates
   - Plan custom library migrations

7. **Testing Strategy**
   - Unit test migration approach
   - E2E test framework migration
   - Test coverage requirements
   - Validation criteria

8. **State Management Integration**
   ```json
   {
     "plan_id": "[generated_plan_id]",
     "migration_type": "angular",
     "source_version": "[current_angular_version]",
     "target_version": "[target_angular_version]",
     "incremental_upgrade": true|false,
     "node_js_requirements": {
       "current": "[current_node_version]",
       "required_for_target": "[required_node_version]",
       "upgrade_needed": true|false
     }
   }
   ```

9. **External Research Workflow**
   - npm package research protocol
   - Compatibility validation strategy
   - Alternative library evaluation process

10. **Risk Assessment and Mitigation**
    - High Risk: Critical blockers, environment conflicts
    - Medium Risk: Library incompatibilities, major refactoring
    - Low Risk: Minor updates, documentation changes

### Chapter 4: Implementation Roadmap and Final Report

**Objective**: Generate actionable implementation roadmap

**Process**:
1. **Detailed Implementation Steps**

   Generate step-by-step roadmap based on incremental or direct approach:
   
   **For Incremental Upgrades**:
   ```markdown
   ### Phase 1: Environment Preparation
   - [ ] Backup project
   - [ ] Create migration branch
   - [ ] Upgrade Node.js to [version] (if needed)
   - [ ] Verify npm/yarn version
   
   ### Phase 2: Angular 13 → 14 Migration
   - [ ] Run: ng update @angular/cli@14 @angular/core@14
   - [ ] Commit changes: "feat: update Angular CLI and Core to v14"
   - [ ] Run: ng update @angular/material@14
   - [ ] Commit changes: "feat: update Angular Material to v14"
   - [ ] Run tests: npm test
   - [ ] Run build: npm run build
   - [ ] Validate application
   
   ### Phase 3: Angular 14 → 15 Migration
   [Similar steps...]
   ```

2. **Angular CLI Commands with Proper Sequencing**
   ```bash
   # CRITICAL: Commit between Core and Material updates
   ng update @angular/cli@X @angular/core@X
   git add . && git commit -m "feat: update Angular CLI and Core to vX"
   
   ng update @angular/material@X
   git add . && git commit -m "feat: update Angular Material to vX"
   ```

3. **Code Transformation Examples**
   - Provide specific examples of deprecated API replacements
   - RxJS operator migration patterns
   - Material component updates (legacy → MDC)
   - TypeScript fixes

4. **Environment Setup Implementation**
   ```bash
   # Check current Node.js version
   node --version
   
   # If upgrade needed, use nvm
   nvm install 18.19.1
   nvm use 18.19.1
   
   # Verify version
   node --version
   ```

5. **Build Integration Validation Steps (CONDITIONAL)**

   Only if backend integration detected:
   ```markdown
   ### Backend Build Validation
   1. Update backend build configuration (pom.xml / build.gradle / etc.)
   2. Update Angular output path references
   3. Test backend build
   4. Verify Angular artifacts in expected location
   ```

6. **CI/CD Configuration Updates (CONDITIONAL)**

   Only if CI/CD detected:
   ```markdown
   ### CI/CD Updates
   1. Update Dockerfile Node.js version (if exists)
   2. Update CI/CD pipeline Node.js version
   3. Test CI/CD build pipeline
   ```

7. **Material Design Components (MDC) Migration**

   For Angular 17+ targets:
   ```markdown
   ### MDC Migration Steps
   1. Run: ng update @angular/material --migrate-only
   2. Update custom theme configurations
   3. Test Material components visually
   4. Update component usage patterns
   ```

8. **Warning Resolution Strategy**
   - Deprecation warnings: Attempt to fix all
   - Optimization suggestions: Document and get user approval
   - Safety pattern preservation: Keep unless explicitly approved

9. **Validation Criteria**
   - Build succeeds without errors
   - All tests pass
   - No blocking warnings
   - Application runs correctly
   - Performance acceptable

10. **Rollback Procedures**
    ```bash
    # If migration fails at any point
    git reset --hard [previous-commit]
    npm install
    ```

## Planning Output Format

**Primary Output**: `.angular-migration/plan.md` (MANDATORY)

**Creation**:
```bash
# Create migration artifacts directory
mkdir -p .angular-migration/findings

# Generate plan file
cat > .angular-migration/plan.md << 'EOF'
[Plan content here]
EOF
```

**Plan File Structure**: `.angular-migration/plan.md`

```markdown
# Angular Migration Analysis: [project_name]
**Generated**: YYYYMMDD-HHmm
**Source**: Angular [source_version]
**Target**: Angular [target_version]
**Plan ID**: [generated_plan_id]
**Status**: Complete

## Executive Summary
- Migration approach: [Incremental/Direct]
- Estimated effort: [X weeks]
- Risk level: [High/Medium/Low]
- Node.js upgrade required: [YES/NO] at Angular [version]

## Chapter 0: Pre-Planning Validation
[Pre-planning validation results]

## Chapter 1: Discovery and Current State
[Discovery findings]

## Chapter 2: Compatibility Assessment
[Compatibility analysis]

## Chapter 3: Migration Planning
[Migration strategy]

## Chapter 4: Implementation Roadmap
[Detailed implementation steps]

### Execution Context for Migration
```json
{
  "plan_id": "angular-migration-[project]-[timestamp]",
  "migration_type": "angular",
  "source_version": "[source]",
  "target_version": "[target]",
  "incremental_upgrade": true|false,
  "node_js_requirements": {
    "current": "[version]",
    "required_for_target": "[version]",
    "upgrade_needed": true|false
  }
}
```
```

## Critical Planning Rules

### Rule 1: Chapter 0 Execution
- **MANDATORY**: Execute Chapter 0 pre-planning validation BEFORE all other chapters
- Access official compatibility matrix BEFORE generating plan
- Validate dependency matrix and prepare research protocol

### Rule 2: User-Specified Target Version
- **MANDATORY**: Use exact target_angular_version specified by user
- **NEVER** auto-select LTS or latest version

### Rule 3: Proactive Environment Planning
- **MANDATORY**: Plan Node.js upgrades BEFORE Angular versions that require them
- Document clear "BEFORE Angular X" instructions

### Rule 4: Incremental Upgrade Planning
- If user requests incremental upgrade, plan version-by-version
- Generate increment for each major version step
- Plan validation checkpoints between versions

### Rule 5: Context-Aware Planning
- Detect project integration pattern (standalone vs backend-integrated)
- **CONDITIONAL**: Include build integration validation IF integration detected
- **CONDITIONAL**: Include CI/CD updates IF CI/CD detected

### Rule 6: Git Workflow Planning
- Plan commits between Core and Material updates
- Never suggest git stash - use commits only
- Plan structured commit messages

### Rule 7: Safety-First Planning
- Plan to preserve runtime safety patterns
- Never plan to use --force without explicit justification
- Plan proper dependency conflict resolution (no --legacy-peer-deps by default)

### Rule 8: External Resource Planning
- Plan to use Angular update guide URLs during execution
- Plan npm package research workflow
- Plan alternative library evaluation

### Rule 9: State Management
- Generate unique plan_id
- Prepare execution context for stateful migration

### Rule 10: Architecture-Specific Planning
- **CONDITIONAL**: If Native Federation detected, plan version alignment with Angular
- **CONDITIONAL**: If NgRx detected, plan migration to standalone providers for Angular 19+
- **CONDITIONAL**: If i18n detected, plan @angular/localize setup

## User Communication

**Progress Updates**:
- Confirmation when Chapter 0 validation complete
- Status after each chapter completion
- Clear indication of chapter dependencies

**Completion Summary**:
- All chapters completed
- Plan ID generated
- Execution context prepared
- Report location provided

**Next Steps**:
- Migration plan ready for review
- Can proceed with execution using execute-angular-migration skill
- State management prepared for execution tracking

## Error Handling

**Invalid Angular Project**:
- Verify angular.json and package.json exist
- Check for valid Angular project structure

**Unsupported Angular Versions**:
- Validate against official Angular release timeline
- Suggest alternative versions if specified version invalid

**Missing Target Version**:
- Prompt user to specify exact desired target version
- Do not assume or auto-select version

**Environment Insufficient**:
- Document environment upgrade requirements
- Provide clear upgrade path

## Success Criteria

Planning is complete when:
- [ ] Chapter 0 pre-planning validation completed
- [ ] Official Angular compatibility matrix accessed and documented
- [ ] Architecture patterns detected (if applicable)
- [ ] All 4 chapters completed
- [ ] Angular project structure validated
- [ ] Source and target version compatibility analyzed
- [ ] Angular ecosystem dependencies assessed
- [ ] Unique plan_id generated
- [ ] Execution context prepared
- [ ] Node.js version requirements assessed proactively
- [ ] Environment upgrade points identified and documented
- [ ] Third-party library research strategy documented
- [ ] Material Design Components migration planned (for Angular 17+)
- [ ] Project integration pattern detected
- [ ] Build integration validation planned (IF integration detected)
- [ ] CI/CD configuration updates planned (IF CI/CD detected)
- [ ] `.angular-migration/` directory created at project root
- [ ] Plan saved to `.angular-migration/plan.md`
- [ ] User instructed to review and commit plan

## Bundled Resources

This skill includes reference documentation to support Angular migration planning:

### references/angular-dependency-matrix.csv
Exact compatible versions for third-party libraries across Angular versions:
- Design Factory, Bootstrap CSS, Ng-Bootstrap, Ng-select
- Ag-grid, ngx-slider, AgnosUI

**Usage**: Consult in Chapter 0 and Chapter 2 for third-party library compatibility analysis.

**Critical Rule**: Always use EXACT versions from this matrix, never "latest" or version ranges.

### references/compatibility-matrix.md
Comprehensive Angular version compatibility reference:
- Official Angular version support (Node.js, npm, TypeScript, RxJS)
- Critical upgrade points (Angular 17→Node 18, Angular 20→Node 20)
- Angular Material MDC migration requirements
- Breaking changes resources and research protocols
- Unmaintained package handling procedures

**Usage**: Load this reference when:
- Analyzing environment compatibility in Chapter 0
- Assessing breaking changes in Chapter 2
- Planning environment upgrades in Chapter 3
- Researching third-party library compatibility

</olaf>
