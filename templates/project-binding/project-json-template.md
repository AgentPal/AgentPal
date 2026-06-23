# Project JSON Template

```json
{
  "schema": "agentpal.project.v0.1",
  "project_name": "REPLACE_WITH_EXTERNAL_PROJECT_NAME",
  "project_root": "REPLACE_WITH_EXTERNAL_PROJECT_ROOT",
  "active_project_root": "REPLACE_WITH_EXTERNAL_PROJECT_ROOT",
  "active_project_role": "user_project",
  "agentpal_enabled": true,
  "created_by": "AgentPal",
  "removable": true,
  "agentpal_workspace": "REPLACE_WITH_AGENTPAL_WORKSPACE_PATH",
  "agentpal_workspace_root": "REPLACE_WITH_AGENTPAL_WORKSPACE_PATH",
  "agentpal_workspace_role": "pal_workspace_reference",
  "default_listener": "Mira",
  "current_project_semantics": "active_project_root_only",
  "workspace_root_policy": {
    "single_active_context_required": true,
    "active_project_root_is_current_project": true,
    "agentpal_workspace_is_only_pal_source": true,
    "do_not_list_agentpal_workspace_as_project_root": true,
    "do_not_answer_project_questions_with_multiple_roots": true,
    "project_terms_mean": "active_project_root",
    "read_agentpal_workspace_only_when_user_explicitly_asks_about_agentpal": true
  },
  "available_pal_scope": "all-installed-pals",
  "pal_access_mode": "lazy",
  "project_bound_mode": true,
  "root_agents_required": true,
  "root_agents_block": {
    "begin_marker": "BEGIN AGENTPAL WORKGROUP",
    "end_marker": "END AGENTPAL WORKGROUP",
    "template": "templates/project-binding/root-agents-agentpal-block-template.md"
  },
  "block_markers": [
    "BEGIN AGENTPAL WORKGROUP",
    "END AGENTPAL WORKGROUP"
  ],
  "remove_policy": {
    "requires_confirmation": true,
    "delete_agentpal_dir": true,
    "remove_root_agents_agentpal_block_only": true,
    "write_deactivation_marker_when_root_agents_empty_or_missing": true,
    "deactivation_marker_template": "templates/project-binding/agentpal-removed-agents-template.md",
    "current_thread_loaded_context_warning_required": true,
    "recommend_new_thread_after_removal": true,
    "do_not_delete_project_source": true,
    "do_not_delete_user_agents_content": true,
    "do_not_delete_agentpal_workspace": true,
    "cleanup_registered_projects": true,
    "clear_active_project_if_matches": true,
    "archive_project_memory_by_default": true
  },
  "cleanup_targets": [
    ".agentpal/",
    "AGENTS.md AgentPal block",
    "AgentPal registered project record",
    "AgentPal active project state"
  ],
  "direct_call_enabled": true,
  "direct_call_pattern": "/pal {display_name}",
  "reply_prefix_required": true,
  "context_policy": {
    "ordinary_messages_go_to": "Mira",
    "specialist_pals_do_not_listen_by_default": true,
    "specialist_pals_need_context_packet": true,
    "project_files_read_only_until_task_requires": true,
    "specialist_tasks_must_be_delegated": true,
    "separate_pal_layer_and_execution_layer": true
  }
}
```

When copied to an external project, the containing directory should be named `.agentpal/`.

`active_project_root` is the external user project. `agentpal_workspace_root` is only a Pal source and routing reference. Current project means `active_project_root`; do not list AgentPal workspace as project root.

项目默认只指 `active_project_root`。AgentPal 工作区不是当前项目内容，只是 Pal 来源。

The binding is removable. Removal deletes `.agentpal/`, removes only the protected AgentPal block from root `AGENTS.md`, and cleans AgentPal registered project state. If root `AGENTS.md` becomes empty or did not exist, removal writes a non-workgroup deactivation marker so new Codex sessions do not continue Mira mode. It must not delete project source files or user-authored `AGENTS.md` content.

Removal does not erase rules already loaded into an existing Codex thread. The removal completion message must recommend starting a new project thread or explicitly using `Codex generic answer` in the old thread.

External project binding must also create or update the external project root `AGENTS.md` with the `BEGIN AGENTPAL WORKGROUP` / `END AGENTPAL WORKGROUP` protected block. The root block is the Codex entry point; `.agentpal/` alone is not enough.

Do not copy all Pal Packs into the external project. Default listener remains Mira, and specialist Pals do not listen or read project files unless Mira routes a task or the user calls `/pal Name`.

Project files are shared knowledge by task need only. Sensitive files, credentials, tokens, secrets, private user data, and private customer data are not shared by default.

