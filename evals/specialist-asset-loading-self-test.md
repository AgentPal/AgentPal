# Specialist Asset Loading Self-Test

## Purpose

Verify that specialist Pals load assets before specialist judgment and report fallback when assets are missing.

## Test input

```text
设计一个 html 页面。
```

## Expected behavior

- owner Pal = Atlas.
- Atlas loads Level 0 identity assets: `PAL.md`, `pal.json`, `SKILL.md`.
- Atlas checks relevant indexes when present.
- Atlas reads the most relevant 1-3 assets when available.
- If no dedicated HTML asset exists, Atlas reports Knowledge gap and fallback method.
- Repeated task record belongs to `pals/Atlas-developer/learning/`.

## Fail signs

- Mira handles the whole owned task.
- No owner Pal is named.
- Missing assets are treated as failure.
- A missing asset is claimed as used.
- Learning goes into Mira instead of Atlas.

