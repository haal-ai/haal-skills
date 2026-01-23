# Research and Report - Tutorial

## Overview
The Research and Report skill provides structured research capabilities with comprehensive reporting and current information validation. This tutorial will guide you through using this skill effectively.

## What This Skill Does

- **Structured Research**: Systematic approach with planning, execution, and finalization phases
- **Current Information Priority**: Web search validation of training data with mandatory URL collection
- **Chapter-by-chapter Workflow**: User approval required for each chapter before proceeding
- **Professional Reporting**: Publication-ready reports with proper formatting and sourcing

## When to Use This Skill

Use `research-andreport` when you need:
- Comprehensive research on any topic with current information
- Systematic investigation with professional documentation
- Web-validated findings to supplement training data
- Reports that require source verification and currency tracking

## Step-by-Step Tutorial

### Step 1: Invoke the Skill
```
olaf research-andreport
```

### Step 2: Provide Research Parameters
When prompted, provide:
- **research_topic**: Specific topic or question to research
- **scope_boundaries**: What is included and excluded from research  
- **expected_outcomes**: Expected deliverables and target audience
- **timeline**: Optional research and writing timeline

Example:
```
research_topic: "Modern containerization strategies for microservices"
scope_boundaries: "Focus on Docker and Kubernetes, exclude legacy systems"
expected_outcomes: "Technical guide for development teams"
timeline: "2 weeks for completion"
```

### Step 3: Review Research Plan
The skill will create a detailed research plan including:
- Scope statement with boundaries
- Key research questions (primary and secondary)
- Proposed chapter structure
- Potential sources strategy
- Timeline with phases

**Important**: You must approve this plan before research begins.

### Step 4: Chapter-by-Chapter Approval
For each chapter, the skill will:
1. Conduct web research for current information
2. Validate training data against recent sources
3. Draft the chapter content
4. Present it for your approval
5. Only proceed to the next chapter after approval

### Step 5: Final Report Delivery
After all chapters are approved:
- Complete report is compiled with table of contents
- Professional formatting applied
- Final file delivered to staging directory

## Output Files

The skill creates these files in your staging directory:

### Research Plan
- **File**: `research-plan-YYYYMMDD-HHmm.md`
- **Purpose**: Detailed research roadmap requiring approval
- **Template**: Uses structured planning template

### Research Report  
- **File**: `research-report-YYYYMMDD-HHmm.md`
- **Purpose**: Final comprehensive report with all findings
- **Template**: Professional report format with sourcing

## Key Features

### Current Information Priority
- Web searches prioritize 2024-2025 content
- Training data validated against recent sources
- All sources marked with currency indicators
- Mandatory URL collection (no generic references allowed)

### Source Validation Rules
- Every source must include full URL
- Sources categorized as "Web 2025", "Training Data", or "Verified 2025"
- Generic references without URLs are rejected
- Search dates documented for web sources

### Quality Standards
- Publication-ready formatting
- Professional structure and flow
- Accurate and current technical details
- Actionable recommendations

## Best Practices

### For Better Research Results
1. **Be Specific**: Provide clear, focused research topics
2. **Define Boundaries**: Clearly state what to include/exclude
3. **Set Expectations**: Specify target audience and use cases
4. **Review Carefully**: Approve each chapter thoughtfully

### For Source Quality
- Prefer official documentation and current vendor sites
- Value recent industry reports and technical blogs
- Use training data as supplementary, not primary source
- Verify conflicting information through multiple sources

### For Effective Workflow
- Allow time for thorough review of each chapter
- Provide feedback on chapter content before approval
- Consider timeline realistically for quality research
- Plan for iteration and refinement

## Common Use Cases

### Technical Research
- Technology stack analysis
- Architecture pattern research  
- Tool comparison and evaluation
- Performance and scaling studies

### Market Analysis
- Industry trend investigation
- Competitive landscape research
- Technology adoption patterns
- Solution comparisons

### Educational Content
- Learning guides and tutorials
- Best practices documentation
- Implementation roadmaps
- Decision frameworks

## Tips for Success

1. **Start with Clear Goals**: Define what you want to learn or decide
2. **Invest in Planning**: Good research plans lead to better reports
3. **Value Current Sources**: Prioritize recent information over training data
4. **Review Thoroughly**: Each chapter builds on previous ones
5. **Think Publication-Ready**: Reports should be professional and shareable

## Troubleshooting

### If Research Plan Needs Changes
- Provide specific feedback during approval phase
- Request modifications to scope, questions, or structure
- Clarify any ambiguous requirements

### If Sources Are Insufficient  
- Request broader search strategies
- Ask for additional source types
- Specify particular sources to investigate

### If Chapters Need Revision
- Provide detailed feedback before approval
- Ask for additional research on specific points
- Request different analysis angles or depth

## Expected Timeline

**Planning Phase**: 15-30 minutes for plan creation and approval
**Research Phase**: 1-3 hours per chapter depending on complexity
**Finalization Phase**: 15-30 minutes for compilation and formatting

Total time varies based on topic complexity, number of chapters, and review cycles.

This tutorial should help you get the most value from the Research and Report skill. Remember that the quality of your research inputs directly impacts the quality of your research outputs!