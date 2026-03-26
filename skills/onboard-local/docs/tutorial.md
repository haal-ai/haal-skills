# onboard-local

> Step-by-step tutorial for local codebase onboarding

## Prerequisites
- A codebase with established patterns to analyze
- No network or authentication required

## Estimated Time
10–20 minutes

## Step-by-Step Instructions

### Step 1: Invoke the Skill
> "Onboard this project locally"

The skill starts with an introduction explaining the process.

### Step 2: Stack Detection
The skill automatically identifies:
- Programming languages used
- Frameworks and libraries
- Build tools and package managers
- Testing frameworks
- Project structure patterns

### Step 3: Core Analysis
The codebase is scanned (read-only) for:
- Naming conventions
- Error handling patterns
- Testing approaches
- File organization patterns
- Common anti-patterns

Each finding includes file-path evidence.

### Step 4: Review Draft Standards
Up to 5 standards are proposed based on detected patterns. Each includes:
- Standard name and description
- Scope (file patterns)
- Rules with code examples
- Source evidence (file paths)

Review and request changes or approve.

### Step 5: Review Draft Commands
Up to 5 reusable commands are proposed. Each includes:
- Command name and description
- What it does
- When to use it

### Step 6: Approve and Save
Confirm to write standards and commands to `.olaf/data/practices/`.

### Step 7: Registry Conversion (Optional)
Convert generated items to HAAL registry format for sharing across projects.

## Troubleshooting

| Issue | Solution |
|-------|----------|
| Too few patterns detected | Point to specific example files |
| Wrong stack detected | Correct the detection and re-analyze |
| Standards too generic | Provide more context about your conventions |
| Commands don't fit workflow | Request specific command types |

## Verification Checklist
- [ ] Stack correctly detected
- [ ] Standards backed by evidence (file references)
- [ ] Commands are useful and accurate
- [ ] Drafts reviewed and approved
- [ ] Files saved in `.olaf/data/practices/`
