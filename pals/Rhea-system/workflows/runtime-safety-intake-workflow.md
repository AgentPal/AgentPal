# runtime-safety-intake-workflow

## Trigger

A request involves runtime capability, commands, files, environment, permissions, release safety, system state, or external tools.

## Inputs

User goal, target system/project, requested action, allowed actions, forbidden actions, sensitive context, and expected evidence.

## Steps

1. Restate the task and target scope.
2. Classify action type and risk.
3. Assess Runtime capability and permission boundary.
4. Prefer read-only checks first.
5. Define approval gates for risky actions.
6. Define evidence required for completion.

## Decision points

- Is the request read-only or modifying?
- Is Runtime capability known?
- Is user confirmation required?
- Is another Pal needed for implementation, research, quality, governance, product, document, or writing work?

## Outputs

Safety intake note, risk level, allowed next step, blocked items, and evidence requirements.

## Quality checks

No execution claim without evidence, no hidden permission escalation, and no broad unclear target.

## Required user confirmation

Required for high or critical risk, destructive actions, privileged access, private data, release publication, or scope expansion.

## Evidence to return

Risk classification, capability evidence, approval state, not-run items, and next action.

