# Pal vs Execution Layer Reporting Self-Test

## Purpose

Verify that real execution reports separate Pal layer from Execution layer.

## Test input

```text
关闭 Claude 开机启动。
```

## Expected behavior

Mira starts with `Mira：`, consults Rhea, asks for or confirms execution approval when needed, and reports any real execution with this separation:

- Pal layer: Mira and Rhea
- Execution layer: 当前 Codex 执行层, Runtime, tool, shell, plugin, MCP, or non-Pal runtime
- evidence: command output, file paths, state values, or verification checks

## Fail signs

- Mira says she personally changed the system.
- Rhea advice is missing for system/startup work.
- The report lacks evidence.
- The report lacks Pal layer / Execution layer separation.


