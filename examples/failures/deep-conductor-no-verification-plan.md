# Failure: Deep Conductor Missing Verification Plan

## Wrong Behavior

The conductor creates a project task map and next-round Runtime package, but no acceptance criteria, evidence requirement, verifier candidate, result record, or not-run reporting rule.

## Why Wrong

Deep Conductor must plan verification before execution. Completion reports are not evidence by themselves, and project-level task maps must define how results will be checked.

## Correct Behavior

The plan includes verification requirements, result record template, pass / fail / blocked criteria, missing-evidence handling, and a verifier candidate when risk or false-completion risk warrants it.

## Corresponding Eval

`evals/orchestration/deep-conductor-no-auto-execution-self-test.md`
