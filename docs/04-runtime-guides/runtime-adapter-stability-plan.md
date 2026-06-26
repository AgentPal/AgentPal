# Runtime Adapter Stability Plan

This plan defines the v0.2 regression surface for AgentPal runtime adapter behavior. Runtime adapters are thin bootstraps. They do not own AgentPal rules and should point back to shared core gates.

## Goals

- Keep Codex workspace initialization stable.
- Keep Claude Code project-first install stable.
- Keep generic CLI thin binding stable.
- Preserve `active_project_root` vs `agentpal_workspace_root`.
- Ensure core gate updates propagate through thin binding.
- Avoid stale copied Pal rosters in external projects.

## Covered Paths

### Codex Workspace Mode

Expected:

- user opens AgentPal Workspace directly;
- runtime reads root `AGENTS.md`, core gates, contacts/registry, and Mira minimum assets;
- current context is AgentPal Workspace, not an external project.

Evidence:

- initialized response starts with `Mira：`;
- contacts/registry list current official Pals;
- no external project root is invented.

### Claude Code Project-First Install

Expected:

- user starts in `<your-project>`;
- one-prompt install creates or updates thin project binding;
- local settings remain local configuration.

Evidence:

- `.agentpal/project.json`;
- protected `CLAUDE.md` / `AGENTS.md` blocks as applicable;
- `.claude/settings.local.json` only when needed and not committed.

### Generic CLI Thin Binding

Expected:

- project-local `AGENTS.md` and `.agentpal/` point to AgentPal core gates;
- no Claude Code settings dependency.

Evidence:

- `.agentpal/project.json`;
- root `AGENTS.md` protected block;
- current project stays the active project.

## Regression Themes

- existing binding upgrade;
- remove and reinstall;
- Pal list refresh from contacts/registry;
- core gate propagation;
- project-root separation;
- failed install troubleshooting;
- no full rule body copy;
- no full Pal roster copy as source of truth.

## No-Code Boundary

This plan does not add adapter code, installers, daemons, scanners, validators, or UI. It only documents and tests prompt/binding behavior.

## Acceptance

Adapter behavior is stable when the regression suite passes for the documented paths and all failed or not-run checks are reported honestly.
