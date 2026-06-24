# Changelog

All notable public changes to AgentPal are recorded here.

## v0.1.0-rc.1

Initial public release candidate for AgentPal as a Pal layer and Pal Pack Standard practice.

### Added

- AgentPal Workspace root files for runtime initialization, Pal identity, and release-safe navigation.
- Simple Pal Mode as the only active task-handling path for v0.1.0-rc.1.
- Mira as the default Main Pal, Leader Pal, Conductor, and Pal team leader and coordinator.
- R32 Fast Route and Deep Conductor protocol split. Fast Route supports current Simple Pal Mode; Deep Conductor remains future design.
- R33 small-sample PalBench smoke validation report with cautious release-safe wording.
- Official bundled Pal Packs: Mira, Atlas, Vega, Rhea, Quinn, Morgan, Harper, and Nova.
- Contacts and registry files as the source of truth for Pal discovery, aliases, and direct `/pal Name` calls.
- Runtime Response Gate, AI routing judgement rules, Pal context slicing, asset loading budget, memory summary loading, and Task Package output contract protocols.
- AgentPal orchestration methodology, PalBench design, and future-oriented Capability Inventory / Context Access List / Pal Isolation / Shared Memory / Routing Reward Memory protocols.
- Capability profile templates, orchestration templates, PalBench eval drafts, and orchestration examples.
- External project workgroup binding templates for connecting AgentPal to a user project without treating the AgentPal Workspace as that project.
- Shared AgentPal core gates under `core/` so Runtime adapters can use thin binding instead of duplicating full rules.
- Claude Code one-prompt project install prompts for project-local setup through `.agentpal/`, `CLAUDE.md`, `AGENTS.md`, and `.claude/settings.local.json`.
- Claude Code post-install Mira welcome output with fixed `Mira：` prefix, Main Pal / Leader Pal / Conductor identity, official Pal list, and Simple Pal Mode reminder.
- Generic CLI Agent one-prompt install prompts through `.agentpal/` and `AGENTS.md`.
- Runtime adapter thin binding examples and evals for Codex, Claude Code, and generic CLI consistency.
- Public release files: `CONTRIBUTING.md`, `RELEASE_NOTES.md`, `GITHUB_RELEASE_DRAFT.md`, `RELEASE_CHECKLIST.md`, `RESOURCE_INDEX.md`, `THIRD_PARTY_NOTICES.md`, and MIT `LICENSE`.

### Clarified

- AgentPal is a Pal layer, not an Agent layer, not a multi-agent runtime, and not an execution layer.
- Pal Packs are runtime-readable working assets, not independent agent processes.
- Future subagent, remote agent, MCP-hosted agent, desktop app, marketplace, and runtime-adapter ideas are not active in v0.1.0-rc.1.
- Future Deep Conductor, capability inventory probing, routing memory writeback, and PalBench claims are design foundations, not active runtime behavior.
- R32 clarifies the current/future boundary: Fast Route is current, Deep Conductor is future-only.
- R33 PalBench observations are small-sample smoke evidence, not statistical benchmark claims and not underlying-model comparisons.
- Private memory, private state, real reports, secrets, and internal development notes must not be published.
- `claude --add-dir` is an optional fallback / advanced path; Claude Code users can start from `cd <your-project>` and use the one-prompt install.
- Runtime adapter prompts should point to shared core gates rather than keeping independent copies of First Pal Gate, Deliverable-aware Task Judgement, or Pal roster rules.
