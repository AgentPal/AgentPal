# Project Context Policy

In an external project-bound session:

- `active_project_root` is the external user project.
- `agentpal_workspace_root` is only a Pal source and routing reference.
- Current project means `active_project_root`.
- Do not list AgentPal workspace as project root.
- Do not treat the AgentPal workspace as current project content.
- Only read AgentPal workspace files when the user explicitly asks about AgentPal itself, Mira files, Pal configuration, or the AgentPal workspace.
- Even if Codex exposes multiple workspace roots, AgentPal must choose one active context.
- Do not answer project questions by listing both the external project and the AgentPal workspace.

外部项目是当前项目。AgentPal 工作区不是当前项目内容。项目默认只指 `active_project_root`。

当前上下文只能有一个。即使 Codex 暴露多个 workspace roots，回答“项目”问题时也不能把外部项目和 AgentPal 工作区同时列出来。

In AgentPal Workspace Mode:

- The current context is the AgentPal Workspace.
- Call it AgentPal Workspace / AgentPal 工作区.
- It is not a project.
- Do not call it "AgentPal project".
- Do not compare it with an external project as two projects.

Remove AgentPal workgroup only removes the target external project's AgentPal binding configuration. It must not delete project source or user-authored AGENTS content.

External project context should be read by task need.

Do not let specialist Pals read the whole project by default.

Context Packet should list only relevant files and needed output.

Private project facts remain in the external project's `.agentpal/`, not public AgentPal release files.

