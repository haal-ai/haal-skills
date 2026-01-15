# Comprehensive PR Review Standards

**Purpose**: Unified standards for evaluating all aspects of pull requests - description quality, CI/CD status, review workflow, and branch management

## PR Title & Description Quality

### Title Standards
- **Clear action verb**: fix, add, update, remove, refactor
- **Scope indication**: component/module affected  
- **Concise**: under 50 characters when possible
- **Format**: Use imperative mood, capitalize first word, no trailing punctuation

#### Quality Examples
- ✅ **Good**: "Fix authentication timeout in user service"
- ❌ **Poor**: "Various fixes", "Updates", "WIP"

### Description Requirements
**Essential Sections:**
- **Purpose/Why**: Problem solved, business justification, linked issues
- **Changes/What**: Summary of modifications, key files affected
- **Testing/How**: Test cases, manual testing, regression notes
- **Breaking Changes**: API changes, migration steps needed

#### Completeness Assessment
- **Complete**: All sections present with meaningful content
- **Partial**: Some sections missing or insufficient detail  
- **Minimal**: Only basic description provided

## CI/CD & Quality Gates

### Build & Test Status
- ✅ **Passing**: All mandatory checks successful
- ⚠️ **Warning**: Passes with warnings (review required)
- ❌ **Failing**: Build/test failures block merge
- 🔄 **Pending**: In progress or queued

### Required Checks
- **Security**: SAST, dependency scans, secret detection
- **Quality**: Code coverage >80%, complexity <10, duplication <3%
- **Testing**: Unit, integration, E2E tests passing
- **Documentation**: API docs, README updates

### Deployment Readiness
- **Green Light**: All mandatory checks pass, no critical issues
- **Yellow Light**: Optional checks fail, manual verification needed
- **Red Light**: Mandatory checks fail, blocks merge

## Review Workflow & Approvals

### Approval Requirements
- **Standard Changes**: 1 peer approval
- **Critical Systems**: 2 senior approvals
- **Security/Performance**: Domain expert approval
- **Breaking Changes**: Product owner + tech lead

### Review Quality Standards
- **Specific**: Point to exact lines/issues
- **Actionable**: Clear improvement steps
- **Categorized**: Must Fix / Should Fix / Consider / Question
- **Complete**: Covers functionality, quality, security, performance

### Conflict Resolution
1. Document disagreement clearly
2. Gather additional context/requirements  
3. Escalate to senior member if needed
4. Record decision rationale
5. Update all reviewers

## Branch Management

### Naming Conventions
- **Pattern**: `type/TICKET-123-short-description`
- **Types**: feature, bugfix, hotfix, release, support
- **Rules**: Lowercase, hyphens only, <50 chars, include ticket reference

#### Examples
- ✅ **Good**: `feature/AUTH-145-oauth-integration`
- ❌ **Poor**: `feature/stuff`, `temp-fix`

### Branch Health
- **Target Branch**: Appropriate for change type (features→develop, hotfix→main)
- **Freshness**: <30 days from target, includes latest changes
- **Conflicts**: Resolved before merge
- **Protection**: Complies with branch protection rules

### Merge Strategy
- **Feature Branches**: Squash merge for clean history
- **Release Branches**: Merge commit to preserve history
- **Hotfixes**: Rebase merge for immediate application

## Severity Classification

### HIGH Priority (Block Merge)
- Failed mandatory CI checks
- Critical security vulnerabilities  
- Unresolved review conflicts
- Missing required approvals
- Major merge conflicts

### MEDIUM Priority (Review Required)
- Incomplete description (missing sections)
- Minor CI warnings
- Workflow deviations
- Missing preferred approvals
- Branch staleness

### LOW Priority (Document & Track)
- Style/formatting issues
- Documentation gaps
- Process improvement suggestions
- Minor quality metrics below target

## Quick Assessment Checklist

### ✅ Ready to Merge
- [ ] Clear title and complete description
- [ ] All mandatory CI checks passing
- [ ] Required approvals obtained
- [ ] No unresolved conflicts or comments
- [ ] Proper branch naming and targeting

### ⚠️ Needs Attention  
- [ ] Minor issues documented
- [ ] Optional checks failing
- [ ] Workflow deviations noted
- [ ] Reviewer feedback addressed

### ❌ Blocks Merge
- [ ] Critical failures identified
- [ ] Security vulnerabilities present
- [ ] Required approvals missing
- [ ] Unresolved conflicts exist