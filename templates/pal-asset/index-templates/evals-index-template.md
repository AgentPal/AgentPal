# Evals Index

## Purpose

This directory lists quality gates, assessment methods, checklists, PalBench cases, smoke checks, and regression cases owned by `[Pal name]`.

Evals help determine whether the Pal's behavior, assets, and boundaries satisfy an intended standard.

## What Belongs Here

- Definition of Done files.
- PalBench cases.
- Boundary evals.
- Regression cases.
- Acceptance checklists.
- Quality rubrics and review procedures.
- Links to related Skills, workflows, runbooks, examples, reports, and standards.

## What Does Not Belong Here

- Private task evidence.
- Full reports that belong in `reports/`.
- Current runtime state.
- Unchecked claims that execution happened.
- Credentials, tokens, secrets, private customer data, or private memory.
- Keyword routing maps or deterministic route tests.

## Current Assets

| Asset | Eval purpose | Status | Notes |
| --- | --- | --- | --- |
| `[asset path]` | `[short purpose]` | `present` | `[public-safe note]` |

## Candidate Assets

| Candidate | Acceptance target | Review status |
| --- | --- | --- |
| `[candidate eval]` | `[what it should check]` | `needs-review` |

## Review Notes

- Keep `pass`, `fail`, `not-run`, `blocked`, `missing`, and `unknown` distinct.
- Do not treat an index or manifest as proof of job fitness by itself.
- Add risky edge cases when a Pal Skill or workflow could affect user trust.

## Related Standards

- `standards/pal-asset/pal-asset-standard.md`
- `standards/pal-asset/pal-asset-directory-standard.md`

## Public Safety Boundary

Do not include private evidence, credentials, tokens, secrets, customer data, or private project state.

## External Project Boundary

Pal evals belong in central Pal assets by default. Do not write eval suites into external project `.agentpal/` by default.
