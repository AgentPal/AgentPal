# Protected Block Standard

AgentPal host-runtime instruction blocks must use stable begin and end markers.

Canonical runtime-qualified markers:

```md
<!-- BEGIN AGENTPAL BINDING: codex -->
<!-- END AGENTPAL BINDING: codex -->
```

```md
<!-- BEGIN AGENTPAL BINDING: claude-code -->
<!-- END AGENTPAL BINDING: claude-code -->
```

Install and update operations may replace only the content inside those markers. They must preserve all user-authored content outside the protected block.

The block should point to `.agentpal/project.json` and `.agentpal/AGENTPAL.md` rather than copying the full AgentPal workspace rules.

Legacy `<!-- AGENTPAL:BEGIN -->` / `<!-- AGENTPAL:END -->` and `<!-- BEGIN AGENTPAL WORKGROUP -->` / `<!-- END AGENTPAL WORKGROUP -->` markers may be read during migration. New adapter writes must use runtime-qualified markers so Codex and Claude Code bindings can coexist safely.
