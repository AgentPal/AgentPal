# Use With Codex

This is the current Codex path for AgentPal v0.3.0-rc.1.

## Quick Start

1. Create a new Codex project with the AgentPal directory.
2. Open `prompts/codex/initialize-agentpal-workspace.md`.
3. Copy the whole prompt.
4. Paste it into the AgentPal project conversation in Codex to initialize AgentPal.
5. Start with Mira for ordinary messages.
6. Use `/pal Name` when you want to call a specialist directly.

## What To Expect

- Mira is the default Main Pal / Leader / Conductor.
- Ordinary messages go to Mira first.
- Specialist Pals do not listen by default.
- `/pal Name` enters the selected Pal working mode inside the current runtime.
- The active path is `Simple Pal Mode only`.

## Important Boundary

- AgentPal is not a Codex replacement.
- AgentPal is not a Codex subagent system.
- Deep Conductor is a no-code protocol foundation, not automatic runtime execution.
- Do not describe parallel child workflows as the current AgentPal runtime path.

## Good First Commands

- Ask Mira what AgentPal can do in the current release.
- Ask Mira to route a task if you are unsure which Pal should own it.
- Call a specialist directly with `/pal Atlas`, `/pal Quinn`, or `/pal Harper`.

## Related

- [Runtime Compatibility](00-runtime-compatibility.md)
- [Current Status](../00-overview/01-current-status.md)
