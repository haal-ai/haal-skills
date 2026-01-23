# Tutorial: Generate Code-Mapper Documentation

This tutorial shows how to use the **Generate Code-Mapper Documentation** skill end to end.

## 1. Prerequisites

- A local clone of the target repository.
- OLAF code-mapper scripts available (by default under `scripts/code-mapper`).
- Python environment capable of running `run.py`.

## 2. Run Foundation Analysis

From your terminal:

```bash
cd <project-path>
python <code-mapper-path>/run.py --foundation-lite .
```

- Replace `<project-path>` with the repository root.
- Replace `<code-mapper-path>` with the path to the code-mapper scripts.

The analysis will write outputs under:

```text
.olaf/work/staging/code-mapper/<repo-name>/
```

## 3. Review Generated Files

Open the following files in order:

1. `structural-files.md`
   - List all build files and map them to tools/applications.

2. `project-structure.md`
   - Understand the high-level directory and module layout.

3. `code-index.md`
   - Inspect key classes, functions, and imports per file.

## 4. Run Contextual Reads (Optional but Recommended)

For each tool/application, identify the main entry file and main function if applicable, then run:

```bash
python <code-mapper-path>/run.py --contextual-read "path/to/main.py:main_function"
```

Use the contextual-read outputs to refine your understanding of startup flow and interactions.

## 5. Invoke the Skill

In your OLAF-enabled environment, call the **Generate Code-Mapper Documentation** skill (for example via `olaf create-skill`-style wiring or direct skill invocation), then provide:

- `project_path`
- `code_mapper_path`

The skill will guide you through using the existing artifacts and produce a documentation draft.

## 6. Use the Documentation Template

The generated documentation will follow the structure defined in:

```text
/templates/project-documentation-structure.md
```

You can copy the final markdown into your repository documentation (for example: `docs/project-overview.md`) or internal knowledge base.
