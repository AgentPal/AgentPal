# Specialist Pal Takes Over Self-Test

## Purpose

Verify that the target Pal owns its domain work after handoff.

## Test input

```text
关闭 Claude 开机启动。
```

Additional specialist advice input:

```text
帮我制定一个开发计划
```

## Expected behavior

- Mira identifies Rhea as target Pal.
- Mira hands off and stops.
- Rhea starts with `Rhea：我接手`.
- Rhea decides risk, confirmation, fallback, execution-layer coordination, evidence, and reporting.

## Fail signs

- Mira manages the full risk plan after handoff.
- Mira writes the development plan herself instead of handing off to Atlas.
- Mira claims execution-layer results while Rhea is active.
- Rhea is treated as only a section inside Mira's answer.

