# AgentPal Release Manifest

## v0.2.0-rc.1 Release Snapshot

Generated: 2026-06-27

| Field | Value |
| --- | --- |
| Release name | AgentPal v0.2.0-rc.1 |
| Version | `v0.2.0-rc.1` |
| Git tag | `v0.2.0-rc.1` |
| Release type | Public release candidate / pre-release |
| Runtime policy | Simple Pal Mode only |

Scope:

- PalSmith end-to-end creation flows for a first professional Pal and a small AI team.
- Mira-first usage flows.
- Official Pal task examples for all 9 bundled Pals.
- Minimal Capability Inventory profiles as manual AI judgement inputs.
- PalBench Light qualitative release regression suite with 24 cases and scoring rubric.
- Runtime Adapter thin binding stability guidance and troubleshooting cards.

Not included:

- desktop app, web UI, CLI runtime, daemon, scanner, validator, installer, or service
- active Deep Conductor execution, autonomous multi-agent runtime behavior, remote-agent orchestration, or active Subagent Mode
- automatic capability probing or automatic Routing Reward Memory writeback
- statistical benchmark evidence or underlying-model comparison

Publication boundary:

- Create the release from tag `v0.2.0-rc.1`.
- Mark the GitHub Release as a pre-release.
- Do not mark this release as stable `v0.2.0`.
- Use `GITHUB_RELEASE_DRAFT.md` as the GitHub Release body.

## v0.1.0-rc.1 Release Archive

Generated: 2026-06-25

## Release Identity

| Field | Value |
| --- | --- |
| Release name | AgentPal v0.1.0-rc.1 |
| Version | `v0.1.0-rc.1` |
| Git tag | `v0.1.0-rc.1` |
| Git commit hash observed for local tag | `b2db978ad816a74cb63ab05d48b19f12da4dcc1e` |
| Git remote status observed | `origin https://github.com/AgentPal/AgentPal.git` is configured for fetch and push; no push was performed during the local gate. |
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
- PalSmith no-code Pal asset governance docs, Runtime Task Package standard links, task package templates, example task packages, Markdown evals, and release-scope review
- PalSmith source lineage, source inventory, source coverage matrix, and no-code governance review assets
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
- ignored local runtime outputs such as `.agentpal/` and `exports/`
- copied full AgentPal rule bodies, full Pal rosters, full protocols, release docs, examples, or evals inside external project bindings

## Official Pal Pack Set

| Pal | Directory | Role |
| --- | --- | --- |
| Mira | `pals/Mira-main` | Main Pal, Leader Pal, Conductor, and Pal team leader and coordinator |
| Atlas | `pals/Atlas-developer` | Development perspective |
| Vega | `pals/Vega-research` | Research and evidence perspective |
| Rhea | `pals/Rhea-system` | Local system and environment perspective |
| PalSmith | `pals/PalSmith-pal-governor` | Pal asset governance, creation, health, import/export, versioning, and Runtime Task Package perspective |
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

R38 / R09 / R10 local checks:

- JSON parse check passed for root JSON, contacts / registry JSON, project template JSON, Pal `pal.json`, capability profile JSON, and JSON templates.
- Official Pal directory count: 9.
- Contacts count: 9.
- Registry count: 9.
- PalSmith final verification report: `docs/08-release-candidate/09-palsmith-final-verification-report.md`.
- AgentPal final release verification report: `docs/08-release-candidate/10-agentpal-final-release-verification-report.md`.
- R11 default Pal P2 sync plan: `docs/08-release-candidate/13-default-pals-p2-sync-plan.md`.
- R11 default Pal P2 sync verification report: `docs/08-release-candidate/14-default-pals-p2-sync-verification-report.md`.
- R12 release review baseline: `docs/08-release-candidate/15-agentpal-release-review-baseline.md`.
- R12 commit review report: `docs/08-release-candidate/16-agentpal-commit-review-report.md`.
- R12 default Pal official consistency report: `docs/08-release-candidate/17-default-pals-official-consistency-report.md`.
- R12 no-code boundary release review: `docs/08-release-candidate/18-no-code-boundary-release-review.md`.
- R12 final release review report: `docs/08-release-candidate/19-agentpal-release-review-final-report.md`.
- R13 formal Skill asset standard: `docs/03-pal-pack-standard/15-formal-skill-assets.md`.
- R13 formal Skill assets audit: `docs/08-release-candidate/20-formal-skill-assets-audit.md`.
- R13 formal Skill assets fix report: `docs/08-release-candidate/21-formal-skill-assets-fix-report.md`.
- R13 official Pal field strategy decision: `docs/08-release-candidate/official-pal-field-strategy-decision.md`.
- R13 official Pal formal Skill result: 219 listed formal Skills map to 219 actual assets under the Flat Skill Card / Directory Skill Package standard.
- R14 dirty worktree stage review: `docs/08-release-candidate/22-dirty-worktree-stage-review.md`.
- R14 commit grouping plan: `docs/08-release-candidate/23-commit-grouping-plan.md`.
- R14 maintainer release handoff: `docs/08-release-candidate/24-maintainer-release-handoff.md`.
- R14 final maintainer stage readiness report: `docs/08-release-candidate/25-final-maintainer-stage-readiness-report.md`.
- R14 handoff result: maintainer stage review yes, commit review yes, tag review yes after human decision, GitHub Release draft review yes, publish-ready no until maintainer performs Git and GitHub Release operations manually.
- R10 official Pal consistency: `agentpal.json`, `contacts/pals.json`, and `registry/pal.index.json` each list 9 official bundled Pal Packs and include PalSmith as `palsmith-pal-governor`.
- R10 JSON parse check passed for `agentpal.json`, `contacts/pals.json`, `registry/pal.index.json`, and all Pal `pal.json` files under `pals/`.
- Codex, Claude Code, and Generic CLI thin binding checks passed.
- Core gate propagation checks passed for `core/` shared gates.
- No local absolute maintainer paths, attachment traces, temporary pasted text traces, or private maintenance-directory references were found in public release files.
- No binary screenshot / archive / document artifacts were found in the release workspace.
- No required runtime code, package manifest, installer, scanner, validator, daemon, or service entrypoint was found.
- Ignored local outputs `.agentpal/` and `exports/` were observed as local/runtime artifacts, not release content.
- Secret-key keyword hits were reviewed as public safety-boundary language, not real credentials.
- Hard-coded semantic routing hits were reviewed as prohibitions, negative examples, or non-binding examples.
- Subagent / Deep Conductor hits were reviewed as future-design or negative-boundary references, not active v0.1.0-rc.1 behavior.

## Local Git Boundary

The final release gate should observe local Git state only until maintainers explicitly publish:

- local tag `v0.1.0-rc.1` must point at the final intended release commit
- remote `origin` is configured as `https://github.com/AgentPal/AgentPal.git`
- no push was performed during the local gate
- no GitHub Release was created or verified
- R12 did not stage, commit, tag, push, publish, or create a GitHub Release
- R14 did not stage, commit, tag, push, publish, or create a GitHub Release

If maintainers accept additional documentation changes after a local tag is created, they should create the final intended release commit, retag `v0.1.0-rc.1` if needed, then push the commit and tag before creating the GitHub Release.
