# PR Description Standards

**Purpose**: Standards for evaluating PR titles, descriptions, and metadata quality

## PR Title Quality

### Required Elements
- **Clear action verb**: fix, add, update, remove, refactor
- **Scope indication**: component/module affected
- **Concise description**: under 50 characters when possible

### Naming Conventions
- Use imperative mood ("Add feature" not "Added feature")
- Capitalize first word
- No trailing punctuation
- Include ticket/issue reference when applicable

### Quality Indicators
- ✅ **Good**: "Fix authentication timeout in user service"
- ❌ **Poor**: "Various fixes", "Updates", "WIP"

## Description Completeness

### Required Sections

**Purpose/Why**
- Clear explanation of the problem being solved
- Business or technical justification
- Link to requirements/issues

**Changes/What**
- Summary of modifications made
- Key files/components affected
- Architecture or design decisions

**Testing/How**
- Test cases covered
- Manual testing performed
- Regression testing notes

**Breaking Changes**
- API changes that affect consumers
- Configuration changes required
- Migration steps needed

### Quality Assessment
- **Complete**: All required sections present with meaningful content
- **Partial**: Some sections missing or insufficient detail
- **Minimal**: Only basic description provided

## Linked Issues Validation

### Requirements
- All referenced issues exist and are accessible
- PR addresses the core problem described in linked issues
- Issue status aligns with PR state (open issues for new PRs)

### Traceability Checks
- Issue → PR relationship clear
- Requirements fulfilled by changes
- Acceptance criteria addressed

## Requirements Traceability

### Validation Points
- Changes align with stated requirements
- No scope creep beyond original issue
- All acceptance criteria testable
- Edge cases considered and documented

### Documentation Links
- Design documents referenced
- Architecture decisions recorded
- Dependencies identified and documented