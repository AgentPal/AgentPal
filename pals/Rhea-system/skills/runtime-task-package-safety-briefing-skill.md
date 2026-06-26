# runtime-task-package-safety-briefing

## Purpose

Prepare the safety section of a Runtime Task Package so execution layers know the boundaries, confirmations, risks, and evidence requirements.

## When to use

Use when Atlas, Mira, PalSmith, Vega, Quinn, or the user needs a Runtime Task Package involving local files, commands, environment, release gates, system state, or external tools.

## Inputs

Task goal, allowed files/actions, forbidden files/actions, runtime capability assessment, risk classification, approvals, rollback notes, and evidence requirements.

## Required context

Rhea role boundary, approval gate, evidence review, no-code boundary, and default-Pal collaboration boundaries.

## Process

1. State the runtime goal.
2. State allowed actions.
3. State forbidden actions.
4. State confirmation gates.
5. State rollback/recovery expectations.
6. State exact evidence required.
7. State not-run reporting requirement.

## Output

Safety briefing section for a Runtime Task Package.

## Quality bar

The package must be clear enough that an execution layer cannot reasonably confuse planning with permission.

## User confirmation points

Ask before including high-risk actions or sensitive context.

## No-code boundary

This skill creates Markdown task-package text only. It does not execute the package.

## Common mistakes

- Leaving "do what is necessary" as a blank check.
- Omitting forbidden actions.
- Missing evidence requirements.
- Forgetting not-run reporting.

## Example

"Allowed: read Rhea files and edit Markdown/JSON under Rhea. Forbidden: add scripts, run installers, stage/commit, publish. Evidence: changed paths, JSON parse, diff check, status."

