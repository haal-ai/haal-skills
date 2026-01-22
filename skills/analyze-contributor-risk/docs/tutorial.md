# Tutorial: analyze-contributor-risk

## Introduction

This tutorial guides you through using the `analyze-contributor-risk` skill to identify bus factor risks and knowledge concentration in your repository. By the end, you'll understand how to assess team health and implement risk mitigation strategies.

## Prerequisites

Before starting, ensure you have:

- [ ] A Git repository with commit history
- [ ] Python installed and available in your environment
- [ ] Write access to the output directory
- [ ] At least 1 month of commit history for meaningful analysis

## Step-by-Step Instructions

### Step 1: Prepare Your Repository

Ensure you're in a valid Git repository or have the path to one ready.

```bash
# Verify you're in a Git repository
git status
```

### Step 2: Invoke the Skill

Start the analysis by requesting contributor risk analysis:

```
Analyze contributor risk for this repository
```

Or with custom parameters:

```
Analyze contributor risk for /path/to/repo over the last 6 months, save to ./reports/
```

### Step 3: Review Validation

The skill will verify:
- Repository path exists and is valid
- Analysis period is reasonable (1-36 months)
- Python tools are available
- Output location is writable

If any validation fails, provide the requested information.

### Step 4: Wait for Analysis

The tool will execute and analyze:
- Commit distribution across contributors
- File ownership patterns
- Automated vs human contributions
- Activity patterns and timing

### Step 5: Interpret the Results

Review the generated report focusing on:

**Bus Factor Assessment**:
| Bus Factor | Risk Level | Meaning |
|------------|------------|---------|
| 1 | CRITICAL | Single point of failure |
| 2 | HIGH | Very limited knowledge distribution |
| 3-4 | MEDIUM | Some concentration concerns |
| ≥5 | LOW | Healthy knowledge distribution |

**Knowledge Concentration**:
- Files with >80% single-owner commits: High risk
- Files with >60% single-owner commits: Medium risk

### Step 6: Act on Recommendations

The report provides actionable recommendations:

1. **Immediate Actions**: Address critical risks first
2. **Pair Programming**: Suggested for high-risk areas
3. **Documentation**: Priorities for concentrated knowledge
4. **Cross-Training**: Opportunities to spread knowledge

### Step 7: Save and Share

The report is saved to your specified output location:
```
[output_location]/contributor-risk-analysis-[YYYYMMDD-HHmm].md
```

Share with your team to discuss findings and plan mitigation.

## Verification Checklist

After completing the analysis, verify:

- [ ] Report was generated successfully
- [ ] Bus factor is calculated and displayed
- [ ] Risk level is assessed with justification
- [ ] High-risk files are identified
- [ ] Recommendations are actionable and relevant
- [ ] You understand your team's health status

## Troubleshooting

### "Not a valid Git repository"

**Cause**: The specified path doesn't contain a `.git` directory.

**Solution**: Verify the repository path and ensure it's a valid Git repository.

### "Insufficient commit history"

**Cause**: The repository has too few commits for meaningful analysis.

**Solution**: Reduce the analysis period or wait for more commit history.

### "Tool execution failure"

**Cause**: Python tool encountered an error.

**Solution**: Check the error message, ensure Python is installed, and verify file permissions.

### "No contributors found"

**Cause**: The analysis period may not contain any commits.

**Solution**: Extend the analysis period or verify the repository has activity.

## Next Steps

After completing your first analysis:

1. **Schedule Regular Reviews**: Run monthly or quarterly to track trends
2. **Address Critical Risks**: Prioritize bus factor = 1 situations
3. **Implement Knowledge Sharing**: Use pair programming and documentation
4. **Track Improvements**: Compare reports over time to measure progress
5. **Explore Related Skills**: Use `onboard-me` to help new contributors ramp up
