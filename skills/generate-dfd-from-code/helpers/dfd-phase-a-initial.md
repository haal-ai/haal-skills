# DFD Phase A: Initial Analysis (Steps 1-3)

## Prerequisites Check
- [ ] Master progress file (`DFD_master_progress.md`) exists
- [ ] Steps 1-3 are marked as incomplete
- [ ] No `DFD_level1_tasks.md` file exists yet

---

## Step 1: Initial System Understanding

### 1.1 Identify Application Type and Purpose
**Analyze the following:**
- What does the application do?
- What is its primary domain (web app, desktop app, microservices, API, etc.)?
- What programming languages and frameworks are used?

### 1.2 Examine Codebase Structure
**Look for:**
- Directory structure and file organization
- Configuration files, build files, and deployment scripts
- Documentation (README, API docs, etc.)

### 1.3 Identify Key Technologies and Patterns
**Investigate:**
- Databases and data storage
- Communication protocols (HTTP, message queues, etc.)
- External services and APIs
- Authentication and security mechanisms

**📄 Update Master Progress:**
- Mark Step 1 as complete: `[x] **Step 1**: Initial System Understanding`
- Update "Last Updated" timestamp
- Add key findings to master progress notes

---

## Step 2: Context Diagram Creation

### 2.1 Identify External Entities
**Look for:**
- Users (different types if applicable)
- External systems and services
- Third-party APIs
- Databases (if external)
- File systems
- Network services

### 2.2 Define System Boundary
**Establish:**
- The application as a single black box
- Clear definition of what's inside vs. outside the system

### 2.3 Map Data Flows
**Document:**
- Input data from external entities to the system
- Output data from the system to external entities
- Bi-directional flows where applicable

### 2.4 Create Context Diagram Documentation

**Add to your main analysis document (`{project}_analysis.md`):**

```markdown
# {Application Name} - Data Flow Diagrams

## Application Overview
- **Purpose:** [What the application does]
- **Type:** [Web app, API, microservices, desktop, etc.]
- **Technologies:** [Languages, frameworks, databases]
- **Architecture:** [Monolith, microservices, serverless, etc.]

## Context Diagram

### External Entities:
1. **[Entity Name]** - [Description and role]
2. **[Entity Name]** - [Description and role]
...

### System Interactions:
- [Entity] → System: [Input data/requests]
- System → [Entity]: [Output data/responses]
...

### ASCII Context Diagram:
```
[External Entity 1] ──> [System] ──> [External Entity 2]
        ↑                               ↓
[External Entity 3] <───────────────────┘
```
```

**📄 Update Master Progress:**
- Mark Step 2 as complete: `[x] **Step 2**: Context Diagram Creation`
- Update context diagram status

---

## Step 3: Level 1 DFD Task Planning

### 3.1 Create Level 1 Task File

**Create `DFD_level1_tasks.md` with the following structure:**

```markdown
# Level 1 DFD Analysis Tasks for {Application Name}

## Task Checklist

### Phase 1: Process Identification
- [ ] **Task 1.1**: Identify input/output handling processes
- [ ] **Task 1.2**: Identify authentication/authorization processes
- [ ] **Task 1.3**: Identify core business logic processes
- [ ] **Task 1.4**: Identify data processing/transformation processes
- [ ] **Task 1.5**: Identify external service integration processes
- [ ] **Task 1.6**: Identify logging/monitoring processes
- [ ] **Task 1.7**: Identify configuration management processes
- [ ] **Task 1.8**: Identify error handling processes

### Phase 2: Data Store Identification
- [ ] **Task 2.1**: Identify primary databases
- [ ] **Task 2.2**: Identify cache systems
- [ ] **Task 2.3**: Identify file storage systems
- [ ] **Task 2.4**: Identify configuration stores
- [ ] **Task 2.5**: Identify session/temporary data stores
- [ ] **Task 2.6**: Identify log storage
- [ ] **Task 2.7**: Identify backup/archive storage

### Phase 3: Data Flow Mapping
- [ ] **Task 3.1**: Map external entity → process flows
- [ ] **Task 3.2**: Map process → process flows
- [ ] **Task 3.3**: Map process → data store flows
- [ ] **Task 3.4**: Map data store → process flows
- [ ] **Task 3.5**: Map process → external entity flows

### Phase 4: Documentation
- [ ] **Task 4.1**: Create process descriptions
- [ ] **Task 4.2**: Create data flow descriptions
- [ ] **Task 4.3**: Create ASCII diagram
- [ ] **Task 4.4**: Document key data elements
- [ ] **Task 4.5**: Validate completeness and accuracy

## Progress Tracking
**Current Phase**: Phase 1
**Last Completed Task**: None
**Next Task**: Task 1.1
**Estimated Completion**: 0/25 tasks completed
```

**📄 Update Master Progress:**
- Mark Step 3 as complete: `[x] **Step 3**: Level 1 DFD Task Planning`
- Update file status: `[x] DFD_level1_tasks.md - Level 1 task tracking`
- Update current phase: `**Current Phase:** Phase B`
- Update next step: `**Next Step:** 4`

---

## Phase A Completion

### Final Phase A Updates

**Update Master Progress File:**
```markdown
### Phase A: Initial Analysis - COMPLETED
- [x] **Step 1**: Initial System Understanding
- [x] **Step 2**: Context Diagram Creation
- [x] **Step 3**: Level 1 DFD Task Planning

**Current Status**
**Active Phase:** B
**Next Step:** 4
**Ready for User Review:** Yes
```

### 🛑 USER REVIEW REQUIRED

Before proceeding to Phase B, the user must:
1. Review `{project}_analysis.md` for context diagram quality
2. Review `DFD_level1_tasks.md` for task planning completeness
3. Verify master progress file reflects actual completion
4. Confirm readiness for Phase B

---

## Technology-Specific Analysis Guidelines

### Web Applications
- Look for: Controllers, views, models, routing, session management
- Common processes: Request handling, authentication, business logic, response generation
- Data stores: Databases, session storage, cache

### Microservices
- Look for: Service boundaries, API gateways, service discovery, inter-service communication
- Common processes: API gateway, individual services, load balancing, monitoring
- Data stores: Per-service databases, shared databases, message queues

### APIs/Backend Services
- Look for: Endpoints, middleware, authentication, data validation
- Common processes: Request validation, business logic, data access, response formatting
- Data stores: Databases, cache, logs

### Desktop Applications
- Look for: UI components, file I/O, local storage, external communications
- Common processes: UI handling, business logic, file processing, configuration
- Data stores: Local files, databases, configuration files
