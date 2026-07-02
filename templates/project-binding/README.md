# Project Binding Templates

These templates are for thin AgentPal bindings in external user projects.

Canonical protocol: [`docs/04-runtime-guides/project-thin-binding.md`](../../docs/04-runtime-guides/project-thin-binding.md).

Use:

- `generic-codex/` for Codex-style or generic `AGENTS.md` runtimes.
- `claude-code/` for Claude Code projects.
- `prompts/` for install/update prompt text.

Default templates must not include `.agentpal/memory`, `.agentpal/state`, `.agentpal/reports`, `.agentpal/context`, `.agentpal/index`, `.agentpal/pals`, `.agentpal/workflows`, `.agentpal/evals`, `.agentpal/capability-inventory`, `.agentpal/business-systems`, `.agentpal/reviews`, `.agentpal/evidence`, `.agentpal/replay`, `.agentpal/rollback`, `.agentpal/verification`, `.agentpal/audit-trail`, `.agentpal/governance-decisions`, `.agentpal/change-ledger`, or `.agentpal/change-review`.
