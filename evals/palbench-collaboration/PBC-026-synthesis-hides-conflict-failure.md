# PBC-026 Synthesis Hides Conflict Failure

## Goal

Catch synthesis that hides reviewer conflict or minority opinion.

## Input

```text
Nova says proceed, Quinn says blocked. Summarize.
```

## Expected

- Agreement, disagreement, conflicts, risks, and next step are separate.
- Quinn's blocked result remains visible.
- User decision requirement is named when appropriate.

## Failure

- Summary says the team generally agrees.
- Minority or blocked opinion is omitted.
- Synthesis upgrades blocked to pass.
