# AgentPal Project Binding

This external project is connected to AgentPal by thin binding.

This folder does not contain the AgentPal rule body, Pal Packs, full protocols, release docs, examples, or evals.

## How To Load AgentPal

1. Read `.agentpal/project.json`.
2. Resolve `agentpal_workspace_root`.
3. Read the current core gates from the AgentPal workspace root:
   - `core/agentpal-core-gate.md`
   - `core/first-pal-gate.md`
   - `core/simple-pal-mode-runtime-contract.md`
   - `core/deliverable-aware-task-judgement-gate.md`
   - `core/main-pal-conductor-gate.md`
   - `core/runtime-adapter-shared-contract.md`
   - `core/project-binding-thin-contract.md`
   - `core/runtime-response-gate.md`
4. Read Pal source of truth from the AgentPal workspace:
   - `workspace/organization/contacts/pals.json`
   - `workspace/organization/contacts/PAL_CONTACTS.md`
5. Read Mira entry assets from the AgentPal workspace:
   - `official/pals/Mira-main/PAL.md`
   - `official/pals/Mira-main/core/output-contract.md`

## Boundary

The active project is this external project directory.

The AgentPal workspace is only a Pal source and routing reference. Do not treat it as part of this project.

If the AgentPal framework updates its core gates, this project should inherit the update by reading `agentpal_workspace_root`; do not paste a full rule copy into this folder.

Project memory, source maps, derived knowledge, task records, reports, governance records, and capability inventory belong in the central `agentpal_project_record` under the AgentPal workspace, not in this project-local `.agentpal/` folder.

## Thin Binding Cleanliness

Do not create `.agentpal/memory`, `.agentpal/state`, `.agentpal/reports`, `.agentpal/context`, `.agentpal/index`, `.agentpal/pals`, `.agentpal/workflows`, or `.agentpal/evals` by default.

Owner selection is AI judgement only. Do not use keyword routing, `keyword_map`, `domain_map`, or `role_map`.
