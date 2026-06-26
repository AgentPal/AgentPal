# Pal Creation With Research Workflow

Status: R16 v0.4-fix no-code workflow.

Use this workflow when PalSmith creates or repairs a Pal that must be fit for a real job, not only structurally complete.

## Flow

1. Ask for Pal name, responsibilities, goals, scenarios, target users, output language, and collaboration boundary.
2. Ask what user materials exist and whether the Runtime may read them.
3. Ask whether optional web research is allowed, which source scope is acceptable, and which topics need current evidence.
4. Build a job expertise model: real tasks, decisions, domain concepts, workflows, reusable templates, evaluation cases, risk boundaries, and evidence required.
5. Prepare a material ingestion plan with source inventory, classification table, and content preservation checklist.
6. Prepare a web research to knowledge plan only when user material is insufficient or the job domain is time-sensitive.
7. Produce a Pal Creation Task Package that includes knowledge, skill, workflow, runbook, template, eval, and output contract assets.
8. After Runtime execution, review evidence through job fitness inspection and report `done`, `missing`, `not-run`, and repair needs.

## Acceptance

- The creation plan includes a job expertise model before file creation.
- User material is mapped to durable Pal assets without over-compression.
- Research facts are source-backed and separated from inference or recommendation.
- The final Pal is judged by job fitness, job expertise, skill depth, knowledge depth, workflow readiness, and eval coverage.

## Boundary

PalSmith does not fetch sources, read private files, or write Pal assets directly. The current Runtime performs approved actions and returns evidence.
