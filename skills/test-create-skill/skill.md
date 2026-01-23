---
name: test-create-skill
description: Regression test to ensure create-skill functionality always works correctly
license: Apache-2.0
metadata:
  olaf_tags: [testing, regression, create-skill, validation]
  copyright: Copyright (c) 2026 pjmp020564
  author: pjmp020564 (on github)
  repository: https://github.com/haal-ai/haal-ide
  provider: Haal AI
---

CRITICAL: Ensure the OLAF condensed framework is loaded and applied: <olaf-work-instructions>, <olaf-framework-validation>. If not loaded, read the full ~/reference/.condensed/olaf-framework-condensed.md

## Time Retrieval

## Time Retrieval\s*Get current timestamp in `YYYYMMDD-HHmm` format



## Input Parameters

You MUST request these parameters if not provided by the user:
- **test_scope**: string|"full"|"basic"|"specific" - Test coverage level (OPTIONAL - default: "full")
- **cleanup_after**: boolean - Remove test artifacts after completion (OPTIONAL - default: true)
- **test_skill_name**: string - Name for test skill if testing specific scenario (OPTIONAL - default: "test-regression-skill")

## User Interaction

You MUST follow these interaction guidelines:
- Execute tests directly without requiring approval (automated testing)
- Provide clear progress updates at each test phase
- Report failures immediately with detailed diagnostics
- Confirm cleanup completion before finishing

## Prerequisites

This skill validates the create-skill functionality is working:
1. You MUST verify create-skill templates exist and are accessible2. You WILL validate OLAF framework structure is intact
3. You MUST confirm skills directory access permissions

## Process

### 1. Validation Phase

You WILL verify all requirements:
- Confirm test parameters and scope
- Validate access to create-skill templates and framework files
- Check skills directory write permissions
- Verify competency directory structure exists

### 2. Execution Phase

<!-- <test_environment_setup> -->
**Test Environment Setup**:
- Create test timestamp identifier
- Prepare test workspace location
- Initialize test artifact tracking
<!-- </test_environment_setup> -->

<!-- <basic_functionality_tests> -->
**Basic Functionality Tests**:
You WILL execute these core validation tests:
1. **Template Access Test**:
   - Verify skill-template.md loads correctly
   - Verify prompting-principles.md loads correctly  
   - Confirm template structure is valid
2. **Parameter Collection Test**:
   - Test required parameter validation
   - Test optional parameter handling
   - Validate parameter type checking
3. **Skill Structure Generation Test**:
   - Test directory creation for new skill
   - Verify manifest generation with correct schema
   - Test prompt file creation following template
   - Validate documentation file generation
<!-- </basic_functionality_tests> -->

<!-- <component_handling_tests> -->
**Component Handling Tests** (if test_scope is "full"):
You WILL validate component scenarios:
1. **Template Component Test**:
   - Test external template file creation
   - Verify template reference in main prompt
   - Validate template path in BOM manifest
2. **Tool Component Test**:
   - Test tool file creation for different types
   - Verify tool reference in main prompt
   - Validate tool path in BOM manifest
3. **Helper Component Test**:
   - Test helper file creation
   - Verify helper reference structure
   - Validate helper path in BOM manifest
4. **Knowledge Base Component Test**:
   - Test KB file creation
   - Verify KB reference in main prompt
   - Validate KB path in BOM manifest
<!-- </component_handling_tests> -->

<!-- <competency_integration_tests> -->
**Competency Integration Tests**:
You WILL validate competency handling:
1. **Existing Competency Test**:
   - Test skill assignment to existing competency
   - Verify competency manifest update
   - Validate skill reference integrity
2. **New Competency Test**:
   - Test new competency creation
   - Verify competency manifest generation
   - Validate competency structure compliance
<!-- </competency_integration_tests> -->

<!-- <schema_validation_tests> -->
**Schema Validation Tests**:
You WILL verify compliance:
1. **Manifest Schema Test**:
   - Validate skill manifest against schema
   - Test BOM completeness and accuracy
   - Verify metadata structure compliance
2. **File Structure Test**:
   - Validate directory organization
   - Test file naming conventions
   - Verify relative path accuracy in BOM
<!-- </schema_validation_tests> -->

<!-- <error_handling_tests> -->
**Error Handling Tests**:
You WILL validate error scenarios:
1. **Invalid Input Test**:
   - Test handling of invalid skill names
   - Test missing required parameters
   - Test invalid competency references
