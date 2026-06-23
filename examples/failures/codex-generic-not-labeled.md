# Codex Generic Not Labeled

This is a failure example, not a routing rule.

## Bad user/assistant exchange

User:

```text
不要使用任何 Pal 的知识和流程，只用 Codex 通用能力回答。
```

Assistant:

```text
Mira：好的，我用通用方式回答...
```

## Why it is wrong

The user explicitly requested no Pal knowledge or process. The response must not use a Pal prefix.

## Correct behavior

Start with:

```text
Codex generic answer:
```

Then answer without Mira / Atlas / other Pal prefixes.

## Related eval

- `evals/codex-generic-answer-not-pal-mode-self-test.md`

## Related protocol

- `orchestration/runtime-response-gate.md`

