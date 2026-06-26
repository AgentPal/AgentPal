# False Completion Detection Skill

## Purpose

Detect cases where a task is reported as complete but the requested end state is not proven or not actually achieved.

## When to use

Use for completion reports, agent handoffs, release reports, import/export claims, Pal upgrades, or any high-confidence claim with thin evidence.

## Inputs

Original request, completion report, changed files, artifacts, test evidence, skipped checks, acceptance criteria, and known blockers.

## Required context

Read the original objective, `false-completion-knowledge.md`, relevant DoD, and the evidence review output.

## Process

1. Derive concrete requirements from the original objective.
2. Check each requirement against current evidence.
3. Identify plan-only work, file-only work, unverified claims, missing artifacts, and incomplete checks.
4. Identify partial completion reported as pass.
5. Mark severity and user impact.
6. Recommend return-to-owner, Runtime check, or blocker report.

## Output

False completion report with requirement, claimed status, evidence status, actual status, severity, and required correction.

## Quality bar

The skill should catch subtle incompleteness without inventing failures. Uncertain evidence remains unproven.

## User confirmation points

Ask before expanding read scope beyond the requested evidence, especially private logs or broad project folders.

## No-code boundary

This is a judgement skill. It does not run validators or automated scanners.

## Common mistakes

- Only searching for obvious placeholder markers.
- Ignoring original numbered requirements.
- Treating missing evidence as pass.
- Reporting "complete enough" when the objective requires proof.

## Example

If Atlas says a Pal can publish but no clean export, eval review, or registry consistency evidence exists, Quinn flags false completion and blocks the publish-ready claim.
