# straf-cli-launcher

## Overview
Interactive launcher for the STRAF CLI tool. Presents available commands, collects parameters, and executes STRAF operations in spawn or interactive mode.

## Purpose
Provide a guided interface for running STRAF CLI commands (analyze, collaborate, multi-persona, team-design, jsdoc-gen, doc-external, web-research, researcher, refactor, document-api) without memorizing command syntax.

## Key Features
- 10 STRAF CLI commands available
- Interactive parameter collection per command schema
- Spawn (background) and interactive execution modes
- Parameter validation before execution
- Includes sub-skills: straf-skill-runner and test-straf

## Usage
Invoke this skill by saying:
- "Launch STRAF CLI"
- "Run a STRAF analysis"
- "Use STRAF to collaborate on this code"

## Parameters

### Required
- **command**: The STRAF command to run (selected from menu)
- **command-specific parameters**: Varies per command (collected interactively)

### Execution Mode
- **spawn**: Background execution via STRAF agent
- **interactive**: Direct terminal interaction

## Available Commands
| Command | Description |
|---------|-------------|
| analyze | Analyze code structure and patterns |
| collaborate | Multi-agent collaboration session |
| multi-persona | Multi-persona code review |
| team-design | Team architecture design session |
| jsdoc-gen | Generate JSDoc documentation |
| doc-external | Document external APIs |
| web-research | Web research on a topic |
| researcher | Deep research agent |
| refactor | Guided refactoring session |
| document-api | API documentation generation |

## Process Flow
1. **Present Commands** — Show available STRAF CLI commands
2. **Collect Parameters** — Gather required inputs per command schema
3. **Validate** — Check parameters before execution
4. **Execute** — Run in spawn or interactive mode
5. **Display Results** — Show output

## Output
- STRAF CLI command output (varies by command)

## Related Skills
- **straf-skill-runner**: Launch any OLAF skill via STRAF
- **test-straf**: Integration testing for STRAF agent
