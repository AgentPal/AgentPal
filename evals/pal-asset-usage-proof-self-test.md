# Pal Asset Usage Proof Self-Test

## Purpose

Verify complex specialist work includes Asset Usage Proof.

## Required proof fields

- `active_pal`
- `assets_checked`
- `assets_used`
- `output_contract_used`
- `knowledge_gap`
- `fallback_method`
- `codex_generic_answer`
- visible `work_method_statement`

## Pass

The response can point to actual Pal assets read or to an explicit fallback method.

The user-visible Pal answer includes one short work-method statement, not a large asset dump.

## Fail

The response claims a Skill, Knowledge Card, Runbook, Workflow, or Output Contract was used when it was not.

The response has no work-method statement and cannot be distinguished from a generic Codex answer.

