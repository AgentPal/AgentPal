# Fake Pal Response

This is a failure example, not a routing rule.

## Bad user/assistant exchange

User:

```text
/pal Atlas 帮我看这个开发任务。
```

Assistant:

```text
Atlas：我觉得可以分三步做。
```

## Why it is wrong

The answer only changed the speaker name. It did not use Atlas assets, Response Fingerprint, Output Contract, or an explicit fallback method.

## Correct behavior

Atlas must load or cite the required Pal assets, use Atlas's output contract, and state its work method. If no Pal asset or fallback was used, the answer must be labeled `Codex generic answer`, not `Atlas：`.

## Related eval

- `evals/pal-mode-validity-self-test.md`
- `evals/pal-asset-usage-proof-self-test.md`

## Related protocol

- `orchestration/pal-mode-validity-protocol.md`
- `templates/asset-usage-proof/asset-usage-proof-template.md`

