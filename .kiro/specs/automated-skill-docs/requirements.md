# Requirements Document

## Introduction

This document specifies the requirements for an AI agent workflow that regenerates documentation (description.md and tutorial.md files) for ALL curated skills listed in the catalog.md file. The workflow will use existing documentation generation skills (create-skill-description and generate-step-by-step-tutorial) to batch-process all curated skills without requiring custom code.

## Glossary

- **Skill**: A reusable AI agent workflow defined in a skill.md file
- **Curated_Skill**: A skill listed under the "Curated" section in catalog.md
- **Stable_Skill**: A skill that has complete documentation and is listed in stable.txt
- **AI_Agent_Workflow**: The AI agent workflow that orchestrates doc generation using existing skills
- **Documentation_Generator_Skill**: The create-skill-description skill used to generate descriptions
- **Tutorial_Generator_Skill**: The generate-step-by-step-tutorial skill used to generate tutorials
- **Description_File**: A description.md file that provides overview and usage information
- **Tutorial_File**: A tutorial.md file that provides step-by-step instructions
- **Catalog**: The docs/skills/catalog.md file that lists all skills and their documentation status
- **Stable_File**: The stable.txt file that lists skills with complete documentation
- **Verified_Skills_File**: The verified-skills.txt file that lists skills pending documentation
- **Skill_Directory**: The folder containing a skill's files (e.g., analyze-contributor-risk/)
- **Docs_Directory**: The /docs/ subfolder within a skill directory
- **Git_Repository**: The version control repository where all changes are committed and pushed

## Requirements

### Requirement 1: Identify All Curated Skills

**User Story:** As a documentation maintainer, I want to identify all curated skills from verified-skills.txt, so that I can regenerate documentation for every curated skill.

#### Acceptance Criteria

1. WHEN the AI_Agent_Workflow runs, THE Agent SHALL read the Verified_Skills_File at verified-skills.txt
2. WHEN parsing the Verified_Skills_File, THE Agent SHALL extract all skill names listed in the file
3. THE Agent SHALL create a list of all skills to be processed
4. THE Agent SHALL output the complete list of skills to be processed

### Requirement 2: Validate Skill Structure

**User Story:** As a documentation maintainer, I want to validate that skills have the required files before attempting documentation generation, so that I can identify any structural issues.

#### Acceptance Criteria

1. WHEN validating a skill, THE Agent SHALL verify that the Skill_Directory exists at the workspace root
2. WHEN validating a skill, THE Agent SHALL verify that skill.md exists within the Skill_Directory
3. IF the Skill_Directory does not exist, THEN THE Agent SHALL report the skill as invalid and skip it
4. IF skill.md does not exist, THEN THE Agent SHALL report the skill as invalid and skip it
5. WHEN a skill is validated successfully, THE Agent SHALL mark it as ready for documentation generation

### Requirement 3: Invoke Description Generation Skill

**User Story:** As a documentation maintainer, I want to use the create-skill-description skill to generate description.md files, so that I can leverage existing proven documentation generation logic.

#### Acceptance Criteria

1. WHEN generating a Description_File, THE Agent SHALL invoke the Documentation_Generator_Skill with parameter skill_name
2. WHEN invoking the Documentation_Generator_Skill, THE Agent SHALL provide the skill name as input
3. WHEN the Documentation_Generator_Skill completes, THE Agent SHALL verify that [Skill_Directory]/docs/description.md was created or updated
4. WHEN the Documentation_Generator_Skill fails, THE Agent SHALL log the error and continue to the next skill

### Requirement 4: Invoke Tutorial Generation Skill

**User Story:** As a documentation maintainer, I want to use the generate-step-by-step-tutorial skill to generate tutorial.md files, so that I can leverage existing proven tutorial generation logic.

#### Acceptance Criteria

1. WHEN generating a Tutorial_File, THE Agent SHALL invoke the Tutorial_Generator_Skill with parameters: source_type="file", source_file="[Skill_Directory]/skill.md", workflow_name="[skill-name]"
2. WHEN invoking the Tutorial_Generator_Skill, THE Agent SHALL provide the skill name and source file path as input
3. WHEN the Tutorial_Generator_Skill completes, THE Agent SHALL verify that [Skill_Directory]/docs/tutorial.md was created
4. WHEN the Tutorial_Generator_Skill fails, THE Agent SHALL log the error and continue to the next skill

