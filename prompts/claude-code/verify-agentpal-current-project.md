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
   - runtime_hint
   - active_mode: simple-pal-mode-only
   - read_core_from_agentpal_workspace: true
   - core_gate_paths
   - pal_source_of_truth
4. AgentPal workspace path is readable.
5. These AgentPal workspace files exist:
   - core/agentpal-core-gate.md
   - core/first-pal-gate.md
   - core/simple-pal-mode-runtime-contract.md
   - core/deliverable-aware-task-judgement-gate.md
   - core/main-pal-conductor-gate.md
   - core/runtime-adapter-shared-contract.md
   - core/project-binding-thin-contract.md
   - core/runtime-response-gate.md
   - contacts/pals.json
   - registry/pal.index.json
   - pals/Mira-main/PAL.md
   - pals/Mira-main/core/output-contract.md
6. The AgentPal workspace contacts / registry are readable and are the Pal source of truth. If project files contain a copied roster, report it as stale or non-authoritative.
7. `CLAUDE.md` contains exactly one AgentPal block between:
   - `<!-- BEGIN AGENTPAL WORKGROUP -->`
   - `<!-- END AGENTPAL WORKGROUP -->`
8. `AGENTS.md` contains exactly one AgentPal block between the same markers.
9. Both blocks point to AgentPal core gates and do not embed a full Pal roster or full protocols.
10. `.claude/settings.local.json` exists and is valid JSON.
11. `permissions.additionalDirectories` contains the AgentPal workspace path, merged with any unrelated existing entries.
12. `.gitignore` contains `.claude/settings.local.json`.
13. `.agentpal/` does not contain copied full protocols, full Mira assets, release docs, examples, evals, or PalBench reports.
14. A Generic CLI binding, if present, has at least root `AGENTS.md` plus `.agentpal/project.json` and does not rely on Claude Code settings.
15. No internal local paths, private user data, or credential-like values are exposed in public project instructions.
16. The active mode is Simple Pal Mode only.
17. Deep Conductor, Subagent Mode, and external Agent orchestration are not activated by the binding.

Output a concise checklist:
- pass / fail / warning
- evidence path
- fix suggestion

If the current session cannot access the AgentPal path even though settings.local.json contains it, recommend restarting Claude Code or using `/add-dir <path-to-AgentPal>` for this session.
```
