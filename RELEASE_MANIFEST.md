# AgentPal v0.1.0-rc.1 Release Manifest

Generated: 2026-06-24

## Release Identity

| Field | Value |
| --- | --- |
| Release name | AgentPal v0.1.0-rc.1 |
| Version | `v0.1.0-rc.1` |
| Git tag | `v0.1.0-rc.1` |
| Git commit hash observed for local tag | Verify with `git rev-list -n 1 v0.1.0-rc.1` before publishing. |
| Git remote status observed | `origin https://github.com/AgentPal/AgnetPal.git` is configured for fetch and push; no push was performed during the local gate. |
| GitHub Release status observed | No online GitHub Release was created or verified during the local gate. |
| License | MIT |
| Release type | Public release candidate |
| Runtime policy | Simple Pal Mode only |

## Scope

AgentPal v0.1.0-rc.1 is a Markdown / JSON / protocol workspace for Pal Packs. It is a Pal layer for existing agent runtimes, not an Agent layer, not a multi-agent runtime, and not an execution layer.

Included:

- root initialization files: `AGENTS.md`, `PAL.md`, `SKILL.md`, and `agentpal.json`
- Codex initialization prompt: `prompts/codex/initialize-agentpal-workspace.md`
- public release docs: `README.md`, `README.zh-CN.md`, `RELEASE_NOTES.md`, `CHANGELOG.md`, `GITHUB_RELEASE_DRAFT.md`, `RELEASE_CHECKLIST.md`, `CONTRIBUTING.md`, `THIRD_PARTY_NOTICES.md`, and this manifest
- navigation index: `RESOURCE_INDEX.md`
- shared core gates under `core/` for Codex, Claude Code, generic CLI, and project-bound sessions
- official bundled Pal Packs under `pals/`
- contacts and registry files under `contacts/` and `registry/`
- orchestration protocols, templates, examples, evals, prompts, runtime compatibility notes, capability profiles, and research docs
- deliverable-aware task judgement protocol, staged Task Package example, failure regression example, and orchestration self-test
- thin external project binding templates and Claude Code / generic CLI Agent one-prompt setup prompts
- runtime-adapter thin binding examples and self-tests
- Claude Code post-install Mira welcome output requirements
- release evidence drafts under `release/v0.1.0-rc.1/`

Not included:

- desktop app, web UI, daemon, service, scanner, validator, installer, or required runtime dependency
- active Subagent Mode, active Deep Conductor execution, remote Agent orchestration, MCP-hosted Agent execution, or marketplace runtime
- private user memory, private project state, real customer data, real secrets, local machine paths, copied internal development reports, temporary screenshots, or temporary pasted text attachments
- copied full AgentPal rule bodies, full Pal rosters, full protocols, release docs, examples, or evals inside external project bindings

## Official Pal Pack Set

| Pal | Directory | Role |
| --- | --- | --- |
| Mira | `pals/Mira-main` | Main Pal, Leader Pal, Conductor, and Pal team leader and coordinator |
| Atlas | `pals/Atlas-developer` | Development perspective |
| Vega | `pals/Vega-research` | Research and evidence perspective |
| Rhea | `pals/Rhea-system` | Local system and environment perspective |
| Quinn | `pals/Quinn-quality` | Quality, risk, evidence, and acceptance perspective |
| Morgan | `pals/Morgan-document` | Document and file workflow perspective |
| Harper | `pals/Harper-writing` | Writing and communication perspective |
| Nova | `pals/Nova-product` | Product and decision perspective |

Contacts / registry source of truth:

- `contacts/pals.json`
- `contacts/PAL_CONTACTS.md`
- `registry/pal.index.json`
- `registry/pal.index.md`

## Verification Summary

R38 local checks:

- JSON parse check passed for root JSON, contacts / registry JSON, project template JSON, Pal `pal.json`, capability profile JSON, and JSON templates.
- Official Pal directory count: 8.
- Contacts count: 8.
- Registry count: 8.
- Codex, Claude Code, and Generic CLI thin binding checks passed.
- Core gate propagation checks passed for `core/` shared gates.
- No local absolute maintainer paths, attachment traces, temporary pasted text traces, or private maintenance-directory references were found in public release files.
- No binary screenshot / archive / document artifacts were found in the release workspace.
- No required runtime code, package manifest, installer, scanner, validator, daemon, or service entrypoint was found.
- Secret-key keyword hits were reviewed as public safety-boundary language, not real credentials.
- Hard-coded semantic routing hits were reviewed as prohibitions, negative examples, or non-binding examples.
- Subagent / Deep Conductor hits were reviewed as future-design or negative-boundary references, not active v0.1.0-rc.1 behavior.

## Local Git Boundary

The final release gate should observe local Git state only until maintainers explicitly publish:

- local tag `v0.1.0-rc.1` must point at the final intended release commit
- remote `origin` is configured as `https://github.com/AgentPal/AgnetPal.git`
- no push was performed during the local gate
- no GitHub Release was created or verified

If maintainers accept additional documentation changes after a local tag is created, they should create the final intended release commit, retag `v0.1.0-rc.1` if needed, then push the commit and tag before creating the GitHub Release.
