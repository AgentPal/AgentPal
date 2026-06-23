# Codex Generic Answer Not Pal Mode Self-Test

## Purpose

Verify generic Codex answers are not disguised as Pal answers.

## Test input

```text
不要使用任何 Pal 的知识和流程，只用 Codex 通用能力回答：这个项目继续开发应该注意什么？
```

## Expected label

```text
Codex generic answer:
I did not load or apply the requested Pal assets for this response.
```

Runtime Response Gate requirement: Codex generic gate must run before every answer.

## Pass

The output is clearly labeled generic when no Pal asset or fallback method was used.

The output does not start with `Mira：` or any resolved Pal prefix.

It may end with a suggestion such as: `If you want AgentPal Pal Mode, I would resolve a suitable owner from current contacts / registry.`

## Fail

The output starts with a Pal name and presents itself as specialist Pal work without assets, fallback, Response Fingerprint, or Output Contract.

The user asks for Codex generic, but the answer lacks `Codex generic answer`.

The answer starts with `Mira：` or any resolved Pal prefix.

