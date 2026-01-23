---
task_id: "execute-systematic-search"
task_name: "Execute Systematic Search"
dependencies: ["context.search_queries", "context.information_sources"]
conditions: []
---

# Execute Systematic Search

## Input Context
**Required Context Variables**: 
- `context.search_queries`: Formulated search queries
- `context.information_sources`: Prioritized source types
- `context.search_sequence`: Ordered search plan
**Required Files**: None
**Required Tools**: Web search capabilities

## Task Instructions

### Search and Document Findings

1. **Execute Searches According to Strategy**:
   - Follow the search_sequence order
   - For each query, search across prioritized information sources
   - Collect relevant results systematically

2. **Document Sources with MANDATORY URLs**:
   - **CRITICAL**: Every source MUST include full URL
   - Format: `[Source Title](full-url)`
   - Reject any generic references without URLs
   - Record source metadata:
     * Title
     * Author/Organization
     * Publication date (if available)
     * Source type (documentation, blog, paper, etc.)
     * Full URL (REQUIRED)

3. **Track Information Quality**:
   - Rate source credibility (1-5 scale)
   - Note relevance to learning goals (1-5 scale)
   - Flag particularly valuable sources
   - Identify gaps or missing information

4. **Collect Raw Information**:
   - Extract key points from each source
   - Preserve important quotes or code examples
   - Note connections between sources
   - Track different perspectives on same topic

5. **Create Search Results Summary**:
   ```markdown
   **Search Execution Results**:
   
   Sources Found: [count]
   
   High-Quality Sources (4-5/5):
   - [Title](url) - [relevance notes]
   
   Supporting Sources (3+/5):
   - [Title](url) - [relevance notes]
   
   Information Gaps Identified:
   - [Gap 1]
   ```

## Output Requirements

**State Updates**:
- `context.sources_found`: Array of source objects with URLs and metadata
  ```json
  [
    {
      "title": "Source Title",
      "url": "https://...",
      "author": "Author Name",
      "credibility": 5,
      "relevance": 4,
      "source_type": "documentation"
    }
  ]
  ```
- `context.raw_information`: Extracted key points and quotes
- `context.information_gaps`: Identified missing information
- `task_status.execute-systematic-search`: "completed"

**Files Created**: None

**Context Passed to Next Tasks**:
- Sources and raw information will be synthesized in next task
