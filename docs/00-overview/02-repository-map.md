# Repository Map

This map explains the public AgentPal Workspace layout. It is a navigation aid, not permission to load the whole workspace into context.

## Root Files

| Path | Purpose |
| --- | --- |
| `agentpal.json` | Machine-readable workspace metadata, version, runtime policy, bundled Pal list, and context strategy. |
| `AGENTS.md` | Runtime-facing workspace instructions for Codex, Claude Code, and other AGENTS-aware runtimes. |
| `PAL.md` | AgentPal Workspace identity. It is not Mira's personal identity file. |
| `SKILL.md` | Workspace-level Skill entry. It is not a single-purpose Skill. |
| `prompts/codex/initialize-agentpal-workspace.md` | Copyable initialization prompt for supported runtimes. |
| `RESOURCE_INDEX.md` | Root resource navigation and context-loading guide. |
| `RELEASE_CHECKLIST.md` | Maintainer checklist for public release validation. |
| `RELEASE_NOTES.md` | User-facing release notes. |
| `THIRD_PARTY_NOTICES.md` | Current third-party notice state and future maintenance policy. |

## Main Directories

| Directory | Purpose |
| --- | --- |
| `capabilities/` | Capability profile notes and boundaries. |
| `contacts/` | Legacy compatibility contact files. Current source of truth is `workspace/organization/contacts/`. |
| `docs/` | Public documentation and reference material. |
| `evals/` | Self-tests and release checks. |
| `examples/` | Public-safe examples and failure examples. |
| `imports/` | Import staging placeholders; not ordinary task context. |
| `memory/` | Public-safe memory placeholders; private memory must not be committed. |
| `models/` | Model-routing notes and boundaries. |
| `orchestration/` | Current protocols and clearly marked future-design material. |
| `official/pals/` | Official bundled Pal Pack pool. Each `official/pals/<Pal>/` directory is one Pal Pack. |
| `plugins/` | Plugin-discovery notes and boundaries. |
| `projects/` | External project workgroup binding templates. |
| `prompts/` | Copyable maintenance and setup prompts. |
| `registry/` | Legacy Pal and resource indexes retained for compatibility and selected historical navigation. |
| `reports/` | Public-safe report placeholders; real reports should remain private or ignored. |
| `response-fingerprints/` | Response fingerprint references for Pal-mode validation. |
| `runtime/` | Runtime-awareness notes and boundaries. |
| `state/` | Public-safe state placeholders; private state must not be committed. |
| `templates/` | Reusable templates for bindings, Context Packets, task packages, and reports. |

## Pal Discovery Boundary

`workspace/organization/contacts/` is the source of truth for Pal discovery. Legacy `contacts/`, `registry/`, and old root `pals/` references are compatibility references only.

Skills, tools, plugins, models, MCP servers, raw repositories, runtime adapters, and knowledge packs do not become Pals because they are indexed. Only valid Pal Packs should enter contacts.

## Related

- [Resource index](../../RESOURCE_INDEX.md)
- [Pal Pack structure](../03-pal-pack-standard/01-pal-pack-structure.md)
- [Contacts and registry](../03-pal-pack-standard/10-contacts-and-registry.md)
- [Public/private boundary](../03-pal-pack-standard/11-public-private-boundary.md)
