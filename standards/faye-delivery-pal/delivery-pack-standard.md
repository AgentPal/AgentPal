# Delivery Pack Standard

Date: 2026-06-29
Standard id: `agentpal-delivery-pack-standard.v0.5`

## Purpose

A Delivery Pack is a no-code project delivery asset package for AgentPal. It turns one concrete business delivery target into reusable structure, project facts, flow plans, task packages, Pal team recommendations, integration notes, acceptance checks, training notes, and reports.

Delivery Pack is the public-facing name. FDE Pack may remain an internal or adjacent concept for expert delivery practice, but this standard uses Delivery Pack for business delivery.

A Delivery Pack is not a program, connector, app, CLI, installer, scanner, validator, daemon, database, marketplace, hub, API client, auto-sync engine, or auto-execution engine.

## Fixed Three-Layer Structure

Every Delivery Pack uses this simple conceptual structure:

```text
Project
  -> Flow Pack
  -> Task Package
```

Project describes the business delivery context. Flow Pack describes one business process inside that project. Task Package describes one actionable work package that a Pal owner and runtime execution layer may handle after separate judgement and evidence.

## Required Minimal Structure

```text
DELIVERY.md
PROJECT.md
FLOWS/
TASKS/
PAL_TEAM.md
INTEGRATIONS/
ACCEPTANCE.md
TRAINING.md
REPORTS/
FAYE_BUILD_REQUEST.md
delivery-pack.json
```

## Required Files

| File | Purpose |
| --- | --- |
| `DELIVERY.md` | Human-facing package entry, purpose, audience, and usage boundary. |
| `PROJECT.md` | Business context, user flows, data list, system notes, risk list, launch plan, and missing information. |
| `FLOWS/` | Flow Pack shells for business processes. |
| `TASKS/` | Task Package shells for concrete work packages. |
| `PAL_TEAM.md` | Pal Team Blueprint and candidate Pal perspectives. |
| `INTEGRATIONS/` | Integration notes, system names, access assumptions, and no-connector boundary. |
| `ACCEPTANCE.md` | Acceptance criteria, review states, evidence requirements, and human review points. |
| `TRAINING.md` | User training, handoff notes, operating rules, and escalation guidance. |
| `REPORTS/` | Report shells, retrospective notes, and delivery evidence placeholders. |
| `FAYE_BUILD_REQUEST.md` | Faye to PalSmith handoff request. |
| `delivery-pack.json` | Machine-readable metadata and safety flags. |

## `delivery-pack.json` Required Defaults

`delivery-pack.json` must parse as JSON and include safe defaults:

```json
{
  "schema": "agentpal.delivery-pack.v0.5",
  "type": "delivery-pack-template",
  "external_projects_copy_assets_by_default": false,
  "customer_private_assets_allowed_in_reusable_pack": false,
  "credentials_allowed": false,
  "keyword_routing_allowed": false,
  "connector_included": false,
  "marketplace_program_included": false,
  "requires_human_review": true
}
```

Recommended additional false flags:

- `scanner_included`
- `validator_included`
- `auto_execution`
- `auto_sync`
- `can_modify_central_roster`
- `official_pal_changes_allowed_by_default`

## Relationship To Org Packs

An Org Pack describes a reusable AI organization. A Delivery Pack describes one concrete business delivery. A Delivery Pack may reference Org Packs as AI judgement inputs, but it must not copy central rosters, official Pal bodies, or customer-private records into public reusable examples.

## Relationship To FDE Packs

An FDE Pack describes an expert delivery method. A Delivery Pack may reference one or more FDE Packs when expert judgement is needed. High-risk professional advice remains `requires-human-review`.

## Relationship To PalSmith

A Delivery Pack may include a Faye Build Request for PalSmith. The request can describe needed Pals, Pal assets, Pal Skill needs, and candidate Runtime Skill references. It must not authorize automatic Pal creation, central roster mutation, official Pal mutation, or external project writes.

## Prohibited Defaults

Delivery Packs must not:

- store credentials or secrets;
- store real customer-private data in reusable templates or public examples;
- copy assets into external project `.agentpal/` by default;
- modify central contacts or official Pals;
- include keyword routes or deterministic semantic routes;
- become connectors, scanners, validators, marketplaces, installers, daemons, databases, API clients, auto-sync engines, or auto-execution engines;
- claim task execution without host-runtime evidence.
