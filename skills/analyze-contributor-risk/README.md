# Analyze Contributor Risk

**Version**: 1.0.0  
**Status**: Active  
**Protocol**: Act

## Overview

The `analyze-contributor-risk` skill helps teams understand their knowledge distribution, identify bus factor risks, and plan for succession by analyzing Git repository contributor patterns.

## What It Does

- **Calculates Bus Factor**: Identifies minimum number of contributors needed to represent 50% of commits
- **Detects Knowledge Silos**: Finds files with concentrated ownership (single contributors)
- **Assesses Team Health**: Analyzes contributor activity patterns and distribution
- **Provides Recommendations**: Suggests actionable risk mitigation strategies

## When to Use

- Before team restructuring or member departures
- During project health assessments
- When planning documentation priorities
- For succession planning initiatives
- To identify training and knowledge transfer needs
- Before critical project milestones

## Usage

### Basic Usage
```
olaf analyze-contributor-risk
```

### With Parameters
```
olaf analyze-contributor-risk
  repository_path: /path/to/repo
  analysis_period_months: 12
  output_location: olaf-data/contributor-risk/
```

## Key Outputs

### Bus Factor Score
- **1**: CRITICAL - Single point of failure
- **2**: HIGH - Very limited distribution
- **3-4**: MEDIUM - Some concentration
- **5+**: LOW - Healthy distribution

### Risk Analysis
- Critical contributor identification
- File ownership concentration
- Knowledge silo detection
- Team health metrics

### Recommendations
- Immediate actions for high-risk areas
- Documentation priorities
- Pair programming suggestions
- Succession planning guidance

## Example Output

```markdown
## Executive Summary
- Repository: my-project
- Bus Factor: 2 (HIGH RISK)
- Critical Contributors: Alice (45%), Bob (28%)
- High-Risk Files: 23 files with >80% single ownership

## Recommendations
- Immediate: Pair programming for auth module (Alice: 92% ownership)
- Short-term: Document deployment process (Bob: sole knowledge)
- Long-term: Cross-train team on core architecture
```

## Related Skills

- `onboard-me`: Full project onboarding including contributor analysis
- `measure-ai-impact`: Quarterly productivity trends
- `review-code`: Code quality assessment

## Technical Details

**Tool**: `contributor_analyzer.py`  
**Requirements**: Python 3.10+, Git repository  
**Analysis Period**: Default 12 months (configurable 1-36 months)

## Limitations

- Requires Git history (commit-based analysis)
- Bot detection may need manual verification
- Cannot measure knowledge quality, only commit distribution
- Recent refactors may skew ownership percentages
