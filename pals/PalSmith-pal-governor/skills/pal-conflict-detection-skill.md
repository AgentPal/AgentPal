# Pal Conflict Detection Skill

## Purpose

Find overlapping, unclear, or unsafe responsibility boundaries between Pals.

## When To Use

Use when teams feel confusing, two Pals answer the same work, aliases collide, or global contacts become crowded.

## Inputs

- target Pal list or team
- registry/contacts scope
- team governance files
- owner/verifier expectations

## Required Context

Read `pal-team-design-knowledge.md`, target Pal responsibilities, team governance, contacts/registry if approved, and conflict detection protocol/template.

## Process

1. List each Pal's role, responsibilities, non-responsibilities, direct call, aliases, and collaboration modes.
2. Compare owned tasks and output types.
3. Identify overlap, gaps, alias conflicts, handoff loops, verifier absence, and contact overexposure.
4. Classify severity as P0/P1/P2.
5. Recommend keep, clarify, merge, split, rename alias, move to team-local, or ask user.
6. Produce a conflict report without modifying contacts/registry.

## Output

- conflict table
- involved Pals
- severity
- recommended action
- user decisions needed
- follow-up Runtime Task Package if changes are approved

## Quality Bar

The report should make responsibilities easier to understand and should not silently erase useful overlap that the user intentionally wants.

## User Confirmation Points

- applying role changes
- changing aliases/direct calls
- changing contacts/registry

## No-Code Boundary

PalSmith reports conflicts. Runtime edits only after confirmed diff packages.

## Common Mistakes

- assuming all overlap is bad
- ignoring missing verifier roles
- changing registry automatically
- treating ordinary Skills as Pals

## Example

If Listing Pal and Content Pal both own product titles, PalSmith should recommend one owner and one consultant role, or ask the user whether titles should be split by platform.
