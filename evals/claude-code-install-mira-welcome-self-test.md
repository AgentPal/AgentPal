# Claude Code Install Mira Welcome Self-Test

## Purpose

Verify that the Claude Code one-prompt install flow does not stop at a file-change summary and always gives the user a clear Mira first-screen welcome after installation.

## Input

Run Claude Code inside a clean external project directory and paste:

```text
prompts/claude-code/install-agentpal-current-project.md
```

Set:

```text
AGENTPAL_HOME = <path-to-AgentPal>
```

## Pass

- The final install response keeps a short install result summary.
- The final install response also includes a first welcome message that starts with `Mira：`.
- The welcome says AgentPal is connected to the current project.
- For Chinese users, the welcome opens with the meaning: `你好，我是 Mira，是你的 Pal 团队 leader。`
- The welcome presents Mira's main identity as the Pal team leader.
- The welcome says the user can tell Mira anything directly.
- The welcome says Mira routes tasks to the right professional Pal when needed.
- The welcome says `/pal Name` can explicitly call a specialist Pal.
- The welcome shows the current Pal team as a Markdown table generated from contacts / registry.
- The table has three columns: `Pal 名称`, `职责`, `技能概述` in Chinese, or `Pal`, `Responsibility`, `Skill overview` in English.
- The welcome does not list any non-bundled former customer Pal.
- The welcome does not mention removed CRM-specific tooling.
- The welcome says AgentPal v0.1 uses Simple Pal Mode only.
- The welcome says Deep Conductor is future design and is not automatically executed in v0.1.
- The Claude Code project-bound welcome does not include the Codex-only "将工作组加入到 项目名 项目中" guidance.
- The install result is not the only output.

## Fail

- The final response only lists created or updated files.
- The final response does not include `Mira：`.
- Mira introduces herself primarily as a support assistant.
- The welcome omits the Pal team table.
- The welcome uses a copied hard-coded project-local Pal roster instead of AgentPal workspace contacts / registry.
- The welcome lists a non-bundled former customer Pal or removed CRM-specific tooling as default AgentPal capability.
- The welcome claims Deep Conductor, Subagent Mode, or multi-agent orchestration is active by default in v0.1.
- The prompt creates runtime code, scripts, installers, daemons, scanners, validators, or new dependencies.
