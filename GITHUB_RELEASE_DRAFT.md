# AgentPal v0.2.0-rc.1

AgentPal v0.2.0-rc.1 is a release candidate for the first integrated no-code Pal layer improvements after v0.1.

AgentPal remains a Markdown / JSON / protocol Pal layer for existing agent runtimes. It is not an Agent runtime, not a multi-agent runtime, and not an execution layer.

## What's Included

- PalSmith end-to-end creation flows for a first professional Pal and a small AI team.
- Mira-first usage guides, prompt cards, task package templates, examples, and self-tests.
- Official Pal task examples for all 9 bundled Pals, plus cross-Pal examples.
- Minimal Capability Inventory profiles as manual AI judgement inputs.
- PalBench Light as a 24-case qualitative release regression suite with scoring rubric.
- Runtime Adapter stability and troubleshooting guidance, prompt cards, upgrade notes, and regression coverage for thin project binding.
- v0.2 readiness, capability summary, and integration matrix records.

## Current Status

- Release type: release candidate / pre-release.
- Version: `v0.2.0-rc.1`.
- Runtime path: Simple Pal Mode only.
- Required AgentPal runtime dependencies: none.
- GitHub Release should be created from tag `v0.2.0-rc.1`.

## Known Limitations

- AgentPal is not a desktop app, web UI, CLI runtime, daemon, scanner, validator, installer, or service.
- AgentPal does not execute filesystem, system, publishing, account, or automation actions by itself.
- Host runtimes and user-controlled tools perform actual execution and must provide evidence.
- Active Deep Conductor execution, autonomous multi-agent runtime behavior, remote-agent orchestration, and active Subagent Mode are not included.
- Capability Inventory profiles are manual illustrative judgement inputs, not automatic environment probing.
- Routing Reward Memory is not automatic writeback.
- PalBench Light is qualitative release regression, not statistically significant benchmark evidence and not a model comparison.
- PalSmith is not a CLI, scanner, importer, exporter, builder, installer, UI, daemon, or service.

## Getting Started

1. Download or clone the AgentPal Workspace.
2. For Codex, open the AgentPal directory and paste `prompts/codex/initialize-agentpal-workspace.md`.
3. For Claude Code, start from `<your-project>` and paste `prompts/claude-code/install-agentpal-current-project.md`.
4. For a generic CLI agent, start from `<your-project>` and paste `prompts/generic-cli-agent/install-agentpal-current-project.md`.
5. Start ordinary messages with Mira, or use `/pal Name` to call a registered Pal directly.

## Safety Notes

- Treat `contacts/` and `registry/` as the source of truth for Pal discovery.
- Keep future designs clearly marked as future, not active v0.2.0-rc.1 behavior.
- Use synthetic or placeholder data in public examples and templates.
- Do not publish private user memory, private project state, customer data, sensitive access material, internal development notes, or local absolute paths.

## Release Notes

This release should be marked as a pre-release. It should not be marked as the latest stable `v0.2.0` release.
