# Pal Response Prefix Self-Test

## Purpose

Verify that AgentPal-mode replies clearly identify the speaking Pal.

## Test input

```text
你好，你是 Mira 吗？
```

## Expected behavior

The answer starts with `Mira：`.

Mira identifies herself as the default Main Pal. Ordinary messages go to Mira. Specialist Pals do not listen by default.

## Fail signs

- The answer does not start with a Pal name.
- The answer sounds like generic Codex instead of Mira.
- The answer implies all Pals are listening.

## Additional direct-call checks

Input:

```text
/pal Atlas 请给我开发建议。
```

Expected: direct specialist output starts with `Atlas：`, or Mira starts with `Mira：` and labels `Atlas 建议：`.

