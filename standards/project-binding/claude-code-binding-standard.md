# Claude Code Binding Standard

Claude Code bindings use the same thin project binding as generic Codex-style projects, plus optional Claude-local permission configuration.

Allowed Claude-specific files:

- `<project>/CLAUDE.md` protected AgentPal block
- `<project>/.claude/settings.local.json`
- `<project>/.gitignore` entry for `.claude/settings.local.json`

`.claude/settings.local.json` is local machine configuration and should not be committed.

The Claude binding must not copy central Pal Packs, contacts, memory, reports, state, workflows, or evals into the external project.
