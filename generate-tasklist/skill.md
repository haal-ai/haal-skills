---
name: generate-tasklist
description: Generate structured tasklists with iteration-task-subtask hierarchy and status tracking
license: Apache-2.0
metadata:
  olaf_tags: [tasklist, planning, project, iteration, tasks]
  copyright: Copyright (c) 2026 pjmp020564
  author: pjmp020564 (on github)
  repository: https://github.com/haal-ai/haal-ide
  provider: Haal AI
---

<olaf>

## Input Parameters

**IMPORTANT**: When you don't have entries provided, ask the USER to provide them.
- **project_purpose**: string - Brief description of the overall goal or project
- **iteration_type**: single|multiple - Whether project has single or multiple iterations
- **iterations_list**: array - List of iteration names/descriptions (if multiple)
- **major_tasks**: array - High-level tasks for each iteration

## Process
1. **Gather Requirements**:
   - Ask: "What is the purpose of this tasklist?"
   - Ask: "Single or multiple iterations?"
   - If multiple: "Please list iteration names/descriptions"
   - Ask: "What are the major tasks for each iteration?"
2. **Generate Tasklist Structure**:
   - Use template: `templates/project-manager/tasklist-template.md.md`
   - Apply status prefixes: todo, wip, done, dump
   - Follow iteration-task-subtask hierarchy
   - Enforce constraints: max 7 tasks per iteration, max 7 subtasks per task
3. **Present for Review**:
   - Display proposed tasklist structure
   - Request user amendments
   - Apply modifications as requested

## Output Format

Follow template structure: `templates/project-manager/tasklist-template.md.md`

## Output to USER
- Present proposed tasklist for review
- Request amendments and modifications
- Confirm final structure
