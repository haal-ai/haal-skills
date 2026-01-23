# Review Workflow Standards

**Purpose**: Standards for managing PR reviews, approvals, and conflict resolution

## Existing Review Integration

### Building on Previous Feedback
- **Address Previous Comments**: All outstanding review comments resolved
- **Acknowledge Feedback**: Responses to reviewer suggestions documented
- **Iterative Improvement**: Show progression from initial to current state
- **Reviewer Re-engagement**: Original reviewers notified of updates

### Review History Analysis
- Changes since last review round
- Outstanding conversation threads
- Resolved vs. unresolved feedback
- Reviewer approval status updates

## Conflicting Review Resolution

### Conflict Types
- **Technical Disagreement**: Different implementation approaches
- **Style Preferences**: Coding style or naming conflicts
- **Architecture Decisions**: System design approach differences
- **Priority Conflicts**: Urgency vs. quality trade-offs

### Resolution Process
1. **Document Conflict**: Clearly state disagreement points
2. **Gather Context**: Additional technical information/requirements
3. **Escalate if Needed**: Senior team member or architect input
4. **Document Decision**: Record rationale for chosen approach
5. **Update Reviews**: Ensure all reviewers acknowledge resolution

### Escalation Criteria
- Security implications involved
- Performance impact concerns
- Breaking changes to public APIs
- Team consensus cannot be reached

## Approval Requirements Validation

### Minimum Approval Thresholds
- **Junior Developer**: 1 senior approval required
- **Senior Developer**: 1 peer approval sufficient
- **Critical Systems**: 2 approvals from senior team members
- **Emergency Hotfix**: 1 approval + post-merge review

### Reviewer Qualifications
- **Domain Expertise**: Knowledge of affected system/component
- **Code Ownership**: Maintainer of modified codebase
- **Security Expert**: For security-sensitive changes
- **Performance Expert**: For performance-critical modifications

### Special Approval Cases
- **Breaking Changes**: Product owner + tech lead approval
- **Database Changes**: DBA review required
- **Infrastructure Changes**: DevOps team approval needed
- **Third-party Dependencies**: Security team review

## Review Comment Quality

### Effective Review Comments
- **Specific**: Point to exact lines/sections
- **Actionable**: Clear steps for improvement
- **Constructive**: Focus on code, not person
- **Educational**: Explain reasoning behind suggestions

### Comment Categories
- **Must Fix**: Blocking issues requiring resolution
- **Should Fix**: Important improvements recommended
- **Consider**: Suggestions for consideration
- **Nitpick**: Minor style/preference items
- **Question**: Seeking clarification or understanding

### Review Completeness
- **Functional Correctness**: Logic and implementation accuracy
- **Code Quality**: Readability, maintainability, best practices
- **Security Considerations**: Vulnerability assessment
- **Performance Impact**: Efficiency and scalability review
- **Testing Coverage**: Test adequacy and quality

## Workflow State Management

### Review States
- **Requested**: Review assigned but not started
- **In Progress**: Reviewer actively examining changes
- **Commented**: Feedback provided, awaiting response
- **Approved**: Changes accepted by reviewer
- **Changes Requested**: Issues must be addressed

### State Transitions
- Author updates → Reset to "Requested" for re-review
- All issues addressed → Move to "Approved"
- New concerns identified → Move to "Changes Requested"
- Review complete → Final "Approved" or "Rejected"

### Notification Management
- Reviewers notified of updates
- Authors notified of new feedback
- Stakeholders notified of approvals
- Team notified of merge/rejection