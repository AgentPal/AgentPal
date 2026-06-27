# Release Checklist

Use this checklist before publishing AgentPal v0.3.0-rc.1 as a public MIT GitHub pre-release.

## v0.2.0-rc.1 Pre-Release Checklist

Use this section before entering `v0.2.0-rc.1` tag / push / GitHub Release work. It supplements the v0.1 release checklist below and does not authorize tag, push, or release creation by itself.

- [ ] `docs/09-roadmap/v0.2-release-readiness.md` recommends entering `v0.2.0-rc.1` release preparation.
- [ ] `docs/09-roadmap/v0.2-public-capability-summary.md` states supported and unsupported v0.2 claims without presenting future design as current behavior.
- [ ] `evals/v0.2-integration/v0.2-integration-test-matrix.md` records pass / candidate integrated readiness.
- [ ] JSON parse check passes for `agentpal.json`, contacts, registry, Pal `pal.json`, templates, and capability profiles; `agentpal.json` uses version `v0.2.0-rc.1`.
- [ ] no-runtime check confirms no scripts, package manifests, UI, installer, daemon, scanner, or validator were added.
- [ ] no-hardcoded-routing check confirms no new static task/domain routing rule.
- [ ] no-future-as-current review confirms Deep Conductor is future design, multi-agent execution is not current v0.2 behavior, Capability Inventory is not automatic probing, Routing Reward Memory is not automatic writeback, and PalBench Light is not benchmark evidence.
- [ ] no-internal-path review confirms public files do not include local absolute paths, private project data, internal report directories, or real credential material.
- [ ] Claude Code thin binding replay is recorded and passes or has an explicit blocker.
- [ ] Generic CLI thin binding replay is recorded and passes or has an explicit blocker.
- [ ] Codex workspace initialization check is recorded and passes or has an explicit blocker.
- [ ] PalSmith E2E entry is reachable from public docs.
- [ ] Mira-first entry is reachable from public docs.
- [ ] Official Pal example library entry is reachable from public docs.
- [ ] Capability Inventory profile entry is reachable from public docs.
- [ ] PalBench Light case count is at least 20 and the scoring rubric exists.
- [ ] Runtime Adapter stability guide and troubleshooting cards are reachable from public docs.
- [ ] `git status --short` is clean before tag / push / release work.
- [ ] Tag, push, and GitHub Release creation remain not done until the maintainer explicitly authorizes release operations.

## v0.3.0-rc.1 Pre-Release Checklist

Use this section before entering `v0.3.0-rc.1` tag / push / GitHub Release work. It supplements the v0.1 and v0.2 checklists and does not authorize tag, push, or release creation by itself.

- [ ] `docs/09-roadmap/v0.3-deep-conductor-readiness.md` recommends entering `v0.3.0-rc.1` release preparation.
- [ ] `evals/v0.3-integration/v0.3-deep-conductor-integration-test-matrix.md` records `pass`, `partial`, `unavailable`, `blocked`, and `not-run` status honestly.
- [ ] `docs/09-roadmap/v0.3-public-capability-summary.md` states allowed public claims and forbidden claims.
- [ ] `docs/09-roadmap/v0.3-release-checklist.md` is complete.
- [ ] `docs/09-roadmap/v0.3-release-preparation-audit.md` records the final release-prep audit.
- [ ] `docs/research/palbench-collaboration-coverage-audit.md` confirms qualitative PalBench Collaboration coverage and states remaining gaps.
- [ ] `CHANGELOG.md`, `RELEASE_NOTES.md`, `RELEASE_MANIFEST.md`, and `GITHUB_RELEASE_DRAFT.md` have `v0.3.0-rc.1` release-candidate wording.
- [ ] Deep Conductor remains documented as no-code coordination methodology, not an executor, scheduler, background workflow, CLI, scanner, validator, service, daemon, database, desktop app, web app, token meter, or cost calculator.
- [ ] Runtime-installed Skill Orchestration remains host Runtime candidate handling with current availability evidence, fallback, verification, and usage-memory records; it is not described as AgentPal executing Skills.
- [ ] Subagent / external Agent handoff remains unavailable / unknown / blocked unless a current host Runtime provides support and permission evidence.
- [ ] Context Budget remains qualitative unless a host Runtime provides exact metering evidence.
- [ ] PalBench Collaboration is described as qualitative regression coverage, not statistical benchmark evidence.
- [ ] README, docs index, roadmap index, and `RESOURCE_INDEX.md` include the v0.3 readiness, public summary, integration matrix, release checklist, and coverage audit entries.
- [ ] JSON parse checks pass.
- [ ] Pal count / contacts / registry count checks pass for the 9 official bundled Pals.
- [ ] PalBench Collaboration case count matches index and file count.
- [ ] Deep Conductor E2E package, R61 replay report, and R62 gap analysis are present.
- [ ] Release notes wording does not describe `v0.3.0-rc.1` as stable.
- [ ] no-runtime / no-program-future / no-hardcoded-routing / no-future-as-current / no-internal-path checks pass.
- [ ] `git diff --check` passes.
- [ ] `git status --short` is clean before tag / push / release work.
- [ ] Tag, push, and GitHub Release creation remain not done until the maintainer explicitly authorizes release operations.

