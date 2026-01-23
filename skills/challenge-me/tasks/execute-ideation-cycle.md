---
task_id: "execute-ideation-cycle"
task_name: "Execute Ideation Cycle"
dependencies: ["cycle_counter", "initial_thoughts", "challenge_intensity", "research_depth", "codebase_index", "documentation_index", "web_search_strategy"]
---

# Task: Execute Ideation Cycle

## Input Context
**Required Context Variables**: 
- `cycle_counter`: Current cycle number
- `initial_thoughts`: Current state of ideas
- `challenge_intensity`: gentle/moderate/rigorous
- `research_depth`: shallow/moderate/deep
- `codebase_index`: Codebase structure (may be empty)
- `documentation_index`: Documentation index (may be empty)
- `web_search_strategy`: Web search approach
- `challenges_list`: Running list of challenges
- `insights_list`: Running list of insights
- `citations_list`: Running list of sources
- `recommendations_list`: Running list of recommendations

**Required Files**: Access to codebase and documentation paths if provided
**Required Tools**: Web search, file reading

## Task Instructions

### 1. Increment Cycle Counter
Increment `cycle_counter` by 1
Display: `🔄 Cycle <cycle_counter>`

### 2. Analysis Phase
Analyze current ideas for:
- Core strengths
- Underlying assumptions
- Potential weaknesses
- Gaps in reasoning

### 3. Codebase Analysis (if available)
If `codebase_index` is not empty:
- Search relevant code patterns
- Identify existing implementations
- Find related architectural decisions
- Document file paths and code sections
- Add to `citations_list`

### 4. Documentation Review (if available)
If `documentation_index` is not empty:
- Search for relevant concepts
- Identify constraints and requirements
- Find best practices and guidelines
- Document specific sections
- Add to `citations_list`

### 5. Challenge Phase
Present 2-3 specific challenges based on:
- Analysis findings
- Codebase evidence
- Documentation constraints
- Research insights

**MANDATORY INTERACTIVE FORMAT**:
- Use numbered lists (1, 2, 3, 4) for choice-based questions and polls
- Use lettered lists (A, B, C, D) for clarification and vision questions
- Present web feedback and ask for user's perspective
- Invite user to explain reasoning
- NEVER ask the same question twice

Add challenges to `challenges_list`

### 6. Research Phase
Conduct web research based on `research_depth`:
- **shallow**: Quick fact-checking, 1-2 sources
- **moderate**: Targeted research, 3-5 sources
- **deep**: Comprehensive research, 6+ sources

Query web resources (specific URLs or general search)
Document all sources with:
- Full URLs
- Access timestamps
- Key excerpts
- Relevance to topic

Add to `citations_list`

### 7. Insight Generation
Provide 2-3 alternative perspectives informed by:
- Codebase analysis
- Documentation review
- Web research findings
- Challenge responses

Add insights to `insights_list`

### 8. Synthesis Phase
Help user refine thinking:
- Build on previous responses
- Connect new evidence to ideas
- Identify patterns and themes
- Suggest refinements

### 9. Recommendations Development
Based on cycle exchanges, update `recommendations_list` with:
- Emerging go/no-go indicators
- Alternative approaches discovered
- Risk assessments
- Resource requirements
- Next steps identified

### 10. Wait for User Response
Prompt user to:
- Respond to challenges
- Share thoughts on insights
- Continue to next cycle
- Type "stop" or "save" to end

## Output Requirements

**Context Variables Updated**:
- `cycle_counter`: Incremented
- `challenges_list`: Appended with new challenges
- `insights_list`: Appended with new insights
- `citations_list`: Appended with new sources
- `recommendations_list`: Updated with emerging recommendations
- `current_ideas`: Updated based on user response

**Files Created**: None

## Notes
This task is meant to be executed in a loop. The master coordinator will repeat this task until user termination.
