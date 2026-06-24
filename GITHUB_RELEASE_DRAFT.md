# AgentPal v0.1.0-rc.1

AgentPal v0.1.0-rc.1 is a release candidate for the AgentPal Workspace and Pal Pack Standard practice.

AgentPal is a Markdown / JSON / protocol Pal layer for existing agent runtimes. It provides Pal identity, public knowledge, skills, context rules, memory boundaries, output contracts, coordination rules, verification habits, summaries, and learning storage.

It is not an Agent layer, not a multi-agent runtime, and not an execution layer.

## What's Included

- AgentPal Workspace root files for initialization and release-safe navigation.
- Simple Pal Mode as the only active task-handling path in v0.1.0-rc.1.
- Shared `core/` gates for Codex, Claude Code, generic CLI, and project-bound runtime adapters.
- Mira as the default Main Pal, Leader Pal, Conductor, and Pal team leader and coordinator.
- Official bundled Pal Packs: Mira, Atlas, Vega, Rhea, Quinn, Morgan, Harper, and Nova.
- Contacts and registry files as the source of truth for Pal discovery and `/pal Name` direct calls.
- Runtime Response Gate, AI routing judgement, Pal context slicing, asset loading budget, memory boundary, and Task Package output contract protocols.
- Thin project binding contracts that point external projects back to the AgentPal workspace instead of copying full rules.
- Fast Route as the current clear-task handoff pattern, with Deep Conductor documented as future complex-workflow design only.
- R33 small-sample PalBench smoke validation for observed workflow benefits.
- Public-safe release evidence under `release/v0.1.0-rc.1/`.
- External project workgroup templates and one-prompt setup prompts for Markdown/JSON-capable runtimes.
- MIT License, contribution guidance, release notes, checklist, manifest, and documentation navigation.

## Current Status

- Release type: release candidate.
- Version: `v0.1.0-rc.1`.
- Runtime path: Simple Pal Mode only.
- Required AgentPal runtime dependencies: none.
- Local tag evidence observed during documentation review: `v0.1.0-rc.1`.
- Local tagged commit: verify with `git rev-list -n 1 v0.1.0-rc.1` before publishing.
- Remote status observed during the local gate: `origin https://github.com/AgentPal/AgnetPal.git` is configured; push has not been performed by this draft.
- GitHub Release status: this draft is for manual publication; an online GitHub Release should not be considered created until maintainers publish it from the intended tag.

Maintainers should verify the final commit, tag, remote, and release page before publication.

## R33 PalBench Boundary

R33 PalBench is six-sample smoke validation. It compares AgentPal-style usage workflows with baseline usage conditions for task clarity, verification awareness, context-scope control, user routing burden, routing-record reuse, and current/future workflow boundaries.

It is not statistically significant. It is not an underlying-model benchmark. It does not prove broad performance improvement across all tasks.

Safe claim:

```text
In a six-sample smoke validation, AgentPal showed observed benefits for task clarity, verification awareness, context-scope control, user routing burden, reusable routing records, and clear current/future workflow boundaries.
```

## Known Limitations

- AgentPal does not include a desktop app, web UI, CLI runtime, daemon, scanner, validator, installer, or service.
- AgentPal does not execute filesystem, system, publishing, account, or automation actions by itself.
- Host runtimes and user-controlled tools perform actual execution and must provide evidence.
- Active multi-agent runtime behavior is not included.
- Active Subagent Mode, remote-agent orchestration, and active Deep Conductor execution are not included in v0.1.0-rc.1.
- Capability Inventory, Context Access List, Workflow Topology, Routing Reward Memory, expanded PalBench, and Deep Conductor materials are design foundations unless a future release activates them.
- Exact token metering is not provided in v0.1.0-rc.1.
- Pal Packs are working assets for a runtime, not independent agent processes.
- Private user memory, private project state, customer data, secrets, credentials, internal development notes, and local absolute paths must not be published.

## Getting Started

1. Download or clone the AgentPal Workspace.
2. For Codex, open the AgentPal directory and paste `prompts/codex/initialize-agentpal-workspace.md`.
3. For Claude Code, start from `<your-project>` and paste `prompts/claude-code/install-agentpal-current-project.md` after replacing `AGENTPAL_HOME`.
4. For a generic CLI Agent, start from `<your-project>` and paste `prompts/generic-cli-agent/install-agentpal-current-project.md` after replacing `AGENTPAL_HOME`.
5. Start ordinary messages with Mira, or use `/pal Name` to call a registered Pal directly, for example `/pal Harper`.

## Safety Notes

- Treat `contacts/` and `registry/` as the source of truth for Pal discovery.
- Keep future designs clearly marked as future, not active v0.1.0-rc.1 behavior.
- Use synthetic or placeholder data in public examples and templates.
- Review release archives before publication to ensure ignored local runtime files are not included.

## License

MIT License. See `LICENSE`.
