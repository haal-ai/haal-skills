# Execute Generate Implementation Plan Skill

## Standalone Execution

Run this skill directly on an existing design.md file:

```powershell
python .\.olaf\core\agentic\straf\olaf_strands_agent.py `
  --prompt "skills/generate-implementation-plan/prompts/generate-implementation-plan.md" `
  --context "design_file=YOUR_DESIGN_FILE_PATH,output_file=YOUR_OUTPUT_FILE_PATH,skill_path=YOUR_SKILL_PATH" `
  --tool-mode standard `
  --aws-profile bedrock
```

## Example: Generate Plan for ESDI Output

```powershell
# Assuming ESDI generated design.md in .olaf/work/staging/esdi/20251122-repo-scanner/
python .\.olaf\core\agentic\straf\olaf_strands_agent.py `
  --prompt "skills/generate-implementation-plan/prompts/generate-implementation-plan.md" `
  --context "design_file=.olaf/work/staging/esdi/20251122-repo-scanner/design.md,output_file=.olaf/work/staging/esdi/20251122-repo-scanner/IMPLEMENTATION-TASK-PLAN.md,skill_path=skills/repo-scanner" `
  --tool-mode standard `
  --aws-profile bedrock
```

## Context Variables

**Required**:
- `design_file`: Path to design.md from generate-design skill
- `output_file`: Path for IMPLEMENTATION-TASK-PLAN.md output

**Optional**:
- `skill_path`: Target path for skill (default: `skills/${skill_name}`)
- `skill_name`: Override skill name (default: extracted from design)
- `include_bootstrap`: Include bootstrap command (default: true)

## What Happens

1. **Task 0**: Extracts layers & components from design.md → Propose-Act gate
2. **Task 1**: Generates Task 0.0 spec (onboarding 0.3 pattern) → Propose-Act gate
3. **Task 2**: Creates complete task breakdown → Propose-Act gate
4. **Task 3**: Generates STRAF commands for all tasks → Propose-Act gate
5. **Task 4**: Creates bootstrap integration command → Propose-Act gate
6. **Task 5**: Writes final IMPLEMENTATION-TASK-PLAN.md → Act

## After Generation

### Step 1: Execute Task 0.0 Manually

```powershell
python .\.olaf\core\agentic\straf\olaf_strands_agent.py `
  --prompt "olaf-core/competencies/onboard/tasks/setup/extract-task-contexts.md" `
  --context "bootstrap_doc=YOUR_OUTPUT_FILE_PATH,skill_path=YOUR_SKILL_PATH" `
  --tool-mode standard `
  --aws-profile bedrock
```

### Step 2: Execute Bootstrap (Autonomous)

```powershell
python .\.olaf\core\agentic\straf\olaf_strands_agent.py `
  --prompt "olaf-core/competencies/onboard/prompts/bootstrap-orchestrator.md" `
  --context "bootstrap_doc=YOUR_OUTPUT_FILE_PATH,checklist_path=.olaf/work/project-tasks/task-checklist.md" `
  --tool-mode auto `
  --aws-profile bedrock
```

## Via ESDI Workflow (Recommended)

This skill is automatically invoked in ESDI Phase 4:

```powershell
python .\.olaf\core\agentic\straf\olaf_strands_agent.py `
  --prompt "skills/run-esdi/prompts/run-esdi-coordinator.md" `
  --context "idea=Your idea here,topic=your-topic" `
  --tool-mode standard `
  --aws-profile bedrock
```

ESDI will run all 4 phases:
1. Exploration (challenge-me)
2. Specification (transform-raw-spec)
3. Design (generate-design)
4. **Implementation Planning (generate-implementation-plan)** ← THIS SKILL

## Notes

- ⚠️ **Task 0.0 must be run manually FIRST** before bootstrap execution
- ✅ All Propose-Act gates require user approval
- 📊 Typical execution: 20-30 minutes for plan generation
- 🚀 Bootstrap execution: Varies by plan size (estimate in plan)

## Troubleshooting

**If design.md format not recognized**:
- Ensure design.md has "Layer 1:", "Layer 2:" sections
- Components should be listed under each layer
- Dependencies should be explicit

**If skill_path conflicts**:
- Check if target path already exists
- Provide unique skill_path in context variables

**If Task 0.0 fails**:
- Verify implementation plan is valid markdown
- Check skill_path directory is writable
- Ensure STRAF agent has necessary permissions
