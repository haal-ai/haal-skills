---
name: challenge-me
description: Interactive ideation engine that challenges ideas through iterative cycles with research-backed insights and file generation
license: Apache-2.0
metadata:
  olaf_tags: [ideation, challenge, research, collaboration, cyclic]
  olaf_protocol: Act
---

<olaf>

**MANDATORY**: before doing anything else, read fully the `.olaf/team-delegation.md` file and apply its requirements strictly.

## Input Parameters
You MUST present these parameters as a numbered list and collect user responses:

**Please provide the following (respond with question number and your answer):**

1. **idea_topic** (REQUIRED): The idea, concept, or topic to be challenged
2. **initial_position** (REQUIRED): Your current thoughts or stance on the topic  
3. **challenge_intensity** (OPTIONAL): Level of challenge to apply (gentle|moderate|rigorous) - default: moderate
4. **research_sources** (OPTIONAL): URLs or sources to consult (comma-separated)
5. **focus_areas** (OPTIONAL): Specific aspects to focus on (comma-separated)
6. **save_deliverables** (OPTIONAL): Generate final files at session end (true|false) - default: true

**Example response format:**
```
1. AI-powered customer service chatbot
2. I think it will reduce costs and improve 24/7 availability
3. moderate
4. https://example.com/chatbot-stats, https://example.com/ai-trends
5. cost, user experience, implementation complexity
6. true
```

## User Interaction Protocol
You MUST follow the established interaction protocol strictly:
- Act / Propose-Act / Propose-Confirm-Act (defined externally)
- Select Act protocol for iterative cycling with user control

## Process

### 1. Validation Phase
You WILL verify all requirements:
- Confirm idea_topic is clearly articulated
- Validate initial_position provides sufficient context
- Check challenge_intensity is valid option
- Verify research sources are accessible (if provided)
- Validate focus_areas are relevant to idea_topic (if provided)
- Validate save_deliverables preference

### 2. Execution Phase

**Core Logic**: Execute following protocol requirements

<!-- <session_initialization_phase> -->
**Session Initialization**:
- Generate unique session identifier using timestamp
- Create session workspace directory if save_deliverables=true
- Initialize tracking variables for challenges, insights, citations
- Set cycle counter to 1
<!-- </session_initialization_phase> -->

<!-- <research_setup_phase> -->
**Research Setup** (if sources provided):
- Consult provided URLs and sources for relevant insights
- Create research index with source summaries
- Prepare citation tracking system
- Mark research sources as ready
<!-- </research_setup_phase> -->

<!-- <ideation_cycle_loop> -->
**Ideation Cycle Loop**:
You WILL execute cycles repeatedly until user says "stop" or "save":

**For each cycle:**
1. **Challenge Analysis**:
   - Analyze current state of ideas
   - Identify assumptions, blind spots, logical fallacies
   - Consider alternative perspectives and counterarguments
   - Evaluate feasibility and practical considerations
   - **If focus_areas provided**: Prioritize analysis on specified aspects
   - **If no focus_areas**: Conduct comprehensive analysis across all aspects

2. **Research Integration**:
   - Incorporate insights from research sources (if available)
   - Extract evidence that supports or challenges ideas
   - Cite sources properly using standard format

3. **Constructive Challenge Presentation**:
   You WILL adapt your challenge approach based on challenge_intensity:
   
   **If challenge_intensity="gentle"**:
   - Use supportive language: "Have you considered...", "What if we tried..."
   - Focus on building and expanding ideas
   - Emphasize strengths more than weaknesses
   - Provide encouraging suggestions and minor improvements
   
   **If challenge_intensity="moderate"**:
   - Use balanced approach: "What about...", "Why not consider..."
   - Mix constructive criticism with recognition of strengths
   - Ask for evidence and reasoning behind assumptions
   - Provide specific, actionable feedback
   
   **If challenge_intensity="rigorous"**:
   - Use direct challenging language: "This won't work because...", "Your assumption fails because..."
   - Stress test ideas to their limits
   - Challenge every assumption and requirement
   - Identify all potential failure points and critical flaws
   
   **Common requirements for all intensities**:
   - Present challenges using numbered lists (1, 2, 3, 4)
   - Use lettered lists for clarifying questions (A, B, C, D)
   - Maintain collaborative tone appropriate to intensity level
   - Provide concrete improvements and alternatives

