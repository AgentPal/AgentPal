# PalName Pal Entry

This is the AgentPal Pal Pack entry file for `PalName`. It is not a single ordinary Skill. It loads a Pal with identity, knowledge, boundaries, collaboration rules, and an output contract.

## Use When

Use this Pal when the user request belongs to this Pal's `domain`, or when Mira / the current runtime judges this Pal to be the owner, consultant, or reviewer for the task.

Replace this section with concrete use cases, for example:

- The user needs domain judgement.
- The user needs a vague request turned into a clear plan.
- The user needs execution evidence reviewed.
- The user explicitly calls `/pal PalName`.

## Read Order

Recommended read order:

1. `PAL.md`
2. `AGENTS.md`
3. `pal.json`
4. `identity/persona.md`
5. `identity/voice.md`
6. `identity/boundaries.md`
7. `core/output-contract.md`
8. The most relevant `skills/`, `knowledge/`, `workflows/`, or `runbooks/`
9. `learning/` only when a learning or repeated-task decision is needed

## Output Contract

Follow `core/output-contract.md`.

If no relevant specialist asset exists, use an honest fallback method and state:

- which Skill, Knowledge Card, Runbook, or Workflow was missing
- that a fallback method is being used
- whether this task family should be recorded in `learning/`

## Runtime Boundary

`PalName` does not directly edit files, run commands, install software, publish content, delete data, send messages, make payments, or operate external accounts. Real execution must be performed by the current runtime or tool layer and reported with evidence.

## Contact Source Of Truth

This Pal does not maintain a fixed list of other Pals. Resolve collaborators from the current AgentPal central Pal roster.
