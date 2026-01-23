# Generate AI Agent Instructions

**Analyze codebase to generate platform-agnostic AI agent instruction files for any coding assistant.**

## What It Does

This skill analyzes your codebase and generates comprehensive instruction files that help AI coding assistants (GitHub Copilot, Cursor, Windsurf, Cline, Kiro, etc.) understand your project's:

- Architecture and design decisions
- Critical patterns and conventions
- Build and development workflows
- Common tasks and scenarios
- Project-specific best practices

## Key Features

### 🔍 **Multi-Platform Support**
Automatically detects and generates instructions for:
- **GitHub Copilot**: `.github/copilot-instructions.md`
- **Cursor**: `.cursorrules`, `.cursor/rules/`
- **Windsurf**: `.windsurfrules`, `.windsurf/rules/`
- **Cline**: `.clinerules`, `.cline/rules/`
- **Kiro**: `.kiro/steering/`
- **Generic**: `AGENTS.md` (works with any assistant)

### 📊 **Intelligent Analysis**
- Scans project structure and identifies patterns
- Detects languages, frameworks, and build tools
- Finds integration points and dependencies
- Extracts critical workflows and conventions
- Focuses on project-specific knowledge (not generic advice)

### 🔄 **Merge Existing Content**
- Discovers existing AI instruction files
- Preserves valuable existing guidance
- Updates outdated sections
- Consolidates multiple platform files

### ✅ **Quality Assurance**
- 150-250 line target (concise but comprehensive)
- References actual files and directories
- Includes real commands and workflows
- Explains "why" behind decisions
- Validates completeness before creation

## When to Use

- Setting up a new project for AI-assisted development
- Onboarding team members using different AI coding tools
- Documenting project-specific patterns for AI assistants
- Migrating between AI coding platforms
- Improving AI assistant effectiveness in your codebase

## How It Works

1. **Platform Discovery** - Detects which AI tools you use
2. **Codebase Analysis** - Examines structure, patterns, workflows
3. **Proposal** - Shows analysis summary and proposed output
4. **Generation** - Creates platform-appropriate instruction file
5. **Validation** - Ensures quality and completeness

## Output

Creates one or more files like:

**`AGENTS.md`** (generic):
```markdown
# AI Assistant Instructions for MyProject

## 🚨 CRITICAL RULES FOR AI BEHAVIOR
[Project-specific guidelines]

## Repository Overview
[Architecture, tech stack, components]

## File Structure Guidelines
[Directory purposes and conventions]

## Development Workflows
[Build, test, run commands]

## Common User Scenarios
[Step-by-step guidance for common tasks]

## AI Assistant Guidelines
[Topic-specific guidance with file references]
```

## Comparison to Other Skills

### vs `onboard-me`
- **`onboard-me`**: Human-focused repository guide (300-1500 lines, setup/build/test commands)
- **`generate-ai-agent-instructions`**: AI-focused guidance (150-250 lines, patterns/conventions/"why")

**Use both**: `onboard-me` for humans, this skill for AI agents.

### vs `generate-tech-spec-from-code`
- **`generate-tech-spec-from-code`**: Detailed technical specification
- **`generate-ai-agent-instructions`**: Practical guidance for AI assistants

## Example Usage

```bash
# Auto-detect platform and generate
olaf generate ai agent instructions

# Explicit platform
olaf generate ai agent instructions --platform cursor

# For generic AGENTS.md
olaf generate ai agent instructions --platform generic
```

## Quality Standards

Generated instructions must:
- ✅ Reference actual files/directories from your codebase
- ✅ Include real commands that work in your project
- ✅ Explain project-specific patterns (not generic best practices)
- ✅ Document the "why" behind architectural decisions
- ✅ Stay concise (150-250 lines) while being comprehensive
- ✅ Be actionable (what to DO, not just theory)

## Related Skills

- **`onboard-me`** - Human-focused repository guide
- **`generate-tech-spec-from-code`** - Technical specification from code
- **`bootstrap-functional-spec-from-code`** - Functional spec generation
