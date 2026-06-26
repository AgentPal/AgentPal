# AgentPal v0.1.0-rc.1 Release Notes Draft

AgentPal v0.1.0-rc.1 is the first release candidate for the AgentPal Workspace and Pal Pack Standard practice.

AgentPal is a Markdown/JSON Pal layer for existing runtimes such as Codex and Claude Code. It helps a runtime load Pal identities, public knowledge, skills, output contracts, routing rules, public-safe memory boundaries, and release-safe collaboration conventions.

## Who This Release Is For

Use this release if you want to:

- try a Pal Workspace inside an existing agent runtime
- inspect the Pal Pack Standard structure
- use the bundled official Pals as public working assets
- use PalSmith as a no-code Pal asset governance Pal for Pal creation, import/export planning, health checks, and Runtime Task Package planning
- create or review public-safe Pal Packs
- study Simple Pal Mode and Pal discovery through contacts and registry files

## Who This Release Is Not For

This release is not suitable if you need:

- a standalone desktop app or web app
- a complete multi-agent runtime
- background execution, daemons, scanners, validators, or installers
- a hosted marketplace or Pal Hub
- automatic deep runtime adapters
- active Subagent Mode, child workflow orchestration, remote agent orchestration, or MCP-hosted agent execution

## What's Included

- AgentPal Workspace root instructions and release files
- initialization prompt for Codex / Claude Code style runtimes
- `agentpal.json` workspace manifest
- contacts and registry files for Pal discovery
- nine official public Pal Packs: Mira, Atlas, Vega, Rhea, PalSmith, Quinn, Morgan, Harper, and Nova
- Pal Pack Standard documentation
- PalSmith docs, Runtime Task Package standard, task package templates, example task packages, Markdown evals, and release-scope review
- release maintenance and public-safe checklist docs
- public examples, evals, prompts, templates, and protocols
- MIT license and third-party notice file

## Current Status

Current active task-handling path: Simple Pal Mode only.

Default entry Pal: Mira.

Direct Pal call pattern: `/pal Name`.

Pal discovery source of truth: `contacts/` and `registry/`.

## Safety Notes

Public releases must not include private user memory, private project state, real task reports, internal development notes, secrets, credentials, customer data, local absolute paths, unauthorized logs, or unauthorized third-party full text.

PalSmith is included only as Markdown/JSON Pal governance content. It is not an executable command layer, scanner, validator, importer program, exporter program, installer, UI, daemon, service, or runtime dependency.

Future design materials must remain clearly labeled as future, experimental, or inactive unless a future release explicitly activates them.

## Known Limitations

- No desktop app.
- No marketplace or hosted Pal Hub.
- No complete multi-agent runtime.
- No execution layer.
- No active Subagent Mode or child workflow orchestration.
- No automatic deep runtime adapters.
- No exact token metering.

## Release Recommendation

This draft is suitable for maintainer review. Publish only after the public-safe audit, docs audit, and Pal Pack audit are accepted for v0.1.0-rc.1.
