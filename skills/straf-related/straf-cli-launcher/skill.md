---
name: straf-cli-launcher
description: Presents available straf-cli commands, explains what each does, collects required parameters from the user, and then runs the selected command either in background spawn mode or in interactive console mode where the user can see output.
license: Apache-2.0
metadata:
  olaf_protocol: "\"Propose-Confirm-Act\""
---

# STRAF CLI Launcher

## Purpose

Present available `straf-cli` commands, let the user ask what each command does, collect the right input parameters, and then run the chosen command either:
- in **spawn mode** (background process, user continues working), or
- in **interactive mode** (foreground process, user sees console output but does not provide extra input).

`straf-cli` itself uses the default AWS Bedrock profile (`bedrock`) and region (`us-east-1`). The launcher does not override these unless the user explicitly asks for it.

## Commands Catalog

The launcher must know and present at least the following commands from `~/.olaf/core/agentic/straf-cli/cli.py`:

1. **analyze**
   - **Summary**: Multi-step analysis workflow on an input file using specialized subagents.
   - **Typical use**: Analyze a dataset or log file and produce an analysis report.

2. **collaborate**
   - **Summary**: Multi-agent collaboration on a topic and goal, with cross-agent communication.
   - **Typical use**: Have multiple agents brainstorm and align on a solution for a topic/goal.

3. **multi-persona**
   - **Summary**: Multi-persona analysis (developer, tester, architect, business, devops) across a solution directory with multiple repos.
   - **Typical use**: Evaluate a multi-repo solution from several stakeholder perspectives.

4. **team-design**
   - **Summary**: Conversational multi-agent team design around a change request.
   - **Typical use**: Ask a team of agents to discuss and design a feature or change request.

5. **jsdoc-gen**
   - **Summary**: Generate comprehensive inline JSDoc comments for JS/TS sources.
   - **Typical use**: Document JavaScript/TypeScript codebases (already front-ended by `generate-jsdoc`).

6. **doc-external**
   - **Summary**: Generate external documentation (MkDocs structure) from a codebase.
   - **Typical use**: Produce architecture/control-flow/use-case docs (already front-ended by `generate-external-docs`).

7. **web-research**
   - **Summary**: Autonomous web research on a subject given explicit URLs.
   - **Typical use**: Fetch and analyze a set of URLs for a specific subject.

8. **researcher**
   - **Summary**: Agent-driven research workflows with quick vs deep modes.
   - **Typical use**: Perform structured research with configurable depth.

9. **refactor**
   - **Summary**: Iterative code maintainability improvement with cycles.
   - **Typical use**: Refactor a code file across a number of cycles.

10. **document-api**
    - **Summary**: Comprehensive API documentation generation from code (plus tests/specs).
    - **Typical use**: Discover and document REST/SOAP/GraphQL APIs in a repo.

When user asks "what does <command> do?" or similar, answer with the corresponding summary and typical use.

## Parameter Schemas Per Command

Model the parameters based on the CLI parser in `~/.olaf/core/agentic/straf-cli/cli.py`. Treat them as follows (only the important ones are listed; default values come from the CLI):

- **analyze**
  - `file` (REQUIRED, string, path) → `--file`
  - `output` (OPTIONAL, string, path, default `analysis_report.txt`) → `--output`
  - `format` (OPTIONAL, enum: `text|json|html`, default `text`) → `--format`
  - `prompts_file` (OPTIONAL, string, path) → `--prompts-file`

- **collaborate**
  - `topic` (REQUIRED, string) → `--topic`
  - `goal` (REQUIRED, string) → `--goal`
  - `prompts_file` (OPTIONAL, string, path) → `--prompts-file`

- **multi-persona**
  - `solution` (REQUIRED, string, path to solution directory) → `--solution`
  - `output` (OPTIONAL, string, path, default `MULTI_PERSONA_ANALYSIS.md`) → `--output`
  - `prompts_file` (OPTIONAL, string, path) → `--prompts-file`

- **team-design**
  - `request` (REQUIRED, string, change request description) → `--request`
  - `codebase` (OPTIONAL, string, path) → `--codebase`
  - `output` (OPTIONAL, string, path) → `--output`

- **jsdoc-gen**
  - `repo` (REQUIRED, string, path to repository) → `--repo`
  - `output` (OPTIONAL, string, path; if omitted, modifies repo in-place) → `--output`
  - `no_branch` (OPTIONAL, boolean flag; default false) → `--no-branch`
  - `max_files` (OPTIONAL, int, default 10000) → `--max-files`
  - `no_resume` (OPTIONAL, boolean flag) → `--no-resume`

- **doc-external**
  - `root` (REQUIRED, string, path to analysis root) → `--root`
  - `output` (OPTIONAL, string, path, default `./docs`) → `--output`
  - `use_cases` (OPTIONAL, string, path) → `--use-cases`
  - `no_branch` (OPTIONAL, boolean flag) → `--no-branch`
  - `replace_all` (OPTIONAL, boolean flag) → `--replace-all`

- **web-research**
  - `subject` (REQUIRED, string) → `--subject`
  - `urls` (REQUIRED, list of strings; at least one URL) → repeated `--urls`
  - `output` (OPTIONAL, string, path, default `web_research_report.md`) → `--output`
  - `max_links` (OPTIONAL, int, default 5) → `--max-links`

- **researcher**
  - `topic` (REQUIRED, string) → `--topic`
  - `quick` (OPTIONAL, boolean, default false) → `--quick`
  - `deep` (OPTIONAL, boolean, default false, but conceptually the default mode) → `--deep`
  - `scope` (OPTIONAL, string) → `--scope`
  - `outcomes` (OPTIONAL, string) → `--outcomes`
  - `output` (OPTIONAL, string, path) → `--output`