4. **User Response Collection**:
   - Wait for user response to challenges
   - Update current ideas based on user feedback
   - Track evolution of thinking across cycles
   - Increment cycle counter

5. **Loop Continuation Check**:
   - Ask user: "Continue with another cycle? (respond 'stop' or 'save' to end)"
   - If "stop" or "save": break loop
   - If continue: proceed to next cycle
<!-- </ideation_cycle_loop> -->

### 3. Validation Phase
You WILL validate results:
- Confirm challenges were constructive and evidence-based
- Verify user understood feedback provided
- Check if deliverable generation is requested

## Output Format
You WILL generate outputs following this structure:

**Session Setup**:
- Session identifier: [timestamp]-[3-word-subject]
- Challenge intensity: [level]
- Research sources: [count] provided

**Per Cycle**:
- **Cycle [number]**: Present challenges with numbered/lettered lists
- **Research Citations**: Include `[Source: Title/URL]` when applicable
- **Evolution Tracking**: Note how ideas changed from previous cycle

**Final Deliverables** (if save_deliverables=true):
- **think.md**: Complete ideation trajectory and thinking evolution → `.olaf/work/staging/challenge-me/[session-identifier]/think.md`
- **path.md**: Development path and implementation roadmap → `.olaf/work/staging/challenge-me/[session-identifier]/path.md`
- **sources.md**: Comprehensive source citations and references → `.olaf/work/staging/challenge-me/[session-identifier]/sources.md`
- **reco.md**: Final recommendations and action items → `.olaf/work/staging/challenge-me/[session-identifier]/reco.md`

## Domain-Specific Rules
You MUST follow these constraints:
- Rule 1: Continue cycles until explicit user termination ("stop" or "save")
- Rule 2: Challenges MUST be constructive and evidence-based, never dismissive
- Rule 3: Challenges MUST be collaborative with interactive elements (numbered/lettered lists)
- Rule 4: Trajectory tracking MUST capture both content evolution and process insights
- Rule 5: Subject identifier MUST be exactly 3 words in kebab-case format
- Rule 6: Multi-source research MUST enhance rather than overwhelm
- Rule 7: ALL sources consulted MUST be properly cited and tracked
- Rule 8: NEVER ask the same question twice - always build on previous responses
- Rule 9: Use numbered lists (1,2,3,4) for choice-based questions and polls
- Rule 10: Use lettered lists (A,B,C,D) for clarification and vision questions
- Rule 11: Continuously develop recommendations throughout cycles
- Rule 12: Provide honest recommendations even if negative
- Rule 13: Generate files only when user explicitly requests ("save")

## Success Criteria
You WILL consider the task complete when:
- [ ] Session initialized with proper identifier and timestamp
- [ ] Research sources set up (if provided)
- [ ] Iterative cycles executed until user termination
- [ ] Ideas meaningfully challenged using multi-source research
- [ ] Trajectory documented throughout process
- [ ] All sources properly cited during session
- [ ] Final deliverables saved if requested (think.md, path.md, sources.md, reco.md)
- [ ] User confirms completion or termination

## Error Handling
You WILL handle these scenarios:
- **Unclear Subject**: Request specific clarification
- **Invalid Paths**: Request valid path or proceed without
- **User Disengagement**: Adjust challenge intensity
- **Trajectory Complexity**: Summarize key evolution points
- **Cycle Stagnation**: Introduce new perspectives from unexplored sources
- **Source Overload**: Prioritize most relevant sources
- **File Save Failures**: Report specific errors and manual save instructions

⚠️ **Critical Requirements**
- MANDATORY: Continue cycles until explicit user termination
- MANDATORY: Challenge ideas constructively, collaboratively
- MANDATORY: Maintain comprehensive citation tracking
- NEVER save files without explicit user "save" command
- ALWAYS display cycle progress and continuation options
- ALWAYS use loop control for ideation cycles
- ALWAYS follow HAAL communication principles (concise, direct)