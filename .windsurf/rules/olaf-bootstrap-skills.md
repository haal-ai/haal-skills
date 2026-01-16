---
trigger: always_on
---


<olaf-session-bootstrap>

"BOOTSTRAP PROTOCOL - MANDATORY FIRST ACTION: Before responding to any user message in a new session, you MUST execute the context loading sequence: 
1) Check .olaf/context/current-context.md, 
2) Fallback to .olaf/data/context/context-current.md, 
3) Fallback to .olaf/data/context/context-default.md. 
Do not proceed until this completes."

**Context switching**:
- Instruct user to use the `switch-context` skill ("switch context").
- Tell them the new context only takes effect after starting a **new** conversation/session (bootstrap runs at session start).
</olaf-session-bootstrap>


On user request, always search for skills using your internal tools before doing anything else.

