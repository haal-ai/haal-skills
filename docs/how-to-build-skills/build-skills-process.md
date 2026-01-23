# Build Skills Process

This guide explains how to develop new AI agent skills iteratively using a two-agent approach.

## Overview

The most effective Skill development process involves the AI agent itself. Work with one instance of the agent ("Agent A") to create a Skill that will be used by other instances ("Agent B"). 

- **Agent A**: Helps you design and refine instructions
- **Agent B**: Tests the Skill in real tasks

This works because AI agents understand both how to write effective agent instructions and what information agents need.

## Creating a New Skill

### Step 1: Complete a Task Without a Skill

Work through a problem with Agent A using normal prompting. As you work, you'll naturally provide context, explain preferences, and share procedural knowledge. Notice what information you repeatedly provide.

### Step 2: Identify the Reusable Pattern

After completing the task, identify what context you provided that would be useful for similar future tasks.

> **Tip**: Not every pattern is worth making a Skill. Consider whether the information you're capturing is truly reusable across different tasks or contexts.

**Example**: If you worked through a code refactoring session, you might have provided:
- Naming conventions
- Error handling patterns (like "always use custom exceptions instead of generic ones")
- Logging standards
- Preferred design patterns for your codebase

### Step 3: Ask Agent A to Create a Skill

Prompt: *"Create a Skill using the above conversation that captures this refactoring pattern we just used. Include the naming conventions, error handling rules, and the logging standards."*

Until LLMs are  trained on skill creation, we recommend using a dedicated skill-writing skill (like `create-skill`) to guide the process. If you don't have one available, you can still rely on the LLM directly—it may work well depending on the model. Another effective approach is to reference existing skills as examples: *"Based on our `review-code` skill structure, create a similar skill for..."* This gives the agent concrete patterns to follow.

### Step 4: Review for Conciseness

Check that Agent A hasn't added unnecessary explanations. 

Prompt: *"Remove the explanation about what SOLID principles are - the agent already knows that."*

### Step 5: Improve Information Architecture

Ask Agent A to organize the content more effectively. Favor external files over inline content:

- **Templates**: Keep templates in separate files (`templates/`) so you can evolve the skill by updating templates without touching the prompt itself.
- **Scripts**: Place code in external files (`tools/`) rather than embedding it in the skill prompt—this makes testing and debugging much easier. Prefer Python over shell scripts; most models produce more reliable Python than shell code.

Prompt: *"Organize this so the naming conventions are in a separate reference file. Move any code snippets to external Python scripts in the tools folder."*

### Step 6: Test on Similar Tasks

Use the Skill with Agent B (a fresh instance with the Skill loaded) on related use cases. Before testing:

- **Close all editor files**: Most agents include open files in their context, which can cause unexpected behavior or give the agent extra hints it wouldn't normally have.
- **Start a fresh conversation**: Don't test in the same session where you created the skill. Accumulated context makes the skill appear to work better than it actually does—you want to test the real skill in isolation.

Observe whether Agent B:
- Finds the right information—including the skill itself if you have many available
- Applies rules correctly
- Handles the task successfully

### Step 7: Iterate Based on Observation

If Agent B struggles or misses something, return to Agent A with specifics.

Prompt: *"When the agent used this Skill, it forgot to add logging for error cases. Should we add a section about mandatory logging patterns?"*

## Iterating on Existing Skills

The same hierarchical pattern continues when improving Skills. You alternate between:

1. Working with Agent A (the expert who helps refine the Skill)
2. Testing with Agent B (the agent using the Skill to perform real work)
3. Observing Agent B's behavior and bringing insights back to Agent A

### Iteration Process

| Step | Action |
|------|--------|
| 1 | **Use the Skill in real workflows** - Give Agent B actual tasks, not test scenarios |
| 2 | **Observe Agent B's behavior** - Note where it struggles, succeeds, or makes unexpected choices |
| 3 | **Return to Agent A for improvements** - Share the current skill.md and describe what you observed |
| 4 | **Review Agent A's suggestions** - Consider reorganizing, using stronger language, or restructuring |
| 5 | **Apply and test changes** - Update the Skill, then test again with Agent B |
| 6 | **Repeat based on usage** - Continue this observe-refine-test cycle |

**Example observation**: *"When I asked Agent B to refactor the authentication module, it applied the naming conventions but forgot to wrap external API calls in try-catch blocks, even though the Skill mentions this rule."*

**Follow-up prompt**: *"I noticed Agent B forgot to add error handling for external calls. The Skill mentions error handling, but maybe it's not prominent enough?"*

Agent A might suggest:
- Reorganizing to make rules more prominent
- Using stronger language like "MUST wrap" instead of "always wrap"
- Restructuring the workflow section

## Gathering Team Feedback

- Share Skills with teammates and observe their usage
- Ask: Does the Skill activate when expected? Are instructions clear? What's missing?
- Incorporate feedback to address blind spots in your own usage patterns

## Observe How the Agent Navigates Skills

As you iterate on Skills, pay attention to how the agent actually uses them in practice:

| Observation | What It Means |
|-------------|---------------|
| **Unexpected exploration paths** | Your structure isn't as intuitive as you thought |
| **Missed connections** | Your links need to be more explicit or prominent |
| **Overreliance on certain sections** | That content should be in the main skill.md instead |
| **Ignored content** | The bundled file might be unnecessary or poorly signaled |

### Critical Metadata

The `name` and `description` in your Skill's metadata are particularly critical. The agent uses these when deciding whether to trigger the Skill in response to the current task. Make sure they clearly describe:
- What the Skill does
- When it should be used

Some platforms like Claude Code support additional fields like `hints`. If you want your skill to work across multiple platforms, stick to the minimum set (`name`, `description`).

