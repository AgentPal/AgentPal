# Runtime Adapter Stability Guide

This guide explains how AgentPal should be connected to Codex, Claude Code, and generic CLI agents without turning the user project into a copy of the AgentPal Workspace.

AgentPal is a Markdown / JSON / protocol workspace. It is not an execution engine, an installer, or a background service. Runtime adapters are thin reading and binding patterns that help the current host runtime load the right Pal rules at the right time.

## Adapter Goal

A stable Runtime Adapter should:

- keep the user's real project as the active project;
- read AgentPal core gates from the AgentPal Workspace;
- read the current Pal list from `contacts/pals.json` and `registry/pal.index.json`;
- load Mira as the ordinary entry Pal;
- preserve Simple Pal Mode only;
- report exact evidence for reads, writes, and command results;
- avoid copying full AgentPal rules, Pal Packs, docs, examples, evals, or release material into the user project.

## Thin Binding Principles

A thin binding is a small local pointer from an external project to the AgentPal Workspace.

The project stores only:

- `.agentpal/project.json`;
- `.agentpal/AGENTPAL.md`;
- one protected AgentPal block in root `AGENTS.md`;
- one protected AgentPal block in root `CLAUDE.md` when Claude Code is used;
- `.claude/settings.local.json` only when Claude Code needs additional directory access.

The binding should point back to:

- `core/agentpal-core-gate.md`;
- `core/first-pal-gate.md`;
- `core/simple-pal-mode-runtime-contract.md`;
- `core/deliverable-aware-task-judgement-gate.md`;
- `core/main-pal-conductor-gate.md`;
- `core/runtime-adapter-shared-contract.md`;
- `core/project-binding-thin-contract.md`;
- `core/runtime-response-gate.md`;
- `contacts/pals.json`;
- `registry/pal.index.json`;
- `pals/Mira-main/PAL.md`;
- `pals/Mira-main/core/output-contract.md`.

The project should not become a second AgentPal Workspace.

## Supported Adapter Modes

### Codex Workspace Mode

Use this when AgentPal itself is opened as the current Codex workspace.

Expected behavior:

- current context is the AgentPal Workspace;
- initialization starts from `prompts/codex/initialize-agentpal-workspace.md`;
- ordinary messages start with Mira;
- the runtime reads the short initialization set instead of all Pals and all docs.

Codex workspace mode does not require a project-local `.agentpal/` binding because the current workspace already is AgentPal.

### Claude Code Project-First Mode

Use this when Claude Code is opened from inside the user's real project.

Expected behavior:

- `active_project_root` is the current project directory;
- `agentpal_workspace_root` is the separate AgentPal Workspace path supplied by the user;
- project files contain only the thin binding;
- `.claude/settings.local.json` includes the AgentPal Workspace path in `permissions.additionalDirectories`;
- Claude Code may need a restart or `/add-dir <path-to-AgentPal>` before it can read the AgentPal Workspace in the current session.

### Generic CLI Thin Binding Mode

Use this when a CLI agent can read Markdown / JSON project instructions but has no Claude Code local settings.

Expected behavior:

- project `AGENTS.md` contains the protected AgentPal block;
- `.agentpal/project.json` stores the two roots and core pointers;
- no `.claude/` files are created;
- the runtime gives honest evidence about which files it can read.

## Root Separation

`active_project_root` is the user's real project.

`agentpal_workspace_root` is the AgentPal Workspace used as a Pal source and core rule source.

In a bound external project:

- "this project" means `active_project_root`;
- normal source inspection stays inside `active_project_root`;
- AgentPal Workspace reads are limited to core gates, contacts, registry, Mira entry files, and selected Pal assets needed for the current task;
- reports should not list AgentPal as a second active project root.

If these roots become identical by accident, the binding should be rejected unless the user explicitly says they are working on AgentPal itself.

## Post-Install Files

After a successful project-first install, expect:

- `.agentpal/project.json` with `active_project_root`, `agentpal_workspace_root`, `runtime_hint`, `active_mode`, `read_core_from_agentpal_workspace`, `core_gate_paths`, and `pal_source_of_truth`;
- `.agentpal/AGENTPAL.md` explaining that the project is thin-bound to AgentPal;
- root `AGENTS.md` AgentPal protected block;
- root `CLAUDE.md` AgentPal protected block for Claude Code;
- `.claude/settings.local.json` for Claude Code only;
- `.gitignore` entry for `.claude/settings.local.json`.

