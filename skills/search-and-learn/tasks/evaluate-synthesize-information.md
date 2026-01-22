---
task_id: "evaluate-synthesize-information"
task_name: "Evaluate and Synthesize Information"
dependencies: ["context.sources_found", "context.raw_information"]
conditions: []
---

# Evaluate and Synthesize Information

## Input Context
**Required Context Variables**: 
- `context.sources_found`: Array of sources with URLs and metadata
- `context.raw_information`: Extracted key points and quotes
- `context.learning_goals`: Original learning goals
**Required Files**: None
**Required Tools**: None

## Task Instructions

### Assess, Synthesize, and Connect Knowledge

1. **Assess Source Credibility and Reliability**:
   - Cross-reference information across multiple sources
   - Identify consensus viewpoints vs. conflicting information
   - Evaluate author expertise and source authority
   - Flag any outdated or questionable information
   - Prioritize most credible sources for synthesis

2. **Synthesize Information from Multiple Sources**:
   - Organize information by learning goal or topic
   - Combine complementary information from different sources
   - Resolve conflicts or contradictions (note different perspectives)
   - Create unified understanding of each topic
   - Extract key concepts, principles, and facts

3. **Create Connections Between Concepts**:
   - Identify relationships between different concepts
   - Map dependencies (concept A requires understanding concept B)
   - Find patterns or common themes across sources
   - Connect new knowledge to user's existing knowledge (from current_knowledge)
   - Build mental model or framework for the topic

4. **Distill Key Insights**:
   - Extract most important takeaways
   - Identify actionable principles or guidelines
   - Note surprising or counter-intuitive findings
   - Highlight practical implications

5. **Create Synthesis Summary**:
   ```markdown
   **Knowledge Synthesis**:
   
   Core Concepts Learned:
   - [Concept 1]: [explanation]
   - [Concept 2]: [explanation]
   
   Key Insights:
   - [Insight 1]
   - [Insight 2]
   
   Concept Relationships:
   - [Concept A] → [Concept B]
   
   Credibility Assessment:
   - High confidence: [topics]
   - Need verification: [topics]
   ```

## Output Requirements

**State Updates**:
- `context.synthesized_knowledge`: Organized knowledge by topic/goal
- `context.key_insights`: Array of key insights and takeaways
- `context.concept_relationships`: Map of concept connections
- `context.credibility_assessment`: Confidence levels for different topics
- `task_status.evaluate-synthesize-information`: "completed"

**Files Created**: None

**Context Passed to Next Tasks**:
- Synthesized knowledge will be applied and tested in next task
