# Project Memory Standard

Project memory is stored in AgentPal central project records, not in external project `.agentpal/` directories.

## Location

Default location:

`workspace/projects/<project-id>/memory/`

## Allowed Memory Types

- Project goal and status memory.
- Task ledger summaries.
- Decisions and rationale.
- Routing memory as judgement evidence.
- Runtime memory about availability and blockers.
- Governance memory about rule changes and workflow improvements.

## Writeback Boundary

AgentPal may read user project docs, design notes, requirements, source files, assets, and data when the user asks for project work. Summaries and structured project memory derived from those materials are written back to the central project record, not to the external project, unless the user explicitly asks for a business document inside that project.

Project memory must not contain secrets, tokens, private credentials, or unnecessary personal data.

