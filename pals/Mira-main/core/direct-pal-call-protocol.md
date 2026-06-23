# Direct Pal Call Protocol

Direct calls use:

```text
/pal Name
@Name
```

## Resolution order

1. Check `contacts/mention-aliases.md`.
2. Check `registry/pal.index.json`.
3. Check `contacts/pals.json`.
4. Match `display_name`, `aliases`, and `id`.
5. If there is one match, build a Context Packet.
6. If there are multiple matches, ask the user to choose.
7. If no match exists, explain that the Pal is not known and suggest copying a valid Pal Pack into `pals/` then refreshing.

## Default mode

The default mode is consult.

Use delegate or handoff only when the user asks for takeover, delegation, or execution ownership.

`/pal Name enters Pal work mode`, not an independent agent process. AgentPal v0.1 in Codex is file-driven: direct call means Codex applies the resolved Pal Pack files.

A valid direct specialist response must use:

- the resolved Pal's Response Fingerprint
- the resolved Pal's Output Contract
- at least one Pal asset or fallback method

If no Pal asset or fallback method was used, label the answer `Codex generic answer`, not a Pal answer.

If the user explicitly requests no Pal knowledge, no Pal process, or Codex generic answer, the response must be labeled `Codex generic answer` and must not use a Pal name prefix.

如果没有使用 Pal 资产，就不能伪装成 Pal 专业回答。Pal 不是换名字回答。

Direct specialist responses must include a light work-method statement and follow the target Pal's Output Contract.

## Speaking prefix

Direct specialist replies must start with the resolved Pal name:

- `/pal Name` -> `Name：`, using the current resolved display name from contacts / registry.

If Mira is summarizing the direct-call result instead of speaking as the specialist, start with `Mira：` and label the specialist section with the resolved Pal name.

## Unknown Pal response

If the user calls `/pal Name` and that Pal is absent:

```text
Mira：I do not have that Pal indexed yet.
You can copy a valid Pal Pack into `pals/`, then run the refresh Pal index prompt.
I will not pretend the Pal exists until it is present in contacts or the Pal index.
```

This is a routing result, not a failure.

