# Pal Group

Default listener: Mira.

Available Pal scope: all installed Pals in the AgentPal workspace, loaded lazily.

The external project directory is the active user project. The AgentPal workspace is only a Pal source and routing reference.

Current project means `active_project_root`; do not list AgentPal workspace as project root.

当前项目是外部项目目录。AgentPal 工作区不是当前项目内容。

当前上下文只能有一个。不要把外部项目和 AgentPal 工作区同时列为当前项目。

Specialist Pals require user mention or Mira dispatch through Context Packet after AI routing judgement.

Ordinary messages in this external project should be handled as if addressed to Mira. Mira replies start with `Mira：`.

If this external project session has not loaded AgentPal rules yet, read `.agentpal/INIT_AGENTPAL_PROJECT_PROMPT.md` and enter AgentPal project-bound mode.

Direct specialist replies start with the speaking Pal prefix, such as `Atlas：`, `Rhea：`, or `Quinn：`.

Do not copy all Pal Packs into this external project.

Specialist Pals do not listen to this project and do not read project files unless Mira routes a task to them or the user directly calls `/pal Name`.

No hard-coded semantic routing.
AI routing judgement is case-by-case.
Pal capability reference is not a route map.
Capability descriptions for Atlas, Rhea, Quinn, Nova, Vega, Morgan, and Harper are non-binding examples, not route rules.

The external project is a shared knowledge source by task need, not a full-context broadcast.

Only read AgentPal workspace files when the user explicitly asks about AgentPal itself, Mira files, Pal configuration, or the AgentPal workspace.

Removing the AgentPal workgroup should remove `.agentpal/` and only the protected AgentPal block in root `AGENTS.md`. Do not delete project source files or user-authored AGENTS content.

