# v0.6 Session Transcript Template

Status: blank template.

Use this template after running one scenario in a real conversation.

```yaml
session_id:
scenario_id:
scenario_title:
runtime_surface: codex | claude-code | other
runtime_validation_level: no-code-protocol | host-runtime | mixed
date:
operator:
user_input: |
  <paste exact user input>
assistant_transcript: |
  <paste complete assistant response or link to transcript>
follow_up_inputs:
  - input:
    reason:

observed_mira_decision:
  present: unknown
  summary:
  evidence_quote:

observed_palsmith_action:
  present: unknown
  summary:
  evidence_quote:

selected_team:
  team_id:
  evidence_quote:

consulted_pals:
  - pal_id:
    reason:
    evidence_quote:

rejected_pals:
  - pal_id:
    reason:
    evidence_quote:

workflow_contract_present:
  status: unknown
  evidence_quote:

closure_gate_present:
  status: unknown
  evidence_quote:

faye_boundary_respected:
  status: unknown
  evidence_quote:

naming_rule_respected:
  status: unknown
  evidence_quote:

verifier_handled:
  status: unknown
  verifier:
  evidence_quote:

team_asset_preflight_present:
  status: unknown
  evidence_quote:

pal_asset_preflight_present:
  status: unknown
  evidence_quote:

runtime_actions_claimed:
  status: none | claimed_with_evidence | claimed_without_evidence
  evidence_quote:

not_run_or_blocked_items:
  - item:
    reason:

pass_fail: not-scored
score_total:
notes:
```

## Scoring Notes

- Use `unknown` only before scoring.
- Use `not-run` when the runtime did not execute a required external action.
- Use `blocked` when user input, source data, permissions, or runtime capability
  are missing.
- Do not mark a scenario `pass` if the transcript only matches the expected
  answer because the operator manually corrected it.
