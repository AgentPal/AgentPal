# R251 Fresh Install Read Order Retest

## Scope

Checked source read-order and binding entry assets after R250:

- `AGENTS.md`
- `agentpal.json`
- `core/agentpal-core-gate.md`
- `core/owner-assignment-integrity-gate.md`
- `templates/project-binding/generic-codex/.agentpal/AGENTPAL.md`
- `templates/project-binding/claude-code/.agentpal/AGENTPAL.md`
- `integrations/claude-code/agentpal-project-binder/templates/CLAUDE.agentpal-block.md`
- `shared/agentpal_binding_common.py`
- `docs/user-tests/v0.6/`

## Observed Current Read Order

Current core gate read order in `core/agentpal-core-gate.md` includes:

1. `core/agentpal-core-gate.md`
2. `core/first-pal-gate.md`
3. `core/deliverable-aware-task-judgement-gate.md`
4. `core/main-pal-conductor-gate.md`
5. `core/owner-assignment-integrity-gate.md`
6. `core/pal-asset-preflight-protocol.md`
7. `core/team-asset-preflight-protocol.md`
8. `orchestration/workflow-execution-contract-protocol.md`
9. `orchestration/workflow-closure-gate-protocol.md`
10. `core/runtime-adapter-shared-contract.md`
11. central contacts
12. Mira entry assets

## Required R251 Anchors

| Anchor | Status | Evidence |
| --- | --- | --- |
| Team Pack first discovery | pass | `AGENTS.md`, core gate, binding templates |
| Pal / Team Asset Preflight | pass | core gate read order and binding templates |
| Owner Assignment Integrity | pass | core gate and `core/owner-assignment-integrity-gate.md` |
| Team Role Assignment Gate semantics | pass | Owner Assignment Integrity: team label anchor, open role gap, no fake participant |
| Workflow Execution Contract | pass | core gate, binding templates, user tests |
| Closure Gate | pass | core gate, binding templates, user tests |
| DeepConductor for composite tasks | pass_with_environment_notes | no-code protocol only, host runtime evidence required for stronger claim |
| PalSmith for durable Pal / Team creation / repair | pass | core gate and binding templates |

## Result

fresh_install_read_order_retest: pass_with_environment_notes

Notes: current source entries no longer point fresh binding reads to legacy Simple Pal Mode as the active runtime contract. This run did not prove a separate host session loaded these files.
