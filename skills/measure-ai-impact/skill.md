---
name: measure-ai-impact
description: Measure AI's impact on code quality and team productivity through file analysis and quarterly metrics
license: Apache-2.0
metadata:
  olaf_tags: [ai, impact, metrics, productivity, quality, halstead, maintainability]
---

# Measure AI Impact

## Description
Measure the impact of AI-assisted development on code quality and team productivity. Supports both targeted file analysis and repository-wide quarterly trend analysis.

## Use Cases

### 1. **File-Level AI Detection**
Detect if specific files were improved using AI by analyzing quality metrics changes (Halstead, Maintainability Index).

### 2. **Quarterly Productivity Analysis**
Track team productivity and code quality trends across quarters to measure AI adoption impact.

### 3. **Before/After Comparison**
Compare code quality metrics before and after AI-assisted refactoring.

## Input Parameters

You MUST request these parameters if not provided:

**Analysis Mode** (REQUIRED):
- **mode**: string - Analysis type: "file-analysis", "quarterly-trends", or "snapshot"

**For file-analysis mode**:
- **file_paths**: array[string] - Specific files to analyze for AI signatures (REQUIRED)
- **baseline_date**: string - Git commit hash or date for baseline comparison (OPTIONAL - defaults to 6 months ago)

**For quarterly-trends mode**:
- **since_date**: string - Start date for analysis (format: YYYY-MM-DD, default: 2024-01-01)
- **compare_quarters**: array[string] - Specific quarters to compare (e.g., ["2024-Q4", "2025-Q1"]) (OPTIONAL)

**For snapshot mode**:
- **snapshot_name**: string - Name for the snapshot (e.g., "2025-Q1", "baseline-before-ai") (OPTIONAL - auto-generates)
- **include_halstead**: boolean - Include Halstead metrics (slower but more detailed) (default: true)

**Common Parameters**:
- **repository_path**: string - Path to repository (default: current workspace)
- **output_location**: string - Where to save the report (default: olaf-data/ai-impact/)

## User Interaction

You MUST follow these interaction guidelines:
- Execute analysis directly without requiring approval
- Provide clear progress updates during metric collection
- Present findings with actionable insights
- Offer to create baseline snapshots when missing historical data

## Process

### 1. Validation Phase
You WILL verify all requirements:
- Confirm repository path exists and is a valid Git repository
- Validate mode selection and required parameters
- Check for Python tools availability
- Verify write access to output location

### 2. Mode-Specific Execution

#### Mode: file-analysis
**Purpose**: Detect AI signatures in specific files

**Steps**:
1. Collect baseline metrics from Git history or specified commit
2. Collect current metrics from working directory
3. Run AI signature detection using `ai_impact_analyzer.py`
4. Generate AI likelihood scores and indicators
5. Create detailed comparison report

**Output**: 
- AI detection report per file
- Confidence scores (0.0-1.0)
- Detected patterns (MI_JUMP, DIFFICULTY_DROP, etc.)
- Before/after metrics comparison

#### Mode: quarterly-trends
**Purpose**: Analyze team productivity trends across quarters

**Steps**:
1. Generate quarterly snapshots using `git_productivity_analyzer.py`
2. Calculate productivity metrics per quarter:
   - Commits/day, commits/week
   - Code churn (additions, deletions)
   - LOC per commit
   - Contributor patterns
3. Compare quarters to identify trends
4. Generate trend visualization report

**Output**:
- Quarterly productivity dashboard
- Trend analysis (improving/declining)
- Contributor churn analysis
- Session patterns

#### Mode: snapshot
**Purpose**: Create baseline snapshot for future comparison

**Steps**:
1. Determine snapshot name (quarter or custom)
2. Run comprehensive metrics collection
3. Save snapshot JSON with timestamp
4. Display snapshot summary

**Output**:
- Snapshot file: `snapshot-{name}.json`
- Summary of captured metrics

### 3. Report Generation

You WILL generate a comprehensive report using the template:
- `templates/ai-impact-report-template.md` for file-analysis
- `templates/quarterly-trends-report-template.md` for quarterly-trends
- `templates/snapshot-summary-template.md` for snapshot

