---
name: agentpal-disable
description: Disable, uninstall, remove, or clean AgentPal thin binding from the current Codex project when the user asks to remove AgentPal or remove the AgentPal team.
---

# AgentPal Disable

Use this Skill to remove the Codex AgentPal thin binding from the current
project.

The Codex plugin is global. This Skill removes AgentPal only from the current
project and keeps `agentpal@agentpal` installed for other projects.

## Allowed Writes

Only remove or update:

- `.agentpal/project.json` when another runtime binding remains
- `.agentpal/` when no other runtime binding remains
- the Codex AgentPal protected block in `AGENTS.md`

## Procedure

1. Treat the current working directory as the target project root unless the user gives a different project path.
2. Remove only the Codex AgentPal protected block from `AGENTS.md`.
3. If `.agentpal/project.json` lists other enabled runtimes, remove only
   `codex` from `enabled_runtimes`, set `last_runtime` to `codex`, and
   preserve `.agentpal/`.
4. If no other runtime binding remains, remove `.agentpal/`.
5. Report changed files and whether other runtime bindings were preserved.

## Boundary

Disabling AgentPal from a project does not uninstall the Codex plugin itself.
Do not delete user-authored `AGENTS.md` content outside the AgentPal protected
block.
