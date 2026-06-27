# Multi-Pal Context Packet Template

from_pal: Mira
to_pal: REPLACE_WITH_OWNER_PAL
mode: handoff
owner_pal: REPLACE_WITH_OWNER_PAL
user_visible_handoff: true
active_speaker_after_handoff: REPLACE_WITH_OWNER_PAL
required_response_fingerprint: response-fingerprints/REPLACE_WITH_OWNER_PAL.md
required_output_contract: official/pals/REPLACE_WITH_OWNER_PAL_DIR/core/output-contract.md
minimum_asset_loading:
  - owner Pal identity
  - owner Pal output contract
  - owner Pal response fingerprint
  - at least one owner Pal asset or fallback method
allow_codex_generic_answer: false
fallback_if_no_asset: true
asset_usage_proof_required: true_for_owner_and_any_substantive_consultant

## User Goal

REPLACE_WITH_USER_GOAL

## Mira Boundary

Mira chooses the owner Pal and stops.

The owner Pal decides consultant Pal(s), reviewer Pal(s), execution layer, stage order, fallback, assets, evidence, and final integration.

## Task Family

REPLACE_WITH_TASK_FAMILY

## Privacy Policy

Share minimum necessary context. Do not include secrets, credentials, private customer data, raw private logs, unrelated personal memory, or full project context unless explicitly approved and necessary.

## Expected Output

- owner Pal takes over
- owner Pal chooses consultants/reviewers if needed
- owner Pal uses its Response Fingerprint and Output Contract
- owner Pal includes Asset Usage Proof for complex or audited work
- consultants answer with their own prefixes
- owner Pal integrates
- Mira returns only if requested or handed back

