# Authoring Overview

## Status

Current for AgentPal `v0.1.0-rc.1`.

Authoring a Pal means creating a valid Pal Pack directory. Start small; a minimal Pal Pack can be useful before it has many Skills or knowledge cards.

## Basic Flow

1. Choose a clear role and boundary.
2. Create `official/pals/<Pal-Directory>/` or the selected organization Pal asset area.
3. Add the required root files.
4. Add `core/output-contract.md` and `core/task-loop.md`.
5. Add identity support files.
6. Add placeholder indexes and README files.
7. Add knowledge, Skills, runbooks, workflows, examples, and evals only as they become useful.
8. Register the Pal in `workspace/organization/contacts/` after it is valid.

## Minimum Directory Reminder

Use [Pal Pack structure](../03-pal-pack-standard/01-pal-pack-structure.md) as the required shape. Directories can be light, but placeholder indexes and README files matter because they tell the runtime what is intentionally empty.

## Validity Rule

The Pal must be able to produce a valid Pal answer: prefix, identity, output contract, relevant asset or fallback, and no unsupported execution claim.
