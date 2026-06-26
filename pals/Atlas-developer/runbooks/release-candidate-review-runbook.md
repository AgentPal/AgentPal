# Release Candidate Review Runbook

## Trigger

A user asks whether changes are ready for release candidate, merge, package, tag, or publication.

## Inputs

- Release candidate scope.
- Changed files and artifacts.
- Test/build/check evidence.
- Changelog/docs/version state.
- Known risks and rollback path.

## Steps

1. Define release scope and target state.
2. Gather evidence already available.
3. Identify missing checks.
4. Ask Quinn for quality gate if needed.
5. Ask Rhea for environment/deployment risk if needed.
6. Report lowest proven readiness state.
7. Prepare next task package for missing evidence.

## Decision points

- Is this ready for local RC, merge, publish, or only further testing?
- Are required artifacts present?
- Is Git state clean enough for the claim?
- Is user confirmation needed for release action?

## Outputs

Release candidate review, blocker list, not-run list, and next action.

## Quality checks

- No unsupported publish-ready claim.
- Evidence is mapped to scope.
- Rollback and risks visible.
- Quinn/Rhea collaboration considered.

## Required user confirmation

Required before staging, committing, tagging, pushing, publishing, deploying, or version changes.

## Evidence to return

Return check results, artifact paths, docs links, Git status, not-run checks, and readiness recommendation.
