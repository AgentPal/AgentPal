# Workflows Index

## Purpose

This directory lists standard multi-step work systems owned by `[Pal name]`.

Workflows describe normal recurring work with inputs, stages, participants, approvals, blockers, outputs, verification, and writeback.

## What Belongs Here

- Multi-step processes used repeatedly by the Pal.
- Workflow candidates with stages and acceptance criteria.
- Collaboration or handoff sequences that are stable enough to document.
- Links to related Skills, runbooks, knowledge, examples, and evals.

## What Does Not Belong Here

- Single command recipes.
- Exception-only operation manuals that belong in `runbooks/`.
- Isolated facts that belong in `knowledge/`.
- Current task state, completion reports, private evidence, credentials, or secrets.
- Keyword routing, deterministic Pal dispatch, `keyword_map`, `domain_map`, or `role_map`.

## Current Assets

| Asset | Workflow purpose | Status | Notes |
| --- | --- | --- | --- |
| `[asset path]` | `[short purpose]` | `present` | `[public-safe note]` |

## Candidate Assets

| Candidate | Reason | Review status |
| --- | --- | --- |
| `[candidate workflow]` | `[why it may become a workflow]` | `needs-review` |

## Review Notes

- Use `unknown` when the workflow stages or acceptance criteria are not clear.
- Promote from `learning/` only after the workflow has repeated value and a stable boundary.
- Keep failure-specific steps in `runbooks/` unless they are part of the normal workflow.

## Related Standards

- `standards/pal-asset/pal-asset-standard.md`
- `standards/pal-asset/pal-asset-directory-standard.md`

## Public Safety Boundary

Do not include private customer workflows, credentials, tokens, secrets, or private project evidence in public workflow indexes.

## External Project Boundary

Pal workflows belong in the central Pal Pack by default. Do not copy central workflows into external project `.agentpal/` by default.
