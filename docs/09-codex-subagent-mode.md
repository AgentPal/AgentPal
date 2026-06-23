<!-- Future design only. Not active in AgentPal v0.1 runtime. / 未来设计，仅作规划参考，不属于 AgentPal v0.1 当前运行行为。 -->

# Codex Subagent Mode

Codex Subagent Mode is future orchestration design material. It is not active in AgentPal v0.1.

AgentPal v0.1 uses Simple Pal Mode only. Mira routes owned work by AI judgement, and the owner Pal answers immediately in the same response.

User-friendly wording:

- Simple Pal Mode: the current conversation answers using one Pal's working style.
- Future Codex Subagent Mode: a possible later design where Codex sends separate child workflows to different Pals, then Mira collects and summarizes their results.

## What It Is

Future Codex Subagent Mode may use Codex child workflows. It would not be an OS-level background process, daemon, non-Pal runtime, or Pal contact.

Subagent Pal identities and asset paths are resolved from the current contacts / registry and `registry/pal-subagent-map.*`. Generic subagent prompts must not hard-code task types to specific Pals. Pal-specific subagent prompts are valid only after that Pal has already been selected.

Historical workflow tool names from earlier validation:

- `multi_agent_v1.spawn_agent`
- `wait_agent`
- `close_agent`

## Tool Discovery

No tool discovery is part of AgentPal v0.1 task handling.

Future orchestration design may need a clear permission model, discovery rule, evidence model, timeout/cancellation model, privacy boundary, and user-facing status model before child workflow tools can become active.

## When To Consider

In a future version, orchestration might be considered when AI judgement finds that independent specialist perspectives would materially improve the current case. These are possible usefulness signals, not triggers:

- multi-Pal collaboration
- owner Pal / consultant Pal / reviewer Pal separation
- parallel review
- release readiness
- questions that may need separate value, implementation, and acceptance views
- cases where Simple Pal Mode may blur Pal roles

AgentPal v0.1 does not use child workflows for these cases. It keeps the interaction in Simple Pal Mode.

Future example only:

```text
Mira：
这个任务适合多 Pal 并行。未来编排层可先从 contacts / registry 解析合适的 owner、consultant 和 reviewer，再分别处理并汇总。
```

## Mira's Role

In the future design, Mira may coordinate and summarize:

1. Decide whether Subagent Mode is appropriate.
2. Choose owner Pal, consultant Pal(s), and reviewer Pal(s).
3. Generate bounded subagent prompts.
4. Start child workflows when supported and authorized.
5. Wait for results.
6. Close completed workflows.
7. Collect and synthesize results.

Future orchestration would need runtime evidence such as:

- workflow id returned by a start operation
- `wait_agent` completion status
- `close_agent` previous status
- whether completed agents were closed

Mira does not rewrite specialist conclusions into a generic answer.

## Specialist Pal Role

Each future specialist child workflow would need to:

- read required Pal assets from the slim embedded Pal module structure
- use its Response Fingerprint
- use its Output Contract
- stay inside its professional boundary
- return structured results
- report `assets_read`
- report risks and evidence

Official bundled specialist Pals no longer carry standalone contacts, registry, runtime, models, plugins, or orchestration folders. Future child workflow prompts should point to the Pal's real embedded assets such as `PAL.md`, `AGENTS.md`, `SKILL.md`, `pal.json`, `core/output-contract.md`, `core/capability-reference.md`, `identity/`, `knowledge/`, `skills/`, `workflows/`, `runbooks/`, and `learning/`.

## Cost And Limits

Future orchestration would have higher token cost than Simple Pal Mode. It may also have thread or workflow limit constraints.

Completed child workflows should be closed after results are collected.

## Fallback

AgentPal v0.1 has no active fallback path from child workflows because child workflows are not part of current task handling. The current behavior is already Simple Pal Mode.

## Current Release Status

In v0.1, Codex Subagent Mode is not active. Do not discover, call, or describe child workflow tools during normal AgentPal task handling.



