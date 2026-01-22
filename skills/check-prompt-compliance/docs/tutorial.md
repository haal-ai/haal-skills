# Check Prompt Compliance: Step-by-Step Tutorial

**How to Validate Prompts Against OLAF Standards**

This tutorial shows how to use the check-prompt-compliance skill to validate prompts against OLAF conventions and get corrected versions when issues are found.

## Prerequisites

- OLAF framework loaded and active
- Prompt text to validate
- Access to OLAF prompting principles

## Estimated Time

5-15 minutes per prompt validation

## Step-by-Step Instructions

### Step 1: Invoke the Skill

**User Action:**
```
check prompt compliance
```

**AI Response:**
Acknowledges request and asks for the prompt to validate.

### Step 2: Provide the Prompt Text

**AI Asks:** "Please provide the prompt text you want to validate."

**User Provides:**
Paste or reference the prompt content to check.

**Example:**
```
Here's my prompt:

You should help users write better code. When they ask for help,
try to give good suggestions. Be friendly and helpful.
```

### Step 3: Specify Target Context (Optional)

**AI Asks:** "What type of prompt is this?"

**Options:**
- skill prompt
- workflow prompt
- tool prompt
- helper prompt

**User Provides:**
```
skill prompt
```

**Why This Helps:**
Different prompt types have different requirements. Specifying context enables more accurate validation.

### Step 4: Load Prompting Principles

**What AI Does:**
1. Reads `templates/prompting-principles.md`
2. Loads OLAF skill structure requirements
3. Prepares validation criteria

**You Should See:**
```
✓ Loaded prompting principles
✓ Validation criteria ready
```

### Step 5: Review Compliance Assessment

**What AI Does:**
Analyzes the prompt against each principle and generates a compliance report.

**Example Output - Non-Compliant:**
```
## Compliance Assessment: NON-COMPLIANT

### Issues Identified:

1. **Passive Language**
   - Found: "should help", "try to give"
   - Required: Imperative language (WILL/MUST/NEVER)
   - Impact: Instructions are ambiguous and optional-sounding

2. **Missing Success Criteria**
   - No explicit acceptance checks defined
   - Required: Measurable success criteria section
   - Impact: Cannot verify task completion

3. **Vague Instructions**
   - Found: "good suggestions", "be friendly"
   - Required: Specific, actionable instructions
   - Impact: Inconsistent behavior across executions

4. **Missing Structure**
   - No Input Parameters section
   - No Process section
   - No Output section
   - No Error Handling section
   - Impact: Incomplete skill definition

5. **Missing Error Handling**
   - No guidance for failure scenarios
   - Required: Comprehensive error handling
   - Impact: Undefined behavior on errors
```

**Example Output - Compliant:**
```
## Compliance Assessment: COMPLIANT

This prompt follows OLAF standards:
✅ Uses imperative language (WILL/MUST)
✅ Has explicit success criteria
✅ Clear input/output sections
✅ Comprehensive error handling
✅ Proper structure and formatting
✅ Consistent markdown formatting
```

### Step 6: Review Corrected Version

**What AI Provides (if non-compliant):**
A corrected version that preserves intent while fixing issues.

**Example Corrected Version:**
```markdown
You WILL assist users in improving their code quality by providing
specific, actionable suggestions.

## Input Parameters
- **code_snippet**: string - The code to review (REQUIRED)
- **improvement_focus**: string - Area to focus on: "readability", 
  "performance", "security" (OPTIONAL)

## Process
1. Analyze the provided code snippet
2. Identify improvement opportunities based on focus area
3. Generate specific suggestions with examples
4. Prioritize suggestions by impact

## Output
- List of improvement suggestions
- Code examples showing before/after
- Priority ranking for each suggestion

## Success Criteria
- [ ] All code analyzed for improvement opportunities
- [ ] Suggestions include specific code examples
- [ ] Improvements prioritized by impact

## Error Handling
- **Empty code snippet**: Request valid code input
- **Unsupported language**: List supported languages
- **No improvements found**: Confirm code quality is good
```

### Step 7: Accept or Iterate

**User Options:**
1. **Accept**: Use the corrected version as-is
2. **Request changes**: Ask for specific modifications
3. **Partial accept**: Take some corrections, keep others original

