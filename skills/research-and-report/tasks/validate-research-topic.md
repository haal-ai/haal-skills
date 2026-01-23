---
task_id: "validate-research-topic"
task_name: "Validate Research Topic"
dependencies: []
---

# Task: Validate Research Topic

## Input Context
**Required Context Variables**: 
- `context.research_topic`: String - Specific topic or question to research
- `context.scope_boundaries`: String - What is included and excluded from research (optional)
- `context.expected_outcomes`: String - Expected deliverables and target audience (optional)

**Required Files**: None
**Required Tools**: None

## Task Instructions

### Analyze and Validate Research Request

1. **Parse Research Topic**:
   - Identify main subject area and key concepts
   - Extract implicit questions or goals
   - Determine research domain (technical, market, academic, etc.)
   - Note any ambiguities requiring clarification

2. **Define Scope Statement**:
   - If `scope_boundaries` provided: validate and refine
   - If not provided: infer reasonable boundaries based on topic
   - Explicitly state what IS included in research
   - Explicitly state what is NOT included in research
   - Identify any edge cases or gray areas

3. **Formulate Key Research Questions**:
   - Break down topic into 3-7 specific questions to answer
   - Ensure questions are:
     - Specific and answerable
     - Relevant to stated or inferred goals
     - Ordered logically (foundational to advanced)
   - Example format:
     - "What is [concept] and why is it important?"
     - "How does [technology] compare to alternatives?"
     - "What are current trends in [domain]?"

4. **Identify Information Needs**:
   - Determine what types of sources are needed:
     - Current web sources (vendor sites, news, forums)
     - Academic or technical documentation
     - Market research or industry reports
     - Comparative analysis or benchmarks
   - Note priority: current vs. historical information
   - Flag areas requiring web search validation

5. **Check for Missing Information**:
   - Review provided context variables
   - If critical information missing, prepare clarification questions
   - Suggest reasonable defaults if user input unavailable

6. **Display Validation Summary**:
   ```
   Research Topic Validation
   ============================
   Topic: [validated topic statement]
   
   Scope:
   - Included: [list]
   - Excluded: [list]
   
   Key Research Questions:
   1. [question 1]
   2. [question 2]
   ...
   
   Information Needs:
   - [source type 1]: [priority]
   - [source type 2]: [priority]
   ```

## Output Requirements

**Context Variables Created**:
- `context.validated_topic`: String - Clear, validated topic statement
- `context.scope_statement`: Object - {included: [list], excluded: [list]}
- `context.key_questions`: Array - List of specific research questions
- `context.information_needs`: Object - {source_types: [list], priority_areas: [list]}
- `context.clarification_needed`: Boolean - True if user input required
- `context.clarification_questions`: Array - Questions for user (if needed)

**Files Created**: None

**Context Passed to Next Tasks**:
- Validated topic and scope for research planning
- Key questions to structure chapter outline
- Information needs to guide source strategy
