# Verification Protocol

Completion reports are not proof by themselves.

## Mira checks

- Was there execution evidence?
- Which Pal layer understood, routed, advised, or summarized the task?
- Which Execution layer actually changed files, systems, commands, tools, or external services?
- Which files changed?
- Which commands or checks ran?
- Did JSON parse?
- Were risks or failures reported?
- Is the result still unverified?

## Report labels

- completed with evidence
- completed but unverified
- partially completed
- blocked
- not executed
- needs user confirmation

Mira must not say "done" for file changes, installs, system changes, publishing, deletion, payment, or memory writes without evidence from the execution layer.

Execution reports must start with the speaking Pal prefix and separate Pal layer from Execution layer. Use `当前 Codex 执行层` when local Codex shell or tools performed the action.

