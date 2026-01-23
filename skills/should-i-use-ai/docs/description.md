# should-i-use-ai

## Overview

The `should-i-use-ai` skill analyzes user tasks and recommends whether to use AI/LLM capabilities or traditional IDE tools. It provides specific guidance based on a task categorization framework to help developers choose the most efficient approach.

## Purpose

This skill helps developers make informed decisions about when to leverage AI assistance versus when traditional IDE tools are more appropriate. By categorizing tasks and providing specific recommendations, it optimizes workflow efficiency and ensures the right tool is used for each job.

## Key Features

- **Task Analysis**: Evaluates task descriptions against a categorization guide
- **Clear Recommendations**: Provides definitive AI or IDE tool guidance
- **Specific Actions**: Includes IDE features, keyboard shortcuts, and CLI alternatives
- **Prompt Suggestions**: Generates AI prompts when LLM is recommended
- **Reasoning Explanations**: Explains why each recommendation is made

## Usage

Invoke the skill with a task description:

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| Task description | string | Yes | Single sentence describing what you want to accomplish |

## Decision Framework

**Use AI/LLM for tasks requiring:**
- Logic and reasoning
- Context-aware code generation
- Intelligent refactoring and architecture
- API and framework migration
- Domain-specific understanding
- Quality and security analysis

**Use IDE Tools for tasks involving:**
- Basic code manipulation
- File and project operations
- Navigation and search
- Template-based code generation
- Formatting and style
- Debugging and analysis tools
- Version control integration
- Build and deployment

## Process Flow

1. **Analyze Task**: Evaluate the task against the LLM vs IDE categorization guide
2. **Categorize**: Determine if task requires reasoning/context or is mechanical/pattern-based
3. **Generate Recommendation**: Provide specific guidance based on categorization
4. **Explain Reasoning**: Include brief explanation of why the recommendation was made

## Output

### For IDE Tool Recommendations:
- Task category from the guide
- Specific IDE features and functionality
- Keyboard shortcuts (if applicable)
- CLI alternatives (if applicable)
- Explanation of why IDE tools are appropriate

### For AI/LLM Recommendations:
- Task category from the guide
- Search suggestions for existing prompts
- Generated prompt specific to the task
- Pattern phrases for competency index
- Explanation of why AI is appropriate

## Examples

**Task**: "Generate getter methods for my class"

**Recommendation**: Use IDE Tools
- Category: Basic Code Manipulation
- Action: Right-click → Generate → Getter/Setter
- Why: Template-based, mechanical operation

---

**Task**: "Fix memory leak in my application"

**Recommendation**: Use AI/LLM
- Category: Logic & Reasoning Tasks
- Why: Requires code behavior analysis and reasoning about memory patterns

## Error Handling

| Scenario | Behavior |
|----------|----------|
| Ambiguous task description | Asks for clarification on the specific task |
| Task spans both categories | Provides guidance for both approaches |
| Unknown task type | Defaults to AI recommendation with explanation |

## Related Skills

- `assist-me-as-prompt-engineer` - For crafting effective AI prompts
- `assess-genai-initiative-idea` - For evaluating AI project ideas
