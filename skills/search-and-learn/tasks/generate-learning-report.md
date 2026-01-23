---
task_id: "generate-learning-report"
task_name: "Generate Learning Report"
dependencies: ["context.timestamp", "context.synthesized_knowledge", "context.practical_applications"]
conditions: []
---

# Generate Learning Report

## Input Context
**Required Context Variables**: 
- `context.timestamp`: Session timestamp for file naming
- `context.learning_objective`: Original learning objective
- `context.learning_goals`: Defined learning goals
- `context.sources_found`: All sources with URLs
- `context.synthesized_knowledge`: Synthesized information
- `context.key_insights`: Key insights discovered
- `context.practical_applications`: Use cases and examples
- `context.understanding_validation`: Success criteria results
- `context.actionable_takeaways`: Next steps and takeaways
- `context.knowledge_gaps`: Identified gaps
**Required Files**: 
- Template: `templates/learning-report-template.md` (if exists)
**Required Tools**: File writing capabilities

## Task Instructions

### Create Structured Learning Report

1. **Determine Report Filename**:
   - Extract topic from learning_objective (sanitize for filename)
   - Format: `search-and-learn-[topic]-[timestamp].md`
   - Example: `search-and-learn-kubernetes-networking-20251120-1948.md`

2. **Determine Report Location**:
   - Directory: `.olaf/work/staging/learning-reports/`
   - Create directory if it doesn't exist

3. **Create Report Content**:
   Structure the report with the following sections:

   ```markdown
   # Learning Report: [learning_objective]
   
   **Generated**: [timestamp]
   **Learning Session**: [date/time]
   
   ---
   
   ## Learning Objective
   [Original learning_objective]
   
   ## Learning Goals Achieved
   [List learning_goals with completion status]
   
   ## Learning Summary
   ### Key Concepts and Insights
   [synthesized_knowledge organized by topic]
   
   ### Key Insights Discovered
   [key_insights list]
   
   ## Source Documentation
   ### Primary Sources
   [High credibility sources with URLs - MANDATORY format: [Title](url)]
   
   ### Supporting Sources
   [Additional sources with URLs]
   
   ### Source Quality Assessment
   [Credibility ratings and notes]
   
   ## Practical Applications
   ### Use Cases
   [practical_applications use cases]
   
   ### Implementation Examples
   [Code snippets, workflows, or procedures]
   
   ## Understanding Validation
   [understanding_validation results against success criteria]
   
   ## Knowledge Gaps
   [knowledge_gaps - areas requiring additional research]
   
   ## Next Steps
   ### Recommended Actions
   [actionable_takeaways]
   
   ### Follow-up Learning
   [Suggestions for deeper or related learning]
   
   ---
   
   **Session Info**:
   - Timestamp: [timestamp]
   - Sources Consulted: [count]
   - Completion: [percentage based on success criteria]
   ```

4. **Write Report File**:
   - Create the learning-reports directory if needed
   - Write the formatted report to the file
   - Preserve all URLs in proper markdown format

5. **Confirm Report Creation**:
   ```
   ✅ Learning report created: [filename]
   Location: .olaf/work/staging/learning-reports/
   ```

## Output Requirements

**State Updates**:
- `context.report_file`: Full path to created report file
- `context.report_created`: true
- `task_status.generate-learning-report`: "completed"

**Files Created**: 
- Learning report markdown file in `.olaf/work/staging/learning-reports/`

**Context Passed to Next Tasks**:
- Report file path available for reference
- Could be used by cleanup task if temporary files were created
