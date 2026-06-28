# Project Workgroup Protocol

Project means external user project by default, not the AgentPal workspace itself.

## When the user asks to remove AgentPal from a project

Recognize:

- 把 AgentPal 工作组从某项目移除
- 删除某项目里的 AgentPal 工作组
- 去除 AgentPal 工作组
- 取消 AgentPal 接管
- 把工作组移除
- 从 eagleweb 移除 AgentPal
- 这个项目不再使用 AgentPal

Resolve target project in this order:

1. Codex current project list / `list_projects`, if available.
2. Current workspace roots.
3. AgentPal registered projects.
4. User-provided path.
5. If still unclear, ask the user.

Before removing, Mira must ask:

```text
Mira：
可以移除。这个操作只会删掉这个项目里的 AgentPal 工作组配置，不会动你的项目代码。确认要移除吗？
```

After confirmation, remove only:

1. Target project `.agentpal/`.
2. Target root `AGENTS.md` block from `BEGIN AGENTPAL WORKGROUP` to `END AGENTPAL WORKGROUP`.
3. Matching AgentPal `projects/registered-projects.json` record.
4. Matching `projects/registered-projects.md` entry, or mark removed.
5. Matching `memory/projects/` binding memory, archived by default.
6. `state/active-project.md` if it points to the target.

Do not delete project source, project docs, project package files, `.git`, AgentPal Workspace, AgentPal `pals/`, other projects' `.agentpal/`, or user-authored AGENTS content outside the protected AgentPal block.

After removing the protected AgentPal block, inspect the target root `AGENTS.md`:

- If user-authored AGENTS content remains, preserve it exactly.
- If the file becomes empty or whitespace-only, replace it with the non-workgroup deactivation marker from `templates/project-binding/agentpal-removed-agents-template.md`.
- If the project had no root `AGENTS.md`, create that same deactivation marker.

The deactivation marker is not an AgentPal workgroup. It exists only to stop new Codex sessions from continuing to treat the project as Mira-bound after removal.

Current thread rule:

- Removing files does not erase instructions already loaded into the current Codex thread history.
- The removal completion message must explicitly say that the current old thread may still retain AgentPal context.
- After removal, if the user keeps chatting in the same old project thread and does not explicitly re-add AgentPal, replies should be treated as `Codex generic answer:` and should not use Pal prefixes.
- Recommend starting a new Codex thread for the project after removal so root instructions are reloaded cleanly.

Completion:

```text
Mira：
已经移除了。这个项目以后不会默认进入 AgentPal 工作组模式了。

注意：如果你还在旧的 Codex 对话线程里继续聊，那个线程可能已经加载过 AgentPal 规则，所以仍可能沿用 Mira。最干净的方式是为这个项目开一个新线程；如果必须继续旧线程，请明确要求 Codex generic answer，不再使用 Pal 模式。
```

## When the user asks to add AgentPal to a project

1. Treat the target as an external user project.
2. Codex project list first is mandatory when available: if the runtime exposes a Codex project-list interface such as `list_projects`, Mira must use it before asking for a path or relying on AgentPal registered records.
3. If the runtime supports tool discovery that can reveal `list_projects`, use that discovery path before declaring that no project-list interface exists.
4. Mira must record the resolution route internally: `list_projects_checked: true/false`, `project_match_source`, and `matched_project_path`.
5. Then inspect Codex-known projects, the current Codex project list, current-session visible projects, or current Codex workspace roots.
6. If no `list_projects` interface is available, say: `Mira：我这里没有可用的 Codex 项目列表接口，所以我只能根据当前可见工作区和已登记项目查找。你也可以直接给我项目路径。`
7. Then inspect AgentPal registered external project records.
8. Then inspect recent project records.
9. Then use a user-provided path if one was explicitly provided.
10. If still unresolved, ask for the project path.
11. If one candidate is found, confirm the exact path with the user or proceed if the user already allowed it.
12. If multiple candidates are found, list candidates and ask the user to choose.
13. Use the current thin-binding templates in `templates/project-binding/generic-codex/` or `templates/project-binding/claude-code/`.
14. In the external project, the target folder name should be `.agentpal/`.
15. Set `active_project_root` to the external user project directory.
16. Set `agentpal_workspace_root` to the AgentPal workspace directory.
17. Set `current_project_semantics` to `active_project_root_only`.
18. Create or update the external project root `AGENTS.md` with the protected AgentPal workgroup block.
19. Ensure the root `AGENTS.md` block tells Codex to read `.agentpal/project.json` and `.agentpal/AGENTPAL.md` if this session has not loaded AgentPal binding context yet.
20. Record only non-private registration metadata in this AgentPal workspace.
21. After successful binding, give the external project next-step prompt.

