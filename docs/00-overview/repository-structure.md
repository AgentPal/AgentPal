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

## Compatibility Directories

Some root directories remain visible as compatibility pointers or current-reference surfaces while the v0.4/v0.5 structure settles:

| Directory | Current status |
| --- | --- |
| `pals/` | Compatibility pointer. Official Pal Packs are under `official/pals/`. |
| `contacts/` | Legacy compatibility contacts. Current source of truth is `workspace/organization/contacts/`. |
| `registry/` | Legacy and selected compatibility indexes. Current Pal discovery uses central contacts. |
| `projects/` | Compatibility project-binding protocols and older workgroup pointers. Current templates are under `templates/project-binding/`. |
| `prompts/` | Copyable runtime and maintenance prompts retained at root for compatibility. |
| `capabilities/` | Current capability profile notes. Capability standards are under `standards/capability-inventory/`; project-specific capability records belong under central project records. |
| `orchestration/` | Current no-code protocol surface. Standards pointers live under `standards/deep-conductor/`. |
| `memory/`, `state/`, `reports/` | Public-safe placeholders only. Private runtime content must not be committed. |

These compatibility directories should not be copied wholesale into external user projects.

## Routing Boundary

AgentPal does not use keyword routing. Pal ownership is judged case-by-case from the current request, central contacts, Pal assets, project context, risks, and expected deliverables.

`/pal Name` and `@Name` are explicit user mentions. They are not keyword or domain routes.

## Runtime Boundary

AgentPal is a Markdown / JSON / protocol workspace. It does not add a CLI, desktop app, web app, scanner, validator, installer, daemon, database, auto sync service, or automatic execution engine.
