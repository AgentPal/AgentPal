# Thin Binding Policy

External projects using this Org Pack remain thin-bound by default.

Allowed project-local binding files:

- `.agentpal/project.json`
- `.agentpal/AGENTPAL.md`
- `AGENTS.md` protected block
- `CLAUDE.md` protected block
- `.claude/settings.local.json`
- `.gitignore` entry for `.claude/settings.local.json`

Forbidden by default:

- `.agentpal/org-pack/`
- `.agentpal/pals/`
- `.agentpal/memory/`
- `.agentpal/reports/`
- `.agentpal/capability-inventory/`
- `.agentpal/business-systems/`
- `.agentpal/governance/`
- `.agentpal/workflows/`
- `.agentpal/evals/`

Org Pack assets stay in AgentPal central workspace, templates, examples, or approved private records.
