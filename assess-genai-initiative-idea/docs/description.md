# assess-genai-initiative-idea

## Overview

The `assess-genai-initiative-idea` skill conducts comprehensive assessments of GenAI solution requests through a structured questionnaire and research process. It helps organizations evaluate whether a proposed GenAI initiative is viable, valuable, and well-defined before committing resources to implementation.

## Purpose

This skill enables documentation maintainers and stakeholders to systematically evaluate GenAI proposals by:
- Collecting structured information about the proposed initiative
- Conducting research on similar implementations and alternatives
- Identifying potential challenges and risks
- Providing actionable recommendations based on thorough analysis

## Key Features

- **Structured Questionnaire**: 10 comprehensive questions covering problem analysis, user impact, and business constraints
- **Quality Review**: Automatic analysis of responses for ambiguities, gaps, and generic information
- **Web Research**: Searches across GitHub, Medium, Reddit, industry publications, and academic papers
- **Alternative Analysis**: Challenges proposals with alternative approaches and requires justification
- **Phased Workflow**: Clear progression through questionnaire, review, research, and recommendation phases

## Usage

Invoke this skill when you need to evaluate a GenAI initiative idea before implementation.

### Parameters

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `assessment_scope` | string | Yes | Specific GenAI use case or problem domain |
| `stakeholder_context` | string | No | Primary users and organizational context |
| `timeline_constraints` | string | No | Expected implementation timeline |

### Example Invocation

```
Skill: assess-genai-initiative-idea
Parameters:
  - assessment_scope: "Automated customer support chatbot for e-commerce"
  - stakeholder_context: "Customer service team, 50+ agents"
  - timeline_constraints: "Q2 2026 launch"
```

## Process Flow

```
┌─────────────────────────────────────────────────────────────────┐
│                    VALIDATION PHASE                              │
│  • Confirm user readiness for questionnaire                      │
│  • Validate assessment scope is clearly defined                  │
│  • Check web search capabilities                                 │
└─────────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────────┐
│                  QUESTIONNAIRE PHASE                             │
│  • Core Problem Analysis (Q1-Q4)                                 │
│  • User and Impact Analysis (Q5-Q8)                              │
│  • Business and Technical Constraints (Q9-Q10)                   │
└─────────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────────┐
│                   DATA REVIEW PHASE                              │
│  • Generate initiative name (3 words max)                        │
│  • Create data file with structured responses                    │
│  • Present for user review and sign-off                          │
│  • Analyze for ambiguities and gaps                              │
│  • Rate issues: Critical, Important, Suggestion                  │
└─────────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────────┐
│                    RESEARCH PHASE                                │
│  • Search 5+ sources across platforms                            │
│  • Document alternatives and challenges                          │
│  • Identify implementation challenges                            │
│  • Challenge proposal with alternatives                          │
│  • Request user justification for rejections                     │
└─────────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────────┐
│                  RECOMMENDATION PHASE                            │
│  • Deliver comprehensive assessment document                     │
│  • Provide actionable next steps                                 │
└─────────────────────────────────────────────────────────────────┘
```

## Output

The skill generates a comprehensive assessment document at `[staging_dir]/genai-assessments/[initiative_name]-data.md` containing:

- **Initiative Overview**: Summary of the proposed GenAI solution
- **Questionnaire Responses**: All 10 structured responses with quality analysis
- **Alternatives and Challenges**: Research findings from multiple platforms
- **Implementation Challenges**: Technical, organizational, and ethical considerations
- **Conclusion and Recommendations**: Actionable next steps for stakeholders

## Examples

### Example 1: Customer Support Chatbot Assessment

**Input:**
```
assessment_scope: "AI-powered customer support chatbot"
stakeholder_context: "E-commerce company, 100 support tickets/day"
```

**Output:** Assessment document covering problem validation, similar implementations found on GitHub, identified challenges around training data quality, and recommendation to start with FAQ automation before full chatbot deployment.

### Example 2: Code Review Assistant Assessment

**Input:**
```
assessment_scope: "GenAI code review assistant for development team"
timeline_constraints: "3 months"
```

**Output:** Assessment document identifying existing solutions (GitHub Copilot, CodeRabbit), technical integration challenges, and recommendation to pilot with specific repository before organization-wide rollout.

## Error Handling

| Scenario | Handling |
|----------|----------|
| Incomplete questionnaire responses | Request specific missing information with guidance |
| Critical quality issues | Stop process and request clarification before research |
| Web search failures | Provide alternative research methods and manual guidance |
| User rejection of alternatives | Document justification and proceed with original proposal |
| Insufficient research sources | Expand search criteria until minimum 5 sources met |
| Unclear initiative scope | Request refined problem definition |

## Related Skills

- `research-and-report` - For general research tasks
- `challenge-me` - For ideation and brainstorming sessions
- `create-decision-record` - For documenting final decisions
