# Pal Export Review Skill

## Purpose

Plan and review clean or private Pal exports without leaking private data.

## When To Use

Use when the user wants to share, back up, move, or publish a Pal Pack.

## Inputs

- target Pal path
- export purpose
- public or private intent
- memory inclusion preference
- target export location

## Required Context

Read export protocol, privacy policy, target Pal public files, and approved private sections only when explicitly confirmed.

## Process

1. Classify export as clean or with-memory.
2. Inventory included public files.
3. Define required exclusions.
4. For with-memory export, ask strong confirmation and create privacy review.
5. Prepare export Runtime Task Package.
6. After Runtime action, review manifest, report, included files, and excluded files.
7. Block public release if private memory or state is included.

## Output

- export plan
- manifest requirements
- privacy report requirements
- clean/with-memory recommendation
- Runtime Task Package

## Quality Bar

Clean export must exclude private memory, project memory, state, reports, logs, credentials, tokens, and runtime files.

## User Confirmation Points

- export target
- with-memory scope
- public release intent
- archive creation

## No-Code Boundary

PalSmith does not create archives or copy files. Runtime does that after confirmation.

## Common Mistakes

- treating private backup as public export
- ignoring state/reports
- skipping privacy report
- modifying source Pal during export

## Example

A Research Pal clean export includes PAL.md, SKILL.md, pal.json, public knowledge and evals, while excluding memory/user, memory/project, state, reports, logs, and cache.
