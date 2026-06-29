# Repository Structure

AgentPal is a central AI organization workspace. The root directory is intentionally organized so users can see the public standards, official assets, central workspace records, templates, examples, evals, release evidence, archive, and docs at a glance.

## Current Root Shape

```text
AgentPal/
  README.md
  AGENTS.md
  PAL.md
  SKILL.md
  agentpal.json
  RESOURCE_INDEX.md
  CHANGELOG.md
  LICENSE
  CONTRIBUTING.md

  standards/
  official/
  workspace/
  templates/
  examples/
  evals/
  release/
  archive/
  docs/
```

## Primary Directories

| Directory | Role |
| --- | --- |
| `standards/` | Public standards for no-code boundaries, thin binding, central organization records, AI judgement routing, Deep Conductor, capability inventory, governance, org packs, and schema notes. |
| `official/` | Official bundled assets such as Pal Packs, future team definitions, no-code workflows, and organization packs. |
| `workspace/` | Central organization workspace for contacts, project-record templates, shared resources, and public-safe state placeholders. |
| `templates/` | Public templates for thin binding, Pal Packs, orchestration packages, context packets, governance, organization records, and prompt families. |
| `examples/` | Public-safe examples and failure examples. |
| `evals/` | Self-tests, qualitative regression cases, and release checks. |
| `release/` | Release evidence, audits, fresh-clone checks, and release-history notes. |
| `archive/` | Historical migration notes and legacy materials retained for traceability. |
| `docs/` | User-facing and contributor-facing documentation. |

## Central Organization Assets

Official Pals live under:

```text
official/pals/
```

The central Pal roster lives under:

```text
workspace/organization/contacts/pals.json
workspace/organization/contacts/PAL_CONTACTS.md
workspace/organization/contacts/aliases.json
```

The central project-record template lives under:

```text
workspace/projects/_template/
```

Real project records use `workspace/projects/<project-id>/` and are private by default. They are not copied into external user projects.

## Thin External Project Binding

External user projects should receive only a thin binding by default:

```text
<project>/.agentpal/project.json
<project>/.agentpal/AGENTPAL.md
<project>/AGENTS.md protected block
<project>/CLAUDE.md protected block
<project>/.claude/settings.local.json
```

The binding points back to the AgentPal workspace. It must not copy full Pal Packs, central contacts, memory, reports, workflows, source maps, derived knowledge, or release files into the external project.

Forbidden default external-project directories include:

```text
.agentpal/memory/
.agentpal/state/
.agentpal/reports/
.agentpal/context/
.agentpal/index/
.agentpal/pals/
.agentpal/workflows/
.agentpal/evals/
```

## Capability Inventory

R78 split the legacy root capability inventory surfaces into three active locations:

| Directory | Role |
| --- | --- |
| `standards/capability-inventory/` | Profile standards, capability matrices, runtime detection protocol, model routing policy, and plugin discovery protocol. |
| `workspace/organization/capability-inventory/` | Current central organization runtime, model, Skill, plugin, MCP, business-system, and usage-memory records. |
| `workspace/projects/_template/capability-inventory/` | Template for project-level capability records under central project records. |
| `examples/capability-inventory/` | Public-safe illustrative profiles and task judgement examples. |
| `templates/capability-inventory/` | Copyable JSON profile templates. |

Capability Inventory is a no-code profile layer. It can be maintained manually by users, organized by Pals from confirmed information, or updated from current host Runtime evidence. It does not scan machines, install tools, enable plugins, or route by keywords.

For the manual update flow, see `docs/03-user-guides/manual-capability-profile.md`. For the full source map, see `docs/00-overview/capability-inventory-navigation.md`.

## Org Pack Foundations

Org Packs are no-code reusable organization asset packages. They are not Pal Packs, project templates, installers, marketplaces, scanners, validators, connectors, databases, or keyword routers.

Current Org Pack foundations:

| Path | Role |
| --- | --- |
| `evals/palbench/v0.5/documentation/archive/docs/09-roadmap/v0.5-local-development-scope.md` | v0.5 local development scope and boundary freeze. |
| `standards/org-pack/org-pack-standard.md` | Org Pack standard. |
| `templates/org-pack/base-org-pack/` | Minimal reusable Org Pack template. |
| `examples/org-packs/base-agentpal-org-pack/` | Public-safe Org Pack example. |
| `evals/palbench/org-pack/r97-org-pack-foundation-boundary.md` | Org Pack foundation boundary eval. |

Org Packs may recommend Pals as AI judgement inputs, but the central roster remains `workspace/organization/contacts/pals.json` and `official/pals/`. External projects remain thin-bound and do not receive `.agentpal/org-pack/` by default.

## Compatibility And Current-Reference Directories

Some root directories remain visible as current-reference surfaces while the v0.4/v0.5 structure settles. R77 moved low-risk root reference directories into central workspace, standards, or archive locations. R79 archived the R78 `capabilities/`, `runtime/`, `models/`, and `plugins/` compatibility pointers after active references moved to the new capability inventory structure.

| Directory | Current status |
| --- | --- |
| `prompts/` | Copyable runtime and maintenance prompts retained at root for compatibility. |
| `orchestration/` | Current no-code protocol surface. Standards pointers live under `standards/deep-conductor/`. |

These current-reference directories should not be copied wholesale into external user projects.

R79 archived these R78 capability inventory root pointers:

| Old root path | Current location |
| --- | --- |
| `capabilities/` | `archive/migration-from-v0.3/root-legacy/capability-inventory/root-pointers/capabilities/` |
| `runtime/` | `archive/migration-from-v0.3/root-legacy/capability-inventory/root-pointers/runtime/` |
| `models/` | `archive/migration-from-v0.3/root-legacy/capability-inventory/root-pointers/models/` |
| `plugins/` | `archive/migration-from-v0.3/root-legacy/capability-inventory/root-pointers/plugins/` |

R76 and R77 moved these old root paths out of the root:

| Old root path | Current location |
| --- | --- |
| `pals/` | `archive/migration-from-v0.3/root-legacy/pals/` |
| `contacts/` | `archive/migration-from-v0.3/root-legacy/contacts/` |
| `registry/` | `workspace/resources/registry/` |
| `projects/` active protocols | `standards/project-binding/` |
| `projects/` legacy records and old templates | `archive/migration-from-v0.3/root-legacy/projects/` |
| `imports/` | `workspace/resources/imports/` |
| `memory/` | `workspace/organization/memory/` |
| `state/` | `archive/migration-from-v0.3/root-legacy/state/` plus ignored local runtime state under `.agentpal/local/state/` |
| `reports/` | `archive/migration-from-v0.3/root-legacy/reports/` |
| `response-fingerprints/` | `workspace/resources/response-fingerprints/` |

The current Pal facts remain `official/pals/` and `workspace/organization/contacts/`.

## Routing Boundary

AgentPal does not use keyword routing. Pal ownership is judged case-by-case from the current request, central contacts, Pal assets, project context, risks, and expected deliverables.

`/pal Name` and `@Name` are explicit user mentions. They are not keyword or domain routes.

## Runtime Boundary

AgentPal is a Markdown / JSON / protocol workspace. It does not add a CLI, desktop app, web app, scanner, validator, installer, daemon, database, auto sync service, or automatic execution engine.