## What Must Not Be Copied

Do not copy these into the user project as binding material:

- full Pal Packs;
- full Pal roster snapshots;
- full Mira assets;
- full core gates or orchestration protocols;
- AgentPal docs, examples, evals, release notes, or PalBench reports;
- optional `.agentpal/state`, `.agentpal/memory`, `.agentpal/reports`, `.agentpal/context`, or `.agentpal/index` folders;
- generated runtime helpers, background services, installers, or UI.

The binding may copy only the small project template files needed to point back to the AgentPal Workspace.

## Refresh Core Gates

When AgentPal is updated, existing project bindings should refresh by rereading the core gate paths from the AgentPal Workspace.

Recommended check:

1. Open `.agentpal/project.json`.
2. Confirm `read_core_from_agentpal_workspace` is true.
3. Confirm `core_gate_paths` points to current files under `core/`.
4. Confirm root `AGENTS.md` and `CLAUDE.md` protected blocks point to the core gates instead of embedding long copied rule bodies.
5. Restart or reload the host runtime if it keeps old instructions in memory.

## Refresh Pal List

The current Pal list comes from:

- `contacts/pals.json`;
- `registry/pal.index.json`.

If a bound project still shows old Pals:

1. Confirm the binding points to the correct AgentPal Workspace.
2. Confirm both source files are readable from that workspace.
3. Confirm no copied Pal roster in project files is being treated as authoritative.
4. Restart or reload the host runtime session if needed.

## Verify Install

Use the verification prompt for the target runtime:

- Claude Code: `prompts/claude-code/verify-agentpal-current-project.md`;
- Generic CLI: inspect `AGENTS.md`, `.agentpal/project.json`, and the AgentPal Workspace pointers manually using the same checklist.

Minimum verification:

- current directory is the user's project, not the AgentPal Workspace;
- `.agentpal/project.json` is valid JSON;
- the AgentPal Workspace path exists and contains the required core, contacts, registry, and Mira files;
- root instruction blocks exist once and point back to core gates;
- the Pal list is read from contacts and registry;
- Claude Code local settings include the AgentPal Workspace path when Claude Code is used;
- no copied full rules or Pal Packs exist in `.agentpal/`.

## Remove Binding

Removing a binding should affect only project-local AgentPal binding files:

1. Delete the project `.agentpal/` directory.
2. Remove only the protected AgentPal block from root `AGENTS.md`.
3. Remove only the protected AgentPal block from root `CLAUDE.md` when present.
4. For Claude Code, remove the AgentPal Workspace path from `.claude/settings.local.json` while preserving unrelated settings.
5. Keep all user-authored project files.
6. Do not delete the AgentPal Workspace.

After removal, restart or reload the runtime if it still remembers old project instructions.

## Troubleshooting FAQ

### Claude Code says install succeeded, but Mira does not welcome me

Check whether the session can read the AgentPal Workspace path. If not, restart Claude Code or use `/add-dir <path-to-AgentPal>` for the session, then rerun verification.

### `/pal Atlas` is treated as normal text

Check that the root instruction block says direct Pal calls are resolved from current contacts and registry. Then confirm the runtime has actually read `contacts/pals.json` and `registry/pal.index.json`.

### The project still shows an old Pal list

Look for copied roster text in root instruction files or `.agentpal/`. The authoritative list should be read from the AgentPal Workspace, not from a project cache.

### The runtime reads AgentPal files as project source

Recheck `.agentpal/project.json`. `active_project_root` must be the user project. AgentPal is only `agentpal_workspace_root`.

### Path names contain spaces or non-ASCII characters

Use exact paths as JSON strings in `.agentpal/project.json` and Claude Code settings. Do not split or normalize the path by hand. Verify by reading the specific required files.

### `settings.local.json` changed but Claude still cannot read AgentPal

Claude Code may keep directory permissions in session memory. Restart Claude Code or add the directory for the current session, then verify again.

## No-Code Boundary

Runtime Adapter stability is a documentation, binding, and verification contract. It should not introduce runtime code, generated scripts, package manifests, background processes, local scanners, validators, installers, daemons, or UI.

AgentPal remains a Pal layer. The host runtime performs actual reads, writes, tool calls, and commands, and must report evidence when it does so.
