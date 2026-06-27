# Official Pal Field Strategy Decision

Date: 2026-06-26

Status: R13 release-readiness decision.

## Problem

AgentPal has several places that can express official Pal status:

- `agentpal.json`
- `registry/pal.index.json`
- `contacts/pals.json`
- individual Pal `pal.json` files

R12 left a P2 question: should `official: true` be required in every location, or should the official set be determined by central workspace files?

## Options

| Option | Description | Tradeoff |
| --- | --- | --- |
| Central only | `agentpal.json` and registry define official Pals. | Lowest schema churn, but contacts and Pal metadata can look less explicit. |
| Contacts also carry official | Contacts preserve an official flag or equivalent registered official set. | Clearer runtime discovery, but duplicates status. |
| Every Pal `pal.json` must carry official | Each official Pal self-identifies as official. | Easy local inspection, but creates release churn and user Pal ambiguity. |

## Decision

For v0.1.0-rc.1, the official bundled Pal set is determined by:

- `agentpal.json` `official_bundled_pals`
- `registry/pal.index.json` `items`
- `contacts/pals.json` `registered_pals`

Individual Pal `pal.json` files may include `official: true`, `system_pal`, or similar metadata when already present, but this release does not require every official Pal Pack to duplicate the `official` field.

## R13 Action

R13 does not perform a broad schema rewrite. It preserves existing fields and avoids reordering Pal metadata.

## Why This Is Not A Blocker

The release already has three central official-set surfaces with 9 entries each. Requiring identical `official` fields in every Pal file would create churn without changing runtime behavior.

## Future Schema Note

A future schema version may make official status explicit through a normalized field model, but that should be done as a schema migration, not as a release-readiness patch.

