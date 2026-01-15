# Tutorial: Create Skill

## Overview
This tutorial guides you through creating a new structured skill for OLAF using the Create Skill skill. You'll learn how to generate skills that follow OLAF's skills architecture, include proper manifests, and integrate seamlessly with the framework.

## Prerequisites
- OLAF framework installed and configured
- Access to OLAF skills directory
- Understanding of the task your skill will address
- Terminal access for timestamp generation
- Basic knowledge of OLAF skills architecture

## Estimated Time
45-60 minutes

## Steps

### Step 1: Invoke the Create Skill
Open your IDE and invoke the skill:
```
olaf create skill
```

**Expected Result**: The skill activates and begins the skill creation workflow.

### Step 2: Provide User Request
When prompted, describe what your new skill should do:
```
Example: "Create a skill that analyzes code quality metrics and generates improvement recommendations"
```

**Expected Result**: The skill acknowledges your request and proceeds to next parameter.

### Step 3: Specify Skill Name
Provide a descriptive name in kebab-case (max 4 words):
```
Example: "analyze-code-quality"
```

**Expected Result**: Name is validated and checked for duplicates in skills directory.

### Step 4: Select Skill Type
Choose the appropriate skill type:
```
Options:
1. "prompt" - Simple, standalone skill
2. "orchestrator" - Complex skill coordinating multiple operations  
3. "workflow" - Step-by-step process skill

Example: "prompt"
```

**Expected Result**: Skill type selection confirmed and skill architecture determined.

### Step 5: Review Generated Skill Structure
The skill generates a complete directory structure:
```
.olaf/skills/analyze-code-quality/
├── prompts/
│   └── analyze-code-quality.md
├── templates/
├── tools/
├── kb/
├── docs/
│   ├── description.md
│   └── tutorial.md
├── helpers/
└── skill-manifest.json
```

**Expected Result**: Complete skill structure created with proper organization.

### Step 6: Review Skill Manifest
Examine the generated skill-manifest.json:
```json
{
  "metadata": {
    "id": "analyze-code-quality",
    "name": "Analyze Code Quality",
    "protocol": "Propose-Confirm-Act",
    "status": "experimental",
    "exposure": "internal"
  },
  "bom": {
    "prompts": [
      {
        "name": "analyze-code-quality",
        "path": "/prompts/analyze-code-quality.md"
      }
    ]
  }
}
```

**Expected Result**: Manifest validates against schema and includes complete metadata.

### Step 7: Review Main Skill Prompt
Examine the generated main prompt file:
- Follows OLAF skill template structure
- Uses imperative language consistently
- Includes comprehensive error handling
- Has measurable success criteria

**Expected Result**: Skill prompt meets all OLAF standards.

### Step 8: Approve or Request Changes
Use the Propose-Confirm-Act protocol:
- **Approve**: Type "approved" to create the skill
- **Request Changes**: Provide specific feedback for modifications

**Expected Result**: Skill creation proceeds based on your response.

### Step 9: Verify Skill Creation
After approval, verify the skill was created successfully:
```
Check: skills/analyze-code-quality/ exists with all files
```

**Expected Result**: Complete skill package available for use.

### Step 10: Test Your New Skill
Test the skill to ensure it works correctly:
```
olaf analyze code quality
```

**Expected Result**: Skill executes and performs as expected.

## Expected Outcomes

### Successful Completion
- Complete skill directory structure under `skills/[skill-name]/`
- Valid skill manifest conforming to schema
- Functional main skill prompt following OLAF standards
- Complete documentation package
- Skill discoverable through OLAF framework

### Files Created
- `prompts/[skill-name].md` - Main skill prompt
- `skill-manifest.json` - Complete metadata and BOM
- `docs/description.md` - Skill overview and usage
- `docs/tutorial.md` - Step-by-step guide
- Template files (if applicable)
- Tool files (if applicable)

### Validation Checklist
- [ ] Skill manifest validates against schema
- [ ] All BOM paths are correct and relative to skill root
- [ ] Main prompt follows OLAF template structure
- [ ] Documentation is complete and accurate
- [ ] Skill can be invoked through OLAF framework
- [ ] No naming conflicts with existing skills

## Troubleshooting

### Common Issues

**Issue**: "Skill name already exists"
**Solution**: Choose a different, more specific name or review existing skill for potential merge

**Issue**: "Schema validation failed"
**Solution**: Review manifest structure and correct invalid fields

**Issue**: "Directory creation failed"
**Solution**: Check permissions and available disk space

**Issue**: "Template files not found"
**Solution**: Verify OLAF framework installation and template availability

### Best Practices

1. **Plan before creating**: Think through your skill's purpose and dependencies
2. **Use descriptive names**: Choose clear, action-oriented names
3. **Test thoroughly**: Always test your skill after creation
4. **Document well**: Provide comprehensive documentation for users
5. **Follow conventions**: Stick to OLAF naming and structure conventions

## Next Steps

After creating your skill:
1. **Test functionality**: Verify the skill works as expected
2. **Refine prompt**: Adjust the main prompt based on testing results
3. **Add dependencies**: Include any needed templates, tools, or knowledge base articles
4. **Update documentation**: Enhance docs based on actual usage
5. **Share with team**: Make the skill available to other team members

## Related Resources

- **Skill Architecture Guide**: Understanding OLAF skills structure
- **Manifest Schema**: Complete schema documentation
- **Template Guidelines**: Best practices for skill templates
- **Testing Framework**: How to test your skills effectively