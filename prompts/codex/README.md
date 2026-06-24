# Codex Prompts

Use these prompts when the AgentPal Workspace is opened directly in Codex.

## Current Prompts

- `initialize-agentpal-workspace.md`: copyable Codex initialization prompt for `Simple Pal Mode only`.
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

## Boundary

Codex initialization reads the AgentPal Workspace as the active workspace. It does not bind AgentPal into an external user project. For external project work, use the project-first prompts under `prompts/claude-code/` or `prompts/generic-cli-agent/`, or the Codex project-local removal prompt when a Codex project already has AgentPal binding files.
