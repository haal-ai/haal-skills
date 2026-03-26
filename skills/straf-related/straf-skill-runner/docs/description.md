# straf-skill-runner

## Overview
Interactive skill launcher that lists available OLAF skills, analyzes parameter requirements, gathers inputs, and launches execution via the STRAF agent.

## Purpose
Provide a menu-driven interface for discovering and running OLAF skills through STRAF. Handles parameter collection and supports both spawn (background) and interactive execution modes.

## Key Features
- Lists all available OLAF skills
- Analyzes parameter requirements per skill
- Interactive parameter gathering
- Spawn and interactive execution modes
- STRAF agent integration for execution

## Usage
Invoke this skill by saying:
- "Run an OLAF skill"
- "Launch a skill via STRAF"
- "Show me available skills and let me pick one"

## Parameters

### Required
- **skill_name**: Name of the OLAF skill to run (selected from menu)
- **skill_parameters**: Collected interactively based on skill requirements

## Process Flow
1. **List Skills** — Show available OLAF skills
2. **Select Skill** — User picks from the list
3. **Analyze Parameters** — Read skill.md to identify required inputs
4. **Collect Parameters** — Gather values interactively
5. **Launch Execution** — Run via STRAF agent (spawn or interactive)
6. **Display Results** — Show execution output

## Output
- Skill execution output (varies by skill)

## Related Skills
- **straf-cli-launcher**: Run STRAF CLI commands directly
- **test-straf**: Integration testing for STRAF agent
