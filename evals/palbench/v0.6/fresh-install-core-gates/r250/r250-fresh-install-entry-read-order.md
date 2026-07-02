# R250 Fresh Install Entry Read Order

## Result

Fresh install and project binding entry points now point to the current v0.6 core gates instead of the legacy simple-mode contract.

## Updated Read Order

Current core gate order used by root workspace and binding templates:

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
11. `core/project-binding-thin-contract.md`
12. `core/runtime-response-gate.md`

## Entry Files Updated

- `AGENTS.md`
- `agentpal.json`
- `core/agentpal-core-gate.md`
- `core/README.md`
- `core/runtime-response-gate.md`
- `core/project-binding-thin-contract.md`
- `templates/project-binding/project-json-template.md`
- `templates/project-binding/generic-codex/.agentpal/project.json`
- `templates/project-binding/claude-code/.agentpal/project.json`
- `templates/project-binding/root-agents-agentpal-block-template.md`
- `shared/agentpal_binding_common.py`
- `integrations/claude-code/agentpal-project-binder/shared/agentpal_binding_common.py`
- `integrations/claude-code/agentpal-project-binder/templates/.agentpal/project.json`

## Legacy Contract Handling

`core/simple-pal-mode-runtime-contract.md` is now marked as a legacy compatibility reference and is no longer listed in current fresh-install read order.
