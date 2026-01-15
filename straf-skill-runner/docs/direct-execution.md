# Direct STRAF Skill Execution - No Intermediate Files

## Problem with Current Approach

**Current Flow** (Complex):
```
STRAF Skill Runner 
  → Generates Python spawner script (.py file)
  → Executes spawner script
  → Spawner calls STRAF agent
  → Multiple failure points (console I/O, paths, encoding)
```

**Issues**:
- Unnecessary intermediate file generation
- Complex error handling across multiple processes
- Console I/O issues in spawned processes
- Path resolution problems

## New Approach: Direct Function Call

**Simplified Flow**:
```
Python function call 
  → Direct STRAF agent invocation
  → Results returned or tracked
```

## Usage Examples

### Example 1: Simple Direct Call (Blocking)

```python
from pathlib import Path
import sys

# Add STRAF utils to path
sys.path.insert(0, str(Path.cwd() / "~/skills/straf-skill-runner/utils"))
from direct_executor import execute_skill_direct

# Execute skill directly - blocks until complete
result = execute_skill_direct(
    skill_path="~/skills/search-and-learn/prompts/search-and-learn.md",
    context_params={
        "learning_objective": "AWS Strands Agents multi-agent orchestration",
        "current_knowledge": "Exploring quick depth learning",
        "application_context": "Focus areas: architecture patterns"
    },
    tool_mode="full",
    background=False  # Wait for completion
)

print(f"Status: {result['status']}")
print(f"Results: {result.get('results', {}).get('response', 'N/A')}")
```

### Example 2: Background Execution (Non-blocking)

```python
from direct_executor import execute_skill_direct

# Execute in background - returns immediately
result = execute_skill_direct(
    skill_path="~/skills/search-and-learn/prompts/search-and-learn.md",
    context_params={
        "learning_objective": "GraphQL best practices",
        "current_knowledge": "Basic understanding",
        "application_context": "Production API development"
    },
    background=True  # Don't wait
)

print(f"Spawned: PID {result['pid']}")
print(f"Tracking: {result['tracking_file']}")
print(f"Logs: {result['log_file']}")

# Later, check status:
# python .olaf/core/agentic/straf/monitor_execution.py --execution-id {timestamp} --once
```

### Example 3: Command Line Usage

```bash
# Direct execution from command line (no intermediate file!)
python ~/skills/straf-skill-runner/utils/direct_executor.py \
  --skill-path ~/skills/search-and-learn/prompts/search-and-learn.md \
  --context '{"learning_objective": "Docker best practices", "current_knowledge": "Beginner", "application_context": "Microservices"}' \
  --tool-mode full \
  --background
```

### Example 4: Import and Use in Skill

```python
# In straf-skill-runner skill
from pathlib import Path
import sys

# Import direct executor
sys.path.insert(0, str(Path.cwd() / "~/skills/straf-skill-runner/utils"))
from direct_executor import execute_skill_direct

# Step 1: Analyze skill requirements (as before)
skill_analysis = analyze_skill(skill_path)

# Step 2: Gather context parameters (as before)
context_params = gather_context(skill_analysis['required_params'])

# Step 3: Execute DIRECTLY - no intermediate file!
result = execute_skill_direct(
    skill_path=skill_path,
    context_params=context_params,
    tool_mode=auto_detect_tool_mode(skill_analysis),
    background=True  # Or False for blocking
)

# Done! No spawner script generated.
```

## Advantages

✅ **No intermediate files** - Direct function call
✅ **Simpler error handling** - Single execution path
✅ **No console I/O issues** - Handled internally
✅ **Better debugging** - Direct stack traces
✅ **Reusable** - Can be imported anywhere
✅ **Same features** - Background/foreground, tracking, logging

## Comparison

| Feature | Current (Spawner Script) | New (Direct Call) |
|---------|-------------------------|-------------------|
| Intermediate files | ✗ Yes (.py spawner) | ✅ No |
| Lines of code | ~85 lines | ~10 lines to call |
| Error points | 5+ (file write, subprocess, console I/O) | 1 (execution only) |
| Console I/O issues | ✗ Yes (Unicode, pipes) | ✅ Handled |
| Debugging | ✗ Multi-process | ✅ Single process |
| Background mode | ✅ Yes | ✅ Yes |
| Tracking | ✅ Yes | ✅ Yes |

## Migration Path

### Before (Current):
```python
# Generate spawner script
spawner_script = generate_spawner_script(skill_path, context)
write_file(spawner_script_path, spawner_script)

# Execute spawner
subprocess.Popen(["python", spawner_script_path])
```

### After (New):
```python
# Direct execution - one line!
result = execute_skill_direct(skill_path, context, background=True)
```

## Conclusion

**Answer**: Yes, we CAN avoid the intermediate Python script!

The `direct_executor.py` provides a clean Python function that:
- Takes skill path and parameters
- Calls STRAF agent directly
- Returns results or tracking info
- No intermediate files needed
- All the same functionality, much simpler
