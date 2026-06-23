# AgentPal Project Binding

This folder is a template for an external project `.agentpal/` binding.

When copied into a real external project, rename this folder to `.agentpal/`.

Ordinary messages go to Mira. Specialist Pals do not listen by default.

Project means the external project that owns this `.agentpal/` folder.

`active_project_root` is the external user project directory. `agentpal_workspace_root` is only a Pal source and routing reference.

Current project means `active_project_root`. Do not list AgentPal workspace as project root. Do not treat the AgentPal workspace as part of this project.

外部项目是当前项目。AgentPal 工作区不是当前项目内容，只是 Pal 来源。用户说“项目”“当前项目”“读取项目目录”时，项目默认只指 `active_project_root`。

Replies should include the speaking Pal prefix, such as `Mira：`, `Atlas：`, or `Rhea：`.

Owned tasks may be delegated through Context Packet after case-by-case AI routing judgement. No hard-coded semantic routing. Pal capability reference is not a route map.

The external project root `AGENTS.md` must include the protected `BEGIN AGENTPAL WORKGROUP` / `END AGENTPAL WORKGROUP` block. Codex sessions in this external project should read root `AGENTS.md`, then `.agentpal/INIT_AGENTPAL_PROJECT_PROMPT.md`, `.agentpal/project.json`, `.agentpal/AGENTPAL.md`, and `.agentpal/PAL_GROUP.md`.

If a session has not loaded AgentPal rules yet, read `.agentpal/INIT_AGENTPAL_PROJECT_PROMPT.md` and enter AgentPal project-bound mode.

Do not copy all AgentPal Pals into this project.

This binding is removable. Removing the workgroup should delete `.agentpal/` and remove only the protected AgentPal block from root `AGENTS.md`; do not delete project source or user-authored AGENTS content.

Do not say two project roots. Do not answer ordinary project questions by saying there are two project roots. If Codex exposes multiple workspace roots, use `.agentpal/project.json` to identify `active_project_root` first.

当前上下文只能有一个。即使 Codex 暴露多个 workspace roots，回答“项目”问题时不能把外部项目和 AgentPal 工作区同时列出来。

Capability descriptions for Atlas, Rhea, Quinn, Nova, Vega, Morgan, and Harper are non-binding examples, not route rules.

Use project files as shared knowledge only when a task requires them. Sensitive files, credentials, tokens, secrets, private customer data, and unrelated private material are not shared by default.

When real file, command, system, or tool execution occurs, report Pal layer and Execution layer separately. If Codex performs the action, call it `当前 Codex 执行层`.

