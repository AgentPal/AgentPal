<!-- Future design only. Not active in AgentPal v0.1 runtime. / 未来设计，仅作规划参考，不属于 AgentPal v0.1 当前运行行为。 -->

# Future Child Workflow Concurrency Policy

AgentPal v0.1 does not start parallel child workflows and does not manage workflow concurrency.

Current behavior:

- Simple Pal Mode only.
- Same-response owner Pal handoff.
- No workflow discovery, spawning, waiting, closing, batching, or retry policy in normal task handling.

Future orchestration may define concurrency limits, batching rules, timeout handling, cancellation, cost controls, and close/cleanup evidence. Those rules are intentionally inactive in v0.1.
