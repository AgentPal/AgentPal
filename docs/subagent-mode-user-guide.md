<!-- Future design only. Not active in AgentPal v0.1 runtime. / 未来设计，仅作规划参考，不属于 AgentPal v0.1 当前运行行为。 -->

# Future Runtime Orchestration User Guide

This document is retained only as future design material.

AgentPal v0.1 does not use this guide during current task handling. Current behavior is Simple Pal Mode only.

## Current User Expectation

In AgentPal v0.1:

- Mira receives ordinary messages.
- Mira routes owned work by AI judgement.
- The owner Pal answers immediately in the same response.
- No separate runtime workflow is started or claimed by AgentPal.
- No runtime-mode metadata is shown in normal answers.

## Future Direction

A later AgentPal version may design an orchestration layer that coordinates child workflows or external execution runtimes. That layer needs a separate permission model, evidence model, timeout/cancellation model, privacy boundary, and user-facing explanation before it becomes active.

Until that design exists, users should evaluate AgentPal v0.1 by whether Simple Pal Mode routes to the correct Pal and uses the correct Pal assets.

