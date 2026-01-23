---
task_id: "collect-parameters"
task_name: "Collect Session Parameters"
dependencies: ["timestamp"]
---

# Task: Collect Session Parameters

## Input Context
**Required Context Variables**: 
- `timestamp`: Current session timestamp

**Required Files**: None
**Required Tools**: None

## Task Instructions

You MUST request these parameters if not provided by the user:

### Required Parameters
1. **subject**: The topic or subject area for ideation
   - Prompt: "What subject or topic would you like to explore?"
   - Validation: Non-empty string

2. **initial_thoughts**: User's initial ideas or description
   - Prompt: "What are your initial thoughts or ideas on this subject?"
   - Validation: Non-empty string

### Optional Parameters
3. **codebase_path**: Path to local repository/codebase for analysis
   - Prompt: "Do you have a codebase to analyze? (provide path or leave empty)"
   - Default: empty

4. **documentation_path**: Path to folder containing relevant documentation
   - Prompt: "Do you have documentation to review? (provide path or leave empty)"
   - Default: empty

5. **web_search_urls**: Specific URLs for web research
   - Prompt: "Any specific URLs to research? (comma-separated or leave empty for general search)"
   - Default: empty

6. **research_depth**: Level of web research to conduct
   - Prompt: "Research depth? (shallow/moderate/deep)"
   - Default: "moderate"
   - Validation: Must be one of: shallow, moderate, deep

7. **challenge_intensity**: How aggressively to challenge ideas
   - Prompt: "Challenge intensity? (gentle/moderate/rigorous)"
   - Default: "moderate"
   - Validation: Must be one of: gentle, moderate, rigorous

## Output Requirements

**Context Variables Created**:
- `subject`: The ideation topic
- `initial_thoughts`: User's starting ideas
- `codebase_path`: Path to codebase (or empty)
- `documentation_path`: Path to documentation (or empty)
- `web_search_urls`: URLs for research (or empty)
- `research_depth`: Research depth level
- `challenge_intensity`: Challenge intensity level

**Files Created**: None