## Root Release Files

- [ ] `README.md` exists and presents AgentPal as a Pal layer and Pal Pack Standard practice.
- [ ] `README.zh-CN.md` exists and matches the English README's current-version boundary.
- [ ] `AGENTS.md` exists and states the Runtime Response Gate, Simple Pal Mode only, Mira default routing, contacts/registry source of truth, and public-safe boundaries.
- [ ] `PAL.md` exists and describes the AgentPal Workspace identity, not a single Pal.
- [ ] `SKILL.md` exists and identifies AgentPal as a Workspace-level Skill entry, not a single-purpose Skill.
- [ ] `prompts/codex/initialize-agentpal-workspace.md` can be copied into Codex for AgentPal Workspace initialization.
- [ ] `agentpal.json` parses as valid JSON and uses version `v0.3.0-rc.1`.
- [ ] `RESOURCE_INDEX.md` exists as navigation, not a default full-context bundle.
- [ ] `core/` exists and centralizes shared AgentPal gates for runtime adapters.

## README And Docs

- [ ] `README.md` and `README.zh-CN.md` do not describe future work as active.
- [ ] `docs/` has a clear user-facing navigation path.
- [ ] Current docs distinguish AgentPal Workspace, Pal Pack, Pal, Skill, and execution runtime.
- [ ] Future-oriented runtime claims are clearly separated from current v0.3.0-rc.1 no-code protocols and host-runtime-dependent execution.
- [ ] Research docs for orchestration methodology and PalBench are present and clearly marked as qualitative design / regression foundations.
- [ ] R33 PalBench small-sample report is present, cautious, and does not claim statistical significance or model superiority.
- [ ] Deep Conductor boundary is documented: current as no-code protocols, templates, examples, evals, task packages, and replay reports; not automatic execution.
- [ ] Mira is documented as Main Pal / Leader Pal / Conductor, with team-leadership as communication layer.
- [ ] Capability Inventory, Context Access List, Workflow Topology, Pal Isolation, and Routing Reward Memory protocols are present.
- [ ] Deliverable-aware Task Judgement is documented as a Main Pal / owner Pal capability for composite deliverables.
- [ ] Context Access List, Pal Isolation, Shared Memory, Routing Reward Memory, and PalBench additions are present.
- [ ] Orchestration templates, capability profile templates, and PalBench result template are present.
- [ ] PalBench eval drafts and orchestration examples are present.
- [ ] R36 deliverable-aware examples and self-test are present: `examples/orchestration/deliverable-aware-task-judgement-example.md`, `examples/failures/domain-only-owner-handoff.md`, and `evals/orchestration/deliverable-aware-task-judgement-self-test.md`.
- [ ] R37 runtime adapter thin binding examples and self-tests are present under `examples/runtime-adapters/`, `examples/failures/`, and `evals/runtime-adapters/`.
- [ ] PalBench R33 examples are public-safe and use synthetic or placeholder data.
- [ ] No internal development reports are linked from public onboarding navigation.

## Pals

