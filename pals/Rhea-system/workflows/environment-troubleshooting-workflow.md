# environment-troubleshooting-workflow

## Trigger

A command, dependency, Runtime, package manager, PATH, version, permission, or local tool fails.

## Inputs

Error text, task goal, OS/runtime, working directory, command attempted, recent changes, and allowed diagnostics.

## Steps

1. Summarize symptom and goal.
2. Identify likely failure classes.
3. Start with read-only checks.
4. Request Runtime evidence for command availability, version, path, config, or logs.
5. Choose next branch based on evidence.
6. Stop for approval before repair.
7. Review repair evidence after action.

## Decision points

- Is the failure local environment, project config, permission, network, version, or Runtime capability?
- Is repair safe without approval?
- Does evidence prove the issue is resolved?

## Outputs

Troubleshooting plan, read-only task package, repair gate, and evidence review.

## Quality checks

No random command sequence; diagnosis and repair are separated.

## Required user confirmation

Required before installs, upgrades, PATH/environment changes, service changes, or external writes.

## Evidence to return

Commands/actions run by Runtime, working directory, exit status, key output, changed files/state, and not-run items.

