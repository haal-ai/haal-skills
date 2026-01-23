# PR Specificities Review Helper

**Purpose**: Analyze PR metadata, reviews, CI status, and workflows using consolidated standards

**CRITICAL**: This helper MUST load and apply the actual standards content by conducting systematic review against each standard criterion, not just referencing them.

## Comprehensive PR Analysis

### Load and Apply Standards (REQUIRED)
**BEFORE ANALYSIS**: Read the complete content of:
- `{workspace_root}\.olaf\data\practices\pr-review\comprehensive-pr-standards.md`

**THEN CONDUCT REVIEW**: Using the loaded Comprehensive PR Standards, systematically evaluate ALL aspects by applying each standard section to the actual PR data:

#### Title & Description Quality
- **Title Standards**: Action verb, scope indication, format compliance
- **Description Requirements**: Essential sections (Purpose/Why, Changes/What, Testing/How, Breaking Changes)
- **Completeness Assessment**: Complete/Partial/Minimal classification

#### CI/CD & Quality Gates  
- **Build Status**: Passing/Warning/Failing/Pending interpretation
- **Required Checks**: Security, quality metrics, testing, documentation
- **Deployment Readiness**: Green/Yellow/Red light assessment

#### Review Workflow & Approvals
- **Approval Requirements**: Standard/Critical/Security/Breaking change thresholds
- **Review Quality**: Specific, actionable, categorized feedback standards
- **Conflict Resolution**: Documentation, escalation, decision recording process

#### Branch Management
- **Naming Conventions**: Type/ticket/description pattern compliance
- **Branch Health**: Target appropriateness, freshness, conflicts, protection
- **Merge Strategy**: Feature/Release/Hotfix strategy selection

### Assessment Output
Generate findings using the standards' unified framework:
- **Ready to Merge** checklist validation
- **Needs Attention** issue identification  
- **Blocks Merge** critical issue flagging

## Severity Classification

### HIGH Priority Issues
- **Failed CI**: Critical build/test failures
- **Security Vulnerabilities**: Critical or high-severity findings
- **Conflicting Reviews**: Unresolved disagreements blocking progress
- **Missing Requirements**: Essential information or approvals absent
- **Branch Conflicts**: Major merge conflicts or protection violations

### MEDIUM Priority Issues
- **Incomplete Description**: Missing sections but core info present
- **Minor CI Issues**: Warnings or optional check failures
- **Workflow Deviations**: Process not followed but not blocking
- **Approval Gaps**: Missing preferred but not required approvals
- **Branch Age**: Moderate staleness requiring attention

### LOW Priority Issues
- **Style Issues**: PR metadata formatting or naming preferences
- **Documentation Gaps**: Nice-to-have information missing
- **Process Suggestions**: Improvements for future PRs
- **Minor Quality**: Below-threshold but acceptable metrics
- **Enhancement Opportunities**: Performance or maintainability improvements

## Integration Guidelines

### Comprehensive Analysis (Always Applied)
- Execute all four analysis sections (PR Description, CI/CD Status, Review Workflow, Branch Workflow)
- Apply complete severity classification (HIGH/MEDIUM/LOW)
- Cover all aspects: security, workflow, quality, and compliance automatically
- Generate detailed findings documentation and recommendations

### Use with review-github-pr
1. Load this helper in Phase 2 of PR review process
2. Read standards content completely 
3. Extract actual PR data from analyzer output
4. Systematically review PR against each standard section
5. Execute comprehensive analysis across all four areas
6. Classify findings by severity (HIGH/MEDIUM/LOW)  
7. Integrate results with code analysis from review-diff 
8. Generate unified recommendations and action plan

### Standalone Usage
- Provides comprehensive PR metadata assessment covering all aspects
- Supports complete workflow compliance auditing
- Enables thorough process improvement identification
- Always applies full analysis without configuration choices