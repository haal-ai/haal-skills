---
task_id: "analyze-skill-structure"
task_name: "Analyze Existing Skill Structure"
dependencies: ["context.skill_prompt_file"]
conditions: []
---

# Analyze Existing Skill Structure

## Input Context
**Required Context Variables**: 
- `context.skill_name`: Name of the skill
- `context.skill_prompt_file`: Path to main skill prompt
**Required Files**: Skill prompt markdown file
**Required Tools**: File reading capabilities

## Task Instructions

### Read and Analyze Skill Prompt

1. **Read the entire skill prompt file**:
   - Use `read_file` to load the complete content
   - Identify file length and structure

2. **Extract Key Information**:
   - **Skill metadata**: name, description, tags, protocol
   - **Main sections**: Identify major logical sections
   - **Instructions**: List all instruction blocks
   - **Dependencies**: Note any external files, tools, or scripts referenced
   - **Workflow steps**: Identify sequential or conditional steps
   - **Context variables**: Find any state or context management

3. **Identify Complexity Indicators**:
   - Count major instruction sections
   - Identify decision points (if/then logic)
   - Note data transformation steps
   - Find external tool invocations
   - Detect file I/O operations

4. **Create Structure Summary**:
```markdown
**Skill Structure Analysis**:
- Name: [skill_name]
- Protocol: [protocol type]
- Complexity: [low/medium/high]
- Major Sections: [count]
- External Dependencies: [list]
- Workflow Type: [linear/conditional/iterative]
```

## Output Requirements

**State Updates**:
- `context.skill_structure`: JSON object with structure analysis
  ```json
  {
    "name": "skill-name",
    "complexity": "medium",
    "section_count": 5,
    "external_tools": ["tool1.py", "tool2.sh"],
    "workflow_type": "conditional",
    "has_loops": false,
    "has_file_io": true
  }
  ```
- `context.skill_content`: Full text of skill prompt (for later analysis)
- `task_status.analyze-skill-structure`: "completed"

**Files Created**: None

**Context Passed to Next Tasks**:
- `context.skill_structure` will be used to identify task boundaries
- `context.skill_content` will be parsed for task extraction
