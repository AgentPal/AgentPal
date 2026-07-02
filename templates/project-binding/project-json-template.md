# Project JSON Template

Use this template for new AgentPal thin project bindings.

```json
{
  "schema_version": "agentpal.project_binding.v1",
  "binding_version": "1.0",
  "binding_type": "thin",
  "project_name": "REPLACE_WITH_EXTERNAL_PROJECT_NAME",
  "project_root_hint": "REPLACE_WITH_EXTERNAL_PROJECT_ROOT",
  "default_pal": "Mira",
  "runtime": "REPLACE_WITH_RUNTIME",
  "agentpal_source": {
    "type": "central_path",
    "value": "REPLACE_WITH_AGENTPAL_WORKSPACE_PATH_OR_SOURCE_URL",
    "workspace_root": "REPLACE_WITH_AGENTPAL_WORKSPACE_PATH_WHEN_LOCAL"
  },
  "enabled_at": "REPLACE_WITH_ISO_TIMESTAMP",
  "updated_at": "REPLACE_WITH_ISO_TIMESTAMP",
  "status": "enabled",
  "last_runtime": "REPLACE_WITH_RUNTIME",
  "enabled_runtimes": [
    "REPLACE_WITH_RUNTIME"
  ],
  "active_project_root": "REPLACE_WITH_EXTERNAL_PROJECT_ROOT",
  "agentpal_workspace_root": "REPLACE_WITH_AGENTPAL_WORKSPACE_PATH_WHEN_LOCAL",
  "agentpal_project_record": "workspace/projects/REPLACE_WITH_PROJECT_ID",
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
  "routing_policy": "ai_judgement_only",
  "keyword_routing_allowed": false,
  "forbidden_default_project_binding_dirs": [
    ".agentpal/memory",
    ".agentpal/state",
    ".agentpal/reports",
    ".agentpal/context",
    ".agentpal/index",
    ".agentpal/pals",
    ".agentpal/workflows",
    ".agentpal/evals",
    ".agentpal/capability-inventory",
    ".agentpal/business-systems",
    ".agentpal/reviews",
    ".agentpal/evidence",
    ".agentpal/replay",
    ".agentpal/rollback",
    ".agentpal/verification",
    ".agentpal/audit-trail",
    ".agentpal/governance-decisions",
    ".agentpal/change-ledger",
    ".agentpal/change-review"
  ]
}
```

Canonical runtime-qualified protected block markers are defined in [`docs/04-runtime-guides/project-thin-binding.md`](../../docs/04-runtime-guides/project-thin-binding.md).

This file is binding metadata only. It is not a copied Pal roster or a copied protocol bundle.

Pal source of truth remains in the AgentPal workspace:

- `workspace/organization/contacts/pals.json`
- `workspace/organization/contacts/PAL_CONTACTS.md`

Project record source of truth remains in the AgentPal workspace:

- `workspace/projects/<project-id>/`

Runtime adapters should read current core gates from `agentpal_workspace_root` when a local AgentPal workspace is available.
