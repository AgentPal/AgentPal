# Faye To PalSmith Handoff Standard

Date: 2026-06-29
Standard id: `agentpal-faye-palsmith-handoff-standard.v0.5`

## Purpose

This standard defines how Faye hands a delivery design to PalSmith without becoming PalSmith and without mutating central roster or official Pal assets.

The handoff artifact is `FAYE_BUILD_REQUEST.md`.

## Required Handoff Sections

Every Faye Build Request must include:

- Pal Team Blueprint;
- Faye Build Request summary;
- PalSmith Build Scope;
- required Pal assets;
- Pal Skill needs;
- candidate Agent Skill refs;
- missing information;
- human review needed;
- forbidden operations;
- evidence expected from PalSmith or the host Runtime.

## Pal Team Blueprint

The Pal Team Blueprint describes candidate Pal responsibilities for the delivery. It may include:

- delivery owner perspective;
- research perspective;
- writing / content perspective;
- developer / implementation perspective;
- quality / verification perspective;
- domain expert perspective;
- operations / reporting perspective.

These are AI judgement inputs only. They are not central roster entries, route maps, keyword routes, role maps, or fixed assignments.

## PalSmith Build Scope

PalSmith may be asked to:

- create a Pal creation package;
- complete missing Minimal Pal assets;
- propose Standard Pal assets;
- classify source materials;
- produce a target file checklist;
- identify Pal-owned Skill candidates;
- identify Agent Skill reference candidates;
- prepare readiness review evidence.

PalSmith must not automatically modify central contacts, official Pal assets, or external project `.agentpal/` directories.

## Required Pal Assets

The request should name required Pal assets using the PalSmith creation standard. A Minimal Pal request should consider:

- `README.md`
- `PAL.md`
- `pal.json`
- `AGENTS.md`
- `SKILL.md`
- `identity/`
- `core/`
- `knowledge/`
- `skills/`
- `workflows/`
- `runbooks/`
- `memory/`
- `evals/`
- `reports/`
- `state/`

If the delivery only needs an existing Pal or an Org Pack reference, the request should say so and avoid creating a new Pal.

## Pal Skill Needs

Pal Skill needs are no-code professional methods that belong under a Pal Pack only after user approval and PalSmith review.

Examples:

- delivery discovery method;
- business-flow decomposition method;
- acceptance-review method;
- training handoff method;
- report synthesis method.

## Candidate Agent Skill Refs

Agent Skill refs are host Runtime capabilities. They may include browser, document, repository, spreadsheet, plugin, MCP, or API helper candidates only when the current Runtime can verify availability.

They must be recorded as candidates, not as Pal-owned Skills, and not as connector execution.

## Missing Information

The request must preserve missing information honestly:

- `missing`: required but absent;
- `unknown`: not enough evidence;
- `not-run`: check was not executed;
- `requires-human-review`: human judgement is required before use.

## Forbidden Operations

The handoff must explicitly forbid:

- central roster mutation;
- official Pal mutation;
- external project `.agentpal/` writes by default;
- credential storage;
- customer-private storage in reusable packs;
- keyword route creation;
- connector execution;
- scanner, validator, marketplace, installer, daemon, database, auto-sync, or auto-execution behavior;
- remote publication operations without explicit user authorization.

## Evidence Returned

After PalSmith or a host Runtime acts on an approved request, the evidence should include:

- files created or changed;
- parse results for JSON metadata;
- required asset checklist;
- no credential or customer-private leak review;
- no keyword routing review;
- no central roster or official Pal diff;
- explicit `not-run` entries for any check not executed.