- [ ] Official bundled Pal directories exist: `pals/Mira-main`, `pals/Atlas-developer`, `pals/Vega-research`, `pals/Rhea-system`, `pals/PalSmith-pal-governor`, `pals/Quinn-quality`, `pals/Morgan-document`, `pals/Harper-writing`, and `pals/Nova-product`.
- [ ] Each official Pal has `PAL.md`, `pal.json`, `SKILL.md`, `AGENTS.md`, `README.md`, and `core/output-contract.md`.
- [ ] Specialist Pals are described as Pal Packs, not independent agent processes.
- [ ] Pal-owned Skills are stored under the owner Pal's own `skills/` directory.
- [ ] Pal memory, state, and report directories contain only public-safe placeholders unless they are ignored runtime-private files.
- [ ] PalSmith is registered as `palsmith-pal-governor` in `agentpal.json`, `registry/pal.index.json`, and `contacts/pals.json`.
- [ ] PalSmith release docs link to `docs/PalSmith.md`, Runtime Task Package standard, import/export standard, end-to-end workflows, task package templates, examples, Markdown evals, no-code release checklist, and release-scope review.
- [ ] PalSmith is documented as no-code Pal governance content, not a CLI, scanner, validator, installer, importer program, exporter program, UI, daemon, service, or runtime dependency.
- [ ] PalSmith final verification report exists at `docs/08-release-candidate/09-palsmith-final-verification-report.md`.
- [ ] AgentPal final release verification report exists at `docs/08-release-candidate/10-agentpal-final-release-verification-report.md`.
- [ ] Default Pal P2 sync plan exists at `docs/08-release-candidate/13-default-pals-p2-sync-plan.md`.
- [ ] Default Pal P2 sync verification report exists at `docs/08-release-candidate/14-default-pals-p2-sync-verification-report.md`.
- [ ] R12 release / commit review reports exist at `docs/08-release-candidate/15-agentpal-release-review-baseline.md` through `docs/08-release-candidate/19-agentpal-release-review-final-report.md`.
- [ ] R14 maintainer handoff reports exist at `docs/08-release-candidate/22-dirty-worktree-stage-review.md` through `docs/08-release-candidate/25-final-maintainer-stage-readiness-report.md`.
- [ ] Formal Skill asset standard exists at `docs/03-pal-pack-standard/15-formal-skill-assets.md`.
- [ ] Each official Pal has `skills/skill-asset-map.md` or an equivalent formal skill map.
- [ ] Flat Skill Cards are accepted when mapped, substantive, and named `skills/<formal-skill-id>.md`.
- [ ] Directory Skill Packages are accepted when mapped and backed by `skills/<formal-skill-id>/SKILL.md` or `README.md`.
- [ ] No formal Skill is represented only by `pal.json` or an index mention.
- [ ] No empty Skill directories or empty README files were created to satisfy release checks.
- [ ] Official Pal field strategy decision exists at `docs/08-release-candidate/official-pal-field-strategy-decision.md`.

## Contacts And Registry

- [ ] `contacts/pals.json` contains only valid Pal Packs.
- [ ] `registry/pal.index.json` matches the current official bundled Pal set.
- [ ] `agentpal.json`, `registry/pal.index.json`, and `contacts/pals.json` agree on the 9 official bundled Pal Packs.
- [ ] Mention aliases resolve `/pal Name` by display name or alias.
- [ ] Contacts and registry are documented as the source of truth for Pal discovery.
- [ ] Individual Pal Packs do not maintain hard-coded route maps for other Pals.

## Runtime Boundary

- [ ] AgentPal v0.1.0-rc.1 uses Simple Pal Mode only.
- [ ] AgentPal is not described as an Agent layer, multi-agent runtime, execution layer, desktop app, web app, marketplace, daemon, scanner, validator, installer, or service.
- [ ] Initialization requires no Python, Node.js, Rust, Go, CLI, UI, or background service.
- [ ] Execution claims require evidence from the host runtime.
- [ ] Exact token metering is not claimed as available in v0.1.0-rc.1.
- [ ] Claude Code project setup is documented as `cd <your-project>` then `claude`, followed by the one-prompt install.
- [ ] `claude --add-dir <path-to-AgentPal>` is documented only as fallback / advanced use, not the required default path.
- [ ] `.claude/settings.local.json` is documented as local machine configuration and not for commit.
- [ ] Generic CLI Agent setup is documented through `AGENTS.md` and `.agentpal/`.
- [ ] Claude Code and Generic CLI Agent setup prompts clearly tell users to replace `AGENTPAL_HOME` with their own AgentPal Workspace path before pasting.
- [ ] Runtime adapters point to shared `core/` gates instead of duplicating full AgentPal rules.
- [ ] Research/future orchestration docs do not activate Subagent Mode, external Agent calls, Deep Conductor, or runtime dependency requirements.

## Project Install Prompts

- [ ] `prompts/claude-code/install-agentpal-current-project.md` exists.
- [ ] `prompts/codex/remove-agentpal-current-project.md` exists.
- [ ] `prompts/codex/remove-agentpal-workspace-from-codex.md` exists.
- [ ] `prompts/claude-code/remove-agentpal-current-project.md` exists.
- [ ] `prompts/claude-code/verify-agentpal-current-project.md` exists.
- [ ] `prompts/generic-cli-agent/install-agentpal-current-project.md` exists.
- [ ] `prompts/generic-cli-agent/remove-agentpal-current-project.md` exists.
- [ ] Claude Code install prompt preserves existing `CLAUDE.md`, `AGENTS.md`, and settings content.
- [ ] Claude Code install prompt merges only `permissions.additionalDirectories`.
- [ ] Generic CLI prompt does not depend on Claude Code settings.
- [ ] Install prompts do not copy all Pal Packs into the user project.
- [ ] Install prompts do not import the whole AgentPal workspace into project instruction files.
- [ ] Project bindings are thin: they store `.agentpal/project.json`, `.agentpal/AGENTPAL.md`, root protected blocks, and runtime-specific local settings only.
- [ ] Project bindings do not copy full protocols, full Mira assets, release docs, examples, evals, or a Pal roster as source of truth.

