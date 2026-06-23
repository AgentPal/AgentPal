<!-- Future design only. Not active in AgentPal v0.1 runtime. / 未来设计，仅作规划参考，不属于 AgentPal v0.1 当前运行行为。 -->

# Future Child Workflow Fallback Policy

AgentPal v0.1 has no active fallback path from child workflows because child workflows are not part of current task handling.

Current behavior is already Simple Pal Mode:

- Mira judges ownership case by case.
- Mira hands off owned work to the selected Pal.
- The selected Pal answers immediately in the same response.
- Normal answers must not show mode metadata, child workflow status, or fallback markers.

This file is retained only to preserve future design notes. Future orchestration may need fallback rules for unavailable child workflows, limits, timeouts, and user cost preferences, but those rules are not active in v0.1.
