# Onboard Me - Tutorial

## Quick Start

### Basic Usage

```
olaf onboard me
```

This will:
1. Analyze the current repository
2. Detect relevant developer personas
3. Generate persona-focused quick start guides
4. Create an overview index file

### Example Session

```
You: olaf onboard me

Copilot:
[*] Analyzing repository...
[*] Detected: TypeScript/React frontend + Python/FastAPI backend
[*] Identified personas: Frontend Developer, Backend Developer, QA Engineer, Architect
[*] Generating guides...

✓ Created: .olaf/data/product/context/my-app/QUICKSTART-FRONTEND-DEVELOPER.md
✓ Created: .olaf/data/product/context/my-app/QUICKSTART-BACKEND-DEVELOPER.md
✓ Created: .olaf/data/product/context/my-app/QUICKSTART-QA-ENGINEER.md
✓ Created: .olaf/data/product/context/my-app/QUICKSTART-ARCHITECT.md
✓ Created: .olaf/data/product/context/my-app/QUICKSTART-OVERVIEW.md

Onboarding guides ready! Share QUICKSTART-OVERVIEW.md with new team members.
```

## Step-by-Step Guide

### Step 1: Run Analysis

The skill automatically runs the repository analyzer:

```bash
python skills/onboard-me/tools/analyze-repository.py <repo-path> --output .olaf/work/onboard-me
```

This extracts:
- Languages and frameworks
- Build tools and commands
- Entry points and key files
- Project structure
- Testing setup

### Step 2: Persona Detection

Based on the analysis, the skill detects relevant personas:

**Always Included:**
- Architect (overview & patterns)
- Business Analyst (features & workflows)
- QA Engineer (if tests exist)
- Docs Contributor

**Technology-Specific:**
- Frontend Developer (React/Vue/Angular/Next.js)
- Backend Developer (FastAPI/Django/Flask/Go APIs)
- Mobile Developer (Kotlin/Swift/React Native)
- CLI Tool Developer (CLI frameworks)
- DevOps Engineer (Docker/K8s/Terraform)
- Data Engineer (pandas/Spark/ML frameworks)
- VS Code Extension Developer

### Step 3: Guide Generation

For each persona, generates a structured guide:

**1. What You'll Build** (Goal)
- Concrete, achievable task relevant to persona

**2. Setup (5 min)**
- Clone, install dependencies
- Environment setup

**3. Build & Run (5 min)**
- Build commands
- Run/start commands
- Verification steps

**4. Understand the Code (10 min)**
- Key files for this persona
- Relevant directories
- Architecture diagrams (when needed)

**5. Make Your First Change (10 min)**
- Specific file to modify
- Exact changes to make
- Test commands to verify

**6. Common Tasks**
- Frequently needed commands
- Development workflows
- Troubleshooting tips

### Step 4: Output

Guides are saved to:
```
.olaf/data/product/context/<repo-name>/
├── QUICKSTART-OVERVIEW.md
├── QUICKSTART-FRONTEND-DEVELOPER.md
├── QUICKSTART-BACKEND-DEVELOPER.md
├── QUICKSTART-QA-ENGINEER.md
└── ...
```

## Advanced Usage

### Analyze Specific Repository

```
olaf onboard me /path/to/other/repo
```

### Customize Output Location

Edit the prompt or analyzer script to change output directory (default: `.olaf/data/product/context/<repo-name>/`)

### Re-run Analysis

Simply run `olaf onboard me` again - it will regenerate all guides with updated information.

## Understanding the Output

### QUICKSTART-OVERVIEW.md

Index file listing all generated guides with:
- Quick links to each persona guide
- Repository overview
- General setup instructions

### Persona Guides

Each `QUICKSTART-<PERSONA>.md` contains:
- **30-minute structure**: Designed for immediate productivity
- **Concrete examples**: Actual file paths and commands from your repo
- **First task**: Safe, testable modification to build confidence
- **Common tasks**: Copy-paste ready commands for daily work

## Tips & Best Practices

### For Repository Owners

1. **Keep setup simple**: Ensure install/build commands work on fresh clone
2. **Document entry points**: Clear main files help the analyzer
3. **Include tests**: Enables QA Engineer persona generation
4. **Use standard tools**: Standard package managers detected automatically

### For New Team Members

1. **Start with OVERVIEW**: Get the big picture first
2. **Pick your persona**: Use the guide matching your role
3. **Follow the 30-min plan**: Complete sections in order
4. **Do the first task**: Builds confidence with a quick win
5. **Bookmark common tasks**: Reference section saves time daily

### For Maintainers

- **Regenerate periodically**: Run when build process changes
- **Validate guides**: Test with actual new team members
- **Customize if needed**: Guides are markdown, easy to edit
- **Share OVERVIEW link**: Perfect for README or onboarding docs

## Common Scenarios

### Scenario 1: Monorepo

The analyzer detects multiple modules and generates personas for each tech stack found.

### Scenario 2: Legacy Codebase

Even without modern build tools, the skill extracts structure and creates guides based on detected patterns.

### Scenario 3: Multiple Languages

Generates personas for each language ecosystem (e.g., Frontend + Backend + Data Pipeline).

### Scenario 4: Microservices

Run on each service repository or on parent repo - adapts to structure.

## Troubleshooting

**No personas detected?**
- Ensure repository has source code files (not just config)
- Check that `.git` directory exists (for analysis)

**Missing commands in guides?**
- Verify `package.json`, `requirements.txt`, `go.mod`, etc. exist
- Standard build files help the analyzer find commands

**Guides too generic?**
- More structured code = better analysis
- Clear entry points improve quality
- Standard project layout helps detection

## Next Steps

After generating guides:

1. **Review**: Check accuracy of detected tech stack
2. **Test**: Have a new team member try a guide
3. **Refine**: Edit generated markdown if needed
4. **Share**: Add link to OVERVIEW in your README
5. **Maintain**: Regenerate when major changes occur
