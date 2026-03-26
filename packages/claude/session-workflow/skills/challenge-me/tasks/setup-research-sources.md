---
task_id: "setup-research-sources"
task_name: "Setup Multi-Source Research"
dependencies: ["codebase_path", "documentation_path", "web_search_urls"]
---

# Task: Setup Multi-Source Research

## Input Context
**Required Context Variables**: 
- `codebase_path`: Path to codebase (may be empty)
- `documentation_path`: Path to documentation (may be empty)
- `web_search_urls`: URLs for research (may be empty)

**Required Files**: Paths specified in context variables
**Required Tools**: File system access, web search capabilities

## Task Instructions

### 1. Scan Codebase (if provided)
If `codebase_path` is not empty:
- Verify path exists and is accessible
- Scan directory structure
- Identify key files, folders, and patterns
- Create codebase index with:
  - File paths
  - Directory structure
  - Key technologies detected
- Store in `codebase_index`

### 2. Index Documentation (if provided)
If `documentation_path` is not empty:
- Verify path exists and is accessible
- List all documentation files
- Identify document types (markdown, text, etc.)
- Create documentation index with:
  - Document names
  - Sections/headings detected
  - Key topics identified
- Store in `documentation_index`

### 3. Prepare Web Search Strategy
If `web_search_urls` is not empty:
- Parse comma-separated URLs
- Validate URL formats
- Store in `web_urls_list`
Else:
- Set `web_search_strategy` to "general"

### 4. Report Setup Status
Display to user:
```
🔍 Research Sources Setup Complete
   Codebase: <status>
   Documentation: <status>
   Web Search: <strategy>
```

## Output Requirements

**Context Variables Created**:
- `codebase_index`: Structure of codebase (or empty)
- `documentation_index`: Index of documentation (or empty)
- `web_urls_list`: List of URLs (or empty)
- `web_search_strategy`: "specific" or "general"
- `research_sources_ready`: Boolean flag (true)

**Files Created**: None
