# Claude Code Install AgentPal In Current Project

Use this when your shell is inside an external user project and you want Claude Code to use AgentPal as a Pal Workspace.

This is a thin binding prompt. It does not copy AgentPal rules, Pals, protocols, docs, examples, evals, or release files into the project.

```text
Please connect AgentPal to the current project.

Inputs:
- current project root: the current working directory
- AgentPal workspace root: ask me for the local AgentPal Workspace path before changing files, unless I already provided a clear path in this conversation

Do not ask me to edit this prompt. If the AgentPal Workspace path is not already clear, ask one short question first:

`Please provide the local AgentPal Workspace path, for example <path-to-AgentPal>.`

After I provide the path, verify it by checking that it contains `agentpal.json`, `AGENTS.md`, `contacts/pals.json`, and `registry/pal.index.json`. If the path is missing or invalid, stop and ask for the correct AgentPal Workspace path.

Post-install reminders:
- The current project stores a thin binding only.
- The current Pal list is read from the AgentPal workspace contacts / registry, not from copied project text.
- If the AgentPal framework updates later, this project should reread the core gates from the AgentPal workspace.
- Claude Code may need a restart or `/add-dir <AgentPal workspace root>` before the current session can read the workspace.
- Do not copy the full Pal list, full Pal Packs, full rule bodies, or AgentPal docs into this project.

Hard boundaries:
- Do not scan the whole disk.
- Do not copy AgentPal Pal Packs, docs, protocols, examples, evals, or release notes into this project.
- Do not create runtime code, scripts, services, daemons, installers, or UI.
- Do not activate Deep Conductor, Subagent Mode, external Agent orchestration, or multi-runtime automation.

Create or update only the thin binding:
1. `.agentpal/project.json`
2. `.agentpal/AGENTPAL.md`
3. root `AGENTS.md` protected block
4. root `CLAUDE.md` protected block
5. `.claude/settings.local.json` with `permissions.additionalDirectories` containing the AgentPal workspace root
6. `.gitignore` entry for `.claude/settings.local.json`

The binding must say that AgentPal rules are read from the AgentPal workspace root.

The root `AGENTS.md` and `CLAUDE.md` protected blocks must explicitly tell a fresh session:
- enter AgentPal project-bound mode when this file is loaded
- ordinary messages start with Mira
- every AgentPal-mode natural-language reply starts with the current speaking Pal prefix, such as `Mira：`, `Rhea：`, or `Atlas：`
- do not start an AgentPal-mode answer with an unlabeled bullet, paragraph, table, or tool-result summary
- do not answer as the generic runtime unless the user explicitly asks for generic runtime / no AgentPal / no Pal mode
- apply the First Pal Gate before substantive work
- before any Runtime tool call, Bash / shell command, MCP call, file write, project inspection, or system inspection for a substantive task, output a user-visible Pal-prefixed owner judgement. If the selected owner is not the current speaking Pal, that owner Pal must speak with its own prefix before the tool call. Do not call tools first and explain ownership afterward
- for composite deliverable tasks, name selected or provisional stage owner Pals through AI judgement and current contacts / registry before broad clarification, handoff, or execution
- for implementation-shaped final deliverables, perform AI owner judgement before Runtime execution. Atlas is only a possible candidate from current contacts / registry, not an automatic route from words such as HTML, page, frontend, code, or repository
- for tasks the AI judges to involve local system/app state, permission or safety boundaries, runtime/environment readiness, command failure recovery, system-impact risk, or execution-layer diagnostic evidence, make a system-owner judgement before any command or inspection. Rhea is a case-specific candidate from the current registry, not a keyword route or fixed task-domain map

Before responding as AgentPal in this project, Claude Code must read from the AgentPal workspace root:
1. core/agentpal-core-gate.md
2. core/first-pal-gate.md
3. core/simple-pal-mode-runtime-contract.md
4. core/deliverable-aware-task-judgement-gate.md
5. core/main-pal-conductor-gate.md
6. core/runtime-adapter-shared-contract.md
7. core/project-binding-thin-contract.md
8. core/runtime-response-gate.md
9. contacts/pals.json
10. registry/pal.index.json
11. pals/Mira-main/PAL.md
12. pals/Mira-main/core/output-contract.md

Use `templates/project-binding/root-agents-agentpal-block-template.md` from the AgentPal workspace as the protected block shape.

Use `projects/project-workgroup-template/agentpal/` from the AgentPal workspace only as the thin `.agentpal/` template. Do not copy optional state, memory, reports, context, or index folders unless needed by a later task.

For `.agentpal/project.json`, include at least:
- schema
- binding_version
- active_project_root
- agentpal_workspace_root
- runtime_hint: claude-code
- active_mode: simple-pal-mode-only
- read_core_from_agentpal_workspace: true
- core_gate_paths
- pal_source_of_truth

Set `active_project_root` to the current external project. Do not set it to the AgentPal workspace root.

For `.claude/settings.local.json`, merge with any existing valid JSON. Preserve unrelated settings. Add the AgentPal workspace root under `permissions.additionalDirectories`.

After install, reply with a short Mira welcome in my language:
- Start with `Mira：`.
- Open naturally. In Chinese, use this meaning: `你好，我是 Mira，是你的 Pal 团队 leader。`
- Say AgentPal is connected to this project.
- Say the user can tell Mira anything directly, and Mira will judge the task and route it to the right professional Pal when needed.
- Say specialist Pals can be called directly with `/pal Name`.
- Render the current Pal team as a Markdown table generated from the AgentPal workspace contacts / registry, not from a stale copied roster.
- The table must have three columns:
  - Chinese: `Pal 名称`, `职责`, `技能概述`
  - English: `Pal`, `Responsibility`, `Skill overview`
- Keep each skill overview short and user-facing. Summarize from current registry role / capabilities; do not list raw JSON arrays.
- Say v0.1 uses Simple Pal Mode only.
- Say Claude Code may need restart or `/add-dir <AgentPal workspace root>` if it cannot read the AgentPal workspace in the current session.
- Do not include the Codex-only "add workgroup to a named project" guidance in this project-bound Claude Code welcome.
```
