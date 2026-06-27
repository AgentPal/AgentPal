# project.json Standard

External project binding file:

`<project>/.agentpal/project.json`

Required fields:

- `schema`
- `binding_style`
- `active_project_root`
- `agentpal_workspace_root`
- `runtime_hint`
- `ordinary_messages_go_to`
- `project_context_policy`
- `allowed_project_binding_files`
- `forbidden_default_project_binding_dirs`

The file is a pointer and policy summary. It is not a project index, memory store, state database, or Pal registry.
