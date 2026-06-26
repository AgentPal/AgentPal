# Claude Code Remove AgentPal From Current Project

Copy this prompt into Claude Code while your shell is inside the target project directory.

```text
Remove AgentPal thin binding from the current project.

This removes only the AgentPal project binding. It must not delete:
- project source files
- project docs
- `.git`
- package files
- user-authored `CLAUDE.md` content outside the AgentPal block
- user-authored `AGENTS.md` content outside the AgentPal block
- the AgentPal workspace itself
- any Pal Pack files

Thin binding note:
- A correct binding should not have copied full Pal lists, full protocols, full Mira assets, docs, examples, evals, or release material into this project.
- If such copied material exists, report it separately and ask before removing anything that is not clearly inside the protected AgentPal block or `.agentpal/`.

Before changing files, confirm the current project root and ask me to confirm removal.

After confirmation:
1. Delete this project's `.agentpal/` directory.
2. Remove only the block between `<!-- BEGIN AGENTPAL WORKGROUP -->` and `<!-- END AGENTPAL WORKGROUP -->` from `CLAUDE.md`.
3. Remove only the same protected block from `AGENTS.md`.
4. Read `.claude/settings.local.json` if it exists.
5. Remove the AgentPal workspace path from `permissions.additionalDirectories`.
6. Preserve all other Claude Code settings.
7. If settings.local.json becomes empty or only contains empty permissions, ask whether to delete it.
8. Do not modify `.claude/settings.json` unless I explicitly ask.
9. Do not delete the AgentPal workspace or any user-authored project content.

If `.claude/settings.local.json` is invalid JSON, stop and ask me how to proceed. Do not overwrite it.

Report briefly:
- `.agentpal/` removed or was absent
- `CLAUDE.md` AgentPal block removed or was absent
- `AGENTS.md` AgentPal block removed or was absent
- `.claude/settings.local.json` additionalDirectories updated or was absent
- no project source files were deleted
- AgentPal workspace was not deleted

An already-open Claude Code session may still have old instructions in memory. The cleanest verification is to restart Claude Code in this project.
```
