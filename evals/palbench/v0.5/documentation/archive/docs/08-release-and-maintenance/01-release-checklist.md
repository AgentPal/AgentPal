# Release Checklist

Use this checklist with the root [`RELEASE_CHECKLIST.md`](../../RELEASE_CHECKLIST.md). The root file is the concise maintainer checklist; this document explains the docs-side release gate for AgentPal v0.1.0-rc.1.

## Version And Scope

- [ ] Release-facing files use `v0.1.0-rc.1`.
- [ ] AgentPal is described as an AgentPal Workspace and Pal Pack Standard practice.
- [ ] Simple Pal Mode is described as the only active task-handling path.
- [ ] Future child workflow, subagent, remote agent, MCP-hosted agent, marketplace, desktop app, and deep runtime adapter materials are not described as active current features.

## Root Release Files

- [ ] `README.md` and `README.zh-CN.md` do not contradict release notes or known limitations.
- [ ] `AGENTS.md`, `PAL.md`, `SKILL.md`, and `prompts/codex/initialize-agentpal-workspace.md` agree on initialization and Pal loading.
- [ ] `agentpal.json` is valid JSON and reflects the actual workspace directories, official Pals, and version boundary.
- [ ] `CHANGELOG.md`, `RELEASE_NOTES.md`, and `GITHUB_RELEASE_DRAFT.md` are consistent but not duplicate copies.
- [ ] `LICENSE` and `THIRD_PARTY_NOTICES.md` are present.

## Docs

- [ ] `docs/README.md` works as the docs entry point.
- [ ] Overview docs explain AgentPal vs Agent Runtime.
- [ ] Pal Pack Standard docs explain `official/pals/<Pal>/` as the official Pal Pack boundary.
- [ ] Public/private boundary docs are linked from release and standard docs.
- [ ] Known limitations are visible from release maintenance docs.
- [ ] Internal development reports are not linked into the public docs flow.

## Pal Packs

- [ ] Each official Pal Pack has `PAL.md`, `pal.json`, `SKILL.md`, `AGENTS.md`, `README.md`, and `core/output-contract.md`.
- [ ] Each official `pal.json` is valid JSON.
- [ ] Public examples and evals use synthetic, placeholder, or clearly authorized material.
- [ ] Pal Pack `memory/`, `state/`, and `reports/` contain only public-safe placeholders or ignored local-only runtime files.

## Contacts And Registry

- [ ] `workspace/organization/contacts/pals.json` and `workspace/organization/contacts/PAL_CONTACTS.md` list the same official Pals.
- [ ] Central contacts remain the Pal discovery source of truth; legacy contacts and registry files are compatibility references only.
- [ ] Skills, tools, models, plugins, MCP resources, and raw repositories are not registered as Pals.

## Public-Safe Release Gate

- [ ] Run the [public-safe checklist](02-public-safe-checklist.md).
- [ ] Scan for secrets, credentials, local paths, private memory, real customer data, internal reports, TODO/FIXME release blockers, and future-feature claims.
- [ ] Confirm `.gitignore` excludes runtime-private memory, state, reports, raw imports, private imports, temporary files, and OS/editor files.
- [ ] Confirm `.gitignore` does not exclude required public templates or README placeholders.

## Release Evidence

- [ ] Update `release/v0.1.0-rc.1/public-safe-audit.md`.
- [ ] Update `release/v0.1.0-rc.1/docs-audit.md`.
- [ ] Update `release/v0.1.0-rc.1/pal-pack-audit.md`.
- [ ] Update `release/v0.1.0-rc.1/release-notes-draft.md`.
- [ ] Record remaining risks and a release recommendation.

## Related

- [Release process](00-release-process.md)
- [Public-safe checklist](02-public-safe-checklist.md)
- [Known limitations](../99-reference/known-limitations.md)
- [Public/private boundary](../03-pal-pack-standard/11-public-private-boundary.md)
