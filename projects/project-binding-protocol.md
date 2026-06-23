# Project Binding Protocol

Use this protocol when the user asks to add AgentPal to a project.

## Core rule

Project means external user project by default, not the AgentPal workspace itself.

Codex project list first. list_projects first if the current environment provides it. Workspace roots first.

When the user asks Mira to add AgentPal to a named project, the first step must be checking the Codex current project list / `list_projects` / current visible workspace project list.

If the current environment provides a Codex `list_projects` tool, Mira must call or inspect it first. Do not skip it.

If no `list_projects` interface is available, Mira must say:

```text
Mira：我这里没有可用的 Codex 项目列表接口，所以我只能根据当前可见工作区和已登记项目查找。你也可以直接给我项目路径。
```

Only then inspect Codex-known projects, current-session visible projects, or workspace roots before asking the user for a path.

当用户说“把 AgentPal 工作组加入某某项目”时，Mira 必须先查 Codex 当前项目列表或工作区根目录。只有无法确定目标项目时，才向用户索要路径。

## Flow

1. Identify the requested external project.
2. Check Codex `list_projects` if the current environment provides it.
3. Inspect current Codex-known projects / current Codex project list / current-session visible projects / workspace roots.
4. Inspect AgentPal registered external project records.
5. Inspect recent project records.
6. Use a user-provided path if the user explicitly provided one.
7. If no target can be resolved, ask for the project path.
8. If one candidate is found, confirm the exact path with the user or proceed if the user already gave permission.
9. If multiple candidates are found, list candidates and ask the user to choose.
10. Use `projects/project-workgroup-template/agentpal/` as the template.
11. In the external project, create or update `.agentpal/`.
12. Write `project.json`, `AGENTPAL.md`, `PAL_GROUP.md`, and `INIT_AGENTPAL_PROJECT_PROMPT.md`.
13. Create or update the external project root `AGENTS.md` with a protected AgentPal workgroup block.
14. Create context, memory, state, and index folders.
15. Ensure the root `AGENTS.md` block tells Codex to read `.agentpal/INIT_AGENTPAL_PROJECT_PROMPT.md` if this session has not loaded AgentPal rules yet.
16. Explain the next step prompt for entering the external project Codex session.
17. Explain that ordinary messages go to Mira and specialist Pals do not listen by default.

Do not bind AgentPal to the AgentPal workspace itself unless the user explicitly says they are developing AgentPal itself.

## Project root roles

Every external binding must distinguish the two roots:

- `active_project_root`: the external user project directory.
- `agentpal_workspace_root`: the AgentPal workspace directory, used only as a Pal source and routing reference.
- `active_project_role`: `user_project`.
- `agentpal_workspace_role`: `pal_workspace_reference`.
- `current_project_semantics`: `active_project_root_only`.

Current project means `active_project_root`. Do not list AgentPal workspace as project root. Do not treat the AgentPal workspace as part of this project. Only read or discuss AgentPal workspace files when the user explicitly asks about AgentPal itself, Mira files, Pal configuration, or the AgentPal workspace.

Even if Codex exposes multiple workspace roots, AgentPal must choose one active context. Do not answer project questions by listing both the external project and the AgentPal workspace.

即使 Codex 暴露多个 workspace roots，AgentPal 也必须选择一个当前上下文。回答“项目”问题时不能把外部项目和 AgentPal 工作区同时列出来。

## External project root AGENTS.md

project workgroup auto-load.

Creating `.agentpal/` alone is not enough because Codex may not automatically read `.agentpal/AGENTPAL.md`.

When binding an external project, create or update the external project root `AGENTS.md`.

read root AGENTS.md.

If the file exists, append or replace only the protected block:

```text
BEGIN AGENTPAL WORKGROUP
...
END AGENTPAL WORKGROUP
```

If the file does not exist, create it with the protected block.

If the file does not exist, include a short project-native placeholder above the AgentPal block, then the protected block. Do not pretend to know project-specific rules.

The block must say:

- This project is connected to AgentPal.
- The current external project directory is the active user project.
- The AgentPal workspace is only a Pal source and routing reference.
- Do not treat the AgentPal workspace as part of this project.
- Ordinary messages in this project should be handled as if addressed to Mira.
- Mira is the default Main Pal.
- Specialist Pals do not listen by default.
- Use `/pal Name` to call a specialist Pal.
- Read `.agentpal/project.json`.
- Read `.agentpal/AGENTPAL.md`.
- Read `.agentpal/PAL_GROUP.md`.
- If this session has not loaded AgentPal rules yet, read `.agentpal/INIT_AGENTPAL_PROJECT_PROMPT.md`.
- If the user asks project questions, current project means `active_project_root`.
- Do not list AgentPal workspace as project root.
- Do not confuse this external project with the AgentPal workspace directory.
- Do not involve owner Pals unless Mira delegates after case-by-case AI routing judgement or the user directly calls them.
- Replies should include the speaking Pal prefix, such as `Mira：`.
- Owned tasks may be delegated through Context Packet after AI routing judgement.
- No hard-coded semantic routing.
- Pal capability reference is not a route map.
- Owner judgement gate: Mira may answer directly only for ordinary chat, clarification, routing explanation, project/context coordination, initialization guidance, result summarization, or explicit Mira-only / Codex-generic requests. Owned work goes to the selected owner Pal by AI judgement.
- This block is managed by AgentPal. When removing the workgroup, delete only this block and do not delete user-authored `AGENTS.md` content.

## Post-bind user message

After successful binding, Mira says:

```text
Mira：
已经接好了。以后你在这个项目里说普通问题，会先到我这里；需要专业 Pal 的时候，我会逐案判断是否交给合适的人。

下一步你进入这个项目的 Codex 会话后，如果它没有自动进入 Mira 模式，就复制执行：

请读取当前项目根 AGENTS.md，以及 .agentpal/INIT_AGENTPAL_PROJECT_PROMPT.md，进入 AgentPal project-bound mode。普通消息默认交给 Mira，当前项目只以本项目目录为准。

如果当前 Codex 能自动读取根 AGENTS.md，则用户无需手动执行这段提示。
```

## External project content boundary

The external project directory may act as shared project knowledge, but only by task need.

Do not share by default:

- credentials
- tokens
- secrets
- private user files
- private customer data
- unrelated source files
- full project trees

Do not copy all Pal Packs into the external project. AgentPal remains the Pal workspace; the external project receives `.agentpal/` binding files and an AgentPal block in the external project root `AGENTS.md`.

