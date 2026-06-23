# Future Agent Orchestration

Future design only. Not active in AgentPal v0.1 runtime.

未来设计，仅作规划参考，不属于 AgentPal v0.1 当前运行行为。

## Current Boundary

AgentPal v0.1 is a Pal layer.

It is not an Agent layer, not a multi-agent runtime, and not an execution layer. The current runtime behavior is Simple Pal Mode only:

- Mira receives ordinary messages.
- Mira routes owned work by AI judgement.
- The owner Pal answers immediately in the same response.
- Pal assets, Output Contracts, fallback rules, evidence reporting, and Skill storage remain active.
- No child workflow, non-Pal runtime runtime, MCP-hosted Agent, or remote agent service is called by AgentPal v0.1 task handling.

## Future Scope

A later AgentPal design may add a separate runtime orchestration layer for:

- Codex child workflows
- Claude Code or CodeWhale delegated work
- MCP-hosted agent tools
- remote agent services
- independent reviewer execution
- bounded parallel task collection

That future layer must be designed as an execution/runtime adapter above the Pal layer. It must not blur the meaning of Pal.

## Pal Vs Agent

Pal:

- identity
- knowledge
- skills
- context
- memory boundary
- output contract
- review and summary habits
- learning and Skill storage

Agent / runtime:

- reads and writes files
- runs commands
- calls tools
- opens UIs
- performs network or system actions
- owns execution evidence

## Future Requirements

Before any future orchestration becomes active, AgentPal needs:

- explicit user-facing design
- clear permission model
- runtime capability detection that is not mixed into normal answers
- evidence schema for spawned work
- cancellation and timeout behavior
- privacy boundary for what context is shared
- result collection contract
- failure handling and cleanup
- documentation that separates current Pal behavior from runtime execution

Until that design exists, AgentPal v0.1 remains Simple Pal Mode only.


