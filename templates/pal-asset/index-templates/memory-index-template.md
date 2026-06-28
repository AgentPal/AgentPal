# Memory Index

## Purpose

This directory lists durable memory records or memory policy notes owned by `[Pal name]`.

Memory stores extracted long-term lessons, preferences, decisions, routing lessons, and references that help future continuity. Memory is not a place for full reports.

## What Belongs Here

- Extracted long-term lessons.
- Stable user or project preference summaries when approved.
- Routing or tool-use lessons with evidence references.
- Pointers to central project memory records.
- Public-safe memory policy notes.

## What Does Not Belong Here

- Full completion reports or audit reports. Reports belong in `reports/`.
- Raw evidence or logs.
- Current mutable state.
- Credentials, tokens, secrets, cookies, passwords, API keys, or private customer data.
- Unapproved private user or project memory.
- External project `.agentpal/memory/` as a default target.
- Keyword routing maps or deterministic dispatch rules.

Project-private memory remains in the central project record, not in the external project.

## Current Assets

| Asset | Memory purpose | Status | Notes |
| --- | --- | --- | --- |
| `[asset path]` | `[short purpose]` | `present` | `[public-safe note]` |

## Candidate Assets

| Candidate | Source report / evidence | Review status |
| --- | --- | --- |
| `[candidate memory]` | `[source ref]` | `needs-review` |

## Review Notes

- Extract lessons from reports instead of copying reports into memory.
- Mark private or uncertain memory as `needs-review`.
- Use `unknown` when sensitivity is unclear.
- Do not write memory into an external project by default.

## Related Standards

- `standards/pal-asset/pal-asset-standard.md`
- `standards/pal-asset/pal-asset-directory-standard.md`

## Public Safety Boundary

Public indexes must not expose private user memory, private project memory, secrets, credentials, tokens, or private evidence.

## External Project Boundary

Memory assets belong in the central Pal Pack or central project record by default. External projects remain thin-bound and should not receive `.agentpal/memory/` by default.
