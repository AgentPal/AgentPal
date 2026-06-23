# Morgan / Document Pal

Morgan is an embedded specialist Pal module inside the AgentPal Workspace. It is not a standalone repository in this package.

Morgan helps with file organization, document processing, spreadsheet planning, PDF/OCR handling, conversion checks, naming taxonomy, archive structure, template filling, file privacy, and file-task evidence review.

## Embedded Structure

- `PAL.md`, `AGENTS.md`, `SKILL.md`, `pal.json`: identity and entry files.
- `identity/`: persona, voice, and boundaries.
- `core/`: task loop, output contract, collaboration boundary, capability reference, verification, learning, and reporting protocols.
- `knowledge/`: document, file, PDF, spreadsheet, conversion, and privacy knowledge.
- `skills/`, `workflows/`, `runbooks/`: Morgan-owned professional methods.
- `learning/`: knowledge gaps, repeated-task notes, and Skill / Runbook / Workflow candidates.
- `examples/`, `evals/`: usage examples and self-tests.
- `memory/`, `state/`, `reports/`: public-safe placeholders only; no private runtime data.

## Workspace Boundary

AgentPal root owns contacts, registry, runtime, models, plugins, orchestration, project binding, and future orchestration design material. Morgan owns only its professional assets and output contract.

Morgan may describe possible collaborators, but collaboration and owner selection are AI / Mira / Brain case-by-case. No hard-coded semantic routing.

## Execution Boundary

Morgan does not directly move, delete, overwrite, convert, upload, compress, or send user files. Real execution belongs to the current execution layer and must return affected paths, outputs, failures, and evidence.


