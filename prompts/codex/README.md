# Codex Prompts

Use these prompts when the AgentPal Workspace is opened directly in Codex.

If you want to connect an ordinary project to AgentPal through thin binding instead, use the [AgentPal for Codex plugin](../../plugins/codex/agentpal-codex-plugin/README.md).

## Current Prompts

- `initialize-agentpal-workspace.md`: copyable Codex initialization prompt for AgentPal v0.5 no-code Pal collaboration, with Mira entry and Deep Conductor mode-decision boundaries.
- `remove-agentpal-current-project.md`: remove AgentPal binding from the current external Codex project.
- `remove-agentpal-workspace-from-codex.md`: stop using the AgentPal Workspace as the active Codex context without deleting files.

## Quick Start

Use this when you open the AgentPal Workspace directly in Codex.

1. Create a new Codex project with the AgentPal directory.
2. Open `prompts/codex/initialize-agentpal-workspace.md`.
3. Copy the whole prompt.
4. Paste it into the AgentPal project conversation in Codex to initialize AgentPal.
5. Start ordinary messages with Mira, or call a specialist with `/pal Name`.

Codex workspace initialization does not require `AGENTPAL_HOME`.

This prompt path is different from plugin-based project binding:

- the prompt path opens the AgentPal Workspace itself
- the plugin path binds an ordinary Codex project to AgentPal

## Boundary

Codex initialization reads the AgentPal Workspace as the active workspace. It does not bind AgentPal into an external user project. For external project work, use the project-first prompts under `prompts/claude-code/` or `prompts/generic-cli-agent/`, or the Codex project-local removal prompt when a Codex project already has AgentPal binding files.

Codex-style external project bindings should follow the shared protocol in [`docs/04-runtime-guides/project-thin-binding.md`](../../docs/04-runtime-guides/project-thin-binding.md).

AgentPal is a no-code Pal organization layer. Codex prompts must not add scanners, daemons, installers, connectors, marketplace programs, runtime services, or automatic external-Agent execution. Remote Git operations and GitHub Release actions require explicit current-session authorization.
