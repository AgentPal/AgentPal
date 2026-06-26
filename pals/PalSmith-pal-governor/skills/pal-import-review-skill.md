# Pal Import Review Skill

## Purpose

Review external or local Pal resources safely before any install decision.

## When To Use

Use for GitHub imports, local directory imports, archives, copied Pal Packs, or unknown resources.

## Inputs

- source URL or local path
- user confirmation for fetch/copy
- staging target
- install intent
- memory handling preference

## Required Context

Read import protocol, staging policy, import templates, registry/contacts only when install or registration is requested, and source files after Runtime stages them.

## Process

1. Classify source and trust boundary.
2. Ask confirmation before network fetch or local copy.
3. Stage source; never install directly.
4. Inspect core files, package shape, scripts, credentials, memory/state/reports, license, and id conflicts.
5. Classify as Pal Pack, Skill, Knowledge Pack, mixed resource, or unknown.
6. Recommend install, quarantine, convert, or reject.
7. Keep registry/contacts writes separate.

## Output

- import review report
- source inventory
- risk list
- quarantine list
- install recommendation
- next Runtime Task Package

## Quality Bar

The review must preserve source trust boundaries and must not execute imported content.

## User Confirmation Points

- network fetch
- local copy
- memory read
- install
- registry/contacts writes

## No-Code Boundary

PalSmith does not download or install. Runtime performs approved actions and returns evidence.

## Common Mistakes

- trusting GitHub source automatically
- executing scripts
- writing contacts during staging
- importing private memory into public package

## Example

For a GitHub Pal Pack, PalSmith first prepares URL Plan, then Runtime Fetch if confirmed, then staging risk review, then an install recommendation.