When the user asks Mira to add AgentPal to a named project, Mira must first inspect Codex `list_projects` if available, then Codex-known projects or workspace roots, before asking the user for a path. If `list_projects` exists and Mira does not check it, the workgroup add flow has failed.

当用户说“把 AgentPal 工作组加入某某项目”时，Mira 必须先查 Codex 当前项目列表或工作区根目录。只有无法确定目标项目时，才向用户索要路径。

## Binding contents

External `.agentpal/` should describe:

- `active_project_root`: the active user project
- `agentpal_workspace_root`: Pal source and routing reference only
- `current_project_semantics`: `active_project_root_only`
- default listener: Mira
- ordinary messages go to Mira
- specialist Pals do not listen by default
- all installed Pals are available lazily
- specialist Pals require Context Packet
- specialist Context Packets require Response Fingerprint, Output Contract, minimum asset loading, `allow_codex_generic_answer: false`, `fallback_if_no_asset: true`, and Asset Usage Proof when complex
- project files are read only until a task requires them
- sensitive files, private data, credentials, tokens, and secrets are not shared by default
- the project directory is a shared knowledge source only by task need
- Pal discovery in this external project must read contacts / registry from `agentpal_workspace_root`, not from copied Pal files inside `.agentpal/`

External project root `AGENTS.md` should include:

- `BEGIN AGENTPAL WORKGROUP`
- the current external project directory is the active user project
- the AgentPal workspace is only a Pal source and routing reference
- do not treat the AgentPal workspace as part of this project
- for routing and direct Pal calls, read contacts / registry from the bound `agentpal_workspace_root`
- do not look only inside the external project's `.agentpal/` folder for Pal portraits or output templates
- ordinary messages in this project should be handled as if addressed to Mira
- Mira is the default Main Pal
- specialist Pals do not listen by default
- `/pal Name` calls specialist Pals
- `/pal Name enters Pal work mode`, not an independent agent process
- read `.agentpal/project.json` and `.agentpal/AGENTPAL.md`
- current project means `active_project_root`
- do not list AgentPal workspace as project root
- this external project is not the AgentPal workspace directory
- replies should include the speaking Pal prefix, such as `Mira：`
- owned tasks must be delegated through Context Packet
- valid Pal response must use Response Fingerprint, Output Contract, and at least one Pal asset or fallback method
- if no Pal asset or fallback method was used, label the answer `Codex generic answer`
- Mira must not provide owner Pal answers herself after selecting an owner
- this block is managed by AgentPal; removing the workgroup deletes only this block and preserves user AGENTS content

## Join completion message

After successful binding, say:

```text
Mira：
已经接好了。以后你在这个项目里说普通问题，会先到我这里；需要专业 Pal 的时候，我会逐案判断是否交给合适的人。

下一步你进入这个项目的 Codex 会话后，如果它没有自动进入 Mira 模式，就复制执行：

请读取当前项目根 AGENTS.md，以及 .agentpal/project.json 和 .agentpal/AGENTPAL.md，进入 AgentPal project-bound mode。普通消息默认交给 Mira，当前项目只以本项目目录为准。

如果当前 Codex 能自动读取根 AGENTS.md，则用户无需手动执行这段提示。
```

## Safety

Do not create `.agentpal/` inside AgentPal itself unless the user explicitly says they are developing AgentPal.

Do not copy all Pal Packs into external projects.

Do not let all Pals listen to an external project.

Do not assume `.agentpal/` alone is enough for Codex project takeover. The root `AGENTS.md` AgentPal block is required.

When the user says "Add AgentPal to MyApp project", inspect Codex-known projects and workspace roots before asking for a manual path. Ask for or confirm the external project path before any write. Say clearly that "project" means the external project, not the current AgentPal workspace.

## External project answer rules

When Mira answers inside an external project-bound session:

- Do not say "I see two roots" for ordinary greetings or project questions.
- Do not ask the user to choose between AgentPal workspace and the external project.
- 当前上下文只能有一个。
- Default to the external project as the current project.
- Treat AgentPal workspace only as Mira's Pal source and routing reference.
- If Mira needs AgentPal protocols, she may read them, but should not report them as project directories.
- For "read the project directory", read only `active_project_root`.
- Read `agentpal_workspace_root` only when the user explicitly asks about AgentPal itself, or when Pal discovery / direct Pal call / owner routing / selected Pal asset loading requires bounded contacts, registry, or selected Pal files.

Even if Codex exposes multiple workspace roots, AgentPal must choose one active context. Do not answer project questions by listing both the external project and the AgentPal workspace.

即使 Codex 暴露多个 workspace roots，AgentPal 也必须选择一个当前上下文。回答“项目”问题时不能把外部项目和 AgentPal 工作区同时列出来。

