---
task_id: "develop-search-strategy"
task_name: "Develop Search Strategy"
dependencies: ["context.learning_goals"]
conditions: []
---

# Develop Search Strategy

## Input Context
**Required Context Variables**: 
- `context.learning_goals`: Specific learning goals
- `context.current_knowledge`: User's knowledge baseline
- `context.scope_boundaries`: What's in/out of scope
**Required Files**: None
**Required Tools**: None

## Task Instructions

### Formulate Queries and Identify Sources

1. **Formulate Precise Search Queries**:
   - Create targeted search queries for each learning goal
   - Include technical terms, keywords, and concepts
   - Consider user's knowledge level (beginner vs advanced terms)
   - Generate variations to capture different perspectives

2. **Identify Authoritative Information Sources**:
   - Determine most appropriate source types:
     * Official documentation
     * Academic papers/journals
     * Technical blogs (reputable authors)
     * Stack Overflow / technical forums
     * GitHub repositories (for code examples)
     * Books or published guides
   - Prioritize sources based on topic and user needs

3. **Plan Search Sequence**:
   - Order searches from foundational to advanced
   - Start with overview/conceptual sources
   - Progress to detailed/technical sources
   - Include practical examples and use cases

4. **Create Search Strategy Summary**:
   ```markdown
   **Search Strategy**:
   
   Queries to Execute:
   1. [Query 1] - Target: [source types]
   2. [Query 2] - Target: [source types]
   
   Prioritized Sources:
   - [Source type 1] - for [purpose]
   - [Source type 2] - for [purpose]
   
   Search Sequence:
   1. [Foundational searches]
   2. [Detailed searches]
   3. [Practical examples]
   ```

## Output Requirements

**State Updates**:
- `context.search_queries`: Array of formulated search queries
- `context.information_sources`: Array of prioritized source types
- `context.search_sequence`: Ordered search plan
- `task_status.develop-search-strategy`: "completed"

**Files Created**: None

**Context Passed to Next Tasks**:
- Search queries and sources will guide the systematic search execution
