# approval-gate-design

## Purpose

Design explicit confirmation gates for high-risk operations so the user understands scope, impact, reversibility, and evidence requirements.

## When to use

Use when an action may modify files, settings, dependencies, services, startup items, permissions, release state, contacts, registry, memory, or public assets.

## Inputs

Task goal, risk classification, exact action, affected paths, allowed actions, forbidden actions, rollback plan, and evidence required.

## Required context

Approval gate knowledge, permission boundary review, file safety review, and PalSmith governance boundary when Pal assets are involved.

## Process

1. State the action in plain language.
2. State the exact target paths or system components.
3. State likely impact and reversibility.
4. State safer alternatives and not-run items.
5. Ask for explicit confirmation when required.
6. Define post-action evidence.

## Output

Approval request text and gate decision: proceed, revise, read-only first, or blocked.

## Quality bar

The user must be able to say yes or no with enough information to understand risk.

## User confirmation points

Explicit confirmation is required for high, critical, destructive, privileged, external, public-release, or privacy-sensitive actions.

## No-code boundary

This skill writes confirmation language only. It does not execute the approved action.

## Common mistakes

- Asking vague permission such as "Is this okay?"
- Hiding affected paths.
- Combining several risky actions in one approval.
- Not explaining rollback.

## Example

"Please confirm: Runtime may rename `Start Summoner Runtime.cmd` to `.disabled` in the Startup folder. This is reversible and does not delete the underlying script."

