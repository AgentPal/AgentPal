<!-- Future design only. Not active in AgentPal v0.1 runtime. / 未来设计，仅作规划参考，不属于 AgentPal v0.1 当前运行行为。 -->

# Subagent Unavailable Fallback

## User input

```text
让 Nova、Atlas、Quinn 分别评审这个版本计划。
```

## Future routing decision

In a future orchestration layer, Mira might attempt child workflows only if the runtime supports them and the user has authorized them.

## Subagents spawned

None in AgentPal v0.1. Current task handling is Simple Pal Mode only.

## Required files each subagent reads

No subagent files are read by independent threads. In fallback, Simple Pal Mode still requires the relevant Pal assets before each labeled Pal response.

## Expected result

```text
Subagent Mode unavailable
Using Simple Pal Mode
Limitations: specialist Pals are not independent Codex subagent threads in this response.
```

User-facing fallback wording:

```text
Mira：
当前环境没有可用 Subagent Mode，我会降级到 Simple Pal Mode。这意味着多个 Pal 不会是独立子线程，结果可能不如并行评审清晰。
```

## Mira synthesis

Mira explains the limitation and either asks whether to continue or proceeds with labeled Simple Pal Mode sections if the user did not require true subagents.

## Fallback if unavailable

This example is the fallback path.


