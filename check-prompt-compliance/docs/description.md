# Check Prompt Compliance

## Overview

Check Prompt Compliance validates prompts against OLAF prompt standards and conventions, identifying non-compliance issues and proposing corrected versions while preserving the original intent.

## Purpose

Maintaining consistent, high-quality prompts across a skills library requires adherence to established standards. This skill solves the challenge of ensuring prompts follow OLAF conventions including proper structure, imperative language, explicit success criteria, clear tool usage guidance, and comprehensive error handling.

## Key Features

### 1. Standards Validation
Validates prompts against OLAF prompting principles:
- Imperative language usage (WILL/MUST/NEVER)
- Explicit success criteria and acceptance checks
- Clear separation between instructions and context
- Explicit tool usage guidance when tools are expected
- Consistent headings and formatting
- Comprehensive error handling

### 2. Issue Identification
Identifies specific non-compliance issues:
- Missing required sections
- Ambiguous instructions
- Missing constraints or rules
- Structural problems
- Formatting inconsistencies
- Passive language usage

### 3. Corrected Version Generation
Proposes corrected versions that:
- Preserve original intent and functionality
- Fix identified compliance issues
- Follow OLAF template structure
- Use proper imperative language
- Include missing sections

## Usage

**Command**: `check prompt compliance`

**Protocol**: Act

**When to Use**: Use this skill when you want to validate a prompt against OLAF standards, before publishing a new skill, after converting external prompts, or during periodic quality audits of your skills library.

## Parameters

### Required Inputs
- **prompt_text**: The prompt content to validate

### Optional Inputs
- **target_context**: The context for the prompt (e.g., "skill prompt", "workflow prompt", "tool prompt")

### Context Requirements
- Access to OLAF prompting principles (`templates/prompting-principles.md`)
- Understanding of OLAF skill structure conventions

## Output

**Deliverables**:
- Compliance assessment (compliant or non-compliant)
- List of identified issues (if non-compliant)
- Corrected version of the prompt (if non-compliant)
- Explanation of changes made

**Format**: Structured report with issue list and corrected prompt in markdown format.

## Examples

### Example 1: Non-Compliant Prompt

**Input**:
```
prompt_text: "You should analyze the code and find bugs. Try to be helpful."
target_context: "skill prompt"
```

**Output**:
```
## Compliance Assessment: NON-COMPLIANT

### Issues Identified:
1. Uses passive language ("should", "try") instead of imperative (WILL/MUST)
2. Missing explicit success criteria
3. Missing error handling section
4. No structured input/output sections
5. Vague instructions ("be helpful")

### Corrected Version:
You WILL analyze the provided code for bugs and issues.

## Input Parameters
- **code_path**: string - Path to the code file to analyze (REQUIRED)

## Process
1. Read the specified code file
2. Analyze for common bug patterns
3. Identify potential issues

## Output
- List of identified bugs with line numbers
- Severity classification for each issue
- Suggested fixes

## Success Criteria
- [ ] All code files analyzed
- [ ] Issues categorized by severity
- [ ] Actionable fixes provided

## Error Handling
- **File not found**: Report error with path and stop
- **Unsupported language**: List supported languages and request valid file
```

### Example 2: Compliant Prompt

**Input**:
```
prompt_text: [well-structured OLAF skill prompt]
target_context: "skill prompt"
```

**Output**:
```
## Compliance Assessment: COMPLIANT

This prompt follows OLAF standards:
✅ Uses imperative language (WILL/MUST)
✅ Has explicit success criteria
✅ Clear input/output sections
✅ Comprehensive error handling
✅ Proper structure and formatting
```

### Example 3: Partial Compliance

**Input**:
```
prompt_text: "You WILL analyze the code. Find all bugs."
target_context: "skill prompt"
```

**Output**:
```
## Compliance Assessment: NON-COMPLIANT

### Issues Identified:
1. Missing input parameters section
2. Missing process section with numbered steps
3. Missing output format specification
4. Missing success criteria
5. Missing error handling

### Corrected Version:
[Full corrected prompt with all sections]
```

## Related Skills

- **create-skill**: Create new skills following OLAF standards
- **convert-prompt-to-skill**: Convert external prompts to OLAF format
- **evaluate-prompt-for-adoption**: Evaluate external prompts before adoption

## Tips & Best Practices

1. **Run before publishing**: Always check compliance before adding skills to your library
2. **Use target_context**: Specify the prompt type for more accurate validation
3. **Review corrections**: Always review proposed corrections before accepting
4. **Iterative improvement**: Use feedback to improve prompt writing skills
5. **Batch validation**: Check multiple prompts during quality audits
6. **Understand principles**: Read prompting-principles.md to internalize standards
7. **Document exceptions**: If a rule doesn't apply, document why

## Compliance Checklist

The skill validates against these criteria:

### Structure
- [ ] Has input parameters section
- [ ] Has process section with numbered steps
- [ ] Has output section with deliverables
- [ ] Has success criteria checklist
- [ ] Has error handling section

### Language
- [ ] Uses imperative language (WILL/MUST/NEVER)
- [ ] Avoids passive voice (should, try, might)
- [ ] Clear and unambiguous instructions
- [ ] Specific and actionable guidance

### Formatting
- [ ] Consistent markdown headings
- [ ] Proper bullet/numbering style
- [ ] Clean, readable layout
- [ ] Appropriate use of code blocks

### Content
- [ ] Explicit success criteria
- [ ] Comprehensive error handling
- [ ] Clear tool usage guidance (if applicable)
- [ ] Separation of instructions and context

## Limitations

- Validation is based on OLAF conventions; other frameworks may have different standards
- Cannot validate runtime behavior, only static prompt structure
- Corrected versions preserve intent but may need manual refinement
- Complex domain-specific prompts may require additional manual review
- Does not validate external file references (templates, tools, etc.)
- Cannot assess prompt effectiveness, only structural compliance

