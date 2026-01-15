# Contributor Risk Analysis

## Executive Summary
- **Repository**: {{repository_name}}
- **Analysis Period**: {{analysis_period_months}} months
- **Bus Factor**: {{bus_factor}}
- **Overall Risk Level**: {{risk_level}}

## Key Findings
- **Total Contributors**: {{human_contributors}} human + {{bot_contributors}} automated
- **Critical Contributors**: {{critical_contributor_names}} ({{critical_percentage}}% of commits)
- **High-Risk Files**: {{high_risk_file_count}} files with concentrated ownership (>80%)
- **Active Days**: {{active_days}} days with commits

## Bus Factor Analysis

### Definition
**Bus Factor** = The minimum number of team members that would need to be unavailable (hit by a bus) to stall the project due to knowledge loss.

### Critical Contributors (50% Threshold)
{{#critical_contributors}}
- **{{rank}}. {{name}}** ({{email}})
  - Commits: {{commit_count}} ({{percentage}}%)
  - Risk Level: {{risk_level}}
{{/critical_contributors}}

### Interpretation
{{bus_factor_interpretation}}

**Risk Assessment**: {{overall_risk_assessment}}

## Contributor Statistics

| Metric | Value |
|--------|-------|
| Total Commits | {{total_commits}} |
| Human Contributors | {{human_contributors}} |
| Automated Contributors | {{bot_contributors}} |
| Commits by Humans | {{human_commits}} ({{human_percentage}}%) |
| Commits by Bots | {{bot_commits}} ({{bot_percentage}}%) |
| Bus Factor | {{bus_factor}} |

## Top Human Contributors

| Rank | Contributor | Email | Commits | % of Total | Risk Level |
|------|------------|-------|---------|------------|------------|
{{#top_contributors}}
| {{rank}} | {{name}} | {{email}} | {{commits}} | {{percentage}}% | {{risk_level}} |
{{/top_contributors}}

## Automated Contributors

| Bot/Service | Commits | Purpose |
|-------------|---------|---------|
{{#automated_contributors}}
| {{name}} | {{commits}} | {{purpose}} |
{{/automated_contributors}}

## File Ownership Concentration

### High-Risk Files (>80% Single Owner)
{{#high_risk_files}}
- **{{file_path}}**
  - Primary Owner: {{owner_name}} ({{owner_email}})
  - Ownership: {{ownership_percentage}}%
  - Risk Level: {{risk_level}}
{{/high_risk_files}}

### Medium-Risk Files (60-80% Single Owner)
{{#medium_risk_files}}
- **{{file_path}}**: {{owner_name}} ({{ownership_percentage}}%)
{{/medium_risk_files}}

## Commit Pattern Analysis

{{#top_contributors_patterns}}
### {{contributor_name}}
- **Total Commits**: {{commit_count}}
- **Active Days**: {{active_days}}
- **Avg Commits/Day**: {{avg_commits_per_day}}
- **Peak Activity**: {{peak_activity_period}}
- **Recent Activity**: {{recent_activity_status}}
{{/top_contributors_patterns}}

## Risk Mitigation Recommendations

### Immediate Actions (High Priority)
{{#immediate_actions}}
- {{action}}
{{/immediate_actions}}

### Short-term Strategies (1-3 months)
{{#short_term_strategies}}
- {{strategy}}
{{/short_term_strategies}}

### Long-term Planning (3-12 months)
{{#long_term_strategies}}
- {{strategy}}
{{/long_term_strategies}}

## Knowledge Transfer Priorities

### Critical Files Requiring Documentation
{{#documentation_priorities}}
1. **{{file_path}}** (Owner: {{owner}}, {{ownership}}% ownership)
   - Rationale: {{rationale}}
{{/documentation_priorities}}

### Recommended Pair Programming Areas
{{#pair_programming_recommendations}}
- {{area}}: {{primary_owner}} should pair with {{suggested_pair}}
{{/pair_programming_recommendations}}

## Succession Planning

### At-Risk Knowledge Areas
{{#at_risk_areas}}
- **{{area}}**: Currently owned by {{owner}}
  - Backup candidates: {{backup_candidates}}
  - Training estimated time: {{training_time}}
{{/at_risk_areas}}

---

**Generated**: {{generation_timestamp}}
**Tool**: contributor_analyzer.py v{{tool_version}}
**Analysis Period**: {{start_date}} to {{end_date}}
