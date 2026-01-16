# Implementation Plan: Automated Skill Documentation

## Overview

This implementation plan describes the steps for an AI agent to execute the automated skill documentation workflow. Skills are processed in batches of 5 to manage context limits across sessions.

## Tasks

- [x] 1. Create a git worktree for documentation work
  - Create a new worktree: git worktree add ../skills-docs-worktree docs/regenerate-curated-skills
  - Change to the worktree directory: cd ../skills-docs-worktree
  - Verify you are in the worktree on the new branch
  - _Requirements: Preparation for isolated work_

- [x] 2. Read and parse verified-skills.txt
  - Read the file at verified-skills.txt
  - Extract all skill names (one per line)
  - Store the list of skills to process
  - Display the total count of skills to process
  - _Requirements: 1.1, 1.2, 1.3, 1.4_

- [-] 3. Process skills in batches of 5
  - For each batch, execute sub-tasks 3.1-3.5 for each skill in the batch
  - After completing a batch, commit progress and stop for new session

  - [x] 3.A Batch 1: Skills 1-5
    - Skills: carry-on-session, create-prompt, create-changelog-entry, challenge-me, tell-me
    - For each skill: validate → generate description → generate tutorial → add to stable.txt → remove from verified-skills.txt
    - _Requirements: 2.1-2.5, 3.1-3.4, 4.1-4.4, 5.1-5.4, 6.1-6.5_

  - [x] 3.B Batch 2: Skills 6-10
    - Skills: search-and-learn, research-and-report, review-code, review-diff, analyze-function-complexity
    - For each skill: validate → generate description → generate tutorial → add to stable.txt → remove from verified-skills.txt
    - _Requirements: 2.1-2.5, 3.1-3.4, 4.1-4.4, 5.1-5.4, 6.1-6.5_

  - [x] 3.C Batch 3: Skills 11-15
    - Skills: analyze-contributor-risk, review-user-story, should-i-use-ai, scaffold-quarkus-microservice, generate-orchestrator
    - For each skill: validate → generate description → generate tutorial → add to stable.txt → remove from verified-skills.txt
    - _Requirements: 2.1-2.5, 3.1-3.4, 4.1-4.4, 5.1-5.4, 6.1-6.5_

  - [ ] 3.D Batch 4: Skills 16-20
    - Skills: store-conversation-record, create-skill, evaluate-prompt-for-adoption, check-prompt-compliance, convert-prompt-to-skill
    - For each skill: validate → generate description → generate tutorial → add to stable.txt → remove from verified-skills.txt
    - _Requirements: 2.1-2.5, 3.1-3.4, 4.1-4.4, 5.1-5.4, 6.1-6.5_

  - [ ] 3.E Batch 5: Skills 21-25
    - Skills: convert-skill-to-chain, assist-me-as-prompt-engineer, switch-context, bootstrap-functional-spec-from-code, deepen-tech-spec-developer
    - For each skill: validate → generate description → generate tutorial → add to stable.txt → remove from verified-skills.txt
    - _Requirements: 2.1-2.5, 3.1-3.4, 4.1-4.4, 5.1-5.4, 6.1-6.5_

  - [ ] 3.F Batch 6: Skills 26-30
    - Skills: assess-genai-initiative-idea, code-in-go, code-in-rust, augment-code-unit-test, run-redocumentation
    - For each skill: validate → generate description → generate tutorial → add to stable.txt → remove from verified-skills.txt
    - _Requirements: 2.1-2.5, 3.1-3.4, 4.1-4.4, 5.1-5.4, 6.1-6.5_

  - [ ] 3.G Batch 7: Skills 31-35
    - Skills: generate-commits-from-changelog, esdi-chain, transform-raw-spec, generate-design, generate-implementation-plan
    - For each skill: validate → generate description → generate tutorial → add to stable.txt → remove from verified-skills.txt
    - _Requirements: 2.1-2.5, 3.1-3.4, 4.1-4.4, 5.1-5.4, 6.1-6.5_

  - [ ] 3.H Batch 8: Skills 36-40
    - Skills: run-implementation-plan, onboard-me, get-bms-expertise, create-otf-variable
    - For each skill: validate → generate description → generate tutorial → add to stable.txt → remove from verified-skills.txt
    - _Requirements: 2.1-2.5, 3.1-3.4, 4.1-4.4, 5.1-5.4, 6.1-6.5_

- [ ] 4. Git commit and push all changes
  - Stage all modified files: git add .
  - Create commit with message: "docs: regenerate documentation for [N] curated skills"
  - Push to remote repository: git push
  - Report any git errors
  - _Requirements: 10.1, 10.2, 10.3, 10.4, 10.5_

- [ ] 5. Display completion summary
  - Output total skills processed
  - Output successful/failed counts
  - _Requirements: 8.1, 8.5_

## Per-Skill Processing Steps (for each skill in a batch)

1. **Validate skill structure**
   - Check if [skill-name]/ directory exists
   - Check if [skill-name]/skill.md file exists
   - If invalid: log error and skip to next skill

2. **Generate description documentation**
   - Read [skill-name]/skill.md
   - Generate [skill-name]/docs/description.md with: Overview, Purpose, Key Features, Usage, Parameters, Process Flow, Output, Examples, Error Handling, Related Skills

3. **Generate tutorial documentation**
   - Read [skill-name]/skill.md
   - Generate [skill-name]/docs/tutorial.md with: Introduction, Prerequisites, Step-by-Step Instructions, Verification Checklist, Troubleshooting, Next Steps

4. **Add skill to stable.txt**
   - Read current stable.txt content
   - Check if skill already exists (skip if yes)
   - Add skill name to list
   - Sort alphabetically
   - Write back to stable.txt

5. **Remove skill from verified-skills.txt**
   - Read current verified-skills.txt content
   - Filter out the skill name line
   - Write updated content back to file

## Skill Name Corrections (typos in verified-skills.txt)

| In verified-skills.txt | Actual directory name |
|------------------------|----------------------|
| bootstrap-functionnal-spec-from-code | bootstrap-functional-spec-from-code |
| deepen-tech-spec-developper | deepen-tech-spec-developer |
| augment-unittest | augment-code-unit-test |
| generat-commits-fron-changelog | generate-commits-from-changelog |
| un-implementation-plan | run-implementation-plan |
| create-otf-varibale | create-otf-variable |
| switch-context (use @swicth-context) | switch-context |
| create-skill-presentation | SKIP - does not exist |

## Notes

- Each batch processes 5 skills (except last batch which may have fewer)
- After completing a batch, start a new session for the next batch
- Errors in one skill do not stop processing of remaining skills in the batch
- Work is done in a separate git worktree (../skills-docs-worktree on branch docs/regenerate-curated-skills)
- carry-over-session was already processed in a previous session