2. **File Access Error Test**:
   - Test behavior with read-only directories
   - Test handling of missing template files
   - Test duplicate skill name scenarios
3. **Schema Validation Error Test**:
   - Test response to invalid manifest structure
   - Test handling of malformed JSON
   - Test BOM validation failures
<!-- </error_handling_tests> -->

<!-- <reindexing_tests> -->
**Reindexing Tests**:
You WILL validate reindexing functionality:
1. **Reindexing Offer Test**:
   - Test that reindexing is offered after skill creation
   - Verify proper reindexing prompt presentation
   - Validate user can accept or decline reindexing
2. **Reindexing Script Execution Test**:
   - Test execution of select_collection.py script
   - Verify script can be found at correct path
   - Validate script executes without errors
3. **Index Update Validation Test**:
   - Test that new skill appears in competency index
   - Verify pattern markers remain intact
   - Validate skill is discoverable through OLAF query
<!-- </reindexing_tests> -->

**Core Logic**: Execute following protocol requirements
- Run comprehensive test suite based on test_scope
- Validate all create-skill functionality paths
- Document test results and any failures
- Clean up test artifacts if cleanup_after=true

### 3. Validation Phase

You WILL validate test results:
- Confirm all tests executed successfully
- Identify any functionality regressions
- Verify test artifact cleanup (if enabled)

## Output Format

You WILL generate outputs following this structure:
- **Test Summary**: Overall pass/fail status with test counts
- **Detailed Results**: Results for each test category with specific failures
- **Regression Report**: Any detected issues with create-skill functionality
- **Recommendations**: Actions needed to address any failures

## User Communication

You WILL provide these updates to the user:

### Progress Updates
- Test execution start with scope confirmation
- Completion status for each test category
- Real-time failure notifications if issues detected
- Cleanup completion confirmation

### Completion Summary
- Total tests executed vs passed/failed
- Summary of any detected regressions
- Location of test artifacts (if preserved)
- Timestamp of test execution: [YYYYMMDD-HHmm format]

### Next Steps

You WILL clearly define:
- Actions required for any test failures
- Recommendations for create-skill improvements
- Schedule for next regression test execution
- Documentation of test coverage achieved

## Domain-Specific Rules

You MUST follow these constraints:
- Rule 1: NEVER modify create-skill source code during testing
- Rule 2: ALWAYS clean up test artifacts unless explicitly requested to preserve
- Rule 3: MUST execute tests in isolated test workspace to avoid conflicts
- Rule 4: ALWAYS validate schema compliance for generated test skills
- Rule 5: MUST document exact failure conditions for any regression detected

## Success Criteria

You WILL consider the task complete when:
- [ ] All test categories executed based on test_scope
- [ ] Test results documented with pass/fail status
- [ ] Any regressions clearly identified and documented
- [ ] Reindexing functionality validated and working
- [ ] Test artifacts cleaned up (if cleanup_after=true)
- [ ] Recommendations provided for any failures
- [ ] Test execution timestamp recorded

## Required Actions
1. Validate test environment and prerequisites2. Execute comprehensive test suite following test_scope
3. Generate detailed test results and regression report4. Provide user communication and recommendations
5. Clean up test artifacts if requested

## Error Handling

You WILL handle these scenarios:
- **Test Environment Setup Failed**: Provide clear error message and resolution steps
- **Template Access Failed**: Report missing files and provide manual verification steps
- **Test Skill Creation Failed**: Document exact failure point and error details
- **Schema Validation Failed**: Report specific validation errors and corrective actions
- **Reindexing Script Not Found**: Report missing script and provide path verification steps
- **Reindexing Script Execution Failed**: Document script errors and troubleshooting steps
- **Index Update Validation Failed**: Report indexing issues and manual validation steps
- **Cleanup Failed**: Report artifacts that couldn't be removed and provide manual cleanup instructions

⚠️ **Critical Requirements**
- MANDATORY: Execute tests in isolated environment to prevent conflicts
- MANDATORY: Document exact failure conditions for reproducibility
- NEVER modify create-skill functionality during testing
- ALWAYS validate that test artifacts are properly isolated
- ALWAYS provide actionable recommendations for any detected issues
- ALWAYS preserve evidence of failures for debugging
- NEVER assume test failures are acceptable without investigation

