---
name: straf-skill-runner
description: Automatically analyze OLAF skill input requirements, intelligently gather required parameters from workspace context or user input, and execute skills via STRAF agent in fully autonomous spawned mode
license: Apache-2.0
---

 ---
name: straf-skill-runner
description: Interactive skill launcher - lists skills, analyzes requirements, gathers parameters, and launches via STRAF
tags: [straf, skill, execution, interactive, launcher]
protocol: Propose-Act
aliases: [run skill with straf, execute skill, launch skill]
  copyright: Copyright (c) 2026 pjmp020564
  author: pjmp020564 (on github)
  repository: https://github.com/haal-ai/haal-ide
  provider: Haal AI
---

# STRAF Skill Runner - Interactive Skill Launcher

## Purpose
Present available OLAF skills, analyze the selected skill's parameter requirements, gather inputs from user, and launch execution via STRAF agent in background.

## Process Flow

### Step 1: Present Skill List
List available skills from `~/skills/` directory for user to choose from.

Example:
```
Available Skills:
1. search-and-learn - Research and learn about a topic
2. researcher - Deep research on a topic  
3. review-code - Code review
4. create-skill - Create a new skill
...

Which skill would you like to run? (enter number or name)
```

### Step 2: Analyze Selected Skill
Read the selected skill's prompt file and extract required parameters from:
- `## Input Parameters` section
- Inline `{parameter_name}` placeholders
- YAML frontmatter `inputs:` fields

Example extraction from `search-and-learn.md`:
```markdown
## Input Parameters
- **learning_objective**: string - What you want to learn (REQUIRED)
```

Identify all REQUIRED parameters only.

### Step 3: Gather Parameters from User
For each required parameter, ask user to provide the value.

Example:
```
Parameter: learning_objective
Description: What you want to learn
Your value: [user enters "Docker security"]
```

### Step 4: Confirm Launch
Show summary and ask for confirmation before proceeding:

```
Ready to launch via STRAF:
  Skill: search-and-learn
  Parameters:
    - learning_objective: Docker security

Proceed? (y/n)
```

### Step 5: Execute and Terminate
If user confirms, execute:

```bash
python ~/skills/straf-skill-runner/utils/run_skill.py \
  --prompt ~/skills/search-and-learn/prompts/search-and-learn.md \
  --context "learning_objective=Docker security"
```

Report the output from run_skill.py:
```
✅ Spawned: PID 12345
📊 Timestamp: 20251127-160142-169

Skill launched successfully! STRAF agent running in background.
```

Then **TERMINATE** - no further interaction needed.
