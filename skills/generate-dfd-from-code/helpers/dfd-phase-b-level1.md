# DFD Phase B: Level 1 Analysis (Steps 4-7)

## Prerequisites Check
- [ ] Master progress shows Steps 1-3 completed
- [ ] `DFD_level1_tasks.md` file exists
- [ ] Steps 4-7 are marked as incomplete
- [ ] Context diagram is complete

---

## Step 4: Level 1 DFD Creation

### 4.1 Execute Level 1 Tasks

**Work through `DFD_level1_tasks.md` systematically:**

#### Phase 1: Process Identification (Tasks 1.1-1.8)
- Mark each task complete [x] as you work through them
- Document findings in the notes sections
- Update progress tracking regularly

#### Phase 2: Data Store Identification (Tasks 2.1-2.7)
- Identify all major data stores
- Focus on logical data categories, not implementation details
- Document purpose and access patterns

#### Phase 3: Data Flow Mapping (Tasks 3.1-3.5)
- Map all significant data movements
- Ensure external entities connect properly
- Validate internal process communications

#### Phase 4: Documentation (Tasks 4.1-4.5)
- Create comprehensive process descriptions
- Document all data flows with clear labels
- Create ASCII diagram
- Validate completeness

### 4.2 Create Level 1 DFD Documentation

**Add to your main analysis document (`{project}_analysis.md`):**

```markdown
## Level 1 Data Flow Diagram

### External Entities:
[Carry forward from context diagram]

### Processes:
1. **P1: [Process Name]** - [Description]
2. **P2: [Process Name]** - [Description]
...

### Data Stores:
- **D1: [Store Name]** - [Description]
- **D2: [Store Name]** - [Description]
...

### Data Flows:

**From External Entities:**
- [Entity] → [Process]: [Data description]

**Between Processes:**
- [Process A] → [Process B]: [Data description]

**To/From Data Stores:**
- [Process] → [Data Store]: [Data description]
- [Process] ← [Data Store]: [Data description]

**To External Entities:**
- [Process] → [Entity]: [Data description]

### Process Descriptions:
**P1: [Process Name]**
- [Detailed description of what this process does]
- [Input data and sources]
- [Processing logic]
- [Output data and destinations]

### ASCII Level 1 Diagram:
```
[External Entity] → [P1: Process] → [D1: Data Store]
                           ↓
                    [P2: Process] → [External Entity]
```

### Key Data Elements:
- **[Data Type 1]:** [Description]
- **[Data Type 2]:** [Description]
```

**📄 Update Master Progress:**
- Mark Step 4 as complete: `[x] **Step 4**: Level 1 DFD Creation`
- Update Level 1 DFD status: `**Level 1 DFD:** Complete`

---

## Step 5: Level 1 vs Level 2 Validation

### 5.1 Level 1 Validation Checklist

**✅ Level 1 Should Show:**
- [ ] **Major business functions** (5-9 processes maximum)
- [ ] **Primary data transformations** (input → processing → output)
- [ ] **High-level data stores** (not implementation details)
- [ ] **External entity interactions** only
- [ ] **What the system does** (not how it does it)

**❌ Move to Level 2 if you have:**
- [ ] More than 9 processes (too detailed)
- [ ] Implementation-specific details (specific algorithms, libraries)
- [ ] Internal sub-processes of a major function
- [ ] Technology-specific operations (individual APIs, specific file formats)
- [ ] Detailed error handling or validation steps

### 5.2 Validation Questions

1. **Process Count Check:** Do you have more than 7-9 processes?
   - If YES: Group related processes into higher-level functions

2. **Abstraction Level Check:** Are your processes describing "how" rather than "what"?
   - If YES: Abstract to higher-level business functions

3. **Implementation Detail Check:** Do process names mention specific technologies?
   - If YES: Use generic functional names instead

4. **Data Store Check:** Are data stores showing internal data structures?
   - If YES: Group into logical data categories

### 5.3 Document Validation Results

**Add validation results to master progress:**
```markdown
### Validation Results:
- **Level 1 Process Count:** [Number] (Target: 5-9)
- **Abstraction Level:** [Appropriate/Too Detailed/Too High]
- **Refinement Needed:** [Yes/No]
```

**📄 Update Master Progress:**
- Mark Step 5 as complete: `[x] **Step 5**: Level 1 vs Level 2 Validation`

---

## Step 6: Level 1 Refinement (if needed)

### 6.1 Refinement Actions (Only if Step 5 identified issues)

**Combine Processes:**
- Group sub-functions into larger business processes
- Reduce process count to 5-9

**Abstract Data Stores:**
- Show logical data categories, not implementation
- Remove technology-specific details

**Simplify Process Names:**
- Focus on business function, not technology
- Use "what" language, not "how" language

**Reserve Details:**
- Move implementation details to Level 2 planning
- Keep Level 1 at appropriate abstraction

**📄 Update Master Progress:**
- Mark Step 6 as complete: `[x] **Step 6**: Level 1 Refinement (if needed)`

---

