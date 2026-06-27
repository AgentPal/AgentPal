# Project JSON Template

```json
{
  "schema": "agentpal.external_project_binding.v0.4",
  "binding_version": "0.4-foundation",
  "binding_created_at": "REPLACE_WITH_ISO_TIMESTAMP",
  "project_id": "REPLACE_WITH_PROJECT_ID",
  "project_name": "REPLACE_WITH_EXTERNAL_PROJECT_NAME",
  "active_project_root": "REPLACE_WITH_EXTERNAL_PROJECT_ROOT",
  "active_project_role": "user_project",
  "agentpal_workspace_root": "REPLACE_WITH_AGENTPAL_WORKSPACE_PATH",
  "agentpal_workspace_role": "pal_workspace_reference",
  "agentpal_project_record": "workspace/projects/REPLACE_WITH_PROJECT_ID",
  "runtime_hint": "REPLACE_WITH_RUNTIME_HINT",
  "active_mode": "simple-pal-mode-only",
  "agentpal_enabled": true,
  "project_bound_mode": true,
  "binding_mode": "thin",
  "binding_style": "thin-binding",
  "read_core_from_agentpal_workspace": true,
  "core_gate_paths": [
    "core/agentpal-core-gate.md",
    "core/first-pal-gate.md",
    "core/simple-pal-mode-runtime-contract.md",
    "core/deliverable-aware-task-judgement-gate.md",
    "core/main-pal-conductor-gate.md",
    "core/runtime-adapter-shared-contract.md",
    "core/project-binding-thin-contract.md",
    "core/runtime-response-gate.md"
  ],
  "pal_source_of_truth": [
    "workspace/organization/contacts/pals.json",
    "workspace/organization/contacts/PAL_CONTACTS.md"
  ],
  "central_pal_contacts": [
    "workspace/organization/contacts/pals.json",
    "workspace/organization/contacts/PAL_CONTACTS.md",
    "workspace/organization/contacts/aliases.json"
  ],
  "central_contacts_are_not_copied": true,
  "project_knowledge_policy": {
    "read_current_project_materials_from": "active_project_root",
    "write_source_map_to": "agentpal_project_record/source-map",
    "write_derived_knowledge_to": "agentpal_project_record/derived-knowledge",
    "write_project_memory_to": "agentpal_project_record/memory",
    "write_tasks_and_reports_to": "agentpal_project_record/tasks and agentpal_project_record/reports",
    "write_governance_to": "agentpal_project_record/governance",
    "write_capability_inventory_to": "agentpal_project_record/capability-inventory",
    "do_not_create_thick_agentpal_dirs_in_external_project": true
  },
  "routing_policy": "ai_judgement_only",
  "keyword_routing_allowed": false,
  "default_main_pal": {
    "id": "mira-main",
    "display_name": "Mira",
    "paths": [
      "official/pals/Mira-main/PAL.md",
      "official/pals/Mira-main/core/output-contract.md"
    ]
  },
  "forbidden_default_project_binding_dirs": [
    ".agentpal/memory",
    ".agentpal/state",
    ".agentpal/reports",
    ".agentpal/context",
    ".agentpal/index",
    ".agentpal/pals",
    ".agentpal/workflows",
    ".agentpal/evals"
  ],
  "root_instruction_blocks": {
    "begin_marker": "<!-- BEGIN AGENTPAL WORKGROUP -->",
    "end_marker": "<!-- END AGENTPAL WORKGROUP -->"
  },
  "claude_code_binding": {
    "project_instruction_file": "CLAUDE.md",
    "local_settings_file": ".claude/settings.local.json",
    "additional_directories_setting": "permissions.additionalDirectories"
  },
  "remove_policy": {
    "delete_agentpal_dir": true,
    "remove_root_instruction_blocks_only": true,
    "remove_claude_additional_directory_entry": true,
    "do_not_delete_agentpal_workspace": true,
    "do_not_delete_project_source": true
  }
}
```

This file is binding metadata only. It is not a copied Pal roster or a copied protocol bundle.

Pal source of truth remains in the AgentPal workspace:

- `workspace/organization/contacts/pals.json`
- `workspace/organization/contacts/PAL_CONTACTS.md`

Project record source of truth remains in the AgentPal workspace:

- `workspace/projects/<project-id>/`

Runtime adapters should read current core gates from `agentpal_workspace_root`.
