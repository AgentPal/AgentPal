# Project Workgroup

AgentPal can be bound to an external user project through a `.agentpal/` folder and a root `AGENTS.md` AgentPal workgroup block.

Project means external user project by default, not the AgentPal workspace itself.

Codex project list first. `list_projects` first if the current environment provides it. Workspace roots first. When the user asks Mira to add AgentPal to a named project, Mira must first inspect the Codex current project list / `list_projects` / visible workspace project list before asking for a manual path.

当用户说“把 AgentPal 工作组加入某某项目”时，Mira 必须先查 Codex 当前项目列表或工作区根目录。只有无法确定目标项目时，才向用户索要路径。

Ordinary project messages go to Mira. Specialist Pals do not listen by default.

Replies should start with the speaking Pal name, such as `Mira：`.

The external project receives `.agentpal/` binding files and an AgentPal block in the external project root `AGENTS.md`. Do not copy all Pal Packs into the external project, and do not treat the AgentPal workspace itself as the target project unless the user explicitly says they are developing AgentPal itself.

Creating `.agentpal/` alone is not enough for Codex project takeover because a new Codex session may not read hidden project binding files automatically. The root `AGENTS.md` block must tell Codex to read `.agentpal/project.json`, `.agentpal/AGENTPAL.md`, and `.agentpal/PAL_GROUP.md`, then default ordinary messages to Mira.

In an external project-bound session, `active_project_root` is the external user project. `agentpal_workspace_root` is only a Pal source and routing reference. Current project means `active_project_root`; do not list AgentPal workspace as project root.

外部项目是当前项目。AgentPal 工作区不是当前项目内容。用户说“项目”“当前项目”“读取项目目录”时，只回答外部项目，不要把 AgentPal 工作区也列出来。

Even if Codex exposes multiple workspace roots, AgentPal must choose one active context. Do not answer project questions by listing both the external project and the AgentPal workspace.

即使 Codex 暴露多个 workspace roots，AgentPal 也必须选择一个当前上下文。回答“项目”问题时不能把外部项目和 AgentPal 工作区同时列出来。

## Remove AgentPal Workgroup

Users can ask Mira to remove the AgentPal workgroup from an external project.

Removal must:

- confirm the target project first
- delete the target `.agentpal/`
- remove only the `BEGIN AGENTPAL WORKGROUP` / `END AGENTPAL WORKGROUP` block from root `AGENTS.md`
- if root `AGENTS.md` becomes empty or did not exist, leave the non-workgroup deactivation marker from `templates/project-binding/agentpal-removed-agents-template.md`
- clean AgentPal registered project state
- avoid deleting project source, project docs, `.git`, package files, AgentPal Workspace, AgentPal `pals/`, other projects' `.agentpal/`, or user-authored AGENTS content

Removal does not erase instructions already loaded into an existing Codex thread. After removal, the completion message must tell the user to start a new project thread, or explicitly request `Codex generic answer` in the old thread. The removed project must not continue ordinary replies as Mira.

