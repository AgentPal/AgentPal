# project.json Standard

External project binding file:

`<project>/.agentpal/project.json`

Canonical protocol:

- `docs/04-runtime-guides/project-thin-binding.md`

Required fields for new writes:

- `schema_version`
- `binding_version`
- `binding_type`
- `project_name`
- `project_root_hint`
- `default_pal`
- `runtime`
- `agentpal_source`
- `enabled_at`
- `updated_at`
- `status`

Recommended multi-runtime fields:

- `last_runtime`
- `enabled_runtimes`

`agentpal_source` should carry the central AgentPal source information, such as source type, local workspace path when available, or GitHub source URL. Adapters may keep compatibility aliases such as `agentpal_source_type`, `agentpal_source_value`, `agentpal_source_detail`, and `agentpal_workspace_root` when older prompts or runtimes still read them.

Legacy bindings may still contain `schema`, `active_project_root`, `agentpal_workspace_root`, `runtime_hint`, `ordinary_messages_go_to`, `project_context_policy`, `allowed_project_binding_files`, and `forbidden_default_project_binding_dirs`. Adapters may read those fields during migration or repair, but new writes should follow the canonical protocol.

The file is a pointer and policy summary. It is not a project index, memory store, state database, or Pal registry.
