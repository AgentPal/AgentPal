# Known Limitations

These limitations apply to AgentPal v0.1.0-rc.1.

## Runtime And Execution

- AgentPal is not an execution layer.
- AgentPal does not run commands, publish releases, modify systems, or perform account actions by itself.
- Host runtimes and user-controlled tools perform actual execution and must provide evidence.
- Simple Pal Mode is the only active task-handling path.
- Active Deep Conductor execution is not included.
- Active subagent or remote-agent orchestration is not included.

## Product Surface

- No desktop app.
- No web UI.
- No hosted Pal Hub.
- No marketplace.
- No required CLI, daemon, service, scanner, validator, installer, or background process.
- No enterprise permission system.
- No cloud memory sync.

## Validation

- R33 PalBench is six-sample smoke validation only.
- It is not statistically significant.
- It does not compare underlying model capability.
- It does not prove broad performance improvement across all tasks.

## Context And Memory

- Exact token metering is not provided in v0.1.0-rc.1.
- Context budgets and asset loading reports are defined as audit methods, not as exact runtime token measurement.
- Private user memory and private project state must not be published.
- Memory-like files remain high-risk and need release review.

## Future Design

Future design materials for Deep Conductor, Context Access Lists, Capability Inventory, Workflow Topology, Routing Reward Memory, PalBench expansion, and runtime adapters are included as design foundations only.

They should not be presented as active v0.1.0-rc.1 runtime behavior.
