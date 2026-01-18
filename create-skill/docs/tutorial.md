# Create Skill: Step-by-Step Tutorial

**How to Create New Structured Skills for OLAF**

This tutorial guides you through creating a new structured skill that follows OLAF's skills architecture and integrates seamlessly with the framework.

## Prerequisites

- OLAF framework installed and configured
- Access to OLAF skills directory
- Understanding of the task your skill will address
- Terminal access for timestamp generation
- Basic knowledge of OLAF skills architecture

## Estimated Time

30-45 minutes

## Step-by-Step Instructions

### Step 1: Invoke the Skill

**User Action:**
```
create skill
```

**AI Response:**
The skill activates and begins the skill creation workflow using Propose-Confirm-Act protocol.

### Step 2: Provide User Request

**AI Asks:** "What should this new skill do?"

**User Provides:**
Describe what your new skill should accomplish.

**Example:**
```
Create a skill that analyzes code quality metrics and generates improvement recommendations
```

**AI Response:**
Acknowledges your request and proceeds to gather additional parameters.

### Step 3: Specify Skill Name

**AI Asks:** "What name would you like for this skill? (kebab-case, max 4 words)"

**User Provides:**
```
analyze-code-quality
```

**What AI Does:**
- Validates name follows kebab-case convention
- Checks for duplicates across all skill roots:
  - `.windsurf/skills/`
  - `.claude/skills/`
  - `agents/skills/`
  - User-specified `skills_root`

**If Duplicate Found:**
```
A skill named "analyze-code-quality" already exists. Please choose:
1. Pick a different skill_name
2. Update the existing skill in place (preferred)
3. Overwrite the existing skill (delete and recreate)
```

### Step 4: Select Skill Type

**AI Asks:** "What type of skill is this?"

**Options:**
1. **prompt** - Simple, standalone skill (default)
2. **orchestrator** - Complex skill coordinating multiple operations
3. **workflow** - Step-by-step process skill

**User Provides:**
```
prompt
```

### Step 5: Specify Target Plugin

**AI Asks:** "Which plugin should this skill be assigned to?"

**User Provides:**
```
code-quality
```

**What AI Does:**
- Checks if plugin exists in `.olaf/plugins.json`
- If not found, adds it to the plugins array
- Records plugin assignment for skill metadata

### Step 6: Determine Skills Root

**What AI Does:**
Determines where to create the skill using this priority:

1. If user provided `skills_root` → use it
2. Else infer from workspace:
   - If `.windsurf/skills/` exists → use it
   - Else if `.claude/skills/` exists → use it
   - Else if `agents/skills/` exists → use it
3. Else ask user to choose agent runtime

**If Asking:**
```
Which agent runtime are you using?
1. windsurf/cascade → .windsurf/skills
2. github-copilot/claude-code → .claude/skills
3. other → agents/skills
```

### Step 7: Component Requirements

**AI Asks:** "Does this skill need any optional components?"

**Options:**
1. **Templates** - External template files for structured outputs
2. **Tools** - Scripts or utilities (Python, shell, JavaScript)
3. **Helpers** - Reusable prompt fragments
4. **Knowledge Base** - Reference articles or data

**User Provides:**
```
No additional components needed
```

**Or with components:**
```
needs_templates: true
template_list: ["quality-report-template", "metrics-template"]
```

### Step 8: Load Templates and Principles

**What AI Does:**
1. Reads `create-skill/kb/skill-structure-schema.md` for structure reference
2. Reads `templates/skill-template.md` for template structure
3. Reads `templates/prompting-principles.md` for best practices

**You Should See:**
```
✓ Loaded skill structure schema
✓ Loaded skill template
✓ Loaded prompting principles
```

### Step 9: Review Generated Skill Structure

**AI Proposes:**
```
Proposed skill structure:

analyze-code-quality/
├── skill.md          # Main skill prompt
├── docs/
│   ├── description.md  # Skill overview
│   └── tutorial.md     # Usage guide
```

