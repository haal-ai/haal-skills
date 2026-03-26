# generate-ai-agent-instructions

## Overview
Analyze a codebase to generate platform-specific AI agent instruction files such as AGENTS.md, .cursorrules, .windsurfrules, .kiro/steering, and Copilot instructions.

## Purpose
Onboard AI coding assistants to your project by automatically generating instruction files that teach them your codebase conventions, architecture, and patterns. Supports auto-detection of the target platform or explicit selection.

## Key Features
- Multi-platform support: Copilot, Cursor, Windsurf, Cline, Kiro, Generic (AGENTS.md)
- Auto-detection of target platform from existing config files
- Deep codebase analysis (architecture, patterns, conventions)
- Merge capability with existing instruction files
- Platform-specific output format and location
- Validation and feedback cycle

## Usage
Invoke this skill by saying:
- "Generate AI agent instructions for this project"
- "Create .cursorrules for this codebase"
- "Set up Copilot instructions"
- "Onboard AI agents to this repo"

## Parameters

### Optional
- **target_platform**: auto | copilot | cursor | windsurf | cline | kiro | generic (default: auto)
- **merge_existing**: Whether to merge with existing instructions (prompts if found)
- **output_location**: Custom output path (auto-detected by default)

## Process Flow
1. **Platform Detection** — Identify target platform from existing files or user choice
2. **Codebase Analysis** — Scan architecture, patterns, tech stack, conventions
3. **Instruction Generation** — Create platform-specific instruction content
4. **Validation** — Verify completeness and accuracy
5. **User Approval** — Present proposed output for review
6. **File Creation** — Write instruction files to appropriate locations

## Output
Platform-specific instruction files:
- Copilot: `.github/copilot-instructions.md`
- Cursor: `.cursorrules`
- Windsurf: `.windsurfrules`
- Kiro: `.kiro/steering/`
- Generic: `AGENTS.md`

## Related Skills
- **onboard-local**: Offline onboarding that generates standards and commands
- **review-skill-quality**: Quality review for skill files
