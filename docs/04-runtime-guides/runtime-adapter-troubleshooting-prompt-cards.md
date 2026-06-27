# Runtime Adapter Troubleshooting Prompt Cards

Copy one card into the host runtime when a project-bound AgentPal setup behaves strangely. Each card asks for bounded inspection only: the current project, `.agentpal/`, root instruction files, runtime-local settings when relevant, and the AgentPal Workspace path already recorded in the binding.

## Card 1: Claude Code Opened In The Wrong Directory

User problem: Claude Code was started outside the intended project.

Copyable prompt:

```text
Check whether this Claude Code session is running in the intended project before touching files. Report the current directory, whether it matches `.agentpal/project.json` `active_project_root` if present, and whether this directory appears to be the AgentPal Workspace itself. Do not install or modify anything yet.
```

Expected checks:

- current directory;
- `.agentpal/project.json` when present;
- whether `active_project_root` matches the current directory;
- whether the current directory contains AgentPal root files.

Should-not behavior:

- do not bind AgentPal to the wrong project;
- do not treat the AgentPal Workspace as the external project.

## Card 2: Install Succeeded But Mira Did Not Welcome

User problem: install reported success, but the first AgentPal reply did not start with Mira.

Copyable prompt:

```text
Verify why Mira did not produce the project-bound welcome. Check only the current project binding, root instruction blocks, the recorded AgentPal Workspace path, central contacts, and Mira entry files. Report pass, fail, or warning with exact evidence and one fix.
```

Expected checks:

- `.agentpal/project.json`;
- protected blocks in `AGENTS.md` and `CLAUDE.md`;
- required core gate paths;
- `workspace/organization/contacts/pals.json`;
- `workspace/organization/contacts/PAL_CONTACTS.md`;
- `official/pals/Mira-main/PAL.md`;
- `official/pals/Mira-main/core/output-contract.md`.

Should-not behavior:

- do not claim success without reading evidence;
- do not copy Mira assets into the project.

## Card 3: Claude Cannot Read AgentPal Directory

User problem: Claude Code has a project binding but cannot access the AgentPal Workspace.

Copyable prompt:

```text
Check Claude Code access to the AgentPal Workspace path recorded in `.agentpal/project.json` and `.claude/settings.local.json`. Preserve unrelated settings. If access fails, recommend restart or `/add-dir <path-to-AgentPal>` for this session.
```

Expected checks:

- `agentpal_workspace_root`;
- `.claude/settings.local.json` valid JSON;
- `permissions.additionalDirectories`;
- a direct read of required AgentPal Workspace files when allowed.

Should-not behavior:

- do not rewrite unrelated Claude settings;
- do not create a copied AgentPal directory inside the project.

## Card 4: `.claude/settings.local.json` Did Not Take Effect

User problem: settings were updated but the running Claude Code session behaves as if nothing changed.

Copyable prompt:

```text
Inspect `.claude/settings.local.json` for valid JSON and the AgentPal Workspace path in `permissions.additionalDirectories`. If the file is correct but this session still cannot read the workspace, say the session likely needs restart or `/add-dir <path-to-AgentPal>`.
```

Expected checks:

- settings file exists;
- valid JSON;
- additional directory value is present once;
- current session read test for core gate files.

Should-not behavior:

- do not repeatedly append duplicate paths;
- do not edit shared Claude settings unless explicitly requested.

## Card 5: Stale Pal List

User problem: a newly added Pal is missing or an old Pal still appears.

Copyable prompt:

```text
Check whether this project reads the Pal list from the AgentPal Workspace central contacts. Look for any copied roster in project files and mark it non-authoritative. Then report the current Pal names from central contacts.
```

Expected checks:

- `workspace/organization/contacts/pals.json`;
- `workspace/organization/contacts/PAL_CONTACTS.md`;
- root instruction blocks;
- `.agentpal/` for copied roster text.

Should-not behavior:

- do not use a project-local roster as source of truth;
- do not update Pal contacts inside the external project.

## Card 6: `/pal Atlas` Treated As Ordinary Text

User problem: direct Pal command was not recognized.

Copyable prompt:

