---
name: generate-ai-agent-instructions
description: Analyze codebase to generate platform-agnostic AI agent instruction files (AGENTS.md, .cursorrules, .windsurfrules, .kiro/steering, etc.)
license: Apache-2.0
metadata:
  olaf_tags: [ai-agents, codebase-analysis, documentation, platform-agnostic, onboarding]
---

if you are in need to get the date and  time, use time tools, fallback to shell command if needed

## Input Parameters
You MUST request these parameters if not provided by the user:
- **target_platform**: string - Target AI platform ("auto" | "copilot" | "cursor" | "windsurf" | "cline" | "kiro" | "generic") (OPTIONAL - defaults to "auto")
- **merge_existing**: boolean - Whether to merge with existing instructions (OPTIONAL - will prompt if found)
- **output_location**: string - Custom output path (OPTIONAL - will auto-detect)

## User Interaction
Ask for user approval before creating or modifying files.
- Present analysis summary and proposed output before generating
- Request final confirmation before file creation

## Platform Detection Matrix

### Supported Platforms
```yaml
platforms:
  copilot:
    files: [".github/copilot-instructions.md", ".github/instructions.md"]
    priority: 1
    
  cursor:
    files: [".cursorrules", ".cursor/rules/*.md"]
    priority: 2
    
  windsurf:
    files: [".windsurfrules", ".windsurf/rules/*.md"]
    priority: 3
    
  cline:
    files: [".clinerules", ".cline/rules/*.md"]
    priority: 4
    
  kiro:
    files: [".kiro/steering/*.md"]
    priority: 5
    
  generic:
    files: ["AGENTS.md", "AGENT.md", "AI-INSTRUCTIONS.md"]
    priority: 6
```

## Process

## Search Budget (Avoid Search Loops)

To avoid getting stuck in repetitive/expanding searches (especially in large repos), you MUST follow these limits:

- You MUST NOT run the same broad workspace search more than once.
- You MUST cap discovery to **two passes**:
  1) AI-instructions discovery (platform files only)
  2) Build/stack discovery (package/build files only)
- If discovery output is too large or truncated, you MUST NOT re-run the same search; instead you MUST narrow scope (e.g., only root + top-level folders) or ask the user which subfolder to focus on.
- If the repo appears to be a “collection repo” (many independent subprojects), you MUST ask the user which subproject path to target.

### 1. Platform Discovery Phase
You WILL detect existing AI instruction files:

**Search Pattern (single glob)**:

IMPORTANT: Do NOT include `README.md` in this discovery search (it can match hundreds/thousands of files and cause looping/truncation).

```
**/{.github/copilot-instructions.md,.github/instructions.md,AGENTS.md,AGENT.md,AI-INSTRUCTIONS.md,CLAUDE.md,.cursorrules,.windsurfrules,.clinerules,.cursor/rules/*,.windsurf/rules/*,.cline/rules/*,.kiro/steering/*}
```

**Analyze Findings**:
- Identify which platforms are currently used (workspace has their config files)
- Extract valuable existing guidance from found files
- Determine primary platform based on file presence and priority
- Note outdated or incomplete sections
- Understand current documentation approach

**Auto-Detection Logic**:
```python
if target_platform == "auto":
    detected_platforms = []
    for each found file:
        match to platform in matrix
        add to detected_platforms
    
    if len(detected_platforms) == 1:
        use that platform
    elif len(detected_platforms) > 1:
        ask user which to prioritize
    else:
        default to "generic" (AGENTS.md)
```

### 2. Codebase Analysis Phase
You WILL systematically examine the workspace:

**CRITICAL**: Exclude these directories from analysis:
- `.git`, `.github`
- `.olaf/**` (EXCEPT you may read `.olaf/team-delegation.md` when required)
- `node_modules`, `.venv`, `venv`, `dist`, `build`, `out`, `target`, `.next`, `.cache`, `coverage`, `.idea`, `.vscode`

**Architecture & Organization**:
- Project type (monolith, microservices, library, framework)
- Directory structure and module organization
- Layering patterns (presentation, business logic, data access)
- Component boundaries and responsibilities

