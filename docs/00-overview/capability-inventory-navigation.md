# Capability Inventory Navigation

Capability Inventory is AgentPal's no-code profile layer for runtime, model, reasoning, Skill, plugin, MCP, business-system, and Pal capability notes.

It is not an automatic scanner, validator, installer, sync service, or keyword router. A host Runtime may provide evidence, and AgentPal records that evidence as Markdown / JSON assets.

## Current Sources

| Source type | Path | Role |
| --- | --- | --- |
| Standards | `standards/capability-inventory/` | Reusable rules, matrices, protocols, and profile standards. |
| Current organization records | `workspace/organization/capability-inventory/` | Public-safe current organization placeholders and maintained capability notes. |
| Examples | `examples/capability-inventory/` | Synthetic example profiles and task judgement examples. |
| Templates | `templates/capability-inventory/` | Copyable JSON profile templates. |
| Historical archive | `archive/migration-from-v0.3/root-legacy/capability-inventory/` | R78/R79/R80 migration evidence and archived legacy pointers. |

## External Project Boundary

External user projects remain thin-bound. Do not copy standards, examples, templates, Pal Packs, central contacts, memory, reports, workflows, or capability inventory directories into the external project by default.

Project-specific capability findings belong under:

```text
workspace/projects/<project-id>/capability-inventory/
```

The external project should keep only binding entrypoints such as `.agentpal/project.json`, `.agentpal/AGENTPAL.md`, and protected root instruction blocks.

## Routing Boundary

Capability Inventory profiles can inform AI judgement. They must not become fixed routes.

Forbidden active behavior:

- `keyword_map`
- `domain_map`
- `role_map`
- deterministic task-domain-to-Pal routing
- automatic runtime selection without current evidence

Explicit `/pal Name` and `@Name` mentions are user intent signals, not keyword routes.

## Legacy Path Notes

R79 archived the old root `capabilities/`, `runtime/`, `models/`, and `plugins/` pointer directories under:

```text
archive/migration-from-v0.3/root-legacy/capability-inventory/root-pointers/
```

R80 renamed the old template tree from `templates/capabilities/` to `templates/capability-inventory/` and moved the old `examples/runtime/README.md` navigation into `examples/runtime-adapters/README.md`.
