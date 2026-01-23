# Measure AI Impact - Tutorial

This tutorial walks you through practical examples of using the **measure-ai-impact** skill to analyze AI's impact on your codebase.

---

## Prerequisites

Before starting, ensure:

✅ You're in a Git repository
✅ Python 3.10+ is installed
✅ You have at least 6 months of commit history (recommended)
✅ Radon library is installed (optional): `pip install radon`

---

## Tutorial 1: Detect AI Usage in Specific Files

### Scenario
You used GitHub Copilot to refactor `src/auth.py` and `src/validator.py` last week. You want to confirm the AI actually improved code quality.

### Steps

#### 1. Invoke the Skill

```
@olaf measure-ai-impact mode:file-analysis files:["src/auth.py", "src/validator.py"]
```

#### 2. What Happens

The skill will:
1. ✅ Validate repository and file paths
2. ✅ Extract baseline metrics from 6 months ago
3. ✅ Calculate current metrics from working directory
4. ✅ Run AI signature detection
5. ✅ Generate detailed comparison report

#### 3. Review the Report

Open the generated report at `olaf-data/ai-impact/ai-impact-file-analysis-[timestamp].md`:

```markdown
### File: `src/auth.py`

**AI Likelihood**: 0.87 (High)

**Detection Indicators**:
- ✓ MI_JUMP_SIGNIFICANT: Maintainability Index increased by 35 points
- ✓ DIFFICULTY_DROP_MAJOR: Halstead Difficulty decreased by 42%
- ✓ EFFORT_REDUCTION: Halstead Effort reduced by 68%

**Metrics Comparison**:

| Metric | Before | After | Change | Impact |
|--------|--------|-------|--------|--------|
| Maintainability Index | 42 | 77 | +35 | ✅ Excellent |
| Cyclomatic Complexity | 18 | 9 | -50% | ✅ Improved |
| Halstead Difficulty | 28.4 | 16.5 | -42% | ✅ Simplified |
| Halstead Effort | 18500 | 5900 | -68% | ✅ Optimized |
```

#### 4. Interpretation

- **High AI Likelihood (0.87)**: Very confident AI was used
- **All indicators present**: Strong evidence of AI-assisted refactoring
- **Metrics improved dramatically**: Code is now easier to understand and maintain

### Key Takeaways

✅ `auth.py` was likely improved using AI
✅ Quality metrics show significant improvement
✅ Code is now more maintainable

---

## Tutorial 2: Track Quarterly Productivity Trends

### Scenario
Your team started using GitHub Copilot in January 2025 (Q1). It's now the end of Q1, and you want to measure productivity impact.

### Steps

#### 1. Generate Quarterly Snapshots

```
@olaf measure-ai-impact mode:quarterly-trends since:"2024-01-01"
```

#### 2. What Happens

The skill will:
1. ✅ Analyze Git commit history from 2024-01-01 to present
2. ✅ Generate snapshots for each quarter (2024-Q1, Q2, Q3, Q4, 2025-Q1)
3. ✅ Calculate productivity metrics per quarter
4. ✅ Identify trends and AI correlation

#### 3. Review the Report

Open `olaf-data/ai-impact/ai-impact-quarterly-trends-[timestamp].md`:

```markdown
## Productivity Overview

| Quarter | Commits | Code Churn | Commits/Day | Contributors |
|---------|---------|------------|-------------|--------------|
| 2024-Q4 | 150 | 12,000 LOC | 2.3 | 5 |
| 2025-Q1 | 210 | 18,500 LOC | 3.2 | 5 |

### Key Trends
- ✅ Commits increased by 40% in Q1 2025
- ✅ Code churn up 54% (more code produced)
- ✅ Daily commit rate improved from 2.3 → 3.2 (+39%)
- ⚠️ Contributor count stable (AI adoption, not team growth)

### Estimated AI Impact
**Assessment**: High (Confident)

Based on:
- Productivity spike in Q1 2025 (AI adoption quarter)
- Increased velocity without team size change
- Commit patterns consistent with AI-assisted development
```

#### 4. Compare Specific Quarters

For deeper analysis:

```
@olaf measure-ai-impact mode:quarterly-trends compare:["2024-Q4", "2025-Q1"]
```

This generates a detailed comparison:

```markdown
### 2024-Q4 vs 2025-Q1

| Metric | 2024-Q4 | 2025-Q1 | Change | Trend |
|--------|---------|---------|--------|-------|
| Commits | 150 | 210 | +60 (+40%) | ↗ |
| Code Churn | 12K | 18.5K | +6.5K (+54%) | ↗ |
| Commits/Day | 2.3 | 3.2 | +0.9 (+39%) | ↗ |
| LOC/Commit | 80 | 88 | +8 (+10%) | ↗ |
```

### Key Takeaways

✅ Productivity increased significantly in Q1 2025
✅ AI adoption likely contributed to 39% improvement in daily commits
✅ Code velocity up without team expansion

---

## Tutorial 3: Create Baseline for Future Comparison

### Scenario
You're about to introduce AI tools to your team next month. You want a baseline snapshot to measure future impact.

### Steps

#### 1. Create Baseline Snapshot

```
@olaf measure-ai-impact mode:snapshot name:"baseline-pre-ai"
```

#### 2. What Happens

The skill will:
1. ✅ Collect current repository metrics
2. ✅ Save snapshot JSON file
3. ✅ Display summary

Output:

