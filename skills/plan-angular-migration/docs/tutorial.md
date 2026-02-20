# Step-by-Step Tutorial

**Plan Angular Migration: Step-by-Step Tutorial**

**How to Execute the "Angular Migration Planning" Workflow**

This tutorial shows exactly how to create a comprehensive Angular migration plan using the plan-angular-migration competency. This workflow performs chapter-based analysis and generates an actionable implementation roadmap.

## Prerequisites

- Angular project with valid angular.json and package.json
- Knowledge of current Angular version
- Target Angular version decided
- Access to project codebase
- Node.js and npm/yarn installed

## Step-by-Step Instructions

### Step 1: Initiate Migration Planning

[Brief description: Start the Angular migration planning process by invoking the plan-angular-migration competency]

**User Action:**

1. Open your terminal or AI interface
2. Navigate to your Angular project directory
3. Execute the plan-angular-migration competency using one of these methods:
   - Direct invocation: `plan angular migration`
   - Via aliases: `plan angular upgrade`, `angular migration plan`, `create angular migration strategy`

**AI Response:**
The system will prompt you to provide the required parameters for migration planning.

### Step 2: Provide Migration Parameters

**User Action:** Specify the migration details

```text
Required Parameters:
- source_angular_version: Current Angular version (e.g., "13", "16.2.0")
- target_angular_version: Desired target version (e.g., "20", "19.0.0")
- project_path: Path to Angular project (optional, defaults to current directory)

Optional Parameters:
- project_name: Name for plan identification (e.g., "enterprise-dashboard")
- incremental_upgrade: Version-by-version migration (default: true for multi-version)
- backend_integration: Backend build system if applicable (e.g., "Maven", "Gradle")
- architecture_notes: Special patterns like "Native Federation micro-frontend"
```


**Provide Requirements/Parameters:**

Example:
- **source_angular_version**: 13
- **target_angular_version**: 20
- **project_name**: enterprise-dashboard
- **incremental_upgrade**: true
- **backend_integration**: Maven

**AI Response:**
The system will validate parameters and begin Chapter 0 pre-planning validation.

### Step 3: Chapter 0 - Pre-Planning Validation

[Brief description: AI performs pre-planning validation including compatibility matrix access and architecture detection]

**AI Action:**
1. Accesses official Angular compatibility matrix at https://angular.dev/reference/versions
2. Extracts Node.js, npm, TypeScript requirements for target version
3. Detects architectural patterns (Native Federation, Module Federation, ADF)
4. Validates dependency matrix access
5. Documents environment upgrade requirements

**Expected Output:**
```markdown
## Chapter 0: Pre-Planning Validation Summary
**Timestamp**: 20260123-1430

### Official Compatibility Matrix Results
- **Target Angular Version**: 20
- **Node.js Required**: 20.19.0+ or 22.12.0+
- **npm Required**: 10.x
- **TypeScript Required**: 5.7+
- **Environment Upgrade Needed**: YES
- **Upgrade Points**: Angular 17 (Node 18.19.1+), Angular 20 (Node 20.19.0+)

### Architecture Detection
- **Native Federation**: Not Detected
- **Module Federation**: Not Detected
- **ADF Integration**: Not Detected
- **Micro-Frontend Pattern**: NO

### Dependency Matrix Access
- **Status**: Bundled (references/angular-dependency-matrix.csv)
- **Compatibility Guide**: references/compatibility-matrix.md
```

**User Action:** Review Chapter 0 validation results

### Step 4: Chapter 1 - Discovery and Current State Analysis

[Brief description: AI analyzes current Angular project structure, dependencies, and features]

**AI Action:**
1. Analyzes angular.json and package.json
2. Documents current Angular version (e.g., 13.3.0)
3. Catalogs framework dependencies (Material, CDK, RxJS, TypeScript)
4. Identifies Angular-specific features (routing, forms, state management, testing)
5. Creates comprehensive third-party library inventory
6. Assesses current environment (Node.js version, build setup)

**User Action:** Review discovery findings for accuracy

### Step 5: Chapter 2 - Compatibility Assessment and Gap Analysis

[Brief description: AI performs detailed compatibility analysis for each version increment]

