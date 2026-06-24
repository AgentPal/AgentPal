# Prompts

`prompts/` contains copy-and-paste prompts for AgentPal setup, project binding, and maintenance.

These files are Markdown instructions, not programs. They do not install dependencies, run scripts, scan the disk, create UI, or activate Deep Conductor, Subagent Mode, or external Agent orchestration.

## Quick Start Prompts

| User path | Prompt | Use when |
| --- | --- | --- |
| Codex | `codex/initialize-agentpal-workspace.md` | You opened the AgentPal Workspace directly in Codex and want to initialize Mira. |
| Claude Code | `claude-code/install-agentpal-current-project.md` | You are already inside `<your-project>` in Claude Code and want project-first AgentPal binding. |
| Generic CLI Agent | `generic-cli-agent/install-agentpal-current-project.md` | Your CLI agent can read directories, follow Markdown / JSON instructions, and maintain context. |

## Project Workgroup Prompts

- `join-external-project-workgroup.md`: AgentPal-led external project binding from an AgentPal Workspace session.
- `remove-agentpal-workgroup.md`: AgentPal-led external project binding removal.
- `codex/remove-agentpal-current-project.md`: Codex project-local AgentPal binding removal.
- `codex/remove-agentpal-workspace-from-codex.md`: stop using AgentPal Workspace in Codex without deleting files.
- `claude-code/remove-agentpal-current-project.md`: Claude Code project-local removal.
- `generic-cli-agent/remove-agentpal-current-project.md`: generic CLI project-local removal.

For Claude Code, prefer the project-first path:

```text
cd <your-project>
claude
```

Then paste `claude-code/install-agentpal-current-project.md`.

For Claude Code and generic CLI agents, the project-first install prompts are copy-paste ready. Do not edit the prompt before pasting. The runtime asks for the local AgentPal Workspace path during installation unless you already provided a clear path in the conversation. Enter a path such as:

```text
<path-to-AgentPal>
```

Keep local machine paths in project-local files such as `.agentpal/project.json` or `.claude/settings.local.json`; do not commit private local configuration.

## Maintenance Prompts

- `refresh-pal-index.md`: refresh contacts / registry after Pal Pack changes.
- `add-pal-to-agentpal.md`: add newly copied valid Pal Pack directories.
- `initialize-agentpal.md`: legacy-compatible workspace initialization prompt.
- `rebuild-mira-main-pal.md`: repair Mira public files only when damaged.
- `test-ai-routing-judgement.md`: manual routing judgement regression prompt.

Run Pal registration and index refresh prompts from the AgentPal Workspace itself:

- In Codex, open the AgentPal directory as its own Codex project, then paste `add-pal-to-agentpal.md` or `refresh-pal-index.md` into that AgentPal project conversation.
- In Claude Code, open a terminal in `<path-to-AgentPal>`, run `claude`, then paste the maintenance prompt there.
- In another CLI agent, open the CLI agent from `<path-to-AgentPal>`, then paste the maintenance prompt there.

Most users use AgentPal from an external project directory. That is normal for day-to-day work, but Pal registration changes the AgentPal Workspace files, so it should be done in the AgentPal Workspace unless the current runtime has explicit read/write access to that path.

## Future / Deprecated-For-Current-Use

- `test-codex-subagent-mode.md` is future-design diagnostic material. Do not use it as normal AgentPal v0.1.0-rc.1 task handling.

## Public-Safe Rules

- Use placeholders such as `<your-project>` and `<path-to-AgentPal>`.
- Do not include local absolute paths, credentials, tokens, customer data, or private project facts in prompt examples.
- Do not ask users to commit `.claude/settings.local.json`; it is local machine configuration.
- Do not copy all Pal Packs into an external project.
- Do not import the whole AgentPal Workspace into a project instruction file.

