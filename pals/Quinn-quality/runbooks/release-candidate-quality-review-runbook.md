# Release Candidate Quality Review Runbook

## Trigger

A package, Pal, docs set, or workspace claims release-candidate readiness.

## Inputs

Release scope, changed files, version notes, validation evidence, source inventory, privacy review, rollback or recovery notes, and known issues.

## Steps

1. Confirm release scope and audience.
2. Check DoD and acceptance evidence.
3. Check no-code or runtime boundary when applicable.
4. Check JSON/docs/source/privacy/release evidence.
5. Check not-run items and blockers.
6. Produce release quality gate decision.

## Decision points

- Is readiness local or public?
- Are blockers unresolved?
- Is user confirmation needed for publish action?

## Outputs

Release candidate quality review report.

## Quality checks

Do not claim published, pushed, or released without external evidence.

## Required user confirmation

Required for stage, commit, tag, push, publish, external send, or release risk waiver.

## Evidence to return

Validation outputs, release artifacts, source inventory, not-run items, blockers, and release decision.
