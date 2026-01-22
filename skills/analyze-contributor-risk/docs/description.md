# analyze-contributor-risk

## Overview

The `analyze-contributor-risk` skill analyzes repository contributor patterns to identify bus factor risks, knowledge concentration, and team health metrics. It provides actionable insights for risk mitigation and succession planning.

## Purpose

This skill helps development teams understand their contributor dynamics and identify potential risks related to knowledge concentration. By analyzing commit history and file ownership patterns, it reveals critical dependencies on individual contributors that could impact project continuity.

## Key Features

- **Bus Factor Analysis**: Calculates the minimum number of contributors whose departure would significantly impact the project
- **Knowledge Concentration Detection**: Identifies files with high single-owner commit percentages
- **Contributor Statistics**: Provides detailed breakdown of human vs automated contributions
- **Risk Assessment**: Generates overall risk levels with justifications
- **Actionable Recommendations**: Suggests pair programming, documentation priorities, and cross-training opportunities

## Usage

Invoke the skill with the following parameters:

| Parameter | Type | Required | Default | Description |
|-----------|------|----------|---------|-------------|
| `repository_path` | string | No | current workspace | Path to the Git repository to analyze |
| `analysis_period_months` | integer | No | 12 | Number of months of history to analyze (1-36) |
| `output_location` | string | No | olaf-data/contributor-risk/ | Directory for the generated report |

## Process Flow

1. **Validation Phase**: Verifies repository exists, analysis period is valid, Python tools are available, and output location is writable
2. **Execution Phase**: Runs the contributor_analyzer.py tool to extract commit data and ownership patterns
3. **Analysis & Interpretation**: Assesses bus factor risk levels and knowledge concentration
4. **Recommendations**: Generates actionable suggestions for risk mitigation

## Output

The skill generates a comprehensive Markdown report containing:

- Executive summary with bus factor and overall risk level
- Key findings including contributor counts and high-risk files
- Bus factor analysis with critical contributor details
- File ownership concentration table
- Commit pattern analysis
- Risk mitigation recommendations (immediate and long-term)

## Examples

**Basic usage** (analyze current repository):
```
Analyze contributor risk for this repository
```

**Custom analysis period**:
```
Analyze contributor risk for the last 6 months
```

**Specific repository**:
```
Analyze contributor risk for /path/to/repo with 24 months of history
```

## Error Handling

| Scenario | Behavior |
|----------|----------|
| Missing Git repository | Prompts user for valid repository path |
| No commit history | Reports insufficient data for analysis |
| Tool execution failure | Displays error details and suggests fixes |
| Insufficient contributors | Notes that analysis may be limited |

## Related Skills

- `onboard-me` - For onboarding new contributors to reduce bus factor
- `measure-ai-impact` - For measuring AI contribution patterns
