# Project Binding Protocol

Use this protocol when the user asks to add AgentPal to an external project.

Project means an external user project by default, not the AgentPal workspace itself.

## Goal

Project binding is thin. It points the external project to the AgentPal workspace and current core gates. It does not copy AgentPal's full rule body into the project.

## Required External Project Files

Always create or update:

- `.agentpal/project.json`
- `.agentpal/AGENTPAL.md`
- root `AGENTS.md` protected block

For Claude Code, also create or update:

- root `CLAUDE.md` protected block
- `.claude/settings.local.json`

Do not create project-local AgentPal state folders by default.

Forbidden default additions:

- `.agentpal/state/`
- `.agentpal/memory/`
- `.agentpal/reports/`
- `.agentpal/context/`
- `.agentpal/index/`
- `.agentpal/pals/`
- `.agentpal/workflows/`
- `.agentpal/evals/`

## Must Not Copy

Do not copy these into the external project binding:

- full Pal list as source of truth
- full Mira assets
- full orchestration protocols
- full docs
- examples
- evals
- release notes
- PalBench reports
- central contacts
- official Pal Packs
- workspace project records

## Core Gate Read Order

The protected root block and `.agentpal/AGENTPAL.md` must tell runtimes to read these from `agentpal_workspace_root`:

1. `core/agentpal-core-gate.md`
2. `core/first-pal-gate.md`
3. `core/simple-pal-mode-runtime-contract.md`
4. `core/deliverable-aware-task-judgement-gate.md`
5. `core/main-pal-conductor-gate.md`
6. `core/runtime-adapter-shared-contract.md`
7. `core/project-binding-thin-contract.md`
8. `core/runtime-response-gate.md`
9. `workspace/organization/contacts/pals.json`
10. `workspace/organization/contacts/PAL_CONTACTS.md`
11. `official/pals/Mira-main/PAL.md`
12. `official/pals/Mira-main/core/output-contract.md`

## Binding Metadata

`.agentpal/project.json` should store:

- schema_version: `agentpal.project_binding.v1`
- binding_version
- binding_type: `thin`
- project_name
- project_root_hint
- default_pal: `Mira`
- runtime
- agentpal_source as a structured object
- enabled_at
- updated_at
- status
- last_runtime
- enabled_runtimes
- active_project_root
- agentpal_workspace_root, when a local AgentPal workspace is available
- core_gate_paths
- pal_source_of_truth

It should not store an authoritative Pal roster.

It must state `routing_policy: ai_judgement_only` and `keyword_routing_allowed: false`.

## Runtime Notes

Codex, Claude Code, generic CLI agents, and future adapters all use the same core gates. Adapter prompts may differ only in how they locate the AgentPal workspace and what runtime-specific local settings they need.

Claude Code requires `.claude/settings.local.json` with `permissions.additionalDirectories` containing the AgentPal workspace root. This local file should be ignored by Git.

## Removal

Removing AgentPal from a project should:

- remove only the current runtime's protected AgentPal block from `AGENTS.md` or `CLAUDE.md`
- remove only the current runtime from `enabled_runtimes`
- delete `.agentpal/` only when no runtime binding remains
- remove the AgentPal workspace path from `.claude/settings.local.json` when present
- leave the AgentPal workspace untouched
- leave project source files untouched

## Verification

Verification should prove:

- the project binding is thin
- core gate files exist in the AgentPal workspace
- central contacts exist in the AgentPal workspace
- Mira entry files exist in the AgentPal workspace
- root instruction blocks point to core gates
- no stale embedded full Pal list is used as source of truth
- no full AgentPal protocols are copied into `.agentpal/`
- active mode remains Simple Pal Mode only
- no `.agentpal/memory`, `.agentpal/state`, `.agentpal/reports`, `.agentpal/context`, `.agentpal/index`, `.agentpal/pals`, `.agentpal/workflows`, or `.agentpal/evals` directories were created by default
- no keyword routing map is used
