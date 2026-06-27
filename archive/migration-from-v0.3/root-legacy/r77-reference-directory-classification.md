# R77 Reference Directory Classification

R77 performs the second root-noise reduction pass after R76. It migrates low-risk public placeholder and compatibility directories, and records plans for high-risk active protocol surfaces without bulk-moving them.

## Low-Risk Inventory

| old_path | files_before | tracked_before | ignored_private_before | README_before | reference_hits_before | risk_level | classification | target_path | action_this_round | kept_at_root_after_r77 | reason | future_round |
| --- | ---: | ---: | ---: | --- | ---: | --- | --- | --- | --- | --- | --- | --- |
| `projects/` | 9 | 9 | 0 | yes | 111 | low | split legacy and active project-binding material | `standards/project-binding/`, `archive/migration-from-v0.3/root-legacy/projects/` | active protocols moved to standards; legacy records/templates archived | no | Current thin binding source is `templates/project-binding/`; legacy registrations are not current truth. | R78 may remove empty filesystem residue and finish archive wording. |
| `imports/` | 7 | 7 | 0 | yes | 22 | low | public-safe import placeholders | `workspace/resources/imports/` | moved | no | Imports are shared workspace resources, not root-level task context. | R78 may add resource-review examples if needed. |
| `memory/` | 10 | 10 | 0 | yes | 123 | low | public-safe organization memory placeholders and examples | `workspace/organization/memory/` | moved | no | Organization memory belongs under the central workspace; private memory remains ignored. | R78 may split project-memory examples further if needed. |
| `state/` | 6 | 1 | 5 | yes | 74 | low | public-safe placeholder plus ignored runtime state | `archive/migration-from-v0.3/root-legacy/state/`, `.agentpal/local/state/` | public README archived; ignored runtime state moved locally | no | Runtime state is not public release content. | R78 may add `workspace/state/` only if a public state standard needs it. |
| `reports/` | 4 | 4 | 0 | yes | 79 | low | legacy public-safe report placeholders | `archive/migration-from-v0.3/root-legacy/reports/` | moved | no | Current project reports belong in central project records or release/eval evidence paths, not root. | R78 may add report templates under `workspace/projects/_template/reports/` only when needed. |
| `response-fingerprints/` | 9 | 9 | 0 | yes | 38 | low | reusable Pal response fingerprint resource | `workspace/resources/response-fingerprints/` | moved | no | Fingerprints are shared workspace resources and selected validation inputs. | R78 may decide whether fingerprints become Pal-local core assets. |

## High-Risk Planning Only

| old_path | risk_level | classification | target_path | action_this_round | kept_at_root_after_r77 | reason | future_round |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `capabilities/` | high | active capability profile examples | `standards/capability-inventory/`, `workspace/organization/capability-inventory/`, examples/evals | plan only | yes | Many docs and evals still reference current profile paths. | R78 staged capability inventory migration. |
| `runtime/` | high | active runtime-awareness notes | `standards/capability-inventory/`, `examples/runtime-adapters/`, release evidence | plan only | yes | Runtime references affect adapter and capability docs. | R78/R79 staged profile split. |
| `models/` | high | active model profile notes | `standards/capability-inventory/`, examples/evals | plan only | yes | Model references affect prompt shaping and capability docs. | R78/R79 staged profile split. |
| `plugins/` | high | active plugin profile notes | `standards/capability-inventory/`, examples/evals | plan only | yes | Plugin references affect Runtime Skill and capability docs. | R78/R79 staged profile split. |
| `orchestration/` | high | active no-code protocol surface | `standards/deep-conductor/`, `official/workflows/`, `templates/orchestration/`, examples/evals | plan only | yes | Core runtime gates and docs directly reference orchestration protocols. | R79 staged protocol split. |
| `prompts/` | medium | active copyable runtime and maintenance prompts | root `prompts/`, `templates/prompts/`, archive | plan only | yes | Runtime setup docs still point to root prompts as copyable entry assets. | R79 staged prompt family cleanup. |
| `core/` | high | active initialization gates | no move this round | checked only | yes | Root core gates are active bootstrap truth for project bindings. | Revisit only after a dedicated adapter compatibility plan. |

## Boundary Notes

- R77 did not create CLI, app, scanner, validator, daemon, database, auto sync, auto execution, tag, Release, or remote operation.
- External projects remain thin-bound. They should receive `.agentpal/project.json`, `.agentpal/AGENTPAL.md`, protected instruction blocks, and Claude Code local settings only when needed.
- `keyword_map`, `domain_map`, and `role_map` remain forbidden as active routing behavior.
