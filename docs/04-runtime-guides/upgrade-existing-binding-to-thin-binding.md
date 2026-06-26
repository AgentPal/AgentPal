# Upgrade Existing Binding To Thin Binding

Use this guide when an external project was connected to AgentPal through an older or oversized binding and now needs the current thin binding pattern.

The goal is to make the project point back to the AgentPal Workspace instead of carrying copied Pal rules, Pal lists, or protocol bodies.

## Problems With Old Bindings

Older bindings may work briefly but become fragile because they can:

- preserve an old Pal roster after the AgentPal Workspace changes;
- embed long core rules that drift from current gates;
- confuse `active_project_root` with `agentpal_workspace_root`;
- make the user project look like a second AgentPal Workspace;
- hide which files are authoritative;
- make removal risky because copied content is mixed with user-authored instructions.

Thin binding keeps the project small and makes AgentPal updates visible through the workspace source files.

## Identify An Old Binding

Signs of an old or oversized binding:

- root `AGENTS.md` or `CLAUDE.md` contains a long copied Pal list;
- root instruction blocks contain full protocols instead of pointers to `core/`;
- `.agentpal/` contains copied Mira assets, Pal Packs, docs, examples, evals, or release material;
- `.agentpal/AGENTPAL.md` claims the project-local copy is authoritative;
- a project-local cache is treated as the current registry;
- direct Pal calls use stale names that do not match workspace contacts or registry;
- the binding lacks `read_core_from_agentpal_workspace: true`.

## Upgrade Steps

1. Confirm the current directory is the external user project.
2. Read `.agentpal/project.json` if it exists.
3. Keep valid root values when they are correct:
   - `active_project_root`;
   - `agentpal_workspace_root`;
   - `runtime_hint`.
4. Validate the AgentPal Workspace path by checking:
   - `agentpal.json`;
   - `AGENTS.md`;
   - `contacts/pals.json`;
   - `registry/pal.index.json`.
5. Replace old root `AGENTS.md` and `CLAUDE.md` AgentPal sections with the protected thin block from `templates/project-binding/root-agents-agentpal-block-template.md`.
6. Rewrite `.agentpal/project.json` to include:
   - `binding_version`;
   - `active_project_root`;
   - `agentpal_workspace_root`;
   - `runtime_hint`;
   - `active_mode: simple-pal-mode-only`;
   - `read_core_from_agentpal_workspace: true`;
   - `core_gate_paths`;
   - `pal_source_of_truth`.
7. Keep `.agentpal/AGENTPAL.md` as a short explanation of the thin binding.
8. Delete or mark old project-local Pal roster and copied protocol material as non-authoritative.
9. For Claude Code, merge `.claude/settings.local.json` so the AgentPal Workspace path is present in `permissions.additionalDirectories`.
10. Run the verification prompt for the target runtime.

## Cautions

- Do not delete user business files.
- Do not delete the AgentPal Workspace.
- Do not treat old project cache content as the current registry.
- Do not replace user-authored instruction text outside the protected AgentPal block.
- Do not create runtime helpers, installers, background processes, or UI.
- Do not activate future orchestration designs through a binding upgrade.

## Verification Checklist

- Current directory is the external project.
- `.agentpal/project.json` is valid JSON.
- `active_project_root` and `agentpal_workspace_root` are distinct unless the user is intentionally working on AgentPal itself.
- `read_core_from_agentpal_workspace` is true.
- Root AgentPal blocks exist once.
- Root AgentPal blocks point to core gates.
- Contacts and registry are read from the AgentPal Workspace.
- `.agentpal/` contains binding files only.
- Claude Code local settings are merged when Claude Code is the target runtime.
- The runtime reports Simple Pal Mode only.
