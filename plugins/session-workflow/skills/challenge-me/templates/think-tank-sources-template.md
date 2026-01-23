# Sources: {subject}

**Purpose**: Comprehensive citation file containing all references used during ideation session
**Used By**: challenge-me.md
**Version**: 1.0
**Last Updated**: 2025-10-27

## Template Structure

---

# Source Citations: {subject}

**Session**: {session_identifier}
**Date**: {timestamp}
**Total Sources**: {total_source_count}

## Codebase References

### File: {file_path_1}
**Cycles Referenced**: {cycle_numbers}
**Lines/Functions**: {specific_locations}
**Key Insights**:
{list_insights_from_this_file}

**Relevance**: {describe_relevance}

---

### File: {file_path_2}
**Cycles Referenced**: {cycle_numbers}
**Lines/Functions**: {specific_locations}
**Key Insights**:
{list_insights_from_this_file}

**Relevance**: {describe_relevance}

---

{repeat_for_additional_codebase_files}

## Documentation References

### Document: {document_name_1}
**Cycles Referenced**: {cycle_numbers}
**Sections**: {specific_sections}
**Page Numbers**: {page_numbers_if_applicable}

**Key Insights**:
{list_insights_from_this_document}

**Relevance**: {describe_relevance}

---

### Document: {document_name_2}
**Cycles Referenced**: {cycle_numbers}
**Sections**: {specific_sections}
**Page Numbers**: {page_numbers_if_applicable}

**Key Insights**:
{list_insights_from_this_document}

**Relevance**: {describe_relevance}

---

{repeat_for_additional_documentation}

## Web Resources

### [{web_source_title_1}]({web_url_1})
**Cycles Referenced**: {cycle_numbers}
**Access Timestamp**: {access_timestamp}
**Source Type**: {article|documentation|forum|blog|academic}

**Key Excerpts**:
> {relevant_quote_1}

> {relevant_quote_2}

**Key Insights**:
{list_insights_from_this_source}

**Relevance**: {describe_relevance}

---

### [{web_source_title_2}]({web_url_2})
**Cycles Referenced**: {cycle_numbers}
**Access Timestamp**: {access_timestamp}
**Source Type**: {article|documentation|forum|blog|academic}

**Key Excerpts**:
> {relevant_quote_1}

> {relevant_quote_2}

**Key Insights**:
{list_insights_from_this_source}

**Relevance**: {describe_relevance}

---

{repeat_for_additional_web_sources}

## Cross-References

### Cycle 1 Sources
**Codebase**: {list_codebase_files_cycle_1}
**Documentation**: {list_documentation_cycle_1}
**Web**: {list_web_sources_cycle_1}

### Cycle 2 Sources
**Codebase**: {list_codebase_files_cycle_2}
**Documentation**: {list_documentation_cycle_2}
**Web**: {list_web_sources_cycle_2}

{repeat_for_additional_cycles}

## Source Impact Analysis

### Most Influential Sources
1. **{source_name_1}** - {describe_impact}
2. **{source_name_2}** - {describe_impact}
3. **{source_name_3}** - {describe_impact}

### Sources by Insight Type

#### Technical Implementation
{list_sources_for_technical_insights}

#### Best Practices
{list_sources_for_best_practices}

#### Risk Assessment
{list_sources_for_risk_insights}

#### Alternative Approaches
{list_sources_for_alternatives}

## Source Quality Assessment

### High Confidence Sources
{list_high_confidence_sources_with_rationale}

### Supporting Sources
{list_supporting_sources_with_rationale}

### Conflicting Information
{describe_any_conflicting_information_and_resolution}

---

## Placeholder Guide

- `{subject}`: The topic or subject area for ideation
- `{session_identifier}`: Session ID in format `<subject-3-words>-YYYYMMDD-HHMM`
- `{timestamp}`: Current timestamp in YYYYMMDD-HHmm format
- `{total_source_count}`: Total number of sources consulted
- `{file_path_N}`: Path to codebase file
- `{document_name_N}`: Name of documentation file
- `{web_source_title_N}`: Title of web resource
- `{web_url_N}`: Full URL of web resource
- `{cycle_numbers}`: Comma-separated list of cycles (e.g., "1, 3, 5")
- `{specific_locations}`: Line numbers, function names, or code sections
- `{specific_sections}`: Document sections or chapter names
- `{page_numbers_if_applicable}`: Page numbers if available
- `{access_timestamp}`: When the web resource was accessed
- `{relevant_quote_N}`: Direct quotes from sources
- `{list_*}`: Bulleted or numbered lists
- `{describe_*}`: Descriptive paragraphs
- `{repeat_for_*}`: Repeat the block for additional items

## Notes

- Every source must be documented with specific location information
- Codebase references must include file paths and specific locations
- Documentation references must include document names and sections
- Web resources must include full URLs and access timestamps
- Cross-references show which sources were used in each cycle
- Source impact analysis identifies the most influential references
- Quality assessment helps evaluate the reliability of information