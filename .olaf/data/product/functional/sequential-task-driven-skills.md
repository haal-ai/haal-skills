# Sequential Task-Driven Skills

## Overview
Introduction of sequential task-driven skills that enable complex workflows through structured, step-by-step execution. The search-and-learn skill serves as the reference implementation for this new approach.

## Business Impact
- Enables smaller, less capable models to deliver complex tasks with reduced errors
- Provides structured execution framework for multi-step processes
- Improves reliability and consistency in skill execution
- Reduces model hallucination through bounded, sequential task processing

## Implementation Context
The sequential task-driven approach uses:
- Master chain coordinators that manage task execution order
- Individual task prompts with specific input/output contracts
- Context passing between tasks via simple variables
- Strict sequential execution with dependency validation

## User Experience Changes
- Users experience more predictable and reliable skill execution
- Complex workflows are broken down into manageable steps
- Clear visibility into task progression and status
- Improved error handling and debugging capabilities

## Success Metrics
- Reduced error rates in complex skill execution
- Improved task completion rates for smaller models
- Enhanced user trust in automated workflows
- Better maintainability of complex skill logic

## Technical Details
- Reference implementation: search-and-learn skill
- Chain prompting converter available for traditional prompt migration
- Supports both Propose-Act and direct execution protocols
- Template-driven task structure for consistency
