# Test STRAF - Automated Code Review with Agentic Framework

## Overview

The `test-straf` skill demonstrates integration of the STRAF (Strategic Task Routing & Agent Framework) agentic framework for automated code review. This skill showcases how to call STRAF agents from within OLAF skill chains to perform autonomous AI-powered tasks.

## Purpose

- **Test STRAF Integration**: Validate that STRAF agents can be called from OLAF skills
- **Demonstrate Agentic Workflow**: Show how to use autonomous agents in skill chains
- **Automated Code Review**: Provide practical example of AI-powered code analysis
- **Multi-language Support**: Handle both Python and Go code reviews

## How It Works

### Chain Architecture

The skill uses a 5-task chain to orchestrate the STRAF agent:

1. **Retrieve Timestamp** (Common Task)
   - Gets environment information
   - Generates session timestamp

2. **Detect Language**
   - Scans workspace for .py or .go files
   - Determines primary language
   - Builds file list for review

3. **Prepare Context**
   - Selects language-specific review prompt
   - Prepares file context array
   - Sets execution mode (interactive/spawned)

4. **Execute STRAF** (Common Task)
   - Calls STRAF wrapper with prompt and context
   - Waits for agent completion (interactive mode)
   - Captures review results

5. **Display Results**
   - Formats and shows review output
   - Provides output file location
   - Extracts summary statistics

### STRAF Agent Execution

The skill leverages the common `call-straf-agent` task to:
- Pass code files as context to the agent
- Use language-specific review prompts
- Execute agent via wrapper script
- Capture and process results

## Supported Languages

### Python
- Review prompt: `review-python-code.md`
- Checks: PEP 8, best practices, design patterns
- Focus: Pythonic idioms, error handling, type hints

### Go
- Review prompt: `review-go-code.md`
- Checks: Go idioms, error handling, goroutines
- Focus: Simplicity, interfaces, resource management

## Usage

### Basic Usage

```
olaf test-straf
```

The skill will:
1. Auto-detect language from workspace files
2. Review all found code files
3. Display comprehensive review

### Specify Language

```
olaf test-straf for Python files
olaf test-straf for Go code
```

### Specify Files

```
olaf test-straf review src/main.py and src/utils.py
```

## Output

### Review Format

```
═══════════════════════════════════════════════════════
🤖 STRAF Agent Code Review
═══════════════════════════════════════════════════════
Language: python
Files Reviewed: 3
Review Type: Automated (STRAF Agent)
═══════════════════════════════════════════════════════

# Python Code Review Summary

## Files Reviewed
- src/main.py
- src/utils.py
- src/config.py

## Overall Assessment
Good - Well-structured code with minor improvements needed

## Strengths
- Clear function naming and documentation
- Proper error handling in critical paths
- Good use of type hints

## Issues Found
[Detailed issues...]

## Recommendations
[Actionable suggestions...]

═══════════════════════════════════════════════════════
📁 Review saved to: .olaf/work/staging/straf-output-20251121-085234.txt
═══════════════════════════════════════════════════════
```

## Technical Details

### STRAF Integration

Uses the `call-straf-agent` common task which:
- Accepts prompt file path
- Takes context files array
- Supports interactive/spawned modes
- Returns structured results

### Execution Modes

**Interactive Mode** (default for this skill):
- Waits for agent completion
- Results immediately available
- Takes 30-120 seconds
- Best for immediate feedback

**Spawned Mode** (available in common task):
- Runs in background
- Returns task ID
- Can check status later
- Best for long-running tasks

## Configuration

### Requirements

- AWS Bedrock access with Claude models
- Python packages: `strands-agents`, `boto3`, `psutil`
- AWS profile: `bedrock` (configured)
- STRAF framework at `~/.olaf/core/agentic/straf/`

### Prompts

Located at `~/.olaf/core/agentic/straf/prompts/`:
- `review-python-code.md` - Python review prompt
- `review-go-code.md` - Go review prompt

## Extending the Skill

### Add New Language

1. Create review prompt: `~/.olaf/core/agentic/straf/prompts/review-[language]-code.md`
2. Update `task-1-detect-language.md` to search for file extension
3. Update `task-2-prepare-context.md` to select new prompt

### Customize Review Criteria

Edit the language-specific prompt files to:
- Add/remove review criteria
- Change output format
- Adjust review depth
- Focus on specific patterns

### Use Spawned Mode

Change in `task-2-prepare-context.md`:
```markdown
Set `context.straf_mode` = "spawned"
```

Then add status checking task to monitor completion.

## Limitations

- Currently supports Python and Go only
- Reviews limited to ~10 files (can be adjusted)
- Requires AWS Bedrock access
- Interactive mode blocks until completion

## Future Enhancements

- [ ] Support for JavaScript, TypeScript, Java
- [ ] Parallel review of multiple files (spawned mode)
- [ ] Custom review checklist input
- [ ] Integration with CI/CD pipelines
- [ ] Comparison with human reviews
