---
name: extract-notes-from-skube-site
description: Create chapter-by-chapter synthesis notes that separate SKube-specific guidance from Quarkus baseline, with resumable TODO/WIP/DONE progress tracking.
license: Apache-2.0
metadata:
  olaf_tags: [skube, documentation-synthesis, chapter-analysis, progress-tracking, quarkus-baseline, multi-agent]
  copyright: Copyright (c) 2026 pjmp020564
  author: pjmp020564 (on github)
  repository: https://github.com/haal-ai/haal-ide
  provider: Haal AI
---

<olaf>

if you are in need to get the date and time, use time tools, fallback to shell command if needed

**MANDATORY**: before doing anything else, read fully the `.olaf/team-delegation.md` file and apply its requirements strictly.

## Purpose
You WILL analyze a documentation site (default: SKube S3J user guide) and produce:
- One synthesis note per chapter.
- A global synthesis note created at the start and updated at the end.
- A progress tracker enabling restart/resume and multi-agent coordination.

You MUST clearly separate:
- **SKube-specific** content (what SKube adds/changes on top of Quarkus)
- **Quarkus-baseline** content (what is standard Quarkus behavior)

In addition, you MUST produce and maintain an aggregated **SKube-specific synthesis** across chapters:
- Each chapter note MUST contain a dedicated "SKube-specific synthesis (portable takeaways)" section.
- The global synthesis MUST consolidate these takeaways into a single aggregated list.

## Input Parameters
You MUST request these parameters if not provided by the user:
- **input_url**: string - Documentation URL to analyze (REQUIRED)
- **agent_name**: string - Agent identifier used to claim tasks in progress tracker (OPTIONAL - default: "unknown")
- **run_id**: string - Timestamp ID `YYYYMMDD-HHmm` used in output folder naming (OPTIONAL - default: current timestamp)
- **chapter_selection**: string - Which chapters to process now (OPTIONAL - default: "next")
  - Allowed values:
    - `next` (process the next TODO chapter not claimed by someone else)
    - `all` (process all TODO chapters)
    - comma-separated chapter numbers (e.g., `2,3,12`)
- **resume**: boolean - If true, resume using existing progress tracker (OPTIONAL - default: true)

## Output Locations (MANDATORY)
You MUST save outputs exactly here:
- **Progress tracker** (shared across sessions/agents): `.olaf/work/skube/progress.md`
- **Per-run output folder**: `.olaf/work/skube/syntheise-${run_id}/`

Within `.olaf/work/skube/syntheise-${run_id}/` you MUST create:
- `00-global-synthesis.md`
- One file per chapter you complete, named with a stable chapter prefix, e.g.:
  - `02-introduction.md`
  - `12-messaging.md`

## User Interaction Protocol
You MUST follow **Propose-Confirm-Act** because this skill writes/updates files under `.olaf/work/`.

## Templates (MANDATORY)
You MUST follow these external templates:
- Chapter note template: `skills/extract-notes-from-skube-site/templates/chapter-synthesis.md`
- Global synthesis template: `skills/extract-notes-from-skube-site/templates/global-synthesis.md`
- Progress tracker template: `skills/extract-notes-from-skube-site/templates/progress-tracker.md`

You MUST NOT embed these templates in your output; you MUST produce files that follow them.

## Progress Tracking Rules (MANDATORY)
The progress tracker is the single source of truth.

### Status vocabulary
You MUST use ONLY these statuses:
- `TODO`
- `WIP`
- `DONE`

You MUST NOT add percentages or any other progress fields.

### Multi-agent coordination
You MUST follow these rules:
- If a chapter is `WIP` and owned by someone else, you MUST skip it.
- To start a chapter, you MUST atomically claim it by updating status to `WIP` and setting `Owner = agent_name`.
- To mark a chapter `DONE`, you MUST set `Output File` to the path of the chapter note you created.

If the progress file does not exist, you MUST create it following the progress tracker template.

## Process

<!-- <validation_phase> -->
### 1. Validation Phase
You WILL:
1. Validate `input_url` is a http/https URL.
2. Ensure `.olaf/work/skube/` exists (create if missing).
3. Ensure `.olaf/work/skube/progress.md` exists:
   - If missing: create it from the progress template.
   - If present and `resume=true`: read it and continue.
4. Determine `run_id` (timestamp) if not provided.
<!-- </validation_phase> -->

<!-- <planning_phase> -->
### 2. Initial Analysis (first run or when progress has no tasks)
If `.olaf/work/skube/progress.md` has no chapter rows, you WILL:
1. Read the documentation at `input_url`.
2. Identify the chapter list (top-level headings).
3. Populate the progress table with one row per chapter set to `TODO`.
4. Create the initial global synthesis at:
   `.olaf/work/skube/syntheise-${run_id}/00-global-synthesis.md`
   following the global synthesis template.
<!-- </planning_phase> -->

<!-- <execution_phase> -->
### 3. Execution Phase (chapter-by-chapter)
You WILL select chapters according to `chapter_selection`:

- If `chapter_selection=next`:
  - Pick the first chapter row with `Status=TODO`.
  - If it is already `WIP` (someone claimed it), skip it and pick the next `TODO`.

- If `chapter_selection=all`:
  - Process all chapters that are `TODO`.
  - You MUST skip any chapter that is `WIP` owned by someone else.

- If `chapter_selection` is a list of numbers:
  - Process only those chapters if they are `TODO`.
  - If any are already `WIP` owned by someone else, skip them.

For each selected chapter you WILL:
1. Update `.olaf/work/skube/progress.md` to mark the chapter as `WIP` with `Owner=agent_name`.
2. Produce a chapter synthesis note in `.olaf/work/skube/syntheise-${run_id}/` using the chapter synthesis template.
3. Classification MUST be explicit:
   - "This is SKube-specific" section:
     - Describe what SKube adds/changes.
     - Provide SKube doc references (URL + section heading; include anchors if possible).
   - "SKube-specific synthesis (portable takeaways)" section:
     - Extract concise, reusable takeaways that summarize SKube-specific constraints, conventions, or platform behaviors.
   - "This is Quarkus-baseline" section:
     - Describe the Quarkus feature.
     - You MUST search and link the official Quarkus documentation page(s).
4. Mark chapter `DONE` in `.olaf/work/skube/progress.md` and set `Output File` to the created note path.

### 4. Global synthesis update (end of each run)
At the end of the run you MUST update:
- `.olaf/work/skube/syntheise-${run_id}/00-global-synthesis.md`

You MUST incorporate:
- New SKube-specific vs Quarkus-baseline learnings from any chapters completed in this run.
- Aggregated SKube-specific synthesis takeaways extracted from the chapter notes completed in this run.
<!-- </execution_phase> -->

## Error Handling
You WILL handle these scenarios:
- **Progress file missing**: Create it from template.
- **Progress file malformed**: Stop and ask user to fix it manually (do not guess).
- **All tasks are WIP by other agents**: Stop and report there is nothing safe to pick.
- **Chapter already DONE**: Do not redo it unless the user explicitly requests rework.
- **Cannot find Quarkus official doc**: Provide best-effort official link and state uncertainty.

## Success Criteria
You WILL consider the run successful when:
- [ ] `.olaf/work/skube/progress.md` exists and contains only TODO/WIP/DONE statuses
- [ ] At least one chapter note is produced OR the skill correctly reports no available TODO tasks
- [ ] Each completed chapter is marked DONE with a valid Output File path
- [ ] `00-global-synthesis.md` exists and is updated at end of run

</olaf>
