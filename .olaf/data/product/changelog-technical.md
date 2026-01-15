# Technical Changelog

## 2025-11

### 2025-11-25
- Refactor: Consolidate git-add-commit task chain into monolithic workflow with dependency chasing
- Refactor: Major enhancement to propose-commit-thread with reference chasing and semantic analysis
- Refactor: Replace task-chain with persona-driven quickstart generation in onboard-me
- Refactor: Rename convert-prompt to convert-prompt-to-skill and align with create-skill guidance
- Refactor: Add KB-driven structure validation and file safety to create-prompt and create-skill
- Architecture: Add AWS Strands CLI multi-agent reference implementation
- Architecture: Add MkDocs generation skill with async spawn execution
- Architecture: Auto-generate OLAF framework loading for all prompts via select-collection
- Architecture: Add olaf-skill-manager context
- Architecture: Sync intent detection across Windsurf and Kiro platforms
- Architecture: Enhance intent-based context injector with mandatory detection and examples
- Infrastructure: Share OLAF olaf-specialist collections with team
- Infrastructure: Update share-skills-with-team for Python-based distribution
- Fix: Complete share-olaf script fixes with enhanced error handling, branch management, and collection validation
- Fix: Correct straf-locks path from .olaf/core/work to .olaf/work

### 2025-11-24
- Architecture: Add specialist competency collections and session-manager collection
- Architecture: Add ESDI meta-skill with session management and architectural improvements
- Architecture: Add competency validation script
- Architecture: Implement STRAF spawn tool for autonomous multi-agent orchestration
- Infrastructure: Update 30+ skills with latest enhancements and validations
- Infrastructure: Update competency registry, collections, syncer, and skill manifests for collection support
- Refactor: Convert git-add-commit to master-chain pattern
- Refactor: Decompose review-diff into modular task-based structure
- Refactor: Simplify tell-me skill to search-first knowledge retrieval
- Refactor: Enhance convert-skill-to-chain task selection and search logic
- Sync: Port task-registry, agentic tools, repo-guide, KB files from feature-olaf-ide-onboarding

### 2025-11-22
- Architecture: Complete OLAF framework with STRAF autonomous execution toolkit
- Architecture: Add onboard competency for intelligent repository analysis

### 2025-11-21
- Architecture: Add STRAF autonomous execution toolkit (spawn, monitor, survey utilities) and framework to .olaf/core/agentic
- Architecture: Add task registry with common and skill-specific tasks
- Architecture: Add straf-skill-runner meta-skill and research-and-report master-chain skill
- Architecture: Add convert-skill-to-chain skill with evaluation task
- Architecture: Add core validation schemas, development practices and standards, and review-diff skill
- Infrastructure: Add common tools directory with get-env.py and update context files for all platforms
- Fix: Update olaf-bootstrap instructions, tool selection hierarchy, and competency index
- Fix: Correct get-env.py path references in challenge-me, convert-skill-to-chain, and review-github-pr
- Fix: Remove conversation records directory reference and update paths in prompts
- Fix: Risk-based test pipeline undefined variables and duplicate logging

### 2025-11-18
- Fix: Time retrieval improvement [Details](technical/time-retrieval-reliability-fix.md)
- Refactor: renames some folder and now everything is under .olaf [Details](technical/folder-restructure-olaf.md)
- Infrastructure: Added full OLAF CLI to install, distribute and bundle [Details](technical/olaf-cli-install-distribute-bundle.md)

### 2025-11-19
- Cleanup: Completed migration by removing duplicate use-competency skill, keeping use-skill as the single router

### 2025-11-17
- Architecture: Renamed kernel skills from competency-based to skills-based terminology (use-competency→use-skill, list-competencies→list-skills) for architectural clarity [Details](technical/structural-reorganization-kernel-skills.md)
- Breaking: Structural folder reorganization (.olaf/olaf-core/→.olaf/core/) improves directory consistency but requires installer updates for compatibility [Details](technical/structural-reorganization-kernel-skills.md)

### 2025-11-15
- Architecture: Added create-skill capability with skill manifest, templates, and automated generation framework [Details](technical/create-skill-architecture.md)
- Architecture: Enhanced intent-based context injection system with cross-platform code review guidelines [Details](technical/intent-router-code-review-integration.md)
- Architecture: Added core principle for tool selection hierarchy to optimize LLM function usage [Details](technical/tool-selection-hierarchy-principle.md)
- Architecture: Moved development root to .olaf folder for simplified installation [Details](technical/development-root-relocation.md)
- Setup: Created technical changelog structure [Details](technical/changelog-setup.md)