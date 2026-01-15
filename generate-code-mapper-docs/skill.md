---
name: generate-code-mapper-docs
description: Workflow skill that guides the user to run OLAF code-mapper foundation analysis and contextual reads, then uses the generated artifacts to produce structured technical project documentation.
license: Apache-2.0
---

<olaf>

if you are in need to get the date and  time, use time tools, fallback to shell command if needed

**MANDATORY**: before doing anything else, read fully the `.olaf/team-delegation.md` file and apply its requirements strictly.

# Generate Code-Mapper Documentation

You WILL act as a workflow skill that generates structured technical documentation for a codebase using OLAF code-mapper outputs. You MUST keep the Python scripts and tooling in the existing `scripts/code-mapper` area and reference them, not duplicate them.

## Goal

You WILL help the user:
- Run code-mapper foundation analysis on a target repository.
- Inspect the structural and index outputs produced by code-mapper.
- Perform contextual reads for key entry points.
- Produce a consistent technical documentation file set following `templates/project-documentation-structure.md`.

## Workflow

### 1. Collect Inputs

You MUST ask the user for:
- `project_path`: absolute path or **workspace-root–relative** path to the repository under analysis (for example: `your-repos/desktoptransactions/JFXATCServices`).
- `code_mapper_path`: path to the OLAF code-mapper scripts **relative to the workspace root**. The default is `scripts/code-mapper`.
- Optional: target output location if different from the default `.olaf/work/staging/code-mapper/<repo-name>/` **under the workspace root**.

You MUST validate that:
- `project_path` is non-empty and clearly identifies a directory (absolute or workspace-root–relative).
- `code_mapper_path` is non-empty.

### 2. Run Foundation Analysis (User-Facing Instructions)

You WILL instruct the user to run the foundation analysis using the existing code-mapper `run.py` script from the **workspace root** (the directory that contains the `.olaf/` folder). You MUST NOT copy or recreate that script.

You WILL present the following command, with placeholders replaced by the user-provided paths:

```bash
cd <workspace-root>
python <code-mapper-path>/run.py --foundation-lite <project-path>
```

Where:
- `workspace-root` is the directory that contains the `.olaf/` folder.
- `project-path` is the absolute or workspace-root–relative path to the repository under analysis.

You WILL explain that:
- The analysis inspects build files, project structure, and code indexes.
- The output will be written under:
  `.olaf/work/staging/code-mapper/<repo-name>/` inside the workspace root.
 - Before asking the user to run this command, you WILL check whether the expected foundation output files (for example: `structural-files.md`, `project-structure.md`, `code-index.md`) already exist in the resolved output directory (default or user-specified).
   - If these files already exist, you WILL explicitly ask the user whether they want to **reuse the existing outputs** or **rerun the foundation analysis and overwrite** them.
   - Only if the user clearly chooses to rerun/overwrite, you WILL instruct them to run the foundation command again; otherwise you WILL proceed using the existing outputs.

### 3. Inspect Generated Artifacts

You WILL guide the user to open and review the generated files in this order:

1. `structural-files.md`
   - Identify all build files (for example: `package.json`, `pom.xml`, `requirements.txt`, `go.mod`, etc.).
   - Treat each build file as defining one tool/application.
   - Capture for each item: build file path, root directory, and likely application name.

2. `project-structure.md`
   - Understand the high-level directory layout.
   - Note languages, major modules, and integration points.

3. `code-index.md`
   - For each relevant file, see key classes, functions, and imports.

You WILL synthesize this information into a mental model of the repository.

### 4. Contextual Reads for Entry Points

For each tool/application identified from the build files, you WILL:

1. Ask the user to identify or confirm the main entry file and main function (if applicable).
2. Instruct the user to run code-mapper contextual reads using the existing script, always in one of the supported formats:

   - **Symbol mode (`FILE:SYMBOL`)** – symbol name MUST match a definition printed under "Available symbols in this file":

```bash
python <code-mapper-path>/run.py --contextual-read "path/to/MainEntry.java:MainEntry"
```

   - **Line-range mode (`FILE:START-END`)** – when symbol names are ambiguous or not known:

```bash
python <code-mapper-path>/run.py --contextual-read "path/to/MainEntry.java:1-200"
```

3. Use the resulting contextual read output to understand:
   - How the application starts up.
   - Key dependencies and integration points.
   - Major flows or responsibilities.

You MUST keep all script execution instructions external; you NEVER duplicate or embed code-mapper’s Python code here.

### 5. Generate Documentation

You WILL generate structured technical documentation for the repository using the `templates/project-documentation-structure.md` template.

You MUST:
- Follow the sections and headings from `templates/project-documentation-structure.md`.
- Populate each section using:
  - structural-files summary (tools/applications and their build files),
  - project-structure overview,
  - code-index highlights,
  - contextual-read findings for each main entry point.
- Use clear, concise technical language suitable for developers and maintainers.

You MUST include at minimum:
- Overview of tools/services in the repository.
- Table of entry points with build file, entry file/function, and short purpose.
- Technology stack summary (languages, frameworks, build tools).
- Architecture overview (modules, interactions, major flows).
- Infrastructure overview (CI/CD, containerization, deployment) if such information is visible from the repo.

You WILL explicitly reference the template:

> Use the output format defined in `templates/project-documentation-structure.md`.

### 6. Error Handling and Edge Cases

You MUST handle these situations explicitly:

- **Missing code-mapper outputs**: If `structural-files.md`, `project-structure.md`, or `code-index.md` are missing, you WILL:
  - Ask the user to confirm that foundation analysis was run successfully.
  - Suggest re-running the foundation step if needed.

- **No build files detected**: If no build files are listed:
  - You WILL document that the repository does not expose standard build files.
  - You WILL fall back to directory and code index analysis for structure and entry points.

- **Unclear entry points**: If entry points cannot be determined:
  - You WILL state the ambiguity in the documentation.
  - You WILL propose likely candidates based on the index (for example: files named `main.*`, `app.*`, `server.*`).

- **Partial infrastructure visibility**: If CI/CD or deployment files are missing or incomplete:
  - You WILL document what is known.
  - You WILL mark unknown aspects explicitly instead of guessing.

### 7. Success Criteria

You WILL consider the documentation generation successful when:
- A complete document following `templates/project-documentation-structure.md` has been produced.
- Each identified tool/application has a documented entry point (or a clear note if ambiguous).
- The technology stack is described with languages and key frameworks.
- Architecture and infrastructure sections are populated with the best available information from code-mapper outputs.

### 8. Output Expectations

You WILL output **in the assistant response**:
- A single markdown document that follows the `templates/project-documentation-structure.md` structure.
- Optional short summary of assumptions or limitations (for example: “CI/CD configuration inferred from GitHub Actions workflows only”).

You WILL THEN:
- Propose auto-saving this document to a sensible default path in the code-mapper staging area, for example:  
  `.olaf/work/staging/code-mapper/<repo-name>/project-documentation.md`.
- Ask the user to confirm or override this target path.

Only AFTER explicit user confirmation, you MAY perform the save operation to the confirmed path (or instruct the caller/tool to do so). If the user declines, you MUST leave the document as response-only output.
