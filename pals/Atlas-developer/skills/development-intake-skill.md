# Development Intake Skill

## Purpose

Help Atlas decide whether an incoming request is ready for development planning, needs product clarification, needs environment review, needs PalSmith governance, or should stop for user approval.

## When to use

Use when a user, Mira, or another Pal asks for a feature, bug fix, refactor, repository change, technical task, or implementation-shaped deliverable.

## Inputs

- User goal and expected outcome.
- Repository or workspace path.
- Known files, modules, or product surface.
- Constraints, forbidden actions, and risk notes.
- Acceptance criteria or evidence expectations.

## Required context

Read Atlas entry files, the current project boundary, contacts / registry when collaboration may matter, and the smallest relevant development asset. Do not read broad project trees before the scope is known.

## Process

1. Classify the request as feature, bug fix, refactor, review, release check, environment issue, Pal asset change, or non-development work.
2. Check whether goal, scope, files, constraints, and acceptance criteria are sufficient.
3. Identify owner gaps: product scope to Nova, research to Vega, environment risk to Rhea, quality gate to Quinn, Pal asset governance to PalSmith, leadership routing to Mira.
4. Identify approval gates: deletion, dependency install, credentials, publishing, deployment, system changes, broad rewrite, or private data.
5. Decide next action: proceed to implementation planning, ask focused clarification, consult another Pal, hand off, or stop for approval.

## Output

A short development intake judgement with readiness state, missing inputs, owner/collaboration needs, risk gates, and next step.

## Quality bar

Atlas must not treat every technical-looking request as ready development work. A good intake protects scope, evidence, and owner boundaries before the runtime edits files.

## User confirmation points

Ask before destructive edits, broad refactors, dependency installs, publishing, real data use, credentials, system changes, registry/contact edits, or Pal asset lifecycle changes.

## No-code boundary

This skill is a Markdown method. It does not run commands, inspect the filesystem broadly, create tools, or modify code by itself.

## Common mistakes

- Accepting a vague request as implementation-ready.
- Treating environment failures as ordinary code tasks.
- Letting a runtime decide the Pal owner.
- Asking many broad questions instead of the one missing acceptance fact.

## Example

User asks "fix the failing build." Atlas requests the failing command/output and allowed scope, checks whether Rhea is needed for environment risk, then prepares a small debugging task package.
