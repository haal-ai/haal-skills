# Research and Report

## Overview

Research and Report is a structured research skill that conducts comprehensive investigations with current information validation and produces well-documented reports. It emphasizes web search integration, source verification, and mandatory URL collection for all references.

## Purpose

This skill addresses the need for thorough, well-sourced research by providing a systematic approach to gathering, validating, and synthesizing information. It ensures all findings are backed by accessible, current sources and delivered in professional report formats.

## Key Features

- **Web Search Integration**: Prioritizes current web sources over training data
- **Mandatory URL Collection**: Every source must include a full, accessible URL
- **Three-Phase Process**: Validation → Execution → Finalization
- **Template-Based Reports**: Uses structured templates for consistency
- **Chapter-by-Chapter Approval**: User reviews each section before proceeding
- **Source Currency Validation**: Verifies information is recent and relevant
- **Comprehensive Documentation**: Includes research plans and final reports

## Usage

Invoke this skill when you need to:
- Conduct thorough research on a specific topic
- Create professional research reports with proper citations
- Validate information against current web sources
- Document findings with accessible, verifiable URLs
- Produce structured deliverables for stakeholders

## Parameters

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| research_topic | string | Yes | Specific topic or question to research |
| scope_boundaries | string | Yes | What is included and excluded from research |
| expected_outcomes | string | Yes | Expected deliverables and target audience |
| timeline | string | No | Research and writing timeline |

## Process Flow

```
Phase 1: Validation
├── Topic Analysis
├── Source Planning
└── Template Selection
        ↓
Phase 2: Execution
├── Web Research
├── Information Synthesis
├── Report Generation
├── Source Documentation
└── Current Information Validation
        ↓
Phase 3: Finalization
├── Source Verification
├── Quality Check
└── Output Review
```

## Output

The skill produces:

1. **Research Plan** (`research-plan-YYYYMMDD-HHmm.md`)
   - Scope statement
   - Key research questions
   - Proposed chapter structure
   - Potential sources with search strategy

2. **Research Report** (`research-report-YYYYMMDD-HHmm.md`)
   - Title page
   - Table of contents
   - All approved chapters
   - Source documentation with URLs

3. **Executive Summary**
   - Key findings
   - Recommendations

## Examples

### Example 1: Technology Evaluation
```
research_topic: "Comparison of container orchestration platforms"
scope_boundaries: "Focus on Kubernetes, Docker Swarm, and Nomad for enterprise use"
expected_outcomes: "Decision matrix for infrastructure team"
timeline: "1 week"
```

### Example 2: Market Research
```
research_topic: "AI code assistant market landscape 2025"
scope_boundaries: "Enterprise tools only, exclude consumer products"
expected_outcomes: "Executive briefing for product strategy"
```

## Error Handling

| Error Condition | Handling |
|----------------|----------|
| Missing URLs | Reject source - no generic references allowed |
| Inaccessible Sources | Verify all URLs before including |
| Outdated Information | Flag conflicts between training data and current sources |
| Scope Creep | Return to user for clarification |
| Missing Parameters | Prompt user to provide required inputs |

## Related Skills

- `search-and-learn` - For personal learning and knowledge acquisition
- `tell-me` - For quick information retrieval
- `generate-tech-spec` - For technical documentation from research
