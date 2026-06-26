# Pal Version Governance Skill

## Purpose

Guide Pal version changes, lifecycle status changes, snapshots, and rollback planning.

## When To Use

Use when a Pal moves from draft to testing, stable, publish-ready, deprecated, archived, or when a user asks for upgrade/rollback.

## Inputs

- target Pal or team
- current state
- proposed change
- evidence from evals, readiness, or runtime reports
- rollback expectations

## Required Context

Read lifecycle workflow, version governance protocol, readiness matrix, audit policy, and target Pal evidence.

## Process

1. Identify current state and proposed state.
2. Check evidence required for that transition.
3. Identify changed files and risk.
4. Recommend snapshot before risky changes.
5. Prepare version upgrade or rollback Runtime Task Package.
6. Require confirmation for writes or overwrite.
7. Verify post-change JSON and evidence.

## Output

- version change report
- lifecycle recommendation
- snapshot/rollback plan
- Runtime Task Package
- post-change verification requirements

## Quality Bar

Version state must follow evidence. `published` requires actual publication evidence.

## User Confirmation Points

- lifecycle state write
- snapshot creation
- rollback overwrite
- release or publish action

## No-Code Boundary

PalSmith plans. Runtime changes files only after confirmation.

## Common Mistakes

- marking stable without eval evidence
- marking published from local files only
- skipping rollback plan
- changing registry as part of unrelated version work

## Example

A Pal can move from draft to testing after root files, output contract, initial knowledge, workflows, and basic evals exist. It cannot move to publish-ready until clean export and public-safety checks pass.
