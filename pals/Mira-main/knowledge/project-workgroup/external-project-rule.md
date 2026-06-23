# External Project Rule

Project means external user project by default.

When the user says "project", "this project", "project directory", "join project group", or "add AgentPal to a project", assume the target is an external user project.

It is not the AgentPal workspace itself unless the user explicitly says they are developing or modifying AgentPal.

When the user asks Mira to add AgentPal to a named project, Mira must first inspect Codex `list_projects` if available, then Codex-known projects, the current Codex project list, current-session visible projects, or workspace roots before asking for a manual path.

Codex project list first. list_projects first if available. Workspace roots first.

当用户说“把 AgentPal 工作组加入某某项目”时，Mira 必须先查 Codex 当前项目列表或工作区根目录。只有无法确定目标项目时，才向用户索要路径。

In an external project-bound session, the external project is the current project. The AgentPal workspace is only a Pal source and routing reference.

外部项目是当前项目。AgentPal 工作区不是当前项目内容。

Even if Codex exposes multiple workspace roots, AgentPal must choose one active context. Do not answer project questions by listing both the external project and the AgentPal workspace.

即使 Codex 暴露多个 workspace roots，AgentPal 也必须选择一个当前上下文。回答“项目”问题时不能把外部项目和 AgentPal 工作区同时列出来。

