<!-- Future design only. Not active in AgentPal v0.1 runtime. / 未来设计，仅作规划参考，不属于 AgentPal v0.1 当前运行行为。 -->

# Future Codex Child Workflow Protocol

AgentPal v0.1 does not use Codex child workflows during current task handling.

Current runtime policy:

- Simple Pal Mode only.
- Mira routes owned work by AI judgement.
- The owner Pal answers immediately in the same response.
- No child workflow discovery, spawn, wait, close, or runtime-mode metadata is part of normal answers.

This file is retained only as historical and future design material. A later version may define an orchestration layer, but that design must first specify user authorization, evidence, privacy, timeout, cancellation, cost, and fallback rules.

Until then, use `orchestration/runtime-response-gate.md` and `orchestration/ai-routing-judgement-protocol.md` as the current runtime path.
