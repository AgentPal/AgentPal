# Memory

## Purpose

This directory stores public-safe durable memory summaries and memory policy
notes for Rhea.

Memory stores extracted long-term lessons, runtime safety decisions, boundary
lessons, incident-review lessons, routing lessons, and continuity references. It
is not a place for full task reports.

## What belongs here

- Reviewed long-term lessons from Rhea system and runtime safety work.
- Public-safe runtime, permission, and boundary memory summaries.
- Pointers to central project memory records.
- Safety review lessons after they are extracted and reviewed.
- Notes that preserve `unknown`, `missing`, or `not-run` evidence.

## What does not belong here

- Full completion reports, safety reports, incident reports, or validation
  records.
- Raw evidence, runtime dumps, customer data, or current mutable state.
- Credentials, tokens, secrets, cookies, passwords, API keys, or private project
  data.
- Unapproved private user or project memory.
- External project `.agentpal/memory/` as a default target.
- Keyword routing maps or deterministic dispatch rules.

## Current assets

| Asset | Memory purpose | Status | Notes |
| --- | --- | --- | --- |
| `skill-memory/` | Skill-related memory candidates or durable lessons | `present` | Keep Agent Skill references as references unless rewritten as Pal-owned methods. |
| `user/` | User-facing preference or continuity memory area | `present` | Use only for approved, public-safe summaries. |

## Candidate memories / needs review

| Candidate | Source report / evidence | Review status |
| --- | --- | --- |
| Runtime boundary lessons | Future safety reports | `needs-review` |
| Permission and rollback lessons | Future verified task evidence | `needs-review` |

## Relationship to reports

Reports belong in `reports/`. Safety reports, incident reviews, and runtime
evidence become memory only after stable lessons are extracted, reviewed, and
summarized without private details.

## Project-private memory boundary

Project-private memory belongs to AgentPal central project records, not external
project directories. Do not copy Rhea memory into an external project's
`.agentpal/` tree by default.

## Related standards

- `standards/pal-asset/pal-asset-directory-standard.md`
- `templates/pal-asset/index-templates/memory-index-template.md`
- `templates/pal-asset/safe-index-backfill-guide.md`

## Public safety boundary

Do not store private user memory, private project memory, runtime dumps,
secrets, credentials, tokens, passwords, API keys, or private evidence in this
public Pal Pack directory.

## External project boundary

Rhea memory assets stay in the AgentPal central workspace or approved central
project records by default. External projects remain thin-bound through
`.agentpal/project.json` and must not receive copied `.agentpal/memory/` assets
by default.
