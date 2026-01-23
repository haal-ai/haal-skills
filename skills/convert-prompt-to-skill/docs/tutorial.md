# Convert Prompt to Skill: Step-by-Step Tutorial

**How to Transform Existing Prompts into OLAF Skills**

This tutorial walks through converting one or more existing prompt files into a properly structured OLAF skill folder with documentation and optional components.

## Prerequisites

- OLAF framework installed and configured
- Source prompt file(s) to convert, or prompt content to paste
- Knowledge of which plugin should own the new skill

## Estimated Time

15-30 minutes (depends on prompt complexity)

## Step-by-Step Instructions

### Step 1: Invoke the Skill

**User Action:**
```
convert prompt to skill
```

**AI Response:**
Acknowledges request and asks for the source prompt.

### Step 2: Provide Source Prompt

**Option A - File Path:**
```
existing_prompt_path: prompts/my-legacy-prompt.md
```

**Option B - Multiple Files:**
```
existing_prompt_path: ["prompts/part1.md", "prompts/part2.md"]
```

**Option C - Direct Paste:**
```
source_text: [paste your prompt content here]
```

**What AI Does:**
- Reads and analyzes the prompt content
- Extracts purpose, inputs, workflow, outputs
- Detects implied components (templates, tools, etc.)
- Prepares analysis summary

**You Should See:**
```
✓ Read prompt content (1,245 characters)
✓ Detected purpose: Code quality analysis
✓ Detected inputs: code_path, analysis_type
✓ Detected workflow: 5 steps
✓ Implied components: templates (1), tools (0)
```

### Step 3: Review Source Analysis

**AI Provides:**
```
## Source Analysis

### Purpose
Analyzes code for quality issues and generates improvement recommendations.

### Detected Inputs
- code_path: Path to code file (inferred from "analyze the file at...")
- analysis_type: Type of analysis (inferred from "focus on security/performance")

### Detected Workflow
1. Read the code file
2. Analyze for issues
3. Categorize findings
4. Generate recommendations
5. Format output

### Implied Components
- Templates: Output report format detected (recommend extracting)
- Tools: None detected
- Helpers: None detected
- KB: None detected

### Proposed Skill Name
analyze-code-quality
```

### Step 4: Provide Target Plugin

**AI Asks:** "Which plugin should this skill be assigned to?"

**User Provides:**
```
target_plugin: code-quality
```

**What AI Does:**
- Checks if plugin exists in `.olaf/plugins.json`
- If not found, will add it during skill creation

### Step 5: Confirm or Override Skill Name

**AI Asks:** "Proposed skill name is 'analyze-code-quality'. Would you like to use this or provide a different name?"

**User Options:**
1. Accept proposed name
2. Provide different name (kebab-case, max 4 words)

**Example:**
```
Use: review-code-quality
```

**What AI Does:**
- Validates name follows kebab-case convention
- Checks for duplicates across all skill roots

### Step 6: Determine Skills Root

**What AI Does:**
Determines where to create the skill:

1. If user provided `skills_root` → use it
2. Else infer from workspace:
   - If `.windsurf/skills/` exists → use it
   - Else if `.claude/skills/` exists → use it
   - Else if `agents/skills/` exists → use it
3. Else ask user to choose

**If Asking:**
```
Which agent runtime are you using?
1. windsurf/cascade → .windsurf/skills
2. github-copilot/claude-code → .claude/skills
3. other → agents/skills
```

### Step 7: Confirm Component Requirements

**AI Asks:** "Based on analysis, I detected these component needs. Please confirm:"

```
1. Templates: YES (output report format detected)
   - Proposed: quality-report-template.md
   
2. Tools: NO
3. Helpers: NO
4. Knowledge Base: NO

Would you like to add or remove any components?
```

**User Options:**
1. Confirm as-is
2. Add components
3. Remove components

**Example:**
```
Confirm templates. Also add a kb article for coding standards reference.
```

### Step 8: Load Templates and Principles

**What AI Does:**
1. Reads `kb/skill-structure-schema.md` for structure reference
2. Reads `templates/skill-template.md` for template structure
3. Reads `templates/prompting-principles.md` for best practices

**You Should See:**
```
✓ Loaded skill structure schema
✓ Loaded skill template
✓ Loaded prompting principles
```

### Step 9: Review Proposed Skill Structure

**AI Proposes:**
```
## Proposed Skill Structure

review-code-quality/
├── skill.md              # Main skill prompt
├── docs/
│   ├── description.md    # Skill overview
│   └── tutorial.md       # Usage guide
├── templates/
│   └── quality-report-template.md
└── kb/
    └── coding-standards.md
```

### Step 10: Review Generated skill.md

