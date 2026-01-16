# Test Create Skill - Description

## Overview
The `test-create-skill` is a comprehensive regression testing skill designed to validate the create-skill functionality within the OLAF framework. This skill ensures that the skill creation process remains reliable and functional across framework updates and modifications.

## Purpose
This skill addresses the critical need for automated testing of the create-skill workflow, preventing regressions that could break skill generation capabilities and ensuring consistent quality in the OLAF framework.

## Key Features

### Comprehensive Test Coverage
- **Template Validation**: Verifies skill templates load correctly and maintain proper structure
- **Parameter Handling**: Tests required and optional parameter collection and validation
- **Component Support**: Validates creation of templates, tools, helpers, and knowledge base components
- **Schema Compliance**: Ensures generated skills conform to manifest schema requirements
- **Reindexing Functionality**: Tests competency index update and skill discoverability
- **Error Scenarios**: Tests error handling for edge cases and invalid inputs

### Test Scopes
- **Full Testing**: Complete validation of all create-skill functionality
- **Basic Testing**: Core functionality validation for quick checks
- **Specific Testing**: Targeted testing of particular scenarios or components

### Automated Cleanup
- Optional cleanup of test artifacts after execution
- Isolated test environment to prevent conflicts
- Preservation of failure evidence for debugging

## Usage Context
Use this skill when:
- Validating create-skill functionality after framework changes
- Running routine regression tests on OLAF skill creation
- Debugging issues with skill generation
- Ensuring quality before framework releases
- Onboarding new team members to validate their environment

## Integration
Part of the `olaf-testers` competency, designed to work alongside other testing and validation skills within the OLAF framework testing suite.

## Quality Assurance
This skill follows OLAF standards for:
- Imperative language usage
- Comprehensive error handling
- Clear success criteria definition
- Proper protocol compliance
- Structured output formatting