```markdown
# Snapshot Created: baseline-pre-ai

**Timestamp**: 2025-01-24 14:30:00
**Git Commit**: a3f7d9c
**Total Files**: 125
**Total LOC**: 45,000

**Metrics Collected**:
- Maintainability Index (avg): 58
- Cyclomatic Complexity (avg): 12
- Halstead Difficulty (avg): 22.5
- Commit activity (last 90 days): 85 commits

**Snapshot saved**: olaf-data/ai-impact/snapshots/snapshot-baseline-pre-ai.json
```

#### 3. Use Baseline Later

Three months later, after AI adoption:

```
@olaf measure-ai-impact mode:file-analysis baseline_date:"baseline-pre-ai" files:["src/**/*.py"]
```

The skill will compare current state against your pre-AI baseline.

### Key Takeaways

✅ Baseline snapshot created for future comparison
✅ Can measure AI impact accurately using historical data
✅ JSON file preserves all metrics for long-term analysis

---

## Tutorial 4: Identify Files Needing AI Assistance

### Scenario
You want to find files with low maintainability that could benefit from AI-assisted refactoring.

### Steps

#### 1. Run File Analysis on All Python Files

```
@olaf measure-ai-impact mode:file-analysis files:["src/**/*.py"]
```

#### 2. Review Recommendations Section

The report includes:

```markdown
## Suggested Next Targets for AI Assistance

- `src/legacy_parser.py` - Current MI: 32 - Complexity: 28
- `src/old_validator.py` - Current MI: 41 - Complexity: 22
- `src/data_processor.py` - Current MI: 38 - Complexity: 19
```

#### 3. Refactor with AI

Use GitHub Copilot or similar tools to refactor `legacy_parser.py`.

#### 4. Validate Improvement

```
@olaf measure-ai-impact mode:file-analysis files:["src/legacy_parser.py"]
```

Expected result:

```markdown
### File: `src/legacy_parser.py`

**AI Likelihood**: 0.92 (High)

**Metrics Comparison**:

| Metric | Before | After | Change |
|--------|--------|-------|--------|
| Maintainability Index | 32 | 68 | +36 ✅ |
| Cyclomatic Complexity | 28 | 12 | -57% ✅ |
```

### Key Takeaways

✅ Identified low-quality files systematically
✅ Validated AI improvements with metrics
✅ Iteratively improved codebase quality

---

## Tutorial 5: Quarterly Review Workflow

### Scenario
Every quarter, you want to generate a standard AI impact report for leadership.

### Standard Workflow

#### End of Each Quarter (e.g., March 31)

**Step 1**: Generate quarterly snapshot

```
@olaf measure-ai-impact mode:quarterly-trends since:"2024-01-01"
```

**Step 2**: Compare current quarter vs previous

```
@olaf measure-ai-impact mode:quarterly-trends compare:["2024-Q4", "2025-Q1"]
```

**Step 3**: Create checkpoint snapshot

```
@olaf measure-ai-impact mode:snapshot name:"2025-Q1-checkpoint"
```

**Step 4**: Review and share reports

- File analysis: `olaf-data/ai-impact/ai-impact-quarterly-trends-[timestamp].md`
- Snapshot: `olaf-data/ai-impact/snapshots/snapshot-2025-Q1-checkpoint.json`

### Automation (Optional)

Add to your CI/CD or scheduled tasks:

```bash
# End-of-quarter automation (PowerShell)
$quarter = "2025-Q1"
python skills/onboard/tools/commons/project-onboarding/git_productivity_analyzer.py snapshots --since 2024-01-01
python skills/onboard/tools/commons/project-onboarding/ai_impact_analyzer.py snapshot --name $quarter
```

---

## Common Patterns

### Pattern 1: Before/After Validation

**Use Case**: Validate AI-assisted changes

```
# Before refactoring
@olaf measure-ai-impact mode:snapshot name:"before-refactor"

# [Perform AI refactoring]

# After refactoring
@olaf measure-ai-impact mode:file-analysis baseline_date:"before-refactor"
```

### Pattern 2: Team Retrospective

**Use Case**: Quarterly team review

```
# Generate trends
@olaf measure-ai-impact mode:quarterly-trends since:"2024-01-01"

# Compare specific quarters
@olaf measure-ai-impact mode:quarterly-trends compare:["2024-Q3", "2024-Q4"]
```

### Pattern 3: Continuous Monitoring

**Use Case**: Track ongoing AI impact

```
# Monthly snapshots
@olaf measure-ai-impact mode:snapshot name:"2025-01-monthly"

# Quarterly full analysis
@olaf measure-ai-impact mode:quarterly-trends
```

---

## Troubleshooting

### Issue: "No baseline data available"

**Solution**: Create a snapshot first:
```
@olaf measure-ai-impact mode:snapshot name:"baseline"
```

### Issue: "Halstead metrics unavailable"

**Solution**: Install Radon library:
```bash
pip install radon
```

Or use limited mode:
```
@olaf measure-ai-impact mode:snapshot include_halstead:false
```

### Issue: "Invalid quarter format"

**Solution**: Use correct format: `YYYY-QN` (e.g., `2025-Q1`, `2024-Q4`)

### Issue: "Not a Git repository"

**Solution**: Run from repository root with `.git` folder

---

## Next Steps

After completing these tutorials:

1. ✅ Create a baseline snapshot for your repository
2. ✅ Set up quarterly review schedule
3. ✅ Identify low-MI files for AI assistance
4. ✅ Track AI impact over time

For advanced usage, see:
- `description.md` - Full capability reference
- Analyzer tool documentation - Technical details

---

**Tutorial Version**: 1.0.0
**Last Updated**: 2025-01-24
