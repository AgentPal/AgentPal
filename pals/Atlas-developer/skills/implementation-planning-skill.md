# Implementation Planning Skill

## Purpose

Turn a ready development request into a bounded implementation plan that a runtime can execute and a reviewer can verify.

## When to use

Use after development intake confirms that Atlas owns the planning stage and the task has enough goal, scope, and acceptance information.

## Inputs

- Development goal.
- Current repository or project context.
- Relevant files and modules.
- Constraints and forbidden actions.
- Acceptance criteria and verification expectations.
- Known risks and rollback needs.

## Required context

Read the smallest relevant source files, local docs, and existing patterns needed to plan. Prefer project evidence over assumptions. Use web or official docs only when library/API behavior may have changed.

## Process

1. Restate the goal in verifiable terms.
2. Identify impacted behavior and likely files.
3. Split work into ordered implementation stages.
4. For each stage, define allowed edits, forbidden edits, acceptance criteria, and required evidence.
5. Identify test and review needs.
6. Add rollback notes and stop conditions.
7. Hand the plan to Runtime Task Package writing.

## Output

An implementation plan with stages, file boundaries, verification, risks, and handoff notes.

## Quality bar

The plan must be specific enough to prevent casual scope expansion and flexible enough for the runtime to discover local implementation details.

## User confirmation points

Ask before expanding scope, changing architecture, replacing dependencies, modifying generated files, or touching production-facing settings.

## No-code boundary

Atlas plans. The current runtime performs edits and commands and returns evidence.

## Common mistakes

- Listing tasks without file boundaries.
- Turning a bug fix into an unrequested refactor.
- Skipping rollback notes for risky changes.
- Confusing a plan with proof of completion.

## Example

For a UI bug, Atlas plans a minimal component change, a CSS regression check, a screenshot requirement, and a rollback path rather than a full design rewrite.
