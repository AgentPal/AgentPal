# No-Code Release Checklist

## Status

Current for AgentPal `v0.1.0-rc.1`.

Use this checklist before public release work that touches PalSmith, Pal import/export, Pal creation, or Runtime Task Package documents.

## PalSmith Final Release Checklist

- PalSmith is listed as an official Pal in `README.md`, `agentpal.json`, `registry/pal.index.json`, and `contacts/pals.json`.
- PalSmith id is `palsmith-pal-governor`, and PalSmith path is `pals/PalSmith-pal-governor`.
- PalSmith direct call is `/pal PalSmith`.
- `docs/PalSmith.md`, `docs/07-authoring-pals/12-use-palsmith.md`, and `docs/07-authoring-pals/13-palsmith-end-to-end-workflows.md` are linked from docs navigation.
- `docs/03-pal-pack-standard/13-pal-import-export.md` and `docs/03-pal-pack-standard/14-runtime-task-package.md` are linked from docs navigation.
- `docs/08-release-candidate/06-palsmith-release-scope-review.md` exists and records releaseable / not releaseable PalSmith content.
- `docs/08-release-candidate/09-palsmith-final-verification-report.md` exists and records the R09 final verification result.
- `RELEASE_NOTES.md`, `CHANGELOG.md`, and release candidate notes mention PalSmith as a no-code Pal asset governance Pal.
- Task package template and example indexes exist at `pals/PalSmith-pal-governor/templates/task-packages/README.md` and `pals/PalSmith-pal-governor/examples/task-packages/README.md`.
- `pals/PalSmith-pal-governor/evals/palsmith-release-scope-eval.md` is present as a Markdown eval, not a script.
- No old executable PalSmith prototype, command docs, scanner, validator, installer, importer program, exporter program, UI, or daemon has been reintroduced.
- Public release content excludes staging, quarantine, `memory/user/`, `memory/project/`, private `state/`, private `reports/`, credentials, tokens, and local-only runtime evidence.

## Forbidden File Check

Release content must not include:

- `.py`
- `.js`
- `.ts`
- `.rs`
- `.ps1`
- `.sh`
- `.bat`
- `.cmd`
- `package.json`
- `requirements.txt`
- `Cargo.toml`

Ignore `.git/` internals and external system caches. Do not ignore releaseable workspace files.

## Forbidden Runtime Direction Check

Confirm that AgentPal and PalSmith are not described as:

- UI
- installer
- daemon
- background service
- scanner
- validator
- importer program
- exporter program
- executable command layer

If words such as `CLI`, `scanner`, `validator`, `installer`, `daemon`, `importer`, or `exporter` appear, they must be in a negative boundary such as "PalSmith is not a CLI" or "AgentPal does not include an importer program." Generic runtime compatibility guides may mention command-line agents, but PalSmith must not be positioned as a command.

## Dependency Check

Public AgentPal use must not require Python, Node.js, Rust, package installation, or language package-manager commands.

If future maintainers add optional external tools, they must live outside the AgentPal standard package or be clearly marked as external, optional, and not part of v0.1.0-rc.1 runtime behavior.

## PalSmith Boundary Check

- PalSmith is a no-code Pal asset governance Pal.
- PalSmith generates Runtime Task Packages.
- PalSmith does not directly read, write, copy, download, package, restore, publish, or delete files.
- Current Agent Runtime executes only after user confirmation where required.
- Runtime evidence is required before PalSmith reports work as done.

## Import / Export Check

- All imports use `Pal Import Staging Task Package` first.
- Imported resources are untrusted by default.
- Staging and quarantine are separate from formal `pals/`.
- Imported scripts are not executed.
- Clean export excludes `memory/user/`, `memory/project/`, `state/`, `reports/`, logs, cache, credentials, and tokens.
- With-memory export requires strong confirmation and privacy report.
- Public release with private memory is refused or converted to clean export.

## Registry / Contacts Check

- Registry and contacts updates are separate task packages.
- Current JSON is snapshotted before approved writes.
- JSON parse evidence is reported after writes.
- Ordinary Skills, tools, models, plugins, raw repositories, Knowledge Packs, and Persona Packs are not contacts.
- Contacts require discoverable/contactable collaboration flags and allowed modes.

## Official Pal Consistency Check

- If README says a Pal is official, `agentpal.json` should include that Pal in the official Pal list or equivalent field.
- `registry/pal.index.json` should include the same Pal id and path.
- `contacts/pals.json` should include the same Pal id and path, or a documented reason why the Pal is not contactable.
- Pal path should exist.
- Pal id should match `pal.json`.
- Pal type should be `pal-pack` or the current standard-compatible value.
- Official no-code Pals should carry `no_runtime_code` or an equivalent no-code boundary.
- The Pal's public docs should not describe it as a CLI, scanner, validator, installer, importer, exporter, daemon, UI, or runtime tool.
- Registration should use `Official Pal Registration Task Package`, `registry update task package`, or `contacts update task package`; it should not use a program.

## Evidence Check

Release report should include:

- forbidden file check result
- forbidden direction check result
- Runtime Task Package anchor check
- JSON parse result
- `git diff --check`
- `git status --short`
- explicit `not-run` for anything not verified
