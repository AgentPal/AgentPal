# Direct Pal Call

Use `/pal Name` or `@Name`.

Known official calls are resolved from contacts / registry. The list below is a current official display, not a separate source of truth:

```text
/pal Mira
/pal Atlas
/pal Vega
/pal Rhea
/pal Quinn
/pal Morgan
/pal Harper
/pal Nova

```

Direct calls default to consult mode unless the user explicitly asks for handoff or delegation.

## Pal Work Mode

`/pal Name enters Pal work mode`, not an independent agent process.

AgentPal v0.1 in Codex is file-driven. A direct Pal call is valid only when Codex applies that Pal's identity, Response Fingerprint, Output Contract, and at least one Pal asset or fallback method.

If no Pal asset or fallback method was used, the result must be labeled `Codex generic answer`, not a Pal answer.

如果没有使用 Pal 资产，就不能伪装成 Pal 专业回答。Pal 不是换名字回答。

Users call by display name, not directory name:

```text
/pal Atlas
```

not:

```text
/pal Atlas-developer
```

If a Pal name is unknown, Mira should check `contacts/pals.json` and `registry/pal.index.json`, report that the Pal is missing, and avoid inventing the Pal.

Individual Pal Packs must not keep separate direct-call lists for other Pals. Adding, removing, or renaming a Pal should mainly update contacts / registry.

## Simple Pal Mode

Direct `/pal Name` calls use Simple Pal Mode by default. This is the lightweight path for one Pal, one task, and lower token cost.

AgentPal v0.1 uses Simple Pal Mode only. Direct Pal calls do not start a separate runtime process. If several Pals are useful, Mira or the owner Pal coordinates them through same-response Pal handoff and clearly labeled sections.

