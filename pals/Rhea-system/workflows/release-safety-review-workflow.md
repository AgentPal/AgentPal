# release-safety-review-workflow

## Trigger

A user or Pal asks whether AgentPal, a Pal Pack, docs, or release candidate is safe to publish, export, or claim ready.

## Inputs

Release scope, changed paths, no-code boundary result, JSON parse result, diff check, status, private/public boundary, and rollback plan.

## Steps

1. Define release scope and excluded scope.
2. Run no-code boundary review through Runtime evidence.
3. Check required JSON parse and index consistency.
4. Check private memory/state/report exposure.
5. Check dirty worktree and untracked files.
6. Check rollback readiness.
7. Report pass, conditional pass, blocked, or not-run.

## Decision points

- Are all required gates covered?
- Does evidence prove the release claim?
- Is publishing requested or forbidden?

## Outputs

Release safety review with evidence, risks, not-run items, and next action.

## Quality checks

No publish-ready claim without evidence for every release requirement.

## Required user confirmation

Required before tag, push, publish, export, or release-scope change.

## Evidence to return

Gate results, command outputs, changed path summary, private/public checks, rollback status, and status summary.

