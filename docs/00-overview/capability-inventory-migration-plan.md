# Capability Inventory Migration Plan

R77 does not bulk-move `capabilities/`, `runtime/`, `models/`, or `plugins/`. These directories still serve active documentation, examples, and evals. This plan defines the staged split for a later round.

## Current Surfaces

| current path | current role | future home |
| --- | --- | --- |
| `capabilities/README.md` | profile index and boundary note | `standards/capability-inventory/README.md` after compatibility links are ready |
| `capabilities/runtime-profiles/` | illustrative runtime profiles | `standards/capability-inventory/runtime-profiles/` or `examples/capability-inventory/runtime-profiles/` |
| `capabilities/model-profiles/` | illustrative model profiles | `standards/capability-inventory/model-profiles/` or examples |
| `capabilities/reasoning-profiles/` | reasoning-strength profile examples | `standards/capability-inventory/reasoning-profiles/` |
| `capabilities/skill-profiles/` | Skill profile examples | `standards/capability-inventory/skill-profiles/` |
| `capabilities/plugin-profiles/` | plugin capability notes | `standards/capability-inventory/plugin-profiles/` |
| `capabilities/mcp-profiles/` | MCP capability notes | `standards/capability-inventory/mcp-profiles/` |
| `capabilities/pal-profiles/` | Pal profile examples | `workspace/organization/capability-inventory/pal-profiles/` or examples |
| `runtime/`, `models/`, `plugins/` | current root reference notes | merged into the capability inventory split where appropriate |

## Target Split

- Standards: reusable schemas, profile fields, privacy rules, and judgement rules go under `standards/capability-inventory/`.
- Organization records: current organization capability inventory and public-safe central examples go under `workspace/organization/capability-inventory/`.
- Project records: project-specific capability findings go under `workspace/projects/<project-id>/capability-inventory/`.
- Examples: illustrative fake profiles go under `examples/capability-inventory/`.
- Evals and release evidence: checks stay under `evals/capability-inventory/` or `release/`.
- Archive: superseded profile notes move to `archive/migration-from-v0.3/root-legacy/`.

## Migration Rounds

1. R78: inventory all references to `capabilities/`, `runtime/`, `models/`, and `plugins/`; add compatibility pointers.
2. R78: move schema-like and standard-like content into `standards/capability-inventory/`.
3. R79: move illustrative examples into `examples/capability-inventory/` and update eval references.
4. R79: decide whether root `runtime/`, `models/`, and `plugins/` can become pointer-only or be archived.

## Boundaries

- Capability profiles are judgement inputs, not fixed routes.
- Do not introduce `keyword_map`, `domain_map`, `role_map`, deterministic semantic routing, or automatic runtime selection.
- Do not create scanners, validators, daemons, databases, or auto inventory sync.
