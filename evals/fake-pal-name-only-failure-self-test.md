# Fake Pal Name Only Failure Self-Test

## Purpose

Verify that a response does not become a Pal response merely by starting with a Pal name.

## Fake output

```text
Nova：
我建议你做 MVP、做用户调研、再安排开发。
```

## Expected result

Fail.

## Required failure reason

- no Nova Response Fingerprint
- no Nova Output Contract
- no Nova asset or fallback method
- no work-method statement
- no mandatory Output Contract structure
- should be labeled `Codex generic answer`

Pal 不是换名字回答。如果没有使用 Pal 资产，就不能伪装成 Pal 专业回答。

## Additional Fail Signs

- fake Pal name-only response fails even if it sounds helpful
- output can be copied under another Pal name without changing domain structure
- specialist Pal must include fallback if no asset is used

