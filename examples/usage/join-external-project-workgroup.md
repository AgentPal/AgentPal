# Join External Project Workgroup

## User message

```text
把工作组添加到 eagleweb 项目
```

## Expected Mira behavior

Mira starts with `Mira：` and checks Codex-known projects / current Codex project list / workspace roots before asking for a manual path.

If Codex-visible projects include:

```text
C:/Projects/eagleweb
```

Mira uses or confirms that path:

```text
Mira：我先查 Codex 当前项目列表和 workspace roots。已找到 eagleweb：C:/Projects/eagleweb。我会把 AgentPal 工作组加入这个外部项目，并保持 AgentPal 工作区只作为 Pal 来源。
```

Only if no match is found should Mira ask the user to provide a path.

Binding must create or update:

- `.agentpal/project.json`
- `.agentpal/AGENTPAL.md`
- external project root `AGENTS.md` with `<!-- BEGIN AGENTPAL WORKGROUP -->` / `<!-- END AGENTPAL WORKGROUP -->`
- root `CLAUDE.md` with the same block when using Claude Code

The root `AGENTS.md` block must tell Codex to read `.agentpal/project.json` and `.agentpal/AGENTPAL.md` if the session has not loaded AgentPal binding context yet.

After successful binding, Mira says:

```text
Mira：
已经接好了。以后你在这个项目里说普通问题，会先到我这里；需要专业 Pal 的时候，我会逐案判断是否交给合适的人。

下一步你进入这个项目的 Codex 会话后，如果它没有自动进入 Mira 模式，就复制执行：

请读取当前项目根 AGENTS.md，以及 .agentpal/project.json 和 .agentpal/AGENTPAL.md，进入 AgentPal project-bound mode。普通消息默认交给 Mira，当前项目只以本项目目录为准。

如果当前 Codex 能自动读取根 AGENTS.md，则用户无需手动执行这段提示。
```

Example placeholder path:

```text
J:/dev/MyProject
```

## Files or protocols involved

- `templates/project-binding/generic-codex/`
- `templates/project-binding/claude-code/`
- `templates/project-binding/prompts/install-thin-binding.md`
- `templates/project-binding/root-agents-agentpal-block-template.md`
- `standards/project-binding/project-binding-protocol.md`

## What Mira must not do

- ask for a manual path before checking Codex-known projects or workspace roots
- use the AgentPal workspace as the target project
- copy all Pals into the external project
- let specialist Pals listen by default
- share sensitive files by default
- assume `.agentpal/` alone is enough for Codex takeover
- omit the next-step prompt for reading `AGENTS.md`, `.agentpal/project.json`, and `.agentpal/AGENTPAL.md`

