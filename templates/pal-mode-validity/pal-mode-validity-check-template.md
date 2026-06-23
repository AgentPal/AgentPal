# Pal Mode Validity Check

active_pal: REPLACE_WITH_ACTIVE_PAL
task_type: REPLACE_WITH_TASK_TYPE
is_specialist_task: true_or_false

## Minimum Proof

- active_pal identified:
- identity / boundary used:
- response_fingerprint_used:
- output_contract_used:
- assets_used:
- fallback_method:
- codex_generic_answer: true_or_false

## Validity Decision

valid_pal_mode: true_or_false

## Fail If

- only speaker name changed
- no Pal asset or fallback method used
- output does not match the Pal response fingerprint
- output does not follow the output contract
- Mira provides the owner Pal answer herself after selecting an owner
- missing asset is falsely claimed as used

## Notes

REPLACE_WITH_NOTES

