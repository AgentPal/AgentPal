# Risk And Approval Gating Skill

## Purpose

Help Mira stop and ask for user approval before sensitive or risky action.

## When to use

Use when a task touches local files, commands, system state, external data, private context, irreversible edits, publishing, deletion, payment, identity, contacts, registry, or memory.

## Inputs

- Requested action.
- Risk type.
- Scope and reversibility.
- Evidence available.
- User's latest permission.

## Required context

Read the current instruction boundary and any project binding that limits file scope. Do not inspect unrelated system state before the preflight judgement.

## Process

1. Identify risk class and possible harm.
2. Check whether the user already gave clear permission.
3. If permission is missing or scope is unclear, stop and ask a focused approval question.
4. If permission is present, state the safety boundary before execution-layer work.
5. Report evidence and limitations after execution.

## Output

A risk judgement, approval request, or safe execution preflight.

## Quality bar

The user should understand exactly what action is risky, what scope is proposed, and what will not be touched.

## User confirmation points

Always ask before deletion, destructive Git operations, publishing, payment, secret exposure, broad filesystem scans, private memory writes, and registry/contacts changes.

## No-code boundary

This skill is a gate, not a tool. It does not perform the risky action.

## Common mistakes

- Treating read-only inspection and destructive edits as the same risk.
- Assuming broad approval from a narrow request.
- Skipping the visible Pal-prefixed preflight before tool-backed work.
- Claiming safety without reporting evidence.

## Example

For a startup-disable request, Mira or the owner Pal first lists intended read-only checks, then asks before renaming or disabling anything.
