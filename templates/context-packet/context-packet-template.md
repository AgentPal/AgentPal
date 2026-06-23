# Context Packet Template

from_pal: Mira
to_pal: REPLACE_WITH_TARGET_PAL
mode: handoff
user_goal: REPLACE_WITH_USER_GOAL
task_type: REPLACE_WITH_TASK_TYPE
active_project: REPLACE_WITH_CURRENT_PROJECT_OR_NONE
constraints:
- REPLACE_WITH_CONSTRAINT
user_visible_handoff: true
required_response_fingerprint: response-fingerprints/REPLACE_WITH_TARGET_PAL.md
required_output_contract: pals/REPLACE_WITH_TARGET_PAL_DIR/core/output-contract.md
minimum_asset_loading:
  - PAL.md or pal.json identity
  - output contract
  - response fingerprint
  - at least one Skill / Knowledge / Runbook / Workflow / learning rule / fallback method
allow_codex_generic_answer: false
fallback_if_no_asset: true
asset_usage_proof_required: true_for_complex_or_audited_tasks

## Active Pal

After this packet, `to_pal` becomes the active speaker.

Mira routes and stops. The target Pal handles its own domain judgment, fallback, execution-layer coordination, reporting, and learning.

## Optional Specialist Expansion

The active specialist Pal may add these fields after taking over:

- asset_loading_level
- known_assets_used
- response_fingerprint_used
- output_contract_used
- asset_usage_proof
- knowledge_gap
- fallback_allowed
- fallback_method
- repeated_task_record
- formal_skill_trigger
- formal_skill_target
- execution_layer
- evidence_required
- consultant_pals
- reviewer_pals

## Privacy Policy

Do not include secrets, credentials, unrelated memory, or full project context unless explicitly approved and necessary.

## Example

```text
from_pal: Mira
to_pal: Rhea
mode: handoff
user_goal: 检查系统启动项都有哪些
task_type: system-startup-audit
active_project: none
constraints:
  - read-only first
  - do not modify startup items without user confirmation
user_visible_handoff: true
required_response_fingerprint: response-fingerprints/Rhea.md
required_output_contract: pals/Rhea-system/core/output-contract.md
minimum_asset_loading:
  - pals/Rhea-system/PAL.md
  - pals/Rhea-system/core/output-contract.md
  - response-fingerprints/Rhea.md
  - Rhea asset or fallback method
allow_codex_generic_answer: false
fallback_if_no_asset: true
asset_usage_proof_required: true
```

