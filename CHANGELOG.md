# Changelog

All notable public changes to AgentPal are recorded here.

## v0.3.0-rc.1 - Unreleased

Release candidate for the v0.3 no-code orchestration prototype line.

### Deep Conductor E2E

- Added Deep Conductor E2E usage guidance, package template, synthesis report template, short user-facing summary, examples, failure examples, evals, and readiness assessment.
- Added a release-preparation integration matrix for Deep Conductor readiness.

### Multi-Pal Collaboration

- Added Context Packet, Context Access, `/pal Name`, and `@Pal` no-code collaboration protocols and prompt-card guidance.
- Clarified that direct calls and mentions remain plain-text AgentPal protocols unless a host Runtime implements native command support.

### Owner + Verifier

- Added evidence-based Owner + Verifier workflow, verifier context packet, verification result record, examples, failure cases, and evals.

### Parallel Independent Review

- Added isolated reviewer workflow, reviewer context packet, reviewer final report, synthesis summary, examples, failure cases, and evals.

### Project Conductor

- Added Deep Conductor Master Loop, Project Conductor workflow, project task map, next-round Runtime Task Package, and conductor decision record.

### Cross-Runtime Pal Memory

- Added Cross-Runtime Pal Memory, memory boundary protocol, Pal Project Memory Snapshot, Routing Memory Record, Runtime Skill Usage Memory Record, and continuation package.

### Runtime-installed Skill Orchestration

- Added Runtime Skill candidate decision, availability check, fallback package, Runtime Skill-aware Task Package, usage memory, examples, failures, and evals.
- Clarified that Runtime-installed Skills belong to the host Runtime and require current availability evidence.

### Token / Cost-aware Context Budget

- Added qualitative Context Budget protocol, Context Budget Plan, Context Usage Report, and prompt-shaping guidance.
- Clarified that Context Budget is not exact token metering or cost calculation.

### Real Runtime Replay / Gap Repair

- Added Deep Conductor real host Runtime replay report and replay gap analysis.
- Strengthened partial, unavailable, blocked, and not-run reporting in E2E packages, synthesis, Routing Memory, and subagent / external Agent handoff boundaries.

### PalBench Collaboration

- Expanded PalBench Collaboration to 87 qualitative no-code regression cases covering R51-R63 collaboration, E2E, replay, and gap-repair scenarios.

### Runtime Adapter Notes

- Updated runtime adapter contracts and public docs to keep host Runtimes as the execution layer and AgentPal as the no-code Pal layer.

### No-code Boundary

- Confirmed that v0.3.0-rc.1 is a release candidate, not a stable release.
- AgentPal still does not provide automatic execution, a CLI, app, service, scanner, validator, installer, daemon, database, token meter, cost calculator, automatic Subagent launch, automatic external Agent calls, or statistical benchmark proof.

## v0.2.0-rc.1

Release candidate for the v0.2 first-phase no-code Pal layer improvements.

### Added

- PalSmith end-to-end creation flows for a first professional Pal and a small AI team, using copyable Runtime Task Packages.
- Mira-first usage guides, prompt cards, task package templates, examples, and self-tests.
- Official Pal task example library covering all 9 bundled Pals, plus cross-Pal examples.
- Minimal Capability Inventory profiles as manual AI judgement inputs.
- PalBench Light as a 24-case qualitative release regression suite with scoring rubric.
- Runtime Adapter stability guidance, troubleshooting prompt cards, upgrade notes, and regression coverage for thin project binding.

### Clarified

- AgentPal remains a Markdown / JSON / protocol Pal layer for existing runtimes.
- Simple Pal Mode remains the active runtime policy.
- Deep Conductor, autonomous multi-agent runtime behavior, automatic capability probing, automatic Routing Reward Memory writeback, and statistical benchmark claims are not current v0.2 behavior.

## v0.1.0-rc.1

Initial public release candidate for AgentPal as a Pal layer and Pal Pack Standard practice.

### Added

- AgentPal Workspace root files for runtime initialization, Pal identity, and release-safe navigation.
- Simple Pal Mode as the only active task-handling path for v0.1.0-rc.1.
- Mira as the default Main Pal, Leader Pal, Conductor, and Pal team leader and coordinator.
- R32 Fast Route and Deep Conductor protocol split. Fast Route supports current Simple Pal Mode; Deep Conductor remains future design.
- R33 small-sample PalBench smoke validation report with cautious release-safe wording.
- Official bundled Pal Packs: Mira, Atlas, Vega, Rhea, PalSmith, Quinn, Morgan, Harper, and Nova.
- PalSmith as the official no-code Pal asset governance Pal, with Pal Pack files, docs, Runtime Task Package standard, task package templates, examples, Markdown evals, PalSmith delegation / handoff guidance, and release-scope review.
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
- PalSmith is releaseable only as Markdown/JSON Pal governance content; it is not a command, tool package, UI, scanner, validator, installer, importer program, exporter program, daemon, or runtime dependency.
- Private memory, private state, real reports, secrets, and internal development notes must not be published.
- `claude --add-dir` is an optional fallback / advanced path; Claude Code users can start from `cd <your-project>` and use the one-prompt install.
- Runtime adapter prompts should point to shared core gates rather than keeping independent copies of First Pal Gate, Deliverable-aware Task Judgement, or Pal roster rules.
