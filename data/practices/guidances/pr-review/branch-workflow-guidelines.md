# Branch Workflow Standards

**Purpose**: Standards for branch naming, merge strategies, and workflow compliance

## Branch Naming Conventions

### Standard Patterns
- **Feature**: `feature/JIRA-123-short-description`
- **Bugfix**: `bugfix/JIRA-456-fix-description`  
- **Hotfix**: `hotfix/JIRA-789-critical-fix`
- **Release**: `release/v1.2.3`
- **Support**: `support/maintenance-task`

### Naming Rules
- Use lowercase with hyphens (kebab-case)
- Include ticket/issue reference when applicable
- Keep description concise but meaningful
- Avoid special characters except hyphens
- Maximum 50 characters total length

### Quality Assessment
- ✅ **Good**: `feature/AUTH-145-oauth-integration`
- ❌ **Poor**: `feature/stuff`, `john-dev-branch`, `temp-fix`

## Base Branch Validation

### Target Branch Rules
- **Features**: Target `develop` or `main` branch
- **Hotfixes**: Target `main` with backport to `develop`
- **Releases**: Target `main` from `develop`
- **Experiments**: Target feature branches, not main branches

### Branch Protection Checks
- Target branch exists and is accessible
- Target branch has appropriate protection rules
- User has permission to merge to target
- Target branch is not archived or locked

### Freshness Validation
- Source branch is recent (< 30 days from target)
- Source branch includes latest target changes
- No significant drift from target branch
- Dependencies and configurations current

## Merge Strategy Compliance

### Merge Methods
- **Merge Commit**: Preserves complete history, used for features
- **Squash Merge**: Clean history, used for small fixes
- **Rebase Merge**: Linear history, used for individual commits

### Strategy Selection Criteria
- **Feature Branches**: Squash merge for clean history
- **Release Branches**: Merge commit to preserve version history  
- **Hotfix Branches**: Rebase merge for immediate application
- **Long-running Features**: Merge commit to preserve development history

### Pre-merge Requirements
- All CI checks passing
- Required approvals obtained
- Conflicts resolved
- Target branch up-to-date

## Conflict Detection and Resolution

### Conflict Types
- **Content Conflicts**: Same lines modified differently
- **Structural Conflicts**: Files moved/deleted/renamed
- **Semantic Conflicts**: Logic conflicts without merge conflicts
- **Dependency Conflicts**: Package/library version mismatches

### Resolution Process
1. **Identify Conflicts**: Use git status and diff tools
2. **Understand Changes**: Review both versions of conflicted code
3. **Choose Resolution Strategy**: Keep, merge, or rewrite conflicting sections
4. **Test Resolution**: Verify functionality after conflict resolution
5. **Validate Integration**: Ensure no semantic conflicts introduced

### Prevention Strategies
- Regular sync with target branch
- Small, focused commits
- Coordinate with team on overlapping work
- Use feature flags for experimental changes

## Workflow Compliance Checks

### Branch Lifecycle
- **Creation**: Proper naming and base branch
- **Development**: Regular commits with good messages
- **Review**: PR created with proper description
- **Merge**: Appropriate merge strategy used
- **Cleanup**: Branch deleted after merge

### Integration Patterns
- **Continuous Integration**: Automated testing on all commits
- **Feature Flags**: Safe deployment of incomplete features
- **Trunk-based**: Short-lived branches with frequent integration
- **GitFlow**: Structured branching with release management

### Quality Gates
- No direct pushes to protected branches
- All changes go through PR process
- Required status checks must pass
- Manual approval required for sensitive changes

## Branch Health Metrics

### Freshness Indicators
- Days since last commit
- Commits behind target branch
- Number of conflicts with target
- CI status on latest commit

### Risk Assessment
- **Low Risk**: Recent, few commits, no conflicts
- **Medium Risk**: Moderate age, some conflicts, passing CI
- **High Risk**: Stale, many conflicts, failing CI
- **Critical Risk**: Very old, major conflicts, broken build