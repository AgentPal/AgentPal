# Response Language Policy Eval

## Purpose

Verify that AgentPal reports follow the user's latest instruction language instead of defaulting to English.

## Current Status

Active regression check for AgentPal `v0.1.0-rc.1`.

## Scope

This eval applies to Simple Pal Mode reports, especially completion reports, release gate reports, verification reports, and blocker reports.

## Cases

### Chinese Release Gate Request

User request:

```text
你是 AgentPal 发布门禁线程。请检查 release gate，并输出完成报告。
```

Expected:

- Quinn may answer with `Quinn：`.
- The natural-language report body is Chinese.
- Technical identifiers remain as-is, including `git status`, commit hashes, `v0.1.0-rc.1`, file paths, filenames, JSON keys, commands, and code blocks.
- The report does not translate quoted source text unless the user asks for translation.

Failure:

- Quinn writes the completion report primarily in English without an explicit user request for English.

### English Request

User request:

```text
Please run a release gate and summarize the result.
```

Expected:

- Quinn may answer in English.
- Technical identifiers remain as-is.

### Explicit Language Override

User request:

```text
请检查 release gate，用英文回复。
```

Expected:

- Quinn may answer in English because the user explicitly requested English.

### Chinese Request With Git Commands

User request:

```text
请检查 git status 和 git diff --check，然后用中文报告结果。
```

Expected:

- The report body is Chinese.
- `git status` and `git diff --check` remain untranslated.

## Related Rules

- [Runtime Response Gate](../../orchestration/runtime-response-gate.md)
- [Pal Mode Validity Protocol](../../orchestration/pal-mode-validity-protocol.md)
- [Quinn Output Contract](../../pals/Quinn-quality/core/output-contract.md)
