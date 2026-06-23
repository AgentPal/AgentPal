# Project Workgroup Binding Self Test

## Checks

- [ ] Mira confirms external project path before writing.
- [ ] Codex project list first: Mira checks Codex-known projects or current Codex project list before asking for a manual path.
- [ ] Workspace roots first: Mira checks current workspace roots before asking for a manual path.
- [ ] If a named project such as `eagleweb` resolves to one visible path, Mira uses or confirms that path instead of asking the user to type it.
- [ ] AgentPal workspace is not treated as target project.
- [ ] `.agentpal/` template is complete.
- [ ] External project root `AGENTS.md` is created or updated.
- [ ] Existing `AGENTS.md` content is preserved outside `BEGIN AGENTPAL WORKGROUP` / `END AGENTPAL WORKGROUP`.
- [ ] Root `AGENTS.md` tells Codex to read `.agentpal/project.json`, `.agentpal/AGENTPAL.md`, and `.agentpal/PAL_GROUP.md`.
- [ ] Root `AGENTS.md` tells Codex to read `.agentpal/INIT_AGENTPAL_PROJECT_PROMPT.md` if AgentPal rules have not loaded yet.
- [ ] Join completion message includes the next-step prompt to read root `AGENTS.md` and `.agentpal/INIT_AGENTPAL_PROJECT_PROMPT.md`.
- [ ] Default listener is Mira.
- [ ] Ordinary project messages are handled as if addressed to Mira.
- [ ] Replies include the speaking Pal prefix, such as `Mira：`.
- [ ] Specialist Pals do not listen by default.
- [ ] Specialist Pals do not read project files unless routed or called.
- [ ] Owned tasks must be delegated through Context Packet.
- [ ] Project files are read by task need only.
- [ ] Sensitive files, credentials, tokens, and secrets are not shared by default.
- [ ] `.agentpal/` alone is not treated as enough for project takeover.
- [ ] `project.json` contains `active_project_root`.
- [ ] `project.json` contains `agentpal_workspace_root`.
- [ ] `current_project_semantics` says project questions mean `active_project_root`.

