# Org Pack Standard

Date: 2026-06-28

## Purpose

An Org Pack is a reusable no-code AI organization asset package for AgentPal. It describes how an AI organization, AI team, professional workflow, or business practice can be represented through public-safe organization materials.

Org Packs help users reuse organization structure, recommended Pal perspectives, workflow candidates, governance rules, capability references, memory policies, and verification checklists without turning AgentPal into a runtime or copying central assets into every external project.

## Org Pack vs Pal Pack

| Org Pack | Pal Pack |
| --- | --- |
| Describes an organization or repeatable work system. | Describes one Pal identity and its assets. |
| May recommend several Pals as AI judgement inputs. | Owns a single Pal's identity, knowledge, skills, workflows, examples, and output contract. |
| Does not copy or modify the central roster. | Can be registered into central contacts through a separate governed process. |
| Focuses on organization-level reuse, governance, and verification. | Focuses on one working companion. |

## Org Pack vs Project Template

An Org Pack is not an external project template.

External user projects remain thin-bound. Org Pack assets live in the AgentPal Workspace, reusable template areas, public examples, or approved private organization records. They are not copied into an external project's `.agentpal/` directory by default.

## Required Files

A minimal Org Pack should include:

- `ORG.md`
- `org.json`
- `README.md`
- `memory-policy.md`
- `customer-private-assets-boundary.md`
- `governance/README.md`
- `workflows/README.md`
- `capability-inventory/README.md`
- `verification/README.md`

## Recommended Files

A fuller Org Pack may include:

- recommended Pals
- workflow candidates
- verification checklists
- business system governance notes
- capability inventory references
- governance decision templates
- FDE / expert delivery notes
- cross-organization handoff notes
- public-safe examples
- PalBench eval cases

## Reusable Assets

Reusable assets can include:

- de-identified organization patterns
- public-safe workflow candidates
- public-safe governance rules
- public-safe verification checklists
- role and responsibility descriptions
- capability profile references
- non-secret business system governance notes
- reusable memory policy

Reusable assets must be safe to publish and safe to copy into another AgentPal Workspace.

## Customer-Private Assets

Customer-private assets include:

- customer data
- customer credentials
- customer system identifiers
- real customer project memory
- private business rules
- private evidence
- private project reports
- private workflow adaptations that reveal sensitive facts

Customer-private assets must not be included in a reusable public Org Pack. They belong in approved private records, such as central project records or customer-private delivery records.

## Central Roster Relationship

An Org Pack may recommend Pals, but it must not copy, replace, or modify the central roster.

The source of truth remains:

- `workspace/organization/contacts/pals.json`
- `workspace/organization/contacts/PAL_CONTACTS.md`
- `official/pals/`

Recommended Pals are AI judgement inputs only. They are not keyword routes, domain routes, hard assignments, or automatic dispatch rules.

## Thin Binding Relationship

External projects still use thin binding by default:

- `.agentpal/project.json`
- `.agentpal/AGENTPAL.md`
- root protected instruction blocks
- optional Claude Code local settings

An Org Pack must not create or require these external project directories by default:

- `.agentpal/org-pack/`
- `.agentpal/pals/`
- `.agentpal/memory/`
- `.agentpal/reports/`
- `.agentpal/capability-inventory/`
- `.agentpal/business-systems/`
- `.agentpal/governance/`
- `.agentpal/workflows/`
- `.agentpal/evals/`

## Capability Inventory Relationship

Org Packs may reference Capability Inventory records and templates as AI judgement inputs. They must not become scanners, automatic detectors, automatic profile writers, or deterministic routing tables.

Capability evidence should preserve `unknown`, `not-run`, and `missing` states until real evidence exists.

## Governance Relationship

Org Packs may define governance rules, review checkpoints, decision records, and change notes. These are human-governed no-code records. They do not execute changes, call external APIs, write back to customer systems, or change central contacts automatically.

## Verification Relationship

Org Packs should include verification checklists and PalBench cases. Verification records must distinguish:

- pass
- fail
- not-run
- blocked
- missing evidence
- unknown

Verification text must not turn `not-run` or `missing` into `pass`.

## Prohibited Contents

Org Packs must not contain:

- installer
- marketplace or hub program
- daemon
- database
- connector
- API client
- credential store
- auto sync engine
- auto execution engine
- scanner
- validator
- keyword router
- `keyword_map`
- `domain_map`
- `role_map`
- deterministic task-domain-to-Pal routing
- copied central roster
- copied Pal Packs in external projects
- real credentials, private tokens, API keys, cookies, passwords, or secrets
- real customer private data

## No Marketplace / No Installer / No Scanner / No Connector Boundary

An Org Pack is a Markdown / JSON / protocol asset package. It is not a software distribution mechanism and must not claim to install, scan, connect, validate, synchronize, execute, or publish anything by itself.

Host runtimes may read Org Pack files and perform real actions only when separately instructed and when they provide evidence.
