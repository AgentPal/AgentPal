# Runtime Validation

Status: manual validation entry; no runtime result recorded here.

This directory holds copyable task packages and evidence templates for real
host-runtime validation. These files do not run tests, start services, install
plugins, create databases, or execute AgentPal automatically.

## Current Packages

| Package | Start here | Status |
| --- | --- | --- |
| v0.6 Team Pack real runtime validation | `v0.6-team-pack/README.md` | `needs-runtime-validation` |

## Boundary

Use these packages only to prepare and record real sessions in hosts such as
Codex, Claude Code, OpenCode, or another CLI agent that can read the AgentPal
workspace and preserve project context.

Do not mark a scenario as passed until an actual host-runtime transcript or
file-system evidence is recorded.
