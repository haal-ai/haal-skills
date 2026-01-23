# Test Create Skill - Tutorial

This tutorial will guide you through using the `test-create-skill` to validate create-skill functionality.

## Prerequisites

Before running the test:
1. Ensure you have access to the OLAF framework
2. Verify you're in a workspace with the `.olaf` directory structure
3. Confirm you have write permissions to the skills directory

## Basic Usage

### Step 1: Invoke the Skill
```
olaf test create skill
```

The skill will automatically run with default settings:
- Full test scope
- Automatic cleanup enabled
- Standard test skill name

### Step 2: Monitor Test Execution
The skill will provide progress updates as it executes:
- Template access validation
- Parameter collection tests
- Component handling tests
- Schema validation tests
- Reindexing functionality tests
- Error handling tests

### Step 3: Review Results
After execution, you'll receive:
- Test summary with pass/fail counts
- Detailed results for each test category
- Regression report if issues detected
- Cleanup confirmation

## Advanced Usage

### Custom Test Scope
To run only basic tests:
```
olaf test create skill
```
Then specify: `test_scope: "basic"`

### Preserve Test Artifacts
To keep test files for inspection:
```
olaf test create skill
```
Then specify: `cleanup_after: false`

### Custom Test Skill Name
To use a specific test skill name:
```
olaf test create skill
```
Then specify: `test_skill_name: "my-custom-test"`

## Understanding Test Results

### Success Indicators
- ✅ All tests passed
- No regressions detected
- Clean test artifact removal
- Schema compliance validated

### Failure Indicators
- ❌ Specific test failures reported
- Regression details provided
- Error conditions documented
- Remediation steps suggested

## Troubleshooting

### Common Issues

**Template Access Errors**
- Verify `~/templates/` exists
- Check file permissions on template files
- Confirm templates contain expected content

**Directory Permission Errors**
- Verify write access to skills directory
- Check competencies directory permissions
- Ensure test workspace can be created

**Schema Validation Failures**
- Review create-skill template structure
- Verify manifest generation logic
- Check for schema definition changes

### Getting Help

If tests fail consistently:
1. Review the detailed error messages
2. Check the specific failure conditions
3. Validate your OLAF framework installation
4. Consult with the OLAF development team

## Best Practices

### Regular Testing
- Run regression tests before framework releases
- Execute tests after any create-skill modifications
- Include testing in CI/CD pipelines

### Test Environment
- Always test in isolated environments
- Use cleanup to prevent artifact accumulation
- Preserve evidence when investigating failures

### Documentation
- Document any recurring test failures
- Track regression patterns over time
- Share results with the development team

## Next Steps

After successful testing:
- Consider the create-skill functionality validated
- Document any improvements needed
- Schedule next regression test cycle
- Update test scenarios if new features added