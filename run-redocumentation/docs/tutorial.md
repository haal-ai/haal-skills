# Tutorial: run-redocumentation

## Introduction

This tutorial guides you through using the `run-redocumentation` skill to execute systematic redocumentation of a complex application. By the end, you'll understand how to set up and run a multi-step documentation workflow with progress tracking.

## Prerequisites

Before starting, ensure you have:

- [ ] Source code accessible in `your-repos/{project-name}/`
- [ ] Staging directory created at `.olaf/work/staging/{project-name}/`
- [ ] Orchestrator plan file created
- [ ] Progress tracker file initialized
- [ ] OLAF framework loaded

## Step-by-Step Instructions

### Step 1: Set Up Project Structure

Create the required directory structure for your documentation project.

**Action:** Create the staging directories.

```bash
# Create staging structure
mkdir -p .olaf/work/staging/my-project/artifacts
mkdir -p .olaf/work/staging/my-project/carry-overs

# Ensure source code is accessible
ls your-repos/my-project/
```

**Expected Structure:**
```
.olaf/work/staging/my-project/
├── artifacts/
│   ├── redocument-my-project-orchestrator.md  (to create)
│   └── redocument-my-project-progress.md      (to create)
└── carry-overs/

your-repos/my-project/
├── src/
├── tests/
└── ...
```

### Step 2: Create the Orchestrator Plan

Define the sequence of documentation steps.

**Action:** Create the orchestrator file.

**File:** `.olaf/work/staging/my-project/artifacts/redocument-my-project-orchestrator.md`

```markdown
# Redocumentation Orchestrator: my-project

## Overview
Systematic redocumentation of the my-project application.

## Steps

### Step 1: Repository Structure Analysis
- Competency: analyze-repo-structure
- Target: your-repos/my-project/
- Output: Repository structure documentation

### Step 2: API Endpoint Documentation
- Competency: document-api-endpoints
- Target: your-repos/my-project/src/api/
- Output: API documentation

### Step 3: Data Model Documentation
- Competency: document-data-models
- Target: your-repos/my-project/src/models/
- Output: Data model documentation

### Step 4: Integration Points Analysis
- Competency: analyze-integrations
- Target: your-repos/my-project/
- Output: Integration documentation

### Step 5: Final Review and Consolidation
- Competency: consolidate-documentation
- Target: All previous artifacts
- Output: Consolidated documentation package
```

### Step 3: Initialize Progress Tracker

Create the progress tracking file.

**Action:** Create the progress file.

**File:** `.olaf/work/staging/my-project/artifacts/redocument-my-project-progress.md`

```markdown
# Redocumentation Progress: my-project

## Session Information
- Project: my-project
- Started: 20260116-0900
- Last Updated: 20260116-0900

## Overall Progress
- Total Steps: 5
- Completed: 0
- In Progress: 0
- Pending: 5

## Step Status

### Step 1: Repository Structure Analysis
- Status: Pending
- Started: -
- Completed: -
- Artifacts: -
- Notes: -

### Step 2: API Endpoint Documentation
- Status: Pending
- Started: -
- Completed: -
- Artifacts: -
- Notes: -

### Step 3: Data Model Documentation
- Status: Pending
- Started: -
- Completed: -
- Artifacts: -
- Notes: -

### Step 4: Integration Points Analysis
- Status: Pending
- Started: -
- Completed: -
- Artifacts: -
- Notes: -

### Step 5: Final Review and Consolidation
- Status: Pending
- Started: -
- Completed: -
- Artifacts: -
- Notes: -
```

### Step 4: Invoke the Skill

Start the redocumentation workflow.

**Action:** Invoke the skill.

```
Skill: run-redocumentation
```

**Expected Response:**

```
Reviewing current progress for: my-project

Orchestrator: .olaf/work/staging/my-project/artifacts/redocument-my-project-orchestrator.md
Progress: .olaf/work/staging/my-project/artifacts/redocument-my-project-progress.md

Current Status:
- Total Steps: 5
- Completed: 0
- Next Step: Step 1 - Repository Structure Analysis

Applying Fresh Assessment Protocol...
- Will analyze source code directly
- Will NOT read previous analysis documents
- Will generate NEW insights

Proceeding with Step 1: Repository Structure Analysis
```

