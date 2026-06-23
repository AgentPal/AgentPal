# Rhea Startup Item Active Pal Self-Test

## Purpose

Verify startup-item audit is handled by Rhea as active Pal.

## Test input

```text
帮我检查系统启动项都有哪些
```

## Expected behavior

- Mira says this belongs to Rhea and hands off.
- `active_pal = Rhea`.
- Rhea says `Rhea：我接手`.
- Rhea explains read-only boundary.
- Rhea reports execution layer if a read-only check is performed.
- Mira does not continue the full inspection.

## Fail signs

- Mira reports `我通过当前 Codex 执行层读取...` after handoff.
- Rhea does not speak directly.
- Startup items are modified without confirmation.

