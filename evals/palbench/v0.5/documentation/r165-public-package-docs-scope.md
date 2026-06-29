# R165 Public Package Docs Scope

## Include In Public Release Package

These paths are suitable for the public v0.5 release candidate package:

| Scope | Paths |
| --- | --- |
| Public entry | `README.md`, `README.zh-CN.md`, `START_HERE.md`, `LICENSE`, `THIRD_PARTY_NOTICES.md`, `CHANGELOG.md`, `RELEASE_NOTES.md`, `RELEASE_CHECKLIST.md`, `GITHUB_RELEASE_DRAFT.md` |
| AgentPal workspace identity | `AGENTS.md`, `PAL.md`, `SKILL.md`, `agentpal.json`, `RESOURCE_INDEX.md` |
| User and contributor docs | `docs/` excluding historical evidence archive content |
| Host prompts | `prompts/`, with Codex current entry at `prompts/codex/initialize-agentpal-workspace.md` |
| Official Pal assets | `official/pals/` |
| Central contacts | `workspace/organization/contacts/` |
| Standards and templates | `standards/`, `templates/` |
| Public examples | `examples/` |
| Current release notes/checklists | `release/current/` |

## Keep As Evidence, Not User Entry

These paths may remain in the repository for traceability, but should not be presented as the first user path:

| Scope | Paths |
| --- | --- |
| PalBench and documentation evidence | `evals/palbench/v0.5/` |
| Fresh-clone validation records | `release/fresh-clone-checks/` |
| Integration decisions | `release/integration-notes/` |
| Historical docs archive | `evals/palbench/v0.5/documentation/archive/docs/` |
| Historical migration archive | `archive/migration-from-v0.3/` |

## Exclude From Any Public Package Artifact

These must stay out of a generated public package artifact:

- `.git/` and local Git internals
- host-local settings such as `.claude/settings.local.json`
- private memory, local project facts, local customer data, secrets, credentials, tokens, and API keys
- external project directories and external project `.agentpal/` bindings
- local internal completion reports outside the repository
- generated caches, temp files, and machine-specific runtime state

## Boundary Result

`pass`

The public package remains a Markdown / JSON / protocol and Pal asset workspace. It does not add a CLI installer, scanner, daemon, marketplace, hosted runtime, connector layer, or automatic multi-Agent execution claim.