## Step 7: Level 2 Decision and Task Planning

### 7.1 Level 2 Decision

**Create Level 2 when:**
- Level 1 process is complex and performs multiple distinct functions
- Stakeholders need to understand internal workings
- Process will be modified or extended
- Process has complex error handling or decision logic

**Level 1 is sufficient when:**
- Process is straightforward with single clear function
- Internal details are not relevant to stakeholders
- Process is unlikely to change
- Time/resources are limited

### 7.2 Document Decision (CRITICAL)

**Add this EXACT section to master progress:**

**If Level 2 is required:**
```markdown
### Level 2 Required?
- **Decision:** Yes
- **Reason:** [Specific justification]
- **Processes requiring Level 2:** [List process names]
- **Task File Created:** Yes - DFD_level2_tasks.md
- **Decision Date:** [Date]
```

**If Level 2 is NOT required:**
```markdown
### Level 2 Required?
- **Decision:** No
- **Reason:** Level 1 provides sufficient detail for intended purpose
- **Processes requiring Level 2:** None
- **Task File Created:** No - Level 2 not needed
- **Decision Date:** [Date]
```

### 7.3 Create Level 2 Task File (if needed)

**If Level 2 is required, create `DFD_level2_tasks.md`:**

```markdown
# Level 2 DFD Analysis Tasks for {Application Name}

## Level 2 Scope
**Processes to Decompose:** [List Level 1 processes requiring Level 2]
**Justification:** [Complexity/Stakeholder needs/Implementation details needed]

## Task Checklist

### Phase 1: Sub-Process Identification
- [ ] **Task 1.1**: Identify input validation/parsing sub-processes
- [ ] **Task 1.2**: Identify core algorithm/logic sub-processes
- [ ] **Task 1.3**: Identify data transformation sub-processes
- [ ] **Task 1.4**: Identify output formatting sub-processes
- [ ] **Task 1.5**: Identify error handling sub-processes
- [ ] **Task 1.6**: Identify logging/monitoring sub-processes

### Phase 2: Internal Data Store Identification
- [ ] **Task 2.1**: Identify temporary/working data stores
- [ ] **Task 2.2**: Identify cache/buffer data stores
- [ ] **Task 2.3**: Identify configuration/lookup data stores
- [ ] **Task 2.4**: Identify intermediate result data stores

### Phase 3: Sub-Process Data Flow Mapping
- [ ] **Task 3.1**: Map input flows to first sub-process
- [ ] **Task 3.2**: Map sub-process to sub-process flows
- [ ] **Task 3.3**: Map sub-process to internal data store flows
- [ ] **Task 3.4**: Map final sub-process to output flows
- [ ] **Task 3.5**: Map error/exception flows

### Phase 4: Level 2 Documentation
- [ ] **Task 4.1**: Create sub-process descriptions
- [ ] **Task 4.2**: Create internal data flow descriptions
- [ ] **Task 4.3**: Create Level 2 ASCII diagram
- [ ] **Task 4.4**: Document internal data elements
- [ ] **Task 4.5**: Validate Level 2 completeness

## Progress Tracking
**Current Phase**: Phase 1
**Last Completed Task**: None
**Next Task**: Task 1.1
**Estimated Completion**: 0/20 tasks completed
```

**📄 Update Master Progress:**
- Mark Step 7 as complete: `[x] **Step 7**: Level 2 Task Planning`
- Update current phase based on Level 2 decision:
  - If Level 2 = Yes: `**Active Phase:** C`, `**Next Step:** 8`
  - If Level 2 = No: `**Active Phase:** D`, `**Next Step:** 10`

---

## Phase B Completion

### Final Phase B Updates

**If Level 2 = Yes:**
```markdown
### Phase B: Level 1 Analysis - COMPLETED
- [x] **Step 4**: Level 1 DFD Creation
- [x] **Step 5**: Level 1 vs Level 2 Validation
- [x] **Step 6**: Level 1 Refinement (if needed)
- [x] **Step 7**: Level 2 Task Planning

**Current Status**
**Active Phase:** C
**Next Step:** 8
**Ready for User Review:** Yes
```

**If Level 2 = No:**
```markdown
### Phase B: Level 1 Analysis - COMPLETED
- [x] **Step 4**: Level 1 DFD Creation
- [x] **Step 5**: Level 1 vs Level 2 Validation
- [x] **Step 6**: Level 1 Refinement (if needed)
- [x] **Step 7**: Level 2 Task Planning

**Current Status**
**Active Phase:** D
**Next Step:** 10
**Ready for User Review:** Yes
```

### 🛑 USER REVIEW REQUIRED

Before proceeding to next phase, the user must:
1. Check Level 1 DFD quality and completeness
2. Verify validation results are accurate
3. Confirm Level 2 decision is appropriate
4. Review master progress file accuracy

**Next Phase:**
- If Level 2 required: Proceed to Phase C (helpers/dfd-phase-c-level2.md)
- If Level 2 not required: Skip to Phase D (helpers/dfd-phase-d-final.md)
