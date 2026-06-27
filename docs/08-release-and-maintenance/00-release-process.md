# Release Process

This process is for publishing AgentPal v0.1.0-rc.1 as a public MIT GitHub release.

AgentPal v0.1.0-rc.1 is a Markdown/JSON AgentPal Workspace. It is not a desktop app, web app, marketplace, multi-agent runtime, execution layer, daemon, scanner, validator, installer, or hosted service.

## Release Scope

The release package may include:

- root release files such as `README.md`, `README.zh-CN.md`, `AGENTS.md`, `PAL.md`, `SKILL.md`, `agentpal.json`, release notes, notices, and checklists
- prompt assets such as `prompts/codex/initialize-agentpal-workspace.md`
- public documentation under `docs/`
- official public Pal Packs under `official/pals/`
- central contacts under `workspace/organization/contacts/` used for Pal discovery
- public examples, evals, prompts, templates, protocols, and placeholder memory/state/report directories
- release audit notes under `release/v0.1.0-rc.1/`

The release package must not include private runtime memory, private project state, real task reports, secrets, credentials, customer data, local machine paths, internal development reports, unauthorized logs, or unauthorized third-party full text.

## Release Flow

1. Confirm the version string is `v0.1.0-rc.1` in release-facing files.
2. Confirm the root release files describe AgentPal as a Pal Workspace and keep Simple Pal Mode as the only active task-handling path.
3. Review `docs/README.md`, the overview docs, Pal Pack Standard docs, runtime guide docs, and reference docs for public-safe navigation.
4. Run the root [release checklist](../../RELEASE_CHECKLIST.md).
5. Run the [public-safe checklist](02-public-safe-checklist.md).
6. Audit `official/pals/` and `workspace/organization/contacts/` for Pal Pack structure and discovery consistency.
7. Confirm third-party notices and license files are present and accurate for the current repository contents.
8. Prepare or update the GitHub release draft and user-facing release notes.
9. Record audit evidence under `release/v0.1.0-rc.1/`.
10. Publish only after the maintainer reviews remaining risks and accepts the release recommendation.

## Evidence To Keep

For each release candidate, keep concise public-safe audit artifacts:

- `public-safe-audit.md` for sensitive content and boundary scans
- `docs-audit.md` for documentation navigation and future-feature wording
- `pal-pack-audit.md` for official Pal Pack structure and registry synchronization
- `release-notes-draft.md` for the release copy to review before publishing

These files are release evidence, not private task reports. They should contain commands or manual checks, findings, fixed issues, remaining risks, and a release recommendation.

## Release Gate

Block the release if any of these are found:

- real secrets, credentials, API keys, tokens, passwords, or private keys
- private user memory or private project state
- real customer data or proprietary user project data
- real task reports, verification reports, internal development reports, or unauthorized logs
- local absolute paths or maintainer machine paths in public release files
- claims that future design work is active in v0.1.0-rc.1
- claims that AgentPal is a complete multi-agent runtime, desktop app, marketplace, or automation platform
- missing license or materially incomplete third-party notices

## RC To Stable

For a future stable release, rerun the same process and require a fresh audit directory for that version. Do not reuse v0.1.0-rc.1 audit conclusions after content changes.

## Related

- [Release checklist](01-release-checklist.md)
- [Public-safe checklist](02-public-safe-checklist.md)
- [Known limitations](../99-reference/known-limitations.md)
- [Root release checklist](../../RELEASE_CHECKLIST.md)
- [Release notes](../../RELEASE_NOTES.md)
