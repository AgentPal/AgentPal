# Orchestration Migration Plan

R77 leaves root `orchestration/` in place because it is an active protocol surface referenced by runtime gates, docs, templates, examples, and evals.

## Target Split

| content type | future home | examples |
| --- | --- | --- |
| current standards and boundary protocols | `standards/deep-conductor/` or dedicated standards subdirectories | routing judgement, no-code execution boundary, memory boundary |
| official reusable workflows | `official/workflows/` | stable no-code workflow definitions approved for bundled AgentPal |
| task/package templates | `templates/orchestration/` | Context Budget Plan, Runtime Skill-aware package, verifier packet |
| examples | `examples/orchestration/` | successful package examples and failure examples |
| evals | `evals/orchestration/` and PalBench suites | regression cases and qualitative checks |
| historical or superseded protocols | `archive/migration-from-v0.3/root-legacy/orchestration/` | replaced drafts or compatibility-only files |

## Migration Rounds

1. R79: classify each `orchestration/*.md` file as active gate, standard, workflow, template, example, eval dependency, or archive.
2. R79: move only non-gate, template-shaped files after all references are updated.
3. R80: move standard-shaped protocols to `standards/` with compatibility links.
4. R80: keep root `orchestration/` for any protocol still read by core gates or project bindings.

## Non-Migration In R77

R77 does not move `orchestration/` because a broken path here would affect runtime response gates, project-bound mode, Context Packet handling, Deep Conductor no-code methodology, and release regression docs.

## Boundaries

- Deep Conductor remains no-code protocol, not automatic runtime execution.
- Owner + Verifier and Parallel Independent Review remain staged no-code workflows, not background multi-agent execution.
- Runtime Skill-aware packages require current host-runtime availability evidence before use.
