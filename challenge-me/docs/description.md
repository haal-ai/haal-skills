# challenge-me

## Overview
Interactive ideation engine that challenges ideas through iterative cycles with research-backed insights and optional file generation.

## Purpose
Stress-test ideas, identify blind spots, and refine thinking through structured challenge cycles with adjustable intensity.

## Key Features
- Iterative challenge cycles until user stops
- Three intensity levels: gentle, moderate, rigorous
- Research integration with source citations
- Tracks idea evolution across cycles
- Generates deliverable files on request

## Usage
```
@challenge-me
```

## Parameters
| Parameter | Required | Description |
|-----------|----------|-------------|
| idea_topic | Yes | The idea or concept to challenge |
| initial_position | Yes | Your current stance on the topic |
| challenge_intensity | No | gentle, moderate (default), rigorous |
| research_sources | No | URLs to consult (comma-separated) |
| focus_areas | No | Specific aspects to focus on |
| save_deliverables | No | Generate files at end (default: true) |

## Process Flow
1. Initializes session with unique identifier
2. Sets up research sources if provided
3. Executes challenge cycles:
   - Analyzes assumptions and blind spots
   - Integrates research insights
   - Presents challenges based on intensity
   - Collects user responses
4. Continues until user says "stop" or "save"
5. Generates deliverables if requested

## Output
Session deliverables (saved on "save" command):
- `think.md` - Ideation trajectory
- `path.md` - Implementation roadmap
- `sources.md` - Source citations
- `reco.md` - Final recommendations

Location: `.olaf/work/staging/challenge-me/[session-id]/`

## Error Handling
| Scenario | Resolution |
|----------|------------|
| Unclear subject | Requests clarification |
| User disengagement | Adjusts challenge intensity |
| Cycle stagnation | Introduces new perspectives |

## Related Skills
- `research-and-report` - Deep research on topics
- `assess-genai-initiative-idea` - AI initiative assessment
