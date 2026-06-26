# PalSmith Handoff Workflow

## Trigger

A task creates, modifies, imports, exports, packages, versions, audits, or reviews Pal assets, Pal Packs, Pal identity, Pal skills, Pal knowledge, Pal workflows, Pal runbooks, Pal evals, contacts suggestions, or registry suggestions.

## Inputs

- User request.
- Current Pal asset target.
- Allowed files.
- Source material.
- Contacts / registry status.
- Risk and preservation constraints.

## Steps

1. Judge whether Pal asset governance is required.
2. If PalSmith fits, consult or hand off with a Context Packet.
3. Ask PalSmith for gap report, preservation concerns, upgrade task package, and review criteria.
4. Let the runtime execute only after the PalSmith task package.
5. Run a PalSmith-style review after edits.
6. Report remaining gaps honestly.

## Decision points

- Is this Pal asset lifecycle work?
- Does the current owner need PalSmith consult or full handoff?
- Are source materials complete enough?
- Are contacts / registry edits allowed?

## Outputs

PalSmith gap report, upgrade task package, runtime execution boundary, PalSmith-style review, and remaining issue list.

## Quality checks

- PalSmith is used as governance, not bypassed.
- Source material is preserved.
- No empty skill, knowledge, workflow, runbook, or eval shells.
- No code or runtime dependencies are created.

## Required user confirmation

Required before contacts / registry changes, identity changes beyond requested scope, private material ingestion, or publication.

## Evidence to return

Return PalSmith files read, target files edited, validation checks, and unresolved gaps.
