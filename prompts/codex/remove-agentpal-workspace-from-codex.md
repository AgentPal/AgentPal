# Stop Using AgentPal Workspace In Codex

Copy this prompt into Codex when you want to stop using the AgentPal Workspace as the active Codex project or conversation context.

This is not a file deletion prompt. It does not uninstall software and does not remove AgentPal from disk.

```text
Please help me stop using AgentPal Workspace in this Codex context.

Boundary:
- Do not delete the AgentPal repository.
- Do not delete any Pal Pack.
- Do not edit AgentPal release files.
- Do not remove AgentPal from external projects.
- Do not change git remotes, branches, tags, or releases.

Explain the difference:
1. Opening AgentPal in Codex is workspace initialization, not an installer.
2. To stop using AgentPal in Codex, I can close or archive this Codex thread, remove the AgentPal directory from my Codex project list if the UI supports it, or start a new Codex project/conversation that does not use AgentPal.
3. If an external project was connected to AgentPal, that is a separate project binding. Use `prompts/codex/remove-agentpal-current-project.md`, `prompts/claude-code/remove-agentpal-current-project.md`, or `prompts/generic-cli-agent/remove-agentpal-current-project.md` depending on the runtime.

If this current thread has already loaded AgentPal instructions, explain that the thread may keep old context in memory. The cleanest verification is to start a fresh Codex conversation outside AgentPal mode.

End with a short checklist:
- AgentPal files were not deleted.
- No project binding was removed by this prompt.
- No git or release state was changed.
- Next step is to start a non-AgentPal Codex conversation or remove the AgentPal project entry through the Codex UI if available.
```
