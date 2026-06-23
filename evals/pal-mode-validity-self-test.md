# Pal Mode Validity Self-Test

## Purpose

Verify that `/pal Name` creates file-driven Pal work mode, not name-only roleplay.

## Test input

```text
/pal Atlas 帮我制定开发计划
```

## Expected behavior

- Output starts with `Atlas：`.
- Output follows `response-fingerprints/Atlas.md`.
- Output uses `pals/Atlas-developer/core/output-contract.md`.
- Output names or internally tracks at least one Atlas asset or fallback method.
- Output includes a light work-method statement.
- `codex_generic_answer: false`.

## Fail signs

- only speaker name changed
- no Response Fingerprint
- no Output Contract
- no asset or fallback method
- no work-method statement
- claims a missing asset was used
- fake Pal name-only response fails

