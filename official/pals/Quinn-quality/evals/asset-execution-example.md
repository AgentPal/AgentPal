# Asset Execution Example

## Status

phase: phase_2_task_asset_packet_example
verified_executable_pal: false
full_asset_usage_regression: not_yet

This example shows how Quinn should review a completion report. It is not a
completed QA run and not representative host acceptance evidence.

## Example Task

User says:

```text
你看一下这个完成报告能不能算通过。
```

## Asset Loading Gate

target_pal: Quinn

task_type: quality / evidence review

required_assets:

- `official/pals/Quinn-quality/PAL.md`
- `official/pals/Quinn-quality/pal.json`
- `official/pals/Quinn-quality/SKILL.md`
- `official/pals/Quinn-quality/core/output-contract.md`
- `official/pals/Quinn-quality/skills/evidence-review-skill.md`
- `official/pals/Quinn-quality/knowledge/not-run-partial-blocked-knowledge.md`
- `core/pal-asset-execution-contract.md`
- `core/asset-loading-gate.md`
- the completion report and raw evidence supplied for review

go_no_go_decision: `go_with_limited_fallback` if raw evidence is missing

reasoning_summary: Quinn may review the report, but a completion report is not
evidence by itself. Quinn must separate claims, evidence, not-run items,
blocked checks, and residual risk.

## Task Asset Packet

task_id: quinn-completion-report-review-example

target_pal: Quinn

task_type: QA review

user_goal: decide whether a completion report can be accepted as pass

execution_mode: no-code evidence review

required_identity_assets:

- Quinn root identity

required_knowledge_assets:

- not-run / partial / blocked knowledge

required_skill_assets:

- evidence review skill

required_workflows:

- quality review sequence or fallback method

required_runtime_policy:

- Quinn reviews evidence; Runtime executes checks

required_memory_scope:

- no private evidence stored unless user approves

required_eval_assets:

- acceptance criteria, Definition of Done, or target regression gate

optional_tools:

- read-only checks if the user asks Quinn to request Runtime evidence

loaded_assets:

- Quinn root entry assets
- output contract
- evidence review skill
- not-run / partial / blocked knowledge
- Pal Asset Execution Contract
- Asset Loading Gate

missing_assets:

- raw command output, changed file list, or artifact evidence if not supplied

allowed_tool_calls:

- none in report-only review; read-only evidence checks require scoped user
  authorization

blocked_tool_calls:

- declaring pass from unsupported claims
- running tests as Quinn
- publishing or release actions

go_no_go_decision: `go_with_limited_fallback`

## Expected Execution

Quinn should output:

- decision: pass, pass_with_notes, partial, blocked, or fail;
- claim-to-evidence table;
- not-run items;
- missing proof;
- risk severity;
- required next action.

If only a summary report exists, Quinn should usually mark acceptance as
`blocked_missing_evidence` or `partial`, not pass.

## Tools / Runtime Boundary

Test runners, shell commands, link checkers, JSON parsers, screenshots, browser
tools, and release tools are execution tools. Quinn can request or review their
outputs, but they are not Quinn assets and Quinn must not claim they ran unless
current Runtime evidence exists.

## Asset Use Summary

task_id: quinn-completion-report-review-example

target_pal: Quinn

used_identity_assets:

- `official/pals/Quinn-quality/PAL.md`

used_knowledge_assets:

- `official/pals/Quinn-quality/knowledge/not-run-partial-blocked-knowledge.md`

used_skill_assets:

- `official/pals/Quinn-quality/skills/evidence-review-skill.md`

used_eval_assets:

- target acceptance criteria if supplied

tools_called: none in this example

quality_gate_result: example only; real review requires actual report and
evidence

next_asset_improvement: add a real Quinn evidence-review host regression in
Phase 3.

## Missing Asset Plan

missing_asset: raw evidence behind the completion report

why_needed: Quinn cannot accept pass claims without command output, changed
files, artifacts, or manual evidence that maps to acceptance criteria.

temporary_fallback_allowed: yes, report-only review with lower confidence.

recommended_asset_path: completion evidence packet with claim, command output,
changed paths, artifacts, not-run items, and risk notes.

priority: high for release, QA, and user-facing changes.

## Lightweight Path

If the user asks "Quinn 是做什么的？", lightweight path is enough. Reviewing a
completion report, release readiness, or test evidence is not lightweight.

## What This Example Does Not Claim

- This does not mark Quinn as fully verified.
- This is not a full migration.
- This is not a real QA pass.
- This is not a runtime, CI, scanner, validator, or release implementation.
