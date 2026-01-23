---
task_id: "load-practices-for-diff"
task_name: "Load repository practices for changed files"
dependencies: ["detect-file-languages", "collect-git-diff"]
---

# Task: Load Repository Practices for Changed Files

## Input Context
- Required Context Variables:
  - diff_file_list: array of changed file paths
  - files_by_language: object mapping language -> file list
- Required Files:
  - .olaf/data/practices/practices/good-bad/*.md (if present)
- Required Tools:
  - file_search, read_file

## Task Instructions
1. Enumerate changed files from `diff_file_list`.
2. Determine languages in scope using `files_by_language`.
3. Search `.olaf/data/practices/practices/good-bad/` for practice docs.
4. Filter practices by:
   - Matching `language` (if present in YAML preamble or title)
   - Heuristics on filename/id tokens that match file path segments
5. Build a concise ordered list to apply first in analysis:
   - Repo Practices (good/bad) → Team/Current Standards → Universal Standards
6. Produce a structured summary with:
   - matching_practices: [ { id, title, path } ]
   - rationale: short note per match
   - precedence: "repo-practices-first"

## Output Requirements
- Context Variables Created:
  - applicable_practices: object with keys { matching_practices, rationale, precedence }
- Files Created: none
