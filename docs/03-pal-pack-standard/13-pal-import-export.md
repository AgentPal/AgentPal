# Pal Import And Export

## Status

Current for AgentPal `v0.3.0-rc.1`.

Pal import and export are Pal asset governance tasks. The official owner Pal is PalSmith (`/pal PalSmith`), while the current Agent Runtime performs actual file operations and must return evidence.

AgentPal does not include a downloader, packer, scanner, validator, importer, exporter, installer, daemon, or CLI for Pal assets.

## Import Rule

All external imports are untrusted by default and must enter staging before installation.

Supported source types for a Runtime Task Package:

- GitHub repository URL
- GitHub repository subdirectory
- GitHub Release archive
- GitHub branch, tag, or commit
- local directory
- local archive
- AgentPal internal Pal copy
- legacy project `.agentpal/pals` archive, if explicitly provided as an import source and not as a default project binding

PalSmith classifies imports as Standard Pal Pack, Pal Team Pack, ordinary Skill, Knowledge Pack, Persona Pack, Tool Pack, Mixed Resource Pack, or Unknown Resource.

Only valid Pal Packs can enter `official/pals/` or the selected organization Pal area and the central contacts. Ordinary Skills, tools, models, plugins, MCP servers, external Agents, raw repositories, Knowledge Packs, and Persona Packs do not become Pal contacts.

## Pal Import Staging Task Package

The staging task package tells the current runtime:

- source to read, copy, download, or extract
- staging target
- allowed read paths
- allowed write paths
- forbidden paths
- files that must not be executed
- risk checks
- expected import report
- confirmation questions

The runtime must not execute imported scripts, directly install into `official/pals/` or another selected organization Pal area, automatically write central contacts, automatically write legacy registry files, or import `memory/user/` and `memory/project/` into a public Pal Pack.

## Pal Install Task Package

After staging review, PalSmith may generate an install task package. Installation still requires user confirmation.

Risk files such as scripts, executables, private memory, state, reports, logs, credentials, and repository metadata should be excluded or quarantined according to the task package. Registry and contacts writes remain separate task packages.

## Registry And Contacts Update Task Packages

Registry updates require a standard Pal Pack and a JSON diff proposal.

Contacts updates require a standard Pal Pack, discoverable/contactable collaboration flags, at least one allowed collaboration mode, and explicit confirmation.

Ordinary Skills, Knowledge Packs, Tool Packs, raw repositories, and unknown resources must not enter contacts.

## Clean Pal Export Task Package

Clean Pack Export includes public-safe Pal files and excludes private runtime data.

Include `PAL.md`, `SKILL.md`, `AGENTS.md`, `pal.json`, `README.md`, `CHANGELOG.md`, `LICENSE`, `identity/`, `core/`, `knowledge/`, `skills/`, `runbooks/`, `workflows/`, `evals/`, `export-manifest.json`, and `export-report.md`.

Exclude `memory/user/`, `memory/project/`, `state/`, `reports/`, private reasoning logs, private contacts history, runtime private logs, user private files, `.env`, credentials, tokens, executable scripts, logs, cache, and temporary files.

## With Memory Export Task Package

With Memory Export may include private memory, state, reports, and usage history. It requires strong confirmation and a follow-up question about which memory types to include.

Do not use With Memory Export for public sharing unless the user explicitly confirms and the privacy check passes.

## Export Manifest

Each export task package should request an `export-manifest.json` with schema, export type, timestamps, Pal identity, source path, included and excluded sections, memory/state/report flags, private data risk, license, compatible runtimes, and checksum or runtime evidence.
