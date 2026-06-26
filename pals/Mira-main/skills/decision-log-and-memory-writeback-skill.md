# Decision Log And Memory Writeback Skill

## Purpose

Help Mira identify which decisions should be captured and where they may be written without leaking private or release-inappropriate material.

## When to use

Use after a multi-stage decision, governance review, release check, project binding, or recurring workflow creates reusable guidance.

## Inputs

- Decision statement.
- Evidence and source files.
- Public/private boundary.
- User instruction about memory or docs.
- Target writeback surface.

## Required context

Read writeback rules and the relevant output contract before writing. If user did not ask to update memory, produce candidates rather than editing memory.

## Process

1. Separate decision, rationale, evidence, and unresolved risks.
2. Decide whether the target is public release content, Pal asset content, project-private state, or user memory.
3. Check whether user permission exists for the writeback target.
4. Create a concise decision log or memory candidate.
5. Report what was written or not written.

## Output

A decision log entry, memory candidate, or explicit no-write report.

## Quality bar

No private project facts, secrets, or internal notes may be placed in public AgentPal release files. No memory update may happen without explicit user request.

## User confirmation points

Ask before writing memory, registry changes, public docs with private facts, or any durable state outside the current requested files.

## No-code boundary

This skill is a documentation method only. It does not create databases, daemons, or background monitors.

## Common mistakes

- Treating every insight as safe public documentation.
- Writing memory because the task was useful but the user did not request it.
- Mixing release facts with private user workflow notes.
- Omitting evidence for a durable decision.

## Example

After R18, Mira can propose a memory candidate that PalSmith governance should be used for future Mira Leader updates, but she does not write memory unless requested.
