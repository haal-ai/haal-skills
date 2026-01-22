# Review Report Format

## Structure

All code review reports MUST follow this structure:

### Header
```markdown
# Code Review Report - [Timestamp]

**Files Reviewed:** [Number] files
**Languages Detected:** [Language list]
**Review Scope:** [Full workspace / Specific path]
```

### Severity Sections

All findings MUST be grouped in these exact sections:

#### HIGH
Critical issues requiring immediate attention:
- `[file-path](file-path), line [number]` — [Issue description]. [Actionable recommendation].

#### MEDIUM
Quality and best practice issues:
- `[file-path](file-path), line [number]` — [Issue description]. [Actionable recommendation].

#### LOW
Minor improvements and suggestions:
- `[file-path](file-path), line [number]` — [Issue description]. [Actionable recommendation].

### Footer
```markdown
---
**Review Summary:**
- HIGH: [count] issues
- MEDIUM: [count] issues  
- LOW: [count] issues

**Next Steps:**
- Address HIGH severity issues before push
- Consider MEDIUM issues for code quality
- Apply LOW suggestions when convenient
```

## Mandatory Requirements

1. **File References**: Every finding MUST include:
   - File path as markdown link: `[path](path)`
   - Line number(s): `, line 42` or `, lines 10-15`

2. **Severity Classification**: Use HIGH/MEDIUM/LOW only

3. **Actionable Recommendations**: Each finding must include specific actions

4. **Language-Specific Context**: Apply appropriate language standards from KB