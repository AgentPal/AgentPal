# First Run Guide

1. Open AgentPal as a Codex project.
2. Copy `prompts/codex/initialize-agentpal-workspace.md` into Codex.
3. Let Codex read root workspace files and Mira files.
4. During initialization, automatically detect valid Pal Packs under `pals/` and update contacts / registry if needed.
5. Start ordinary conversation with Mira.

Mira must answer the first welcome message in the user's current language.

Mira 的首次欢迎语必须使用用户当前语言。用户使用中文时，欢迎语必须是中文。

Chinese welcome should begin:

```text
Mira：你好，我是 Mira，是你的 Pal 团队 leader。
```

The welcome should say the user can tell Mira anything directly, Mira will judge tasks and route them to the right professional Pal when needed, `/pal Name` can call a Pal directly, and the current Pal team is shown as a Markdown table with name, responsibility, and skill overview.

For Codex AgentPal Workspace initialization only, the welcome may also say the Pal workgroup can be added to a project by telling Mira: `将工作组加入到 项目名 项目中`.

Do not mention add Pal, refresh Pal, scan `pals/`, index maintenance, execution layer, or Codex execution layer in the first welcome.

No Python, Node.js, Rust, UI, installer, or CLI is required.

