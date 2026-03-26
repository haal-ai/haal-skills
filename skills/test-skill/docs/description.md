# test-skill

## Overview
A test fixture skill that exists only on the `test` branch to validate multi-registry merging in the HAAL installer.

## Purpose
Verify that the installer correctly merges skills from secondary repositories (branches) alongside the main registry. When both `main` and `test` branches are loaded, this skill should appear in the catalog.

## Key Features
- Test-only fixture (no production use)
- Validates multi-registry merge behavior
- Proves secondary repos are loaded correctly

## Usage
This skill is not invoked directly. It exists to:
1. Be present on the `test` branch
2. Appear in the installer catalog when `test` branch is loaded
3. Confirm merge logic works correctly

## Parameters
None — this is a test fixture.

## Process Flow
1. Installer loads `main` branch skills
2. Installer loads `test` branch skills
3. This skill appears in the merged catalog
4. Merge behavior is validated

## Output
No output — presence in the catalog is the validation.

## Related Skills
None — standalone test fixture.
