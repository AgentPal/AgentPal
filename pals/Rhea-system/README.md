# Rhea / System Pal

Rhea is an embedded specialist Pal module inside the AgentPal Workspace. It is not a standalone repository in this package.

Rhea helps with system maintenance planning, app installation handoff, runtime setup, dependency diagnosis, PATH/environment checks, command risk review, permission boundaries, recovery planning, and execution evidence review.

## Embedded Structure

- `PAL.md`, `AGENTS.md`, `SKILL.md`, `pal.json`: identity and entry files.
- `identity/`: persona, voice, and boundaries.
- `core/`: task loop, output contract, collaboration boundary, capability reference, verification, learning, and reporting protocols.
- `knowledge/`: system, safety, permission, and environment knowledge.
- `skills/`, `workflows/`, `runbooks/`: Rhea-owned professional methods.
- `learning/`: knowledge gaps, repeated-task notes, and Skill / Runbook / Workflow candidates.
- `examples/`, `evals/`: usage examples and self-tests.
- `memory/`, `state/`, `reports/`: public-safe placeholders only; no private runtime data.

## Workspace Boundary

AgentPal root owns contacts, registry, runtime, models, plugins, orchestration, project binding, and future orchestration design material. Rhea owns only its professional assets and output contract.

Rhea may describe possible collaborators, but collaboration and owner selection are AI / Mira / Brain case-by-case. No hard-coded semantic routing.

## Execution Boundary

Rhea does not directly run commands, install, uninstall, delete, modify PATH, change services, close processes, or alter system settings. Real execution belongs to the current execution layer and must return evidence.


