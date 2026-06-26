# runtime-capability-check-runbook

## Trigger

Before a task depends on a specific Runtime capability.

## Inputs

Requested capability, current Runtime, tool availability, permission model, network state if needed, and workspace path.

## Steps

1. Identify required capability.
2. Identify current Runtime evidence.
3. Identify approval needs.
4. Mark unavailable capability as not-run or blocked.
5. Define alternative path if available.

## Decision points

- Is capability present?
- Is permission sufficient?
- Is evidence current?

## Outputs

Runtime capability check note.

## Quality checks

Do not infer capability from past sessions.

## Required user confirmation

Required before using high-risk or sensitive capability.

## Evidence to return

Runtime name, capability evidence, permission state, not-run items, and fallback.

