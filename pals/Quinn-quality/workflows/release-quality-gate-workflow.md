# Release Quality Gate Workflow

## Trigger

A user or Pal asks whether something can be published, exported, tagged, released, sent, or called release-ready.

## Inputs

Release scope, artifacts, changed files, tests, docs, source inventory, privacy review, rollback plan, and user confirmation status.

## Steps

1. Confirm release intent and audience.
2. Review acceptance and DoD evidence.
3. Review tests, regression, privacy, source, license, and rollback evidence.
4. Include Rhea safety and PalSmith governance findings when relevant.
5. Classify release risk and not-run items.
6. Decide pass, conditional pass, fail, blocked, or needs-more-evidence.

## Decision points

- Is this local readiness or public release?
- Are any release blockers unresolved?
- Has the user confirmed high-risk release actions?

## Outputs

Release quality gate report with decision, blockers, not-run, residual risk, and next action.

## Quality checks

No release pass without evidence. No publish claim without publish evidence.

## Required user confirmation

Required before tag, push, publish, external send, public export, with-memory export, or high-risk waiver.

## Evidence to return

Artifacts, checks, release notes, privacy status, rollback status, user confirmations, and release decision.
