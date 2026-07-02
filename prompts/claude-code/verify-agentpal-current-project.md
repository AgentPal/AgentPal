# Claude Code AgentPal Project Verification

Copy this prompt into Claude Code while your shell is inside the target project directory.

```text
Verify whether AgentPal thin binding is correctly connected to the current project.

Check only:
- the current project
- `.agentpal/project.json`
- the AgentPal workspace path recorded in project.json or `.claude/settings.local.json`

Do not scan the whole disk.

Verify:
1. Current directory is the active project root and is not the AgentPal workspace itself.
2. `.agentpal/project.json` exists and is valid JSON.
3. `project.json` has:
   - active_project_root
   - agentpal_workspace_root
   - agentpal_project_record
   - binding_mode: thin
   - runtime_hint
   - active_mode: agentpal-v0.5-pal-collaboration, or an older binding value with an explicit warning that it should be refreshed
   - simple_pal_path_available: true, if the binding has been refreshed for v0.5
   - deep_conductor_no_code_protocol_enabled: true, if the binding has been refreshed for v0.5
   - read_core_from_agentpal_workspace: true
   - core_gate_paths
   - pal_source_of_truth
   - central_pal_contacts
4. AgentPal workspace path is readable.
5. These AgentPal workspace files exist:
   - agentpal.json
   - RESOURCE_INDEX.md
   - core/agentpal-core-gate.md
   - core/first-pal-gate.md
   - core/simple-pal-mode-runtime-contract.md
   - core/deliverable-aware-task-judgement-gate.md
   - core/main-pal-conductor-gate.md
   - core/runtime-adapter-shared-contract.md
   - core/project-binding-thin-contract.md
   - core/runtime-response-gate.md
   - workspace/organization/contacts/pals.json
   - workspace/organization/contacts/PAL_CONTACTS.md
   - workspace/projects/README.md
   - workspace/projects/_template/project.json
   - official/pals/Mira-main/PAL.md
   - official/pals/Mira-main/core/output-contract.md
   - standards/deep-conductor/
   - standards/capability-inventory/
   - standards/asset-boundary/
   - templates/project-binding/
6. The AgentPal workspace central contacts are readable and are the Pal source of truth. If project files contain a copied roster, report it as stale or non-authoritative.
6a. `agentpal_project_record` points to `workspace/projects/<project-id>` and project memory, source maps, derived knowledge, tasks, reports, governance records, and capability inventory are not stored in project-local `.agentpal/`.
7. `CLAUDE.md` contains exactly one AgentPal block between:
   - `<!-- BEGIN AGENTPAL BINDING: claude-code -->`
   - `<!-- END AGENTPAL BINDING: claude-code -->`
8. If Codex is also enabled, `AGENTS.md` contains exactly one AgentPal block between:
   - `<!-- BEGIN AGENTPAL BINDING: codex -->`
   - `<!-- END AGENTPAL BINDING: codex -->`
9. Both blocks point to AgentPal core gates and do not embed a full Pal roster or full protocols.
10. `.claude/settings.local.json` exists and is valid JSON.
11. `permissions.additionalDirectories` contains the AgentPal workspace path, merged with any unrelated existing entries.
12. `.gitignore` contains `.claude/settings.local.json`.
13. `.agentpal/` does not contain copied full protocols, full Mira assets, release docs, examples, evals, or PalBench reports.
14. A Generic CLI binding, if present, has at least root `AGENTS.md` plus `.agentpal/project.json` and does not rely on Claude Code settings.
15. No internal local paths, private user data, or credential-like values are exposed in public project instructions.
16. The binding does not claim deterministic keyword routing or fixed task-domain routes.
17. AgentPal v0.5 treats Deep Conductor as a no-code collaboration and mode-decision protocol. It may judge Fast Route, Owner + Verifier, Plan-Execute-Verify, Parallel Review, Sequential Chain, External Agent handoff, and Fallback shapes, but the binding must not claim automatic subagent execution or external Agent execution.
18. Capability unknown is handled honestly: no automatic runtime / model / plugin / Skill / MCP scan is claimed, and any manual capability profile is marked as manual or unverified.
19. No prompt or binding instruction authorizes `git push`, `git pull`, `git fetch`, tag creation, GitHub Release creation, or GitHub API publication without explicit current-session user authorization.

Output a concise checklist:
- pass / fail / warning
- evidence path
- fix suggestion

If the current session cannot access the AgentPal path even though settings.local.json contains it, recommend restarting Claude Code or using `/add-dir <path-to-AgentPal>` for this session.
```
