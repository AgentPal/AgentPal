# Generic CLI Agent Remove AgentPal From Current Project

Copy this prompt into a Markdown/JSON-capable CLI Agent while your shell is inside the target project directory.

```text
Remove AgentPal thin binding from the current project.

This removes only the AgentPal project binding. It must not delete project source files, project docs, `.git`, package files, user-authored `AGENTS.md` content outside the AgentPal block, or the AgentPal workspace itself.

Before changing files, confirm the current project root and ask me to confirm removal.

After confirmation:
1. Remove the current runtime entry from `.agentpal/project.json` `enabled_runtimes` if `.agentpal/project.json` exists.
2. Delete this project's `.agentpal/` directory only if no runtime binding remains.
3. Remove only the block between `<!-- BEGIN AGENTPAL BINDING: codex -->` and `<!-- END AGENTPAL BINDING: codex -->` from `AGENTS.md` for Codex-style generic bindings.
4. Preserve all other `AGENTS.md` content.
5. Do not modify Claude Code `.claude/settings.local.json` unless I explicitly ask.
6. Do not delete AgentPal workspace files.

Report briefly:
- `.agentpal/` removed or was absent
- `AGENTS.md` AgentPal block removed or was absent
- no project source files were deleted
- AgentPal workspace was not deleted

An already-open CLI Agent session may still have old instructions in memory. The cleanest verification is to restart the session in this project.
```