**AI Action:**
1. Analyzes each incremental version (13→14, 14→15, ..., 19→20)
2. Identifies breaking changes using Angular update guide URLs
3. Assesses Angular Material compatibility and MDC migration (Angular 17+)
4. Validates RxJS and TypeScript compatibility
5. **CRITICAL**: Documents Node.js upgrade requirements
6. Plans build system changes (webpack → esbuild)
7. Identifies testing framework migrations
8. Creates third-party library research strategy

**User Action:** Review compatibility assessment and confirm understanding of critical upgrade points

### Step 6: Chapter 3 - Migration Planning and Strategy

[Brief description: AI creates comprehensive migration strategy with command sequencing]

**AI Action:**
1. Generates unique Plan ID: `angular-migration-enterprise-dashboard-20260123-1430`
2. Decides on incremental approach (13→14→...→20)
3. Creates Angular CLI command sequence with git commit strategy
4. Plans version-specific tasks for each increment
5. Sequences dependency upgrades (Core → Material → third-party)
6. Defines testing strategy and validation criteria
7. Prepares state management integration
8. Documents external research workflow
9. Assesses risks and mitigation strategies

**User Action:** Review migration strategy and approve approach

### Step 7: Chapter 4 - Implementation Roadmap and Final Report

[Brief description: AI generates actionable step-by-step implementation roadmap]

**AI Action:**
1. Creates detailed implementation steps for each phase
2. Documents Angular CLI commands with proper sequencing
3. Provides code transformation examples
4. Plans environment setup steps
5. Includes backend build validation (if applicable)
6. Plans CI/CD configuration updates (if applicable)
7. Documents MDC migration steps (Angular 17+)
8. Creates warning resolution strategy
9. Defines validation criteria and rollback procedures

**User Action:** Review complete implementation roadmap

### Step 8: Review Migration Plan Report

[Brief description: Review the generated migration plan report]

**AI Action:**
Generates final report file at:
`.angular-migration/plan.md`

**User Action:** 
1. Review complete migration plan
2. View plan: `cat .angular-migration/plan.md`
3. Confirm understanding of critical upgrade points
4. Note Plan ID for execution phase
5. Commit plan to git: `git add .angular-migration/ && git commit -m "docs: add Angular migration plan"`

### Step 9: Confirm Readiness for Execution

[Brief description: Confirm plan is ready for execution phase]

**User Action:**
1. Review all critical Node.js upgrade points
2. Confirm understanding of incremental approach
3. Note testing requirements between versions
4. Verify rollback procedures are clear
5. Approve plan for execution

**AI Response:**
```
✅ Migration plan complete
✅ Plan ID: angular-migration-enterprise-dashboard-20260123-1430
✅ Ready for execution using execute-angular-migration competency
```

## Common Scenarios

### Scenario A: Discovering Native Federation
If AI detects Native Federation during Chapter 0, planning includes:
- Version alignment requirements
- Shared dependency coordination
- Federation configuration updates

### Scenario B: Backend Build Integration
If Maven/Gradle integration detected, planning includes:
- Build configuration updates
- Output path reference changes
- Backend build validation checkpoints

### Scenario C: Unmaintained Package
If unmaintained package discovered (>6 months no updates), planning includes:
- Alternative library research protocol
- Migration strategy to replacement
- Risk mitigation for continued use

## Tips for Success

1. **Be Specific with Versions**: Provide exact versions (e.g., "13.3.0") for more accurate planning
2. **Document Architecture**: Mention micro-frontends or special patterns upfront
3. **Review Chapter 0 Carefully**: Environment upgrade requirements are critical
4. **Save Plan ID**: You'll need it for execution tracking
5. **Confirm Incremental Path**: Multi-version jumps are safer with incremental approach
6. **Review Bundled Resources**: Check angular-dependency-matrix.csv and compatibility-matrix.md
7. **Ask Questions**: Clarify any unclear steps before proceeding to execution

## Next Steps

After completing migration planning:
1. Save migration plan report file
2. Review with team if applicable
3. Proceed to execution using `execute-angular-migration` competency
4. Use Plan ID for state tracking during execution
5. Follow roadmap step-by-step with validation checkpoints
