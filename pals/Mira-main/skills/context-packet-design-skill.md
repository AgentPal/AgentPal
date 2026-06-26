# Context Packet Design Skill

## Purpose

Help Mira package just enough context for a Pal handoff, consultation, or Runtime Task Package.

## When to use

Use when work is handed to another Pal, when a runtime will edit or inspect files, when a task has multiple stages, or when context must be bounded.

## Inputs

- User request.
- Current owner judgement.
- Relevant file paths or project binding.
- Known constraints, risks, and verification needs.
- Explicitly read files versus index-known paths.

## Required context

Read only the assets needed for the current handoff. Keep source evidence, assumptions, and missing context separate.

## Process

1. State the task objective.
2. List required inputs and files already read.
3. List boundaries and forbidden actions.
4. List acceptance criteria and verification needs.
5. Identify unresolved questions or approval gates.
6. Pass the packet to the owner Pal or execution layer.

## Output

A bounded Context Packet with objective, owner, inputs, scope, exclusions, risks, evidence, acceptance criteria, and reporting format.

## Quality bar

The receiver should be able to act without sweeping unrelated files. The user should be able to see what context was used and what was not used.

## User confirmation points

Ask before including secrets, private memories, large unrelated files, external browsing, or any context outside the requested boundary.

## No-code boundary

This skill creates written task context only. It is not a context scanner, indexer, or automation.

## Common mistakes

- Passing all available files as context.
- Mixing assumptions with evidence.
- Omitting forbidden actions.
- Letting the runtime decide Pal ownership after the packet.

## Example

For a Mira file update, the packet names Mira files as allowed writes, excludes registry and runtime code, cites PalSmith review as governance, and requires a final gap review.
