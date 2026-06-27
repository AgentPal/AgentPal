# Specialist Advice AI-Judged Owner Self-Test

## Purpose

Verify that Mira uses AI routing judgement for specialist advice instead of answering it herself or applying a fixed owner map.

## Test input

```text
如果这个项目继续开发，你会给我一些专业建议
```

## Expected behavior

- Mira starts with `Mira：`.
- Mira decides case-by-case whether a registered owner Pal exists.
- If Mira selects an owner Pal, the selection reason must cite the current request and available context, not a keyword or default owner table.
- Mira hands off and stops as active speaker.
- Mira route output is max 2 short sentences.
- Owner Pal starts immediately with `{Owner}：我接手`.
- Any consultant or reviewer Pal is selected case-by-case by the active owner or coordinator.
- The selected owner follows its own `workspace/resources/response-fingerprints/{Owner}.md` when present.
- The selected owner uses its own output contract.
- The selected owner uses at least one Pal asset or explicit fallback method.
- If no Pal asset or fallback method is used, the answer is labeled `Codex generic answer`.

## Fail signs

- Mira says `我的专业建议是...`.
- Mira gives the full product, development, or quality advice herself.
- Mira outputs more than 2 short sentences.
- Mira outputs a numbered or bullet professional plan.
- Mira says the task goes to a Pal because of a fixed domain, keyword, or default owner rule.
- No owner Pal takes over.
- Owner Pal does not answer immediately.
- Mira hosts the whole workflow.
- The owner Pal only changes the speaker name without Response Fingerprint, Output Contract, or asset/fallback proof.

