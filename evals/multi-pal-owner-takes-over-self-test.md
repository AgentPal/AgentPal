# Multi-Pal Owner Takes Over Self-Test

## Purpose

Verify that multi-Pal tasks are owned by one selected Pal, not hosted entirely by Mira, and that multi-Pal participation is chosen case-by-case.

## Test Input

```text
帮我判断这个功能值不值得做，并拆成开发任务，还要考虑风险。
```

Additional input:

```text
如果这个项目继续开发，你会给我一些专业建议
```

## Expected Behavior

Mira must use AI routing judgement and choose an owner with a current-context reason.

One valid response shape:

```text
Mira：
我判断这次更适合由 Nova 先接手，因为当前问题需要先确定价值和范围，再决定是否请其他 Pal 补充开发或验收视角。我请 Nova 接手。

Nova：
我接手。我按 Nova 的版本范围切分流程处理，先定目标，再收范围。
```

Then the owner Pal decides case-by-case:

- whether consultants are needed
- whether reviewers are needed
- whether additional Pal perspectives are useful
- whether evidence or execution layer is required

No fixed Pal set is required by semantic task wording alone.

## Fail Signs

- Mira keeps hosting every stage.
- Mira provides the full specialist advice herself.
- Mira outputs more than 2 short sentences.
- Mira outputs a numbered or bullet specialist plan.
- No owner Pal takes over.
- Owner Pal does not answer immediately after handoff.
- Consultants answer without owner coordination.
- Owner Pal has no work-method statement or Output Contract structure.
- The response says a fixed task phrase requires a fixed Pal set.


