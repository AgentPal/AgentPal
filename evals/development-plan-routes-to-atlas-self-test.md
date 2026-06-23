# Development Plan AI Judgement Self-Test

This self-test is a non-binding example. It must not be used as a keyword routing rule.

## Purpose

Verify that a development-plan-like request does not cause hard-coded semantic routing, and that Mira does not write the owned work body after choosing an owner.

## Test Input

```text
帮我制定一个开发计划
```

## Expected Behavior

Mira must:

- use AI routing judgement case-by-case
- explain the owner choice with a current-context reason
- keep route-only output to max 2 short sentences
- avoid writing the development plan herself
- ensure the owner Pal answers immediately after handoff

One valid response shape:

```text
Mira：
我判断这次更适合由 Atlas 接手，因为当前请求需要工程基线、开发阶段和验收边界。我请 Atlas 接手。

Atlas：
我接手。我按 Atlas 的开发规划流程处理，先看工程基线，再拆下一步任务。
```

This example does not mean the phrase "开发计划" always selects Atlas.

## Fail Signs

- Mira writes the development plan herself.
- Mira gives engineering architecture advice before handoff.
- Mira outputs more than 2 short sentences.
- Mira outputs a numbered or bullet development plan.
- Owner Pal does not become active speaker.
- Owner Pal does not answer immediately after Mira.
- Owner Pal gives a generic answer without Response Fingerprint, Output Contract, or asset/fallback proof.
- Owner Pal has no work-method statement.
- The response says the owner was selected because a keyword always maps to that Pal.

