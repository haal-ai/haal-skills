---
name: conventional-commits
description: Configure Cascade to use conventional commit prefixes for better commit message organization
---

# Conventional Commit Configuration for Cascade

## Commit Message Categories

When generating commit messages, Cascade should automatically prepend appropriate conventional commit prefixes based on the type of changes:

### **feat:** - New Features
- Adding new functionality
- New skills or capabilities
- New user-facing features

### **fix:** - Bug Fixes
- Fixing broken functionality
- Resolving issues or errors
- Correcting unexpected behavior

### **docs:** - Documentation
- Updating README files
- Adding or modifying skill documentation
- Changing comments or docstrings

### **style:** - Code Style
- Formatting changes (indentation, spacing)
- Code style improvements without logic changes
- Linting fixes

### **refactor:** - Code Refactoring
- Restructuring code without changing functionality
- Improving code organization
- Optimizing performance without API changes

### **chore:** - Maintenance
- Updating dependencies
- Build process changes
- Configuration updates
- Routine maintenance tasks

### **test:** - Testing
- Adding new tests
- Modifying existing tests
- Improving test coverage

### **perf:** - Performance
- Performance optimizations
- Speed improvements
- Memory usage optimizations

### **ci:** - Continuous Integration
- CI/CD pipeline changes
- Build system updates
- Deployment configurations

## Automatic Prefix Detection Rules

Cascade should analyze the changes and automatically select the most appropriate prefix:

1. **If changes include .md files** → Use `docs:`
2. **If changes include skill.md files** → Use `docs:` or `feat:` for new skills
3. **If changes include Python scripts** → Analyze content:
   - Bug fixes → `fix:`
   - New functions → `feat:`
   - Code restructuring → `refactor:`
   - Style/formatting → `style:`
4. **If changes include configuration files** → Use `chore:`
5. **If changes include test files** → Use `test:`
6. **If changes include build/deployment files** → Use `ci:` or `chore:`

## Examples

**Before:** "Update the API consistency analysis skill"
**After:** `docs: update API consistency analysis skill documentation`

**Before:** "Fix the layout resolution in PowerPoint generation"
**After:** `fix: resolve layout resolution issues in PowerPoint generation`

**Before:** "Add visual enhancements to presentation slides"
**After:** `feat: add enhanced visual elements to presentation generation`

**Before:** "Clean up import statements and formatting"
**After:** `style: clean up imports and code formatting`

## Implementation Notes

- Always use lowercase prefixes
- Add a space after the colon
- Keep the original commit message after the prefix
- For multiple types of changes, use the most significant type
- When in doubt, ask the user for clarification

This configuration ensures consistent, professional commit messages that follow industry best practices and improve repository maintainability.
