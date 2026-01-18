# Transform Raw Spec

**Source**: transform-raw-spec/skill.md

## Overview

Transform Raw Spec uses a Propose-Act protocol to transform a raw rules or specification document into a complete, testable specification through a 7-step process, using curated templates, best examples, and timestamped outputs.

## Purpose

Converting informal requirements and rules into formal, testable specifications is critical for software quality. This skill provides a structured methodology for transforming raw specifications into EARS (Easy Approach to Requirements Syntax) format, ensuring completeness, consistency, and testability.

## Usage

**Command**: `transform raw spec`

**Protocol**: Propose-Act with user engagement at decision points

**When to Use**: Use this skill when you have raw requirements, rules, or specifications that need to be formalized into a structured, testable format. It's particularly valuable during the specification phase of ESDI or when preparing requirements for development teams.

## Parameters

### Required Inputs
- **raw_rules_path**: Path to the source rules/spec document (e.g., `scripts/olaf/rules.md`)
- **output_folder**: Target folder to write step files (e.g., `spec-<channel>-<model>`)
- **spec_name**: Short name for the spec (used in headings)

### Optional Inputs
- **strict_template_compliance**: Enforce templates strictly (default: `true`)

### Context Requirements
- Access to templates under `templates/`
- Read access to source specification
- Write access to output folder
- Time tools for timestamp generation

## Output

**Deliverables**:
- Step 1-7 markdown files with timestamps
- Final consolidated `specification.md`

**Output Structure**:
```
[output_folder]/
├── step1-<timestamp>.md    # Clarify & Group
├── step2-<timestamp>.md    # Initial EARS
├── step3-<timestamp>.md    # Quality Check + Decisions
├── step4-<timestamp>.md    # Completeness + Decisions
├── step5-<timestamp>.md    # Challenge + Decisions
├── step6-<timestamp>.md    # Visual Documentation
├── step7-<timestamp>.md    # Testability Assessment
└── specification.md        # Final consolidated EARS spec
```

## Process Flow

### Step 1: Clarify & Group (Automated)
- Extract domains from raw specification
- Identify gaps and questions
- Group related requirements

### Step 2: Transform to EARS (Automated)
- Convert requirements to EARS format
- Normalize flags and terminology
- Structure with Trigger/Condition/Response/Measure

### Step 3: Quality Check (User Decisions Required)
- Identify contradictions and duplicates
- Present scope/clarification items
- Record user decisions

### Step 4: Completeness & Consistency (User Decisions Required)
- Identify missing scenarios and edge cases
- Check terminology consistency
- Resolve conflicts with user input

### Step 5: Challenge, Simplify, Amplify (User Decisions Required)
- Web-researched challenge catalog
- CLI UX, error taxonomy, security patterns
- MoSCoW priority assignment

### Step 6: Visual Documentation (Automated)
- Generate Mermaid diagrams
- Architecture and flow visualizations
- State diagrams for complex processes

### Step 7: Testability Assessment (Automated)
- Verification criteria framework
- Test automation recommendations
- Quality metrics and thresholds

### Final Consolidation (Automated)
- Create definitive `specification.md`
- Integrate all decisions
- Ready for design phase consumption

## Examples

### Example 1: CLI Tool Specification

**Input**:
- raw_rules_path: `docs/cli-rules.md`
- output_folder: `spec-cli-tool`
- spec_name: "CLI Tool"

**Output**: Complete EARS specification with 7 step files and consolidated specification.md

### Example 2: API Specification

**Input**:
- raw_rules_path: `api/requirements.md`
- output_folder: `spec-api-v2`
- spec_name: "API v2"

**Output**: Formal API specification with testability assessment and visual documentation

## Related Skills

- **esdi-chain**: Orchestrates transform-raw-spec as Phase 2
- **generate-design**: Consumes specification.md for Phase 3
- **review-human-written-spec**: Alternative for reviewing existing specs

## Tips

1. **Prepare raw input**: Ensure your source document is readable and organized
2. **Engage at decision points**: Steps 3-5 require your input for quality
3. **Use strong models for diagrams**: Step 6 benefits from capable models for Mermaid generation
4. **Review step outputs**: Each step builds on previous ones
5. **Keep specification.md updated**: This is the primary output for downstream phases

## Limitations

- Requires user engagement at Steps 3, 4, and 5
- Mermaid diagram quality depends on model capability
- Cannot automatically resolve all ambiguities in source documents
- Templates must be available for proper formatting
