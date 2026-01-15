---
task_id: "generate-deliverables"
task_name: "Generate Final Deliverables"
dependencies: ["session_identifier", "subject_3_words", "timestamp", "trajectory", "citations_list", "recommendations_list", "current_ideas"]
---

# Task: Generate Final Deliverables

## Input Context
**Required Context Variables**: 
- `session_identifier`: Session ID
- `subject_3_words`: 3-word subject identifier
- `timestamp`: Session timestamp
- `trajectory`: Complete trajectory documentation
- `citations_list`: All sources consulted
- `recommendations_list`: All recommendations developed
- `current_ideas`: Final refined ideas
- `subject`: Original subject
- `initial_thoughts`: Original starting thoughts
- `cycle_counter`: Total cycles completed

**Required Files**: 
- Template: `templates/think-tank-think-template.md`
- Template: `templates/think-tank-path-template.md`
- Template: `templates/think-tank-sources-template.md`
- Template: `templates/think-tank-reco-template.md`

**Required Tools**: File system write access

## Task Instructions

### 1. Create Output Directory
Create folder: `.olaf/work/staging/think-tank/<subject_3_words>-<timestamp>/`

### 2. Generate think.md
Load template: `think-tank-think-template.md`
Fill with:
- Session identifier
- Subject
- Final refined ideas
- Key insights summary
- Supporting details
- Source attributions

Save to: `<output_dir>/think.md`

### 3. Generate path.md
Load template: `think-tank-path-template.md`
Fill with:
- Complete trajectory from `trajectory`
- Initial state
- Cycle progression
- Evolution markers
- Milestone highlights
- Research integration points

Save to: `<output_dir>/path.md`

### 4. Generate sources.md
Load template: `think-tank-sources-template.md`
Organize citations from `citations_list` by:
- **Codebase References**:
  - File paths
  - Line numbers
  - Functions/classes
  - Cycle where used
- **Documentation References**:
  - Document names
  - Sections
  - Page numbers
  - Cycle where used
- **Web Resources**:
  - Full URLs
  - Titles
  - Access timestamps
  - Key excerpts
  - Cycle where used
- **Cross-References**:
  - Which sources informed each cycle
  - Which sources informed each insight

Save to: `<output_dir>/sources.md`

### 5. Generate reco.md
Load template: `think-tank-reco-template.md`
Fill with recommendations from `recommendations_list`:
- **Go/No-Go Decision**:
  - Clear recommendation
  - Supporting evidence from cycles
  - Confidence level
- **Alternative Approaches** (if no-go or risky):
  - Specific alternatives to study
  - Why they might be better
  - Resources for exploration
- **Risk Mitigation**:
  - Identified risks
  - Mitigation strategies
  - Success criteria
- **Next Steps**:
  - Prioritized actionable steps
  - Timelines
  - Resource requirements
- **Success Criteria**:
  - Measurable outcomes
  - Validation methods

Save to: `<output_dir>/reco.md`

### 6. Generate Summary Report
Display to user:
```
✅ Session Complete

📊 Session Statistics:
   - Total Cycles: <cycle_counter>
   - Challenges Presented: <count from challenges_list>
   - Insights Generated: <count from insights_list>
   - Sources Consulted: <count from citations_list>
   - Recommendations: <count from recommendations_list>

📁 Files Saved:
   - think.md (Final refined ideas)
   - path.md (Evolution trajectory)
   - sources.md (Comprehensive citations)
   - reco.md (Actionable recommendations)

   Location: <output_dir>

🔍 Next Steps:
   <suggestions based on recommendations>
```

## Output Requirements

**Context Variables Created**:
- `output_directory`: Path to saved files
- `files_saved`: List of saved file paths

**Files Created**:
- `<output_dir>/think.md`
- `<output_dir>/path.md`
- `<output_dir>/sources.md`
- `<output_dir>/reco.md`
