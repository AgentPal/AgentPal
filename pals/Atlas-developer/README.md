# suitable implementation collaborator

Atlas is an embedded specialist Pal module inside the AgentPal Workspace. It is not a standalone repository in this package.

Atlas helps with development planning, requirement-to-task shaping, architecture boundaries, debugging intake, repository handoff, verification requirements, release readiness, and execution evidence review.

## Embedded Structure

- `PAL.md`, `AGENTS.md`, `SKILL.md`, `pal.json`: identity and entry files.
- `identity/`: persona, voice, and boundaries.
- `core/`: task loop, output contract, collaboration boundary, capability reference, verification, learning, and reporting protocols.
- `knowledge/`: development knowledge and reference cards, including migrated public skill cards under `knowledge/references/`.
- `skills/`, `workflows/`, `runbooks/`: Atlas-owned professional methods.
- `learning/`: knowledge gaps, repeated-task notes, and Skill / Runbook / Workflow candidates.
- `examples/`, `evals/`: usage examples and self-tests.
- `memory/`, `state/`, `reports/`: public-safe placeholders only; no private runtime data.

## Workspace Boundary

AgentPal root owns contacts, registry, runtime, models, plugins, orchestration, project binding, and future orchestration design material. Atlas owns only its professional assets and output contract.

Atlas may describe possible collaborators, but collaboration and owner selection are AI / Mira / Brain case-by-case. No hard-coded semantic routing.

## Execution Boundary

Atlas does not directly edit code, run commands, install dependencies, publish, delete, deploy, or approve high-risk operations. Real execution belongs to the current execution layer and must return evidence.


