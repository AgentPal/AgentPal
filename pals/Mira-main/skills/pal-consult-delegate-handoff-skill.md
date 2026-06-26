# Pal Consult Delegate Handoff Skill

## Purpose

Help Mira choose and perform consult, delegate, or handoff while preserving Pal ownership boundaries.

## When to use

Use when another Pal's expertise is useful, when the task owner changes, or when Mira needs governance input before continuing.

## Inputs

- Owner judgement.
- Contacts / registry.
- User intent and urgency.
- Task risk and expected deliverable.
- Context Packet.

## Required context

Read the owner candidate's minimum entry assets only if needed. Do not load the whole Pal pool.

## Process

1. Decide collaboration mode:
   - consult: Mira remains owner but asks for advice;
   - delegate: another Pal owns a stage and returns output;
   - handoff: another Pal becomes active owner.
2. State why the mode fits this case.
3. Provide a Context Packet.
4. Keep Mira's later role limited to coordination, progress summary, or final synthesis.
5. Do not write the specialist's professional answer as Mira.

## Output

A collaboration statement and Context Packet, followed by the receiving Pal's answer when the runtime supports same-response handoff.

## Quality bar

The receiving owner must have enough context and clear authority. Mira must not keep doing specialist work after a handoff.

## User confirmation points

Ask confirmation when the handoff shares sensitive context or changes the requested owner.

## No-code boundary

This is a communication protocol. It does not create runtime subagents or parallel workflows.

## Common mistakes

- Calling every collaboration a handoff.
- Letting Mira summarize so heavily that the specialist judgement disappears.
- Treating future Deep Conductor design as active execution.
- Making PalSmith governance optional for Pal asset lifecycle work that needs quality review.

## Example

Mira receives a Pal creation request, consults PalSmith for governance, then allows Codex to edit Markdown assets only under PalSmith's Task Package.
