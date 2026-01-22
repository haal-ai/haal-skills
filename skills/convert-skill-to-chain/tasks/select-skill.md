---
task_id: "select-skill"
task_name: "Skill Selection"
dependencies: ["context.timestamp"]
conditions: []
---

# Select Skill to Convert

## Input Context
**Required Context Variables**: 
- `context.timestamp`: Session timestamp
**Required Files**: None
**Required Tools**: File system access

## Task Instructions

### Get Skill Name from User

1. **List Available Skills**:
   - Read `skills/` directory
   - Filter out `common` folder and `task-registry.json`
   - Sort skill names alphabetically
   - Create numbered list for user selection

2. **Present Options**:
```
**Skill Conversion - Select Source Skill**

Available skills to convert (choose by number OR skill name):

1. skill-name-1
2. skill-name-2
3. skill-name-3
...

Enter the NUMBER or EXACT SKILL NAME you want to convert to master-chain pattern:
(Note: This is for CONVERSION, not execution)
```

3. **Get User Selection**:
   - Wait for user to provide either:
     - A NUMBER from the list (e.g., "4" or "42")
     - An EXACT skill name (e.g., "review-diff")
   - **CRITICAL**: If user provides a skill name that exists in the list, treat it as a selection for CONVERSION
   - **DO NOT** attempt to execute the skill when user provides a skill name
   - Map number to corresponding skill name if number provided
   - Validate skill exists in `skills/[skill-name]`
   - Confirm skill has a `prompts/` directory

4. **Validate Skill Structure**:
   - Check if `skills/[skill-name]/prompts/[skill-name].md` exists
   - If not found, look for any `.md` file in `prompts/` directory
   - Confirm with user if multiple prompts found

5. **Confirm Selection for Conversion**:
   - Display clear confirmation message:
   ```
   ✓ Selected skill for CONVERSION: [skill-name]
   
   This skill will be analyzed and converted to master-chain pattern.
   (We will NOT execute this skill, only convert its structure)
   
   Proceeding with conversion analysis...
   ```
   - Store skill information in context variables

## Output Requirements

**State Updates**:
- `context.skill_name`: Selected skill name (string)
- `context.skill_path`: Full path to skill directory
- `context.skill_prompt_file`: Path to main skill prompt file
- `context.file_to_backup`: Set to same as skill_prompt_file (for backup task)
- `task_status.select-skill`: "completed"

**Files Created**: None

**Context Passed to Next Tasks**:
- Next task will use `context.skill_name` and `context.skill_prompt_file`
