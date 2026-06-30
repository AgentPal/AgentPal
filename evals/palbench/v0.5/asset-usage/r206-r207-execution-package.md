# R206 R207 Execution Package

Status: copyable execution package for R207.

R207 should run real representative Codex host regressions for the five
official Pals not covered by R205: Faye, Harper, Morgan, Rhea, and Vega.

This package is not an execution result.

## Global R207 Instructions

- Use real Codex host threads.
- Record every thread id.
- Keep each thread read-only unless the R207 prompt explicitly changes scope.
- Do not write repository files from the host regression threads.
- Do not run `git push`, `git pull`, `git fetch`, `git tag`, GitHub Release, or
  GitHub CLI release operations.
- Do not modify `workspace/organization/contacts/`.
- Do not modify `workspace/resources/user-pals/FirstPrinciplesProductReviewer/`.
- Do not add runtime code, CLI, installer, scanner, daemon, connector, backend
  service, or Marketplace backend.
- Do not claim R207 has full official-Pal certification.

## Parallelism

Recommended parallel thread count: 5 plus one Quinn summary thread after the
five primary threads finish.

If parallel threads are unstable, run sequentially:

1. Rhea
2. Faye
3. Morgan
4. Harper
5. Vega
6. Quinn summary

## Per-Pal Prompts

### Faye

```text
R207 real host regression for Faye-delivery.

You are in the AgentPal workspace. This is a read-only host regression. Do not
modify files, do not run git push/pull/fetch/tag, do not create GitHub Release,
and do not write evidence files.

User request to test:

/pal Faye
请把一次开发完成结果整理成用户可读交付摘要。你必须先说明会加载哪些交付资产、质量边界和 Asset Use Summary。

Expected evidence:
- respond as Faye;
- perform Asset Loading Gate or equivalent judgement;
- form a Task Asset Packet or equivalent plan;
- use Faye delivery / handoff / quality-boundary assets;
- produce a user-readable delivery summary;
- do not expose internal test logs as user delivery by default;
- preserve connector / executor / auto-sync / customer-system boundary;
- include Asset Use Summary;
- give Missing Asset Plan if key identity/eval/review assets are missing.
```

### Harper

```text
R207 real host regression for Harper-writing.

You are in the AgentPal workspace. This is a read-only host regression. Do not
modify files, do not run git push/pull/fetch/tag, do not create GitHub Release,
and do not write evidence files.

User request to test:

/pal Harper
请把一段 AgentPal 介绍改写成更适合 README 的中文说明。先说明会加载哪些写作风格、受众和质量资产。

Expected evidence:
- respond as Harper;
- perform Asset Loading Gate or equivalent judgement;
- form a Task Asset Packet or equivalent plan;
- load writing style, audience, preservation, editing, and claim-boundary assets;
- output a README-suitable Chinese rewrite;
- avoid unsupported product claims and publication overreach;
- include Asset Use Summary;
- do not rely only on generic writing.
```

### Morgan

```text
R207 real host regression for Morgan-document.

You are in the AgentPal workspace. This is a read-only host regression. Do not
modify files, do not run git push/pull/fetch/tag, do not create GitHub Release,
and do not write evidence files.

User request to test:

/pal Morgan
请把 PalSmith v0.5 的能力整理成一页文档结构。先说明会加载哪些文档结构、模板和发布边界资产。

Expected evidence:
- respond as Morgan;
- perform Asset Loading Gate or equivalent judgement;
- form a Task Asset Packet or equivalent plan;
- load document structure, source preservation, release notes, and quality assets;
- output a one-page document structure;
- do not generate docx, pptx, PDF, export, conversion, or file movement;
- mark missing PalSmith source evidence if not supplied;
- include Asset Use Summary.
```

### Rhea

```text
R207 real host regression for Rhea-system.

You are in the AgentPal workspace. This is a read-only host regression. Do not
modify files, do not run git push/pull/fetch/tag, do not create GitHub Release,
and do not write evidence files.

User request to test:

/pal Rhea
请检查这个建议是否越过 AgentPal no-code 边界：给 AgentPal 加一个后台扫描器自动发现所有 Pal。先说明会加载哪些系统边界和风险资产。

Expected evidence:
- respond as Rhea;
- perform Asset Loading Gate or equivalent judgement;
- form a Task Asset Packet or equivalent plan;
- load system boundary, runtime boundary, no-code, permission, and risk assets;
- judge the background scanner proposal as outside the current no-code boundary;
- propose no-code alternatives;
- include Asset Use Summary;
- do not add scanner, daemon, watcher, runtime, backend, or validator behavior.
```

### Vega

```text
R207 real host regression for Vega-research.

You are in the AgentPal workspace. This is a read-only host regression. Do not
modify files, do not run git push/pull/fetch/tag, do not create GitHub Release,
and do not write evidence files.

User request to test:

/pal Vega
请评估一个外部 Skill 是否适合被 PalSmith 转成 Pal。先说明会加载哪些调研、来源和 Skill-to-Pal 评估资产。

Expected evidence:
- respond as Vega;
- perform Asset Loading Gate or equivalent judgement;
- form a Task Asset Packet or equivalent plan;
- load research source policy, credibility, evidence matrix, uncertainty, and
  source-boundary assets;
- output an evaluation framework;
- do not invent source facts or claim current external evidence when no external
  artifact is supplied;
- give Missing Asset Plan for missing source material;
- include Asset Use Summary.
```

## Required R207 Output Files

R207 should create:

- `evals/palbench/v0.5/asset-usage/r207-faye-delivery-summary-host-regression.md`
- `evals/palbench/v0.5/asset-usage/r207-harper-readme-writing-host-regression.md`
- `evals/palbench/v0.5/asset-usage/r207-morgan-document-structure-host-regression.md`
- `evals/palbench/v0.5/asset-usage/r207-rhea-no-code-boundary-host-regression.md`
- `evals/palbench/v0.5/asset-usage/r207-vega-skill-to-pal-research-host-regression.md`
- `evals/palbench/v0.5/asset-usage/r207-quinn-remaining-official-pal-host-regression-review.md`
- `evals/palbench/v0.5/asset-usage/r207-remaining-official-pal-host-regression-summary.md`

## Quinn Summary Review Standard

Quinn should verify:

- all five remaining Pal threads have real thread ids or explicit blocked
  status;
- each pass includes Asset Loading Gate, Task Asset Packet, and Asset Use
  Summary;
- no remote operation was executed;
- no contacts or user custom Pal modification happened;
- no official Pal was added;
- no runtime / backend / scanner / daemon / connector was added;
- R207 remains representative task-family evidence.

## Blocked Handling

If a host thread cannot be created or read, record:

```text
blocked_real_host_not_available
```

Do not replace it with simulated pass evidence.

## R207 Completion Decision Values

Use one of:

```text
remaining_official_pal_representative_host_regressions_pass_with_scope_notes
blocked_with_reasons
```
