# Tutorial: onboard-me

## Introduction

This tutorial guides you through using the `onboard-me` skill to generate persona-focused onboarding documentation for any repository. You'll learn how to analyze a codebase and create tailored quickstart guides that help developers become productive in 30 minutes.

## Prerequisites

Before starting, ensure you have:
- Python installed (for the repository analyzer tool)
- Access to the target repository
- Write permissions to create output files

## Step-by-Step Instructions

### Step 1: Identify the Target Repository

Determine the repository you want to generate onboarding guides for:

```bash
# Example: Your project directory
/path/to/my-project

# Or the current workspace
./
```

### Step 2: Run the Skill

Invoke the onboard-me skill:

```
Execute onboard-me for repository: /path/to/my-project
```

The skill will automatically:
1. Run the repository analyzer
2. Detect applicable personas
3. Generate all quickstart guides

### Step 3: Repository Analysis

The skill runs the analyzer tool:

```bash
python ./onboard-me/tools/analyze-repository.py /path/to/my-project --output /path/to/my-project/.olaf/work/onboard-me
```

This generates `repository-analysis.json` containing:
- Detected languages and frameworks
- Available commands (install, build, run, test)
- Entry points and key files
- Architecture information

### Step 4: Review Detected Personas

Based on the analysis, the skill detects relevant personas. For example, a TypeScript React project might detect:

- Frontend Developer (TypeScript + React)
- QA Engineer (has tests)
- Architect (always included)
- Business Analyst (always included)
- Docs Contributor (always included)

### Step 5: Guide Generation

The skill generates a quickstart guide for each persona. Each guide follows this structure:

```markdown
# my-project - Frontend Developer Quick Start

[(Back to Overview)](./QUICKSTART-OVERVIEW.md)

**Get productive in 30 minutes**

## What You'll Build
[Concrete task matching the persona]

## Your First 30 Minutes

### 1. Setup (5 min)
[Install commands]

### 2. Build & Run (5 min)
[Build and run commands with verification]

### 3. Understand the Code (10 min)
[Key files and architecture diagram]

### 4. Make Your First Change (10 min)
[Specific, testable modification task]

## Common Tasks
[Frequently needed commands]

## Development Workflow
[Git workflow and testing]

## Debugging
[Debug approaches and common issues]

## Resources
[Links to documentation]
```

### Step 6: Review Generated Files

Check the output directory:

```
.olaf/data/product/context/my-project/
├── QUICKSTART-OVERVIEW.md
├── QUICKSTART-FRONTEND-DEVELOPER.md
├── QUICKSTART-ARCHITECT.md
├── QUICKSTART-BUSINESS-ANALYST.md
├── QUICKSTART-QA-ENGINEER.md
└── QUICKSTART-DOCS-CONTRIBUTOR.md
```

### Step 7: Verify the Overview

Open `QUICKSTART-OVERVIEW.md` to see:
- Links to all generated guides
- Repository snapshot (languages, frameworks)
- General setup commands
- Decision tree for choosing a guide

### Step 8: Customize if Needed

The generated guides use real data from your repository. You may want to:
- Add project-specific context
- Update commands if they differ from detected ones
- Add team-specific workflows

## Verification Checklist

After running the skill, verify:

- [ ] `repository-analysis.json` was created in `.olaf/work/onboard-me/`
- [ ] `QUICKSTART-OVERVIEW.md` exists and links to all guides
- [ ] Each persona guide has the "Back to Overview" link
- [ ] Commands in guides are accurate and copy-pasteable
- [ ] Mermaid diagrams render correctly (for Architect/Business Analyst guides)
- [ ] Key files referenced in guides actually exist

## Troubleshooting

### Analyzer Tool Fails

**Symptom**: Error running analyze-repository.py

**Solution**:
1. Verify Python is installed: `python --version`
2. Check the repository path exists
3. Ensure write permissions for output directory
4. Review error message for specific issues

### Missing Personas

**Symptom**: Expected persona not detected

**Solution**:
1. Check `repository-analysis.json` for detected technologies
2. Verify the detection rules match your stack
3. The skill always includes Architect, Business Analyst, and Docs Contributor

### Incorrect Commands

**Symptom**: Generated commands don't work

**Solution**:
1. Review `repository-analysis.json` commands section
2. The analyzer detects commands from package.json, Makefile, etc.
3. Manually update guides if commands differ

### Guides Not Regenerating

**Symptom**: Old content persists after re-running

**Solution**:
1. The skill overwrites existing files by design
2. Check file permissions
3. Verify you're running against the correct repository

### Diagrams Not Rendering

**Symptom**: Mermaid diagrams show as code blocks

**Solution**:
1. Ensure your Markdown viewer supports Mermaid
2. GitHub and VS Code render Mermaid natively
3. Check diagram syntax for errors

## Next Steps

After generating onboarding guides:

- **Share with team**: Distribute guides to new team members
- **Iterate**: Update guides based on feedback
- **Automate**: Run periodically to keep guides current
- **Extend**: Add project-specific sections as needed

## Tips for Success

1. **Run on complete repositories**: The analyzer works best with full codebases
2. **Check detected commands**: Verify install/build/test commands are accurate
3. **Review architecture diagrams**: Ensure they reflect actual system design
4. **Update after major changes**: Regenerate guides when architecture evolves
5. **Customize for your team**: Add team-specific workflows and conventions
