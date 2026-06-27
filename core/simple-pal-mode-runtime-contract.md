# Simple Pal Mode Runtime Contract

AgentPal active task handling is host-runtime executed and no-code governed. Simple Pal Mode remains the conservative default path.

## Current Practical Patterns

Current v0.1 patterns:

- Fast Route for clear single-owner tasks
- Single Owner answer with immediate owner Pal response
- compact Task Package
- staged Task Package for composite deliverables

## Future Design Only

The following are not active v0.1 behavior:

- Deep Conductor execution
- Subagent Mode as AgentPal behavior
- parallel child workflows
- external Agent orchestration
- multi-runtime automatic scheduling
- MCP-hosted Agent execution

Future design documents may exist in the repository, but they do not activate current runtime behavior.

## Runtime Boundary

Runtime can read files, write files, run commands, call tools, render outputs, and produce evidence when available and permitted.

Runtime is not a Pal. Runtime does not replace Pal identity, owner judgement, output contracts, or stage ownership.

When real execution happens, the active Pal reports which execution layer produced the evidence.
