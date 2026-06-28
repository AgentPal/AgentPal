# Memory

## Purpose

This directory stores public-safe durable memory summaries and memory policy
notes for Morgan.

Memory stores extracted long-term lessons, document workflow preferences,
preservation decisions, routing lessons, and references that help future
continuity. It is not a place for full task reports.

## What Belongs Here

- Reviewed long-term lessons from Morgan document and file workflow work.
- Public-safe project, runtime, and tool-use memory summaries.
- Pointers to central project memory records.
- Skill-use lessons after they are extracted and reviewed.
- Notes that preserve `unknown`, `missing`, or `not-run` evidence.

## What Does Not Belong Here

- Full completion reports, document audit reports, or validation records;
  reports belong in `reports/`.
- Raw evidence, file dumps, or current runtime state.
- Credentials, tokens, secrets, cookies, passwords, API keys, or customer data.
- Unapproved private user or project memory.
- External project `.agentpal/memory/` as a default target.
- Keyword routing maps or deterministic dispatch rules.

Project-private memory belongs in central project records, not external project
directories.

## Current Assets

| Asset | Memory purpose | Status | Notes |
| --- | --- | --- | --- |
| `project/` | Project-related durable memory area | `present` | Store only approved summaries or central project-record pointers. |
| `runtime/` | Runtime evidence and file-workflow memory area | `present` | Preserve `not-run`, `missing`, and runtime-availability boundaries. |
| `skill-memory/` | Skill-related memory candidates or durable lessons | `present` | Keep Agent Skill references as references unless rewritten as Pal-owned methods. |
| `user/` | User-facing preference or continuity memory area | `present` | Use only for approved, public-safe summaries. |

## Candidate Assets / Needs Review

| Candidate | Source report / evidence | Review status |
| --- | --- | --- |
| Document preservation lessons | Future completion reports | `needs-review` |
| File workflow boundary lessons | Future verified task evidence | `needs-review` |

## Related Standards

- `standards/pal-asset/pal-asset-standard.md`
- `standards/pal-asset/pal-asset-directory-standard.md`
- `templates/pal-asset/safe-index-backfill-guide.md`

## Public Safety Boundary

Do not store private user memory, private project memory, raw files, secrets,
credentials, tokens, or private evidence in this public Pal Pack directory.

## External Project Boundary

Morgan memory assets stay in the AgentPal central workspace or approved central
project records by default. External projects remain thin-bound through
`.agentpal/project.json` and must not receive copied `.agentpal/memory/` assets
by default.

