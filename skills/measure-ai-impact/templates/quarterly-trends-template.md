# AI Impact Analysis - Quarterly Trends

**Generated**: {{timestamp}}
**Repository**: {{repository_path}}
**Analysis Period**: {{start_date}} to {{end_date}}
**Quarters Analyzed**: {{quarters_list}}

---

## Executive Summary

### Productivity Overview

| Quarter | Commits | Code Churn (LOC) | Commits/Day | Contributors | Active Days |
|---------|---------|------------------|-------------|--------------|-------------|
{{#quarters}}
| {{quarter_name}} | {{total_commits}} | {{total_churn}} | {{commits_per_day}} | {{contributor_count}} | {{active_days}} |
{{/quarters}}

### Key Trends
{{#key_trends}}
- {{trend_description}}
{{/key_trends}}

### Estimated AI Impact
**Assessment**: {{ai_impact_level}} ({{ai_impact_confidence}})

---

## Quarter-by-Quarter Comparison

{{#quarter_comparisons}}
### {{quarter1_name}} vs {{quarter2_name}}

#### Productivity Metrics

| Metric | {{quarter1_name}} | {{quarter2_name}} | Change | Trend |
|--------|-------------------|-------------------|--------|-------|
| Total Commits | {{q1_commits}} | {{q2_commits}} | {{commit_change}} | {{commit_trend}} |
| Code Churn | {{q1_churn}} | {{q2_churn}} | {{churn_change}} | {{churn_trend}} |
| Commits/Day | {{q1_commits_day}} | {{q2_commits_day}} | {{commits_day_change}} | {{commits_day_trend}} |
| Commits/Week | {{q1_commits_week}} | {{q2_commits_week}} | {{commits_week_change}} | {{commits_week_trend}} |
| LOC/Commit | {{q1_loc_commit}} | {{q2_loc_commit}} | {{loc_commit_change}} | {{loc_commit_trend}} |

#### Team Dynamics

| Metric | {{quarter1_name}} | {{quarter2_name}} | Change |
|--------|-------------------|-------------------|--------|
| Contributors | {{q1_contributors}} | {{q2_contributors}} | {{contributor_change}} |
| Active Days | {{q1_active_days}} | {{q2_active_days}} | {{active_days_change}} |
| Avg Commit Size | {{q1_avg_commit_size}} | {{q2_avg_commit_size}} | {{commit_size_change}} |

#### Interpretation
{{comparison_interpretation}}

---

{{/quarter_comparisons}}

## Detailed Quarterly Analysis

{{#quarters}}
### Quarter: {{quarter_name}} ({{quarter_start}} - {{quarter_end}})

#### Commit Activity
- **Total Commits**: {{total_commits}}
- **Active Days**: {{active_days}} / {{total_days}} ({{active_percentage}}%)
- **Peak Activity**: {{peak_activity_day}} ({{peak_commits}} commits)
- **Commits per Active Day**: {{commits_per_active_day}}

#### Code Changes
- **Lines Added**: {{lines_added}}
- **Lines Deleted**: {{lines_deleted}}
- **Net Change**: {{net_change}}
- **Code Churn**: {{code_churn}} LOC
- **Churn Rate**: {{churn_rate}}/commit

#### Contributor Breakdown
{{#contributors}}
- **{{contributor_name}}**: {{contributor_commits}} commits ({{contributor_percentage}}%), {{contributor_loc}} LOC
{{/contributors}}

#### Session Patterns
- **Average Session Gap**: {{avg_session_gap}} hours
- **Max Session Gap**: {{max_session_gap}} days
- **Typical Work Pattern**: {{work_pattern_description}}

#### Quality Indicators
{{#quality_indicators}}
- {{indicator_name}}: {{indicator_value}} ({{indicator_interpretation}})
{{/quality_indicators}}

---

{{/quarters}}

## Trend Visualizations

### Productivity Velocity Over Time

```
Commits per Day:
{{quarter1}}: [{{q1_bar}}] {{q1_commits_day}}
{{quarter2}}: [{{q2_bar}}] {{q2_commits_day}}
{{quarter3}}: [{{q3_bar}}] {{q3_commits_day}}
{{quarter4}}: [{{q4_bar}}] {{q4_commits_day}}

Code Churn per Quarter:
{{quarter1}}: [{{q1_churn_bar}}] {{q1_churn}}K LOC
{{quarter2}}: [{{q2_churn_bar}}] {{q2_churn}}K LOC
{{quarter3}}: [{{q3_churn_bar}}] {{q3_churn}}K LOC
{{quarter4}}: [{{q4_churn_bar}}] {{q4_churn}}K LOC
```

### Team Growth

```
Contributors:
{{quarter1}}: {{q1_contributors}} [{{q1_contributor_icons}}]
{{quarter2}}: {{q2_contributors}} [{{q2_contributor_icons}}]
{{quarter3}}: {{q3_contributors}} [{{q3_contributor_icons}}]
{{quarter4}}: {{q4_contributors}} [{{q4_contributor_icons}}]
```

---

## AI Adoption Impact Analysis

### Correlation Indicators

{{#ai_indicators}}
#### {{indicator_name}}
- **Observation**: {{observation}}
- **AI Correlation**: {{correlation_strength}}
- **Reasoning**: {{reasoning}}
{{/ai_indicators}}

### Estimated AI Contribution

Based on productivity patterns and timeline correlation:

| Impact Area | Pre-AI Baseline | Current | Change | AI Attribution |
|-------------|-----------------|---------|--------|----------------|
| Commits/Day | {{baseline_commits_day}} | {{current_commits_day}} | {{commits_day_delta}} | {{ai_commit_attribution}} |
| Code Velocity | {{baseline_velocity}} | {{current_velocity}} | {{velocity_delta}} | {{ai_velocity_attribution}} |
| Commit Quality | {{baseline_quality}} | {{current_quality}} | {{quality_delta}} | {{ai_quality_attribution}} |

**Overall AI Impact Score**: {{ai_impact_score}}/10

---

## Recommendations

### Productivity Insights
{{#productivity_insights}}
- {{insight_description}}
{{/productivity_insights}}

### Optimization Opportunities
{{#optimization_opportunities}}
- {{opportunity_description}}
{{/optimization_opportunities}}

### Next Steps
{{#next_steps}}
1. {{next_step}}
{{/next_steps}}

---

## Methodology Notes

- **Data Source**: Git commit history analysis
- **Quarter Definition**: Calendar quarters (Jan-Mar, Apr-Jun, Jul-Sep, Oct-Dec)
- **Metrics Calculation**:
  - Commits/Day: Total commits ÷ calendar days in quarter
  - Code Churn: Sum of absolute value of additions + deletions
  - Active Days: Days with at least one commit
- **Tools Used**: `git_productivity_analyzer.py`
- **Limitations**:
  - Metrics reflect commit behavior, not absolute productivity
  - Cannot distinguish AI-assisted vs manual commits directly
  - Requires correlation with AI adoption timeline for attribution

---

**Generated by**: OLAF measure-ai-impact skill
**Report Type**: Quarterly Productivity Trends
