# Product Requirements Document (PRD): {Product/Feature Name}

**Purpose**: Agile-focused template for documenting user stories and iterative development  
**Used By**: review-prd-spec.md  
**Template Type**: Agile  
**Version**: 1.0  
**Last Updated**: 2025-11-19

---

## Sprint Overview

| Field | Value |
|-------|-------|
| **Epic ID** | {EPIC-YYYYMMDD-NNN} |
| **Feature Name** | {project_name} |
| **Sprint Version** | {sprint_number} |
| **Sprint Start** | {YYYY-MM-DD} |
| **Sprint End** | {YYYY-MM-DD} |
| **Product Owner** | {po_name} |
| **Scrum Master** | {sm_name} |
| **Dev Team** | {team_members} |

---

## Table of Contents

1. [Epic Summary](#1-epic-summary)
2. [User Stories](#2-user-stories)
3. [Acceptance Criteria](#3-acceptance-criteria)
4. [Technical Tasks](#4-technical-tasks)
5. [Definition of Ready](#5-definition-of-ready)
6. [Definition of Done](#6-definition-of-done)
7. [Sprint Goals](#7-sprint-goals)
8. [Dependencies & Blockers](#8-dependencies--blockers)

---

## 1. Epic Summary

### 1.1 Epic Goal
{What problem are we solving for users?}

### 1.2 User Value
{How will this improve the user experience?}

### 1.3 Business Value
{What business metrics will this improve?}

### 1.4 Success Metrics
| Metric | Current | Target | How Measured |
|--------|---------|--------|--------------|
| {metric_name} | {current_value} | {target_value} | {measurement_method} |

---

## 2. User Stories

### Story 1: {Story Title}
**Story ID**: {US-NNN}  
**Priority**: {High/Medium/Low}  
**Story Points**: {points}  

**As a** {user_type}  
**I want** {functionality}  
**So that** {benefit/value}  

**Additional Context**: {any_additional_details}

### Story 2: {Story Title}
{Similar structure}

---

## 3. Acceptance Criteria

### Story {US-NNN}: {Story Title}

#### Scenario 1: {Scenario Name}
**Given** {precondition}  
**When** {action}  
**Then** {expected_result}  

#### Scenario 2: {Scenario Name}
**Given** {precondition}  
**When** {action}  
**Then** {expected_result}  

**Edge Cases**:
- {Edge case 1}
- {Edge case 2}

---

## 4. Technical Tasks

### Development Tasks
| Task | Owner | Estimate | Dependencies | Status |
|------|-------|----------|--------------|--------|
| {task_description} | {developer_name} | {hours/points} | {dependencies} | {status} |

### Testing Tasks
| Task | Owner | Estimate | Type | Status |
|------|-------|----------|------|--------|
| {test_description} | {tester_name} | {hours} | {unit/integration/e2e} | {status} |

---

## 5. Definition of Ready

- [ ] User story is clearly written and understood
- [ ] Acceptance criteria are defined and testable
- [ ] Story is properly sized (not too large for a sprint)
- [ ] Dependencies are identified and resolved
- [ ] Technical approach is understood
- [ ] UI/UX designs are available (if needed)
- [ ] Performance criteria are defined (if applicable)

---

## 6. Definition of Done

- [ ] Code is written and follows coding standards
- [ ] Unit tests are written and passing (>80% coverage)
- [ ] Integration tests are written and passing
- [ ] Code review is completed and approved
- [ ] Feature is deployed to staging environment
- [ ] Acceptance criteria are verified by PO/QA
- [ ] Documentation is updated
- [ ] Feature is deployed to production

---

## 7. Sprint Goals

### Primary Goal
{Main objective for this sprint}

### Secondary Goals
- {Secondary objective 1}
- {Secondary objective 2}

### Sprint Commitment
{What the team commits to deliver this sprint}

### Risk Assessment
| Risk | Impact | Probability | Mitigation |
|------|--------|-------------|------------|
| {risk_description} | {H/M/L} | {H/M/L} | {mitigation_plan} |

---

## 8. Dependencies & Blockers

### Dependencies
| Dependency | Type | Owner | Expected Resolution | Impact |
|------------|------|-------|-------------------|--------|
| {dependency_description} | {Internal/External} | {owner_name} | {YYYY-MM-DD} | {impact_description} |

### Current Blockers
| Blocker | Impact | Owner | Target Resolution |
|---------|--------|-------|------------------|
| {blocker_description} | {impact_level} | {responsible_person} | {YYYY-MM-DD} |

### Assumptions
- {Assumption 1}
- {Assumption 2}

---

## Retrospective Items

### What Went Well
- {Item 1}
- {Item 2}

### What Could Be Improved
- {Item 1}
- {Item 2}

### Action Items
- {Action item 1} - Owner: {name} - Due: {date}
- {Action item 2} - Owner: {name} - Due: {date}

---

## Placeholder Guide

- `{project_name}`: Short identifier for the feature/epic
- `{sprint_number}`: Current sprint number (e.g., Sprint 15)
- `{US-NNN}`: User story identifier (e.g., US-001)
- `{user_type}`: Specific user role or persona
- `{functionality}`: What the user wants to do
- `{benefit/value}`: Why the user wants this functionality
- `{points}`: Story points estimate (1, 2, 3, 5, 8, 13, 21)
- `{H/M/L}`: High/Medium/Low rating

## Notes

- Stories should be INVEST (Independent, Negotiable, Valuable, Estimable, Small, Testable)
- Acceptance criteria should be written in Given/When/Then format
- Story points should reflect complexity, not time
- All dependencies should be identified before sprint planning
- Definition of Done should be consistent across the team
- Regular retrospectives should inform process improvements