**AI Shows Preview:**
```markdown
---
name: review-code-quality
description: Analyzes code for quality issues and generates improvement recommendations
license: Apache-2.0
metadata:
  plugins: code-quality
---

<olaf>

## Input Parameters
- **code_path**: string - Path to code file to analyze (REQUIRED)
- **analysis_type**: string - Focus area: "security", "performance", "all" (OPTIONAL)

## Process
1. Read the specified code file
2. Analyze code for quality issues based on analysis_type
3. Categorize findings by severity
4. Generate improvement recommendations
5. Format output using quality report template

## Output
Follow template: templates/quality-report-template.md

## Success Criteria
- [ ] Code file successfully read
- [ ] Issues identified and categorized
- [ ] Recommendations provided for each issue
- [ ] Report formatted correctly

## Error Handling
- **File not found**: Report error with path, request valid file
- **Unsupported language**: List supported languages
- **No issues found**: Confirm code quality is good

 
```

### Step 11: Approve or Request Changes

**AI Asks:** "Does this converted skill look correct?"

**User Options:**
1. **Approve**: Type "approved" to create the skill
2. **Request Changes**: Provide specific feedback

**Example Feedback:**
```
Add a parameter for output format (brief/detailed)
```

**AI Response:**
Makes requested changes and presents updated proposal.

### Step 12: Generate Skill Files

**What AI Does After Approval:**
1. Creates skill directory
2. Creates skill.md with full content
3. Creates docs/description.md
4. Creates docs/tutorial.md
5. Creates component files (templates, kb, etc.)
6. Updates .olaf/plugins.json

**You Should See:**
```
✓ Created directory: .windsurf/skills/review-code-quality/
✓ Created skill.md
✓ Created docs/description.md
✓ Created docs/tutorial.md
✓ Created templates/quality-report-template.md
✓ Created kb/coding-standards.md
✓ Updated plugins.json
```

### Step 13: Validation

**What AI Does:**
Validates the generated skill:
- Follows proper directory structure
- Uses imperative language consistently
- Includes comprehensive error handling
- Has measurable success criteria
- All external references have files

**You Should See:**
```
## Validation Results
✓ Directory structure correct
✓ Imperative language used
✓ Error handling included
✓ Success criteria defined
✓ All external references valid
✓ Original functionality preserved
```

### Step 14: Test the Converted Skill

**User Action:**
Test the skill to ensure it works correctly:
```
review code quality
```

**Expected Result:**
Skill executes with same functionality as original prompt, but with improved structure.

## Verification Checklist

After conversion, verify:

✅ **Directory Structure**
- Skill folder exists at correct location
- All required files present
- Optional folders only if requested

✅ **Main Prompt (skill.md)**
- Follows OLAF template structure
- Uses imperative language (WILL/MUST)
- Has input parameters section
- Has process section
- Has output section
- Has success criteria
- Has error handling

✅ **Documentation**
- `docs/description.md` exists with overview
- `docs/tutorial.md` exists with steps

✅ **Components**
- Template files created if requested
- Tool files created if requested
- KB files created if requested
- All references in skill.md point to existing files

✅ **Functionality**
- Original intent preserved
- All original capabilities available
- Improvements documented

## Troubleshooting

**Issue: "Source file not found"**
- Verify the file path is correct
- Check file permissions
- Try using absolute path

**Issue: "Skill name conflict"**
- Choose a different, more specific name
- Or select "Update in place" to modify existing

**Issue: "Analysis missed important features"**
- Provide additional context via user_request
- Manually specify component needs

**Issue: "Converted skill behaves differently"**
- Compare original and converted prompts
- Check if any logic was lost in conversion
- Request specific preservation of features

## Best Practices

1. **Review analysis**: Verify AI correctly understood the source prompt
2. **Preserve intent**: Ensure original functionality is maintained
3. **Check compliance**: Run check-prompt-compliance after conversion
4. **Test thoroughly**: Test all features of the converted skill
5. **Keep originals**: Source files are preserved for reference
6. **Document changes**: Note any modifications made during conversion

## Conversion Patterns

### Pattern 1: Simple Prompt
- Single file, clear purpose
- Minimal components needed
- Quick conversion (10-15 min)

### Pattern 2: Complex Prompt
- Multiple sections, embedded templates
- Extract templates to separate files
- Moderate conversion (20-30 min)

### Pattern 3: Multi-File Merge
- Related prompts combined
- Identify common patterns
- Resolve conflicts
- Longer conversion (30-45 min)

## Next Steps After Conversion

1. **Run compliance check**: `check prompt compliance`
2. **Test functionality**: Execute the skill with test inputs
3. **Refine if needed**: Iterate on any issues found
4. **Update documentation**: Enhance docs based on testing
5. **Archive originals**: Keep source files for reference

## Related Skills

- **create-skill**: Create new skills from scratch
- **check-prompt-compliance**: Validate converted skill quality
- **evaluate-prompt-for-adoption**: Assess prompts before converting

## Expected Timeline

- **Simple conversion**: 15-20 minutes
- **Complex conversion**: 25-35 minutes
- **Multi-file merge**: 35-45 minutes

