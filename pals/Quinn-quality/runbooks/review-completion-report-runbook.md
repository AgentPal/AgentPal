# Review Completion Report Runbook

## Trigger

A Pal, Runtime, or agent says a task is complete.

## Inputs

Original objective, completion report, changed files, checks run, artifacts, failures, skipped checks, risks, and final claim.

## Steps

1. Extract explicit requirements from the original objective.
2. Create a requirement-to-evidence table.
3. Verify changed files and artifacts exist when claimed.
4. Mark each requirement pass, fail, partial, not-run, blocked, or unknown.
5. Check for false completion patterns.
6. Produce final quality decision.

## Decision points

- Does evidence prove every required item?
- Are missing checks acceptable or blocking?
- Should work return to Atlas, Rhea, Vega, PalSmith, Mira, or Runtime?

## Outputs

Completion report review with decision, evidence, gaps, risks, and next action.

## Quality checks

Do not rely on intent, partial progress, or polished reporting as proof.

## Required user confirmation

Required before accepting high-risk residual gaps or reading private evidence.

## Evidence to return

Requirement table, evidence paths, not-run register, false completion findings, and decision.
