<!-- Future design only. Not active in AgentPal v0.1 runtime. / 未来设计，仅作规划参考，不属于 AgentPal v0.1 当前运行行为。 -->

# Future Child Workflow Result Collection

AgentPal v0.1 does not collect results from child workflows during current task handling.

Current result handling is Simple Pal Mode only:

- Mira routes owned work by AI judgement.
- The owner Pal answers immediately in the same response.
- Multi-Pal input, when useful, is represented as labeled Pal sections in the current conversation.
- Normal answers do not show workflow ids, wait status, close status, or mode metadata.

Future orchestration may define a result collection record for child workflows, including ownership, assets read, output contract use, evidence, timeout status, close status, and unresolved conflicts.
