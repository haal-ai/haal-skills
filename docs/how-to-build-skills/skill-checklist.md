# Skill Checklist

Use this checklist before sharing a skill (PR, verified list, or stable list).

## Content

- [ ] The skill has a clear intent (1–2 sentences) and a crisp “when to use / when not to use”.
- [ ] Inputs/outputs are explicit: required parameters, optional parameters, defaults, and constraints.
- [ ] The happy path is step-by-step and reproducible.
- [ ] Edge cases are called out (missing files, wrong folder, permissions, network failures).
- [ ] Any destructive operations are explicitly confirmed and reversible where possible.

## Instructions quality

- [ ] Commands are copy/paste-safe for the intended shell (PowerShell vs bash) and OS.
- [ ] File references use repo-relative paths when possible.
- [ ] The skill avoids over-configurability; advanced options are documented but not required.
- [ ] There is no hidden state: required tools, env vars, and credentials are stated.

## Safety

- [ ] The skill avoids leaking secrets (logs, env dumps, config prints).
- [ ] It does not encourage unsafe commands (blind `rm -rf`, running remote scripts without review).
- [ ] External calls are bounded (rate limits, paging/limits, timeouts where appropriate).

## Verification

- [ ] There is a verification section with observable outcomes (files created, commands succeed, expected output).
- [ ] There is basic troubleshooting guidance for common failure modes.

## Maintainability

- [ ] Links are valid (no 404s) and point to the canonical docs location.
- [ ] The skill is consistent with repo conventions (folder layout, naming, style).
