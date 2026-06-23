# Asset Usage Proof

active_pal: REPLACE_WITH_ACTIVE_PAL
task_type: REPLACE_WITH_TASK_TYPE
owner_pal: REPLACE_WITH_OWNER_PAL

## Assets

work_method_statement: REPLACE_WITH_LIGHT_VISIBLE_METHOD_LINE

assets_checked:
- REPLACE_WITH_CHECKED_ASSET

assets_used:
- REPLACE_WITH_USED_ASSET_OR_FALLBACK

output_contract_used: REPLACE_WITH_OUTPUT_CONTRACT

## Gaps And Fallback

knowledge_gap: REPLACE_WITH_GAP_OR_NONE
fallback_method: REPLACE_WITH_FALLBACK_OR_NONE

## Learning

repeated_task_family: REPLACE_WITH_TASK_FAMILY
candidate_trigger: count >= 3

## Confidence

confidence: high | medium | low

## Codex Generic Answer Check

codex_generic_answer: true_or_false

If `codex_generic_answer: true`, do not label the response as a valid Pal answer.

If the user explicitly requested Codex generic answer, do not use a Pal prefix.

