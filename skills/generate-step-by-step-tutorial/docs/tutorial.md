# generate-step-by-step-tutorial

> Step-by-step tutorial for generating tutorials from conversations and workflows

## Prerequisites
- A completed conversation or workflow file to document
- Clear understanding of the process to capture

## Estimated Time
5–10 minutes

## Step-by-Step Instructions

### Step 1: Choose Your Source
**From current conversation:**
> "Generate a tutorial from this conversation about setting up the CI pipeline"

**From a file:**
> "Create a step-by-step guide from workflows/deploy-process.md"

### Step 2: Name the Workflow
Provide a descriptive name:
> "Workflow name: CI/CD Pipeline Setup for Kubernetes"

### Step 3: Select Language (Optional)
Default is English. Specify another:
> "Generate in French"

### Step 4: Review Extracted Steps
The skill analyzes the source and extracts:
- Sequential steps taken
- Key decisions made
- Commands executed
- Outcomes achieved

Review the extracted steps for accuracy and completeness.

### Step 5: Review the Tutorial Draft
A structured tutorial is presented with:
- Title and description
- Prerequisites
- Numbered steps with explanations
- Expected outcomes for each step
- Troubleshooting tips

### Step 6: Approve and Save
Confirm to save the tutorial file.

## Troubleshooting

| Issue | Solution |
|-------|----------|
| Steps are out of order | Rearrange during the review phase |
| Missing important steps | Point to specific parts of the source |
| Too much detail | Request a more concise version |
| Wrong language | Specify the target language explicitly |

## Verification Checklist
- [ ] Source material validated
- [ ] Steps accurately capture the workflow
- [ ] Prerequisites are listed
- [ ] Each step has clear instructions
- [ ] Tutorial saved with timestamp
