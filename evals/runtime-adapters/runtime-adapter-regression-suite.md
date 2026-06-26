# Runtime Adapter Regression Suite

This suite is the v0.2 checklist for Codex, Claude Code, and generic CLI Agent thin binding behavior.

## RA-001 Codex Workspace Mode

Input: open AgentPal Workspace and initialize from `prompts/codex/initialize-agentpal-workspace.md`.

Expected:

- response starts with `Mira：`;
- reads shared core gates;
- uses contacts/registry as Pal source of truth;
- labels current context as AgentPal Workspace.

Failure modes:

- treats AgentPal as external project;
- loads all Pal Packs by default;
- skips Runtime Response Gate.

## RA-002 Claude Code Project-First Install

Input: start Claude Code inside an external user project and paste install prompt.

Expected:

- creates thin `.agentpal/` binding;
- preserves user project as active project;
- uses AgentPal workspace only as Pal source/reference.

Failure modes:

- copies full AgentPal rules;
- copies full Pal roster as source of truth;
- commits local settings.

## RA-003 Generic CLI Thin Binding

Input: run a Markdown/JSON-capable CLI Agent in an external project and paste generic install prompt.

Expected:

- updates project `AGENTS.md` and `.agentpal/`;
- does not depend on Claude Code settings;
- uses core gates from AgentPal workspace.

Failure modes:

- assumes `.claude/settings.local.json`;
- treats generic runtime as fully verified without evidence.

## RA-004 Existing Binding Upgrade

Input: project already has `.agentpal/` and protected instruction blocks.

Expected:

- preserves user content;
- updates only AgentPal-owned blocks;
- keeps `active_project_root` and `agentpal_workspace_root`.

Failure modes:

- overwrites user instructions;
- duplicates blocks;
- changes project root.

## RA-005 Remove / Reinstall

Input: remove AgentPal workgroup, then reinstall.

Expected:

- removal affects only AgentPal-owned blocks and `.agentpal/`;
- reinstall recreates thin binding;
- user project files are not deleted.

Failure modes:

- deletes project source;
- leaves stale roster;
- does not explain that current thread context may still contain old instructions.

## RA-006 Pal List Refresh

Input: contacts/registry changed in AgentPal workspace.

Expected:

- bound project reads current contacts/registry from AgentPal workspace;
- external `.agentpal/` does not become source of truth for Pal assets.

Failure modes:

- stale copied Pal list;
- looks only in project `.agentpal/` for portraits/assets.

## RA-007 Core Gate Propagation

Input: shared core gate changes.

Expected:

- adapter prompts point to `core/` gates;
- project bindings inherit behavior by reading AgentPal workspace.

Failure modes:

- independent copied gate body drifts;
- adapter contradicts core gate.

## RA-008 Root Separation

Input: user asks "read this project" in a bound external project.

Expected:

- reads `active_project_root`;
- does not list AgentPal workspace as a second project root;
- AgentPal workspace read is limited to Pal discovery and selected Pal assets.

Failure modes:

- scans AgentPal workspace as project source;
- reports two active roots.

## RA-009 Failed Install Troubleshooting

Input: install cannot access AgentPal workspace path.

Expected:

- reports exact blocker;
- no partial success claim;
- suggests path correction or permission check.

Failure modes:

- claims install succeeded;
- creates broken binding without warning.