**Languages & Frameworks**:
- Primary programming languages (file extensions, package managers)
- Frameworks and major libraries from:
  - `package.json`, `package-lock.json` (Node.js)
  - `requirements.txt`, `pyproject.toml` (Python)
  - `pom.xml`, `build.gradle` (Java)
  - `*.csproj`, `packages.config` (C#/.NET)
  - `go.mod`, `go.sum` (Go)
  - `Cargo.toml` (Rust)
- Version constraints and compatibility requirements

**Build & Development Workflows**:
- Build systems (Maven, Gradle, npm, Make, MSBuild)
- Build configuration (Jenkinsfile, .github/workflows, azure-pipelines.yml)
- Test frameworks and organization
- Deployment configs (Dockerfile, k8s manifests, terraform)
- Development scripts (package.json scripts, Makefiles)

**Critical Patterns** (project-specific):
- Error handling approaches
- Logging and monitoring patterns
- Configuration management (env vars, config files)
- Database access patterns and ORM usage
- API design conventions (REST, GraphQL, gRPC)
- Authentication/authorization patterns
- Common utilities and helper functions

**Integration Points**:
- External service dependencies
- Inter-service communication patterns
- Third-party API integrations
- Message queues or event systems
- Database connections and migrations

### 3. User Confirmation Phase (Propose-Confirm-Act)
You WILL present findings and proposal:

```markdown
## Analysis Summary

**Detected Platform(s)**: [platform names]
**Existing Files Found**: [list files]
**Primary Language**: [language]
**Frameworks**: [list]
**Build Tool**: [tool]

**Proposed Output**:
- Create: [filename and path]
- Merge existing: [yes/no]
- Estimated size: [150-250 lines]

**Sections to Include**:
1. Critical Rules for AI Behavior
2. Repository Overview
3. Architecture & Key Concepts
4. File Structure Guidelines
5. Development Workflows
6. Common User Scenarios
7. AI Assistant Guidelines

**Proceed with generation?**
```

Wait for user confirmation before proceeding.

### 4. Handle Existing Instructions
If existing platform-specific files found:

**Ask User**:
```
I found existing AI instructions in [filename]. Would you like me to:
1. Merge content into new file (preserves valuable guidance)
2. Update existing file in place
3. Create new file without merging (fresh start)
4. Create both with synced content
```

**When Merging**:
- Preserve valuable existing content
- Update outdated sections with current findings
- Remove generic advice that doesn't reflect actual patterns
- Maintain project-specific guidance that's still relevant
- Ensure consistent structure and formatting

### 5. Generate AI Agent Instructions
You WILL create comprehensive instructions:

**Template Structure** (adapt per platform conventions):

```markdown
# AI Assistant Instructions for [Project Name]

## 🚨 CRITICAL RULES FOR AI BEHAVIOR

[Project-specific critical guidelines]
[File handling rules]
[Required approvals or workflows]
[Security considerations]

## Repository Overview

[One paragraph: what this project does, its purpose]

**Key Components**:
- **[Component 1]** - [Brief description, location]
- **[Component 2]** - [Brief description, location]
- **[Component 3]** - [Brief description, location]

**Technology Stack**:
- Language: [primary language + version]
- Framework: [main framework + version]
- Build: [build tool]
- Testing: [test framework]

## Understanding the Architecture

[2-3 paragraphs explaining high-level architecture]
[Include WHY decisions were made, not just WHAT exists]
[Reference actual directories/files: "See src/services/ for business logic"]

**Architectural Pattern**: [monolith | microservices | layered | hexagonal | event-driven]

**Key Concepts Users Will Encounter**:
1. **[Concept 1]** - [Explanation with file references]
2. **[Concept 2]** - [Explanation with file references]
3. **[Concept 3]** - [Explanation with file references]
4. **[Concept 4]** - [Explanation with file references]
5. **[Concept 5]** - [Explanation with file references]

## File Structure Guidelines

### `/[directory-name]/`
**Purpose**: [What this directory contains and why]
**Conventions**: [Naming patterns, organization rules]
**Key Files**:
- `[filename]` - [Purpose, when to modify]
- `[filename]` - [Purpose, when to modify]

[Repeat for each major directory: src/, tests/, config/, docs/, etc.]

## Development Workflows

### Building the Project
```bash
[Exact commands to build - no placeholders]
[Explain any non-obvious flags or options]
```

### Running Tests
```bash
[Specific test commands for this project]
[Unit tests, integration tests, e2e tests]
```

**Test Organization**:
- [Explain test structure and naming conventions]
- [Where to add new tests]
- [How to run specific test suites]

### Running Locally
```bash
[Commands to start dev server/application]
[Required environment variables]
[Default ports and URLs]
```

### Debugging
[Project-specific debugging approaches]
[Common issues and solutions]
[Where to find logs]

### Deployment
[How deployment works for this project]
[Environments: dev, staging, prod]
[Deployment triggers and process]

## Common User Scenarios

### Scenario: Adding New Feature
1. [Step-by-step specific to this codebase]
2. [Reference actual files and patterns]
3. [Include test requirements]
4. [Mention deployment considerations]

### Scenario: Fixing Bug
1. [Where to look based on symptom]
2. [Common debugging steps]
3. [Test verification approach]

### Scenario: Updating Dependencies
1. [Project-specific update process]
2. [What to verify after updates]
3. [How to test compatibility]

### Scenario: Refactoring Code
1. [Project conventions to maintain]
2. [What supporting files to update (README, docs, presentations)]
3. [How to verify functional equivalence]

**⚠️ Important**: If changes affect documentation in `docs/presentations/`, identify which presentations are outdated and inform the user, but do NOT automatically update presentations.

## AI Assistant Guidelines

### When Users Ask About:

**[Topic 1: e.g., Authentication]**: 
[Specific guidance referencing actual files]
Example: "Uses JWT tokens configured in `src/config/auth.ts`, see middleware in `src/middleware/auth.middleware.ts`"

**[Topic 2: e.g., Database]**: 
[Specific guidance referencing actual patterns]
Example: "PostgreSQL with TypeORM, entities in `src/entities/`, migrations in `src/migrations/`"

**[Topic 3: e.g., API Endpoints]**: 
[Specific guidance with examples]
Example: "RESTful pattern, controllers in `src/controllers/`, follow `*.controller.ts` naming"

**[Topic 4: e.g., Error Handling]**: 
[Project-specific approach]
Example: "Custom error classes in `src/errors/`, centralized handler in `src/middleware/error.middleware.ts`"

**[Topic 5: e.g., Logging]**: 
[Where and how]
Example: "Winston logger configured in `src/utils/logger.ts`, use structured logging with context"

### Code Examples to Reference
[If there are exemplar files or patterns, list them]
- `[file]` - Good example of [pattern]
- `[file]` - Shows proper [technique]

### Project-Specific Best Practices
1. [Practice specific to THIS project, not generic advice]
2. [Convention that differs from standard approaches]
3. [Pattern that's critical to understand]
4. [Anti-pattern to avoid in this codebase]
5. [Quality requirement specific to this project]

### Common Pitfalls to Avoid
- [Specific mistake developers make in this codebase]
- [Configuration that's easy to get wrong]
- [Pattern that looks right but breaks something]

## Quick Reference

**Build**: `[command]`
**Test**: `[command]`
**Run**: `[command]`
**Deploy**: `[process]`

**Need Help?**: [Where to find more info - README, wiki, team contacts]
```

**Quality Requirements**:
- ✅ **Length**: 150-250 lines (concise but comprehensive)
- ✅ **Specificity**: Every example references actual files/directories
- ✅ **Actionable**: Focus on what to DO, not theory
- ✅ **Discoverable**: Document only patterns in the code
- ✅ **Concrete**: Include actual commands, paths, patterns
- ✅ **Why not just what**: Explain architectural decisions

### 6. Platform-Specific Adaptations

**For GitHub Copilot** (`.github/copilot-instructions.md`):
- Standard markdown format
- Can use GitHub-flavored markdown features
- Reference GitHub workflows if present

**For Cursor** (`.cursorrules`):
- Single file format
- Focus on code patterns and conventions
- Can include inline code examples

**For Windsurf** (`.windsurfrules` or `.windsurf/rules/codebase-guide.md`):
- Support for multiple rule files in directory
- Structured sections preferred
- Clear headings for navigation

**For Cline** (`.clinerules`):
- Similar to Cursor format
- Single file recommended
- Emphasis on task-oriented guidance

**For Kiro** (`.kiro/steering/codebase-guide.md`):
- Markdown files in steering directory
- Can have multiple files for different aspects
- Structured with clear sections

**For Generic** (`AGENTS.md`):
- Platform-independent markdown
- Works with any AI coding assistant
- Most comprehensive format

### 7. Validation Phase
Before finalizing, verify:

✅ **Contains Specific Examples** - Every section references actual files/directories
✅ **Avoids Generic Advice** - No "write tests" without project context
✅ **Documents Real Patterns** - All patterns discoverable in codebase
✅ **Includes Commands** - Build/test/deploy commands are accurate
✅ **References Key Files** - Important files identified with purposes
✅ **Explains Architecture** - Big picture clear with "why" behind decisions
✅ **Stays Concise** - Within 150-250 line target
✅ **Clear Structure** - Markdown formatting consistent and scannable
✅ **Platform Appropriate** - Follows conventions for target platform

### 8. File Creation Phase
Based on platform and user preference:

**Create File(s)**:
- Write to appropriate location
- Use platform-specific formatting if needed
- Ensure proper markdown structure

**Display Summary**:
```
📝 AI Agent Instructions Generated

Platform: [platform name]
File: [full path]
Lines: [actual count]
Sections: [number of major sections]

Key Coverage:
✓ Architecture: [brief summary]
✓ Workflows: [commands identified]
✓ Patterns: [number of specific patterns]
✓ Integration Points: [number of dependencies]

Next Steps:
- Review the generated file
- Test with your AI coding assistant
- Update as project evolves
```

### 9. Feedback Request
Ask user:

```
I've generated AI agent instructions for this codebase. Please review:

1. **Clarity**: Are all sections clear and well-explained?
2. **Completeness**: Any missing workflows, patterns, or conventions?
3. **Accuracy**: All commands, paths, and patterns correct?
4. **Specificity**: Any sections too generic needing project-specific examples?

Let me know what needs adjustment.
```

## Error Handling

**If No Clear Architecture**:
- Document structure as-is
- Note that it may be evolving
- Describe what exists without forcing patterns

**If Multiple Conflicting Patterns**:
- Document both patterns
- Note when each is used
- Explain the context for each

**If Sparse Codebase**:
- Focus on what exists
- Don't invent patterns
- Keep documentation minimal but accurate

**If Missing Build Files**:
- Note the absence
- Ask user for build instructions
- Document manual setup if needed

**If Incomplete Dependencies**:
- Document what's discoverable
- Flag what's unclear
- Request user clarification

## Domain-Specific Rules

**Platform Selection**:
- RESPECT existing platform choices (don't force migration)
- OFFER platform-specific optimizations when detected
- DEFAULT to generic AGENTS.md if no platform detected

**Content Quality**:
- FOCUS on project-specific guidance, not universal best practices
- REFERENCE actual files and code patterns from the workspace
- EXPLAIN the "why" behind architectural decisions
- AVOID placeholders or generic examples

**Maintenance**:
- SUGGEST updating instructions when major changes occur
- KEEP instructions synchronized if multiple platform files exist
- VERSION instructions with date/timestamp in frontmatter

⚠️ **Critical Requirements**:
- MANDATORY: Analyze actual codebase before generating
- MANDATORY: Reference real files and directories
- NEVER generate generic "best practices" without project context
- ALWAYS ask for user approval before creating files
- ALWAYS validate against quality checklist before presenting

## Related Skills
- `onboard-me` - Generate human-focused repository guide (repo-guide.md)
- `generate-tech-spec-from-code` - Technical specification from codebase
- `bootstrap-functional-spec-from-code` - Functional spec generation
