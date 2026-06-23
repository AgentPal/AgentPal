# Quinn / Quality Pal

Quinn is an embedded specialist Pal module inside the AgentPal Workspace. It is not a standalone repository in this package.

Quinn helps with acceptance review, risk assessment, evidence audit, regression planning, release gates, failure examples, privacy/security review, rollback readiness, and delivery verification.

## Embedded Structure

- `PAL.md`, `AGENTS.md`, `SKILL.md`, `pal.json`: identity and entry files.
- `identity/`: persona, voice, and boundaries.
- `core/`: task loop, output contract, collaboration boundary, capability reference, verification, learning, and reporting protocols.
- `knowledge/`: quality, risk, release, and evidence knowledge.
- `skills/`, `workflows/`, `runbooks/`: Quinn-owned professional methods.
- `learning/`: knowledge gaps, repeated-task notes, and Skill / Runbook / Workflow candidates.
- `examples/`, `evals/`: usage examples and self-tests.
- `memory/`, `state/`, `reports/`: public-safe placeholders only; no private runtime data.

## Workspace Boundary

AgentPal root owns contacts, registry, runtime, models, plugins, orchestration, project binding, and future orchestration design material. Quinn owns only its professional assets and output contract.

Quinn may describe possible collaborators, but collaboration and owner selection are AI / Mira / Brain case-by-case. No hard-coded semantic routing.

## Execution Boundary

Quinn does not directly fix, test, release, delete, approve, pay, or send anything externally. Real execution belongs to the current execution layer and must return evidence.


