---
name: analyze-contributor-risk
description: Analyze bus factor, knowledge concentration, and contributor risk patterns in repositories
license: Apache-2.0
metadata:
  olaf_tags: [contributors, bus-factor, risk, knowledge-concentration, team-health]
  olaf_protocol: Act
  copyright: Copyright (c) 2026 pjmp020564
  author: pjmp020564 (on github)
  repository: https://github.com/haal-ai/haal-ide
  provider: Haal AI
---

if you are in need to get the date and  time, use time tools, fallback to shell command if needed

# Analyze Contributor Risk

## Description
Analyze repository contributor patterns to identify bus factor risks, knowledge concentration, and team health metrics. Provides actionable insights for risk mitigation and succession planning.

## Input Parameters

You MUST request these parameters if not provided:

- **repository_path**: string - Path to repository (default: current workspace)
- **analysis_period_months**: integer - Number of months to analyze (default: 12)
- **output_location**: string - Where to save the report (default: olaf-data/contributor-risk/)

## User Interaction Protocol

You WILL use **Act** protocol for analysis execution.

## Process

### 1. Validation Phase
You WILL verify all requirements:
- Confirm repository path exists and is a valid Git repository
- Validate analysis period is reasonable (1-36 months)
- Check for Python tools availability
- Verify write access to output location

### 2. Execution Phase

**Tool Invocation**:
```bash
python skills/analyze-contributor-risk/tools/contributor_analyzer.py \
  "{repository_path}" -m {analysis_period_months} -o "{output_location}/contributor-risk-analysis.md" -v
```

**Data Extraction**:
You WILL read and parse the generated output file to extract:

- **Executive Summary**: Commit distribution, bus factor, file ownership overview
- **Contributor Statistics**: Total commits, human vs automated, unique contributors, bus factor
- **Top Contributors**: Rank, names, commit counts, percentages, risk levels
- **Bus Factor Analysis**: Critical contributors representing 50% of commits
- **Automated Contributors**: Bots/services, commit counts, purposes
- **File Ownership**: High concentration files, primary owners, percentages
- **Risk Assessment**: Overall risk level, factors, recommendations
- **Commit Patterns**: Activity patterns, timing, frequency for top contributors

### 3. Analysis & Interpretation

You WILL provide interpretation:

**Bus Factor Assessment**:
- Bus Factor = 1: CRITICAL risk - single point of failure
- Bus Factor = 2: HIGH risk - very limited knowledge distribution
- Bus Factor = 3-4: MEDIUM risk - some concentration concerns
- Bus Factor ≥ 5: LOW risk - healthy knowledge distribution

**Knowledge Concentration**:
- Files with >80% single-owner commits: High risk
- Files with >60% single-owner commits: Medium risk
- Identify critical files requiring knowledge transfer

**Team Health Indicators**:
- Contributor churn patterns
- Active vs inactive contributor ratio
- Bot contribution percentage

### 4. Recommendations

You WILL generate actionable recommendations:
- Pair programming suggestions for high-risk areas
- Documentation priorities for concentrated knowledge
- Cross-training opportunities
- Succession planning for critical contributors

## Output Specifications

**Primary Deliverable**: Comprehensive contributor risk analysis saved as:
`[output_location]/contributor-risk-analysis-[YYYYMMDD-HHmm].md`

**Report Structure**:
```markdown
# Contributor Risk Analysis

## Executive Summary
- Repository: {name}
- Analysis Period: {months} months
- Bus Factor: {number}
- Overall Risk: {LOW/MEDIUM/HIGH/CRITICAL}

## Key Findings
- Total Contributors: {human} + {bots} automated
- Critical Contributors: {names} ({percentage}% of commits)
- High-Risk Files: {count} files with concentrated ownership

## Bus Factor Analysis
### Critical Contributors (50% threshold)
- Contributor 1: {commits} commits ({percentage}%)
- Contributor 2: {commits} commits ({percentage}%)

### Interpretation
{Risk assessment and impact analysis}

## File Ownership Concentration
### High-Risk Files (>80% single owner)
| File | Primary Owner | Ownership % | Risk Level |
|------|--------------|-------------|------------|
| ... | ... | ... | ... |

## Commit Pattern Analysis
{Activity patterns and contributor behaviors}

## Risk Mitigation Recommendations
### Immediate Actions
- {Specific recommendations}

### Long-term Strategies
- {Strategic planning}
```

## Error Handling

You MUST handle these scenarios:
- **Missing Git repository**: Prompt user for valid repo path
- **No commit history**: Report insufficient data
- **Tool execution failure**: Display stderr and suggest fixes
- **Insufficient contributors**: Note that analysis may be limited

## Success Criteria

- ✅ Report generated with bus factor calculation
- ✅ Risk level assessed and justified
- ✅ High-risk files identified
- ✅ Actionable recommendations provided
- ✅ User understands team health status

---

**Related Skills**: onboard-me, measure-ai-impact
**Tools Used**: contributor_analyzer.py
