# Runbooks Index

## Purpose

This directory lists concrete operation manuals and exception-handling procedures owned by `[Pal name]`.

Runbooks describe stable checks, steps, stop conditions, escalation rules, and verification for repeated operations or failure situations.

## What Belongs Here

- Repeated operational procedures.
- Failure handling steps.
- Stop conditions and escalation rules.
- Recovery or repair procedures with verification evidence.
- Links to related Skills, workflows, knowledge, reports, and evals.

## What Does Not Belong Here

- Broad normal work systems that belong in `workflows/`.
- Strategy notes or domain facts that belong in `knowledge/`.
- One-off task logs or completion reports.
- Raw tool manuals, unapproved command lists, credentials, tokens, or secrets.
- Keyword routing or deterministic task-to-Pal routing maps.

## Current Assets

| Asset | Runbook purpose | Status | Notes |
| --- | --- | --- | --- |
| `[asset path]` | `[short purpose]` | `present` | `[public-safe note]` |

## Candidate Assets

| Candidate | Reason | Review status |
| --- | --- | --- |
| `[candidate runbook]` | `[why it may become a runbook]` | `needs-review` |

## Review Notes

- Mark incomplete or untested steps as `not-run` or `needs-review`.
- Do not imply runtime execution without current evidence.
- Keep command details behind approval and verification boundaries.

## Related Standards

- `standards/pal-asset/pal-asset-standard.md`
- `standards/pal-asset/pal-asset-directory-standard.md`
- `standards/pal-asset/pal-skill-vs-agent-skill-standard.md`

## Public Safety Boundary

Do not include private system details, customer identifiers, credentials, tokens, secrets, or private evidence.

## External Project Boundary

Runbooks are Pal assets in the AgentPal central workspace by default. Do not write them into external project `.agentpal/` by default.
