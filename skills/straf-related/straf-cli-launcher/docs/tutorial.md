# straf-cli-launcher

> Step-by-step tutorial for using the STRAF CLI launcher

## Prerequisites
- STRAF CLI installed and accessible
- Codebase to analyze (for most commands)

## Estimated Time
5–15 minutes (depends on command)

## Step-by-Step Instructions

### Step 1: Launch the Skill
> "Launch STRAF CLI"

A menu of available commands is presented.

### Step 2: Select a Command
Choose from the 10 available commands:
1. **analyze** — Code structure analysis
2. **collaborate** — Multi-agent collaboration
3. **multi-persona** — Multi-persona review
4. **team-design** — Architecture design session
5. **jsdoc-gen** — JSDoc generation
6. **doc-external** — External API documentation
7. **web-research** — Web research
8. **researcher** — Deep research
9. **refactor** — Guided refactoring
10. **document-api** — API docs generation

### Step 3: Provide Parameters
Each command has specific parameters. The skill walks you through collecting each one. Common parameters include:
- Target file or directory
- Output location
- Specific options for the command

### Step 4: Choose Execution Mode
- **Spawn**: Runs in the background via STRAF agent (recommended for long tasks)
- **Interactive**: Direct terminal interaction (recommended for collaborative commands)

### Step 5: Review Results
Command output is displayed. For spawn mode, results appear when the background task completes.

## Troubleshooting

| Issue | Solution |
|-------|----------|
| STRAF CLI not found | Verify STRAF is installed and on PATH |
| Command fails | Check parameters match expected schema |
| Spawn mode hangs | Check STRAF agent status |
| Wrong output format | Specify output parameters explicitly |

## Verification Checklist
- [ ] STRAF CLI is accessible
- [ ] Command selected from menu
- [ ] Parameters collected and validated
- [ ] Execution mode chosen
- [ ] Output received and reviewed
