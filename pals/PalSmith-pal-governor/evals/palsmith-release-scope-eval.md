# PalSmith Release Scope Eval

This is a Markdown evaluation checklist, not a script.

## Registration

- PalSmith is registered in `agentpal.json`.
- PalSmith is registered in `registry/pal.index.json`.
- PalSmith is registered in `contacts/pals.json`.
- PalSmith id is `palsmith-pal-governor`.
- PalSmith path is `pals/PalSmith-pal-governor`.
- PalSmith direct call is `/pal PalSmith`.

## Pal Pack Shape

- `PAL.md` exists.
- `SKILL.md` exists.
- `AGENTS.md` exists.
- `pal.json` exists and parses.
- `core/output-contract.md` exists.
- PalSmith is marked or described as no-code.

## Documentation

- `docs/03-pal-pack-standard/14-runtime-task-package.md` exists.
- `docs/08-release-candidate/05-no-code-release-checklist.md` exists.
- `docs/08-release-candidate/06-palsmith-release-scope-review.md` exists.
- Task package templates have `templates/task-packages/README.md`.
- Example task packages have `examples/task-packages/README.md`.
- PalSmith delegation and handoff guidance has few-shot examples.

## Boundary Consistency

- Clean export excludes `memory/user/`, `memory/project/`, `state/`, and `reports/`.
- With-memory export requires strong confirmation and privacy review.
- GitHub/local import starts in staging and does not execute imported scripts.
- Health inspection is read-first and reports `missing` / `not-run`.
- Registry and contacts updates require exact confirmation and must not add ordinary Skills to contacts.
- Snapshot and rollback require explicit target and overwrite confirmation.

## No-Code Boundary

- No forbidden code or package files are present in releaseable workspace content.
- PalSmith is not described as a CLI, scanner, validator, installer, importer, exporter, UI, daemon, or background service.
- Any future CLI / UI / Pal Hub manager is documented as external, optional, and outside the AgentPal standard package.

## Evidence To Record

- files inspected
- JSON parse result
- forbidden file search result
- forbidden direction search result
- consistency result
- `not-run` checks
