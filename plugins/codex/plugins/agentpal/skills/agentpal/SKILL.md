---
name: agentpal
description: Use when the user asks about AgentPal in Codex, wants to enable or remove AgentPal, asks what AgentPal is, or needs the current project AgentPal binding checked.
---

# AgentPal

AgentPal for Codex is a global host-level Codex plugin that helps connect any
current Codex project to AgentPal through a project-local thin binding.

The public Codex install document should also prepare the full public AgentPal
workspace and write:

```text
%USERPROFILE%\.agentpal\config.json
```

Project setup should read that config automatically. Users should only need to
say "Add AgentPal to this project" or "Add the AgentPal team to this project"
after installation.

The global plugin remains installed when a project's binding is removed. Project
removal should only clean the current project's thin binding.

## Routing

- For "add AgentPal", "install AgentPal in this project", "connect AgentPal",
  "add the AgentPal team", or "add the workgroup", use `agentpal-enable`.
- For "check AgentPal", "is AgentPal enabled", or "status", use
  `agentpal-status`.
- For "repair AgentPal", "fix AgentPal", or a partial binding, use
  `agentpal-repair`.
- For "disable AgentPal", "remove AgentPal from this project",
  "remove the AgentPal team", or "uninstall AgentPal from this project", use
  `agentpal-disable`.
- For uninstalling the Codex plugin itself, explain that host-level removal uses
  `codex plugin remove agentpal@agentpal`; removing the marketplace source uses
  `codex plugin marketplace remove agentpal`.

## Boundary

The project binding is thin. It writes only:

- `.agentpal/project.json`
- `.agentpal/AGENTPAL.md`
- the Codex AgentPal protected block in `AGENTS.md`

Do not copy AgentPal Pal Packs, central Pal assets, memory, reports, workflows,
evals, examples, release files, services, daemons, databases, scanners, or
background sync into the user project.
