# Examples Index

## Purpose

This directory lists public-safe examples for `[Pal name]`.

Examples teach how a Pal may be used. They are not binding rules, central roster entries, or proof of current runtime execution.

## What Belongs Here

- Public-safe input/output examples.
- Sample task packages.
- Success and failure cases.
- Demo prompts.
- De-identified scenario examples.
- Links to related Skills, workflows, runbooks, evals, and standards.

## What Does Not Belong Here

- Private customer data.
- Real credentials, tokens, secrets, cookies, or API keys.
- Current user or project memory.
- Formal core protocols that belong in `core/`.
- Stable domain facts that belong in `knowledge/`.
- Keyword routing examples that imply deterministic dispatch.
- External project `.agentpal/` source-of-truth files.

## Current Assets

| Asset | Example purpose | Status | Notes |
| --- | --- | --- | --- |
| `[asset path]` | `[short purpose]` | `present` | `[public-safe note]` |

## Candidate Assets

| Candidate | Reason | Review status |
| --- | --- | --- |
| `[candidate example]` | `[why it may help users]` | `needs-review` |

## Review Notes

- Keep examples de-identified and public-safe.
- Mark examples derived from user material as `needs-review` until approved.
- Examples may inspire Skills or workflows but do not become authoritative by themselves.

## Related Standards

- `standards/pal-asset/pal-asset-standard.md`
- `standards/pal-asset/pal-asset-directory-standard.md`

## Public Safety Boundary

Examples must not expose private user data, customer data, credentials, tokens, secrets, or private project details.

## External Project Boundary

Examples belong in central Pal assets or public-safe example areas by default. Do not copy them into external project `.agentpal/` by default.
