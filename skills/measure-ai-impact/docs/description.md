# Measure AI Impact - Skill Description

## Overview

The **measure-ai-impact** skill provides data-driven insights into how AI-assisted development affects your codebase quality and team productivity. It combines two powerful analysis approaches:

1. **File-Level AI Detection**: Uses Halstead complexity metrics and Maintainability Index changes to detect AI-generated code improvements
2. **Quarterly Trend Analysis**: Tracks team productivity patterns over time to measure the impact of AI adoption

## Why This Matters

As teams adopt AI coding assistants (like GitHub Copilot), understanding the actual impact on code quality and developer productivity becomes critical:

- **Validate ROI**: Measure tangible improvements from AI tool investments
- **Identify Patterns**: Understand which files/areas benefit most from AI assistance
- **Track Progress**: Monitor productivity trends as AI adoption increases
- **Optimize Usage**: Learn which types of tasks AI handles best

## Key Capabilities

### 1. AI Signature Detection

Analyzes code metrics before and after changes to identify AI-assisted improvements:

- **Maintainability Index (MI)** jumps >20 points
- **Cyclomatic Complexity** reductions
- **Halstead Difficulty** drops >30%
- **Effort** reductions >50%

**Example Use Case**: "Did we use AI to refactor our authentication module?"

### 2. Quarterly Productivity Snapshots

Generates time-series data showing team productivity evolution:

- Commits per day/week
- Code churn (LOC changed)
- Contributor activity patterns
- Session gaps and work patterns

**Example Use Case**: "How has our productivity changed since adopting Copilot in Q1 2025?"

### 3. Baseline Comparison

Creates historical snapshots for accurate before/after comparisons:

- Snapshot repository state at any point in time
- Compare current metrics against historical baselines
- Track long-term quality trends

**Example Use Case**: "Create a baseline snapshot before we start using AI tools"

## How It Works

### Detection Methodology

The skill uses **Halstead Complexity Metrics**, a well-established software science approach that measures:

- **Program Vocabulary**: Unique operators and operands
- **Program Length**: Total operators and operands
- **Difficulty**: How hard is the code to understand?
- **Effort**: Mental effort required to comprehend/modify code

When AI refactors code, these metrics typically show dramatic improvements:
- Lower difficulty → Simpler logic
- Reduced effort → Easier maintenance
- Higher MI → Better overall quality

### Productivity Analysis

The skill analyzes Git commit history to extract:

- **Temporal Patterns**: When are developers most active?
- **Velocity Trends**: Are commits increasing/decreasing?
- **Team Dynamics**: How does contributor count affect output?
- **Code Efficiency**: LOC per commit trends

By comparing quarters, you can correlate AI tool adoption with productivity changes.

## Analysis Modes

### Mode: file-analysis

**Purpose**: Detect AI signatures in specific files

**When to Use**:
- After refactoring specific modules
- Validating AI-assisted code improvements
- Identifying which files benefited from AI

**Outputs**:
- AI likelihood scores per file
- Detected improvement patterns
- Before/after metrics comparison
- Confidence ratings

### Mode: quarterly-trends

**Purpose**: Track team-wide productivity over time

**When to Use**:
- Quarterly reviews and retrospectives
- Measuring AI adoption impact
- Identifying productivity trends
- Team performance analysis

**Outputs**:
- Quarterly comparison dashboard
- Productivity trend graphs
- Contributor analysis
- AI impact estimation

### Mode: snapshot

**Purpose**: Create baseline for future comparison

**When to Use**:
- Before starting AI tool adoption
- Quarterly checkpoints
- Major refactoring milestones
- Release benchmarks

**Outputs**:
- JSON snapshot file with all metrics
- Summary statistics
- Timestamp and Git reference

## Integration with OLAF Ecosystem

This skill complements other OLAF skills:

- **onboard-me**: Use measure-ai-impact after onboarding to track quality improvements
- **review-code**: Combine with AI detection to validate review suggestions
- **report-my-daily**: Include AI impact metrics in daily reports

## Requirements

- **Python 3.10+**: Required for analyzer scripts
- **Git Repository**: Must be run in a Git-tracked repository
- **Radon Library**: Optional but recommended for full Halstead metrics (install: `pip install radon`)
- **Git History**: At least 6 months of commit history recommended for accurate baselines

## Limitations

### What This Skill CAN Do:

✅ Detect statistical patterns consistent with AI-generated improvements
✅ Track productivity trends over time
✅ Compare code quality before/after changes
✅ Estimate AI impact based on metrics correlation

### What This Skill CANNOT Do:

❌ Definitively prove code was written by AI (no 100% certainty)
❌ Detect AI usage in non-Python files (limited language support)
❌ Attribute specific commits to AI vs human
❌ Measure developer satisfaction or code correctness

### Accuracy Considerations:

- **False Positives**: Manual refactoring can also improve metrics
- **False Negatives**: Not all AI assistance produces detectable patterns
- **Baseline Quality**: Requires sufficient historical data
- **Language Support**: Best results with Python; partial support for other languages

## Example Workflows

### Workflow 1: Validate AI-Assisted Refactoring

1. **Before Refactoring**: Create baseline snapshot
   ```
   @olaf measure-ai-impact mode:snapshot name:"pre-refactor"
   ```

2. **Perform Refactoring**: Use AI to improve code quality

3. **After Refactoring**: Analyze specific files
   ```
   @olaf measure-ai-impact mode:file-analysis files:["src/auth.py", "src/validator.py"]
   ```

4. **Review Report**: Check AI likelihood scores and metric improvements

### Workflow 2: Quarterly Team Review

1. **Generate Quarterly Snapshots**:
   ```
   @olaf measure-ai-impact mode:quarterly-trends since:"2024-01-01"
   ```

2. **Compare Quarters**:
   ```
   @olaf measure-ai-impact mode:quarterly-trends compare:["2024-Q4", "2025-Q1"]
   ```

3. **Review Trends**: Analyze productivity changes and AI correlation

4. **Adjust Strategy**: Optimize AI tool usage based on findings

### Workflow 3: Repository Health Check

1. **Create Baseline**: Snapshot current state
2. **Quarterly Analysis**: Run trends every 3 months
3. **File Targeting**: Identify low-MI files for AI assistance
4. **Validate Impact**: Re-run file-analysis after improvements

## Output Locations

All reports are saved to `olaf-data/ai-impact/`:

- **File Analysis Reports**: `ai-impact-file-analysis-[YYYYMMDD-HHmm].md`
- **Quarterly Trends**: `ai-impact-quarterly-trends-[YYYYMMDD-HHmm].md`
- **Snapshots**: `snapshots/snapshot-{name}.json`

## Support

For issues, questions, or feature requests:
- See `tutorial.md` for step-by-step examples
- Check analyzer tool documentation in `skills/onboard/tools/commons/project-onboarding/`
- Review OLAF core documentation

---

**Skill Version**: 1.0.0
**Last Updated**: 2025-01-24
**Maintainer**: OLAF Framework
