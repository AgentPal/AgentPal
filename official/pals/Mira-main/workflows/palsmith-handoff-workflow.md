# PalSmith Handoff Workflow

## Trigger

A task creates, modifies, imports, exports, packages, versions, audits, or reviews Pal assets, Pal Packs, Pal identity, Pal skills, Pal knowledge, Pal workflows, Pal runbooks, Pal evals, contacts suggestions, or registry suggestions.

For v0.6 this also includes Team Pack creation, Team Pack repair, team roster
planning, team workflow / eval / memory placeholders, and Pal naming or
same-name import conflict handling.

## Inputs

- User request.
- Current Pal asset target.
- Current Team Pack target, if any.
- Allowed files.
- Source material.
- Contacts / registry status.
- Risk and preservation constraints.

## Steps

1. For team-like natural-language requests, require Mira or the current owner to run Team Pack first discovery before PalSmith handoff. If a fitting Team Pack exists, reuse it and do not ask PalSmith to redesign it.
2. Judge whether Pal asset governance is required.
3. If PalSmith fits, consult or hand off with a Context Packet that includes Team Pack discovery results.
4. For team requests without a fitting reusable Team Pack, ask PalSmith for the Team Pack creation or repair plan, including `TEAM.md`, `team.json`, `roster.json`, workflow / eval / memory placeholders, routing-card placeholder, and member Pal boundary checks.
5. For new Pal requests, require human-name + role-title naming and conflict handling before any contact or registry proposal.
6. Ask PalSmith for gap report, preservation concerns, upgrade task package, and review criteria.
7. Let the runtime execute only after the PalSmith task package and user confirmation when writes are durable.
8. Run a PalSmith-style review after edits.
9. Report remaining gaps honestly.
## Decision points

- Is this Pal asset lifecycle work?
- Is this Team Pack lifecycle work?
- Does the current owner need PalSmith consult or full handoff?
- Are source materials complete enough?
- Are contacts / registry edits allowed?
- Would the requested new Pal name be only a role title?
- Does an imported or newly created Pal conflict with an existing display name?

## Outputs

PalSmith gap report, Team Pack or Pal Pack task package, naming / conflict
result when relevant, runtime execution boundary, PalSmith-style review, and
remaining issue list.

## Quality checks

- PalSmith is used as governance, not bypassed.
- Source material is preserved.
- No empty skill, knowledge, workflow, runbook, or eval shells.
- New Pals are not role-name-only Pals.
- Team Packs are not treated as Pals.
- No code or runtime dependencies are created.

## Required user confirmation

Required before contacts / registry changes, identity changes beyond requested scope, private material ingestion, or publication.

## Evidence to return

Return PalSmith files read, target files edited, validation checks, and unresolved gaps.
