# Runtime Adapter Regression Suite

This suite is the v0.2 checklist for Codex, Claude Code, and generic CLI Agent thin binding behavior. It is a Markdown regression suite, not an executable validator.

Scoring suggestion:

- `pass`: expected behavior is demonstrated with evidence;
- `warning`: behavior is usable but needs a clear manual step or session refresh;
- `fail`: behavior contradicts the thin binding contract or lacks evidence.

## RA-001 Codex Workspace Mode

Input: open AgentPal Workspace and initialize from `prompts/codex/initialize-agentpal-workspace.md`.

Expected:

- response starts with `Mira：`;
- shared core gates are read;
- contacts and registry are Pal source of truth;
- current context is labeled AgentPal Workspace;
- no external project binding is invented.

Failure modes:

- treats AgentPal as an external project;
- loads all Pal Packs by default;
- skips Runtime Response Gate.

## RA-002 Claude Code Project-First Install

Input: start Claude Code inside an external user project and paste `prompts/claude-code/install-agentpal-current-project.md`.

Expected:

- creates thin `.agentpal/` binding;
- preserves user project as `active_project_root`;
- uses AgentPal Workspace only as Pal source and core reference;
- merges `.claude/settings.local.json` without losing unrelated settings;
- welcome table is generated from current contacts and registry.

Failure modes:

- copies full AgentPal rules;
- copies full Pal roster as source of truth;
- commits local Claude Code settings.

## RA-003 Generic CLI Thin Binding

Input: run a Markdown/JSON-capable CLI Agent in an external project and paste `prompts/generic-cli-agent/install-agentpal-current-project.md`.

Expected:

- updates project `AGENTS.md` and `.agentpal/`;
- does not depend on Claude Code settings;
- uses core gates from AgentPal Workspace;
- reports whether the runtime actually loaded `AGENTS.md`.

Failure modes:

- assumes `.claude/settings.local.json`;
- treats generic runtime behavior as verified without evidence.

## RA-004 Existing Binding Upgrade

Input: project already has `.agentpal/` and protected instruction blocks from an older binding.

Expected:

- preserves user content outside protected AgentPal blocks;
- keeps correct `active_project_root` and `agentpal_workspace_root`;
- replaces copied rule bodies with thin pointers;
- marks old project-local roster material as non-authoritative.

Failure modes:

- overwrites user instructions;
- duplicates protected blocks;
- changes the user project root.

## RA-005 Remove And Reinstall

Input: remove AgentPal binding, then reinstall.

Expected:

- removal affects only AgentPal-owned blocks, `.agentpal/`, and the Claude Code additional directory entry when applicable;
- reinstall recreates thin binding;
- user project files are not deleted;
- report explains that the current runtime session may still remember old instructions.

Failure modes:

- deletes project source;
- leaves stale protected blocks;
- fails to preserve unrelated Claude Code settings.

## RA-006 Pal List Refresh Via Contacts And Registry

Input: contacts or registry changed in the AgentPal Workspace.

Expected:

- bound project reads current contacts and registry from AgentPal Workspace;
- external `.agentpal/` does not become source of truth for Pal assets;
- welcome or roster output is regenerated from current files.

Failure modes:

- stale copied Pal list;
- looks only in project `.agentpal/` for portraits, output contracts, or assets.

## RA-007 Core Gate Propagation

Input: shared core gate files change in the AgentPal Workspace.

Expected:

- adapter prompts point to `core/` gate paths;
- project bindings inherit behavior by rereading AgentPal Workspace;
- root instruction blocks stay short and pointer-based.

Failure modes:

- independent copied gate body drifts;
- adapter contradicts core gate;
- project-local long rules are treated as current.

## RA-008 Active Project Root Versus AgentPal Workspace Root

Input: user asks "read this project" in a bound external project.

Expected:

- routine project inspection uses `active_project_root`;
- AgentPal Workspace reads are limited to Pal discovery and selected Pal assets;
- report does not list AgentPal Workspace as a second active project root.

Failure modes:

- scans AgentPal Workspace as project source;
- reports two active roots;
- confuses user source files with Pal framework files.

## RA-009 Failed Install Troubleshooting

Input: install cannot access the AgentPal Workspace path.

Expected:

- reports exact blocker;
- makes no partial success claim;
- suggests path correction, permission correction, restart, or session directory addition as appropriate;
- leaves project files unchanged unless a safe partial write is explicitly reported.

Failure modes:

- claims install succeeded;
- creates broken binding without warning;
- scans unrelated folders looking for AgentPal.

## RA-010 Path With Spaces Or Non-ASCII Characters

Input: either root path contains spaces or non-ASCII characters.

Expected:

- paths are stored as JSON strings;
- required files are read through exact recorded paths;
- no path is split on spaces or normalized by guessing;
- Claude Code additional directory entry uses the same path string.

Failure modes:

- partial path is stored;
- manual escaping breaks file access;
- failure is hidden behind a success message.

## RA-011 Stale Binding Detection

Input: project has older `.agentpal/` content, copied Pal list, or long copied protocols.

Expected:

- old material is detected and reported;
- current contacts and registry are read from AgentPal Workspace;
- upgrade path points to `docs/04-runtime-guides/upgrade-existing-binding-to-thin-binding.md`.

Failure modes:

- old project cache is treated as current;
- copied rules override core gates;
- duplicate AgentPal blocks remain.

## RA-012 No Copied Full Rules

Input: inspect a freshly installed or upgraded binding.

Expected:

- `.agentpal/` contains only binding files;
- root instruction blocks point to AgentPal core gates;
- no full Pal Packs, docs, examples, evals, release material, or long protocol bodies are copied into the user project;
- no runtime helpers, services, installers, scanners, validators, or UI are created.

Failure modes:

- copied AgentPal Workspace appears under the user project;
- project-local rules become authoritative;
- extra runtime files are introduced.
