# BMS Management (Testing, Delivery, Contributions)

## Summary
This section covers how BMS is managed as a shared build tool used by 1,500+ C++ developers with 2,000,000 weekly executions. It explains version management (stable, beta, previous), backward compatibility guarantees, change request processes, support channels, and contribution guidelines. Understanding this is critical when requesting features, reporting issues, or contributing to BMS.

> This documentation defines the operational rules and processes for BMS, including how versions are maintained, how changes are prioritized, and how users should interact with the BMS team.

---

## Key Concepts
- **Three-tier versioning**: BMS stable (default), BMS beta (next release), BMS previous (emergency fallback only)
- **Backward compatibility guarantee**: All delivered Descriptions remain readable and interpretable across all future BMS versions
- **Forward compatibility window**: 3-version forward compatibility for beta testers to prevent breaking non-beta users
- **Support prioritization**: Urgent problems → non-urgent problems → urgent features → chronological feature queue
- **Change rejection criteria**: Changes that break BMS axioms, backward compatibility, cause support burden, or require massive refactoring are rejected
- **Documentation-first policy**: Users must check documentation before requesting support to avoid wasting resources

---

## Usage

### Version Selection
- **Default**: Always use BMS stable unless explicitly opting into beta
- **Beta testing**: Encouraged for early adoption; safe due to 3-version forward compatibility
- **Previous version**: Only use as temporary workaround for critical bugs in stable

### Requesting Changes
1. Discuss with BMS administrators first
2. Once agreed, open ticket via [R&D Request Portal](http://rndwww.nce.amadeus.net/rndrequest/) with category `BMS`
3. Expect rejection if the change:
   - Breaks BMS axioms (library uniqueness, name/version uniqueness, warning visibility)
   - Breaks backward compatibility for delivered Descriptions
   - Creates significant support burden
   - Requires extensive BMS refactoring
   - Tunes BMS for a single project's needs (exceptions rare)

### Problem Reporting
- See "Reporting bugs" documentation
- **Never request a fallback** — explain the issue; BMS admins will determine the solution
- Exceptional actions are decided and executed by BMS administrators

### Getting Support
Support channels (in order of preference):
1. [R&D Request Portal](http://rndwww.nce.amadeus.net/rndrequest/) with topic `BMS`
2. [BMS admin mailing list](mailto:NCE-BMS-Admin@amadeus.com)
3. Chat with current "sheriff" (BMS administrator on support rotation)

**Pre-requisite**: Check documentation first — BMS admins are not a living documentation service

### Contributing
Follow the [contribution guidelines](https://rndwww.nce.amadeus.net/git/projects/BMS/repos/bms/browse/CONTRIBUTING.md) to implement features yourself and bypass the potentially long feature queue.

---

## Backward/Forward Compatibility Rules

```text
Backward Compatibility (strict):
- Delivered Description in BMS v1 → readable in all BMS v2, v3, v4...
- Breaking changes to local components (options/plugins) documented in release notes

Forward Compatibility (3 versions):
- Description created in BMS beta → readable in previous 3 stable versions
- New features that break this rule documented with risk warnings
- Beta users must wait for next release before using such features if fallback is required
```

---

## Change Management Process

```text
Priority Order:
1. Urgent Problems (critical bugs)
2. Non-urgent Problems
3. Urgent Features (identified by BMS admins + management)
4. Other Features (chronological queue — potentially very long)

Alternatives:
- Implement changes yourself via contribution process
- Wait in chronological queue
```

---

## Documentation Policy
- BMS documentation must be **exhaustive** and **up to date**
- Report documentation issues via [R&D Request Portal](http://rndwww.nce.amadeus.net/rndrequest/)
- Users must check documentation before contacting support

---

## Scale and Context
- **Users**: 1,500+ OBE C++ developers
- **Usage**: 2,000,000 executions per week
- **Maintainers**: Small team of programmers
- **Implication**: Strict processes required to manage high-volume usage with limited resources