## Public-Safe Boundary

- [ ] No private user memory is included.
- [ ] No private project state is included.
- [ ] No real task, user, verification, or internal development reports are included.
- [ ] No API keys, tokens, passwords, credentials, secrets, or private keys are included.
- [ ] No customer data or proprietary user project data is included.
- [ ] No local absolute paths are included in public-facing release files.
- [ ] Examples and templates use synthetic or placeholder data.
- [ ] `.gitignore` excludes runtime-private memory, state, reports, raw imports, temporary files, and system files while keeping release-safe README/template files.
- [ ] `.gitignore` excludes `.claude/settings.local.json`.

## License And Notices

- [ ] `LICENSE` exists and is MIT.
- [ ] `THIRD_PARTY_NOTICES.md` exists.
- [ ] Third-party resources keep their original licenses and notices.
- [ ] No long third-party source, README, Skill, or documentation text is copied into the release.

## Release Notes

- [ ] `CHANGELOG.md` records user-visible release changes for `v0.1.0-rc.1`.
- [ ] `RELEASE_NOTES.md` is user-facing and explains who the release is for, who it is not for, what is included, and what is not included.
- [ ] PalSmith release notes describe official registration, Runtime Task Package planning, import/export planning, release-scope review, and the no-code boundary.
- [ ] `GITHUB_RELEASE_DRAFT.md` is suitable for manual GitHub Release drafting and includes What's included, Current status, Known limitations, Getting started, and Safety notes.
- [ ] `GITHUB_RELEASE_DRAFT.md` does not claim a remote push or online GitHub Release exists unless that has been verified.
- [ ] `RELEASE_MANIFEST.md` records the observed local tag, commit, remote, and GitHub Release state.

## GitHub Publication

- [ ] Final intended release contents are committed.
- [ ] Local tag `v0.1.0-rc.1` points to the final intended release commit.
- [ ] If no remote exists, create an empty GitHub repository before adding a remote.
- [ ] Add or verify the intended remote.
- [ ] Confirm the intended remote URL is `https://github.com/AgentPal/AgentPal.git`.
- [ ] Confirm whether existing local tags `v0.1.0-rc.1` and `v0.1.0-rc.2` are both intentional before creating, moving, or publishing any release tag.
- [ ] Review the full dirty worktree and stage only maintainer-approved release content.
- [ ] Review `docs/08-release-candidate/22-dirty-worktree-stage-review.md` before staging.
- [ ] Choose single release commit or split commit plan from `docs/08-release-candidate/23-commit-grouping-plan.md`.
- [ ] Review `docs/08-release-candidate/24-maintainer-release-handoff.md` before any tag or push.
- [ ] Push the final release commit.
- [ ] Push tag `v0.1.0-rc.1`.
- [ ] Create the GitHub Release from tag `v0.1.0-rc.1`.
- [ ] Paste and review `GITHUB_RELEASE_DRAFT.md` as the release body.
- [ ] Mark the GitHub Release as a pre-release or release candidate if that matches the repository policy.
- [ ] Confirm the published release page links to the intended tag and commit.

## Validation

- [ ] JSON parse checks passed.
- [ ] Official Pal count checks passed for `agentpal.json`, `contacts/pals.json`, and `registry/pal.index.json`.
- [ ] Official Pal root-file checks passed for `README.md`, `PAL.md`, `SKILL.md`, `AGENTS.md`, `pal.json`, and `core/output-contract.md`.
- [ ] Formal Skill count / listed Skill asset consistency checks passed or gaps are documented.
- [ ] Formal Skill asset maps show missing asset count 0 under the current release standard.
- [ ] Capability profile JSON templates and examples parse as valid JSON.
- [ ] no-runtime check confirms no scripts, package files, CLI, UI, installer, daemon, scanner, or validator were added.
- [ ] Ignored local output directories such as `.agentpal/` and `exports/` are not included as release content.
- [ ] no-hardcoded-routing check confirms no new task/domain fixed route rules.
- [ ] Markdown sanity checks passed.
- [ ] Relative links in root release files were reviewed.
- [ ] Native `/pal` runtime API behavior is treated as not-run unless verified in the target runtime.
- [ ] Live web fetch and external link checking are treated as not-run unless separately verified.
- [ ] Public-safety keyword search was reviewed by a human.
- [ ] Version references in root release files use `v0.1.0-rc.1`.
- [ ] If `SECURITY.md` is absent, maintainers have accepted that as a release-candidate limitation or added a release-safe security policy before publication.