- **refactor**
  - `file` (REQUIRED, string, path to code file) → `--file`
  - `max_cycles` (OPTIONAL, int, default 5) → `--max-cycles`
  - `output_dir` (OPTIONAL, string, path) → `--output-dir`

- **document-api**
  - `repo` (REQUIRED, string, path) → `--repo`
  - `output` (REQUIRED, string, path) → `--output`
  - `doc_folder` (OPTIONAL, string, path) → `--doc-folder`
  - `spec_folder` (OPTIONAL, string, path) → `--spec-folder`
  - `test_folder` (OPTIONAL, string, path) → `--test-folder`
  - `limit` (OPTIONAL, int) → `--limit`
  - `generate` (OPTIONAL, list, choices [`docs`,`tests`,`specs`,`data`,`all`], default [`all`]) → `--generate`

When asking the user for parameters:
- Always collect **required** parameters.
- Offer **optional** parameters one by one with clear defaults and allow the user to skip.

## Execution Modes

The launcher supports two modes when constructing and using `straf-cli` commands:

1. **Spawn mode (background)**
   - Construct a full CLI command, e.g.:
     - `python ~/.olaf/core/agentic/straf-cli/cli.py document-api --repo "..." --output "..."`
   - Clearly label it as "background" / "non-blocking" in the explanation.
   - In environments where you can execute terminal commands, start the process without waiting for completion and report back the command that was launched.
   - In environments without direct command execution, present the exact CLI for the user to run themselves if they want a background process.

2. **Interactive mode (foreground)**
   - Construct the same CLI command string.
   - In environments where you can execute terminal commands, run the command in the foreground and stream or summarize its output.
   - In environments without direct command execution, present the exact CLI and clearly state that running it in the user's terminal will show the live output.

The launcher MUST always ask the user which mode to use:

- Examples of background: "spawn", "run in background", "async", "non-blocking".
- Examples of interactive: "interactive", "foreground", "run here", "show output in console".

If the user does not specify, default to **spawn mode** for long-running tasks (jsdoc-gen, doc-external, document-api, multi-persona, refactor, researcher) and **interactive** for simpler or one-off tasks (analyze, collaborate, web-research, team-design). You may override the default based on explicit user preference in the conversation.

## High-Level Flow

Follow this sequence, always asking for user approval before executing:

1. **Discover and Present Commands**
   - Present the 10 known commands as a numbered list with short descriptions.
   - Allow the user to ask for more detail about any command before making a choice.

2. **User Chooses Command**
   - Accept either the number or the command name (case-insensitive).
   - Confirm the choice back to the user.

3. **Gather Parameters**
   - For the chosen command, iterate through the parameter schema:
     - Ask for all REQUIRED parameters.
     - For each OPTIONAL parameter:
       - Briefly explain what it is.
       - Propose a default (if any).
       - Ask if the user wants to set it or keep the default/skip.
   - Validate obvious issues (e.g., empty required values).

4. **Choose Execution Mode**
   - Ask explicitly whether to use spawn or interactive mode.
   - If unclear, propose a sensible default and ask for confirmation.

5. **Propose Final Plan**
   - Show a concise summary:
     - Selected command name.
     - Parameters as a key/value list.
     - Chosen execution mode.
     - The approximate CLI equivalent, e.g.:
       - `python ~/.olaf/core/agentic/straf-cli/cli.py document-api --repo "..." --output "..." --generate docs tests`
   - Ask the user to confirm before executing.

6. **Execute**
   - Build the final CLI argument list for `straf-cli`, e.g.:
     - `python ~/.olaf/core/agentic/straf-cli/cli.py <command> [args...]`
   - If mode is **spawn**:
     - Clearly state that the process is intended to continue in background and that the provided CLI can be re-run or monitored from the user's shell.
   - If mode is **interactive**:
     - Show or summarize relevant console output when available.
     - Report success / failure based on exit code or observable behavior.

7. **Report Result & Terminate**
   - For **spawn**:
     - Clearly state that the process is intended to continue in background and that the provided CLI can be re-run or monitored from the user's shell.
   - For **interactive**:
     - Show or summarize relevant console output when available.
     - Report success / failure based on exit code or observable behavior.
   - Then terminate the skill.

## Error Handling

Handle at least the following error cases gracefully:

- **Unknown command**:
  - If the user picks a name or number that does not map to a known command, explain and re-display only the valid options.

- **Missing straf-cli**:
  - If a helper reports that `~/.olaf/core/agentic/straf-cli/cli.py` does not exist, surface a clear error and stop.

- **Invalid parameters**:
  - If the helper or CLI reports validation errors (e.g., missing required path), show the error and offer to re-run the launcher for that command.

- **Execution failure**:
  - For interactive mode, if exit code is non-zero, explicitly state that the command failed and surface key error output.

## Example Interactions

### Example 1: Spawn document-api

- User: "olaf run straf cli to document my API in background"
- Skill:
  - Suggest `document-api`.
  - Ask for `repo` and `output` paths.
  - Ask about optional generation flags (default `all`).
  - Default to **spawn** mode.
  - Propose final CLI and get confirmation.
  - Call `spawn-straf-command`.

### Example 2: Interactive researcher deep

- User: "olaf run straf researcher deep on topic X interactively"
- Skill:
  - Pick `researcher`.
  - Set `topic = "X"`, `deep = true`, `quick = false`.
  - Ask for optional scope/outcomes/output.
  - Set mode to **interactive**.
  - Propose, confirm, then call `run-straf-command-interactive`.

## Dependencies

- Python 3.x available in the environment.
- `~/.olaf/core/agentic/straf-cli/cli.py` present and runnable.
- AWS credentials configured for the `bedrock` profile in `us-east-1`.

The launcher must respect these constraints and rely on the two helper tools for actual process execution.
