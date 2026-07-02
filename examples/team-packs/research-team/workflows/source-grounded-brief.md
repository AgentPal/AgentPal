# Source-Grounded Brief Workflow

## Purpose

Produce a concise brief with source boundaries, findings, uncertainty, and next
research gaps.

## Use When

- the user asks for a research brief;
- source quality and uncertainty matter;
- the output should support a decision.

## Do Not Use When

- the task is pure code implementation;
- no source access is available and the user needs current facts;
- the user asks for final expert advice in a regulated domain.

## Default Roles

- research-coordinator
- lead-researcher
- evidence-verifier when risk is medium or high

## Steps

1. Clarify the research question.
2. Define source scope and exclusion rules.
3. Gather or request source material.
4. Create or update a Workflow Execution Contract for the research task.
5. Run Pal Asset Preflight before assigned member Steps.
6. Synthesize findings.
7. Mark uncertainty and missing evidence.
8. Review against `evals/definition-of-done.md` when verification is required.
9. Run the Closure Gate before the final report.

## Output Contract

- brief summary
- evidence inventory or source notes
- findings
- uncertainty and gaps
- recommended next step

## Workflow Execution Contract Shape

| Step ID | Owner Role | Owner Pal | Output Contract | Verifier | Closure Status |
| --- | --- | --- | --- | --- | --- |
| R1 | research-coordinator | Mira | research question and source scope | none | must close |
| R2 | lead-researcher | Vega | source inventory and evidence notes | Quinn if medium/high risk | must close |
| R3 | lead-researcher | Vega | findings, confidence, and gaps | Quinn | must close |
| R4 | evidence-verifier | Quinn | claim and source-quality review | none | must close |
| R5 | research-coordinator | Mira | final brief and writeback decision | none | must close |

## Workflow Execution Contract

Use `templates/orchestration/workflow-execution-contract.md` and close through
`orchestration/workflow-closure-gate-protocol.md`.

Required Step fields for this workflow include `team_id`, `owner_pal`,
`context_access_list`, `verification_required`, and member Pal Asset Preflight
status.
