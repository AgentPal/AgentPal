# Vega / Research Pal

Vega is an embedded specialist Pal module inside the AgentPal Workspace. It is not a standalone repository in this package.

Vega helps with research intake, source discovery, source quality, freshness checks, comparison, GitHub/project evaluation, citation summaries, uncertainty handling, and knowledge-card candidates.

## Embedded Structure

- `PAL.md`, `AGENTS.md`, `SKILL.md`, `pal.json`: identity and entry files.
- `identity/`: persona, voice, and boundaries.
- `core/`: task loop, output contract, collaboration boundary, capability reference, source verification, learning, and reporting protocols.
- `knowledge/`: research methods and reference cards, including migrated public research cards under `knowledge/references/`.
- `skills/`, `workflows/`, `runbooks/`: Vega-owned professional methods.
- `learning/`: knowledge gaps, repeated-task notes, and Skill / Runbook / Workflow candidates.
- `examples/`, `evals/`: usage examples and self-tests.
- `memory/`, `state/`, `reports/`: public-safe placeholders only; no private runtime data.

## Workspace Boundary

AgentPal root owns contacts, registry, runtime, models, plugins, orchestration, project binding, and future orchestration design material. Vega owns only its professional assets and output contract.

Vega may describe possible collaborators, but collaboration and owner selection are AI / Mira / Brain case-by-case. No hard-coded semantic routing.

## Execution Boundary

Vega does not directly browse, query APIs, scrape, download, extract PDFs, run commands, edit files, or make high-risk final decisions. Real execution belongs to the current execution layer and must return evidence and source timestamps.


