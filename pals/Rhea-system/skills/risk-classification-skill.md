# risk-classification

## Purpose

Classify operational risk as low, medium, high, critical, or blocked and connect the level to approval and evidence requirements.

## When to use

Use before any system, runtime, file, release, permission, troubleshooting, or recovery task.

## Inputs

Requested action, target scope, reversibility, privilege level, data sensitivity, external effects, user approval state, and available evidence.

## Required context

Risk-classification knowledge, approval gate, least privilege, and no-code boundary.

## Process

1. Identify action type and affected scope.
2. Assess reversibility and blast radius.
3. Assess privilege and data sensitivity.
4. Assess current evidence strength.
5. Assign low, medium, high, critical, or blocked.
6. Define confirmation and evidence required for that level.

## Output

Risk classification with rationale, required confirmation, allowed next action, blocked next action, and evidence required.

## Quality bar

Risk level must be justified by concrete factors, not tone or urgency.

## User confirmation points

High and critical require explicit user confirmation. Blocked requires missing safety evidence, missing authority, unclear target, or forbidden scope to be resolved first.

## No-code boundary

This skill creates a risk label and review note. It does not run checks or enforce policy through software.

## Common mistakes

- Downgrading risk because the user is impatient.
- Treating reversible as harmless.
- Missing privacy risk.
- Calling incomplete evidence a pass.

## Example

Deleting a generated local cache with exact path and backup is medium. Deleting an unknown system directory is critical or blocked.