**Example - Request Changes:**
```
Accept the corrected version, but add a parameter for output format (brief/detailed)
```

**AI Response:**
Makes requested changes and presents updated version.

### Step 8: Apply Corrections

**User Action:**
Replace original prompt with corrected version in your skill file.

**Verification:**
Run compliance check again to confirm all issues resolved.

## Verification Checklist

After validation, verify:

✅ **Imperative Language**
- Uses WILL/MUST/NEVER instead of should/try/might
- Clear, direct instructions

✅ **Explicit Success Criteria**
- Has measurable acceptance checks
- Criteria are specific and verifiable

✅ **Clear Structure**
- Input Parameters section defined
- Process section with numbered steps
- Output section with deliverables
- Error Handling section

✅ **Tool Usage Guidance**
- If tools are expected, explicit guidance provided
- Tool names and usage patterns documented

✅ **Consistent Formatting**
- Proper markdown headings
- Consistent bullet/numbering style
- Clean, readable layout

## Common Issues and Fixes

### Issue 1: Passive Language

**Before:**
```
You should analyze the code and try to find issues.
```

**After:**
```
You WILL analyze the code and identify all issues.
```

### Issue 2: Missing Success Criteria

**Before:**
```
Help the user with their task.
```

**After:**
```
## Success Criteria
- [ ] Task requirements understood
- [ ] Solution provided and explained
- [ ] User confirms task completion
```

### Issue 3: Vague Instructions

**Before:**
```
Make the output look nice and be helpful.
```

**After:**
```
## Output Format
- Use markdown formatting with headers
- Include code blocks for examples
- Provide step-by-step explanations
```

### Issue 4: Missing Error Handling

**Before:**
```
Process the file and return results.
```

**After:**
```
## Error Handling
- **File not found**: Report error with path, request valid file
- **Invalid format**: List supported formats, request conversion
- **Processing failed**: Log error details, suggest alternatives
```

### Issue 5: Missing Input Parameters

**Before:**
```
Analyze the code for bugs.
```

**After:**
```
## Input Parameters
- **code_path**: string - Path to code file (REQUIRED)
- **analysis_depth**: string - "quick" or "thorough" (OPTIONAL, default: "quick")
```

## Troubleshooting

**If validation seems too strict:**
- Check if target_context is correctly specified
- Some rules may not apply to all prompt types
- Request specific rule exceptions if justified

**If corrected version changes intent:**
- Point out specific sections that changed meaning
- Request preservation of original intent
- Iterate until both compliance and intent are satisfied

**If principles file not found:**
- Verify `templates/prompting-principles.md` exists
- Check file permissions
- Request manual principles application

## Best Practices

1. **Validate early**: Check compliance during prompt development
2. **Understand the rules**: Read prompting-principles.md to internalize standards
3. **Iterate quickly**: Make small corrections and re-validate
4. **Document exceptions**: If a rule doesn't apply, document why
5. **Batch validation**: Check multiple prompts together during audits
6. **Learn from corrections**: Use feedback to improve future prompts

## Compliance Principles Summary

### Language Rules
- Use WILL for actions the AI will perform
- Use MUST for mandatory requirements
- Use NEVER for prohibited actions
- Avoid should, try, might, could

### Structure Rules
- Always include Input Parameters
- Always include Process with numbered steps
- Always include Output specification
- Always include Success Criteria
- Always include Error Handling

### Formatting Rules
- Use consistent markdown headings
- Use bullet lists for options
- Use numbered lists for sequences
- Use code blocks for examples

## Next Steps After Validation

1. **If compliant**: Proceed with skill publication
2. **If non-compliant**: Apply corrections and re-validate
3. **For new skills**: Use create-skill to ensure compliance from start
4. **For external prompts**: Use convert-prompt-to-skill after validation

## Related Skills

- **create-skill**: Create new compliant skills from scratch
- **convert-prompt-to-skill**: Convert and validate external prompts
- **evaluate-prompt-for-adoption**: Assess external prompts before importing

## Expected Timeline

- **Simple prompts**: 2-5 minutes
- **Complex prompts**: 10-15 minutes
- **Batch validation**: 5-10 minutes per prompt

