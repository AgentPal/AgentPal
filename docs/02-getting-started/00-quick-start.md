# Quick Start

Use this path when you want to try AgentPal v0.5 in Codex.

For real user projects in Claude Code or generic CLI Agents, prefer the project-first workflow:

```text
cd <your-project>
claude
```

Then paste the one-prompt install prompt from `prompts/claude-code/install-agentpal-current-project.md`. Do not edit the prompt first; Claude Code asks for the AgentPal Workspace path during installation.

## Steps

1. Clone or download the AgentPal Workspace.
2. For Codex, open the AgentPal directory in Codex.
3. Paste the contents of `prompts/codex/initialize-agentpal-workspace.md`.
4. Start ordinary messages with Mira.
5. Use `/pal Name` to call a registered Pal directly.

Example:

```text
/pal Harper Help me rewrite this release note.
```

## What Should Happen

- Mira is the default Main Pal, Leader Pal, and Conductor.
- Specialist Pals do not listen by default.
- Direct calls resolve from the central Pal roster under `workspace/organization/contacts/`.
- Simple Pal Mode remains the only active task-handling path.

## No Required Runtime Dependency

AgentPal initialization does not require Python, Node.js, Rust, Go, a desktop app, a web UI, a daemon, a scanner, a validator, or an installer.

## Related

- [Install or download](01-install-or-download.md)
- [Use with Codex](02-open-in-codex.md)
- [Use with Claude Code](03-open-in-claude-code.md)
- [Claude Code project install](../04-runtime-guides/02-use-with-claude-code.md)
- [Generic CLI Agent project install](../04-runtime-guides/03-use-with-generic-cli-agent.md)
- [Initialize AgentPal](04-initialize-agentpal.md)
- [Call your first Pal](05-call-your-first-pal.md)
