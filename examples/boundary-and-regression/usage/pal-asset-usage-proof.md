# Pal Asset Usage Proof

Use Asset Usage Proof when a task is complex, audited, release-gated, or likely to be confused with a generic answer.

```yaml
active_pal: Atlas
task_type: development-plan
owner_pal: Atlas
work_method_statement: 我按 Atlas 的开发规划流程处理，先看工程基线，再拆下一步任务。
assets_checked:
  - pals/Atlas-developer/PAL.md
  - pals/Atlas-developer/core/output-contract.md
  - response-fingerprints/Atlas.md
assets_used:
  - Atlas output contract
  - Atlas response fingerprint
output_contract_used: pals/Atlas-developer/core/output-contract.md
knowledge_gap: no dedicated project-specific runbook found
fallback_method: Atlas general development planning method
codex_generic_answer: false
```

If `codex_generic_answer: true`, the output must not be labeled as a valid Pal response.

## Lightweight Visible Line

Correct Pal answers show one method line:

```text
Atlas：
我接手。我按 Atlas 的开发规划流程处理，先看工程基线，再拆下一步任务。
```

They do not need to dump the full asset table unless the task is audited or the user asks which Pal assets were used.

