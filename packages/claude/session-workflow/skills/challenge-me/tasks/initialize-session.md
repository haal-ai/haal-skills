---
task_id: "initialize-session"
task_name: "Initialize Ideation Session"
dependencies: ["timestamp", "subject"]
---

# Task: Initialize Ideation Session

## Input Context
**Required Context Variables**: 
- `timestamp`: Session timestamp (YYYYMMDD-HHMM format)
- `subject`: The ideation topic

**Required Files**: None
**Required Tools**: None

## Task Instructions

### 1. Create Session Identifier
Extract 3-word subject identifier from `subject`:
- Convert to kebab-case
- Use only first 3 meaningful words
- Example: "improving microservices architecture" → "improving-microservices-architecture"
- Example: "AI chatbot design" → "ai-chatbot-design"

Create session identifier: `<subject-3-words>-<timestamp>`

### 2. Initialize Trajectory Tracking
Create trajectory structure:
```
Initial State:
- Subject: <subject>
- Timestamp: <timestamp>
- Starting Thoughts: <initial_thoughts>
- Source Paths: <codebase_path>, <documentation_path>, <web_search_urls>
```

### 3. Set Up Framework
Initialize:
- Cycle counter: 0
- Challenge tracking: empty list
- Insight tracking: empty list
- Source citations: empty list
- Recommendations tracking: empty list

### 4. Confirm Initialization
Display to user:
```
✅ Session Initialized
   Session ID: <session_identifier>
   Subject: <subject>
   Research Sources:
   - Codebase: <codebase_path or "Not provided">
   - Documentation: <documentation_path or "Not provided">
   - Web Search: <web_search_urls or "General search">
   Challenge Intensity: <challenge_intensity>
   Research Depth: <research_depth>
```

## Output Requirements

**Context Variables Created**:
- `session_identifier`: Unique session ID (<subject-3-words>-YYYYMMDD-HHMM)
- `subject_3_words`: 3-word kebab-case subject identifier
- `cycle_counter`: Initialized to 0
- `trajectory`: Initialized trajectory structure
- `challenges_list`: Empty list for tracking challenges
- `insights_list`: Empty list for tracking insights
- `citations_list`: Empty list for tracking sources
- `recommendations_list`: Empty list for tracking recommendations

**Files Created**: None
