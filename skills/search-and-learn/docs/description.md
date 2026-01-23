# Search and Learn

## Overview

Search and Learn is a master coordinator skill for systematic information discovery, knowledge acquisition, and practical application. It follows a lean methodology approach to help users efficiently research topics, synthesize information, and apply their learning in practical contexts.

## Purpose

This skill addresses the challenge of conducting thorough, organized research by providing a structured 8-task workflow that guides users from initial goal definition through to actionable takeaways. It ensures comprehensive coverage while maintaining focus on practical outcomes.

## Key Features

- **Sequential Task Chain**: Executes 8 interconnected tasks in strict order for systematic learning
- **Context Passing**: Maintains state between tasks using simple variables for seamless workflow
- **Goal-Oriented**: Starts with clear learning objectives and success criteria
- **Search Strategy Development**: Creates prioritized, systematic search plans
- **Information Synthesis**: Evaluates, organizes, and connects discovered information
- **Practical Application**: Tests understanding through real-world application
- **Comprehensive Reporting**: Generates detailed learning reports with actionable insights

## Usage

Invoke this skill when you need to:
- Research a new topic systematically
- Learn a technology or concept with structured approach
- Gather and synthesize information from multiple sources
- Create actionable knowledge from research findings
- Document learning outcomes for future reference

## Parameters

This skill collects parameters interactively through its task chain:

| Parameter | Description | Collected In |
|-----------|-------------|--------------|
| learning_objective | User's specific learning goal | Task 1 |
| current_knowledge | User's knowledge baseline | Task 1 |
| application_context | Context and constraints | Task 1 |

## Process Flow

```
Task 1: Collect User Parameters
    ↓
Task 2: Validate Prerequisites
    ↓
Task 3: Define Learning Goals
    ↓
Task 4: Develop Search Strategy
    ↓
Task 5: Execute Systematic Search
    ↓
Task 6: Evaluate and Synthesize Information
    ↓
Task 7: Apply and Test Learning
    ↓
Task 8: Generate Learning Report
```

## Output

The skill produces:

1. **Learning Goals**: Specific, measurable objectives with success criteria
2. **Search Strategy**: Prioritized queries and source types
3. **Synthesized Knowledge**: Organized information by topic with key insights
4. **Concept Relationships**: Map of how concepts connect
5. **Practical Applications**: Use cases and examples
6. **Learning Report**: Comprehensive document with:
   - Actionable takeaways
   - Knowledge gaps identified
   - Credibility assessments
   - Next steps for continued learning

## Examples

### Example 1: Learning a New Framework
```
Learning Objective: "Understand React Server Components"
Current Knowledge: "Familiar with React basics and client-side rendering"
Application Context: "Building a new e-commerce application"
```

### Example 2: Research for Decision Making
```
Learning Objective: "Compare container orchestration options"
Current Knowledge: "Basic Docker experience"
Application Context: "Selecting infrastructure for microservices deployment"
```

## Error Handling

- **Task Failure**: Chain stops and reports the specific error
- **Missing Dependencies**: Clear message showing required context variables
- **Script Failures**: Displays script output for debugging
- **Partial States**: Tasks complete atomically - no partial results

## Related Skills

- `research-and-report` - For generating formal research reports
- `challenge-me` - For testing and validating learned concepts
- `tell-me` - For quick information retrieval without full research workflow