### 4. Tool Invocation

**For file-analysis**:
```bash
python skills/measure-ai-impact/tools/ai_impact_analyzer.py \
  snapshot --name baseline --months 6
python skills/measure-ai-impact/tools/ai_impact_analyzer.py \
  compare baseline {latest}
```

**For quarterly-trends**:
```bash
python skills/measure-ai-impact/tools/git_productivity_analyzer.py \
  snapshots --since {since_date}
python skills/measure-ai-impact/tools/git_productivity_analyzer.py \
  compare {quarter1} {quarter2}
```

**For snapshot**:
```bash
python skills/measure-ai-impact/tools/ai_impact_analyzer.py \
  snapshot --name {snapshot_name} [--no-halstead]
```

## Output Specifications

**Primary Deliverable**: Comprehensive AI impact report saved as:
- File analysis: `[output_location]/ai-impact-file-analysis-[YYYYMMDD-HHmm].md`
- Quarterly trends: `[output_location]/ai-impact-quarterly-trends-[YYYYMMDD-HHmm].md`
- Snapshot: `[output_location]/snapshots/snapshot-{name}.json`

**Report Structure** (file-analysis):
```markdown
# AI Impact Analysis - File Level

## Executive Summary
- Files analyzed: N
- AI signatures detected: N (percentage)
- Overall confidence: High/Medium/Low

## Per-File Analysis
### File: path/to/file.py
- **AI Likelihood**: 0.85 (High)
- **Indicators**: MI_JUMP_SIGNIFICANT, DIFFICULTY_DROP_MAJOR
- **Metrics Change**:
  - Maintainability Index: 45 → 78 (+33)
  - Difficulty: 25 → 12 (-52%)
  - Effort: 15000 → 5000 (-67%)

## Recommendations
- Files likely AI-improved
- Suggested next targets for AI assistance
```

**Report Structure** (quarterly-trends):
```markdown
# AI Impact Analysis - Quarterly Trends

## Quarter Comparison: 2024-Q4 vs 2025-Q1

### Productivity Metrics
- Commits: 150 → 200 (+33%)
- Code churn: 12K LOC → 18K LOC (+50%)
- Commits/day: 2.3 → 3.1 (+35%)

### Quality Indicators
- Average commit size: 80 LOC → 90 LOC
- Contributors: 5 → 6
- Active days: 65 → 70

## Trend Analysis
- Productivity: ↗ Improving
- Code velocity: ↗ Increasing
- Team growth: Stable

## AI Adoption Impact
Based on productivity increase and commit patterns, estimated AI impact: **Moderate to High**
```

## Error Handling

You MUST handle these scenarios:
- **Missing Git repository**: Prompt user for valid repo path
- **No baseline data**: Offer to create baseline snapshot first
- **Halstead unavailable**: Warn user and proceed with limited metrics
- **Invalid quarter format**: Suggest correct format (YYYY-QN)
- **Tool execution failure**: Display stderr and suggest fixes

## Example Invocations

### Detect AI in specific files
```
User: "Did we use AI to improve auth.py and validator.py?"
Mode: file-analysis
Files: ["src/auth.py", "src/validator.py"]
```

### Quarterly productivity trends
```
User: "How has our productivity changed since we started using AI in Q1 2025?"
Mode: quarterly-trends
Since: 2024-01-01
Compare: ["2024-Q4", "2025-Q1"]
```

### Create baseline snapshot
```
User: "Create a baseline snapshot before we start using AI"
Mode: snapshot
Name: baseline-pre-ai
```

## Success Criteria

- ✅ Report generated with actionable insights
- ✅ AI likelihood scores calculated (file-analysis)
- ✅ Trend analysis completed (quarterly-trends)
- ✅ Snapshot saved successfully (snapshot mode)
- ✅ User understands AI impact on their codebase

---

**Related Skills**: onboard-me, review-code, report-my-daily
**Tools Used**: ai_impact_analyzer.py, git_productivity_analyzer.py
