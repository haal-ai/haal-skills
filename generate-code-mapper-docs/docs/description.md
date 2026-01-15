# Generate Code-Mapper Documentation

This skill generates structured technical documentation for a codebase using the outputs of the OLAF code-mapper scripts.

It guides you to:
- Run the `run.py --foundation-lite` analysis on a target repository.
- Inspect the structural, project-structure, and code-index artifacts under `.olaf/work/staging/code-mapper/<repo-name>/`.
- Perform contextual reads for key entry points in each application or tool.
- Produce a consistent documentation artifact using the `templates/project-documentation-structure.md` template.

The code-mapper Python scripts remain in their existing location; this skill only orchestrates how to use them and how to transform their outputs into documentation.