### Step 5: Execute Documentation Step

The skill executes the current step using fresh assessment.

**What Happens:**

1. **Load Competency:** The appropriate OLAF competency is loaded
2. **Direct Analysis:** Source code is analyzed directly (not previous docs)
3. **Generate Artifacts:** New documentation is created
4. **Update Progress:** Progress tracker is updated

**Example Output:**

```
Executing Step 1: Repository Structure Analysis

Fresh Assessment - Analyzing:
- your-repos/my-project/src/
- your-repos/my-project/tests/
- your-repos/my-project/config/

Findings:
- 3 main modules identified: api, core, utils
- 47 source files analyzed
- Test coverage: 23 test files found
- Configuration: 5 config files

Generating artifact: repository-structure.md

Step 1 completed successfully.
```

### Step 6: Review Progress Update

The progress tracker is automatically updated.

**Updated Progress File:**

```markdown
### Step 1: Repository Structure Analysis
- Status: Completed
- Started: 20260116-0915
- Completed: 20260116-0932
- Artifacts: .olaf/work/staging/my-project/artifacts/repository-structure.md
- Notes: 47 source files, 3 modules, 23 test files
```

### Step 7: Review Carry-Over File

A carry-over file is generated for session continuity.

**File:** `.olaf/work/staging/my-project/carry-overs/carry-over-20260116-0932.txt`

```
# Carry-Over: my-project Redocumentation
Generated: 20260116-0932

## Completed Step
Step 1: Repository Structure Analysis
- Duration: 17 minutes
- Artifacts generated: repository-structure.md
- Key findings: 3 modules (api, core, utils), 47 source files

## Next Step
Step 2: API Endpoint Documentation
- Competency: document-api-endpoints
- Target: your-repos/my-project/src/api/
- Prerequisites: Step 1 complete ✓

## Context for Continuation
- Repository structure documented
- API module identified at src/api/
- Ready to proceed with API documentation

## Key Artifacts
- .olaf/work/staging/my-project/artifacts/repository-structure.md
```

### Step 8: Continue to Next Step

Invoke the skill again to continue.

**Action:** Run the skill for the next step.

```
Skill: run-redocumentation
```

**Expected Response:**

```
Reviewing current progress for: my-project

Current Status:
- Total Steps: 5
- Completed: 1
- Next Step: Step 2 - API Endpoint Documentation

Proceeding with Step 2...
```

### Step 9: Complete All Steps

Repeat the process until all steps are complete.

**Final Progress:**

```markdown
## Overall Progress
- Total Steps: 5
- Completed: 5
- In Progress: 0
- Pending: 0

Status: COMPLETE
```

## Verification Checklist

After completing the redocumentation workflow, verify:

- [ ] All steps in orchestrator plan executed
- [ ] Progress tracker shows all steps completed
- [ ] Artifacts generated for each step
- [ ] Carry-over files created for each session
- [ ] Fresh assessment methodology followed (direct source analysis)
- [ ] No synthesis from previous analysis documents
- [ ] Quality gates validated at each step

## Troubleshooting

### Issue: Orchestrator Plan Not Found

**Symptom:** Skill cannot locate orchestrator file.

**Solution:**
- Verify file exists at expected path
- Check naming convention: `redocument-{project-name}-orchestrator.md`
- Ensure staging directory structure is correct

### Issue: Progress Tracker Corrupted

**Symptom:** Skill reports parsing errors.

**Solution:**
- Back up current progress file
- Recreate with correct Markdown structure
- Manually update completed step statuses

### Issue: Source Code Not Accessible

**Symptom:** Skill cannot analyze target files.

**Solution:**
- Verify source code path in `your-repos/{project-name}/`
- Check file permissions
- Ensure repository is cloned/available

### Issue: Competency Not Found

**Symptom:** Step fails due to missing competency.

**Solution:**
- Verify competency name in orchestrator plan
- Check if competency file exists
- Update orchestrator with correct competency path

## Next Steps

After completing redocumentation:

1. **Review Artifacts:** Examine all generated documentation
2. **Consolidate:** Merge artifacts into final documentation
3. **Publish:** Deploy documentation to appropriate location
4. **Archive:** Store carry-over files for reference
5. **Schedule Updates:** Plan periodic redocumentation cycles
