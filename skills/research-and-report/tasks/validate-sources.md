---
task_id: "validate-sources"
task_name: "Validate Sources"
dependencies: ["conduct-research-chapter"]
---

# Task: Validate Sources

## Input Context
**Required Context Variables**: 
- `context.all_sources`: Array - All sources collected from chapters
- `context.report_file`: String - Path to report file

**Required Files**: 
- Research report file (for reference)

**Required Tools**: 
- Web requests (http_request) for URL validation

## Task Instructions

### Verify Source Accessibility and Currency

1. **Compile Source List**:
   - Extract all unique sources from `all_sources`
   - Remove duplicates (same URL)
   - Count total sources collected

2. **Validate Each Source**:
   
   **A. Check URL Accessibility**:
   - For each source URL:
     - Send HEAD request using http_request tool
     - Check response status:
       - 200 OK: Accessible
       - 301/302: Redirect (follow and note final URL)
       - 404: Not Found
       - 403: Forbidden
       - 500+: Server Error
   - Record validation status
   
   **B. Verify URL Format**:
   - Ensure full URL provided (not generic reference)
   - Check format: `[Title](https://full-url.com)`
   - Flag any malformed or missing URLs
   
   **C. Assess Currency**:
   - Review `currency` field from source metadata
   - Count sources by year:
     - 2025: Current
     - 2024: Recent
     - 2023 or older: Potentially outdated
   - Flag if majority of sources are outdated

3. **Generate Validation Report**:
   
   ```
   ============================================
   SOURCE VALIDATION REPORT
   ============================================
   
   Total Sources: [count]
   
   Accessibility:
   - Accessible (200 OK): [count] ([percentage]%)
   - Redirects (301/302): [count]
   - Not Found (404): [count]
   - Other Errors: [count]
   
   Currency Distribution:
   - 2025 Sources: [count] ([percentage]%)
   - 2024 Sources: [count] ([percentage]%)
   - 2023 or Older: [count] ([percentage]%)
   
   Issues Found:
   [List any problematic sources]
   
   Recommendations:
   [Any suggestions for improvement]
   
   ============================================
   ```

4. **Flag Critical Issues**:
   - If >20% of URLs inaccessible: WARNING
   - If >50% of sources pre-2024: WARNING (outdated)
   - If any sources lack URLs: ERROR (violates requirement)
   - Display warnings prominently

5. **Update Source Metadata**:
   - Add validation status to each source:
     ```
     {
       "title": "Source Title",
       "url": "https://full-url.com",
       "accessed_date": "[timestamp]",
       "relevance": "...",
       "currency": "2024|2025|older",
       "validation_status": "accessible|redirect|not_found|error",
       "validation_date": "[timestamp]"
     }
     ```

6. **Store Validation Results**:
   - Save validation report to context
   - Make available for final report inclusion

## Output Requirements

**Context Variables Created**:
- `context.validated_sources`: Array - Sources with validation metadata
- `context.source_validation_report`: String - Full validation report text
- `context.validation_warnings`: Array - List of warnings (if any)
- `context.validation_passed`: Boolean - True if no critical issues

**Files Created**: None (report stored in context)

**Context Passed to Next Tasks**:
- Validated sources for inclusion in final report
- Validation report for appendix
- Validation status for quality assurance

## Validation Criteria

**PASS Criteria**:
- All sources include full URLs
- At least 80% of URLs are accessible
- At least 50% of sources are from 2024-2025

**WARNING Criteria**:
- 60-79% URLs accessible
- 30-49% sources are current
- Some redirects or minor issues

**FAIL Criteria**:
- Any sources without URLs
- Less than 60% URLs accessible
- Less than 30% sources are current
