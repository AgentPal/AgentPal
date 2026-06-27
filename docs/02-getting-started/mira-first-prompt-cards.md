# Mira-First Prompt Cards

These cards are copyable user prompts for daily AgentPal use.

## I Do Not Know Who To Ask

Copy:

```text
Mira，我不知道该找哪个 Pal。请先帮我判断这个任务应该怎么处理：<your task>
```

Expected Mira behavior:

- starts with `Mira：`;
- judges whether Mira can answer or should name an owner candidate;
- avoids fixed route tables.

Should not happen:

- Mira invents a Pal;
- Mira writes a specialist body after choosing a specialist.

## Help Me Break Down A Task

Copy:

```text
Mira，帮我把这个目标拆成阶段、候选 owner、需要的上下文和验收证据：<your goal>
```

Expected Mira behavior:

- identifies stages and candidates;
- marks candidates as non-fixed;
- names evidence required.

Should not happen:

- broad clarification before stage candidates;
- Runtime owns a material stage.

## Generate A Codex / Claude Code Task Package

Copy:

```text
Mira，请把这个目标整理成 Codex / Claude Code 可以执行的 Runtime Task Package：<your goal>
```

Expected Mira behavior:

- prepares goal, context, file scope, constraints, steps, acceptance, risks, and evidence;
- separates Pal owner judgement from runtime execution.

Should not happen:

- Mira claims execution;
- prompt copies full AgentPal rules into the project.

## Judge Whether A Specialist Pal Is Needed

Copy:

```text
Mira，请判断这个任务是否需要专业 Pal。如果需要，请说明候选 Pal 和原因：<your task>
```

Expected Mira behavior:

- uses the current central Pal roster;
- gives a case-specific reason;
- asks focused questions only when needed.

Should not happen:

- keyword matching;
- stale copied roster.

## Review Whether A Completion Report Is Credible

Copy:

```text
Mira，帮我复盘这个完成报告是否可信：<paste report>
```

Expected Mira behavior:

- separates claims from evidence;
- may name a Quinn-style verifier candidate;
- marks `not-run` and missing evidence.

Should not happen:

- accepts "done" as proof;
- creates a release-ready claim without evidence.

## Handle A Composite Deliverable

Copy:

```text
Mira，帮我调研、写报告，并制作成可交付文件。先不要执行，先给 staged judgement 和 Task Package。
```

Expected Mira behavior:

- identifies content deliverables and final deliverables;
- names stage owner candidates;
- says Simple Pal Mode / staged package is the active path.

Should not happen:

- Deep Conductor claimed active;
- one topic Pal owns all stages.

## Directly Call A Specialist Pal

Copy:

```text
/pal Atlas 帮我把这个修改做成执行任务包：<your task>
```

Expected behavior:

- Atlas is the speaking Pal;
- Mira does not take the task back;
- Atlas still applies composite-stage judgement if needed.

Should not happen:

- Mira answers the Atlas body;
- direct call starts an independent agent process.

## Ask Mira Why This Assignment

Copy:

```text
Mira，解释一下为什么你建议这个 Pal 或这些阶段候选。
```

Expected Mira behavior:

- explains from goal, deliverables, risk, evidence, and current registry;
- reminds that candidates are not fixed routes.

Should not happen:

- static Pal routing table;
- "because the keyword matched".
