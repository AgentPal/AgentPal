# Harper / Writing Pal

Harper is an embedded specialist Pal module inside the AgentPal Workspace. It is not a standalone repository in this package.

Harper helps with writing, rewriting, editing, tone, audience fit, email/message drafts, announcements, explanations, reports, localization, source-grounded expression, and communication-risk review.

## Embedded Structure

- `PAL.md`, `AGENTS.md`, `SKILL.md`, `pal.json`: identity and entry files.
- `identity/`: persona, voice, and boundaries.
- `core/`: task loop, output contract, collaboration boundary, capability reference, verification, learning, and reporting protocols.
- `knowledge/`: writing, style, communication, localization, and source-grounding knowledge.
- `skills/`, `workflows/`, `runbooks/`: Harper-owned professional methods.
- `learning/`: knowledge gaps, repeated-task notes, and Skill / Runbook / Workflow candidates.
- `examples/`, `evals/`: usage examples and self-tests.
- `memory/`, `state/`, `reports/`: public-safe placeholders only; no private runtime data.

## Workspace Boundary

AgentPal root owns contacts, registry, runtime, models, plugins, orchestration, project binding, and future orchestration design material. Harper owns only its professional assets and output contract.

Harper may describe possible collaborators, but collaboration and owner selection are AI / Mira / Brain case-by-case. No hard-coded semantic routing.

## Execution Boundary

Harper does not directly send email, publish, upload, operate accounts, run commands, install dependencies, or delete files. Real execution belongs to the current execution layer and must return evidence.


