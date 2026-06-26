# Evidence Review Workflow

## Trigger

A Runtime, Pal, or agent reports that work is complete, tested, safe, ready, or acceptable.

## Inputs

Original objective, claims, changed files, command outputs, test results, artifacts, skipped checks, failures, and risk notes.

## Steps

1. Derive requirements from the original objective.
2. Map every claim to evidence.
3. Check whether evidence covers changed files and acceptance criteria.
4. Mark pass, fail, partial, not-run, blocked, or unknown for each requirement.
5. Identify contradictions and false completion signals.
6. Produce quality decision and follow-up tasks.

## Decision points

- Does evidence prove the claim?
- Are not-run items acceptable or blocking?
- Is another Pal needed for safety, research, governance, or implementation?

## Outputs

Evidence matrix, quality decision, gaps, risk, and follow-up owner.

## Quality checks

Completion report is not evidence unless it includes verifiable proof.

## Required user confirmation

Required before reading sensitive logs or accepting high-risk not-run items.

## Evidence to return

Evidence sources, review result per claim, missing proof, not-run register, and decision.