### Requirement 5: Move Skills to Stable

**User Story:** As a documentation maintainer, I want successfully documented skills to be added to stable.txt, so that the file tracks all skills with complete documentation.

#### Acceptance Criteria

1. WHEN documentation generation succeeds for a skill, THE Agent SHALL add the skill name to stable.txt
2. WHEN adding to stable.txt, THE Agent SHALL append the skill name on a new line
3. WHEN adding to stable.txt, THE Agent SHALL maintain alphabetical order
4. IF the skill name already exists in stable.txt, THE Agent SHALL skip adding it

### Requirement 6: Remove from Verified Skills

**User Story:** As a documentation maintainer, I want successfully documented skills to be removed from verified-skills.txt, so that the file only contains skills pending documentation.

#### Acceptance Criteria

1. WHEN a skill is added to stable.txt, THE Agent SHALL remove the skill name from verified-skills.txt
2. WHEN removing from verified-skills.txt, THE Agent SHALL read the entire file content
3. WHEN removing from verified-skills.txt, THE Agent SHALL filter out the skill name line
4. WHEN removing from verified-skills.txt, THE Agent SHALL write the updated content back to the file
5. IF the skill name is not found in verified-skills.txt, THE Agent SHALL log a warning but continue processing

### Requirement 7: Batch Processing Workflow

**User Story:** As a documentation maintainer, I want to process all curated skills in a single AI agent workflow, so that I can efficiently regenerate all documentation at once.

#### Acceptance Criteria

1. WHEN running the workflow, THE Agent SHALL process all identified curated skills sequentially
2. WHEN processing each skill, THE Agent SHALL: generate description, generate tutorial, add to stable.txt, remove from verified-skills.txt
3. WHEN a skill generation fails, THE Agent SHALL log the error and continue processing remaining skills
4. WHEN the workflow completes, THE Agent SHALL report total skills processed, successful generations, and failures
5. THE Agent SHALL maintain a processing log with timestamps and status for each skill

### Requirement 8: Progress Reporting

**User Story:** As a documentation maintainer, I want to see real-time progress updates during the workflow execution, so that I can monitor the documentation regeneration process.

#### Acceptance Criteria

1. WHEN the workflow starts, THE Agent SHALL display the total number of curated skills to process
2. WHEN processing each skill, THE Agent SHALL display the current skill name and documentation type being generated
3. WHEN a skill completes successfully, THE Agent SHALL display a success message with file locations
4. WHEN a skill fails, THE Agent SHALL display an error message with the failure reason
5. WHEN the workflow completes, THE Agent SHALL display a summary report with statistics

### Requirement 9: Error Handling

**User Story:** As a documentation maintainer, I want clear error messages when documentation generation fails, so that I can troubleshoot and fix issues.

#### Acceptance Criteria

1. IF a skill.md file cannot be read, THEN THE Agent SHALL report a file access error with the file path
2. IF the Documentation_Generator_Skill fails, THEN THE Agent SHALL report the specific error from the skill
3. IF the Tutorial_Generator_Skill fails, THEN THE Agent SHALL report the specific error from the skill
4. THE Agent SHALL continue processing remaining skills after encountering an error

### Requirement 10: Git Commit and Push

**User Story:** As a documentation maintainer, I want all changes to be automatically committed and pushed to the repository, so that the documentation updates are persisted and the GitHub workflow rebuilds the catalog and mkdocs site.

#### Acceptance Criteria

1. WHEN all skills have been processed, THE Agent SHALL stage all modified and new files using git add
2. WHEN staging files, THE Agent SHALL include: generated docs, stable.txt, and verified-skills.txt
3. WHEN creating a commit, THE Agent SHALL use a descriptive message: "docs: regenerate documentation for [N] curated skills"
4. WHEN the commit is created, THE Agent SHALL push the changes to the remote repository
5. IF git operations fail, THEN THE Agent SHALL report the error with the git command output
