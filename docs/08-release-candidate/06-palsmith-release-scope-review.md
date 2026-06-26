# PalSmith Release-Scope Review

## Status

Current for AgentPal `v0.1.0-rc.1`.

PalSmith is ready to enter the GitHub-ready release scope as an official no-code system Pal, with one condition: release preparation must keep the no-code boundary intact and must not convert PalSmith into tool software.

## 1. Current Positioning

PalSmith is AgentPal's official no-code Pal asset governance Pal. It plans Pal creation, Pal team creation, import staging, clean export, with-memory export, health inspection, registry/contacts updates, official Pal registration, snapshots, and rollback through Runtime Task Packages.

PalSmith is not a CLI, scanner, validator, importer, exporter, installer, daemon, UI, background service, or runtime dependency.

## 2. Completed Capability Scope

- Official Pal registration in `agentpal.json`, `registry/pal.index.json`, and `contacts/pals.json`.
- Runtime Task Package field standard.
- End-to-end PalSmith workflows.
- Task package templates for creation, team creation, import, install, export, health inspection, registry, contacts, official registration, snapshot, and rollback.
- Example task packages for user learning, Mira few-shot context, and release checks.
- Markdown evals for official registration, registry/contacts consistency, no-code boundary, and release scope.
- PalSmith delegation and handoff guidance with few-shot examples.

## 3. What PalSmith Does Not Include

- No Python, Node.js, Rust, shell, or compiled code.
- No built-in download, copy, archive, import, export, scan, validation, install, registry sync, or contacts sync program.
- No UI, daemon, service, background worker, marketplace, or hosted component.
- No private user memory, private project memory, runtime state, staging content, export output, quarantine content, or logs.

## 4. GitHub-Ready Release Scope

The following PalSmith assets are releaseable:

- `pals/PalSmith-pal-governor/PAL.md`
- `pals/PalSmith-pal-governor/SKILL.md`
- `pals/PalSmith-pal-governor/AGENTS.md`
- `pals/PalSmith-pal-governor/pal.json`
- `pals/PalSmith-pal-governor/identity/`
- `pals/PalSmith-pal-governor/core/`
- `pals/PalSmith-pal-governor/governance/`
- `pals/PalSmith-pal-governor/checklists/`
- `pals/PalSmith-pal-governor/templates/`
- `pals/PalSmith-pal-governor/workflows/`
- `pals/PalSmith-pal-governor/examples/`
- `pals/PalSmith-pal-governor/evals/`
- Runtime Task Package standard docs.
- PalSmith usage and end-to-end workflow docs.
- No-code release checklist.
- Mira PalSmith routing knowledge.
- AgentPal registry, contacts, and manifest entries for PalSmith.

## 5. Not Releaseable

Do not publish runtime-private or generated state as PalSmith release content:

- `.agentpal/`
- `exports/`
- import staging
- snapshots
- quarantine
- runtime logs
- `memory/user/`
- `memory/project/`
- private `state/`
- private `reports/`
- credentials, tokens, keys, local settings, or real user/project data
- any PalSmith CLI or tool code

## 6. Must-Keep Documents

- `docs/PalSmith.md`
- `docs/03-pal-pack-standard/14-runtime-task-package.md`
- `docs/07-authoring-pals/12-use-palsmith.md`
- `docs/07-authoring-pals/13-palsmith-end-to-end-workflows.md`
- `docs/08-release-candidate/05-no-code-release-checklist.md`
- this release-scope review
- `RELEASE_NOTES.md`
- `CHANGELOG.md`
- `GITHUB_RELEASE_DRAFT.md`
- `pals/Mira-main/knowledge/agentpal-usage/palsmith-routing.md`
- `pals/PalSmith-pal-governor/templates/task-packages/README.md`
- `pals/PalSmith-pal-governor/examples/task-packages/README.md`
- `pals/PalSmith-pal-governor/evals/palsmith-release-scope-eval.md`

## 7. Later Work

- More industry Pal examples.
- More official Pal consistency evals.
- Optional external tooling only if it lives outside the AgentPal standard package.

## 8. Forbidden Backflow

Do not reintroduce:

- old PalSmith tool directories
- old PalSmith executable files
- test scripts
- package manifests
- CLI command docs for PalSmith
- scanner / validator / importer / exporter / installer programs
- UI or daemon work

## 9. Pre-Release Consistency Check

Before release, verify:

- PalSmith id is `palsmith-pal-governor`.
- PalSmith path is `pals/PalSmith-pal-governor`.
- `agentpal.json`, `registry/pal.index.json`, and `contacts/pals.json` all point to the same id/path.
- PalSmith direct call is `/pal PalSmith`.
- `no_runtime_code` is present or equivalently stated.
- Task package and example indexes exist.
- PalSmith delegation and handoff guidance contains few-shot cases.
- Forbidden files are absent.
- Forbidden direction terms appear only in negative boundary or generic runtime compatibility contexts.

## 10. Current Open Risks

- The PalSmith documentation set is useful but broad. Future maintenance should avoid adding overlapping guides when a small index or cross-link is enough.
- If a future Pal Hub, CLI, or UI is pursued, it must be an independent optional project and must not become part of the AgentPal v0.1 standard package.