**With Components:**
```
analyze-code-quality/
├── skill.md
├── docs/
│   ├── description.md
│   └── tutorial.md
├── templates/
│   ├── quality-report-template.md
│   └── metrics-template.md
```

### Step 10: Review Main Skill Prompt

**AI Shows:**
Preview of generated `skill.md` with:
- Proper frontmatter metadata
- Input parameters section
- Process section with numbered steps
- Output format section
- Success criteria checklist
- Error handling section
- Domain-specific rules

**Key Elements to Verify:**
- Uses imperative language (WILL/MUST/NEVER)
- Has explicit success criteria
- Includes comprehensive error handling
- References external files (not embedded)

### Step 11: Approve or Request Changes

**AI Asks:** "Does this skill structure look correct? (Propose-Confirm-Act)"

**User Options:**
1. **Approve**: Type "approved" to create the skill
2. **Request Changes**: Provide specific feedback for modifications

**Example Feedback:**
```
Add a parameter for specifying which metrics to analyze
```

**AI Response:**
Makes requested changes and presents updated proposal.

### Step 12: Generate Skill Files

**What AI Does:**
After approval:
1. Creates skill directory at `${skills_root}/analyze-code-quality/`
2. Creates `skill.md` with full content
3. Creates `docs/description.md`
4. Creates `docs/tutorial.md`
5. Creates optional component folders/files
6. Updates `.olaf/plugins.json` with plugin assignment

**You Should See:**
```
✓ Created directory: .windsurf/skills/analyze-code-quality/
✓ Created skill.md
✓ Created docs/description.md
✓ Created docs/tutorial.md
✓ Updated plugins.json
```

### Step 13: Validation

**What AI Does:**
Validates the generated skill:
- Follows proper directory structure
- Uses imperative language consistently
- Includes comprehensive error handling
- Has measurable success criteria
- Contains proper XML markup where appropriate

**You Should See:**
```
Validation Results:
✓ Directory structure correct
✓ Imperative language used
✓ Error handling included
✓ Success criteria defined
✓ All external references have files
```

### Step 14: Test Your New Skill

**User Action:**
Test the skill to ensure it works correctly:
```
analyze code quality
```

**Expected Result:**
Skill executes and performs as expected.

## Verification Checklist

After creation, verify:

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

✅ **Plugin Assignment**
- Plugin added to `.olaf/plugins.json`
- Plugin in skill.md metadata

✅ **External References**
- All referenced files exist
- No embedded template content

## Troubleshooting

**Issue: "Skill name already exists"**
- Choose a different, more specific name
- Or select "Update in place" to modify existing skill

**Issue: "Directory creation failed"**
- Check permissions on skills root directory
- Verify available disk space

**Issue: "Template files not found"**
- Verify OLAF framework installation
- Check template file paths

**Issue: "Plugin validation failed"**
- Verify `.olaf/plugins.json` exists
- Check JSON syntax in plugins file

## Best Practices

1. **Plan before creating**: Think through purpose and dependencies
2. **Use descriptive names**: Choose clear, action-oriented names
3. **Test thoroughly**: Always test after creation
4. **Document well**: Provide comprehensive documentation
5. **Follow conventions**: Stick to OLAF naming and structure
6. **Keep it focused**: One skill, one purpose
7. **Handle errors**: Consider all failure scenarios

## Next Steps After Creation

1. **Test functionality**: Verify the skill works as expected
2. **Refine prompt**: Adjust based on testing results
3. **Add dependencies**: Include needed templates, tools, or kb articles
4. **Update documentation**: Enhance docs based on actual usage
5. **Share with team**: Make the skill available to others

## Expected Timeline

- **Simple skill**: 15-20 minutes
- **Skill with components**: 30-45 minutes
- **Complex orchestrator**: 45-60 minutes

