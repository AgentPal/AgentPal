# Codex One-Prompt AgentPal Project Removal

Copy this prompt into Codex while the current Codex project is the external user project that has an AgentPal workgroup binding.

Use this only for a user project that contains AgentPal binding files. Do not use it to delete the AgentPal Workspace itself.

```text
Please remove AgentPal from the current Codex project.

This removes only the AgentPal project binding. It must not delete:
- project source files
- project docs
- .git
- package files
- user-authored AGENTS.md content outside the AgentPal block
- user-authored CLAUDE.md content outside the AgentPal block, if present
- the AgentPal Workspace itself
- any Pal Pack files

Step 1 - Confirm current project root:
1. Treat the current Codex project directory as the target user project.
2. If the current directory appears to be the AgentPal Workspace itself, stop and say this prompt is for external project binding removal, not AgentPal Workspace deletion.
3. AgentPal Workspace indicators include:
   - root agentpal.json
   - prompts/codex/initialize-agentpal-workspace.md
   - official/pals/Mira-main/
   - workspace/organization/contacts/pals.json

Step 2 - Detect binding:
Check whether the current project has any of:
- .agentpal/
- AGENTS.md block between <!-- BEGIN AGENTPAL BINDING: codex --> and <!-- END AGENTPAL BINDING: codex -->

If none exist, report that no AgentPal project binding was found and do not change files.

Step 3 - Confirm before changing:
Before changing files, ask me to confirm removal.

Step 4 - Remove only the binding:
After confirmation:
1. Remove the `codex` entry from `.agentpal/project.json` `enabled_runtimes` if `.agentpal/project.json` exists.
2. Delete this project's .agentpal/ directory only if no runtime binding remains.
3. Remove only the block between <!-- BEGIN AGENTPAL BINDING: codex --> and <!-- END AGENTPAL BINDING: codex --> from AGENTS.md.
4. Preserve all other AGENTS.md content.
5. Do not remove any Claude Code block from CLAUDE.md unless I explicitly ask, because this is the Codex project-local removal path.
6. Do not modify .claude/settings.local.json unless I explicitly ask.
7. Do not delete AgentPal workspace files.

Step 5 - Report:
Report briefly:
- current project root
- .agentpal/ removed or was absent
- AGENTS.md AgentPal block removed or was absent
- CLAUDE.md was not touched by this Codex removal path
- no project source files were deleted
- AgentPal Workspace was not deleted

Note: an already-open Codex thread may still have old AgentPal instructions in memory. The cleanest verification is to start a new Codex conversation for this project. If you continue in the old thread, explicitly ask for `Codex generic answer:` when you do not want Pal mode.
```
