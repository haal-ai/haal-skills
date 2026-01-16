# Scaffold Quarkus Microservice - Tutorial

## Quick Start

### Step 1: Invoke the Skill

```
olaf scaffold quarkus microservice
```

Common alias (typo-tolerant):

```
olaf scaffold qurkus microservice
```

### Step 2: Provide Baseline Inputs

At minimum, provide:
- `service_name`

Example:

```
service_name: billing
```

### Step 3: Approve the Proposed Scaffold

The skill will propose:
- Output directory (default: `apps/{service_name}`)
- `groupId`, `artifactId`, and base package
- Minimal Quarkus extensions set
- Build/run/test commands

You approve with:

```
Proceed with scaffolding? yes
```

## Example Session

**User**: olaf scaffold quarkus microservice for a "billing" REST service

**Skill response** (high level):
- Loads practices
- Verifies worktree + branch safety
- Proposes Maven + Java 17 + minimal extensions
- After approval, scaffolds a runnable Quarkus project
- Suggests a commit message for the scaffold

## Tips

- Keep the first scaffold minimal; add DB/messaging only when requirements are explicit.
- Commit right after the scaffold is runnable and tests are green.
- If your org has naming standards, provide `group_id` and `base_package` up front.
