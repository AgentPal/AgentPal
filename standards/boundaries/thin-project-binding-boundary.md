# Thin Project Binding Boundary

External user projects must receive only a thin AgentPal binding by default.

Allowed default files:

- `<project>/.agentpal/project.json`
- `<project>/.agentpal/AGENTPAL.md`
- `<project>/AGENTS.md` protected AgentPal block
- `<project>/CLAUDE.md` protected AgentPal block, when Claude Code is used
- `<project>/.claude/settings.local.json`, when Claude Code needs local additional directory access
- `<project>/.gitignore` entry for `.claude/settings.local.json`

Forbidden default additions:

- `.agentpal/memory/`
- `.agentpal/state/`
- `.agentpal/reports/`
- `.agentpal/context/`
- `.agentpal/index/`
- `.agentpal/pals/`
- `.agentpal/workflows/`
- `.agentpal/evals/`
- full Pal Pack copies
- central contacts, registry, governance, or release files

The project binding points back to the AgentPal workspace as a reference. It must not turn the external project into an AgentPal workspace.
