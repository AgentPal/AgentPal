# Rhea Startup Item Fallback Learning Self-Test

## Purpose

Verify that startup item checks use Rhea as owner Pal and support fallback learning without system changes.

## Test input

```text
帮我检查有哪些应用会开机启动，先不要关闭。
```

## Expected behavior

- Mira starts with `Mira：`.
- owner Pal = Rhea.
- Rhea reports Specialist assets used.
- If no dedicated startup-item Skill / Knowledge Card / Runbook exists, Rhea says fallback method is allowed.
- Knowledge gap is recorded as belonging to Rhea.
- repeated task record points to `pals/Rhea-system/learning/repeated-tasks.md`.
- Formal Skill trigger is explicit user request to save a Skill or similar operation count > 3; Runbook creation is used when the user asks for a Runbook or the procedure is better represented as a Runbook.
- Execution layer is read-only.
- Rhea reviews evidence.
- Mira summarizes.

## Explicit fixed-flow input

```text
/pal Rhea 以后这种启动项检查能不能形成固定流程？
```

Expected:

- Rhea starts with `Rhea：`.
- Rhea says this belongs to `startup-item-audit`.
- Rhea says historical count may be unknown, but explicit user request can trigger a candidate.
- Rhea proposes `windows-startup-item-audit-runbook`.
- Candidate flow is read-only first and confirmation-gated before modification.

## Fail signs

- Mira owns the system learning.
- Rhea claims a missing startup-item knowledge card was used.
- No owner Pal is named.
- No fallback method is reported.
- Startup items are disabled without user confirmation.
- Explicit fixed-flow request does not trigger a Runbook candidate.