```text
Verify direct Pal call support for this project. Check that root AgentPal blocks mention `/pal Name`, that central contacts are readable, and that Atlas exists in the current central roster. Do not infer from a copied roster.
```

Expected checks:

- direct mention instructions in root blocks;
- central contacts readable;
- `Atlas` present in current registry;
- active mode is Simple Pal Mode only.

Should-not behavior:

- do not add a new project-local command parser;
- do not change Atlas assets for an adapter issue.

## Card 7: Generic CLI Is Not Reading `AGENTS.md`

User problem: a generic CLI agent ignores the project binding.

Copyable prompt:

```text
Check whether this CLI agent has actually loaded root `AGENTS.md`. If not, report that the runtime must be given the file contents or started in a mode that reads project instructions. Do not create Claude Code settings for a generic CLI setup.
```

Expected checks:

- root `AGENTS.md` exists;
- protected AgentPal block exists once;
- `.agentpal/project.json` exists;
- runtime behavior confirms whether instructions were loaded.

Should-not behavior:

- do not create `.claude/` files for a generic CLI;
- do not claim the adapter is validated without runtime evidence.

## Card 8: Roots Are Confused

User problem: the runtime reads AgentPal files as if they are the user's project.

Copyable prompt:

```text
Audit root separation. Report `active_project_root`, `agentpal_workspace_root`, current directory, and which root should be used for user project source inspection. Then stop unless a fix is clearly bounded to the binding files.
```

Expected checks:

- current directory;
- `.agentpal/project.json`;
- root instruction blocks;
- any report text that lists AgentPal as a project root.

Should-not behavior:

- do not scan both roots as project source;
- do not call AgentPal the user project unless explicitly working on AgentPal itself.

## Card 9: Leftover Block After Remove

User problem: AgentPal was removed but the runtime still loads AgentPal instructions.

Copyable prompt:

```text
Check for leftover AgentPal protected blocks in root instruction files and leftover `.agentpal/` binding files. Report exact locations and remove only AgentPal-owned blocks after confirmation.
```

Expected checks:

- `AGENTS.md`;
- `CLAUDE.md`;
- `.agentpal/`;
- `.claude/settings.local.json` for leftover additional directory entry.

Should-not behavior:

- do not delete user-authored instruction content;
- do not delete the AgentPal Workspace.

## Card 10: Project Not Reading New Rules After AgentPal Update

User problem: AgentPal was updated, but an external project still follows old behavior.

Copyable prompt:

```text
Check whether this project has a thin binding or copied old rules. Confirm the protected blocks point to core gate paths in the AgentPal Workspace. If they embed long old rule bodies, recommend upgrading the binding to thin form.
```

Expected checks:

- protected block length and content shape;
- `read_core_from_agentpal_workspace`;
- `core_gate_paths`;
- AgentPal Workspace core files readable.

Should-not behavior:

- do not paste a new full core gate body into the project;
- do not mark old copied rules as authoritative.

## Card 11: Path With Spaces Or Non-ASCII Characters

User problem: binding fails when paths contain spaces or non-ASCII characters.

Copyable prompt:

```text
Verify path handling without changing files. Read `.agentpal/project.json` as JSON, report the exact recorded roots, and check the required files through those paths. Do not split the path on spaces or rewrite characters.
```

Expected checks:

- JSON parsing;
- exact root strings;
- required file reads;
- Claude Code additional directory entry when applicable.

Should-not behavior:

- do not manually escape by guessing;
- do not replace paths with partial directory names.

## Card 12: Confirm This Project Is Thin-Bound

User problem: user wants proof the project is not a copied AgentPal workspace.

Copyable prompt:

```text
Confirm whether this project is thin-bound to AgentPal. Check `.agentpal/project.json`, root AgentPal blocks, and whether `.agentpal/` contains only binding files. Report any copied Pal Packs, docs, examples, evals, or long protocol bodies as failures.
```

Expected checks:

- `.agentpal/project.json`;
- `.agentpal/AGENTPAL.md`;
- root protected blocks;
- absence of copied Pal Packs, docs, examples, evals, release material, and long protocol bodies.

Should-not behavior:

- do not treat copied files as a stronger install;
- do not remove business files while checking.
