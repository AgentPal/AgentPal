# Pal Quality Inspection Task Package

task_name: Pal Quality Inspection Task Package
owner_pal: PalSmith
executing_runtime: current Agent Runtime

## User Goal

Inspect a Pal Pack for job fitness: whether it can actually perform the role, not only whether files exist.

## Allowed Reads

- target Pal public root files
- target Pal skills, knowledge, workflows, runbooks, examples, templates, and evals
- `agentpal.json`, `registry/pal.index.json`, and `contacts/pals.json` only when registration consistency is in scope
- memory/state/report directory names, not private content, unless explicitly approved
- approved user materials or research reports if user confirmed them

## Forbidden Reads

- private memory content without explicit approval
- private project state
- credentials, tokens, logs, or unrelated local files
- unrelated Pals outside approved scope

## Verification Requirements

- parse target `pal.json`
- check required root files
- build required job expertise model
- check Role Fit, Job Expertise Depth, Skill Coverage, Knowledge Coverage, Workflow Coverage, Output Contracts, Eval Coverage, Research Gap, User Material Gap, and Collaboration Fit
- report `missing`, `not-run`, and risk per dimension
- distinguish live web research from local inference

## Expected Output

`Pal Job Fitness Report` with dimension scores, missing knowledge/skills/workflows/evals, suggested web research, suggested user uploads, must-fix items, nice-to-have items, and next Runtime Task Package.

## PalSmith Acceptance

Accept only when the report explains whether the Pal can do the intended job and identifies real improvement paths. A file-complete but shallow Pal must not receive a strong job fitness judgement.
