# Release Check Request Runbook

## Trigger

The user asks whether AgentPal or a Pal asset is release-ready, publishable, packaged, or safe to ship.

## Inputs

- Target release surface.
- Required checks.
- Current worktree state when relevant.
- Source files and docs.
- Owner Pal for quality judgement.

## Steps

1. Identify release target and quality owner.
2. Separate content consistency, technical validation, Git state, package state, and publish state.
3. Run or request evidence-producing checks only within approved scope.
4. Report pass, fail, not-run, and blockers separately.
5. Do not claim publish readiness when remote, tag, artifact, or release evidence is missing.

## Decision points

- Is the target AgentPal workspace content, a Pal Pack, or external project artifact?
- Which checks are required by the user?
- Are any checks unavailable?
- Is publishing requested or only readiness review?

## Outputs

Release readiness report, blocker list, validation evidence, and next repair package.

## Quality checks

- Evidence supports every pass claim.
- Dirty worktree or missing release evidence is not hidden.
- Private material is not written to public docs.
- Specialist quality owner is preserved.

## Required user confirmation

Required before tagging, committing, pushing, publishing, or changing release artifacts beyond requested edits.

## Evidence to return

Return commands run, files inspected, status output summary, source links, and not-run checks.
