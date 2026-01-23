---
name: detect-test-directives
description: Analyze repository test patterns and generate documentation for test frameworks, commands, and conventions across multiple languages
license: Apache-2.0
metadata:
  olaf_tags: [testing, analysis, documentation, patterns]
  copyright: Copyright (c) 2026 pjmp020564
  author: pjmp020564 (on github)
  repository: https://github.com/haal-ai/haal-ide
  provider: Haal AI
---

if you are in need to get the date and  time, use time tools, fallback to shell command if needed

## Input Parameters
You MUST request these parameters if not provided by the user. Present them as a numbered list to ease user response:
1. **repo_path**: string - Absolute path to the repository root (REQUIRED)
2. **branch**: string - Branch to analyze; default is currently checked out (OPTIONAL)
3. **os**: string - Assume Windows; produce PowerShell-friendly commands (OPTIONAL)
4. **sample_limit**: number - Number of recent test commits/files to sample (OPTIONAL - default: 30)

## User Interaction
You MUST follow these interaction guidelines:
- Ask for user approval before running commands that download dependencies or execute tests
- Present generated documentation for review before saving
- Provide clear progress updates during repository scanning and analysis
- Confirm destructive operations before executing

## Process

### 1. Validation Phase
- Verify `repo_path` exists and is a Git repository (`git rev-parse --is-inside-work-tree`).
- Detect dominant languages and test frameworks by scanning for well-known files:
  - Java/Kotlin: `pom.xml`, `build.gradle*`, `src/test/java`, `src/test/kotlin`
  - JS/TS: `package.json`, `jest.config.*`, `vitest.config.*`, `cypress.*`
  - Python: `pyproject.toml`, `pytest.ini`, `requirements.txt`
  - Go: `go.mod`, `*_test.go`
  - C/C++: `CMakeLists.txt`, `Makefile`, `meson.build`, `conanfile.*`, `vcpkg.json`, `tests/`, `**/*_test.(c|cc|cpp)`
  - .NET: `*.csproj`, `Directory.Build.props`, `test/*`
- Infer test runner/frameworks from dependency files and configs.

### 2. Execution Phase

#### 2.1 Git-based recent changes (Windows-safe)
- Current branch: `git rev-parse --abbrev-ref HEAD`
- Latest commit overview: `git log -1 --name-status --pretty=fuller`
- Recently changed tests (sample):
  - `git log -n {sample_limit} --name-status --date=short --pretty=format:"%h\t%ad\t%s" -- src/test`
  - If tests are elsewhere, adapt: `test`, `tests`, `__tests__`, `*.test.*`, `*.spec.*`, `**/*_test.go`, `**/*_test.cpp`
- You WILL write an ephemeral `recent-tests-report.md` during the run ONLY to aid analysis.

#### 2.2 Sample tests for pattern analysis
Choose a representative small set:
- Controller/HTTP tests
- Service/component tests
- Utility/pure unit tests
- Integration tests (if present)
Identify patterns ("test directives"):
- Test runner annotations/markers
- Mocking libraries and techniques
- Assertion styles
- Test fixtures/resources
- Naming/structure conventions

#### 2.3 Generate documentation (persistent outputs)
You WILL create/update under `.olaf/data/practices/` using kebab-case filenames:
- `how-to-run-tests.md`
  - Prerequisites (runtime, build tool)
  - Exact commands to run tests and coverage (Windows-friendly)
  - How to run single test/file/case
  - Report locations and useful variations
- `unit-test-patterns.md`
  - Recent change highlights
  - Frameworks/runners and directives
  - Web-layer/testing patterns
  - Mocking patterns, assertions, fixtures
  - Naming/structure and validated code snippets

#### 2.4 Optional: run tests with coverage (requires approval)
- Maven (JUnit): `mvn clean test jacoco:report`
- Gradle (JUnit): `gradlew clean test jacocoTestReport`
- Node.js (Jest): `npm test -- --coverage` or `npx jest --coverage`
- Python (pytest): `pytest --maxfail=1 --disable-warnings --cov --cov-report=html`
- Go: `go test ./... -coverprofile=coverage.out` then `go tool cover -html=coverage.out -o coverage.html`
- C/C++: configure/build/`ctest --output-on-failure`; coverage with `gcovr`/`lcov` (or platform alternatives)
- Artifacts: tool reports and coverage HTML paths should be recorded in the docs.

### 3. Validation Phase
- Confirm docs exist with required sections and stack-accurate commands/snippets.
- Verify `recent-tests-report.md` is deleted at end of run.

## Output Format
- Persistent:
  - `.olaf/data/practices/how-to-run-tests.md`
  - `.olaf/data/practices/unit-test-patterns.md`
- Ephemeral (deleted at end):
  - `recent-tests-report.md`

## User Communication

### Progress Updates
- Progress updates on detection, sampling, doc generation, and cleanup
- Prompt for approval before any command that downloads deps or runs coverage

### Completion Summary
- Summary of detected test frameworks and languages
- Files created/updated with locations
- Coverage report locations (if tests were run)

### Next Steps
- Documentation is ready for use at `.olaf/data/practices/`
- Review generated test commands and patterns
- Consider running tests with coverage for deeper analysis

## Domain-Specific Rules
- You MUST keep persistent practice docs under `.olaf/data/practices/`
- You MUST use kebab-case lowercase filenames for all generated artifacts
- You MUST delete `recent-tests-report.md` after each run
- If legacy files exist with uppercase or underscores (e.g., `HOW_TO_RUN_TESTS.md`, `UNIT_TEST_PATTERNS.md`, `RECENT_TESTS_REPORT.md`), you MUST rename them to kebab-case equivalents and update references:
  - `HOW_TO_RUN_TESTS.md` → `how-to-run-tests.md`
  - `UNIT_TEST_PATTERNS.md` → `unit-test-patterns.md`
  - `RECENT_TESTS_REPORT.md` → `recent-tests-report.md`
- You MUST use Windows-safe commands by default

## Success Criteria
You WILL consider the task complete when:
- [ ] Detected dominant test stack and summarized directives
- [ ] Generated `how-to-run-tests.md` with exact commands and report locations
- [ ] Generated `unit-test-patterns.md` with concrete, repo-specific patterns and snippets
- [ ] Deleted `recent-tests-report.md` at the end of the run
- [ ] User notified of completion with file locations

## Required Actions
1. Validate repository path and detect test frameworks
2. Analyze git history for recent test changes
3. Sample representative tests and extract patterns
4. Generate documentation files in `.olaf/data/practices/`
5. Optionally run tests with coverage (with user approval)
6. Clean up ephemeral files and confirm completion

## Error Handling
- **Missing inputs or unknown test locations**: Request clarification from user
- **Unsupported stack or missing tools**: Propose alternatives or skips
- **Command failures**: Show stderr, propose remediation steps
- **Write failures**: Suggest alternate paths under `.olaf/data/practices/`
